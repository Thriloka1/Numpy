# axes=0 => rows
# axes=1 => columns

import numpy as np

n=np.array([[1,2,3],[14,5,6],[7,8,9]])
for x in n:
    print(x)

print(f"{n.min()} and {n.min(axis=0)} and {n.min(axis=1)}")