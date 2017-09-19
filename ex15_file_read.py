from sys import argv

script, filename = argv

txt = open(filename) # returns a file object-its like a DVD player- a common object used to point to a file.

print "Here's your file %r:" % filename
print txt.read() # can perform operations on the file with a '.'

txt.close() # close file after opening

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

print txt_again.close() # prints none
