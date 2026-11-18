import sys
import os
import math
import bpy
import mathutils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from blender_base import reset_scene, create_pbr_material, export_draco_glb, set_pivot_bottom_center

def build_grand_bookshelf(out_path):
    reset_scene()
    mahogany_mat = create_pbr_material("Carved_Mahogany", (0.16, 0.06, 0.02, 1.0), metallic=0.04, roughness=0.3)
    books_leather = create_pbr_material("Book_Spines_Leather", (0.35, 0.12, 0.08, 1.0), metallic=0.05, roughness=0.6)
    books_gold = create_pbr_material("Book_Spines_Gilt", (0.8, 0.65, 0.2, 1.0), metallic=0.85, roughness=0.25)
    brass_mat = create_pbr_material("Library_Brass", (0.85, 0.7, 0.25, 1.0), metallic=0.9, roughness=0.2)

    # Main Case Frame (3m high x 2.4m wide x 0.5m deep)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.5))
    case = bpy.context.active_object
    case.scale = (2.4, 0.5, 3.0)
    case.data.materials.append(mahogany_mat)

    # 5 Horizontal Shelves
    for i in range(5):
        z_pos = 0.5 + i * 0.55
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, z_pos))
        shelf = bpy.context.active_object
        shelf.scale = (2.3, 0.45, 0.05)
        shelf.data.materials.append(mahogany_mat)

        # Varied book spine rows on each shelf
        for b in range(12):
            x_pos = -0.95 + b * 0.17
            height = 0.32 + (b % 3) * 0.04
            bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x_pos, 0.05, z_pos + height/2 + 0.025))
            book = bpy.context.active_object
            book.scale = (0.14, 0.35, height)
            book.data.materials.append(books_leather if b % 2 == 0 else books_gold)

    # Rolling ladder brass guide rail at top
    bpy.ops.mesh.primitive_cylinder_add(radius=0.025, depth=2.4, location=(0, -0.28, 2.7))
    rail = bpy.context.active_object
    rail.rotation_euler = (0, math.radians(90), 0)
    rail.data.materials.append(brass_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Audiobook_Bookshelf"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_gramophone(out_path):
    reset_scene()
    wood_mat = create_pbr_material("Gramophone_Rosewood", (0.15, 0.05, 0.02, 1.0), metallic=0.03, roughness=0.3)
    brass_mat = create_pbr_material("Spun_Brass_Horn", (0.9, 0.72, 0.22, 1.0), metallic=0.95, roughness=0.18)
    vinyl_mat = create_pbr_material("Shellac_78_Record", (0.02, 0.02, 0.02, 1.0), metallic=0.1, roughness=0.25)

    # Wooden Cabinet Base
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.15))
    base = bpy.context.active_object
    base.scale = (0.5, 0.5, 0.3)
    base.data.materials.append(wood_mat)

    # Turntable Platter
    bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=0.02, location=(0, 0, 0.31))
    platter = bpy.context.active_object
    platter.data.materials.append(vinyl_mat)

    # Spun Brass Horn (flared cone + bell rim)
    bpy.ops.mesh.primitive_cone_add(radius1=0.28, radius2=0.03, depth=0.5, location=(0.1, 0.05, 0.65))
    horn = bpy.context.active_object
    horn.rotation_euler = (math.radians(-35), math.radians(25), 0)
    horn.data.materials.append(brass_mat)

    # Tone Arm
    bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.25, location=(-0.1, 0.1, 0.36))
    arm = bpy.context.active_object
    arm.rotation_euler = (0, math.radians(75), math.radians(30))
    arm.data.materials.append(brass_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Audiobook_Gramophone"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

def build_chesterfield_armchair(out_path):
    reset_scene()
    leather_mat = create_pbr_material("Oxblood_Chesterfield_Leather", (0.2, 0.04, 0.03, 1.0), metallic=0.05, roughness=0.4)
    studs_mat = create_pbr_material("Brass_Tacks", (0.85, 0.65, 0.2, 1.0), metallic=0.9, roughness=0.2)
    wood_mat = create_pbr_material("Turned_Leg_Walnut", (0.1, 0.04, 0.02, 1.0), metallic=0.02, roughness=0.35)

    # Deep Seat Cushion
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.45))
    seat = bpy.context.active_object
    seat.scale = (0.9, 0.85, 0.3)
    seat.data.materials.append(leather_mat)

    # Deep Buttoned Backrest
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0.35, 0.75))
    back = bpy.context.active_object
    back.scale = (0.9, 0.25, 0.7)
    back.data.materials.append(leather_mat)

    # Rolled Scroll Arms (Left & Right)
    for x_side in [-0.5, 0.5]:
        bpy.ops.mesh.primitive_cylinder_add(radius=0.14, depth=0.85, location=(x_side, 0, 0.6))
        arm = bpy.context.active_object
        arm.rotation_euler = (math.radians(90), 0, 0)
        arm.data.materials.append(leather_mat)

    # 4 Turned Wooden Legs
    for lx in [-0.38, 0.38]:
        for ly in [-0.35, 0.35]:
            bpy.ops.mesh.primitive_cylinder_add(radius=0.04, depth=0.2, location=(lx, ly, 0.1))
            leg = bpy.context.active_object
            leg.data.materials.append(wood_mat)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.join()
    obj = bpy.context.active_object
    obj.name = "Audiobook_Chesterfield_Armchair"
    set_pivot_bottom_center(obj)
    export_draco_glb(out_path)

if __name__ == "__main__":
    base_dir = r"C:\Users\ELI\Desktop\Petros-music\public\models\audiobook"
    build_grand_bookshelf(os.path.join(base_dir, "audiobook_bookshelf.glb"))
    build_gramophone(os.path.join(base_dir, "audiobook_gramophone.glb"))
    build_chesterfield_armchair(os.path.join(base_dir, "audiobook_chesterfield.glb"))
    print("ALL AUDIOBOOK HERO MODELS GENERATED SUCCESSFULLY!")
