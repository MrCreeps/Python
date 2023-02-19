import time
import random
from tqdm import tqdm

# Title message
input("Welcome to MrCreeps' CPU Benchmark. This is a Python program that sorts through arrays, times it, then calculates a score based off the speed. Press any 'Enter' to start.")

# Sets time 1 before starting
t1 = time.perf_counter()

# Initiates the benchmark
sum = 0
for i in tqdm(range(100000)):
    array = [random.randint(0, 100) for _ in range(3000)]
    array.sort()
    i += 1

# Sets time 2 after ending
t2 = time.perf_counter()

# Finds the difference of the two times
elapsed_time = t2 - t1

# Calculates score
score = 1 / elapsed_time
score = round(score * 1000000)

# Prints score and final message
print(f"Score: {score}")
input("Press 'Enter' to exit")
