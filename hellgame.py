print("Welcome to hell!")
name = input("What is your name victim: ")
print(f"Jk i actually couldnt care less loser {name}. ")
print('''

Your goal is to somehow find a way out so...

good luck''')

input("Do you wish to continue? y/n: ")
print("Not that you even had a choice. Congratulations you chose to play!")

sword = input("POV: You see demons and hellbats all around... but you see a sword to your right! Do you wish to grab it? y/n:")
if sword == "y":
    print("You grab the sword and fight off the demons and bats that surround you. ")
else:
    print("You do not grab the sword. The demons and hellbats attack you and eat you. You die.")
    exit()
print("POV: You hear a sinester voice say, 'Ooooooh so you have passed my first test... my next ones will not be so easy...'")
path = input('''

You start walking foward and you come to a a fork in the road. 
Which path do you wish to go on? l/r/m: ''')

if path == "l":
    print("POV: You start walking but fall into a spike trap that pierces your everything. You died.")
    exit()
elif path == "m":
    print("POV: You start walking and enter an empty room. The walls start closing on you and you get crushed. You died.")
    exit()
else:
    print("POV: You start walking and you enter a room with five doors...")
print('''

POV: You hear the same voice again... 'Good luck weak soul.''')

doors = input('''MIND: "Man, which door should I choose?"

Choose a door: 1,2,3,4,5: ''')
if doors == "1":
    print("POV: You enter a room full of fire lions. They eat yourinsides. You died.")
    exit()
elif doors == "3":
    print("POV: You enter a room that was filled to the brim with lava. You disintegrate.")
    exit()
elif doors == "4":
    print("POV: You enter a room with demons who look like they are in the middle of a meeting... you die instantly.")
    exit()
elif doors == "5":
    print("POV: You see a lion being raped by a monkey... you faint and die on the spot.")
    exit()
else:
    print("POV: You enter a room with blinding lights but you get used to it.")
input('''

POV: You now see three objects floating on pedistools. 
You wonder how tf they be doing that...
but then you realize you're in hell.

The three objects that in front of you are,
1. Water sword
2. Suspecious paper
3. Huge Fire bomb

Which do you wish to grab? WS, SP, FB: ''')

print('''POV: You now have aquired this item.

You see a door in front of you and you open it... ''')

print('''

The moment you open the door you hear boss music start to play and you see a huge beast in front of you.
You know that is is the end and you're about to go home...''')

print('''

POV: You hear in a deep growling voice, "SO WEAKLING! YOU HAVE MADE IT PAST MY TESTS,
BUT NOW THERE IS NO MORE HOPE FOR YOU! GOODBYE!!!!''')

movement = input('''POV: You see a long arm with a demon scythe in it speeding towards you! 
Move: stay = s, right = r, left = l: ''')
if movement == "s":
    print("You stay still hoping for the best and the scythe chops you in half. You died.")
    exit()
else:
    print("You quickly evade the scythe just in time!")
print("POV: The beast is now breathing fire at you from your left! s, l, r: ")
if movement == "s":
    print("The fire consumes you and you burn and die instantly. ")
    exit()
elif movement == "l":
    print("The fire consumes you and you burn and die instantly.")
    exit()
else:
    print("You move barely dodging the buring fire. You realize that you still have your object! ")
object1 = input("What object did you grab? WS, SP, FB: ")
if object1 == "WS":
    print("You use the water sword but it's no use! The beast is too powerful! You die.")
    exit()
elif object1 == "FB":
    print("Your fire bombs are useless against the firey demon. You die. ")
    exit()
else:
    print('''You use the suspicious paper and it turns into a Water Demon!
    The Water Demon over powers the beast and in the beast's dying breath you hear,
    "Theres... theres no way! There-" the beast gets cut off because the Water demon chops off the head.
    It gets tired of its bickering. 
    
    
    You beat the game and you return home to your family and your new pet!''')
