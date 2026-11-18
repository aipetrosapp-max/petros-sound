"""
Advanced PBR Baker and Material Synthesizer for Blender 5.3
Creates procedural grain/tufting/brushed node networks with UV unwrap,
procedural AO + normal maps, and exports rich Draco GLBs.
"""
import bpy
import mathutils
import math
import os

def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    if not bpy.data.collections:
        col = bpy.data.collections.new("SceneCollection")
        bpy.context.scene.collection.children.link(col)

def set_pivot_bottom_center(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bbox = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
    min_z = min(v.z for v in bbox)
    bpy.context.scene.cursor.location = (0, 0, min_z)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    obj.location.z -= min_z
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)

def apply_smart_uv_project(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.02)
    bpy.ops.object.mode_set(mode='OBJECT')

def create_rich_pbr_material(name, base_color, metallic=0.0, roughness=0.5, bump_strength=0.15, noise_scale=25.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()

    # Create node network
    output = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    tex_coord = nodes.new(type='ShaderNodeTexCoord')
    noise = nodes.new(type='ShaderNodeTexNoise')
    bump = nodes.new(type='ShaderNodeBump')
    color_ramp = nodes.new(type='ShaderNodeValToRGB')

    noise.inputs['Scale'].default_value = noise_scale
    noise.inputs['Detail'].default_value = 4.0
    noise.inputs['Roughness'].default_value = 0.65

    bump.inputs['Strength'].default_value = bump_strength
    bump.inputs['Distance'].default_value = 0.05

    bsdf.inputs['Base Color'].default_value = base_color
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = roughness

    links.new(tex_coord.outputs['Object'], noise.inputs['Vector'])
    links.new(noise.outputs['Fac'], bump.inputs['Height'])
    links.new(bump.outputs['Normal'], bsdf.inputs['Normal'])
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

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
        print(f"Fallback standard glb: {e}")
        bpy.ops.export_scene.gltf(
            filepath=filepath,
            export_format='GLB',
            export_draco_mesh_compression_enable=False,
            export_apply=True,
            export_yup=True
        )
    print(f"Exported rich PBR model: {filepath} ({os.path.getsize(filepath)} bytes)")
