# Exercise 20
# http://learnpythonthehardway.org/book/ex20.html

# import the argv function from the sys module
from sys import argv

# set up script for one parameter
script, input_file = argv

# define function to print contents of file object f
def print_all(f):
    print f.read()

# define function to move cursor to first position of file object f
def rewind(f):
    f.seek(0)

# define function to print the contents of a specific line of file object f, and number of its line
def print_a_line(line_count, f):
    print line_count, f.readline()

# open the passed file and assign it to a variable
current_file = open(input_file)

# print your intent to print
print "First let's print the whole file:\n"

# send file to the print_all function
print_all(current_file)

# print your intent to rewind
print "Now let's rewind, kind of like a tape."

# send the file to the rewind function
rewind(current_file)

# print your intent to print more
print "Let's print three lines:"

# index current line
current_line = 1
# send current line and file to the print_a_line function
# current line = 1
print_a_line(current_line, current_file)

# increment current line by 1
current_line += 1
# send current line and file to the print_a_line function
# current line = 2
print_a_line(current_line, current_file)

# increment current line by 1
current_line += 1
# send current line and file to the print_a_line function
# current line = 1
print_a_line(current_line, current_file)
