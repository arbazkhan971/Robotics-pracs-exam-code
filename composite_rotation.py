import math
import numpy as np
tx=int(input("Enter the x axis: "))
ty=int(input("Enter the y axis: "))
tz=int(input("Enter the z axis: "))
r=int(input("Enter the rotation of angle: "))
axis=int(input("Enter the axis if rotation: "))

a=r*math.pi/180

mat_trans=np.array([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])
T=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

s=round(math.sin(a),2)

c=round(math.cos(a),2)

r1=np.array([[1,0,0,0],
             [0,c,-s,0],
             [0,s,c,0],
             [0,0,0,1]])


r2=np.array([[c,0,s,0],
             [0,1,0,0],
             [-s,0,c,0],
             [0,0,0,1]])


r3=np.array([[c,-s,0,0],
             [s,c,0,0],
             [0,0,1,0],
             [0,0,0,1]])
           

if axis==1:
    mat_rot=r1
elif axis==2:
    mat_rot=r2
elif axis==3:
    mat_rot=r3
op=int(input("Enter: "))
if op==1:
    T=mat_trans.dot(mat_rot)
else:
    T=mat_trans.dot(mat_trans)
print(T)

x=int(input("Enter the x axis: "))
y=int(input("Enter the y axis: "))
z=int(input("Enter the z axis: "))
P=np.array([x,y,z,1])
result=T.dot(P)
print(result)


