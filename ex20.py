from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

# To go to start of file @ 0 byte, can move to any file position with byte count
def rewind(f):
    f.seek(0)

# Comma after print stmt, to prevent extra /n char,
# as there is one already returned from f.readline()
def print_a_line(line_count, f):
    print line_count, f.readline(),
    # or return line_count, f.readline(), 

current_file = open(input_file)

print "Print all file contents:"
print_all(current_file)

print "Let's rewind the file, like a tape"
rewind(current_file)

print "Let's print 3 lines"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
