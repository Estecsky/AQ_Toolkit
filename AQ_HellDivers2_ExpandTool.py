import bpy
import os

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
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.select_all(action="DESELECT")
        for obj in selected_objects:
            if obj.type == "MESH":

                obj.select_set(True)
                bpy.ops.object.mode_set(mode="EDIT")
                bpy.ops.mesh.select_all(action="DESELECT")
                # 获取物体的所有材质槽
                if len(obj.material_slots) == 0:
                    continue
                else:
                    for index, slot in enumerate(obj.material_slots):
                        if slot.material:
                            # 获取材质名称
                            mat_name = slot.material.name
                            if mat_name.startswith("12070197922454493211"):
                                bpy.ops.object.mode_set(mode="EDIT")
                                bpy.ops.mesh.select_all(action="DESELECT")
                                obj.active_material_index = index

                                # 选择目标材质的网格
                                bpy.ops.mesh.select_mode(
                                    use_extend=False, use_expand=False, type="VERT"
                                )

                                bpy.ops.object.material_slot_select()

                                bpy.ops.mesh.delete(type="VERT")
                                bpy.ops.mesh.select_all(action="DESELECT")
                                # bpy.ops.object.mode_set(mode="OBJECT")
                                deleted_num += 1

                bpy.ops.object.mode_set(mode="OBJECT")
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

class ButtonImportAvaterHelldiverRig(bpy.types.Operator):
    bl_idname = "object.import_avatar_helldiver_rig"
    bl_label = "导入Helldiver2角色通用绑定"
    bl_description = "导入Helldiver2角色通用绑定骨架"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        skeleton_name = "5556372446766824087_rig"
        dir_path = os.path.dirname(__file__)
        rig_file_path = os.path.join(dir_path,"AvaterHelldiverRig","avater_helldiver_rig.blend")
        #检查文件是否存在
        if not os.path.exists(rig_file_path):
            self.report({"ERROR"}, f"骨架文件: {rig_file_path} 不存在")
            return {"CANCELLED"}
        # 使用 bpy.ops.wm.append() 函数从.blend文件追加到场景中
        bpy.ops.wm.append(
            filepath=os.path.join(rig_file_path, "Object", skeleton_name),
            directory=os.path.join(rig_file_path, "Object"),
            filename=skeleton_name,
        )
        # 获取追加的物体
        appended_object = bpy.context.selected_objects[0] if bpy.context.selected_objects else None
        if appended_object:
        # 高亮物体
            bpy.ops.object.select_all(action="DESELECT")
            appended_object.select_set(True)
            bpy.context.view_layer.objects.active = appended_object 
            # =======================
            if bpy.context.scene.AQ_Props.AvaterHelldiverNewCollection:
                # 创建新集合
                collection_name = "Avater_Helldiver_Rig"
                if collection_name in bpy.data.collections:
                    new_collection = bpy.data.collections[collection_name]
                else:
                    new_collection = bpy.data.collections.new(collection_name)
                    bpy.context.scene.collection.children.link(new_collection)
                  # 将物体放入新集合
                if appended_object.name in bpy.context.collection.objects:
                    bpy.context.collection.objects.unlink(appended_object)
                new_collection.objects.link(appended_object)
        
        
        
        self.report({"INFO"}, "已导入通用绑定骨架")
        return {"FINISHED"}


def ExpandPanel(layout):
    props = bpy.context.scene.AQ_Props
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="HellDivers2 拓展组件", icon="TOOL_SETTINGS")
    row = layout.row()
    row.scale_y = 1.3
    row.operator("object.delete_mutilation_mesh", text="删除断肢网格", icon="MESH_DATA")
    row = layout.row()
    row.scale_y = 1
    row.prop(props, "AvaterHelldiverNewCollection", text="导入时创建新集合")
    row = layout.row()
    row.scale_y = 1.5
    row.operator("object.import_avatar_helldiver_rig", text="导入Helldiver2角色通用绑定", icon="IMPORT")

def register():
    bpy.utils.register_class(ButtonDeleteMutilationMesh)
    bpy.utils.register_class(ButtonImportAvaterHelldiverRig)


def unregister():
    bpy.utils.unregister_class(ButtonDeleteMutilationMesh)
    bpy.utils.unregister_class(ButtonImportAvaterHelldiverRig)
