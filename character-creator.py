import random
import json
import os

def create_character():
    name = input("Enter your character's name: ")

    logged_in_user = os.getlogin()
    # Get the path to the AppData directory
    app_data_dir = f"C:\\Users\\{logged_in_user}\\AppData\\Roaming\\"

    # Create the path to the playerobjects folder in the Roaming directory
    playerobjects_dir = os.path.join(app_data_dir, "playerobjects")

    # Create the playerobjects folder if it doesn't exist
    if not os.path.exists(playerobjects_dir):
        os.makedirs(playerobjects_dir)

    # Check if a file with the character's name exists
    playerobject_path = os.path.join(playerobjects_dir, f"{name}.playerobject")
    try:
        with open(playerobject_path, "r") as f:
            # Load the character's attributes from the file
            character_data = json.load(f)
            max_health = character_data['max_health']
            current_health = character_data['current_health']
            damage = character_data['damage']
            print(f"Character values for {name} have been loaded.")
    except FileNotFoundError:
        # If the file doesn't exist, generate new values for the character
        max_health = random.randint(80, 121)
        current_health = max_health
        damage = random.randint(5, 16)

    # Save the character's values to a file in JSON format
    character_data = {
        'max_health': max_health,
        'current_health': current_health,
        'damage': damage
    }
    with open(playerobject_path, "w") as f:
        json.dump(character_data, f)
        print(f"Your character, {name}, has been created with a max health of {max_health}, a current health of {current_health}, and a damage of {damage}.")

create_character()
