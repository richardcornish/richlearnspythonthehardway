# Exercise 13
# https://learnpythonthehardway.org/book/ex13.html

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

opinion = raw_input("What do you think of this script? ")
print "You think %s is %s!" % (script, opinion)
