import bpy
from .AQ_Prefs import AQ_PublicClass
from 。 import addon_updater_ops
from bpy.props import BoolProperty, IntProperty

@addon_updater_ops.make_annotations
class AQ_Toolkit_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = AQ_PublicClass.AQ_ADDON_NAME

    # addon updater preferences
    auto_check_update: bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False,
    )  # type: ignore

    updater_interval_months: bpy.props.IntProperty(
        name="Months",
        description="Number of months between checking for updates",
        default=0,
        min=0,
    )  # type: ignore
    updater_interval_days: bpy.props.IntProperty(
        name="Days",
        description="Number of days between checking for updates",
        default=7,
        min=0,
    )  # type: ignore
    updater_interval_hours: bpy.props.IntProperty(
        name="Hours",
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23,
    )  # type: ignore
    updater_interval_minutes: bpy.props.IntProperty(
        name="Minutes",
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59,
    )  # type: ignore

    HD2ExpandTool: BoolProperty(
        name="HellDivers2 扩展工具",
        default=False,
        description="HellDivers2 扩展工具",
    )  # type: ignore

    MHWildsExpandTool: BoolProperty(
        name="MHWilds 扩展工具",
        default=False,
        description="MHWilds 扩展工具",
    )  # type: ignore

    def draw(self, context):

        layout = self.layout
        layout.label(text="拓展工具")
        # 扩展工具开关
        layout.prop(self, "HD2ExpandTool")
        layout.prop(self, "MHWildsExpandTool")
        # print(self.HD2_ExpandToolSwitch)
        addon_updater_ops.update_settings_ui(self, context)


def register():
    bpy.utils.register_class(AQ_Toolkit_AddonPreferences)


def unregister():
    bpy.utils.unregister_class(AQ_Toolkit_AddonPreferences)
