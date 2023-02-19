import os
import time

print("""Welcome to Papa Pete's Pizzeria, new hire!
    Here at Papa Pete's Pizzeria, we value our staff like family.
    And as all good families do, we make sure to make sure we all contribute as much as we can!
    """)
name = input("What is your first name, new hire? ")
lastName = input(f"Hello {name}, what is your last name? ")
age = int(input("And you are how old? "))
if age < 16:
    print(f"Sorry, but here at Papa Pete's Pizzeria we cannot accept those under the age of 16. You need to wait {16-age} more years.")
    exit()
elif age > 50 and age < 120:
    print(f"Sorry boomer. But you are too old to work here. As a {age} year old, you are at risk in dying within the next {70-age} to {120-age} years.")
    exit()
elif age >= 120:
    print("You should be dead by now you insanely old person.")
    exit()
else:
    pass
homeTown = input("What is your home town? ")
confirmation = input(f"""
    Full Name: {name} {lastName}
    Age: {age}
    Home Town: {homeTown}
    
Are the above details correct? (y/n) """)
if confirmation == "y":
    pass
else:
    print("Too bad.")

input("You will be asked 5 questions. Based on your answer, a specific position will be assigned to you. Press `Enter` to start.") ; os.system("cls")
input("Question 1: What is your mother's maiden name OR the name of your first pet? ") ; os.system("cls")
input("Question 2: How would you handle a customer complaint about their pizza order? ") ; os.system("cls")
input("Question 3: What would you do if a customer has a specific dietary restriction or allergy and needs to modify their order? ") ; os.system("cls")
input("Question 4: How would you react upon hearing a rumor that Papa Pete's Pizzeria contains a hidden network of underground tunnels leading across the city? ") ; os.system("cls")
input("Question 5: How would you ensure that the kitchen and dining area are kept clean and organized during your shift? ") ; os.system("cls")
print("Based on your inputs... your idea position is...")
time.sleep(1)
print("AFTER HOURS JANITOR")
time.sleep(0.5)
print(f"\nWelcome to the Papa Pete's Pizzeria family, {name} {lastName}. You start on Monday at 9:00 PM.")
input("\n\n\nPress `Enter` to continue.")  ; os.system("cls")
