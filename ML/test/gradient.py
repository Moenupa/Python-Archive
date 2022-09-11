import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = (x-5) ** 2 + 2
plt.scatter(x[0], y[0], color='r', marker='x')
print(x[0], y[0])
plt.plot(x,y,color='g')

plt.xlabel('theta', fontsize=12)
plt.xlabel('loss function', fontsize=12)
plt.show()

# 损失函数
def J(theta):
    return (theta-5) ** 2 + 2

# gradient
def dJ(theta):
    return 2 * (theta-5)

theta = x[5]
theta_record = [theta]

eta = .1

epsilon = 1e-6

while True:
    gradient = dJ(theta)
    last_theta = theta
    theta = theta - eta * gradient
    theta_record.append(theta)
    if (abs(J(theta) - J(last_theta)) < epsilon):
        break

plt.plot(x,J(x),color="g")
plt.plot(np.array(theta_record), J(np.array(theta_record)), "-.", color='r',marker='o')

plt.show()
print(len(theta_record))
