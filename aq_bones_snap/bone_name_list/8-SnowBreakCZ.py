# 编写字典时最好按照骨骼层级的顺序来编写，简单来说就是胯到胸到头，左臂到左手，右臂到右手，左腿到左脚，右腿到右脚。
# 注意，请确保rename_vg_fixed_name_list字典中的前6个骨骼名，普遍都存在于该字典对应的一类外部骨架中，插件会用于判定选择的字典是否匹配当前选中的外部骨架。

snap_bone_fixed_name_list = [
            ['Bip001-Pelvis', 'Hip'],
            ['Bip001-Pelvis', 'Hip_HJ_00'],
            ['Bip001-Spine', 'Spine_0'],
            ['Bip001-Spine', 'Spine_0_HJ_00'],
            ['Bip001-Spine1', 'Spine_1'],
            ['Bip001-Spine1', 'Spine_1_HJ_00'],
            ['Bip001-Spine2', 'Spine_2'],
            ['Bip001-Spine2', 'Spine_2_HJ_00'],
            ['Bip001-Neck', 'Neck_0'],
            ['Bip001-Neck', 'Neck_0_HJ_00'],

            #    ['','R_Bust_HJ_00'],
            #    ['','R_Bust_HJ_01'],
            #    ['','L_Bust_HJ_00'],
            #    ['','L_Bust_HJ_01'],

            ['Bip001-Head', 'Head'],


            ['Bip001-L-Clavicle', 'L_Shoulder'],
            ['Bip001-L-UpperArm', 'L_UpperArm'],
            ['Bip001-L-Forearm', 'L_Forearm'],
            ['Bip001-L-Hand', 'L_Hand'],
            ['Bip001-L-Hand', 'L_Wep'],

            ['Bip001-L-Finger0', 'L_Thumb1'],
            ['Bip001-L-Finger01', 'L_Thumb2'],
            ['Bip001-L-Finger02', 'L_Thumb3'],

            ['Bip001-L-Finger0', 'L_Thumb_HJ_00'],
            ['Bip001-L-Finger01', 'L_Thumb_HJ_01'],
            ['Bip001-L-Finger02', 'L_Thumb_HJ_02'],
            ['Bip001-L-Finger0', 'L_Thumb_HJ_03'],

            ['Bip001-L-Finger1', 'L_IndexF1'],
            ['Bip001-L-Finger11', 'L_IndexF2'],
            ['Bip001-L-Finger12', 'L_IndexF3'],

            ['Bip001-L-Finger1', 'L_IndexF_HJ_01'],
            ['Bip001-L-Finger11', 'L_IndexF_HJ_02'],
            ['Bip001-L-Finger12', 'L_IndexF_HJ_03'],
            ['Bip001-L-Finger1', 'L_IndexF_HJ_00'],
            ['Bip001-L-Finger1', 'L_IndexF_HJ_04'],

            ['Bip001-L-Finger2', 'L_MiddleF1'],
            ['Bip001-L-Finger21', 'L_MiddleF2'],
            ['Bip001-L-Finger22', 'L_MiddleF3'],

            ['Bip001-L-Finger2', 'L_MiddleF_HJ_01'],
            ['Bip001-L-Finger21', 'L_MiddleF_HJ_02'],
            ['Bip001-L-Finger22', 'L_MiddleF_HJ_03'],
            ['Bip001-L-Finger2', 'L_MiddleF_HJ_00'],
            ['Bip001-L-Finger2', 'L_MiddleF_HJ_04'],

            ['Bip001-L-Hand', 'L_Palm'],

            ['Bip001-L-Finger3', 'L_RingF1'],
            ['Bip001-L-Finger31', 'L_RingF2'],
            ['Bip001-L-Finger32', 'L_RingF3'],

            ['Bip001-L-Finger3', 'L_RingF_HJ_01'],
            ['Bip001-L-Finger31', 'L_RingF_HJ_02'],
            ['Bip001-L-Finger32', 'L_RingF_HJ_03'],
            ['Bip001-L-Finger3', 'L_RingF_HJ_00'],
            ['Bip001-L-Finger3', 'L_RingF_HJ_04'],

            ['Bip001-L-Finger4', 'L_PinkyF1'],
            ['Bip001-L-Finger41', 'L_PinkyF2'],
            ['Bip001-L-Finger42', 'L_PinkyF3'],

            ['Bip001-L-Finger4', 'L_PinkyF_HJ_01'],
            ['Bip001-L-Finger41', 'L_PinkyF_HJ_02'],
            ['Bip001-L-Finger42', 'L_PinkyF_HJ_03'],
            ['Bip001-L-Finger4', 'L_PinkyF_HJ_00'],
            ['Bip001-L-Finger4', 'L_PinkyF_HJ_04'],

            ['Bip001-L-Hand', 'L_HandRZ_HJ_00'],
            ['Bip001-L-Hand', 'L_Hand_HJ_01'],
            ['Bip001-L-Hand', 'L_Wep_Sub'],
            ['Bip001-L-Hand', 'L_Hand_HJ_00'],

            ['Bip001-L-ForeTwist1', 'L_ForearmTwist_HJ_02'],
            ['Bip001-L-Forearm', 'L_ForearmRY_HJ_00'],
            ['Bip001-L-Forearm', 'L_ForearmRY_HJ_01'],
            ['Bip001-L-ForeTwist1', 'L_ForearmTwist_HJ_01'],
            ['Bip001-L-Forearm', 'L_ForearmTwist_HJ_00'],
            ['Bip001-L-Forearm', 'L_Forearm_HJ_00'],
            ['Bip001-L-Forearm', 'L_Elbow_HJ_00'],

            ['Bip001-L-UpperArm', 'L_UpperArmTwist_HJ_00'],

            ['Bip001-LUpArmTwist1', 'L_UpperArmTwist_HJ_01'],
            ['Bip001-LUpArmTwist1', 'L_Triceps_HJ_00'],
            ['Bip001-LUpArmTwist1', 'L_Biceps_HJ_00'],
            ['Bip001-LUpArmTwist1', 'L_Biceps_HJ_01'],
            ['Bip001-LUpArmTwist1', 'L_UpperArmTwist_HJ_02'],

            ['Bip001-L-Forearm', 'L_ForearmDouble_HJ_00'],
            ['Bip001-L-UpperArm', 'L_UpperArm_HJ_00'],
            ['Bone_UpArmTwist_l', 'L_Deltoid_HJ_00'],
            ['Bone_UpArmTwist_l', 'L_Deltoid_HJ_01'],
            ['Bone_UpArmTwist_l', 'L_Deltoid_HJ_02'],
            ['Bone_UpArmTwist_l', 'L_UpperArmDouble_HJ_00'],

            ['Bip001-L-Clavicle', 'L_Shoulder_HJ_00'],

            ['Bip001-R-Clavicle', 'R_Shoulder'],
            ['Bip001-R-UpperArm', 'R_UpperArm'],
            ['Bip001-R-Forearm', 'R_Forearm'],
            ['Bip001-R-Hand', 'R_Hand'],
            ['Bip001-R-Hand', 'R_Wep'],

            ['Bip001-R-Finger0', 'R_Thumb1'],
            ['Bip001-R-Finger01', 'R_Thumb2'],
            ['Bip001-R-Finger02', 'R_Thumb3'],

            ['Bip001-R-Finger0', 'R_Thumb_HJ_00'],
            ['Bip001-R-Finger01', 'R_Thumb_HJ_01'],
            ['Bip001-R-Finger02', 'R_Thumb_HJ_02'],
            ['Bip001-R-Finger0', 'R_Thumb_HJ_03'],

            ['Bip001-R-Finger1', 'R_IndexF1'],
            ['Bip001-R-Finger11', 'R_IndexF2'],
            ['Bip001-R-Finger12', 'R_IndexF3'],

            ['Bip001-R-Finger1', 'R_IndexF_HJ_01'],
            ['Bip001-R-Finger11', 'R_IndexF_HJ_02'],
            ['Bip001-R-Finger12', 'R_IndexF_HJ_03'],
            ['Bip001-R-Finger1', 'R_IndexF_HJ_00'],
            ['Bip001-R-Finger1', 'R_IndexF_HJ_04'],

            ['Bip001-R-Finger2', 'R_MiddleF1'],
            ['Bip001-R-Finger21', 'R_MiddleF2'],
            ['Bip001-R-Finger22', 'R_MiddleF3'],

            ['Bip001-R-Finger2', 'R_MiddleF_HJ_01'],
            ['Bip001-R-Finger21', 'R_MiddleF_HJ_02'],
            ['Bip001-R-Finger22', 'R_MiddleF_HJ_03'],
            ['Bip001-R-Finger2', 'R_MiddleF_HJ_00'],
            ['Bip001-R-Finger2', 'R_MiddleF_HJ_04'],

            ['Bip001-R-Hand', 'R_Palm'],

            ['Bip001-R-Finger3', 'R_RingF1'],
            ['Bip001-R-Finger31', 'R_RingF2'],
            ['Bip001-R-Finger32', 'R_RingF3'],

            ['Bip001-R-Finger3', 'R_RingF_HJ_01'],
            ['Bip001-R-Finger31', 'R_RingF_HJ_02'],
            ['Bip001-R-Finger32', 'R_RingF_HJ_03'],
            ['Bip001-R-Finger3', 'R_RingF_HJ_00'],
            ['Bip001-R-Finger3', 'R_RingF_HJ_04'],

            ['Bip001-R-Finger4', 'R_PinkyF1'],
            ['Bip001-R-Finger41', 'R_PinkyF2'],
            ['Bip001-R-Finger42', 'R_PinkyF3'],

            ['Bip001-R-Finger4', 'R_PinkyF_HJ_01'],
            ['Bip001-R-Finger41', 'R_PinkyF_HJ_02'],
            ['Bip001-R-Finger42', 'R_PinkyF_HJ_03'],
            ['Bip001-R-Finger4', 'R_PinkyF_HJ_00'],
            ['Bip001-R-Finger4', 'R_PinkyF_HJ_04'],

            ['Bip001-R-Hand', 'R_HandRZ_HJ_00'],
            ['Bip001-R-Hand', 'R_Hand_HJ_01'],
            ['Bip001-R-Hand', 'R_Wep_Sub'],
            ['Bip001-R-Hand', 'R_Hand_HJ_00'],

            ['Bip001-R-ForeTwist1', 'R_ForearmTwist_HJ_02'],
            ['Bip001-R-Forearm', 'R_ForearmRY_HJ_00'],
            ['Bip001-R-Forearm', 'R_ForearmRY_HJ_01'],
            ['Bip001-R-ForeTwist1', 'R_ForearmTwist_HJ_01'],
            ['Bip001-R-Forearm', 'R_ForearmTwist_HJ_00'],
            ['Bip001-R-Forearm', 'R_Shield'],
            ['Bip001-R-Forearm', 'R_Forearm_HJ_00'],
            ['Bip001-R-Forearm', 'R_Elbow_HJ_00'],

            ['Bip001-R-UpperArm', 'R_UpperArmTwist_HJ_00'],

            ['Bip001-RUpArmTwist1', 'R_UpperArmTwist_HJ_01'],
            ['Bip001-RUpArmTwist1', 'R_Triceps_HJ_00'],
            ['Bip001-RUpArmTwist1', 'R_Biceps_HJ_00'],
            ['Bip001-RUpArmTwist1', 'R_Biceps_HJ_01'],
            ['Bip001-RUpArmTwist1', 'R_UpperArmTwist_HJ_02'],

            ['Bip001-R-Forearm', 'R_ForearmDouble_HJ_00'],
            ['Bip001-R-UpperArm', 'R_UpperArm_HJ_00'],
            ['Bone_UpArmTwist_r', 'R_Deltoid_HJ_00'],
            ['Bone_UpArmTwist_r', 'R_Deltoid_HJ_01'],
            ['Bone_UpArmTwist_r', 'R_Deltoid_HJ_02'],
            ['Bone_UpArmTwist_r', 'R_UpperArmDouble_HJ_00'],

            ['Bip001-R-Clavicle', 'R_Shoulder_HJ_00'],

            ['Bip001-L-Clavicle', 'L_Traps_HJ_00'],
            ['Bip001-L-Clavicle', 'L_Traps_HJ_01'],
            ['Bip001-L-Clavicle', 'L_Pec_HJ_00'],
            ['Bip001-L-Clavicle', 'L_Pec_HJ_01'],
            ['Bip001-L-Clavicle', 'L_Lats_HJ_00'],
            ['Bip001-L-Clavicle', 'L_Lats_HJ_01'],

            ['Bip001-R-Clavicle', 'R_Traps_HJ_00'],
            ['Bip001-R-Clavicle', 'R_Traps_HJ_01'],
            ['Bip001-R-Clavicle', 'R_Pec_HJ_00'],
            ['Bip001-R-Clavicle', 'R_Pec_HJ_01'],
            ['Bip001-R-Clavicle', 'R_Lats_HJ_00'],
            ['Bip001-R-Clavicle', 'R_Lats_HJ_01'],


            ['Bip001-L-Thigh', 'L_Thigh'],
            ['Bip001-L-Calf', 'L_Knee'],
            ['Bip001-L-Calf', 'L_Shin'],
            ['Bip001-L-Foot', 'L_Foot'],
            #    ['Left toe','L_Instep'],
            ['Bip001-L-Toe0', 'L_Toe'],
            ['Bip001-L-Foot', 'L_Foot_HJ_00'],
            ['Bip001-L-Calf', 'L_Calf_HJ_00'],
            ['Bip001-L-Calf', 'L_Shin_HJ_00'],
            ['Bip001-L-Calf', 'L_Shin_HJ_01'],
            ['Bip001-L-Calf', 'L_Knee_HJ_00'],
            ['Bip001-L-Calf', 'L_KneeDouble_HJ_00'],
            ['Bip001-L-Calf', 'L_KneeRX_HJ_00'],
            ['Bip001-LThighTwist', 'L_ThighTwist_HJ_00'],
            ['Bip001-L-Thigh', 'L_ThighTwist_HJ_01'],
            ['Bip001-L-Calf', 'L_ThighTwist_HJ_02'],

            ['Bip001-R-Thigh', 'R_Thigh'],
            ['Bip001-R-Calf', 'R_Knee'],
            ['Bip001-R-Calf', 'R_Shin'],
            ['Bip001-R-Foot', 'R_Foot'],
            #    ['Right toe','R_Instep'],
            ['Bip001-R-Toe0', 'R_Toe'],
            ['Bip001-R-Foot', 'R_Foot_HJ_00'],
            ['Bip001-R-Calf', 'R_Calf_HJ_00'],
            ['Bip001-R-Calf', 'R_Shin_HJ_00'],
            ['Bip001-R-Calf', 'R_Shin_HJ_01'],
            ['Bip001-R-Calf', 'R_Knee_HJ_00'],
            ['Bip001-R-Calf', 'R_KneeDouble_HJ_00'],
            ['Bip001-R-Calf', 'R_KneeRX_HJ_00'],
            ['Bip001-RThighTwist', 'R_ThighTwist_HJ_00'],
            ['Bip001-R-Thigh', 'R_ThighTwist_HJ_01'],
            ['Bip001-R-Calf', 'R_ThighTwist_HJ_02'],

            ['Bip001-L-Thigh', 'L_ThighRZ_HJ_00'],
            ['Bip001-L-Thigh', 'L_ThighRZ_HJ_01'],
            ['Bip001-R-Thigh', 'R_ThighRZ_HJ_00'],
            ['Bip001-R-Thigh', 'R_ThighRZ_HJ_01'],
            ['Bip001-L-Thigh', 'L_Hip_HJ_00'],
            ['Bip001-L-Thigh', 'L_Hip_HJ_01'],
            ['Bip001-R-Thigh', 'R_Hip_HJ_00'],
            ['Bip001-R-Thigh', 'R_Hip_HJ_01'],
            ['Bip001-L-Thigh', 'L_ThighRX_HJ_00'],
            ['Bip001-L-Thigh', 'L_ThighRX_HJ_01'],
            ['Bip001-R-Thigh', 'R_ThighRX_HJ_00'],
            ['Bip001-R-Thigh', 'R_ThighRX_HJ_01'],


        ]
        
rename_vg_fixed_name_list = [
            ['Bip001-Pelvis', 'Hip_HJ_00'],
            ['Bip001-Spine', 'Spine_0_HJ_00'],
            ['Bip001-Spine1', 'Spine_1_HJ_00'],
            ['Bip001-Spine2', 'Spine_2_HJ_00'],
            ['Bip001-Neck', 'Neck_0_HJ_00'],
            ['Bip001-Head', 'Head'],

            ['Bip001-L-Clavicle', 'L_Shoulder_HJ_00'],
            ['Bip001-L-UpperArm', 'L_UpperArmTwist_HJ_01'],
            ['Bip001-L-Forearm', 'L_ForearmTwist_HJ_00'],
            ['Bip001-L-Hand', 'L_Hand'],
            ['Bip001-L-Finger0', 'L_Thumb1'],
            ['Bip001-L-Finger01', 'L_Thumb2'],
            ['Bip001-L-Finger02', 'L_Thumb3'],
            ['Bip001-L-Finger1', 'L_IndexF1'],
            ['Bip001-L-Finger11', 'L_IndexF2'],
            ['Bip001-L-Finger12', 'L_IndexF3'],
            ['Bip001-L-Finger2', 'L_MiddleF1'],
            ['Bip001-L-Finger21', 'L_MiddleF2'],
            ['Bip001-L-Finger22', 'L_MiddleF3'],
            ['自定义L', 'L_Palm'],
            ['Bip001-L-Finger3', 'L_RingF1'],
            ['Bip001-L-Finger31', 'L_RingF2'],
            ['Bip001-L-Finger32', 'L_RingF3'],
            ['Bip001-L-Finger4', 'L_PinkyF1'],
            ['Bip001-L-Finger41', 'L_PinkyF2'],
            ['Bip001-L-Finger42', 'L_PinkyF3'],

            ['Bip001-R-Clavicle', 'R_Shoulder_HJ_00'],
            ['Bip001-R-UpperArm', 'R_UpperArmTwist_HJ_01'],
            ['Bip001-R-Forearm', 'R_ForearmTwist_HJ_00'],
            ['Bip001-R-Hand', 'R_Hand'],
            ['Bip001-R-Finger0', 'R_Thumb1'],
            ['Bip001-R-Finger01', 'R_Thumb2'],
            ['Bip001-R-Finger02', 'R_Thumb3'],
            ['Bip001-R-Finger1', 'R_IndexF1'],
            ['Bip001-R-Finger11', 'R_IndexF2'],
            ['Bip001-R-Finger12', 'R_IndexF3'],
            ['Bip001-R-Finger2', 'R_MiddleF1'],
            ['Bip001-R-Finger21', 'R_MiddleF2'],
            ['Bip001-R-Finger22', 'R_MiddleF3'],
            ['自定义R', 'R_Palm'],
            ['Bip001-R-Finger3', 'R_RingF1'],
            ['Bip001-R-Finger31', 'R_RingF2'],
            ['Bip001-R-Finger32', 'R_RingF3'],
            ['Bip001-R-Finger4', 'R_PinkyF1'],
            ['Bip001-R-Finger41', 'R_PinkyF2'],
            ['Bip001-R-Finger42', 'R_PinkyF3'],

            ['Bip001-L-Thigh', 'L_Thigh'],
            ['Bip001-L-Calf', 'L_Shin'],
            ['Bip001-L-Foot', 'L_Foot'],
            ['Bip001-L-Toe0', 'L_Toe'],

            ['Bip001-R-Thigh', 'R_Thigh'],
            ['Bip001-R-Calf', 'R_Shin'],
            ['Bip001-R-Foot', 'R_Foot'],
            ['Bip001-R-Toe0', 'R_Toe'],

            ['+ElbowAux_L', 'L_Elbow_HJ_00'],
            ['ElbowAux_L', 'L_Elbow_HJ_00'],
            ['Bone_UpArmTwist_l', 'L_Deltoid_HJ_00'],
            ['Bip001-L-ForeTwist1', 'L_ForearmTwist_HJ_02'],
            ['Bip001-LThighTwist', 'L_ThighTwist_HJ_00'],

            ['+ElbowAux_R', 'R_Elbow_HJ_00'],
            ['ElbowAux_R', 'R_Elbow_HJ_00'],
            ['Bone_UpArmTwist_r', 'R_Deltoid_HJ_00'],
            ['Bip001-R-ForeTwist1', 'R_ForearmTwist_HJ_02'],
            ['Bip001-RThighTwist', 'R_ThighTwist_HJ_00'],

            ['OhButt_L', 'L_Hip_HJ_01'],
            ['+KneeAux_L', 'L_Knee_HJ_00'],
            ['KneeAux_L', 'L_Knee_HJ_00'],

            ['OhButt_R', 'R_Hip_HJ_01'],
            ['+KneeAux_R', 'R_Knee_HJ_00'],
            ['KneeAux_R', 'R_Knee_HJ_00'],
        ]