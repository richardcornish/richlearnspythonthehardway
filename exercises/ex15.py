# Exercise 15
# https://learnpythonthehardway.org/book/ex15.html

# import argv from the sys module
from sys import argv

# assign the the name of the file as an argument to argv
script, filename = argv

# open the file and assign the result to txt
txt = open(filename)

# print the name of the file and the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# prompt asking the name of the file again
print "Type the filename again:"
file_again = raw_input("> ")

# open the file
txt_again = open(file_again)

# print the contents of the file
print txt_again.read()
