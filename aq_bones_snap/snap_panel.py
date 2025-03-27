import bpy


def draw_SnapPanel(layout):
    props = bpy.context.scene.AQ_Props
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="必须先标记吸附骨架，需要同时选中目标骨架与吸附骨架", icon="ERROR")
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="提示：吸附骨架将会吸附到目标骨架", icon="ERROR")
    
    row = layout.row()
    row.scale_y = 1.3
    row.operator("skel.sign_snap_armature",text="标记为吸附骨架",icon="MODIFIER")
    row.operator("skel.del_snap_sign",text="",icon="TRASH")
    
    
    row = layout.row()
    row.scale_y = 1.3
    row.prop(props,"MHWilds_Fix_Bones",text="MHWilds骨骼修正")
    
    row = layout.row()
    row.scale_y = 1.4
    row.prop(props,"BoneList")
    row.operator("open.bone_dict_path",text="打开字典文件夹",icon="FILE_FOLDER")
    
    row = layout.row()
    row.scale_y = 1.3
    row.operator("skel.aq_snap_bone", text="吸附骨骼", icon="OUTLINER_OB_ARMATURE")
    row = layout.row()
    row.scale_y = 1.3
    row.operator("skel.aq_rename_bones_vg", text="重命名顶点组", icon="GROUP_VERTEX")