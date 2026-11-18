import sys
import os
import math
import bpy
import mathutils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blender_base import reset_scene, create_pbr_material, export_draco_glb, set_pivot_bottom_center

def build_shure_sm7b_arm(out_path):
    reset_scene()
    body_mat = create_pbr_material("Dark_Charcoal_Anodized", (0.04, 0.04, 0.04, 1.0), metallic=0.6, roughness=0.35)
    foam_mat = create_pbr_material("Acoustic_Foam_Windscreen", (0.02, 0.02, 0.02, 1.0), metallic=0.0, roughness=0.95)
    steel_mat = create_pbr_material("Boom_Arm_Steel", (0.1, 0.1, 0.1, 1.0), metallic=0.8, roughness=0.3)

    # Base Desk Clamp
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.08, location=(0, 0, 0.04))
    clamp = bpy.context.active_object
    clamp.data.materials.append(steel_mat)

    # Lower Boom Arm Segment
    bpy.ops.mesh.primitive_cylinder_add(radius=0.014, depth=0.45, location=(0, 0.08, 0.25))
    lower_arm = bpy.context.active_object
    lower_arm.rotation_euler = (math.radians(-25), 0, 0)
    lower_arm.data.materials.append(steel_mat)

    # Upper Boom Arm Segment
    bpy.ops.mesh.primitive_cylinder_add(radius=0.014, depth=0.45, location=(0, 0.22, 0.58))
    upper_arm = bpy.context.active_object
    upper_arm.rotation_euler = (math.radians(35), 0, 0)
    upper_arm.data.materials.append(steel_mat)

    # Yoke Shockmount Bracket
    bpy.ops.mesh.primitive_torus_add(major_radius=0.065, minor_radius=0.008, location=(0, 0.38, 0.72))
    yoke = bpy.context.active_object
    yoke.rotation_euler = (math.radians(90), 0, 0)
    yoke.data.materials.append(body_mat)

    # SM7B Microphone Body
    bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.16, location=(0, 0.38, 0.72))
    mic = bpy.context.active_object
    mic.rotation_euler = (0, math.radians(90), 0)
    mic.data.materials.append(body_mat)

    # Foam Windscreen Front
    bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=0.07, location=(0.1, 0.38, 0.72))
    foam = bpy.context.active_object
    foam.rotation_euler = (0, math.radians(90), 0)
    foam.data.materials.append(foam_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Podcast_SM7B_BoomMic"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_rodecaster_console(out_path):
    reset_scene()
    body_mat = create_pbr_material("Aluminium_Beveled_Chassis", (0.05, 0.05, 0.05, 1.0), metallic=0.7, roughness=0.3)
    pad_mat = create_pbr_material("RGB_Silicone_Pads", (0.9, 0.2, 0.1, 1.0), metallic=0.0, roughness=0.3)
    fader_mat = create_pbr_material("Silver_Fader_Cap", (0.85, 0.85, 0.88, 1.0), metallic=0.9, roughness=0.2)
    touchscreen_mat = create_pbr_material("Glass_Capacitive_Screen", (0.05, 0.2, 0.3, 1.0), metallic=0.1, roughness=0.1)

    # Slanted Desktop Console Housing
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.04))
    body = bpy.context.active_object
    body.scale = (0.35, 0.28, 0.06)
    body.rotation_euler = (math.radians(-8), 0, 0)
    body.data.materials.append(body_mat)

    # 5.5-inch Color Touchscreen
    bpy.ops.mesh.primitive_plane_add(size=1.0, location=(-0.06, 0.05, 0.078))
    screen = bpy.context.active_object
    screen.scale = (0.12, 0.07, 1.0)
    screen.rotation_euler = (math.radians(-8), 0, 0)
    screen.data.materials.append(touchscreen_mat)

    # 8 Trigger Sound Pads (2x4 array)
    for px in [0.06, 0.11]:
        for py in [-0.04, 0.0, 0.04, 0.08]:
            bpy.ops.mesh.primitive_cube_add(size=1.0, location=(px, py, 0.075))
            pad = bpy.context.active_object
            pad.scale = (0.028, 0.028, 0.01)
            pad.rotation_euler = (math.radians(-8), 0, 0)
            pad.data.materials.append(pad_mat)

    # 4 Channel Broadcast Faders
    for fx in [-0.12, -0.07, -0.02, 0.03]:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(fx, -0.06, 0.075))
        fader = bpy.context.active_object
        fader.scale = (0.018, 0.03, 0.015)
        fader.rotation_euler = (math.radians(-8), 0, 0)
        fader.data.materials.append(fader_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Podcast_RodeCaster_Pro"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_acoustic_diffuser_panel(out_path):
    reset_scene()
    walnut_mat = create_pbr_material("Acoustic_Slatted_Walnut", (0.16, 0.09, 0.04, 1.0), metallic=0.03, roughness=0.45)
    felt_backing = create_pbr_material("Recycled_PET_Acoustic_Felt", (0.03, 0.03, 0.03, 1.0), metallic=0.0, roughness=0.95)

    # Dark Acoustic Felt Backing (1.2m x 2.4m)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.2))
    backing = bpy.context.active_object
    backing.scale = (1.2, 0.04, 2.4)
    backing.data.materials.append(felt_backing)

    # 16 Vertical Walnut Slats
    for i in range(16):
        x_pos = -0.55 + i * 0.072
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x_pos, -0.03, 1.2))
        slat = bpy.context.active_object
        slat.scale = (0.035, 0.025, 2.38)
        slat.data.materials.append(walnut_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Podcast_Acoustic_Diffuser"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

if __name__ == "__main__":
    base_dir = r"C:\Users\ELI\Desktop\Petros-music\public\models\podcast"
    build_shure_sm7b_arm(os.path.join(base_dir, "podcast_sm7b_arm.glb"))
    build_rodecaster_console(os.path.join(base_dir, "podcast_rodecaster.glb"))
    build_acoustic_diffuser_panel(os.path.join(base_dir, "podcast_acoustic_diffuser.glb"))
    print("ALL PODCAST HERO MODELS GENERATED SUCCESSFULLY!")
