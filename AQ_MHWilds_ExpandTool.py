import bpy
from bpy_extras.io_utils import ExportHelper
import os
from bpy.props import StringProperty


class ButtonMakeDirsPath(bpy.types.Operator, ExportHelper):
    bl_description = "创建多级目录"
    bl_idname = "object.make_dirs_path"
    bl_label = "创建多级文件夹"
    bl_options = {"REGISTER", "UNDO"}

    filename_ext = ""

    filter_glob: StringProperty(
        default="",
        options={"HIDDEN"},
        maxlen=255,
    )  # type: ignore
    filepath: StringProperty(
        default="",
        subtype="DIR_PATH",
    )  # type: ignore

    def invoke(self, context, event):
        self.filepath = ""  # 确保 filepath 为空字符串
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

    @classmethod
    def poll(cls, context):
        if bpy.context.scene.AQ_Props.MakeDirs_Path != "":
            return True
        return False

    def execute(self, context):
        input_path = bpy.context.scene.AQ_Props.MakeDirs_Path
        is_moreDirs = bpy.context.scene.AQ_Props.MakeSeqDirs_Path
        if "\\" in input_path:
            input_path = input_path.replace("\\", "/")
        try:
            if input_path.startswith("natives/STM") or input_path.startswith(
                "natives/stm"
            ):
                if is_moreDirs:
                    for i in range(1, 6):
                        os.makedirs(self.filepath + input_path + "/" + str(i))
                    self.report(
                        {"INFO"},
                        f"更多文件夹在多级文件夹创建完成{self.filepath + input_path}",
                    )
                else:
                    os.makedirs(self.filepath + input_path)
                    self.report(
                        {"INFO"}, f"多级文件夹创建完成{self.filepath + input_path}"
                    )

            # elif input_path.startswith("STM") or input_path.startswith("stm"):
            #     input_path = "natives/" + input_path
            else:
                if is_moreDirs:
                    for i in range(1, 6):
                        os.makedirs(self.filepath + input_path + "/" + str(i))
                    self.report(
                        {"WARNING"},
                        f"路径没有从根目录natives/STM开始，更多文件夹创建完成{self.filepath + input_path}",
                    )
                else:
                    os.makedirs(self.filepath + input_path)
                    self.report(
                        {"WARNING"},
                        f"路径没有从根目录natives/STM开始，多级文件夹创建完成{self.filepath + input_path}",
                    )
        except FileExistsError as e:
            self.report(
                {"ERROR"},
                f"目录已存在，多级文件夹创建失败{self.filepath + input_path}",
            )
        return {"FINISHED"}


def ExpandPanel(layout):
    row = layout.row()
    props = bpy.context.scene.AQ_Props
    row.scale_y = 0.5
    row.label(text="Monster Hunter Wilds拓展组件", icon="TOOL_SETTINGS")
    row = layout.row()
    row.scale_y = 1
    row.prop(props, "MakeSeqDirs_Path", text="自动在底层文件夹下创建编号1到5的文件夹")
    row = layout.row()
    row.scale_y = 1.3
    row.prop(props, "MakeDirs_Path", text="输入多级目录")
    row = layout.row()
    row.scale_y = 1.3
    row.operator("object.make_dirs_path", text="创建多级文件夹", icon="FILE_FOLDER")


def register():
    bpy.utils.register_class(ButtonMakeDirsPath)


def unregister():
    bpy.utils.unregister_class(ButtonMakeDirsPath)
