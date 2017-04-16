# Exercise 11
# https://learnpythonthehardway.org/book/ex11.html

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "Do you like bed?",
bed = raw_input()
print "Do you wish you were in bed?",
wish = raw_input()
print "Good night. Sleep...",
tight = raw_input()

print "Do you like bed? %r." % bed
print "Do you wish you were in bed? %r." % wish
print "Good night. Sleep...%r!" % tight
