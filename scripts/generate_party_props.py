import sys
import os
import math
import bpy
import mathutils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blender_base import reset_scene, create_pbr_material, export_draco_glb, set_pivot_bottom_center

def build_dj_console(out_path):
    reset_scene()
    matte_black = create_pbr_material("DJ_Chassis", (0.04, 0.04, 0.04, 1.0), metallic=0.2, roughness=0.4)
    brushed_alu = create_pbr_material("Brushed_Aluminum", (0.75, 0.75, 0.77, 1.0), metallic=0.9, roughness=0.2)
    display_screen = create_pbr_material("Waveform_OLED", (0.01, 0.35, 0.8, 1.0), metallic=0.1, roughness=0.1)
    led_blue = create_pbr_material("LED_Cyan", (0.0, 0.8, 1.0, 1.0), metallic=0.0, roughness=0.1)

    # DJ Table Stand
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.45))
    table = bpy.context.active_object
    table.scale = (2.2, 0.85, 0.9)
    table.data.materials.append(matte_black)

    # DJM Mixer (Center)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.94))
    mixer = bpy.context.active_object
    mixer.scale = (0.42, 0.48, 0.08)
    mixer.data.materials.append(matte_black)

    # Mixer EQ knobs array
    for col in [-0.12, -0.04, 0.04, 0.12]:
        for row in [0.05, 0.12, 0.18]:
            bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.03, location=(col, row, 1.0))
            knob = bpy.context.active_object
            knob.data.materials.append(brushed_alu)

    # 2x CDJ-3000 Players (Left & Right)
    for side in [-0.55, 0.55]:
        # Player body
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(side, 0, 0.94))
        cdj = bpy.context.active_object
        cdj.scale = (0.38, 0.48, 0.08)
        cdj.data.materials.append(matte_black)

        # Jog Wheel (center of CDJ)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.11, depth=0.03, location=(side, -0.06, 0.99))
        jog = bpy.context.active_object
        jog.data.materials.append(brushed_alu)

        # Jog Wheel Display Ring
        bpy.ops.mesh.primitive_torus_add(major_radius=0.115, minor_radius=0.006, location=(side, -0.06, 1.0))
        ring = bpy.context.active_object
        ring.data.materials.append(led_blue)

        # Tilted 9-inch Touch Display
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(side, 0.16, 1.01))
        screen = bpy.context.active_object
        screen.scale = (0.24, 0.14, 0.02)
        screen.rotation_euler = (math.radians(-15), 0, 0)
        screen.data.materials.append(display_screen)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Party_DJ_Console"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_subwoofer_stack(out_path):
    reset_scene()
    wood_paint = create_pbr_material("Tour_Grade_Polyurea", (0.05, 0.05, 0.06, 1.0), metallic=0.05, roughness=0.85)
    grill_mat = create_pbr_material("Steel_Hex_Grill", (0.1, 0.1, 0.12, 1.0), metallic=0.8, roughness=0.35)
    horn_mat = create_pbr_material("ABS_Horn_Flare", (0.02, 0.02, 0.02, 1.0), metallic=0.2, roughness=0.3)

    # 2x 18-inch Subwoofer Cabinets (stacked vertically)
    for z in [0.45, 1.25]:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, z))
        sub = bpy.context.active_object
        sub.scale = (0.9, 0.85, 0.75)
        sub.data.materials.append(wood_paint)

        # Recessed driver baffle & grill
        bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=0.05, location=(0, -0.42, z))
        cone = bpy.context.active_object
        cone.rotation_euler = (math.radians(90), 0, 0)
        cone.data.materials.append(grill_mat)

    # Top Line-array mid/high cabinet
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.85))
    top = bpy.context.active_object
    top.scale = (0.8, 0.6, 0.4)
    top.data.materials.append(wood_paint)

    # Horn flare mouth
    bpy.ops.mesh.primitive_cone_add(radius1=0.2, radius2=0.05, depth=0.2, location=(0, -0.3, 1.85))
    horn = bpy.context.active_object
    horn.rotation_euler = (math.radians(-90), 0, 0)
    horn.data.materials.append(horn_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Party_Subwoofer_Stack"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_stage_truss_rig(out_path):
    reset_scene()
    steel_mat = create_pbr_material("Silver_Aluminum_Truss", (0.8, 0.82, 0.85, 1.0), metallic=0.95, roughness=0.2)
    lamp_mat = create_pbr_material("Moving_Head_Casing", (0.03, 0.03, 0.04, 1.0), metallic=0.3, roughness=0.4)
    lens_mat = create_pbr_material("Optical_Glass_Lens", (0.9, 0.95, 1.0, 1.0), metallic=0.1, roughness=0.05)

    # Main 4-chord Box Truss Beam (4m span)
    for x_offset, z_offset in [(-0.2, -0.2), (0.2, -0.2), (-0.2, 0.2), (0.2, 0.2)]:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=4.0, location=(0, x_offset, 2.5 + z_offset))
        chord = bpy.context.active_object
        chord.rotation_euler = (0, math.radians(90), 0)
        chord.data.materials.append(steel_mat)

    # Triangular web cross-bracing
    for i in range(8):
        pos_x = -1.75 + i * 0.5
        bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.015, location=(pos_x, 0, 2.5))
        brace = bpy.context.active_object
        brace.rotation_euler = (0, math.radians(90), 0)
        brace.data.materials.append(steel_mat)

    # 4x Moving Head Beam Lights clamped to truss
    for pos_x in [-1.5, -0.5, 0.5, 1.5]:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=0.22, location=(pos_x, 0, 2.2))
        head = bpy.context.active_object
        head.rotation_euler = (math.radians(25), 0, 0)
        head.data.materials.append(lamp_mat)

        bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.03, location=(pos_x, -0.05, 2.1))
        lens = bpy.context.active_object
        lens.rotation_euler = (math.radians(25), 0, 0)
        lens.data.materials.append(lens_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Party_Stage_Truss_Rig"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_vip_leather_booth(out_path):
    reset_scene()
    leather_mat = create_pbr_material("VIP_Tufted_Leather", (0.08, 0.04, 0.03, 1.0), metallic=0.05, roughness=0.45)
    brass_mat = create_pbr_material("Ice_Bucket_Brass", (0.9, 0.85, 0.4, 1.0), metallic=0.95, roughness=0.15)
    glass_mat = create_pbr_material("Champagne_Bottle", (0.1, 0.3, 0.1, 1.0), metallic=0.1, roughness=0.1)

    # Curved Semi-circular Lounge Bench
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1.6, depth=0.45, location=(0, 0, 0.22))
    base = bpy.context.active_object
    base.scale = (1.0, 0.65, 1.0)
    base.data.materials.append(leather_mat)

    # High Backrest with Tufting
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1.65, depth=0.9, location=(0, 0.15, 0.75))
    back = bpy.context.active_object
    back.scale = (1.0, 0.6, 1.0)
    back.data.materials.append(leather_mat)

    # Low VIP Coffee Table in Center
    bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=0.4, location=(0, -0.3, 0.2))
    table = bpy.context.active_object
    table.data.materials.append(leather_mat)

    # Champagne Ice Bucket on Table
    bpy.ops.mesh.primitive_cone_add(radius1=0.14, radius2=0.18, depth=0.22, location=(0, -0.3, 0.51))
    bucket = bpy.context.active_object
    bucket.data.materials.append(brass_mat)

    # Champagne Bottle inside Bucket
    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.28, location=(0.02, -0.28, 0.62))
    bottle = bpy.context.active_object
    bottle.rotation_euler = (math.radians(15), math.radians(10), 0)
    bottle.data.materials.append(glass_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Party_VIP_Booth"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

if __name__ == "__main__":
    base_dir = r"C:\Users\ELI\Desktop\Petros-music\public\models\party"
    build_dj_console(os.path.join(base_dir, "party_dj_console.glb"))
    build_subwoofer_stack(os.path.join(base_dir, "party_subwoofer_stack.glb"))
    build_stage_truss_rig(os.path.join(base_dir, "party_truss_rig.glb"))
    build_vip_leather_booth(os.path.join(base_dir, "party_vip_booth.glb"))
    print("ALL PARTY HERO MODELS GENERATED SUCCESSFULLY!")
