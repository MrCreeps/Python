import os
import hashlib
import datetime
import random
import time
import socket

should_have_correct_username = True
#should_have_correct_username = False

def encrypt(string):
    sha512 = hashlib.sha512()
    sha512.update(string.encode())
    return sha512.hexdigest()

try:

    directory = "C:\\naos\\"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Successfully created main directory")
        
    directory = "C:\\naos\\rcap"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Successfully created directory 'rcap'")
        
    directory = "C:\\naos\\exfs"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Successfully created directory 'exfs'")
    
    correct_username = "root"
    default_password = correct_username
    username = "NAOS"
    try:
        with open("C:\\naos\\rootpswd", "r") as f:
            correct_password = f.read()
    except FileNotFoundError:
        with open("C:\\naos\\rootpswd", "w") as f:
            f.write(encrypt(default_password))
            correct_password = f.read()
    try:
        with open("C:\\naos\\motd", "r") as f:
            motd = f.read()
    except FileNotFoundError:
        with open("C:\\naos\\motd", "w") as f:
            f.write("")
            motd = f.read()
      
    
    try:
        with open("C:\\naos\\clrs", "r") as f:
            colors = f.readlines()
            colors = [color.strip() for color in colors]
    except FileNotFoundError:
        with open("C:\\naos\\clrs", "w") as f:
            f.write("38;2;255;0;0m\n")
            f.write("38;2;50;205;50m\n")
            f.write("36m\n")
            f.write("38;2;255;165;0m\n")
            f.write("0m")
            colors = f.readlines()
            colors = [color.strip() for color in colors]
    
    red = "\033[" + colors[0]
    green = "\033[" + colors[1]
    cyan = "\033[" + colors[2]
    orange = "\033[" + colors[3]
    reset = "\033[" + colors[4]

    error_msg = red+"You do not have permission to use this command"+reset

    print("Welcome to "+green+"NAOS.S, "+reset+"a version of NAOS made with the "+red+"Spyder IDE"+reset)
    print("NAOS stands for "+green+"'Not Actually an Operating System'"+reset)
    print("Use the "+cyan+"'history'"+reset+" command to learn more")
    print("Use the "+cyan+"'help'"+reset+" command for a list of commands")
    if motd != "":
        print(orange+"Message of the Day: " + reset + motd)
        
    while True:
        with open("C:\\naos\\rootpswd", "r") as f:
            correct_password = f.read()
            
        if (should_have_correct_username):
            username = correct_username
            
        cmd = input("\n" + cyan + username + reset + "<< ")
        
        if cmd == "history":
            print("NAOS.S is programmed completely in Python")
            print("These first lines of NAOS.S code were written on 1/13/2023")
            print("There are other versions of NAOS that may never be released")
        if cmd == "help":
            print(cyan+"help"+reset+" - This command")
            print(cyan+"history"+reset+" - Gives some information on the history of NAOS.S")
            print(cyan+"leave"+reset+" - Exits the program")
            print(cyan+"login"+reset+" - Prompts the user to input a username and password")
            print(cyan+"logout"+reset+" - Logs the user out")
            print(cyan+"time"+reset+" - Prints time")
            print(cyan+"sum"+reset+" - Prompts the user twice to enter a number, then prints the sum (use negatives for subtraction)")
            print(cyan+"mul"+reset+" - Prompts the user twice to enter a number, then prints the product")
            print(cyan+"div"+reset+" - Prompts the user twice to enter a number, then prints the quotient")
            print(cyan+"exp"+reset+" - Prompts the user twice to enter a number, then prints the power")
            print(cyan+"rcap"+reset+" - Prompts the user to enter a string and a percentage of the letters to capitalize")
            print(cyan+"ipget"+reset+" - Prints the public and private IPv4 and IPv6 addresses")
            print(cyan+"dgadd"+reset+" - Prompts the user to enter an integer, then it will print the sum of all the digits")
            print(cyan+"getmotd"+reset+" - Prints the message of the day")
            print(cyan+"ref"+reset+" - Prompts the user to enter the name of a .py file to run")
            if username == correct_username:
                print(orange+"password"+reset+" - Changes the root account password")
                print(orange+"reset"+reset+" - Resets the root account password")
                print(orange+"setmotd"+reset+" - Prompts the user for a string to set the motd")
                print(orange+"sudel rcap"+reset+" - Deletes the contents of the rcap (random capitalization) folder")
                print(orange+"sudel exfs"+reset+" - Deletes the contents of the exfs (external files) folder")
        if cmd == "leave": print("Exiting!"); break
        if cmd == "login":
            username = input("login<< ")
            password = input(username + "<< ")
            password = encrypt(password)
            if username == correct_username:
                if password == correct_password:
                    print("Sucessfully logged in as " + username + "!")
                else:
                    print("Incorrect password")
                    username = "NAOS"
            else:
                print("Incorrect username")
                username = "NAOS"
        if cmd == "logout":
            if username != "NAOS":
                print("Goodbye " + username + "!")
                username = "NAOS"
                print("Sucessfully logged out")
            else:
                print("User not logged in")
        if cmd == "password":
            if username == correct_username:
                entered_password = encrypt(input("password?<< "))
                print(reset)
                if entered_password == correct_password:
                    new_password = input("newpassword?<< ")
                    confirmed_password = input("confirm?<< ")
                    if confirmed_password == new_password:
                        correct_password = encrypt(new_password)
                        with open("C:\\naos\\rootpswd", "w") as f:
                            f.write(encrypt(new_password))
                        print("New password saved!")
                    else:
                        print("Passwords did not match")
                else:
                    print("Incorrect password")
            else:
                print(error_msg)
        if cmd == "reset":
            if username == correct_username:
                with open("C:\\naos\\rootpswd", "w") as f:
                    f.write(encrypt(default_password))
                print("Password reset")
            else:
                print(error_msg)
        if cmd == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S %p %Z")
            print(current_time)
        if cmd == "sum":
            num1 = int(input("add1<< "))
            num2 = int(input("add2<< "))
            print(num1+num2)
        if cmd == "mul":
            num1 = int(input("mprl<< "))
            num2 = int(input("mcnd<< "))
            print(num1*num2)
        if cmd == "div":
            num1 = int(input("numr<< "))
            num2 = int(input("denm<< "))
            print(num1/num2)
        if cmd == "exp":
            num1 = int(input("base<< "))
            num2 = int(input("expo<< "))
            print(num1**num2)
        if cmd == "rcap":
            string = input("Enter string: ")
            percentage = float(input("\nEnter percentage of letters to capitalize: "))
            percentage = percentage/100
            result = ""
            for i in range(len(string)):
                if random.random() < percentage:
                    result += string[i].upper()
                else:
                    result += string[i]
            print(result)
            will_save = input("\nSave to file? (y/n): ")
            file_date = str(time.time())
            if will_save.lower() == "y":
                with open("C:\\naos\\rcap\\" + file_date + ".txt", "w") as file:
                    file.write(result)
                    print("Printed the text to a file in C:\\naos\\rcap")
        if cmd == "ipget":
            try:
                public_ipv4 = socket.gethostbyname(socket.gethostname())
                public_ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                private_ipv4 = s.getsockname()[0]
                s.close()
                s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
                s.connect(("2001:4860:4860::8888", 80))
                private_ipv6 = s.getsockname()[0]
                s.close()
                print("Public IPv4:", public_ipv4)
                print("Public IPv6:", public_ipv6)
                print("Private IPv4:", private_ipv4)
                print("Private IPv6:", private_ipv6)
            except:
                print("IP could not be retrieved")
        if cmd == "dgadd":
            integer = input("Enter an integer: ")
            result = 0
            for number in integer:
                result = result + int(number)
            print(result)
        if cmd == "setmotd":
            if username == correct_username:
                motd = input("Enter new motd: ")
                with open("C:\\naos\\motd", "w") as f:
                    f.write(motd)
                print("The message of the day has been updated")
            else:
                print(error_msg)
        if cmd == "getmotd":
            print(orange+"Message of the Day: " + reset + motd)
        if cmd == "ref":
            print(red+"USE WITH CAUTION"+reset)
            file_to_run = input(orange+"ref<<"+reset+" ")
            exec(open("C:\\naos\\exfs\\" + file_to_run + ".py").read())
        if cmd == "sudel rcap":
            if username == correct_username:
                will_del = input("Delete saved rcap files? (y/n): ")
                if will_del.lower() == "y":
                    password = encrypt(input("password?<< "))
                    if password == correct_password:
                        for file in os.listdir("C:\\naos\\rcap"):
                            file_path = os.path.join("C:\\naos\\rcap", file)
                            if os.path.isfile(file_path):
                                os.unlink(file_path)
                                print("Deleted file " + file_path)
                    else:
                        print("Incorrect password")
            else:
                print(error_msg)
        if cmd == "sudel exfs":
            if username == correct_username:
                will_del = input("Delete external files? (y/n): ")
                if will_del.lower() == "y":
                    password = encrypt(input("password?<< "))
                    if password == correct_password:
                        for file in os.listdir("C:\\naos\\exfs"):
                            file_path = os.path.join("C:\\naos\\exfs", file)
                            if os.path.isfile(file_path):
                                os.unlink(file_path)
                                print("Deleted file " + file_path)
                    else:
                        print("Incorrect password")
            else:
                print(error_msg)

            
except KeyboardInterrupt:
    print("\nUser exited the program externally")
except FileNotFoundError:
    print("\n"+red+"A fatal exception occurred: "+orange+"Critical file or folder in unavailable"+reset)
except OverflowError:
    print("\n"+red+"A fatal exception occurred: "+orange+"Number too big, think smaller"+reset)
except ValueError:
    print("\n"+red+"A fatal exception occurred: "+orange+"Error related to variable type, not a number?"+reset)
except ZeroDivisionError:
    print("\n"+red+"A fatal exception occurred: "+orange+"Tried to divide by 0"+reset)
except UnicodeEncodeError:
    print("\n"+red+"A fatal exception occurred: "+orange+"Could not parse unkown character(s)"+reset)
except PermissionError:
    print("\n"+red+"A fatal exception occurred: "+orange+"External permission error occurred"+reset)
except OSError:
    print("\n"+red+"A fatal exception occurred: "+orange+"Something bad happened. It's not us, it's you."+reset)
