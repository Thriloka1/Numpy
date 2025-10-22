import numpy as np

a=np.array([2,4,6,8,10])
b=np.array([3,6,9,12,15])


print(f"{np.setdiff1d(a,b)} and {np.setdiff1d(b,a)}")