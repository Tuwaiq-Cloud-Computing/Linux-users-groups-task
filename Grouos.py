import grp, os
groups_to_be_added = ["HR", "CEO", "Sales", "Shiping", "Manager", "Finance"]
def add_group():
	grep_groups = grp.getgrall()
	existed_groups = []
	for group in grep_groups:
		existed_groups.append(group[0])
	#print(existed_groups)
	for g in groups_to_be_added:
        	add_group = g
        	if add_group in existed_groups:
        		print("Group is existed")
       		else:
        		os.system(f"sudo groupadd {add_group}")
        		print("Group", add_group, "is added")
add_group()
