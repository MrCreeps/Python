# NAOS.X
# Newest version of NAOS, previous... NAOS.S (Spyder)

# VSCODE
# Pthon 3.11.2
# By MrCreeps / Caden

vers = "0.0.3"
mainLoop = True

# Temporary
passwords = {
    "" : "",
    "user" : "123",
    "admin" : "123",
    "snakamoto" : "btc",
    "vbuterin" : "eth",
    "rulbricht" : "dpr",
    "esnowden" : "wiki"
}

class wrongPassword(Exception):
    pass

print(f"NAOS.X {vers}\n\n")

try:
    user = input("Username? ")
    
    input_password = input("Password? ")
    if user not in passwords or input_password != passwords[user]:
        raise wrongPassword()

    while mainLoop:
        cmd = input(f"{user}>> ")

except wrongPassword: print("Incorrect Username or Password")
except: exit()
