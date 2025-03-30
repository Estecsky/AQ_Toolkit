import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty,EnumProperty
from .aq_bones_snap.reload_presets import reloadPresets

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
    Auto_Xray_Shading: BoolProperty(
        name="Auto Xray Shading",
        description="保留面后自动打开透视模式",
        default=True,
    )  # type: ignore
    Auto_BacktoObject: BoolProperty(
        name="Auto Backto Object",
        description="缩放后自动返回物体模式",
        default=True,
    )  # type: ignore
    Comebine_vgroup_num: IntProperty(
        name="Comebine vgroup num",
        description="将需要合并的组改为同前缀名，（例如0，0.001，1，1.001，将分别合并为0，1两组）从0开始，往后顺延",
        default=0,
        min=0,
        max=999,
    )  # type: ignore

    MakeDirs_Path: StringProperty(
        name="MakeDirsPath",
        description="需要创建的多级目录，建议从根目录natives开始复制输入路径",
        default="",
    )  # type: ignore
    MakeSeqDirs_Path: BoolProperty(
        name="MakeSeqDirsPath",
        description="在底层文件夹下再创建编号1到5的文件夹",
        default=False,
    )  # type: ignore
    SelectAndRemove_bone: BoolProperty(
        name="SelectAndRemove_bone",
        description="选择后直接删除骨骼",
        default=False,
    )  # type: ignore

    ApplyMirrorModifier: BoolProperty(
        name="ApplyMirrorModifier",
        description="导入时应用模板的镜像修改器",
        default=False,
    )

    TemplateNewCollection: BoolProperty(
        name="NewCollection",
        description="导入时创建新集合",
        default=True,
    )
    #--------------------
    
    BoneSnapPanel : BoolProperty(default=False)  # type: ignore
    MHWilds_Fix_Bones : BoolProperty(default=False,description="只有对于荒野骨骼才有的修正应该开启此项")  # type: ignore
    
    def getBoneList(self, context):
        return reloadPresets()
    
    BoneList: EnumProperty(
    name="",
    description="",
    items=getBoneList
    )  # type: ignore