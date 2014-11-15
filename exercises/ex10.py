# Exercise 10
# http://learnpythonthehardway.org/book/ex10.html

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
print u"Character with 16-bit hex value xxxx: \uF8FF"
print u"Character with 32-bit hex value xxxxxxxx: \U0001F4A9"
print "ASCII vertical tab: \v"
print "Character with octal value ooo: \ooo"
print "Character with hex value hh: \x00"

# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,
