import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

class Statistics():
    def __init__(self, data) -> None:
        self.data = data
        
        self.n = len(data)
        self.X_bar = np.mean(data[:,0])
        self.y_bar = np.mean(data[:,1])

        self.SXX = np.sum((data[:,0] - self.X_bar)**2)
        self.SYY = np.sum((data[:,1] - self.y_bar)**2)
        self.SXY = np.sum((data[:,0] - self.X_bar)*(data[:,1] - self.y_bar))

        self.model = lm.LinearRegression()
        self.model.fit(data[:,0].reshape(-1, 1), data[:,1])

        # predicted y (y hat) - true y
        self.residuals = self.model.predict(data[:,0].reshape(-1, 1)) - data[:,1]
        
        self.SSE = np.sum(self.residuals**2)
        self.SST = self.SYY
        self.SSR = self.SST - self.SSE
        self.MSR = self.SSR / 1
        self.MSE = self.SSE / (len(data) - 2)
        
        self.s_beta1 = np.sqrt(self.MSE / self.SXX)
        
    def plot(self):
        plt.plot(self.data[:,0], self.data[:,1], 'o')
        plt.plot(self.data[:,0], self.model.predict(self.data[:,0].reshape(-1, 1)))
        plt.show()
        
    def getYh(self, x):
        x_h = x
        y_h = self.model.predict(np.array([x]).reshape(-1, 1))[0]
        s_yh = np.sqrt(self.MSE * (1/self.n + ((x_h-self.X_bar)**2)/self.SXX))
        s_yhnew = np.sqrt(self.MSE * (1 + 1/self.n + ((x_h-self.X_bar)**2)/self.SXX))
        
        print(f'''
            Xh,Yh: ({x_h},{y_h}), s_yh: {s_yh}, s_yhnew: {s_yhnew}
              ''')

    def print(self):
        print(f'''
            X_bar: {self.X_bar}, y_bar: {self.y_bar}, 
            SXX: {self.SXX}, SYY: {self.SYY}, SXY: {self.SXY}, 
            n: {len(self.data)}
            
            y={self.model.intercept_}+{self.model.coef_[0]}X
            
            Residuals: {np.sum(self.residuals)}
            MSE: {self.MSE}, sigma: {np.sqrt(self.MSE)},
            SST: {self.SST}, SSR: {self.SSR}, SSE: {self.SSE}
            r^2: {self.SSR/self.SST}
            
            s_beta1: {self.s_beta1}
            
            t-test: {self.model.coef_[0] / self.s_beta1}
            f-test: {self.MSR / self.MSE}
          ''')

def pm(e, s):
    '''
    return a interval of e plus/minus s
    '''
    return (e-s, e+s)