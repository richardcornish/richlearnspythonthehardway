# Exercise 7
# http://learnpythonthehardway.org/book/ex7.html

# Print first line of "Mary Had a Little Lamb" nursery rhyme
print "Mary had a little lamb."

# Print second line of nursery rhyme with string formatting of "snow"
print "Its fleece was white as %s." % 'snow'

# Print third line of nursery rhyme
print "And everywhere that Mary went."

# Print the period character 10 times
print "." * 10 # what'd that do?

# Assign each letter of "CheeseBurger" to a respective ascending variable
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

# Prints the concatenation of variables end1-end6, a space via the comma, and
# continues to print the concatenation of variables end7-end12
# Removing the comma forces a line break between both lines

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
