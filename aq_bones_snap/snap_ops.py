import bpy
import os
import importlib
from . import MHWilds_fixed_bones

class ButtonOpenDictFolder(bpy.types.Operator):
    bl_description = "打开字典文件夹"
    bl_idname = "open.bone_dict_path"
    bl_label = "Open Dict Path"
    
    def execute(self, context):
        presetsPath = os.path.join(os.path.dirname(os.path.split(os.path.abspath(__file__))[0]),"aq_bones_snap/bone_name_list/")
        os.startfile(presetsPath)
        return {'FINISHED'}


class ButtonSignSnapArmature(bpy.types.Operator):
    bl_idname = "skel.sign_snap_armature"
    bl_label =  "aq_sign_snap_armature"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if len(context.selected_objects) > 1:
            return False
        return context.active_object.type == 'ARMATURE'
    
    def execute(self, context):
        active_object = context.active_object
        active_object["AQ_Armature_Type"] = "Snap"
        
        self.report({'INFO'}, "标记为吸附骨骼完成")
        return {'FINISHED'}
    
class ButtonDelSignSnap(bpy.types.Operator):
    bl_idname = "skel.del_snap_sign"
    bl_label =  "aq_del_snap_sign"
    bl_description = "删除吸附骨骼的标记"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        try:
            active_object = context.active_object
            return active_object["AQ_Armature_Type"]
        except:
            return False
    
    def execute(self, context):
        active_object = context.active_object
        del active_object["AQ_Armature_Type"]
        self.report({'INFO'}, "标记已删除")
        return {'FINISHED'}
    
    
    


class ButtonBoneSnap(bpy.types.Operator):
    bl_label = "button_aq_snap_bone"
    bl_idname = "skel.aq_snap_bone"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if not context.selected_objects:
            return False
        # if len(context.selected_objects) != 2:
        #     return False
        # 检查所有选中的对象是否都是骨骼
        for obj in context.selected_objects:
            if obj.type != "ARMATURE":
                return False
        # 如果所有选中的对象都是骨骼，则返回True
        return True
    
    def execute(self, context):
        props = bpy.context.scene.AQ_Props
        enumValue = props.BoneList
        file_name, file_extension = os.path.splitext(os.path.basename(enumValue))
        
        preset_module = importlib.import_module(f"..bone_name_list.{file_name}", package=__name__)
        # 热更新骨骼字典
        if "preset_module" in locals():
            importlib.reload(preset_module)
            
        fixed_name_list = preset_module.snap_bone_fixed_name_list
        rename_name_list = preset_module.rename_vg_fixed_name_list
        
        
        
        #若选中的骨架多于两个，则报错
        if len(context.selected_objects) > 2:
            # showErrorMessageBox(
            #     "There are too many skeletons selected. Please select only two skeletons.")
            self.report({"ERROR"}, "选择了过多骨架，只能选择两个骨架！")
            return {"CANCELLED"}
        else:
            #吸附骨骼
            bpy.ops.object.mode_set(mode='OBJECT')

            #区分选中的两个骨架中哪个是外部（目标）骨架，哪个是MHWilds（吸附）骨架
            armature_snap = None
            armature_target = None
            for obj in bpy.context.selected_objects:
                if obj.type == 'ARMATURE' and obj.get("AQ_Armature_Type") == "Snap":
                    armature_snap = obj
                else:
                    if armature_target is None:
                        armature_target = obj
                        
            #判定选中的两个骨架中，是否同时存在外部骨架和游戏骨架
            both_exist = armature_snap is not None and armature_target is not None
            #若不同时存在，则报错
            if not both_exist:
                # showErrorMessageBox(
                #     "The selected skeletons doesn't contain both the external skeleton and MHWilds skeleton.")            
                self.report({"ERROR"}, "选择的骨架没有同时包含吸附骨架和目标骨架")
                return {'CANCELLED'}
            else:
                #获取并保存复制骨架中所有骨骼的名称
                name_target = [bone.name for bone in armature_target.data.bones]
                #用字典中的几个骨骼名来判定选择的字典是否匹配当前选中的外部骨架
                if rename_name_list[0][0] in name_target and rename_name_list[1][0] in name_target and rename_name_list[2][0] in name_target and rename_name_list[4][0] in name_target and rename_name_list[5][0] in name_target:
                    #复制一个外部骨架对象出来用于吸附
                    armature_target_copy = armature_target.copy()
                    armature_target_copy.data = armature_target.data.copy()
                    armature_target_copy.name = f"{armature_target.name}_copy"
                    bpy.context.collection.objects.link(armature_target_copy)

                    #激活并选中MHWilds骨架，然后与复制的外部骨架合并在一起
                    bpy.context.view_layer.objects.active = armature_snap
                    bones = bpy.context.active_object.data.bones
                    name_ori = [bone.name for bone in bones]
                    bpy.ops.object.select_all(action='DESELECT')
                    armature_target_copy.select_set(True)
                    armature_snap.select_set(True)
                    bpy.ops.object.join()

                    #获取并保存合并后骨架中所有骨骼的名称
                    ArmatureName = bpy.context.active_object.data.name
                    bones = bpy.context.active_object.data.bones
                    name_in = [bone.name for bone in bones]

                    bpy.ops.object.mode_set(mode='EDIT')
                    for bone_name in fixed_name_list:
                        bone1_name, bone2_name = bone_name
                        #仅当字典中的两列骨骼名都存在于合并后的骨架中时才进行吸附操作
                        if bone1_name in name_in and bone2_name in name_in:
                            bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[
                                bone1_name]
                            bpy.context.object.data.use_mirror_x = False
                            bpy.ops.armature.select_all(action='DESELECT')
                            bpy.ops.object.select_pattern(pattern=bone1_name, case_sensitive=False, extend=True)
                            bpy.ops.object.select_pattern(pattern=bone2_name, case_sensitive=False, extend=True)
                            bpy.context.area.type = 'VIEW_3D'
                            bpy.ops.view3d.snap_selected_to_active()
                            # bpy.context.area.type = 'TEXT_EDITOR'
                            bpy.ops.armature.select_all(action='DESELECT')
                    # 为MHWILDS 修正骨骼
                    if bpy.context.scene.AQ_Props.MHWilds_Fix_Bones:
                        MHWilds_fixed_bones.MHWidls_fixed_bones_fun(name_in = name_in,ArmatureName = ArmatureName)

                    for bone_name in name_in:
                        if bone_name not in name_ori:
                            bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[bone_name]
                            bpy.ops.armature.delete()
        
                    bpy.ops.object.mode_set(mode='OBJECT')
                #若选择的字典不匹配当前选中的外部骨架，则报错
                else:
                    # showErrorMessageBox(
                    #     "The selected dictionary may not match the currently selected external skeleton. Please select the correct dictionary.")
                    self.report({'ERROR'}, "The selected dictionary may not match the currently selected external skeleton. Please select the correct dictionary.")
                    return {'CANCELLED'}
        
        
        self.report({'INFO'}, "吸附完成")
        return {'FINISHED'}



class ButtonRenameSkelVertexGroup(bpy.types.Operator):
    bl_idname = "skel.aq_rename_bones_vg"
    bl_label = "button_RenameSkelVertexGroup"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        if bpy.context.selected_objects is not None:
            for obj in bpy.context.selected_objects:
                return obj.type == "MESH"
    
    
    def execute(self, context):
        props = bpy.context.scene.AQ_Props
        enumValue = props.BoneList
        file_name, file_extension = os.path.splitext(os.path.basename(enumValue))

        preset_module = importlib.import_module(f"..bone_name_list.{file_name}", package=__name__)
        # 热更新骨骼字典
        if "preset_module" in locals():
            importlib.reload(preset_module)
            
        fixed_name_list = preset_module.rename_vg_fixed_name_list

        for obj in bpy.context.selected_objects:
            v_groups = obj.vertex_groups

            if fixed_name_list[0][0] in v_groups:
                for n in fixed_name_list:
                    if n[0] in v_groups:
                        v_groups[n[0]].name = n[1]
            else:
                for n in fixed_name_list:
                    if n[0] in v_groups:
                        v_groups[n[0]].name = n[1]

        self.report({'INFO'}, '改名完成')
        
        
        
        return {'FINISHED'}













lst = [
    ButtonOpenDictFolder,
    ButtonBoneSnap,
    ButtonRenameSkelVertexGroup,
    ButtonSignSnapArmature,
    ButtonDelSignSnap,

]



def register():
    for cls in lst:
        bpy.utils.register_class(cls)


def unregister():
    for cls in lst:
        bpy.utils.unregister_class(cls)