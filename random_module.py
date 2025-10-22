import  numpy as np

from numpy import random

a=random.randint(99)
print(f"only one {a}")



a=random.randint(99,size=2)
print(f"fixing size {a}")



a=random.choice([2,4,6,8,10,12])
print(a)