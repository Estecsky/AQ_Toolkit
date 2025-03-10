from . import ops

bl_info = {
    "name": "UV Keying",
    "author": "emm",
    "version": (1, 0, 2),
    "blender": (2, 90, 0),
    "location": "3DView -> Panel -> 黑白",
    "description": "BW UV",
    "category": "UV",
}

modules = [
    ops,
]


def register():
    for module in modules:
        module.register()


def unregister():
    for module in modules:
        module.unregister()
