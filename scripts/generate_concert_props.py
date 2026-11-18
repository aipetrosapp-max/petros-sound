import sys
import os
import math
import bpy
import mathutils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blender_base import reset_scene, create_pbr_material, export_draco_glb, set_pivot_bottom_center

def build_drum_kit(out_path):
    reset_scene()
    shell_mat = create_pbr_material("Burgundy_Sparkle_Wrap", (0.35, 0.04, 0.08, 1.0), metallic=0.4, roughness=0.25)
    chrome_mat = create_pbr_material("Drum_Hardware_Chrome", (0.9, 0.9, 0.92, 1.0), metallic=0.98, roughness=0.1)
    head_mat = create_pbr_material("Coated_Remo_Head", (0.92, 0.92, 0.9, 1.0), metallic=0.0, roughness=0.4)
    cymbal_mat = create_pbr_material("Cast_Bronze_B20", (0.85, 0.65, 0.22, 1.0), metallic=0.92, roughness=0.22)

    # 1. Bass Drum 22-inch
    bpy.ops.mesh.primitive_cylinder_add(radius=0.35, depth=0.45, location=(0, 0, 0.38))
    kick = bpy.context.active_object
    kick.rotation_euler = (math.radians(90), 0, 0)
    kick.data.materials.append(shell_mat)

    # Kick Drum Head
    bpy.ops.mesh.primitive_cylinder_add(radius=0.34, depth=0.46, location=(0, 0, 0.38))
    kick_head = bpy.context.active_object
    kick_head.rotation_euler = (math.radians(90), 0, 0)
    kick_head.data.materials.append(head_mat)

    # 2. Snare Drum on Chrome Stand
    bpy.ops.mesh.primitive_cylinder_add(radius=0.22, depth=0.14, location=(-0.35, 0.2, 0.7))
    snare = bpy.context.active_object
    snare.data.materials.append(shell_mat)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.018, depth=0.65, location=(-0.35, 0.2, 0.32))
    snare_stand = bpy.context.active_object
    snare_stand.data.materials.append(chrome_mat)

    # 3. Two Rack Toms on Kick mount
    for tx, trot in [(-0.18, math.radians(-12)), (0.18, math.radians(12))]:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=0.22, location=(tx, 0.05, 0.88))
        tom = bpy.context.active_object
        tom.rotation_euler = (math.radians(15), trot, 0)
        tom.data.materials.append(shell_mat)

    # 4. Floor Tom
    bpy.ops.mesh.primitive_cylinder_add(radius=0.26, depth=0.35, location=(0.48, 0.22, 0.6))
    ftom = bpy.context.active_object
    ftom.data.materials.append(shell_mat)

    # 5. Hi-Hat Cymbal Pair
    bpy.ops.mesh.primitive_cylinder_add(radius=0.22, depth=0.02, location=(-0.65, 0.25, 0.95))
    hihat = bpy.context.active_object
    hihat.data.materials.append(cymbal_mat)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.95, location=(-0.65, 0.25, 0.47))
    hh_stand = bpy.context.active_object
    hh_stand.data.materials.append(chrome_mat)

    # 6. Ride & Crash Cymbals
    for cx, cy, cz in [(-0.55, -0.2, 1.25), (0.6, -0.15, 1.35)]:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=0.015, location=(cx, cy, cz))
        cymbal = bpy.context.active_object
        cymbal.rotation_euler = (math.radians(10), math.radians(8), 0)
        cymbal.data.materials.append(cymbal_mat)

        bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=cz, location=(cx, cy, cz/2))
        stand = bpy.context.active_object
        stand.data.materials.append(chrome_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Concert_Stage_Drum_Kit"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_marshall_amp_stack(out_path):
    reset_scene()
    tolex_mat = create_pbr_material("Elephant_Grain_Tolex", (0.03, 0.03, 0.03, 1.0), metallic=0.05, roughness=0.8)
    cloth_mat = create_pbr_material("Salt_Pepper_Grill_Cloth", (0.2, 0.2, 0.18, 1.0), metallic=0.1, roughness=0.85)
    gold_panel = create_pbr_material("Brushed_Gold_Plexi", (0.8, 0.65, 0.2, 1.0), metallic=0.85, roughness=0.25)
    logo_white = create_pbr_material("Script_Logo_White", (0.95, 0.95, 0.95, 1.0), metallic=0.0, roughness=0.2)

    # 2x 4x12 Speaker Cabinets (angled A-cab and straight B-cab)
    for z_pos in [0.42, 1.2]:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, z_pos))
        cab = bpy.context.active_object
        cab.scale = (0.76, 0.36, 0.74)
        cab.data.materials.append(tolex_mat)

        # Grill Cloth Baffle
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.17, z_pos))
        grill = bpy.context.active_object
        grill.scale = (0.7, 0.04, 0.68)
        grill.data.materials.append(cloth_mat)

        # White Script Logo
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.19, z_pos))
        logo = bpy.context.active_object
        logo.scale = (0.25, 0.015, 0.06)
        logo.data.materials.append(logo_white)

    # 100W Tube Amplifier Head on Top
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.74))
    head = bpy.context.active_object
    head.scale = (0.75, 0.32, 0.28)
    head.data.materials.append(tolex_mat)

    # Gold Brushed Faceplate
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.15, 1.74))
    plate = bpy.context.active_object
    plate.scale = (0.68, 0.03, 0.14)
    plate.data.materials.append(gold_panel)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Concert_Marshall_Amp_Stack"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

if __name__ == "__main__":
    base_dir = r"C:\Users\ELI\Desktop\Petros-music\public\models\concert"
    build_drum_kit(os.path.join(base_dir, "concert_stage_drum_kit.glb"))
    build_marshall_amp_stack(os.path.join(base_dir, "concert_marshall_stack.glb"))
    print("ALL CONCERT HERO MODELS GENERATED SUCCESSFULLY!")
