import random

limit = 100000
attempts = 0
brute = 0

num = random.randint(0, limit)
notSolved = True

while notSolved:
    attempts+=1

    
    if attempts < limit:
        condition = random.randint(0, limit)
    else:
        brute+=1
        condition = brute

    if condition == num:
            notSolved = False
    
    #if i == num:
        #notSolved = False

grade = round(limit / attempts, 2)
print(f"Num Found: {num}")
print(f"Limit: {limit}")
print(f"Grade: {grade}")
