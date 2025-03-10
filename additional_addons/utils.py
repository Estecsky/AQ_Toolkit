from contextlib import contextmanager

import bmesh
import bpy
import mathutils


def get_bm(context, mesh: bpy.types.Mesh):
    if context.mode == "EDIT_MESH":
        return bmesh.from_edit_mesh(mesh)
    else:
        bm = bmesh.new()
        bm.from_mesh(mesh)
        return bm


def update_bm(context, bm, obj):
    if context.mode == "EDIT_MESH":
        bmesh.update_edit_mesh(obj.data)
    else:
        bm.to_mesh(obj.data)


def from_mesh_get_kd_true(context, obj: bpy.types.Object):
    matrix = obj.matrix_world
    bm = get_bm(context, obj.data)

    kd_true = mathutils.kdtree.KDTree(len(bm.verts))

    for vert in bm.verts:
        kd_true.insert(matrix @ vert.co, vert.index)

    kd_true.balance()
    bm.free()
    return kd_true


def get_vg_index(vg_name: str, obj: bpy.types.Object, new=False) -> int:
    if (vg_name not in obj.vertex_groups) or new:
        return obj.vertex_groups.new(name=vg_name).index
    return obj.vertex_groups[vg_name].index


def from_data_get_material(data: bpy.types.Mesh) -> "list[bpy.types.Image]":
    res = []
    for material in data.materials:
        for node in material.node_tree.nodes:
            if node.type == "TEX_IMAGE" and node.image is not None:
                res.append(node.image)
    return res


@contextmanager
def pop_prop():
    active = None
    indexs = []
    try:
        active = bpy.context.view_layer.objects.active
        indexs = [obj.vertex_groups.active_index for obj in bpy.context.selected_objects]
        yield
    finally:
        bpy.context.view_layer.objects.active = active
        for index, ai in enumerate(indexs):
            bpy.context.selected_objects[index].vertex_groups.active_index = ai
