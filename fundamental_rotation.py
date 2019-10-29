import numpy as np 
import math


x = int(input("Enter the X axis:"))
y = int(input("Enter the y axis:"))
z = int(input("Enter the X axis:"))
axis = int(input("enter axis of rotations"))
r = int(input("Enter angle of rotations"))
a = r * math.pi/180
p = np.array([[x],[y],[z]])
r1 = np.array([[1,0,0],[0,math.cos(a),-math.sin(a)],[0,math.sin(a),math.cos(a)]])
r2 = np.array([[math.cos(a),0,math.sin(a)],[0,1,0],[-math.sin(a),0,math.cos(a)]])
r3 = np.array([[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])

if axis == 1:
    c = r1.dot(p)
if axis == 2:
    c = r2.dot(p)
if axis == 3:
    c = r3.dot(p)

print(c)