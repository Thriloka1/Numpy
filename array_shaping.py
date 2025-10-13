import numpy as np
# shapiing to 2d
arr = np.arange(12).reshape(2, 6)

# reshaping from 2d to 1d
arr=arr.reshape(-1)
print(arr)