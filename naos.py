# NAOS.X
# Newest version of NAOS, previous... NAOS.S (Spyder)

# VSCODE
# Pthon 3.11.2
# By MrCreeps / Caden

##############################
#####   Initialization   #####
##############################

import os

vers = "0.0.5"
mainLoop = True
quickLogin = True
funUsers = True
adminEnabled = True

# Temporary
passwords = {
    "user" : "123"
}

if funUsers:
    passwords["snakamoto"] = "btc"
    passwords["vbuterin"] = "eth"
    passwords["rulbricht"] = "dpr"
    passwords["esnowden"] = "wiki"
if adminEnabled:
    passwords["admin"] = "123"
if quickLogin:
    passwords[""] = ""

class wrongPassword(Exception):
    pass
class userExits(Exception):
    pass

print(f"NAOS.X {vers}\n\n")

########################
#####   Commands   #####
########################

def clear():
    os.system("cls")
    
def tempuser():
    temp_username = input("Temporary username? ")
    temp_password = input(f"Username for {temp_username}? ")
    if temp_username not in passwords:
        passwords[temp_username] = temp_password
        print(f"New temporary user with password '{temp_password}' and username '{temp_username}' created!")
    else:
        raise userExists()
        
def logout():
    print("Successfully logged out!")
    user = input("Username? ")
    input_password = input("Password? ")
    if user not in passwords or input_password != passwords[user]:
        raise wrongPassword()
    return user

def listall():
    for user in passwords:
        print (user)
        
def userpolicies():
    print(f"""quickLogin = {quickLogin}
funUsers = {funUsers}
adminEnabled = {adminEnabled}""")

#########################
#####   Main Loop   #####
#########################

try:
    user = input("Username? ")
    
    input_password = input("Password? ")
    if user not in passwords or input_password != passwords[user]:
        raise wrongPassword()

    while mainLoop:
        cmd = input(f"{user}>> ")
        if cmd == "clear": clear()
        if cmd == "tempuser": tempuser()
        if cmd == "logout": user = logout()
        if cmd == "listall" and user == "admin": listall()
        if cmd == "userpolicies" and user == "admin": userpolicies()

except wrongPassword: print("Incorrect username or password")
except userExists: print("Cannot add user as user already exists")
except: exit()
