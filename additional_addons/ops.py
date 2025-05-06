import time
import bpy.utils.previews
import bmesh.types
import bpy
import numpy
from mathutils import Vector
import bmesh
from .utils import (
    from_mesh_get_kd_true,
    from_data_get_material,
    get_vg_index,
    pop_prop,
    get_bm,
)

previews_icons = bpy.utils.previews.new()  # 用于存所有的缩略图


def load_images_to_icons(images_list: "list[bpy.types.Image]"):
    global previews_icons
    previews_icons.clear()
    for image in images_list:
        name = image.name
        if name in previews_icons:
            previews_icons.pop(name)
        icon = previews_icons.new(name)
        icon.icon_size = image.size
        icon.icon_pixels_float = image.pixels


images = []

textures_cache = {}


class UVKeying(bpy.types.Operator):
    bl_idname = "uv.keying_uv"
    bl_label = "Keying"

    @classmethod
    def poll(cls, context):
        return (
            context.object
            and context.object.type == "MESH"
            and context.object.mode == "EDIT"
        )

    image_index: bpy.props.IntProperty(name="Image Index", default=0)

    def draw(self, context):
        column = self.layout.column(align=True)
        column.operator_context = "EXEC_DEFAULT"
        for i, image in enumerate(images):
            # row.template_icon(icon_value=previews_icons.get(image.name).icon_id, scale=2)
            column.operator(UVKeying.bl_idname, text=image.name).image_index = i

    def invoke(self, context, event):
        global images
        data = context.object.data
        images = from_data_get_material(data)
        if len(images) == 0:
            self.report({"ERROR"}, "未找到图像")
        if len(images) == 1:
            self.image_index = 0
            return self.execute(context)
        # load_images_to_icons(images)
        context.window_manager.popup_menu(
            self.__class__.draw, title="选择UV图", icon="INFO"
        )
        return {"FINISHED"}

    def execute(self, context):
        data = context.object.data

        active_ui_layout = data.uv_layers.active

        if active_ui_layout is None:
            self.report({"ERROR"}, "未找到活动UV")
            return {"FINISHED"}

        images = from_data_get_material(data)
        if len(images) == 0:
            self.report({"ERROR"}, "未找到图像")
            return {"FINISHED"}

        # w 2 h 3
        """
        Buffer(UBYTE, [
        [[162, 137, 137, 255], [158, 133, 133, 255]], 
        [[192, 133, 133, 255], [133, 74, 74, 255]],
        [[230, 137, 137, 255], [163, 70, 70, 255]]
         ]
         )
        """
        image: bpy.types.Image = images[self.image_index]
        print("image", image.name, image.size[:])
        width, height = image.size
        st = time.time()
        # texture = numpy.array(gpu.texture.from_image(image).read())
        if image.name in textures_cache:
            texture = textures_cache[image.name]
        else:
            texture = numpy.array(image.pixels, dtype=numpy.float64)
            texture = texture.reshape(height, width, image.channels)
            textures_cache[image.name] = texture
        print("time", time.time() - st)

        import bmesh

        bm = bmesh.from_edit_mesh(data)

        layout = bm.loops.layers.uv.get(active_ui_layout.name, None)
        if layout is None:
            self.report({"ERROR"}, "在Bmesh中未找到活动UV")
            return {"FINISHED"}

        nwh = numpy.array([width, height], dtype=numpy.float64)
        wh = numpy.array([1, 1], dtype=numpy.float64) / nwh
        # print(texture)
        print("wx hy", width, height, wh)

        remove_vertices = set()
        index_list = set()
        # return {"FINISHED"}

        zero = numpy.array([0.0, 0.0, 0.0])
        for face in bm.faces:
            for loop in face.loops:
                vert = loop.vert
                if (
                    vert.select
                    and vert not in remove_vertices
                    and vert.hide is not True
                    and vert.index not in index_list
                ):
                    uv = loop[layout].uv  # Vector((0,0))
                    # u, v = uv[:]

                    # # # 确保坐标在图像范围内
                    # x = int(u // wx)
                    # y = int(v // hy)
                    # px = max(0, min(x, width - 1))
                    # py = max(0, min(y, height - 1))
                    nuv = numpy.array(uv, dtype=numpy.float64)
                    xy = numpy.floor(nuv // wh)
                    px = max(0, min(int(xy[0]), width - 1))
                    py = max(0, min(int(xy[1]), height - 1))

                    pixel = texture[py][px]
                    # print(pixel, "np", vert.index, nuv, "wh", wh, xy, px, py)

                    if pixel.size == 4:
                        pixel = pixel[:3]

                    # print(vert.index, pixel, "\t pixel", xy, px, py, uv, wh, numpy.array(uv, dtype=numpy.float32) // wh)
                    if (pixel == zero).all():
                        remove_vertices.add(vert)

                    index_list.add(vert.index)

        rl = len(remove_vertices)
        bmesh.ops.delete(bm, geom=list(remove_vertices), context="VERTS")
        bmesh.update_edit_mesh(data)

        self.report({"INFO"}, f"{rl} 个顶点被删除")

        return {"FINISHED"}


class ButtonRemoveAndScaleMesh(bpy.types.Operator):
    bl_idname = "mesh.remove_and_scale_mesh"
    bl_label = "删除并缩放"
    bl_description = "编辑模式下，删除所选网格并在所选质心处新建三角面并缩放到最小"
    bl_options = {"REGISTER", "UNDO"}

    scale: bpy.props.FloatProperty(name="缩放", default=0.00001)  # type: ignore

    @classmethod
    def poll(cls, context):
        return (
            context.object
            and context.object.type == "MESH"
            and context.object.mode == "EDIT"
        )

    def execute(self, context):

        scale = self.scale

        for obj in context.selected_objects:
            bm = bmesh.from_edit_mesh(obj.data)

            co = Vector()
            count = 0
            for vert in bm.verts:
                if vert.select:
                    co += vert.co
                    count += 1

            if count != 0:

                faces = [face for face in bm.faces if face.select]
                bmesh.ops.delete(bm, geom=faces, context="FACES")

                co /= count

                verts = []
                for i in range(3):
                    verts.append(bm.verts.new(co))
                bm.verts.ensure_lookup_table()
                face = bm.faces.new(verts)
                face.select = True

                bm.faces.ensure_lookup_table()

            bmesh.update_edit_mesh(obj.data)

            obj.data.update()
        if bpy.context.scene.AQ_Props.Auto_BacktoObject:
            bpy.ops.object.mode_set(mode="OBJECT")
        return {"FINISHED"}


class ButtonMarkContrastVert(bpy.types.Operator):
    bl_idname = "mesh.a7_compare_and_contrast_vert_to_vg"
    bl_label = "对比两个物体到顶点组"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "对比两个物体到顶点组，使两个物体相交的顶点组权重相同"

    thresholds: bpy.props.FloatProperty(name="阈值", default=0.001)
    vert_groups_name: bpy.props.StringProperty(
        name="顶点组名称", default="Contrast Vert"
    )

    kd_a = None
    # kd_b = None
    obj_a = None
    obj_b = None

    @classmethod
    def poll(cls, context):
        types = [obj.type for obj in context.selected_objects]
        return types == ["MESH", "MESH"]

    def invoke(self, context, event):
        obj_a, obj_b = context.selected_objects
        self.kd_a = from_mesh_get_kd_true(context, obj_a)
        # self.kd_b = from_data_get_material(self.obj_b)
        bpy.ops.ed.undo_push(message="Push Undo")
        self.mode = context.mode
        return self.execute(context)

    def execute(self, context):
        contrast_vert_dict = {}  # {物体A顶点索引,物体B顶点索引}
        obj_a, obj_b = context.selected_objects
        b_mat = obj_b.matrix_world
        for vert in obj_b.data.vertices:
            co = b_mat @ vert.co
            f_co, index, distance = self.kd_a.find(co)
            if distance < self.thresholds:
                contrast_vert_dict[index] = vert.index
        print("contrast_vert_dict", contrast_vert_dict)
        """
        bpy.context.object.data.vertices[0].groups[0].group
        bpy.context.object.vertex_groups['Group'].index
        """
        a_vg_index = get_vg_index(self.vert_groups_name, obj_a, True)
        b_vg_index = get_vg_index(self.vert_groups_name, obj_b, True)

        with pop_prop():
            obj_a.vertex_groups.active_index = a_vg_index
            obj_b.vertex_groups.active_index = b_vg_index

            ba = get_bm(context, obj_a.data)
            bb = get_bm(context, obj_b.data)

            al = list(contrast_vert_dict.keys())
            bl = list(contrast_vert_dict.values())

            def assign_vg(obj: bpy.types.Object, bm: bmesh.types.BMesh, vert_list: []):
                for v in bm.verts:
                    v.select = v.index in vert_list
                if context.mode == "EDIT_MESH":
                    bmesh.update_edit_mesh(obj.data)
                else:
                    bm.to_mesh(obj.data)
                context.view_layer.objects.active = obj
                obj.data.update()
                obj.update_tag()
                bpy.ops.object.vertex_group_assign()

            if context.mode != "EDIT_MODE":
                bpy.ops.object.mode_set(mode="EDIT")
            assign_vg(obj_a, ba, al)
            assign_vg(obj_b, bb, bl)
            if self.mode != "EDIT_MODE" and context.mode == "EDIT_MODE":
                bpy.ops.object.mode_set(mode="EDIT", toggle=True)

        obj_a.data.update()
        obj_b.data.update()
        return {"FINISHED"}


def register():
    global previews_icons
    bpy.utils.register_class(UVKeying)
    bpy.utils.register_class(ButtonRemoveAndScaleMesh)
    bpy.utils.register_class(ButtonMarkContrastVert)


def unregister():
    bpy.utils.unregister_class(UVKeying)
    bpy.utils.unregister_class(ButtonRemoveAndScaleMesh)
    bpy.utils.unregister_class(ButtonMarkContrastVert)

    previews_icons.clear()
