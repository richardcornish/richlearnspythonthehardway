# Exercise 19
# http://learnpythonthehardway.org/book/ex19.html

# define a function with two parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print the number of cheeses
    print "You have %d cheeses!" % cheese_count
    # print the number of boxes
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # print your party animal street cred
    print "Man that's enough for a party!"
    # print the necessity for warmth
    print "Get a blanket.\n"

# print description of calling the function
print "We can just give the function numbers directly:"
# call the function with two arguments that are integers
cheese_and_crackers(20, 30)

# print description of calling the function
print "OR, we can use variables from our script:"
# assign integer values to cheese and crackers
amount_of_cheese = 10
amount_of_crackers = 50
# call the function with two arguments that are variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print description of calling the function
print "We can even do math inside too:"
# call the function with two arguments that are addition of integers with plus operator
cheese_and_crackers(10 + 20, 5 + 6)

# print desciption of calling the function
print "And we can combine the two, variables and math:"
# call the function with two arguments that are variables and addition of integers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# My own function
import random

def creeping_on_my_ex(text_messages, calls):
    print "You sent %d text messages and made %d calls. Creep!" % (text_messages, calls)

def random_int():
    return random.random() * 100

for x in xrange(1, 11):
    creeping_on_my_ex(random_int(), random_int())
