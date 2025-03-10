import bpy
from .ops import (
    UVKeying,
    ButtonMarkContrastVert,
)


# class UVKeyingPanel(bpy.types.Panel):
#     bl_idname = "UV_KEYING_PT_PANEL"
#     bl_label = "UV 切割"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "UV 切割"
#     bl_options = set()

#     def draw(self, context):
#         from .ops import (
#             UVKeying,
#             RemoveAndScale,
#             MarkContrastVert,
#             RemoveEmptyVertGroup,
#         )

#         column = self.layout.column(align=True)
#         column.operator(UVKeying.bl_idname, text="UV 切割", icon="UV_FACESEL")
#         column.operator(RemoveAndScale.bl_idname)
#         column.operator(MarkContrastVert.bl_idname)


def extra_addons_panel(layout):
    row = layout.row()
    row.scale_y = 0.5
    row.label(text="额外工具", icon="TOOL_SETTINGS")
    row = layout.row()
    row.scale_y = 1.3
    row.operator(UVKeying.bl_idname, text="UV 切割", icon="UV_FACESEL")
    row = layout.row()
    row.scale_y = 1.3
    row.operator(
        ButtonMarkContrastVert.bl_idname, icon="GROUP_VERTEX", text="对比顶点组"
    )


def draw_ButtonRemoveAndScaleMesh(layout):
    row = layout.row()
    row.scale_y = 1.5
    row.operator("mesh.remove_and_scale_mesh", icon="MESH_DATA", text="删除所选并缩放")


# def register():
#     bpy.utils.register_class(UVKeyingPanel)


# def unregister():
#     bpy.utils.unregister_class(UVKeyingPanel)
