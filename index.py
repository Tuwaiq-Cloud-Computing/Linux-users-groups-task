import os
import crypt


encPass= crypt.crypt("alibaba@s1","22")
ExpirationDate="2025-01-01"
user_groups = [
	{
		"groupName":"CEO",
		"users":["Ali"]
	},
	{
		"groupName":"Manager",
		"users":["Salem"]
	},
	{
		"groupName":"HR",
		"users":["Salem","Norah","Deem"]
	},
	{
		"groupName":"Shipping",
		"users":["Sara","Naif"]
	},
	{
		"groupName":"Sales",
		"users":["Hanan","Khaled"]
	}

]


for group in user_groups:
	os.system(f'groupadd {group["groupName"]}')
	for user in group["users"]:
		os.system(f'useradd {user}  --groups {group["groupName"]} --password {encPass} --expiredate {ExpirationDate}')
		




