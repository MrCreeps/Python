# NAOS.X
# Newest version of NAOS, previous... NAOS.S (Spyder)

# VSCODE
# Pthon 3.11.2
# By MrCreeps / Caden

vers = "0.0.1"

top_level_user = "toplevel"
default_user = "default"
current_user = default_user

print(f"NAOS.X {vers}\n\n")
current_user = input("Username? ")

while True:
    cmd = input(f"{current_user}>> ")