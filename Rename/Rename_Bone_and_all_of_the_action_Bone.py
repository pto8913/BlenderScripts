import bpy
from typing import List, Tuple

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

bpy.ops.object.mode_set(mode = "EDIT")

rev_rename_bone_name_list = []
# Use this if you have manually changed the bone name of the action up to the halfway point.
def Init_rev_bone_name_list():
    return [(b, a) for a, b in rename_bone_name_list]
    
# rev_rename_bone_name_list = Init_rev_bone_name_list()

def rename_bones():
    __rename_bones(rev_rename_bone_name_list)
    __rename_bones(rename_bone_name_list)
        
def __rename_bones(TargetArr : List[Tuple]):
    for name, nname in TargetArr:
        pb = armature.pose.bones.get(name)
        if pb is None:
            continue
        pb.name = pb.name.replace(name, nname)

for anim in bpy.data.actions:
    armature.animation_data.action = anim
    rename_bones()
