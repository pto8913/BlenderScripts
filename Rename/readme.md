# Rename_Bone_and_all_of_the_action_Bone.py
japanese : https://pto8913.hatenablog.com/entry/2020/09/28/132306<br>

# Table of content
- [details rename_bone_name_list](#details_rename_bone_name_list)<br>
- [NOTE](#NOTE)<br>
- [Commentary](#Commentary)<br>

# details_rename_bone_name_list
@rename_bone_armature_name : The bone name you want to rename. <br>
@rename_bone_name_list : A list of tuples with the name you want to change and the new name. <br>
e.g. <br>
```python
rename_bone_name_list = [
   ("Tail.005", "Tail"),
   ("Tail.006", "Tail.001")
]
```

# NOTE
NOTE: <br>
For all animations, an operation is performed to change the pose of the armature and rename the bones, <br>
so the If you are editing multiple armatures in the same file, <br>
you can use Make a backup, create another file and append it before doing so, etc. <br>

# Commentary
**The bone names registered to the animation will automatically update the bone names registered to the animation by renaming the original bone with the pose active. **<br>.

However, we need to repeat this process for all of our animations as they are only updated in the active pose. <br>.

When the process is repeated, the original bone name has already been changed, so the original bone name is required to change the registered bone name in the animation. <br>.

So, `Init_rev_bone_name_list()` is used to create a list of unchanged bone names. <br>.

The update process is performed by using the list of unchanged bone names, renaming the active pose to the unchanged bone name, and then renaming it to the new bone name. <br>.
