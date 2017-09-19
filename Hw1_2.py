'''
PLA implementation in Python
'''
from random import uniform
from random import randint
import matplotlib.pyplot as plt
from pylab import plot, show, xlabel, ylabel

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

def h(w,x):
    # To generate the hypothesis function, h(x) = w0*x0+w1*x1+....
    result = 0
    for i in range(len(x)):
        result = result + w[i]*x[i]
    return sign(result)

def PLA(Number_points = 100):
    # To return:
    # train_set: [[vector_x], y] for N samples
    # w: vector of optimized weights
    # iteration: Number of iterations required to converge
    # f: target function

    N = Number_points
    iteration = 0
    # geberate random contelation of points in interval [-1,1]
    d = features(N)
    # generate random target function
    l = startline()
    # to define a function in one line. this is a line equation
    f = lambda x: l[0]*x + l[1]
    # weight vector: [w0 , w1, w2]
    w = [0,0,0]
    # generate training set
    train_set = []

    for i in range(len(d)):
        x = d[i]
        y = label(x,f)
        train_set.append( [ [ 1 ,x[0],x[1] ] , y ] )

    # iterate the Perceptron Algorithm
    iterate = True
    count = 0
    while iterate:
        iteration = iteration + 1
        # choose a misclasified point from misclassified set
        misclassified_set = generate_misclassified_set(train_set,w)

        # if all points are classified, break iteration
        if len(misclassified_set) == 0:break

        index = randint(0,len(misclassified_set)-1)
        m = misclassified_set[index]
        point = train_set[m][0]
        yn = train_set[m][1]
        s = h(w,point)

        # update weights for misclassified points
        if s != yn:
            xn = point
            w[0] = w[0] + yn*xn[0]
            w[1] = w[1] + yn*xn[1]
            w[2] = w[2] + yn*xn[2]
    return train_set,w,iteration,f

def evaluate_diff_f_g(f,w):
    # Calculate the number of differences between f and g
    count = 0
    maximum = 100
    diff = 0
    while count < maximum:
        count = count + 1

        x = uniform(-1,1)
        y = uniform(-1,1)
        vector = [1,x,y]

        sign_f = sign(f(x),y)
        sign_g = h(w,vector)
        if sign_f != sign_g: diff = diff + 1

    return diff/(count*1.0)

def run_PLA(Number_samples,Number_points):

    samples = [] # vector to store 1 clasified and 0 misclassified
    iterations = [] # vector of number of iterations required for each PLA
    mis_classified = False
    diff = [] # vector of average of difference between f and g

    for i in range(Number_samples):
        # Run the PLA in sample
        train_set,w,iteration,f = PLA(Number_points)
        iterations.append(iteration)

        # check if the points are classified or not
        for i in range(len(train_set)):
            point = train_set[i][0]
            s = h(w,point)
            yn = train_set[i][1]
            if yn != s:
                samples.append(0)
                mis_classified = True
                break

        # calculate difference between f and g
        diff.append(evaluate_diff_f_g(f,w))

        if not mis_classified: samples.append(1)

        mis_classified = False

    # Plot the graph: Number of samples vs Difference between f and g
    # plt.plot([1:Number_samples:2],diff, 'b')
    # plt.axis(1,max(diff),1, Number_samples)
    # plt.xlabel('Difference between f and g')
    # plt.ylabel('Number of samples')
    # plt.show()

    print 'Number of misclassified samples: %s' % samples.count(0)
    print 'Number of classified samples: %s' % samples.count(1)
    print 'Average of the number of iterations: %s' % (str(sum(iterations)/len(iterations)*1.0))
    print 'Average of the difference between function f and g: %s' % (sum(diff)/(len(diff)*1.0))

run_PLA(100,20)
