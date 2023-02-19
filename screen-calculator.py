import math

def find_length_and_width(hypotenuse, length_width_ratio):
  # Calculate the length of the triangle
  length = hypotenuse / math.sqrt(1 + (1 / (length_width_ratio ** 2)))
  # Calculate the width of the triangle
  width = length / length_width_ratio
  return (length, width)

# All the Variables!!!
hypotenuse = float(input("Diagonal Length: "))
width_ratio = float(input("Width Ratio: "))
length_ratio = float(input("Length Ratio: "))
length_width_ratio = width_ratio/length_ratio
length, width = find_length_and_width(hypotenuse, length_width_ratio)
area = length * width
hres = float(input("Horizontal Resolution: "))
vres = hres / length_width_ratio
tpx = hres * vres
ppi = (tpx / area)**0.5

# All the Prints!!!
print (f"\nVertical Resolution: {vres}")
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area: {area}")
print(f"Total Pixel Resolution: {tpx}")
print(f"Pixel Density (Pixels per Inch): {ppi}")
