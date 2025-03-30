import bpy
import bmesh
import os


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
    bl_description = "根据模型的骨架修改器选中/移除骨架中没有对应顶点组的骨骼"
    bl_idname = "misremove_unused.ops_bones"

    def execute(self, context):
        props = bpy.context.scene.AQ_Props
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

            # 选择编辑不存在对应顶点组的骨骼
            bpy.ops.object.mode_set(mode="OBJECT")  # 确保在对象模式下
            bpy.ops.object.select_all(action="DESELECT")
            skeleton.select_set(True)
            bpy.context.view_layer.objects.active = skeleton
            bpy.ops.object.mode_set(mode="EDIT")  # 进入编辑模式以编辑骨骼

            if bones_to_remove:
                # 根据开关判断是否移除选中的未使用骨骼
                if props.SelectAndRemove_bone == True:
                    for bone_name in bones_to_remove:

                        edit_bone = skeleton_data.edit_bones.get(bone_name)

                        skeleton_data.edit_bones.remove(edit_bone)
                        self.report({"INFO"}, f"骨骼 '{bone_name}' 已移除.")
                else:
                    select_num = 0
                    bpy.ops.armature.select_all(action="DESELECT")
                    for bone_name in bones_to_remove:
                        edit_bone = skeleton_data.edit_bones.get(bone_name)
                        # 选中bone
                        edit_bone.select = True
                        select_num += 1

                    self.report({"INFO"}, f"已选中{select_num}个未使用骨骼")

            else:
                self.report({"WARNING"}, "没有找到任何未使用骨骼，请先移除空顶点组")

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
            utils_limit_and_normalize_weights(mesh, limitValue)
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
        if bpy.context.object.mode == "OBJECT":
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
        bpy.ops.mesh.select_all(action="SELECT")

        if bpy.context.scene.AQ_Props.Auto_Xray_Shading:
            if not is_xray_enabled():
                bpy.ops.view3d.toggle_xray()

        return {"FINISHED"}


class ButtonSelectSeams(bpy.types.Operator):
    bl_idname = "select.aq_select_seams"
    bl_label = "select_seams"
    bl_description = "选中缝合边"

    @classmethod
    def poll(cls, context):
        if bpy.context.active_object:
            obj = bpy.context.active_object
        else:
            return False
        return obj.type == "MESH"

    def execute(self, context):
        obj = bpy.context.active_object

        if bpy.context.object.mode != "OBJECT":
            bpy.ops.object.mode_set(mode="OBJECT")

        bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type="EDGE")
        bpy.ops.mesh.select_all(action="DESELECT")

        bm = bmesh.from_edit_mesh(obj.data)
        bm.edges.ensure_lookup_table()

        for e in bm.edges:
            e.select = e.seam

        bmesh.update_edit_mesh(obj.data)
        return {"FINISHED"}


# Inspired by SilentNightSound#7430
# Combines vertex groups with the same prefix into one
class ButtonCombineVertexGroups(bpy.types.Operator):
    bl_idname = "object.aq_combine_vertex_groups"
    bl_label = "Combine Vertex Groups"
    bl_description = "合并同前缀名的顶点组权重，从0开始，往后顺延（0，0.001，1，1.001，将分别合并为0，1两组）"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.context.active_object:
            obj = bpy.context.active_object
        else:
            return False
        return obj.type == "MESH"

    def execute(self, context):
        props = bpy.context.scene.AQ_Props
        vgroup_num = props.Comebine_vgroup_num
        for num in range(0, vgroup_num + 1):
            obj = bpy.context.active_object
            relevant = [
                x.name for x in obj.vertex_groups if x.name.split(".")[0] == f"{num}"
            ]

            vgroup = obj.vertex_groups.new(name=f"x{num}")

            for vert_id, vert in enumerate(obj.data.vertices):
                available_groups = [v_group_elem.group for v_group_elem in vert.groups]

                combined = 0
                for v in relevant:
                    if obj.vertex_groups[v].index in available_groups:
                        combined += obj.vertex_groups[v].weight(vert_id)

                if combined > 0:
                    vgroup.add([vert_id], combined, "ADD")

            for vg in [
                x for x in obj.vertex_groups if x.name.split(".")[0] == f"{num}"
            ]:
                obj.vertex_groups.remove(vg)

            for vg in obj.vertex_groups:
                if vg.name[0].lower() == "x":
                    vg.name = vg.name[1:]

        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.vertex_group_sort()

        return {"FINISHED"}

class ButtonImportFaceOptimizeTemplate(bpy.types.Operator):
    bl_idname = "model.import_face_optimize_template"
    bl_label = "import_face_optimize_template"
    bl_description = "导入二次元面部法向优化模板"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        object_name = "Face_DataTransfer_Normal"
        
        dir_path = os.path.dirname(__file__)
        blend_file_path = os.path.join(dir_path, "NormalOptimizeTemplate", "FaceTemplate.blend")
        # 确保文件存在
        if not os.path.exists(blend_file_path):
            self.report({"ERROR"}, f"文件 {blend_file_path} 不存在")
            return {"CANCEL"}
        # 使用 bpy.ops.wm.append 追加对象到当前场景
        bpy.ops.wm.append(
            filepath=os.path.join(blend_file_path, "Object", object_name),
            directory=os.path.join(blend_file_path, "Object"),
            filename=object_name
        )
            
        # 获取追加的物体
        appended_object = bpy.context.selected_objects[0] if bpy.context.selected_objects else None
        if appended_object:
        # 高亮物体
            bpy.ops.object.select_all(action="DESELECT")
            appended_object.select_set(True)
            bpy.context.view_layer.objects.active = appended_object
            # =====================
            if bpy.context.scene.AQ_Props.TemplateNewCollection:
                # 创建新集合
                collection_name = "Face_DataTransfer_Normal"
                if collection_name not in bpy.data.collections:
                    new_collection = bpy.data.collections.new(collection_name)
                    bpy.context.scene.collection.children.link(new_collection)
                else:
                    new_collection = bpy.data.collections[collection_name]
                
                # 将物体放入新集合
                if appended_object.name in bpy.context.collection.objects:
                    bpy.context.collection.objects.unlink(appended_object)
                new_collection.objects.link(appended_object)
            

            # 应用镜像修改器
            if bpy.context.scene.AQ_Props.ApplyMirrorModifier:
                # 添加镜像修改器
                # mirror_mod = appended_object.modifiers.new(name="Mirror", type='MIRROR')
                # 应用镜像修改器
                bpy.ops.object.modifier_apply(modifier="Mirror")
        

        return{"FINISHED"}


# ----------Utils----------#


def is_xray_enabled():
    # 获取当前活动的 3D 视图空间
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D":
            for space in area.spaces:
                if space.type == "VIEW_3D":
                    return space.shading.show_xray
    return False


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
def utils_limit_and_normalize_weights(mesh, limitValue):
    for vg in mesh.vertex_groups:
        # limit total weights
        bpy.ops.object.vertex_group_limit_total(
            group_select_mode="ALL", limit=limitValue
        )
        # normalize all weights
        bpy.ops.object.vertex_group_normalize_all(
            group_select_mode="ALL", lock_active=False
        )


classes = [
    ButtonRemoveEmpty,
    ButtonRemoveUnusedBones,
    ButtonSplitMeshAlongUVs,
    ButtonDeleteLooseGeometry,
    ButtonSelect0WeightVertices,
    ButtonLimitAndNormalizeAllWeights,
    ButtonReservedOneFace,
    ButtonSelectSeams,
    ButtonCombineVertexGroups,
    ButtonImportFaceOptimizeTemplate,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
