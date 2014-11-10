# Exercise 4
# http://learnpythonthehardway.org/book/ex4.html

# Number of total cars
cars = 100

# Number of spaces in each car
space_in_a_car = 4

# Number of total drivers
drivers = 30

# Number of total passengers
passengers = 90

# Cars left over without drivers
cars_not_driven = cars - drivers

# Each driver represents a car driven
cars_driven = drivers

# All the cars times the space in each car equal the total capacity
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers is all passengers divided by total cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
