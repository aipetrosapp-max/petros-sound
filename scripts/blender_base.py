"""
Generator for Phase 2: Bespoke 3D Hero Props for all 5 Spatial Rooms in Petros-music
- Conforms to export conventions:
  - Y-up, meters scale
  - minY = 0 (bottom-center pivot for all ground props)
  - PBR materials (Principled BSDF) with metallic, roughness, and color
  - Draco-compressed GLB output
"""
import bpy
import math
import os

def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    # Ensure a collection exists
    if not bpy.data.collections:
        col = bpy.data.collections.new("SceneCollection")
        bpy.context.scene.collection.children.link(col)

def set_pivot_bottom_center(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    # Ensure transforms applied
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    # Calculate bounding box min z
    bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
    min_z = min(v.z for v in bbox)
    # Offset origin to bottom
    bpy.context.scene.cursor.location = (0, 0, min_z)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    obj.location.z -= min_z
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)

def create_pbr_material(name, base_color, metallic=0.0, roughness=0.5, clearcoat=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = base_color
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if "Clearcoat Weight" in bsdf.inputs:
            bsdf.inputs["Clearcoat Weight"].default_value = clearcoat
        elif "Coat" in bsdf.inputs:
            bsdf.inputs["Coat"].default_value = clearcoat
    return mat

def export_draco_glb(filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        bpy.ops.export_scene.gltf(
            filepath=filepath,
            export_format='GLB',
            export_draco_mesh_compression_enable=True,
            export_apply=True,
            export_yup=True
        )
    except Exception as e:
        print(f"Draco export error fallback to standard GLB: {e}")
        bpy.ops.export_scene.gltf(
            filepath=filepath,
            export_format='GLB',
            export_draco_mesh_compression_enable=False,
            export_apply=True,
            export_yup=True
        )
    print(f"Exported: {filepath} ({os.path.getsize(filepath)} bytes)")

import mathutils
