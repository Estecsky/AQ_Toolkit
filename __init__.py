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
    addonPreferences,
    AQ_MHWilds_ExpandTool,
)
from . import addon_updater_ops
from .additional_addons import (
    register as register_additional_addons,
    unregister as unregister_additional_addons,
)
from .aq_bones_snap import snap_ops

bl_info = {
    "name": "AQ_Toolkit",
    "description": "为blender定制的个人工具箱",
    "author": "AQ_Echoo",
    "blender": (4, 0, 0),
    "location": "3D 视图 > 侧边栏 | 着色器编辑器 > 侧边栏 > 工具",
    "category": "3D View",
    "version": (1, 2, 0),
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
    if "addonPreferences" in locals():
        importlib.reload(addonPreferences)
    if "addon_updater_ops" in locals():
        importlib.reload(addon_updater_ops)
    if "AQ_MHWilds_ExpandTool" in locals():
        importlib.reload(AQ_MHWilds_ExpandTool)
        
def show_addon_version(bl_info = bl_info ):
    addon_version =  str(bl_info['version'][0])+"."+str(bl_info['version'][1])+"."+str(bl_info['version'][2])
    return addon_version


class AQ_3DViewPanel(bpy.types.Panel):
    # 标签
    bl_order = 0
    bl_label = f"AQの工具箱 V{show_addon_version()}"
    bl_idname = "AQ_PT_Toolkit_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AQ_Toolkit"

    def draw(self, context):
        AQ_panel.drawAQ_3DViewPanel(self.layout)
        

def register():
    
    bpy.utils.register_class(AQ_3DViewPanel)
    bpy.utils.register_class(AQ_CusProperty)
    bpy.types.Scene.AQ_Props = PointerProperty(type=AQ_CusProperty)
    AQ_Toolkit_ops.register()
    AQ_panel.register()
    AQ_Batch_img_load.register()
    AQ_HellDivers2_ExpandTool.register()
    AQ_MHWilds_ExpandTool.register()
    addonPreferences.register()
    addon_updater_ops.register(bl_info)
    register_additional_addons()
    snap_ops.register()


def unregister():
    bpy.utils.unregister_class(AQ_3DViewPanel)
    AQ_Toolkit_ops.unregister()
    AQ_panel.unregister()
    AQ_Batch_img_load.unregister()
    AQ_HellDivers2_ExpandTool.unregister()
    AQ_MHWilds_ExpandTool.unregister()
    bpy.utils.unregister_class(AQ_CusProperty)
    del bpy.types.Scene.AQ_Props
    addonPreferences.unregister()
    addon_updater_ops.unregister()
    unregister_additional_addons()
    snap_ops.unregister()


if __name__ == "__main__":
    register()
    # unregister()
