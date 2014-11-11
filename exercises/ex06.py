# Exercise 6
# http://learnpythonthehardway.org/book/ex6.html

# Assign values to cryptic variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # 1) and 2) a string inside a string

# Print x and y
print x
print y

# Print the literal representation of x and the string of y
print "I said: %r." % x
print "I also said: '%s'." % y # 3) a string inside a string

# Determine how funny this joke is and allow evaluation to have a literal representation value appended to it
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the evaluation and insert the hilarious status into it
print joke_evaluation % hilarious

# Assign strings to variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# Print the concatenation of w and e
print w + e
