import numpy as np

arr1=np.array([1,2,3,4,5])

arr2=np.array([6,7,8,9,10])
# using concatenate()
print(np.concatenate([arr1,arr2]))

# using stack methods

print(f"\n{np.stack((arr1,arr2))}")
print(f"\n{np.vstack((arr1,arr2))}")
print(f"\n{np.hstack((arr1,arr2))}")
print(f"\n{np.dstack((arr1,arr2))}") #3rd dimension
print(f"\n{np.column_stack((arr1,arr2))}")
