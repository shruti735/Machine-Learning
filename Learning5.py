import numpy as np
import numpy.core.records as ncr

a= np.array([0,1,2,3,4,5,6,7,3,3])
print(a)
print(ncr.array([0,1,2,3,4,5]))
print(a.ndim)
print("Shape --",a.shape)
b = a.reshape((2,5))
print("Reshape  ",b)
b[0][4]=77
print("After",b)
print(a*2)
print(a**2)
print([0,1,2,3,4,5,3,4,6,7,3,3]*2)
print(a>4)
c = np.array([1,2,np.NAN,shruti,3,4])
print(np.isnan(c))