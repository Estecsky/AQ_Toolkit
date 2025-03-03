import bpy
import bmesh


class ButtonRemoveEmpty(bpy.types.Operator):
    bl_idname = "panel_ops.remove_empty"
    bl_label = "remove_empty_vg"
    bl_description = "移除选中模型的空顶点组"

    def execute(self, context):
        obj = bpy.context.object
        if obj.type != "MESH":
            self.report({"ERROR"}, "所选物体不是网格")
            return {"CANCELLED"}
        try:
            vertex_groups = obj.vertex_groups
            groups = {r: None for r in range(len(vertex_groups))}

            for vert in obj.data.vertices:
                for vg in vert.groups:
                    i = vg.group
                    if i in groups:
                        del groups[i]

            lis = [k for k in groups]
            lis.sort(reverse=True)
            for i in lis:
                print(f"{vertex_groups[i].name} removed")
                vertex_groups.remove(vertex_groups[i])
        except Exception as e:
            print(e)
        return {"FINISHED"}


class ButtonRemoveUnusedBones(bpy.types.Operator):
    bl_label = "remove_unused_bones"
    bl_description = "根据模型的骨架修改器移除骨架中没有对应顶点组的骨骼"
    bl_idname = "misremove_unused.ops_bones"

    def execute(self, context):
        obj = bpy.context.object
        vertex_groups = obj.vertex_groups
        skeleton = obj.find_armature()
        if obj.type != "MESH":
            self.report({"ERROR"}, "所选物体不是网格,需要选择一个网格")
            return {"FINISHED"}
        if skeleton is None:
            self.report({"ERROR"}, "选中物体未找到正确的骨架修改器")
            return {"FINISHED"}
        if obj.type == "MESH" and len(obj.vertex_groups) > 0:
            bones_to_remove = []
            bones = skeleton.data.bones
            skeleton_data = skeleton.data
            vg_lst = []
            for vg in vertex_groups:
                vg_lst.append(vg.name)
            for bone in bones:
                bone_name = bone.name
                exists_in_vg = False

                if bone_name in vg_lst:
                    exists_in_vg = True

                if not exists_in_vg:
                    bones_to_remove.append(bone_name)

            # 删除不存在对应顶点组的骨骼
            bpy.ops.object.mode_set(mode="OBJECT")  # 确保在对象模式下
            bpy.ops.object.select_all(action="DESELECT")
            skeleton.select_set(True)
            bpy.context.view_layer.objects.active = skeleton
            bpy.ops.object.mode_set(mode="EDIT")  # 进入编辑模式以删除骨骼
            # print(bones_to_remove)
            if bones_to_remove:

                for bone_name in bones_to_remove:

                    edit_bone = skeleton_data.edit_bones.get(bone_name)

                    skeleton_data.edit_bones.remove(edit_bone)
                    self.report({"INFO"}, f"骨骼 '{bone_name}' 已移除.")

            else:
                self.report({"WARNING"}, "没有找到任何未使用骨骼，请先移除空顶点组")

            # 更新物体的所有顶点组
            # obj.vertex_groups.clear()
            # for vg in vertex_groups:
            #     obj.vertex_groups.new(name=vg.name)

            return {"FINISHED"}


class ButtonSplitMeshAlongUVs(bpy.types.Operator):
    bl_idname = "meshops.split_mesh_along_uvs"
    bl_label = "Along UV Islands"
    bl_description = (
        "Splits the edges along UV Islands to prevent UVs from joining on export."
    )
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return (
            context.active_object is not None and context.active_object.type == "MESH"
        )

    def execute(self, context):
        try:
            self.report({"INFO"}, f"Mesh(es) successfully split along UVs!")
            split_faces_by_edge_seams(context.active_object)
        except Exception as err:
            print(f"{err}")
            pass
        return {"FINISHED"}


class ButtonDeleteLooseGeometry(bpy.types.Operator):
    bl_idname = "meshops.delete_loose_edges_and_verts"
    bl_label = "Delete Loose Verts & Edges"
    bl_description = "Deletes Loose any loose Vertices & Edges on the mesh."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return (
            context.active_object is not None and context.active_object.type == "MESH"
        )

    def execute(self, context):
        try:
            mesh = context.active_object.data
            init_verts = len(mesh.vertices)
            init_edges = len(mesh.edges)
            init_faces = len(mesh.polygons)
            utils_set_mode("EDIT")
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.mesh.delete_loose(use_verts=True, use_edges=True, use_faces=False)
            utils_set_mode("OBJECT")
            removed_verts = init_verts - len(mesh.vertices)
            removed_edges = init_edges - len(mesh.edges)
            removed_faces = init_faces - len(mesh.polygons)
            self.report(
                {"INFO"},
                f"Removed: {removed_verts} vertices, {removed_edges} edges, {removed_faces} faces",
            )
        except Exception as err:
            print(f"{err}")
            pass
        return {"FINISHED"}


class ButtonSelect0WeightVertices(bpy.types.Operator):
    bl_idname = "meshops.select_0_weight_vertices"
    bl_label = "Select Zero Weight Vertices"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Selects all vertices on the active mesh that have no weights."

    @classmethod
    def poll(cls, context):
        return (
            context.active_object is not None and context.active_object.type == "MESH"
        )

    def execute(self, context):
        try:
            active_object = context.active_object
            zero_weight_vert_count = utils_select_0_weight_vertices(active_object)
            self.report({"INFO"}, f"{zero_weight_vert_count} Vertices Selected")
        except Exception as err:
            print(f"{err}")
            raise Exception(f"{err}")
            pass
        return {"FINISHED"}


class ButtonLimitAndNormalizeAllWeights(bpy.types.Operator):
    bl_idname = "meshops.limit_and_normalize_weights"
    bl_label = "Limit & Normalize Weights"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Limits the weights of all vertices on the mesh to CustomValue vertex groups, and normalizes them."

    @classmethod
    def poll(cls, context):
        return (
            context.active_object is not None and context.active_object.type == "MESH"
        )

    def execute(self, context):
        limitValue = bpy.context.scene.AQ_props.AQ_limitWeightValue
        try:
            mesh = context.active_object
            utils_limit_and_normalize_weights(mesh,limitValue)
            self.report(
                {"INFO"}, f"Weights normalized and limited to 4 groups per vetex."
            )
        except Exception as err:
            print(f"{err}")
            raise Exception(f"{err}")
            pass
        return {"FINISHED"}


class ButtonReservedOneFace(bpy.types.Operator):
    bl_idname = "objectops.reserved_one_face"
    bl_label = "保留所选物体的单面网格"
    bl_description = "保留活动物体的面索引为0的单面，并删除其余面"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object and context.active_object.type == "MESH"

    def execute(self, context):

        active_obj = bpy.context.active_object

        bpy.ops.object.select_all(action="DESELECT")
        active_obj.select_set(True)
        bpy.context.view_layer.objects.active = active_obj
        
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.ops.mesh.select_mode(type="FACE")

        # 获取编辑模式下的网格数据
        bm = bmesh.from_edit_mesh(active_obj.data)
        bm.faces.ensure_lookup_table()  # 确保索引可用

        # 选择索引为0的面
        try:
            face = bm.faces[0]  # 获取索引为0的面
            face.select = True  # 选中该面
        except IndexError:
            self.report({"WARNING"}, "网格为空，无法保留单面")
            bpy.ops.object.mode_set(mode="OBJECT")
            return {"FINISHED"}

        # 反选（取消选中其他所有面）
        bpy.ops.mesh.select_all(action="INVERT")

        # 删除
        bpy.ops.mesh.delete(type="FACE")

        # 更新网格数据
        bmesh.update_edit_mesh(active_obj.data)
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action='SELECT')


        return {"FINISHED"}


# ----------Utils----------#


def split_faces_by_edge_seams(obj):  # Split mesh faces by seams
    utils_set_mode("EDIT")
    bpy.ops.mesh.select_all(action="SELECT")

    bpy.ops.uv.select_all(action="SELECT")  # Select all UVs
    bpy.ops.uv.seams_from_islands(
        mark_seams=True
    )  # Mark boundary edges of UV islands as seams

    bpy.context.tool_settings.mesh_select_mode = (False, True, False)  # Set Edge Select
    bpy.ops.mesh.select_all(action="DESELECT")

    utils_set_mode(
        "OBJECT"
    )  # For some reason we can only select edges in object mode ???????? :) Funny Blender
    for edge in obj.data.edges:  # Select all edge seams
        if edge.use_seam:
            edge.select = True

    utils_set_mode("EDIT")

    bpy.ops.mesh.edge_split(type="EDGE")  # Split faces by selected edge seams


def utils_set_mode(mode):
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode=mode, toggle=False)


# Select all 0 weight vertices on mesh
# Credit to WolfieBeat
def utils_select_0_weight_vertices(mesh):
    zero_weight_vert_count = 0
    utils_set_mode("EDIT")
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.reveal(select=False)  # Unhide all vertices
    bpy.ops.mesh.select_all(action="DESELECT")
    mesh_data = mesh.data
    utils_set_mode("OBJECT")  # Funny blender only allows object mode selection :)
    for vertex in mesh_data.vertices:
        total_vert_weight = 0.0  # keep track of vertex's total weight
        for (
            vertex_group
        ) in (
            vertex.groups
        ):  # add up total weightr for each vertex group vert belongs to
            total_vert_weight += vertex_group.weight
        if (
            total_vert_weight == 0.0
        ):  # if the vertex weights doesn't add up to roughly 1.0, select it
            vertex.select = True
            zero_weight_vert_count += 1
    utils_set_mode("EDIT")
    return zero_weight_vert_count


# Limit and Normalize all vertex weights
def utils_limit_and_normalize_weights(mesh,limitValue):
    for vg in mesh.vertex_groups:
        # limit total weights
        bpy.ops.object.vertex_group_limit_total(group_select_mode="ALL", limit=limitValue)
        # normalize all weights
        bpy.ops.object.vertex_group_normalize_all(
            group_select_mode="ALL", lock_active=False
        )

classes =[ ButtonRemoveEmpty, ButtonRemoveUnusedBones, ButtonSplitMeshAlongUVs, 
          ButtonDeleteLooseGeometry, ButtonSelect0WeightVertices, 
          ButtonLimitAndNormalizeAllWeights, ButtonReservedOneFace]



def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

