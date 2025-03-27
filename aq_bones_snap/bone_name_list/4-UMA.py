# 编写字典时最好按照骨骼层级的顺序来编写，简单来说就是胯到胸到头，左臂到左手，右臂到右手，左腿到左脚，右腿到右脚。
# 注意，请确保rename_vg_fixed_name_list字典中的前6个骨骼名，普遍都存在于该字典对应的一类外部骨架中，插件会用于判定选择的字典是否匹配当前选中的外部骨架。

snap_bone_fixed_name_list = [
            ['Hip', 'Hip'],
            ['Waist', 'Spine_0'],
            ['Spine', 'Spine_1'],
            ['Chest', 'Spine_2'],
            ['Neck', 'Neck_0'],
            ['Neck', 'Neck_0_HJ_00'],

            # ['Head', 'Head'],

            ['Shoulder_L', 'L_Shoulder'],
            ['ShoulderRoll_L', 'L_UpperArm'],
            ['Elbow_L', 'L_Forearm'],
            ['Wrist_L', 'L_Hand'],
            ['Wrist_L', 'L_Wep'],

            ['Thumb_01_L', 'L_Thumb1'],
            ['Thumb_02_L', 'L_Thumb2'],
            ['Thumb_03_L', 'L_Thumb3'],

            ['Thumb_01_L', 'L_Thumb_HJ_00'],
            ['Thumb_02_L', 'L_Thumb_HJ_01'],
            ['Thumb_03_L', 'L_Thumb_HJ_02'],
            ['Thumb_01_L', 'L_Thumb_HJ_03'],

            ['Index_01_L', 'L_IndexF1'],
            ['Index_02_L', 'L_IndexF2'],
            ['Index_03_L', 'L_IndexF3'],

            ['Index_01_L', 'L_IndexF_HJ_01'],
            ['Index_02_L', 'L_IndexF_HJ_02'],
            ['Index_03_L', 'L_IndexF_HJ_03'],
            ['Index_01_L', 'L_IndexF_HJ_00'],
            ['Index_01_L', 'L_IndexF_HJ_04'],

            ['Middle_01_L', 'L_MiddleF1'],
            ['Middle_02_L', 'L_MiddleF2'],
            ['Middle_03_L', 'L_MiddleF3'],

            ['Middle_01_L', 'L_MiddleF_HJ_01'],
            ['Middle_02_L', 'L_MiddleF_HJ_02'],
            ['Middle_03_L', 'L_MiddleF_HJ_03'],
            ['Middle_01_L', 'L_MiddleF_HJ_00'],
            ['Middle_01_L', 'L_MiddleF_HJ_04'],

            ['Wrist_L', 'L_Palm'],

            ['Ring_01_L', 'L_RingF1'],
            ['Ring_02_L', 'L_RingF2'],
            ['Ring_03_L', 'L_RingF3'],

            ['Ring_01_L', 'L_RingF_HJ_01'],
            ['Ring_02_L', 'L_RingF_HJ_02'],
            ['Ring_03_L', 'L_RingF_HJ_03'],
            ['Ring_01_L', 'L_RingF_HJ_00'],
            ['Ring_01_L', 'L_RingF_HJ_04'],

            ['Pinky_01_L', 'L_PinkyF1'],
            ['Pinky_02_L', 'L_PinkyF2'],
            ['Pinky_03_L', 'L_PinkyF3'],

            ['Pinky_01_L', 'L_PinkyF_HJ_01'],
            ['Pinky_02_L', 'L_PinkyF_HJ_02'],
            ['Pinky_03_L', 'L_PinkyF_HJ_03'],
            ['Pinky_01_L', 'L_PinkyF_HJ_00'],
            ['Pinky_01_L', 'L_PinkyF_HJ_04'],

            ['Wrist_L', 'L_HandRZ_HJ_00'],
            ['Wrist_L', 'L_Hand_HJ_01'],
            ['Wrist_L', 'L_Wep_Sub'],
            ['Wrist_L', 'L_Hand_HJ_00'],

            ['ArmRoll_L', 'L_ForearmTwist_HJ_02'],
            ['Elbow_L', 'L_ForearmRY_HJ_00'],
            ['Elbow_L', 'L_ForearmRY_HJ_01'],
            ['ArmRoll_L', 'L_ForearmTwist_HJ_01'],
            ['Elbow_L', 'L_ForearmTwist_HJ_00'],
            ['Elbow_L', 'L_Forearm_HJ_00'],
            ['Elbow_L', 'L_Elbow_HJ_00'],

            ['ShoulderRoll_L', 'L_UpperArmTwist_HJ_00'],

            ['Arm_L', 'L_UpperArmTwist_HJ_01'],
            ['Arm_L', 'L_Triceps_HJ_00'],
            ['Arm_L', 'L_Biceps_HJ_00'],
            ['Arm_L', 'L_Biceps_HJ_01'],
            ['Arm_L', 'L_UpperArmTwist_HJ_02'],

            ['Elbow_L', 'L_ForearmDouble_HJ_00'],
            ['ShoulderRoll_L', 'L_UpperArm_HJ_00'],
            ['ShoulderRoll_L', 'L_Deltoid_HJ_00'],
            ['ShoulderRoll_L', 'L_Deltoid_HJ_01'],
            ['ShoulderRoll_L', 'L_Deltoid_HJ_02'],
            ['ShoulderRoll_L', 'L_UpperArmDouble_HJ_00'],

            ['Shoulder_L', 'L_Shoulder_HJ_00'],

            ['Shoulder_R', 'R_Shoulder'],
            ['ShoulderRoll_R', 'R_UpperArm'],
            ['Elbow_R', 'R_Forearm'],
            ['Wrist_R', 'R_Hand'],
            ['Wrist_R', 'R_Wep'],

            ['Thumb_01_R', 'R_Thumb1'],
            ['Thumb_02_R', 'R_Thumb2'],
            ['Thumb_03_R', 'R_Thumb3'],

            ['Thumb_01_R', 'R_Thumb_HJ_00'],
            ['Thumb_02_R', 'R_Thumb_HJ_01'],
            ['Thumb_03_R', 'R_Thumb_HJ_02'],
            ['Thumb_01_R', 'R_Thumb_HJ_03'],

            ['Index_01_R', 'R_IndexF1'],
            ['Index_02_R', 'R_IndexF2'],
            ['Index_03_R', 'R_IndexF3'],

            ['Index_01_R', 'R_IndexF_HJ_01'],
            ['Index_02_R', 'R_IndexF_HJ_02'],
            ['Index_03_R', 'R_IndexF_HJ_03'],
            ['Index_01_R', 'R_IndexF_HJ_00'],
            ['Index_01_R', 'R_IndexF_HJ_04'],

            ['Middle_01_R', 'R_MiddleF1'],
            ['Middle_02_R', 'R_MiddleF2'],
            ['Middle_03_R', 'R_MiddleF3'],

            ['Middle_01_R', 'R_MiddleF_HJ_01'],
            ['Middle_02_R', 'R_MiddleF_HJ_02'],
            ['Middle_03_R', 'R_MiddleF_HJ_03'],
            ['Middle_01_R', 'R_MiddleF_HJ_00'],
            ['Middle_01_R', 'R_MiddleF_HJ_04'],

            ['Wrist_R', 'R_Palm'],

            ['Ring_01_R', 'R_RingF1'],
            ['Ring_02_R', 'R_RingF2'],
            ['Ring_03_R', 'R_RingF3'],

            ['Ring_01_R', 'R_RingF_HJ_01'],
            ['Ring_02_R', 'R_RingF_HJ_02'],
            ['Ring_03_R', 'R_RingF_HJ_03'],
            ['Ring_01_R', 'R_RingF_HJ_00'],
            ['Ring_01_R', 'R_RingF_HJ_04'],

            ['Pinky_01_R', 'R_PinkyF1'],
            ['Pinky_02_R', 'R_PinkyF2'],
            ['Pinky_03_R', 'R_PinkyF3'],

            ['Pinky_01_R', 'R_PinkyF_HJ_01'],
            ['Pinky_02_R', 'R_PinkyF_HJ_02'],
            ['Pinky_03_R', 'R_PinkyF_HJ_03'],
            ['Pinky_01_R', 'R_PinkyF_HJ_00'],
            ['Pinky_01_R', 'R_PinkyF_HJ_04'],

            ['Wrist_R', 'R_HandRZ_HJ_00'],
            ['Wrist_R', 'R_Hand_HJ_01'],
            ['Wrist_R', 'R_Wep_Sub'],
            ['Wrist_R', 'R_Hand_HJ_00'],

            ['ArmRoll_R', 'R_ForearmTwist_HJ_02'],
            ['Elbow_R', 'R_ForearmRY_HJ_00'],
            ['Elbow_R', 'R_ForearmRY_HJ_01'],
            ['ArmRoll_R', 'R_ForearmTwist_HJ_01'],
            ['Elbow_R', 'R_ForearmTwist_HJ_00'],
            ['Elbow_R', 'R_Shield'],
            ['Elbow_R', 'R_Forearm_HJ_00'],
            ['Elbow_R', 'R_Elbow_HJ_00'],

            ['ShoulderRoll_R', 'R_UpperArmTwist_HJ_00'],

            ['Arm_R', 'R_UpperArmTwist_HJ_01'],
            ['Arm_R', 'R_Triceps_HJ_00'],
            ['Arm_R', 'R_Biceps_HJ_00'],
            ['Arm_R', 'R_Biceps_HJ_01'],
            ['Arm_R', 'R_UpperArmTwist_HJ_02'],

            ['Elbow_R', 'R_ForearmDouble_HJ_00'],
            ['ShoulderRoll_R', 'R_UpperArm_HJ_00'],
            ['ShoulderRoll_R', 'R_Deltoid_HJ_00'],
            ['ShoulderRoll_R', 'R_Deltoid_HJ_01'],
            ['ShoulderRoll_R', 'R_Deltoid_HJ_02'],
            ['ShoulderRoll_R', 'R_UpperArmDouble_HJ_00'],

            ['Shoulder_R', 'R_Shoulder_HJ_00'],

            ['Shoulder_L', 'L_Traps_HJ_00'],
            ['Shoulder_L', 'L_Traps_HJ_01'],
            ['Shoulder_L', 'L_Pec_HJ_00'],
            ['Shoulder_L', 'L_Pec_HJ_01'],
            ['Shoulder_L', 'L_Lats_HJ_00'],
            ['Shoulder_L', 'L_Lats_HJ_01'],

            ['Shoulder_R', 'R_Traps_HJ_00'],
            ['Shoulder_R', 'R_Traps_HJ_01'],
            ['Shoulder_R', 'R_Pec_HJ_00'],
            ['Shoulder_R', 'R_Pec_HJ_01'],
            ['Shoulder_R', 'R_Lats_HJ_00'],
            ['Shoulder_R', 'R_Lats_HJ_01'],

            ['Chest', 'Spine_2_HJ_00'],

            #    ['','R_Bust_HJ_00'],
            #    ['','R_Bust_HJ_01'],
            #    ['','L_Bust_HJ_00'],
            #    ['','L_Bust_HJ_01'],

            ['Spine', 'Spine_1_HJ_00'],
            ['Waist', 'Spine_0_HJ_00'],

            ['Thigh_L', 'L_Thigh'],
            ['Knee_L', 'L_Knee'],
            ['Knee_L', 'L_Shin'],
            ['Ankle_offset_L', 'L_Foot'],

            ['Toe_offset_L', 'L_Toe'],
            ['Ankle_offset_L', 'L_Foot_HJ_00'],
            ['Knee_L', 'L_Calf_HJ_00'],
            ['Knee_L', 'L_Shin_HJ_00'],
            ['Knee_L', 'L_Shin_HJ_01'],
            ['Knee_L', 'L_Knee_HJ_00'],
            ['Knee_L', 'L_KneeDouble_HJ_00'],
            ['Knee_L', 'L_KneeRX_HJ_00'],
            ['Thigh_L', 'L_ThighTwist_HJ_00'],
            ['Thigh_L', 'L_ThighTwist_HJ_01'],
            ['Knee_L', 'L_ThighTwist_HJ_02'],

            ['Thigh_R', 'R_Thigh'],
            ['Knee_R', 'R_Knee'],
            ['Knee_R', 'R_Shin'],
            ['Ankle_offset_R', 'R_Foot'],

            ['Toe_offset_R', 'R_Toe'],
            ['Ankle_offset_R', 'R_Foot_HJ_00'],
            ['Knee_R', 'R_Calf_HJ_00'],
            ['Knee_R', 'R_Shin_HJ_00'],
            ['Knee_R', 'R_Shin_HJ_01'],
            ['Knee_R', 'R_Knee_HJ_00'],
            ['Knee_R', 'R_KneeDouble_HJ_00'],
            ['Knee_R', 'R_KneeRX_HJ_00'],
            ['Thigh_R', 'R_ThighTwist_HJ_00'],
            ['Thigh_R', 'R_ThighTwist_HJ_01'],
            ['Knee_R', 'R_ThighTwist_HJ_02'],

            ['Thigh_L', 'L_ThighRZ_HJ_00'],
            ['Thigh_L', 'L_ThighRZ_HJ_01'],
            ['Thigh_R', 'R_ThighRZ_HJ_00'],
            ['Thigh_R', 'R_ThighRZ_HJ_01'],
            ['Thigh_L', 'L_Hip_HJ_00'],
            ['Thigh_L', 'L_Hip_HJ_01'],
            ['Thigh_R', 'R_Hip_HJ_00'],
            ['Thigh_R', 'R_Hip_HJ_01'],
            ['Thigh_L', 'L_ThighRX_HJ_00'],
            ['Thigh_L', 'L_ThighRX_HJ_01'],
            ['Thigh_R', 'R_ThighRX_HJ_00'],
            ['Thigh_R', 'R_ThighRX_HJ_01'],

            ['Hip', 'Hip_HJ_00'],
        ]
        
rename_vg_fixed_name_list = [
            ['Hip', 'Hip_HJ_00'],
            ['Waist', 'Spine_0_HJ_00'],
            ['Spine', 'Spine_1_HJ_00'],
            ['Chest', 'Spine_2_HJ_00'],
            ['Neck', 'Neck_0_HJ_00'],
            ['Head', 'Head'],

            ['Shoulder_L', 'L_Shoulder_HJ_00'],
            ['Arm_L', 'L_UpperArmTwist_HJ_01'],
            ['Elbow_L', 'L_ForearmTwist_HJ_00'],
            ['Wrist_L', 'L_Hand'],
            ['Thumb_01_L', 'L_Thumb1'],
            ['Thumb_02_L', 'L_Thumb2'],
            ['Thumb_03_L', 'L_Thumb3'],
            ['Index_01_L', 'L_IndexF1'],
            ['Index_02_L', 'L_IndexF2'],
            ['Index_03_L', 'L_IndexF3'],
            ['Middle_01_L', 'L_MiddleF1'],
            ['Middle_02_L', 'L_MiddleF2'],
            ['Middle_03_L', 'L_MiddleF3'],

            ['Ring_01_L', 'L_RingF1'],
            ['Ring_02_L', 'L_RingF2'],
            ['Ring_03_L', 'L_RingF3'],
            ['Pinky_01_L', 'L_PinkyF1'],
            ['Pinky_02_L', 'L_PinkyF2'],
            ['Pinky_03_L', 'L_PinkyF3'],

            ['Shoulder_R', 'R_Shoulder_HJ_00'],
            ['Arm_R', 'R_UpperArmTwist_HJ_01'],
            ['Elbow_R', 'R_ForearmTwist_HJ_00'],
            ['Wrist_R', 'R_Hand'],
            ['Thumb_01_R', 'R_Thumb1'],
            ['Thumb_02_R', 'R_Thumb2'],
            ['Thumb_03_R', 'R_Thumb3'],
            ['Index_01_R', 'R_IndexF1'],
            ['Index_02_R', 'R_IndexF2'],
            ['Index_03_R', 'R_IndexF3'],
            ['Middle_01_R', 'R_MiddleF1'],
            ['Middle_02_R', 'R_MiddleF2'],
            ['Middle_03_R', 'R_MiddleF3'],

            ['Ring_01_R', 'R_RingF1'],
            ['Ring_02_R', 'R_RingF2'],
            ['Ring_03_R', 'R_RingF3'],
            ['Pinky_01_R', 'R_PinkyF1'],
            ['Pinky_02_R', 'R_PinkyF2'],
            ['Pinky_03_R', 'R_PinkyF3'],

            ['Thigh_L', 'L_Thigh'],
            ['Knee_L', 'L_Shin'],
            ['Ankle_offset_L', 'L_Foot'],
            ['Toe_offset_L', 'L_Toe'],

            ['Thigh_R', 'R_Thigh'],
            ['Knee_R', 'R_Shin'],
            ['Ankle_offset_R', 'R_Foot'],
            ['Toe_offset_R', 'R_Toe'],


            ['ShoulderRoll_L', 'L_Deltoid_HJ_00'],
            ['ArmRoll_L', 'L_ForearmTwist_HJ_02'],


            ['ShoulderRoll_R', 'R_Deltoid_HJ_00'],
            ['ArmRoll_R', 'R_ForearmTwist_HJ_02'],
        ]