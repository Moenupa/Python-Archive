# The Tri-City Office Equipment Corporation sells 
# an imported copier on a franchise basis and performs 
# preventive maintenance and repair service on this copier. 
# Data we collected from 45 recent calls to perform routine 
# preventive maintenance service; for each call, X is the 
# number of copiers serviced and Y is the total number of 
# minutes spent by the service person. The data can be 
# found at “copiers.txt”.

import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

data = np.loadtxt('copiers.txt', delimiter='\t')

model = lm.LinearRegression()
model.fit(data[:,0].reshape(-1, 1), data[:,1])

residuals = data[:,1] - model.predict(data[:,0].reshape(-1, 1))

if __name__ == '__main__':
    print(f'y={model.coef_[0]}x+{model.intercept_}')
    print(f'residuals: {sum(residuals)}')

    plt.plot(data[:,0], data[:,1], 'o')
    plt.plot(data[:,0], model.predict(data[:,0].reshape(-1, 1)))
    plt.show()
    