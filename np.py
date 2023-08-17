import numpy as np
arr=np.array([[2,3,4],[1,6,5]])
print("sum of array = ",arr.sum())
print("maximum of the array = ",arr.max())
print("minimum of the array = ",arr.min())
print("minium between array = ",arr.min(axis=1))
print("maximum between array = ",arr.max(axis=1))
print("cumulatite sum = ",arr.cumsum(axis=1))
print("average of the array = ",np.average(arr))


