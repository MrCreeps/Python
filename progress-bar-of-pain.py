import time
import random
from tqdm import tqdm

var1 = random.randint(10, 20)
var2 = random.randint(10, 20)
var3 = random.randint(10, 20)
var4 = random.randint(10, 20)
var5 = random.randint(10, 20)

if var1 + var2 + var3 + var4 + var5 != 100:
    var6 = 100 - (var1 + var2 + var3 + var4 + var5)
else:
    var6 = 0

total = 100
pbar = tqdm(total=total)

for i in range(var1):
    pbar.update()
    time.sleep(random.uniform(0.1, 0.3))
time.sleep(random.uniform(3,5))
for i in range(var2):
    pbar.update()
    time.sleep(random.uniform(0.1, 0.7))
time.sleep(random.uniform(3,5))
for i in range(var3):
    pbar.update()
    time.sleep(1)
time.sleep(random.uniform(3,5))
for i in range(var4):
    pbar.update()
    time.sleep(random.uniform(1, 1.3))
time.sleep(random.uniform(3,5))
for i in range(var5):
    pbar.update()
    time.sleep(random.uniform(0.1, 0.2))
time.sleep(random.uniform(15, 15.1))
for i in range(var6):
    pbar.update()
    time.sleep(random.uniform(1, 2))

pbar.close()
