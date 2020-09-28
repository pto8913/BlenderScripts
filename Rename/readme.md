# Rename_Bone_and_all_of_the_action_Bone.py
japanese : https://pto8913.hatenablog.com/entry/2020/09/28/132306<br>

@rename_bone_armature_name : The bone name you want to rename. <br>
@rename_bone_name_list : A list of tuples with the name you want to change and the new name. <br>
e.g. <br>
```python
rename_bone_name_list = [
   ("Tail.005", "Tail"),
   ("Tail.006", "Tail.001")
]
```

Use `Init_rev_bone_name_list` if you have manually changed the bone name of the action up to the halfway point.<br>
Please remove comments at line 32.<br>
```python
def Init_rev_bone_name_list():
    return [(b, a) for a, b in rename_bone_name_list]
    
rev_rename_bone_name_list = Init_rev_bone_name_list()
```

NOTE: <br>
For all animations, an operation is performed to change the pose of the armature and rename the bones, <br>
so the If you are editing multiple armatures in the same file, <br>
you can use Make a backup, create another file and append it before doing so, etc. <br>
