# Calculates grade based on the amount of problems and the amount of problems missed.

try:
  problems = int(input("How many problems are on the assignment? "))
  missed = int(input("How many problems did you miss? "))
except ValueError:
  print("Not a number...")
  exit()
grade = 100 - ((100 / problems) * missed)
print(f"You got a {round(grade, 1)}!")
