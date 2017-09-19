name = 'Archana'
age = 35
height = 65 #inches
height_in_cm = height * 2.54
weight = 162 # lbs
weight_in_kg = 0.453 * weight
eyes = 'Black'
hair = 'Black'

print "Let's talk about %s." % name
print "She is %d inches tall" % height
print "She is %d cm tall" % height_in_cm
print "She is %d pounds heavy" % weight
print "She is %d kg heavy" % weight_in_kg
print "She has got %s eyes and %s hair." % (eyes, hair)

print "If I add %d, %d and %d, I get %d." %(age, height, weight, age + height + weight)
print "hair is %r" % hair
