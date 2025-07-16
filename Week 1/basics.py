import math
# or
from math import sqrt

# f-strings
print(f"square root of 4 is:  {math.sqrt(4)}")
print(f"square root of 4 is:  {sqrt(4)}")

# print both expression and its results - helpful in debugging
abc = "value"
print(f"{abc=}")

# loops
count = 0
while(True):
    print(count)
    count += 1
    if(count == 3):
        continue
    if count>5:
        break

def greet(name="stranger"):
    print(f"Hi {name}!")
    