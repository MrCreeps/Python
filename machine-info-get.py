import platform
import psutil
import os
import getpass
import datetime

# Get the processor name
processor_name = platform.processor()
print("Processor name:", processor_name)

# Get the current processor speed
processor_speed = psutil.cpu_freq().current
print("Processor speed:", processor_speed, "MHz")

# Get the system virtual memory information
svmem = psutil.virtual_memory()

# Get the operating system name
os_name = platform.system()
print("Operating system:", os_name)

# Check if the operating system is a Windows operating system
if os.name == "nt":
    print("The operating system is a Windows operating system.")
else:
    print("The operating system is not a Windows operating system.")

# Get the signed-in user
signed_in_user = getpass.getuser()
print("Signed-in user:", signed_in_user)

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Open the file in write mode
with open("info.txt", "w") as file:
  # Convert the variables to strings and write them to the file
  file.write("Processor name: " + str(processor_name) + "\n")
  file.write("Processor speed: " + str(processor_speed) + " MHz" + "\n")
  file.write("Operating system: " + str(os_name) + "\n")
  if os.name == "nt":
    file.write("The operating system is a Windows operating system." + "\n")
  else:
    file.write("The operating system is not a Windows operating system." + "\n")
  file.write("Signed-in user: " + str(signed_in_user) + "\n")
  file.write("Current date and time: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
