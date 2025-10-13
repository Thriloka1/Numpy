import numpy as np

n=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(n[1:3])
print(n[:3])
print(n[3:])
print(n[1:10:3])

# slice - 2d array
dim=int(input("enter dime"))
shape=[]
for i in range(dim):
    ele=int(input(f"enter no.of values to {i} dimension"))
    shape.append(ele)
total=np.prod(shape)
ele=[]

for i in range(total):
    ele.append(int(input(f"enter elements for {i}")))

arr=np.array(ele).reshape(shape)
print(arr)
print("===================")
print(arr[:2, 2:5]) #arr[row,columns]