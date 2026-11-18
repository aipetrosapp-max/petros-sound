import sys
import os
import math
import bpy
import mathutils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blender_base import reset_scene, create_pbr_material, export_draco_glb, set_pivot_bottom_center

def build_saloon_bar(out_path):
    reset_scene()
    wood_mat = create_pbr_material("Mahogany_Carved", (0.22, 0.08, 0.03, 1.0), metallic=0.05, roughness=0.35)
    brass_mat = create_pbr_material("Tarnished_Brass", (0.85, 0.65, 0.25, 1.0), metallic=0.9, roughness=0.25)
    mirror_mat = create_pbr_material("Mercury_Glass", (0.7, 0.72, 0.75, 1.0), metallic=0.98, roughness=0.08)

    # 1. Main Bar Counter (curved L or U shape / heavy bevel)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.55))
    counter = bpy.context.active_object
    counter.scale = (4.2, 0.9, 1.1)
    counter.data.materials.append(wood_mat)
    
    # Counter Top overhang lip
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.12))
    lip = bpy.context.active_object
    lip.scale = (4.4, 1.05, 0.08)
    lip.data.materials.append(wood_mat)

    # Footrail Brass
    bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=4.2, location=(0, -0.55, 0.18))
    footrail = bpy.context.active_object
    footrail.rotation_euler = (0, math.radians(90), 0)
    footrail.data.materials.append(brass_mat)

    # 2. Backbar Shelves & Mirror Frame
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 1.2, 1.7))
    backbar = bpy.context.active_object
    backbar.scale = (4.0, 0.4, 2.4)
    backbar.data.materials.append(wood_mat)

    # Mercury Mirror Insert
    bpy.ops.mesh.primitive_plane_add(size=1.0, location=(0, 0.99, 1.9))
    mirror = bpy.context.active_object
    mirror.scale = (3.4, 1.4, 1.0)
    mirror.rotation_euler = (math.radians(90), 0, 0)
    mirror.data.materials.append(mirror_mat)

    # Join and set bottom-center pivot
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    main_obj = bpy.context.active_object
    main_obj.name = "Saloon_Hero_Bar"
    set_pivot_bottom_center(main_obj)
    export_draco_glb(out_path)

def build_upright_piano(out_path):
    reset_scene()
    body_mat = create_pbr_material("Antique_Walnut", (0.12, 0.05, 0.02, 1.0), metallic=0.02, roughness=0.28)
    ivory_mat = create_pbr_material("Aged_Ivory", (0.92, 0.88, 0.78, 1.0), metallic=0.0, roughness=0.35)
    ebony_mat = create_pbr_material("Ebony_Keys", (0.02, 0.02, 0.02, 1.0), metallic=0.1, roughness=0.2)
    brass_mat = create_pbr_material("Piano_Brass", (0.85, 0.65, 0.25, 1.0), metallic=0.9, roughness=0.2)

    # Piano body case
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.7))
    case = bpy.context.active_object
    case.scale = (1.5, 0.65, 1.4)
    case.data.materials.append(body_mat)

    # Keyboard bed
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.38, 0.72))
    keybed = bpy.context.active_object
    keybed.scale = (1.42, 0.35, 0.12)
    keybed.data.materials.append(body_mat)

    # White keys plate
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.4, 0.77))
    keys = bpy.context.active_object
    keys.scale = (1.35, 0.22, 0.03)
    keys.data.materials.append(ivory_mat)

    # Black keys strip
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.34, 0.79))
    bkeys = bpy.context.active_object
    bkeys.scale = (1.3, 0.12, 0.025)
    bkeys.data.materials.append(ebony_mat)

    # Pedals
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.3, 0.08))
    pedals = bpy.context.active_object
    pedals.scale = (0.25, 0.15, 0.04)
    pedals.data.materials.append(brass_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Saloon_Upright_Piano"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_saloon_poker_table(out_path):
    reset_scene()
    felt_mat = create_pbr_material("Green_Felt", (0.04, 0.22, 0.08, 1.0), metallic=0.0, roughness=0.85)
    rim_mat = create_pbr_material("Carved_Wood_Rim", (0.18, 0.08, 0.03, 1.0), metallic=0.05, roughness=0.35)
    brass_mat = create_pbr_material("Cup_Holder_Brass", (0.8, 0.6, 0.2, 1.0), metallic=0.9, roughness=0.25)

    # Table rim (octagonal or circular)
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1.05, depth=0.08, location=(0, 0, 0.78))
    rim = bpy.context.active_object
    rim.data.materials.append(rim_mat)

    # Felt surface inset
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.92, depth=0.09, location=(0, 0, 0.79))
    felt = bpy.context.active_object
    felt.data.materials.append(felt_mat)

    # Central turned pedestal leg
    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.18, depth=0.74, location=(0, 0, 0.37))
    pedestal = bpy.context.active_object
    pedestal.data.materials.append(rim_mat)

    # Base paws
    bpy.ops.mesh.primitive_cylinder_add(vertices=4, radius=0.7, depth=0.08, location=(0, 0, 0.04))
    base = bpy.context.active_object
    base.data.materials.append(rim_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Saloon_Poker_Table"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_wagon_wheel_chandelier(out_path):
    reset_scene()
    wood_mat = create_pbr_material("Rustic_Oak", (0.15, 0.09, 0.04, 1.0), metallic=0.05, roughness=0.7)
    iron_mat = create_pbr_material("Wrought_Iron", (0.05, 0.05, 0.05, 1.0), metallic=0.85, roughness=0.45)
    brass_mat = create_pbr_material("Lantern_Brass", (0.8, 0.6, 0.2, 1.0), metallic=0.9, roughness=0.25)

    # Wheel Rim
    bpy.ops.mesh.primitive_torus_add(major_radius=1.1, minor_radius=0.07, location=(0, 0, 0))
    rim = bpy.context.active_object
    rim.data.materials.append(wood_mat)

    # Wheel Hub
    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=0.3, location=(0, 0, 0))
    hub = bpy.context.active_object
    hub.data.materials.append(wood_mat)

    # Spokes
    for i in range(8):
        ang = i * (math.pi / 4)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=1.0, location=(math.cos(ang)*0.55, math.sin(ang)*0.55, 0))
        spoke = bpy.context.active_object
        spoke.rotation_euler = (0, math.radians(90), ang)
        spoke.data.materials.append(wood_mat)

    # Hurricane lamps on rim
    for i in range(6):
        ang = i * (math.pi / 3)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.06, depth=0.25, location=(math.cos(ang)*1.1, math.sin(ang)*1.1, 0.15))
        lamp = bpy.context.active_object
        lamp.data.materials.append(brass_mat)

    # Hanging iron chain suspension
    for i in range(3):
        ang = i * (2 * math.pi / 3)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.8, location=(math.cos(ang)*0.5, math.sin(ang)*0.5, 0.4))
        chain = bpy.context.active_object
        chain.rotation_euler = (math.radians(15)*math.cos(ang), math.radians(15)*math.sin(ang), 0)
        chain.data.materials.append(iron_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Saloon_Wagon_Wheel_Chandelier"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

if __name__ == "__main__":
    base_dir = r"C:\Users\ELI\Desktop\Petros-music\public\models\cafe\hero"
    build_saloon_bar(os.path.join(base_dir, "saloon_bar_counter.glb"))
    build_upright_piano(os.path.join(base_dir, "saloon_upright_piano.glb"))
    build_saloon_poker_table(os.path.join(base_dir, "saloon_poker_table.glb"))
    build_wagon_wheel_chandelier(os.path.join(base_dir, "saloon_wagon_wheel_chandelier.glb"))
    print("ALL CAFE HERO MODELS GENERATED SUCCESSFULLY!")
