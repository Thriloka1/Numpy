import numpy as np

a=np.array([2,4,6,8,10])
b=np.array([3,6,9,12,15])


res=np.sum([a,b],axis=0)
print(res)
res=np.sum([a,b],axis=1)
print(res)


res=np.subtract(a,b)
print(res)




res=np.multiply(a,b)
print(res)


res=np.divide(a,b)
print(res)


res=np.divmod(a,b)
print(res)