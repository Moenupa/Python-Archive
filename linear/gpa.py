# Fit a simple linear regression using ACT score as the explanatory variable, and GPA as the response variable by computing X ̄, Y ̄ and then SXX, SXY and SY Y .

import sklearn.linear_model as lm
import numpy as np

# Load the data
data = np.loadtxt('GPA.txt', delimiter='\t')

# Compute the mean of the ACT scores and the mean of the GPA
# remember to exclude the headers
X_bar = np.mean(data[:,0])
y_bar = np.mean(data[:,1])

SXX = np.sum((data[:,0] - X_bar)**2)
SYY = np.sum((data[:,1] - y_bar)**2)

SXY = np.sum((data[:,0] - X_bar)*(data[:,1] - y_bar))

model = lm.LinearRegression()
model.fit(data[:,0].reshape(-1, 1), data[:,1])

if __name__ == '__main__':
    print(f'{X_bar}, {y_bar}, {SXX}, {SYY}, {SXY}')
    print(f'y={model.coef_[0]}x+{model.intercept_}')
    
