## dont change anything, it is working fine

import os
import pwd

accounts = [{'name':'Ali','role':'HR Manager','password':"alibaba@S1"},{'name':'SALEM','role':'CEO','password':"alibaba@S1"},{'name':'RAGHED','role':'HR Specialist','password':"alibaba@S1"},{'name':'SARAH','role':'Sales representative','password':"alibaba@S1"},{'name':'ABDULLAH','role':'Shipping','password':"alibaba@S1"},{'name':'DEEM','role':'HR Specialist','password':"alibaba@S1"},{'name':'KHALID','role':'Finance Manager','password':"alibaba@S1"},{'name':'NORAH','role':'Finance Specialist','password':"alibaba@S1"},{'name':'RANEEM','role':'Sales representative','password':"alibaba@S1"},{'name':'AHMED','role':'Shipping','password':"alibaba@S1"},{'name':'OUDI','role':'Shipping','password':"alibaba@S1"},{'name':'ABDULAZIZ','role':'Shipping','password':"alibaba@S1"},{'name':'NAIF','role':'Sales representative','password':"alibaba@S1"},{'name':'GHADA','role':'HR Manager','password':"alibaba@S1"},{'name':'MOHAMMED','role':'shipping','password':"alibaba@S1"},{'name':'HANAN','role':'Sales representative','password':"alibaba@S1"}]



def add_user():
    for i in accounts:
        username = i["name"]
        password = i["password"]
        role = i["role"]
        try:
            pwd.getpwnam(username)
            print('Username', username, 'is existed.')
        except:
            print('Username', username, 'does not exist.')
            if role != "CEO":
                os.system(f"sudo useradd -p  {password} -c role -e 2025-01-01 {username}")
            else:
                os.system(f"sudo useradd -p  {password} -c role {username}")
add_user()