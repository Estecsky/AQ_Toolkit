import bpy

def MHWidls_fixed_bones_fun(name_in,ArmatureName):
        # 需要修正位置的骨骼
    fix_neck_bone = ['Neck_1', 'HeadRX_HJ_01', 'Neck_1_HJ_00']
    fix_spine2_bone = ['Spine_2', 'Spine_2_HJ_00']
    fix_shin_bone = ['L_Shin', 'R_Shin']
    fix_instep_bone = ['L_Instep', 'R_Instep']
    
    
    
        # 修正骨骼，Neck_1应当位于Head与Neck_0的中点
    if 'Head' in name_in and 'Neck_0' in name_in:
        bone1 = bpy.data.armatures[ArmatureName].edit_bones['Head']
        bone2 = bpy.data.armatures[ArmatureName].edit_bones['Neck_0']

    # if bone1 and bone2:
        center_x = (bone1.head.x + bone2.head.x) / 2
        center_y = (bone1.head.y + bone2.head.y) / 2
        center_z = (bone1.head.z + bone2.head.z) / 2

        center_point = (center_x, center_y, center_z)

        for fnb in fix_neck_bone:
            bone = bpy.data.armatures[ArmatureName].edit_bones[fnb]
            original_length = (bone.tail - bone.head).length
            direction = (bone.tail - bone.head).normalized()
            bone.head = center_point
            bone.tail = bone.head + direction * original_length

    # 修正骨骼，若mmd模型骨架没有Upper Chest骨骼，则Spine_2移动到Spine_1与Neck_0的中点
    if 'Upper Chest' not in name_in:
        bone1 = bpy.data.armatures[ArmatureName].edit_bones['Spine_1']
        bone2 = bpy.data.armatures[ArmatureName].edit_bones['Neck_0']

        if bone1 and bone2:
            center_x = (bone1.head.x + bone2.head.x) / 2
            center_y = (bone1.head.y + bone2.head.y) / 2
            center_z = (bone1.head.z + bone2.head.z) / 2

            center_point = (center_x, center_y, center_z)

        for fs2b in fix_spine2_bone:
            bone = bpy.data.armatures[ArmatureName].edit_bones[fs2b]
            original_length = (bone.tail - bone.head).length
            direction = (bone.tail - bone.head).normalized()
            bone.head = center_point
            bone.tail = bone.head + direction * original_length

    # 修正骨骼，Instep应位于Foot与Toe的中点，额外修正Z轴坐标与Toe平齐，即在脚底
    if 'L_Foot' in name_in and 'L_Toe' in name_in:
        bone1 = bpy.data.armatures[ArmatureName].edit_bones['L_Foot']
        bone2 = bpy.data.armatures[ArmatureName].edit_bones['L_Toe']

    # if bone1 and bone2:
        center_x = (bone1.head.x + bone2.head.x) / 2
        center_y = (bone1.head.y + bone2.head.y) / 2
        center_z = bone2.head.z

        center_point = (center_x, center_y, center_z)

        bone = bpy.data.armatures[ArmatureName].edit_bones[fix_instep_bone[0]]
        original_length = (bone.tail - bone.head).length
        direction = (bone.tail - bone.head).normalized()
        bone.head = center_point
        bone.tail = bone.head + direction * original_length

    if 'R_Foot' in name_in and 'R_Toe' in name_in:
        bone1 = bpy.data.armatures[ArmatureName].edit_bones['R_Foot']
        bone2 = bpy.data.armatures[ArmatureName].edit_bones['R_Toe']

    # if bone1 and bone2:
        center_x = (bone1.head.x + bone2.head.x) / 2
        center_y = (bone1.head.y + bone2.head.y) / 2
        center_z = bone2.head.z

        center_point = (center_x, center_y, center_z)

        bone = bpy.data.armatures[ArmatureName].edit_bones[fix_instep_bone[1]]
        original_length = (bone.tail - bone.head).length
        direction = (bone.tail - bone.head).normalized()
        bone.head = center_point
        bone.tail = bone.head + direction * original_length

    # 修正骨骼，Shin应当位于Knee的正下方距离0.01的位置
    for fshb in fix_shin_bone:
        if fshb in name_in:
            bone = bpy.data.armatures[ArmatureName].edit_bones[fshb]
            bone.head.z = bone.head.z - 0.01
            bone.tail.z = bone.tail.z - 0.01