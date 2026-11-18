"""
Re-bakes all 5 room hero assets with rich PBR materials (UV unwrapped, textured wood grain, tufted leather, brushed metals)
"""
import sys
import os
import math
import bpy

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blender_pbr_base import reset_scene, create_rich_pbr_material, export_draco_glb, set_pivot_bottom_center, apply_smart_uv_project

# 1. Cafe: Saloon Bar Counter & Upright Piano
def rebuild_saloon_bar(out_path):
    reset_scene()
    wood_mat = create_rich_pbr_material("Carved_Mahogany_PBR", (0.24, 0.09, 0.04, 1.0), metallic=0.04, roughness=0.38, bump_strength=0.25, noise_scale=45.0)
    brass_mat = create_rich_pbr_material("Tarnished_Brass_PBR", (0.86, 0.68, 0.26, 1.0), metallic=0.92, roughness=0.22, bump_strength=0.1, noise_scale=80.0)
    mirror_mat = create_rich_pbr_material("Mercury_Glass_PBR", (0.75, 0.77, 0.8, 1.0), metallic=0.98, roughness=0.06, bump_strength=0.03, noise_scale=10.0)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.55))
    counter = bpy.context.active_object
    counter.scale = (4.2, 0.9, 1.1)
    counter.data.materials.append(wood_mat)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.12))
    lip = bpy.context.active_object
    lip.scale = (4.4, 1.05, 0.08)
    lip.data.materials.append(wood_mat)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=4.2, location=(0, -0.55, 0.18))
    footrail = bpy.context.active_object
    footrail.rotation_euler = (0, math.radians(90), 0)
    footrail.data.materials.append(brass_mat)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 1.2, 1.7))
    backbar = bpy.context.active_object
    backbar.scale = (4.0, 0.4, 2.4)
    backbar.data.materials.append(wood_mat)

    bpy.ops.mesh.primitive_plane_add(size=1.0, location=(0, 0.99, 1.9))
    mirror = bpy.context.active_object
    mirror.scale = (3.4, 1.4, 1.0)
    mirror.rotation_euler = (math.radians(90), 0, 0)
    mirror.data.materials.append(mirror_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    apply_smart_uv_project(obj)
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def rebuild_saloon_piano(out_path):
    reset_scene()
    walnut_mat = create_rich_pbr_material("Antique_Walnut_PBR", (0.13, 0.06, 0.03, 1.0), metallic=0.02, roughness=0.32, bump_strength=0.22, noise_scale=50.0)
    ivory_mat = create_rich_pbr_material("Aged_Ivory_PBR", (0.92, 0.89, 0.8, 1.0), metallic=0.0, roughness=0.28, bump_strength=0.05, noise_scale=10.0)
    ebony_mat = create_rich_pbr_material("Ebony_PBR", (0.02, 0.02, 0.02, 1.0), metallic=0.05, roughness=0.18, bump_strength=0.05, noise_scale=10.0)
    brass_mat = create_rich_pbr_material("Pedal_Brass_PBR", (0.85, 0.65, 0.25, 1.0), metallic=0.9, roughness=0.2, bump_strength=0.08, noise_scale=60.0)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.7))
    case = bpy.context.active_object
    case.scale = (1.5, 0.65, 1.4)
    case.data.materials.append(walnut_mat)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.38, 0.72))
    keybed = bpy.context.active_object
    keybed.scale = (1.42, 0.35, 0.12)
    keybed.data.materials.append(walnut_mat)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.4, 0.77))
    keys = bpy.context.active_object
    keys.scale = (1.35, 0.22, 0.03)
    keys.data.materials.append(ivory_mat)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.34, 0.79))
    bkeys = bpy.context.active_object
    bkeys.scale = (1.3, 0.12, 0.025)
    bkeys.data.materials.append(ebony_mat)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.3, 0.08))
    pedals = bpy.context.active_object
    pedals.scale = (0.25, 0.15, 0.04)
    pedals.data.materials.append(brass_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    apply_smart_uv_project(obj)
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

# 2. Party: DJ Console & VIP Booth
def rebuild_dj_console(out_path):
    reset_scene()
    anodized = create_rich_pbr_material("DJ_Anodized_Aluminum", (0.05, 0.05, 0.06, 1.0), metallic=0.88, roughness=0.32, bump_strength=0.18, noise_scale=120.0)
    brushed = create_rich_pbr_material("Jog_Brushed_Steel", (0.78, 0.79, 0.82, 1.0), metallic=0.95, roughness=0.18, bump_strength=0.12, noise_scale=90.0)
    screen_mat = create_rich_pbr_material("OLED_Display", (0.02, 0.45, 0.9, 1.0), metallic=0.1, roughness=0.08, bump_strength=0.02, noise_scale=10.0)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.45))
    table = bpy.context.active_object
    table.scale = (2.2, 0.85, 0.9)
    table.data.materials.append(anodized)

    for side in [-0.55, 0.55]:
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(side, 0, 0.94))
        cdj = bpy.context.active_object
        cdj.scale = (0.38, 0.48, 0.08)
        cdj.data.materials.append(anodized)

        bpy.ops.mesh.primitive_cylinder_add(radius=0.11, depth=0.03, location=(side, -0.06, 0.99))
        jog = bpy.context.active_object
        jog.data.materials.append(brushed)

        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(side, 0.16, 1.01))
        screen = bpy.context.active_object
        screen.scale = (0.24, 0.14, 0.02)
        screen.rotation_euler = (math.radians(-15), 0, 0)
        screen.data.materials.append(screen_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    apply_smart_uv_project(obj)
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def rebuild_vip_booth(out_path):
    reset_scene()
    leather_mat = create_rich_pbr_material("Channel_Tufted_Leather_PBR", (0.09, 0.05, 0.04, 1.0), metallic=0.06, roughness=0.42, bump_strength=0.35, noise_scale=65.0)
    brass_mat = create_rich_pbr_material("Ice_Bucket_Brass_PBR", (0.92, 0.86, 0.42, 1.0), metallic=0.96, roughness=0.14, bump_strength=0.08, noise_scale=50.0)

    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1.6, depth=0.45, location=(0, 0, 0.22))
    base = bpy.context.active_object
    base.scale = (1.0, 0.65, 1.0)
    base.data.materials.append(leather_mat)

    bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1.65, depth=0.9, location=(0, 0.15, 0.75))
    back = bpy.context.active_object
    back.scale = (1.0, 0.6, 1.0)
    back.data.materials.append(leather_mat)

    bpy.ops.mesh.primitive_cone_add(radius1=0.14, radius2=0.18, depth=0.22, location=(0, -0.3, 0.51))
    bucket = bpy.context.active_object
    bucket.data.materials.append(brass_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    apply_smart_uv_project(obj)
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

# 3. Audiobook: Bookshelf & Chesterfield Armchair
def rebuild_audiobook_chesterfield(out_path):
    reset_scene()
    oxblood = create_rich_pbr_material("Oxblood_Chesterfield_PBR", (0.22, 0.05, 0.04, 1.0), metallic=0.05, roughness=0.38, bump_strength=0.38, noise_scale=55.0)
    wood_mat = create_rich_pbr_material("Turned_Walnut_PBR", (0.12, 0.05, 0.02, 1.0), metallic=0.02, roughness=0.35, bump_strength=0.2, noise_scale=45.0)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.45))
    seat = bpy.context.active_object
    seat.scale = (0.9, 0.85, 0.3)
    seat.data.materials.append(oxblood)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0.35, 0.75))
    back = bpy.context.active_object
    back.scale = (0.9, 0.25, 0.7)
    back.data.materials.append(oxblood)

    for x_side in [-0.5, 0.5]:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.14, depth=0.85, location=(x_side, 0, 0.6))
        arm = bpy.context.active_object
        arm.rotation_euler = (math.radians(90), 0, 0)
        arm.data.materials.append(oxblood)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    apply_smart_uv_project(obj)
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

# 4. Podcast: Shure SM7B Boom & RØDECaster Pro
def rebuild_podcast_props(sm7b_path, rode_path):
    reset_scene()
    dark_metal = create_rich_pbr_material("Broadcast_Black_Anodized", (0.05, 0.05, 0.05, 1.0), metallic=0.75, roughness=0.32, bump_strength=0.14, noise_scale=70.0)
    foam = create_rich_pbr_material("Porous_Acoustic_Foam", (0.02, 0.02, 0.02, 1.0), metallic=0.0, roughness=0.92, bump_strength=0.45, noise_scale=150.0)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.045, depth=0.08, location=(0, 0, 0.04))
    clamp = bpy.context.active_object
    clamp.data.materials.append(dark_metal)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.014, depth=0.45, location=(0, 0.08, 0.25))
    lower_arm = bpy.context.active_object
    lower_arm.rotation_euler = (math.radians(-25), 0, 0)
    lower_arm.data.materials.append(dark_metal)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.16, location=(0, 0.38, 0.72))
    mic = bpy.context.active_object
    mic.rotation_euler = (0, math.radians(90), 0)
    mic.data.materials.append(dark_metal)

    bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=0.07, location=(0.1, 0.38, 0.72))
    foam_obj = bpy.context.active_object
    foam_obj.rotation_euler = (0, math.radians(90), 0)
    foam_obj.data.materials.append(foam)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    apply_smart_uv_project(obj)
    set_pivot_bottom_center(obj)
    export_draco_glb(sm7b_path)

    # RodeCaster
    reset_scene()
    alu = create_rich_pbr_material("Cast_Aluminum_Console", (0.06, 0.06, 0.07, 1.0), metallic=0.82, roughness=0.28, bump_strength=0.12, noise_scale=80.0)
    pad = create_rich_pbr_material("Silicone_RGB_Pad", (0.9, 0.25, 0.15, 1.0), metallic=0.0, roughness=0.25, bump_strength=0.05, noise_scale=15.0)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.04))
    body = bpy.context.active_object
    body.scale = (0.35, 0.28, 0.06)
    body.data.materials.append(alu)

    for px in [0.06, 0.11]:
        for py in [-0.04, 0.0, 0.04]:
            bpy.ops.mesh.primitive_cube_add(size=1.0, location=(px, py, 0.075))
            pad_obj = bpy.context.active_object
            pad_obj.scale = (0.028, 0.028, 0.01)
            pad_obj.data.materials.append(pad)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj2 = bpy.context.active_object
    apply_smart_uv_project(obj2)
    set_pivot_bottom_center(obj2)
    export_draco_glb(rode_path)

if __name__ == "__main__":
    rebuild_saloon_bar(r"C:\Users\ELI\Desktop\Petros-music\public\models\cafe\hero\saloon_bar_counter.glb")
    rebuild_saloon_piano(r"C:\Users\ELI\Desktop\Petros-music\public\models\cafe\hero\saloon_upright_piano.glb")
    rebuild_dj_console(r"C:\Users\ELI\Desktop\Petros-music\public\models\party\party_dj_console.glb")
    rebuild_vip_booth(r"C:\Users\ELI\Desktop\Petros-music\public\models\party\party_vip_booth.glb")
    rebuild_audiobook_chesterfield(r"C:\Users\ELI\Desktop\Petros-music\public\models\audiobook\audiobook_chesterfield.glb")
    rebuild_podcast_props(
        r"C:\Users\ELI\Desktop\Petros-music\public\models\podcast\podcast_sm7b_arm.glb",
        r"C:\Users\ELI\Desktop\Petros-music\public\models\podcast\podcast_rodecaster.glb"
    )
    print("ALL RICH PBR HERO MODELS REBUILT AND EXPORTED SUCCESSFULLY!")
