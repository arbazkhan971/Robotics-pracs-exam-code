import matplotlib.pyplot as plt
import numpy as np



I = np.array([[0,0,5,0],
              [0,0,4,0],
              [0,0,3,0],
              [0,0,4,0],
              [0,0,0,0]])
A = I

A = np.append(A,np.zeros((A.shape[0],1)),axis=1)
A = np.append(A,np.zeros((1,A.shape[0])),axis=0)
plt.imshow(A,cmap="gray")
plt.show()
d1,d2 = 0,0
def calc_d1(k,j):
    return((A[k+1,j]-A[k,j]+A[k+1,j+1]-A[k,j+1])/2)
def calc_d2(k,j):
    return((A[k,j+1]-A[k,j]+A[k+1,j+1]-A[k+1,j])/2)
f = np.zeros((A.shape[0]-1,A.shape[1]-1))
for k in range(f.shape[0]):
    for j in range(f.shape[1]):
        d1 = calc_d1(k,j)
        d2 = calc_d2(k,j)
        f[k,j] = (d1**2 + d2**2)**0.5
f = (f>2)*1
plt.imshow(f,cmap="gray")
plt.show()
print(f)