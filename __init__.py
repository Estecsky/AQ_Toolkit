import bpy
from bpy.props import PointerProperty, BoolProperty
from .AQ_property import AQ_CusProperty
from . import (
    AQ_Toolkit_ops,
    AQ_panel,
    AQ_Batch_img_load,
    AQ_property,
    AQ_HellDivers2_ExpandTool,
    AQ_Prefs,
)


bl_info = {
    "name": "AQ_Toolkit",
    "description": "为blender定制的个人工具箱",
    "blender": (4, 0, 0),
    "location": "3D 视图 > 侧边栏 | 着色器编辑器 > 侧边栏 > 工具",  # 插件显示的位置
    "category": "3D View",
    "version": (0, 7, 0),
    "doc_url": "https://github.com/Estecsky/AQ_Toolkit",
}

# Reloads the addons on script reload
# Good for editing script
if "bpy" in locals():
    import importlib

    if "AQ_Toolkit_ops" in locals():
        importlib.reload(AQ_Toolkit_ops)
    if "AQ_property" in locals():
        importlib.reload(AQ_property)
    if "AQ_panel" in locals():
        importlib.reload(AQ_panel)
    if "AQ_Batch_img_load" in locals():
        importlib.reload(AQ_Batch_img_load)
    if "AQ_HellDivers2_ExpandTool" in locals():
        importlib.reload(AQ_HellDivers2_ExpandTool)
    if "AQ_Prefs" in locals():
        importlib.reload(AQ_Prefs)


def register():

    bpy.utils.register_class(AQ_CusProperty)
    bpy.types.Scene.AQ_Props = PointerProperty(type=AQ_CusProperty)
    AQ_Toolkit_ops.register()
    AQ_panel.register()
    AQ_Batch_img_load.register()
    AQ_HellDivers2_ExpandTool.register()
    AQ_Prefs.register()


def unregister():
    AQ_Toolkit_ops.unregister()
    AQ_panel.unregister()
    AQ_Batch_img_load.unregister()
    AQ_HellDivers2_ExpandTool.unregister()
    bpy.utils.unregister_class(AQ_CusProperty)
    del bpy.types.Scene.AQ_Props
    AQ_Prefs.unregister()


if __name__ == "__main__":
    register()
    # unregister()
