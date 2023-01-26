from calc import Statistics, pm
import numpy as np

X=[77,50,71,72,81,94,96,99,67]
Y=[82,66,78,84,74,85,99,99,68]
data = np.array([X, Y]).T

data = np.loadtxt('GPA.txt', delimiter='\t')
# data = np.loadtxt('copiers.txt', delimiter='\t')

if __name__ == "__main__":
    s = Statistics(data)
    s.print()
    s.getYh(5)
    # print(pm(74.59608355091385, 1.3298310691570479 * 1.6811))
    # print(pm(89.6313315926893, 9.022227643898203 * 2.0167))