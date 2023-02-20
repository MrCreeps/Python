# NAOS.X
# Newest version of NAOS, previous... NAOS.S (Spyder)

# VSCODE
# Pthon 3.11.2
# By MrCreeps / Caden

##############################
#####   Initialization   #####
##############################

import os

vers = "0.0.4"
mainLoop = True
quickLogin = True

# Temporary
passwords = {
    "user" : "123",
    "admin" : "123",
    "snakamoto" : "btc",
    "vbuterin" : "eth",
    "rulbricht" : "dpr",
    "esnowden" : "wiki"
}

if quickLogin:
    passwords[""] = ""

class wrongPassword(Exception):
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
    passwords[temp_username] = temp_password
    print(f"New temporary user with password '{temp_password}' and username '{temp_username}' created!")
        
def logout():
    print("Successfully logged out!")
    user = input("Username? ")
    input_password = input("Password? ")
    if user not in passwords or input_password != passwords[user]:
        raise wrongPassword()
    return user

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

except wrongPassword: print("Incorrect Username or Password")
except: exit()
