# Automatonophobia

import time

print("You wake up in a dark room, lit only by the light of the moon shining through the window and the red glow from the alarm clock.")
print("1 - Check time\n2 - Get up\n3 - Stay in bed")
shouldContinue = False
while not shouldContinue:
    var = input("> ")
    if var == "1":
        print("It is 3:00 AM")
    elif var == "2":
        shouldContinue = True
    elif var == "3":
        print("You attempt to go back to sleep. You close your eyes but hear a loud thud.")
        shouldContinue = True
shouldContinue = False
print("You get out of bed.") ; time.sleep(1)
print("The cold, seemingly wood floors creak below your feet.")  ; time.sleep(1)
if var !="3":
    print("You hear a thud.")  ; time.sleep(1)
print("1 - Check time\n2 - Go back to bed\n3 - Turn on the light")

inBed = False
isSpotted = False

while not shouldContinue:
    var = input("> ")
    if var == "1":
        print("It is 3:02 AM")
    elif var == "2":
        print("You go back and sit in your bed. Ignoring the fact you heard a thud.") ; time.sleep(1)
        print("Only the moon illuminates the shadowy figure that is standing in the doorway.") ; time.sleep(1)
        print("Fortunately, the figure does not seem to notice you.") ; time.sleep(1)
        inBed = True
        shouldContinue = True
    elif var == "3":
        print("You walk towards the what you think is the light switch.") ; time.sleep(1)
        print("As you do the door creaks open. There is no light on the other side.") ; time.sleep(1)
        print("Standing in the doorway is a figure with no hair. From what you can tell they stand near 7 feet tall.") ; time.sleep(1)
        print("Their lanky arms reach down to their knees and their eyes, glow a deep bloody red. Redder than any red you have seen.") ; time.sleep(1)
        isSpotted = True
        shouldContinue = True
shouldContinue = False
if inBed:
    print("The tall, lanky creature walks around the room.") ; time.sleep(1)
    print("Its eyes glow a deep bloody red. Redder than any red you have seen before.") ; time.sleep(1)
    print("You cower beneath your blankets and wait for what seems like eternity.") ; time.sleep(1)
    print("Finally, the creature leaves, leaving the door ajar.") ; time.sleep(1)
    print("1 - Check the time\n2 - Chase the creature\n3 -  Grab the alarm clock")
    while not shouldContinue:
        var = input("> ")
        if var == "1":
            print("It is 3:08 AM")
        if var == "2":
            print("You get up out of bed and chase the creature.")
            shouldContinue = True
        if var == "3":
            grabbedClock = True
            if not grabbedClock:
                print("You managed to unplug the clock and grab it.")
            else:
                print("You already grabbed the clock.")
    shouldContinue = False


if isSpotted:
    print("The creature walks swiftly towards you and swipes at you with its clawed hands.") ; time.sleep(1)
    print("You fall to the floor and black out.") ; time.sleep(1)
