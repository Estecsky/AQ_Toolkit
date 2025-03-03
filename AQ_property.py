import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty


class AQ_CusProperty(bpy.types.PropertyGroup):

    AQ_Batch_imgfile_path: StringProperty(
        name="Img File Path", subtype="DIR_PATH", default=""
    )  # type: ignore

    AQ_limitWeightValue: IntProperty(
        name="Limit Weight Value",
        description="The maximum weight value for the selected object",
        default=4,
        min=1,
        max=10,
    )  # type: ignore
