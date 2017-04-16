# Exercise 17
# https://learnpythonthehardway.org/book/ex17.html

from sys import argv; script, from_file, to_file = argv; open(to_file, 'w').write(open(from_file).read())
