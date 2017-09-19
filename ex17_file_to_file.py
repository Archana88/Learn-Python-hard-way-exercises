from sys import argv
from os.path import exists # return true if file exists

script, from_file, to_file = argv

print "Copying from file %s to %s" % (from_file, to_file)
print "The length of the input file is: %d bytes" % len(from_file)


open(to_file,'w').write(open(from_file).read())

print "Copied file verified below"

print open(to_file).read()

# to_file.close()
