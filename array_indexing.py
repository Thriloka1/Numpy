import numpy as np

arr = np.array([[[1, 2], [3, 4]],[[5, 6], [7, 8]]])

dim1, dim2, dim3 = arr.shape
# traditional way of accessing elements
for i in range(dim1):
    for j in range(dim2):
        for k in range(dim3):
            print(f"Element at ({i},{j},{k}) = {arr[i, j, k]}")



# blocks, rows, columns
arr = np.arange(24).reshape(2, 3, 4)  # 3D array

# advanced method with iterator
for x in np.nditer(arr):
    print(x, end=" ")


def access_elements(arr, indices=()):
    if arr.ndim == 0:
        print(f"Element at {indices} = {arr.item()}")
    elif arr.ndim == 1: 
        for i in range(arr.shape[0]):
            print(f"Element at {indices + (i,)} = {arr[i]}")
    else: 
        for i in range(arr.shape[0]):
            access_elements(arr[i], indices + (i,))

# Example with a 3D array
access_elements(arr)



# advanced method with index
for idx in np.ndindex(arr.shape):
    print(f"Element at {idx} = {arr[idx]}")


user_dimensions=int(input("enter dimensions "))
shape=[]
for i in range(user_dimensions):
    ele=int(input(f"enter no.of values for {i+1} dimension"))
    shape.append(ele)

total=np.prod(shape)
elements=[]
for i in range(total):
    data=int(input(f" enter {i+1} element: "))
    elements.append(data)

arr=np.array(elements).reshape(shape)

print(arr)