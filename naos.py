# NAOS.X
# Newest version of NAOS, previous... NAOS.S (Spyder)

# VSCODE
# Pthon 3.11.2
# By MrCreeps / Caden

##############################
#####   Initialization   #####
##############################

import os
import json
import time

vers = "0.1.0"
mainLoop = True

# Temporary password storage initialization
# Better solutuin not yet implemented
passwords = {"user" : "123"}

#############################
#####   User Policies   #####
#############################

with open("userpolicies.json", "r") as file:
    userPolicies = json.load(file)

quickLogin = userPolicies["quickLogin"]
if quickLogin:
    passwords[""] = ""

funUsers = userPolicies["funUsers"]
if funUsers:
    passwords["snakamoto"] = "btc"
    passwords["vbuterin"] = "eth"
    passwords["rulbricht"] = "dpr"
    passwords["esnowden"] = "wiki"

adminEnabled = userPolicies["adminEnabled"]
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
    tempPassword = input(f"Password for {tempUsername}? ")
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
    print(f""" 1 = True ; 0 = False
quickLogin = {quickLogin}
funUsers = {funUsers}
adminEnabled = {adminEnabled}""")

def setpolicy():
    policyName = input("Policy to change? ")
    if userPolicies[policyName] == 0:
        userPolicies[policyName] = 1
    else:
        userPolicies[policyName] = 0
    with open("userpolicies.json", "w") as file:
        json.dump(userPolicies, file)

def shutdown():
    print("Shutting down in 3 seconds...")
    time.sleep(3)
    exit()

#####################################
#####   Main Loop Definitions   #####
#####################################

def restart():
    print("Restarting in 3 seconds...")
    time.sleep(3)
    os.system("cls")
    main()

def main():
    print(f"NAOS.X {vers}\n\n")
    if quickLogin: print("Quick Login is enabled. Press enter twice to login.")

    try:
        user = input("Username? ")
        
        inputPassword = input("Password? ")
        if user not in passwords or inputPassword != passwords[user]:
            raise wrongPasswordError()

        while mainLoop:
            cmd = input(f"{user}>> ")
            if cmd == "help": pass
            elif cmd == "clear": clear()
            elif cmd == "tempuser": tempuser()
            elif cmd == "logout": user = logout()
            elif cmd == "listall" and user == "admin": listall()
            elif cmd == "userpolicies" and user == "admin": userpolicies()
            elif cmd == "setpolicy" and user == "admin": setpolicy()
            elif cmd == "restart": restart()
            elif cmd == "shutdown": shutdown()
            else: print("Invalid command or permission level")

    except wrongPasswordError: print("Incorrect username or password") ; restart()
    except userExistsError: print("Cannot add user as user already exists") ; restart()
    except KeyError: print("Policy not available.") ; restart()
    except:
        restart()

###########################
#####   Entry Point   #####
###########################

if __name__ == "__main__":
    main()
