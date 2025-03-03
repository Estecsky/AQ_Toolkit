import bpy
import os
from os.path import dirname, realpath, basename
from bpy.props import BoolProperty, IntProperty


class AQ_Prefs:

    @staticmethod
    def pref_():
        return bpy.context.preferences.addons[AQ_PublicClass.AQ_ADDON_NAME].preferences

    @property
    def pref(self):
        return self.pref_()

    @staticmethod
    def get_addon_prefs(addon_name=None):
        addon = AQ_PublicClass.AQ_ADDON_NAME if addon_name is None else addon_name
        return bpy.context.preferences.addons[addon].preferences


class AQ_PublicClass(AQ_Prefs):

    AQ_ADDON_NAME = basename(dirname(realpath(__file__)))


class AQ_Toolkit_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = AQ_PublicClass.AQ_ADDON_NAME

    HD2ExpandTool: BoolProperty(
        name="HellDivers2 扩展工具",
        default=False,
        description="HellDivers2 扩展工具",
    )  # type: ignore
    
    def draw(self, context):

        layout = self.layout
        layout.label(text="拓展工具")
        # 扩展工具开关
        layout.prop(self, "HD2ExpandTool")   
        # print(self.HD2_ExpandToolSwitch)


def register():
    bpy.utils.register_class(AQ_Toolkit_AddonPreferences)



def unregister():
    bpy.utils.unregister_class(AQ_Toolkit_AddonPreferences)
