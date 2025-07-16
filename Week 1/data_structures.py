# lists
numbers  = [1,8,3,5,7]
numbers.append(11)
numbers.remove(8) # for first occurrence
numbers.pop() # for index
numbers.extend([5,7])
numbers.sort()
numbers.insert(1, 'a')
print(numbers)
print(numbers[1:4]) # last is exclusive

# tuples (they are faster and use less memory)
tuplee = (1,) #  for a single-element tuple, comma is a must
tuplee = ((1,2),(3,4),(5,4))
print(tuplee[1])

# shallow vs deep copy
list1 = [1,2,3]
list2 = [5,3,1]

list1 = list2 # its just pointing list1 to same memory location as list2

import copy

# shallow copy (one level)
shallow = list1[:]           # slicing
shallow = list(list1)        # constructor
shallow = copy.copy(list1)   # copy module

#  deep copy
deep = copy.deepcopy(list2)

# dictionary
student = {"name": "ema","age":21, "grades": {
    "probability": 20,
    "algebra": 20
}}
student["grades"]["algebra"] = 40
print(*student.items())

# set
s = {1, 2, 3, 2}  # duplicates are removed → {1, 2, 3}
a = {1, 2, 3}
b = {7, 4, 5}

print(a | b)     # Union → {1, 2, 3, 4, 5}
print(a & b)     # Intersection → {3}
print(a - b)     # Difference → {1, 2}
print(a ^ b)     # Symmetric difference → {1, 2, 4, 5}

print(a.issubset(b))     # False
print(a.isdisjoint(b))   # True
