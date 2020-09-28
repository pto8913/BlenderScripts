import bpy

rename_bone_armature_name = "hoge"
""" 
[
    (current_bone_name, new_bone_name),
         ~~
]
"""
rename_bone_name_list = [
    ("Tail.006", "Tail"),
    ("Tail.007", "Tail.001"),
    ("Tail.008", "Tail.002"),
    ("Tail.009", "Tail.003"),
    ("Tail.010", "Tail.004"),
    ("Tail.011", "Tail.005")
]

def get_object(name : str):
    return bpy.data.objects[name]
    
armature = get_object(rename_bone_armature_name)

if armature is None:
    return

bpy.ops.object.mode_set(mode = "EDIT")

def rename_bones(): 
    for name, nname in rename_bone_name_list:
        pb = armature.pose.bones.get(name)
        #print(pb)
        if pb is None:
            continue
        pb.name = pb.name.replace(name, nname)
        print(pb.name)

for anim in bpy.data.actions:
    print(armature.animation_data.action)
    armature.animation_data.action = anim
    rename_bones()
