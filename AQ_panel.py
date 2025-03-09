import bpy
import webbrowser
from .AQ_Batch_img_load import BatchImgLoad, RemoveFilePath, ImportImgFilePath

from . import AQ_HellDivers2_ExpandTool
from . import AQ_MHWilds_ExpandTool
from .AQ_Prefs import AQ_PublicClass


class AQ_3DViewPanel(bpy.types.Panel):
    # 标签
    bl_order = 0
    bl_label = "AQの工具箱"
    bl_idname = "AQ_PT_Toolkit_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AQ_Toolkit"

    def draw(self, context):
        props = context.scene.AQ_Props
        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.scale_y = 0.5
        row.label(text="顶点断离:", icon="MESH_DATA")
        row = box.row(align=True)
        row.scale_y = 1.5
        row.operator("meshops.split_mesh_along_uvs", icon="UV", text="根据UV岛断离网格")

        row = box.row()
        row.scale_y = 0.5
        row.label(text="网格清理:", icon="MESH_DATA")
        row = box.row()
        row.scale_y = 1.0
        row.prop(props, "AQ_limitWeightValue", text="自定义权重限制值")
        row = box.row()
        row.scale_y = 1.5
        row.operator(
            "meshops.limit_and_normalize_weights",
            icon="MESH_DATA",
            text="限制并规范权重",
        )
        row = box.row()
        row.scale_y = 1.5
        row.operator(
            "meshops.delete_loose_edges_and_verts",
            icon="MESH_DATA",
            text="删除孤立边和顶点",
        )
        row = box.row()
        row.scale_y = 0.5
        row.label(text="网格编辑:", icon="MESH_DATA")
        row = box.row()
        row.scale_y = 1
        row.prop(props, "Auto_Xray_Shading", text="自动打开透视模式")
        row = box.row()
        row.scale_y = 1.5
        row.operator("objectops.reserved_one_face", icon="MESH_DATA", text="保留一个面")

        row = box.row()
        row.scale_y = 0.5
        row.label(text="常用工具:", icon="TOOL_SETTINGS")
        row = box.row()
        row.scale_y = 1.5
        row.operator(
            "meshops.select_0_weight_vertices", icon="VERTEXSEL", text="选择0权重顶点"
        )
        row = box.row()
        row.scale_y = 1.5
        row.operator("panel_ops.remove_empty", icon="GROUP_VERTEX", text="移除空顶点组")
        row = box.row()
        row.scale_y = 1.4
        row.operator("select.aq_select_seams", icon="EDGESEL", text="选中缝合边")
        row = box.row()
        row.scale_y = 1.4
        row.operator(
            "misremove_unused.ops_bones", icon="BONE_DATA", text="删除未使用的骨骼"
        )
        row = box.row()
        row.scale_y = 0.5
        row.label(text="顶点组权重合并:", icon="GROUP_VERTEX")
        row = box.row()
        row.scale_y = 1.0
        row.prop(props, "Comebine_vgroup_num", text="合并组的编号")
        row = box.row()
        row.scale_y = 1.4
        row.operator(
            "object.aq_combine_vertex_groups", icon="CHECKMARK", text="合并顶点组权重"
        )


class AQ_BatchLoadImgUI(bpy.types.Panel):
    # 标签
    bl_label = "AQの批量导入图片"  # 面板显示名称
    bl_idname = "AQ_PT_Batch_Img_Load"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout
        props = context.scene.AQ_Props
        box = layout.box()
        box.label(text="选择图片文件路径")
        box_row = box.row()
        box_row.operator(
            ImportImgFilePath.bl_idname, text="导入图片路径", icon="IMPORT"
        )
        box_row.operator(RemoveFilePath.bl_idname, text="", icon="TRASH")
        box.prop(props, "AQ_Batch_imgfile_path", text="路径", emboss=False)
        box.operator(
            BatchImgLoad.bl_idname, text="批量导入图片", icon="SEQ_CHROMA_SCOPE"
        )


class AQ_Toolkit_ExpandTools(bpy.types.Panel):
    global HD2_ExpandToolSwitch
    bl_order = 50
    bl_label = "拓展工具"
    bl_idname = "AQ_PT_Toolkit_ExpandTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AQ_Toolkit"
    # bl_options = {"DEFAULT_CLOSED"}

    # @classmethod
    # def poll(cls, context):
    #     return context.scene.expand_tools

    def draw(self, context):

        # =================================
        # 获取插件Prefs
        # =================================
        try:
            addon_prefs = AQ_PublicClass.get_addon_prefs()
            # 添加后续工具开关
            HD2_ExpandToolSwitch = addon_prefs.HD2ExpandTool
            MHWilds_ExpandToolSwitch = addon_prefs.MHWildsExpandTool
        except AttributeError as err:
            HD2_ExpandToolSwitch = True
            print(err)
            print("没有找到插件偏好设置")
        Expandlist = [HD2_ExpandToolSwitch, MHWilds_ExpandToolSwitch]
        # =======================
        # 绘制
        # =======================
        layout = self.layout
        box = layout.box()
        if any(Expandlist):
            if HD2_ExpandToolSwitch:
                AQ_HellDivers2_ExpandTool.ExpandPanel(box)
            if MHWilds_ExpandToolSwitch:
                AQ_MHWilds_ExpandTool.ExpandPanel(box)
        # if  某开关：
        #     绘制某工具面板函数
        else:
            box.label(text="没有启用任何拓展工具，在插件偏好设置中开启")


class AQ_Toolkit_Credits(bpy.types.Panel):
    bl_order = 99
    bl_label = "作者"
    bl_idname = "AQ_PT_Toolkit_Credits"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AQ_Toolkit"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="作者：AQ_Echoo")
        col = box.column(align=True)
        col.operator(ButtonAQGitHub.bl_idname, text="GitHub", icon="URL")
        col.operator(ButtonAQBilibili.bl_idname, text="Bilibili", icon="URL")


class ButtonAQGitHub(bpy.types.Operator):
    bl_idname = "aq_web.githubweb"
    bl_label = "GitHub"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        webbrowser.open("https://github.com/Estecsky/AQ_Toolkit")
        return {"FINISHED"}


class ButtonAQBilibili(bpy.types.Operator):
    bl_idname = "aq_web.bilibiliweb"
    bl_label = "Bilibili"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        webbrowser.open("https://space.bilibili.com/3493298962434150")
        return {"FINISHED"}


def register():
    bpy.utils.register_class(AQ_3DViewPanel)
    bpy.utils.register_class(AQ_BatchLoadImgUI)
    bpy.utils.register_class(AQ_Toolkit_ExpandTools)
    bpy.utils.register_class(AQ_Toolkit_Credits)
    bpy.utils.register_class(ButtonAQGitHub)
    bpy.utils.register_class(ButtonAQBilibili)


def unregister():
    bpy.utils.unregister_class(AQ_3DViewPanel)
    bpy.utils.unregister_class(AQ_BatchLoadImgUI)
    bpy.utils.unregister_class(AQ_Toolkit_ExpandTools)
    bpy.utils.unregister_class(AQ_Toolkit_Credits)
    bpy.utils.unregister_class(ButtonAQGitHub)
    bpy.utils.unregister_class(ButtonAQBilibili)
