# NAOS.X
# Newest version of NAOS, previous... NAOS.S (Spyder)

# VSCODE
# Pthon 3.11.2
# By MrCreeps / Caden

##############################
#####   Initialization   #####
##############################

import os

vers = "0.0.6"
mainLoop = True

# Temporary password storage initialization
# Better solutuin not yet implemented
passwords = {"user" : "123"}

#############################
#####   User Policies   #####
#############################

quickLogin = True
if quickLogin:
    passwords[""] = ""

funUsers = True
if funUsers:
    passwords["snakamoto"] = "btc"
    passwords["vbuterin"] = "eth"
    passwords["rulbricht"] = "dpr"
    passwords["esnowden"] = "wiki"

adminEnabled = True
if adminEnabled:
    passwords["admin"] = "123"

#############################
#####   Custom Errors   #####
#############################
    
class wrongPasswordError(Exception):
    pass
class userExistsError(Exception):
    pass

########################
#####   Commands   #####
########################

def clear():
    os.system("cls")
    
def tempuser():
    tempUsername = input("Temporary username? ")
    tempPassword = input(f"Username for {tempUsername}? ")
    if tempUsername not in passwords:
        passwords[tempUsername] = tempPassword
        print(f"New temporary user with password '{tempPassword}' and username '{tempUsername}' created!")
    else:
        raise userExistsError()
        
def logout():
    print("Successfully logged out!")
    user = input("Username? ")
    inputPassword = input("Password? ")
    if user not in passwords or inputPassword != passwords[user]:
        raise wrongPasswordError()
    return user

def listall():
    for user in passwords:
        print (user)
        
def userpolicies():
    print(f"""quick_login = {quickLogin}
funUsers = {funUsers}
adminEnabled = {adminEnabled}""")

#########################
#####   Main Loop   #####
#########################

print(f"NAOS.X {vers}\n\n")

try:
    user = input("Username? ")
    
    inputPassword = input("Password? ")
    if user not in passwords or inputPassword != passwords[user]:
        raise wrongPasswordError()

    while mainLoop:
        cmd = input(f"{user}>> ")
        if cmd == "clear": clear()
        if cmd == "tempuser": tempuser()
        if cmd == "logout": user = logout()
        if cmd == "listall" and user == "admin": listall()
        if cmd == "userpolicies" and user == "admin": userpolicies()

except wrongPasswordError: print("Incorrect username or password")
except userExistsError: print("Cannot add user as user already exists")
except: exit()
