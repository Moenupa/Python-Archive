import numpy as np


na = 10
nb = 10
Ya = 103.02
Yb = 122.17
Xa = 86
Xb = 93

Y_bar = (Ya + Yb) / (na + nb)

XYa = 905.57
Y2a = 1083.6532
XYb = 1168.67
Y2b = 1528.4109

xtx = np.matrix([
    [20 , 179 , 10 , 86],
    [179, 1661, 86 , 764],
    [10 ,  86 ,  10, 86],
    [86 , 764 ,86 ,764],
])

xtx_inverse = np.matrix([
    [218868 , -22692,-218868, 22692 ],
    [-22692 , 2440  , 22692 , -2440 ],
    [-218868, 22692 , 464112, -50298],
    [22692  , -2440 , -50298, 5650  ]
])

xty = np.array(
    [225.19, 2074.24, 103.02, 905.57]
)

beta = xtx_inverse.dot(xty)/78324

if __name__ == '__main__':
    # to verify the inverse is correct
    print(xtx_inverse.dot(xtx)/78324)
    
    # output beta estimates
    print(beta)
    print(beta.dot(xty.T))
    print(f'n*Ybar^2 is {(na+nb)*(Y_bar)**2}')