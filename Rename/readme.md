# Rename_Bone_and_all_of_the_action_Bone.py

@rename_bone_armature_name : The bone name you want to rename. <br>
@rename_bone_name_list : A list of tuples with the name you want to change and the new name. <br>
e.g. <br>
```python
rename_bone_name_list = [
   ("Tail.005", "Tail"),
   ("Tail.006", "Tail.001")
]
```

NOTE: <br>
For all animations, an operation is performed to change the pose of the armature and rename the bones, <br>
so the If you are editing multiple armatures in the same file, <br>
you can use Make a backup, create another file and append it before doing so, etc. <br>

japanese : https://pto8913.hatenablog.com/entry/2020/09/28/132306<br>
my cheat sheet : https://pto8913.hatenablog.com/entry/2020/09/28/134236<br>