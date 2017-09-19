def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_nothing():
    print "I got nothin'"

# Direct inputs for function
print_two("Archana", "Ram")
print_two_again("Archana", "Ram")
print_one("Amazing!!!")
print_nothing()

# Variables as input for functions
first = 100
last = 540
print_two_again(first, last)

# Math inside functions
print_two_again(10 + 5, 20 + 6)

# Math and variables inside functions
print_two_again(first + 10, last + 3)

# Get from user
print "Type first item to be printed:",
a = raw_input()
print "Type second item to be printed:",
b = raw_input()
print_two_again(a,b)
