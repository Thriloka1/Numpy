import numpy as np

n=np.array([1,2,3,4,5])

for x in n:
    print(x)

resarr=np.array_split(n,3)

for x in resarr:
    print(x)


n=np.array([[1,2,3],[4,5,6]])

for x in n:
    print(x)

resarr=np.array_split(n,2)
print(resarr[0])
print(resarr[1])