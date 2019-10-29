import numpy as np
I = np.array([[0,0,5,0],
              [0,0,4,0],
              [0,0,3,0],
              [0,0,4,0],
              [0,0,0,0]])

def moment(I,k,j):
    m = 0
    for i in range(len(I)):
        for l in range(len(I[i])):
            if I[i,l] == 1:
                m+=(i**k)*(l**j)
    return m

xc,yc = moment(I,1,0)/moment(I,0,0),moment(I,0,1)/moment(I,0,0)

def first_order_moment(I,xc,yc,k,j):
    mu = 0
    for i in range(len(I)):
        for l in range(len(I[i])):
            if I[i,l] == 1:
                mu+=((i-xc)**k)*((l-yc)**j)
    return mu
    
principal_angle = 0.5*math.atan2(2*first_order_moment(I,xc,yc,1,1),
                                 first_order_moment(I,xc,yc,2,0)-first_order_moment(I,xc,yc,0,2))

print(xc,yc,principal_angle*180/math.pi)