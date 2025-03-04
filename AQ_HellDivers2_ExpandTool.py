import bpy


# =======================
# HellDivers2 ExpandTool可选组件
# =======================


class ButtonDeleteMutilationMesh(bpy.types.Operator):
    bl_idname = "object.delete_mutilation_mesh"
    bl_label = "删除所选物体断肢网格"
    bl_description = "根据物体材质名称,删除所选物体所有断肢网格（可多选），必须将有断肢材质的物体设为活跃物体"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        is_match = False
        obj = context.object
        if obj and obj.type == "MESH":
            for slot in obj.material_slots:
                if slot.material:
                    mat_name = slot.material.name
                    if mat_name.startswith("12070197922454493211"):
                        is_match = True
        return is_match and obj

    def execute(self, context):

        active_obj = bpy.context.active_object
        selected_objects = bpy.context.selected_objects
        deleted_num = 0
        bpy.ops.object.select_all(action="DESELECT")
        for obj in selected_objects:
            if obj.type == "MESH":

                obj.select_set(True)
                bpy.ops.object.mode_set(mode="EDIT")
                bpy.ops.mesh.select_all(action="DESELECT")
                bpy.ops.object.mode_set(mode="OBJECT")
                # 获取物体的所有材质槽
                if len(obj.material_slots) == 0:
                    continue
                for index, slot in enumerate(obj.material_slots):
                    if slot.material:
                        # 获取材质名称
                        mat_name = slot.material.name
                        if mat_name.startswith("12070197922454493211"):
                            obj.active_material_index = index
                            bpy.ops.object.mode_set(mode="EDIT")
                            bpy.ops.mesh.select_all(action="DESELECT")

                            # 选择目标材质的网格
                            bpy.ops.mesh.select_mode(
                                use_extend=False, use_expand=False, type="FACE"
                            )

                            bpy.ops.object.material_slot_select()

                            bpy.ops.mesh.delete(type="VERT")
                            bpy.ops.mesh.select_all(action="DESELECT")
                            bpy.ops.object.mode_set(mode="OBJECT")
                            deleted_num += 1

                obj.select_set(False)
            else:
                continue
        # 还原之前的所选状态
        for obj in selected_objects:
            obj.select_set(True)
        # 还原激活物体
        bpy.context.view_layer.objects.active = active_obj

        self.report({"INFO"}, "删除了{}个物体的断肢网格".format(deleted_num))

        return {"FINISHED"}


def ExpandPanel(layout):
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="HellDivers2 拓展组件", icon="TOOL_SETTINGS")
    row = layout.row()
    row.scale_y = 1.3
    row.operator("object.delete_mutilation_mesh", text="删除断肢网格", icon="MESH_DATA")


def register():
    bpy.utils.register_class(ButtonDeleteMutilationMesh)


def unregister():
    bpy.utils.unregister_class(ButtonDeleteMutilationMesh)
