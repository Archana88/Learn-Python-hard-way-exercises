# Linear regression in python

from numpy import loadtxt, zeros, ones, array, linspace, logspace, mean, std, arange
import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel
from random import uniform
from random import randint

def features(N = 100):
    # To generate N number of features x, each of length 2 (d=2)
    d = []
    for i in range(N):
        x = uniform(-1,1)
        y = uniform(-1,1)
        d.append([x,y])
    return d # d = [[x1,x2],[x1,x2],...]

def startline():
    # To compute m and c for y = mx+c
    x1 = uniform(-1,1)
    x2 = uniform(-1,1)
    y1 = uniform(-1,1)
    y2 = uniform(-1,1)

    m = abs(x1-x2)/abs(y1-y2)
    c = y1 - m*x1
    return [m,c] # mx+c

def label(point,f):
    # Labeling the data set
    x1 = point[0]
    y1 = point[1]

    y = f(x1)
    compare = y1
    return sign(y,compare)

def sign(x,compare = 0):
    # To return +1/-1
    if x > compare:
        return +1
    else:
        return -1

def generate_misclassified_set(train_set,w):
    # To generate a list of indices of misclassified data sets
    result = tuple()

    for i in range(len(train_set)):
        point = train_set[i][0]
        s = h(w,point)
        yn = train_set[i][1]
        if s != yn:
            result = result + (i,) # adds the index 'i' to the result tuple, result consists of indexes of all mis classified data sets
    return result

def compute_cost(X, y, theta):

    # Calculate cost function
    m = y.size

    prediction = X.dot(theta)

    error = (prediction - y)

    J = (1.0 / (2 * m)) * error.T.dot(error)

    return J


def gradient_descent(X, y, theta, alpha, num_iters):
    # To perform gradient descent
    m = y.size
    J_history = zeros(shape=(num_iters, 1))

    for i in range(num_iters):

        prediction = X.dot(theta)

        theta_size = theta.size

        for j in range(theta_size):

            temp = X[:, j]
            temp.shape = (m, 1)

            errors_x1 = (prediction - y) * temp

            theta[j][0] = theta[j][0] - alpha * (1.0 / m) * errors_x1.sum()

        J_history[i, 0] = compute_cost(X, y, theta)

    return theta, J_history

N = 20
iteration = 0
# geberate random contelation of points in interval [-1,1]
d = features(N)
# generate random target function
l = startline()
# to define a function in one line. this is a line equation
f = lambda x: l[0]*x + l[1]

# generate training set
train_set = []
theta = zeros(shape=(3, 1))
for i in range(len(d)):
    x = d[i]
    y = label(x,f)
    train_set.append( [ [ 1 ,x[0],x[1] ] , y ] )

X = train_set[m][0]
y = train_set[m][1]

gradient_descent(X, y, theta, 0.0001, 100)
