import bpy
import os
import importlib

# =======================
# HellDivers2 ExpandTool可选组件
# =======================

def reload_armor_dict():
    global armor_target_list
    global target_dict
    armor_target_list = []
    ID_module = importlib.import_module("..HD2_ArmorID.AQ_HellDivers2_ArmorID", package=__name__)
    if "ID_module" in locals():
        importlib.reload(ID_module)
        
    target_dict = ID_module.armor_dict
    for target_name in target_dict.keys():
        if 'A_need_fix' in target_dict[target_name].keys():
            continue
        armor_target_list.append((target_name, target_name,""))
    
    return armor_target_list

def reload_armor_dict_single():
    global armor_target_list
    global target_dict_single
    armor_target_list = []
    ID_module = importlib.import_module("..HD2_ArmorID.AQ_HellDivers2_ArmorID_single", package=__name__)
    if "ID_module" in locals():
        importlib.reload(ID_module)
        
    target_dict_single = ID_module.armor_dict
    for target_name in target_dict_single.keys():
        if 'A_need_fix' in target_dict_single[target_name].keys():
            continue
        armor_target_list.append((target_name, target_name,""))
    
    return armor_target_list

def clear_all_swaps_id(obj):
    SwapID_keys_id = [int(key.split("_")[-1]) for key in obj.keys() if key.startswith("Z_SwapID_")]
    if len(SwapID_keys_id) != 0:
        SwapID_keys_id.sort()
        for index in SwapID_keys_id:
            obj[f"Z_SwapID_{index}"] = ""
            
def aq_part_swap(obj,swap_list):
    swap_part_count = 0
    list_index = 0
    SwapID_keys_id = [int(key.split("_")[-1]) for key in obj.keys() if key.startswith("Z_SwapID_")]
    if len(SwapID_keys_id) != 0:
        SwapID_keys_id.sort()
        for index in SwapID_keys_id:
            list_index += 1
            if obj[f"Z_SwapID_{index}"] == "":
                swap_part_count = index
                break

        if list_index == len(SwapID_keys_id):
            swap_part_count = SwapID_keys_id[-1] + 1
            
    for swap_id in swap_list:        
        obj[f"Z_SwapID_{swap_part_count}"] = str(swap_id).replace(" ","")
        swap_part_count += 1

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

class ButtonSetHD2_Part(bpy.types.Operator):
    bl_idname = "object.set_aq_hd2_part"
    bl_label = "标记为HD2部位属性"
    bl_description = "将所选物体标记为HD2部位"
    bl_options = {"REGISTER", "UNDO"}
    
    part_name: bpy.props.EnumProperty(
        name="部件名称",
        description="HD2部件名称",
        items=(
            ("Head", "头部", ""),
            ("Chest", "胸部", ""),
            ("Chest_Armor", "胸部护甲", ""),
            ("Left_Arm", "左臂", ""),
            ("Right_Arm", "右臂", ""),
            ("Hip", "臀部", ""),
            ("Left_Leg", "左腿", ""),
            ("Right_Leg", "右腿", ""),
        )
    )
    
    @classmethod
    def poll(cls, context):
        if context.active_object is None:
            return False
        obj = bpy.context.active_object
        try:
            ObjectID = obj["Z_ObjectID"]
            if obj.type == "MESH" and ObjectID != "":
                return True
            else:
                return False
            
        except KeyError:
            return False
        
    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == "MESH":
                if self.part_name == "Head":
                    obj["AQ_HD2_Part"] = "Head"
                elif self.part_name == "Left_Leg":
                    obj["AQ_HD2_Part"] = "Left_Leg"
                elif self.part_name == "Right_Leg":
                    obj["AQ_HD2_Part"] = "Right_Leg"
                elif self.part_name == "Chest":
                    obj["AQ_HD2_Part"] = "Chest"
                elif self.part_name == "Chest_Armor":
                    obj["AQ_HD2_Part"] = "Chest_Armor"
                elif self.part_name == "Hip":
                    obj["AQ_HD2_Part"] = "Hip"
                elif self.part_name == "Left_Arm":
                    obj["AQ_HD2_Part"] = "Left_Arm"
                elif self.part_name == "Right_Arm":
                    obj["AQ_HD2_Part"] = "Right_Arm"
        self.report({"INFO"}, f"已将所选{len(selected_objects)}个物体标记为{self.part_name}")
        return {"FINISHED"}

class ButtonSetHD2_Part_Type(bpy.types.Operator):
    bl_idname = "object.set_aq_hd2_part_type"
    bl_label = "标记为HD2部位属性"
    bl_description = "将所选物体标记为HD2部位属性"
    bl_options = {"REGISTER", "UNDO"}
    
    body_type: bpy.props.EnumProperty(
        name="体型",
        description="身体类型",
        # default="Slim",
        items=(
            ("Slim", "清瘦", ""),
            ("Stocky", "健壮", ""),
        ),
    )
    part_name: bpy.props.EnumProperty(
        name="部件名称",
        description="HD2部件名称",
        items=(
            ("Chest", "胸部", ""),
            ("Chest_Armor", "胸部护甲", ""),
            ("Hip", "臀部", ""),
            ("Left_Arm", "左臂", ""),
            ("Right_Arm", "右臂", ""),
        )
    )
    
    @classmethod
    def poll(cls, context):
        if context.active_object is None:
            return False
        obj = bpy.context.active_object
        try:
            ObjectID = obj["Z_ObjectID"]
            if obj.type == "MESH" and ObjectID != "":
                return True
            else:
                return False
            
        except KeyError:
            return False
        
    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        for obj in selected_objects:
            if obj.type == "MESH":
                if self.part_name == "Chest":
                    obj["AQ_HD2_Part"] = f"Chest_{self.body_type}"
                elif self.part_name == "Chest_Armor":
                    obj["AQ_HD2_Part"] = f"Chest_Armor_{self.body_type}"
                elif self.part_name == "Hip":
                    obj["AQ_HD2_Part"] = f"Hip_{self.body_type}"
                elif self.part_name == "Left_Arm":
                    obj["AQ_HD2_Part"] = f"Left_Arm_{self.body_type}"
                elif self.part_name == "Right_Arm":
                    obj["AQ_HD2_Part"] = f"Right_Arm_{self.body_type}"


        if self.body_type == "Slim":
            self.report({"INFO"}, f"已将所选{len(selected_objects)}个物体标记为{self.part_name}_{self.body_type}")
        else:
            self.report({"INFO"}, f"已将所选{len(selected_objects)}个物体标记为{self.part_name}_{self.body_type}")
        return {"FINISHED"}

    def draw(self, layout):
        layout = self.layout
        row = layout.row()
        row.prop(self, "body_type", text="体型")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class ButtonDeleteHD2_Part(bpy.types.Operator):
    bl_idname = "object.delete_aq_hd2_part"
    bl_label = "删除HD2部位属性"
    bl_description = "删除所选物体的HD2部位属性"
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        if context.active_object is None:
            return False
        obj = bpy.context.active_object
        try:
            ObjectID = obj["Z_ObjectID"]
            if obj.type == "MESH" and ObjectID != "":
                return True
            else:
                return False
            
        except KeyError:
            return False
        
    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        deleted_count = 0
        for obj in selected_objects:
            if obj.type == "MESH" and "AQ_HD2_Part" in obj.keys():
                del obj["AQ_HD2_Part"]
                deleted_count += 1
        self.report({"INFO"}, f"已删除{deleted_count}个物体的HD2部位属性")
        return {"FINISHED"}

class ButtonQuickSwapID_HD2(bpy.types.Operator):
    bl_idname = "object.quick_swap_id_hd2"
    bl_label = "HD2快速换ID"
    bl_description = "根据已标记的HD2部位属性，快速为所选物体的添加对应部位的转移ID"
    bl_options = {"REGISTER", "UNDO"}
    
    @classmethod
    def poll(cls, context):
        if context.active_object is None:
            return False
        obj = bpy.context.active_object
        try:
            ObjectID = obj["Z_ObjectID"]
            if obj.type == "MESH" and ObjectID != "":
                return True
            else:
                return False
            
        except KeyError:
            return False
        
    def execute(self, context):
        props = bpy.context.scene.AQ_Props
        enumValue = props.SwapIDTargetList
        if props.IgnoreArmorIDReuse:
            enumValue = props.SwapIDTargetList_single
        active_obj = bpy.context.active_object
        selected_objects = bpy.context.selected_objects
        
        if "AQ_HD2_Part" not in active_obj.keys():
            self.report({"ERROR"}, "请先标记HD2部位属性")
            return {"CANCELLED"}        
        
        swap_count = 0
        for obj in selected_objects:
            if obj.type == "MESH" and "AQ_HD2_Part" in obj.keys():
                if props.ClearPreviousSwapID:
                # 清除所有SwapID属性
                    clear_all_swaps_id(obj)
                
                AQ_HD2_Part = obj["AQ_HD2_Part"]
                if props.IgnoreArmorIDReuse:
                    target_part_dict = target_dict_single[enumValue]
                else:
                    target_part_dict = target_dict[enumValue]
                # 处理胸部与胸部护甲
                if "Chest" in AQ_HD2_Part:
                    if "Armor" in AQ_HD2_Part:
                        if "Chest_Armor" == AQ_HD2_Part:
                            chest_swap = target_part_dict["Chest_Armor_Slim"] + target_part_dict["Chest_Armor_Stocky"]
                            if chest_swap:
                                aq_part_swap(obj,chest_swap)
                            else:
                                self.report({"ERROR"}, "未找到胸部护甲的转移ID")
                                swap_count -= 1
                        else:
                            if target_part_dict[AQ_HD2_Part]:
                                aq_part_swap(obj,target_part_dict[AQ_HD2_Part])
                            else:
                                self.report({"ERROR"}, "未找到胸部护甲的转移ID")
                                swap_count -= 1
                    
                    else:
                        if "Chest" == AQ_HD2_Part:
                            chest_swap = target_part_dict["Chest_Slim"] + target_part_dict["Chest_Stocky"]
                            aq_part_swap(obj,chest_swap)
                        else:
                            aq_part_swap(obj,target_part_dict[AQ_HD2_Part])
                # 处理左臂
                elif "Left_Arm" in AQ_HD2_Part:
                    if "Left_Arm" == AQ_HD2_Part:
                        left_arm_swap = target_part_dict["Left_Arm_Slim"] + target_part_dict["Left_Arm_Stocky"]
                        aq_part_swap(obj,left_arm_swap)
                    else:
                        aq_part_swap(obj,target_part_dict[AQ_HD2_Part])
                # 处理右臂
                elif "Right_Arm" in AQ_HD2_Part:
                    if "Right_Arm" == AQ_HD2_Part:
                        right_arm_swap = target_part_dict["Right_Arm_Slim"] + target_part_dict["Right_Arm_Stocky"]
                        aq_part_swap(obj,right_arm_swap)
                    else:
                        aq_part_swap(obj,target_part_dict[AQ_HD2_Part])
                # 处理臀部
                elif "Hip" in AQ_HD2_Part:
                    if "Hip" == AQ_HD2_Part:
                        hip_swap = target_part_dict["Hip_Slim"] + target_part_dict["Hip_Stocky"]
                        aq_part_swap(obj,hip_swap)
                    else:
                        aq_part_swap(obj,target_part_dict[AQ_HD2_Part])
                else:
                    aq_part_swap(obj,target_part_dict[AQ_HD2_Part])
                
                
                swap_count += 1
            else:
                continue

        self.report({"INFO"}, f"已为所选{swap_count}个物体快速换ID到{enumValue}")
        
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
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="HD2部位标记", icon="GREASEPENCIL")
    row = layout.row()
    row.scale_y = 1.3
    row.prop(props, "IgnoreBodyType", text="忽略壮瘦区分")
    row = layout.row()
    row.scale_y = 1.3
    row.operator("object.set_aq_hd2_part", text="标记为头部", icon="GREASEPENCIL").part_name = "Head"
    if not props.IgnoreBodyType:
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part_type", text="标记为胸部", icon="BOOKMARKS").part_name = "Chest"
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part_type", text="标记为胸部护甲", icon="BOOKMARKS").part_name = "Chest_Armor"
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part_type", text="标记为左臂", icon="BOOKMARKS").part_name = "Left_Arm"
        row.operator("object.set_aq_hd2_part_type", text="标记为右臂", icon="BOOKMARKS").part_name = "Right_Arm"
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part_type", text="标记为臀部", icon="BOOKMARKS").part_name = "Hip"
    else:
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part", text="标记为胸部", icon="GREASEPENCIL").part_name = "Chest"
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part", text="标记为胸部护甲", icon="GREASEPENCIL").part_name = "Chest_Armor"
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part", text="标记为左臂", icon="GREASEPENCIL").part_name = "Left_Arm"
        row.operator("object.set_aq_hd2_part", text="标记为右臂", icon="GREASEPENCIL").part_name = "Right_Arm"
        row = layout.row()
        row.scale_y = 1.3
        row.operator("object.set_aq_hd2_part", text="标记为臀部", icon="GREASEPENCIL").part_name = "Hip"
    row = layout.row()
    row.scale_y = 1.3
    row.operator("object.set_aq_hd2_part", text="标记为左腿", icon="GREASEPENCIL").part_name = "Left_Leg"
    row.operator("object.set_aq_hd2_part", text="标记为右腿", icon="GREASEPENCIL").part_name = "Right_Leg"
    row = layout.row()
    row.scale_y = 1.3
    row.operator("object.delete_aq_hd2_part", text="删除HD2部位属性", icon="TRASH")
    row = layout.row()
    row.scale_y = 1
    row.label(text="HD2快速换ID", icon="SEQ_CHROMA_SCOPE")
    row = layout.row()
    row.scale_y = 1.3
    row.prop(props, "IgnoreArmorIDReuse", text="忽略护甲污染")
    if props.IgnoreArmorIDReuse:
        row = layout.row()
        row.scale_y = 1.4
        row.prop(props, "SwapIDTargetList_single")
    else:
        row = layout.row()
        row.scale_y = 1.4
        row.prop(props, "SwapIDTargetList")

    row = layout.row()
    row.scale_y = 1.1
    row.prop(props,"ClearPreviousSwapID",text ="清除先前存在的转移属性")
    row = layout.row()
    row.scale_y = 1.5
    row.operator("object.quick_swap_id_hd2", text="快速换ID", icon="SEQ_CHROMA_SCOPE")
    
register_class = [
    ButtonDeleteMutilationMesh,
    ButtonImportAvaterHelldiverRig,
    ButtonSetHD2_Part,
    ButtonSetHD2_Part_Type,
    ButtonDeleteHD2_Part,
    ButtonQuickSwapID_HD2,
]


def register():
    for cls in register_class:
        bpy.utils.register_class(cls)


def unregister():
    for cls in register_class:
        bpy.utils.unregister_class(cls)
