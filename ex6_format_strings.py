# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

print "Its fleece was white as %s." % 'snow'
print '.' * 10 # prints it 10 times
print '*' * 10

# Assign CHeeseburger alphabets to an ascending variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# Comma introduces a space and prints both words on same line
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) #returns the string as it is
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# 3rd string above is printed with double quotes, cos it has single
# quotes and to prevent python from getting confused and executing the rest of string as a math logic

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

# To print a paragraph of multiple lines - """ or '''
print '''
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
'''
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "Backslash: \\"
print "Single-quote: \'"
print "Double-quote: \""
print "ASCII bell: \a"
print "ASCII backspace: \b"
print "ASCII formfeed: \f"
print "ASCII linefeed: \n"
print "Character named name in the Unicode database: \N{name}"
print "Carriage return: \r"
print "Horizontal tab: \t"
#print u"Character with 16-bit hex value xxxx: \uF8FF"
#print u"Character with 32-bit hex value xxxxxxxx: \U0001F4A9"
print "ASCII vertical tab: \v"
print "Character with octal value ooo: \ooo"
print "Character with hex value hh: \x00"

# /r - resets the cursor position to beginning of the line of text, can also overprint
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
