import numpy as np

a=np.array([10,2,4,6,8])
b=np.array([15,3,6,9,12])

a=np.sort(a)
b=np.sort(b)
print(np.intersect1d(a,b))