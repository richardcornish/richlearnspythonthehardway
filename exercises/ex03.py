# Exercise 3
# http://learnpythonthehardway.org/book/ex3.html

# Announce the counting of the chickens
print "I will now count my chickens:"

# Prints Hens and Roosters counts, according to "operator precedence"

# 25 + 30 / 6
# 25 + 5
# 30
print "Hens", 25 + 30 / 6

# 100 - 75 % 4
# 100 - 3
# 97
print "Roosters", 100 - 25 * 3 % 4

# Announce the counting of the eggs
print "Now I will count the eggs:"

# Compute the egg expression
# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - 0 + 6
# 5 + -4 + 0 + 6
# 1 + 6
# 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# Ask a question
print "Is it true that 3 + 2 < 5 - 7?"

# Print AND compute the expression AND compare them
# 5 < -2
print 3 + 2 < 5 - 7 # False

# Print the question AND compute the expression
print "What is 3 + 2?", 3 + 2 # 5
print "What is 5 - 7?", 5 - 7 # -2

# Print a grand revelation
print "Oh, that's why it's False."

# Print your desire to continue
print "How about some more."

# Print the question AND compute the expression, now with more truthiness
print "Is it greater?", 5 > -2 # True
print "Is it greater or equal?", 5 >= 2 # True
print "Is it less or equal?", 5 <= -2 # False
