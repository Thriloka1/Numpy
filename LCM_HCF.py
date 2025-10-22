import numpy as np

a=np.arange(10).reshape(2,-1)
print(f"\n{a}")
res=np.lcm.reduce(a)
print(f"\n{res}")
res=np.gcd.reduce(a)
print(f"\n{res}")