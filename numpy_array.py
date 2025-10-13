import numpy as np

# 0 dimension
data=np.array((1))
print(data.ndim)

# 1 dimension
data=np.array([1,2,3])
print(data.ndim)



data=np.array([[1,2],[3,4]])
print(data.ndim)

# multi dimensional array

data=np.zeros([3,3,3])
print(data)

# integer array
n=np.array([1,2,3])
print(n.dtype)

# U1 - U= unicode; 1= max number characters input 
n=np.array(['1','2','3'])
print(n.dtype)

# setting datatype of array
n=np.array([1,2,3],dtype='S1')
print(f"\n {n} - {n.dtype}")

# converting from one data type to another data type
n=n.astype('i')
print(n.dtype)
