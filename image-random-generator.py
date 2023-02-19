from PIL import Image
import random
import os
import json

def generate(name):
    # Load the file weights from a JSON file
    with open('file_weights.json') as f:
        file_weights = json.load(f)

    # Get a list of files in the directory
    dir = name
    choices = os.listdir(dir)

    # Calculate the total weight
    total_weight = sum(file_weights[file] for file in choices)

    # Generate a random number between 0 and the total weight
    random_weight = random.uniform(0, total_weight)

    # Iterate through the files and add the weights until we find the
    # file with a weight greater than or equal to the random number
    weight_sum = 0
    for file in choices:
        weight_sum += file_weights[file]
        if weight_sum >= random_weight:
            selected_file = file
            break

    # Open the selected file using PIL and convert it to the RGBA format
    img = (Image.open(os.path.join(dir, selected_file))).convert("RGBA")
    return img

def main(filename):
    bkgr = generate("background")
    head = generate("head")
    body = generate("body")
    legs = generate("legs")

    result = Image.alpha_composite(bkgr, head)
    result = Image.alpha_composite(result, body)
    result = Image.alpha_composite(result, legs)

    name = 'output/complete_' + filename + '.png'
    # Save the resulting image
    result.save(name)

main("1")
main("2")
main("3")
main("4")
main("5")

"""
Example json

{
    "white.png" : 1,
    "red.png" : 1,
    "green.png" : 1,
    "blue.png" : 1,
    "pink.png" : 1,
    "orange.png" : 1,
    "blue_camo.png" : 1,
    "gold_camo.png" : 1,
    "frost.png" : 1,
    "grey_pattern.png" : 1,
    "magenta_pattern.png" : 1,
    "pink_pattern.png" : 1,
    "lime_pattern.png" : 1,
    "funky.png" : 1,
    "peppermint.png" : 1,
    "greenmint.png" : 1,
    "spearmint.png" : 1
}
"""
