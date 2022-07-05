# 1 Countdown
# build function that returns list of numbers from number argument down to 0
def countdown_from_value(value):
    countdown_list = []
    for i in range(value,-1,-1):
        countdown_list.append(i)
    return countdown_list

# 2 Print and Return
# function that prints first number and returns second
def print_and_return(number_list):
    print(number_list[0])
    return(number_list[1])

# 3 First Plus Length
# function that returns sum of first value plus length of list
def first_plus_length(number_list):
    return(number_list[0] + len(number_list))

# 4 Values Greater than Second
# function that:
# a) accepts a list
# b) creates a new list with only the values greater than value of 2nd element
# c) prints length of new list
# d) returns new list if length >= 2, else return false
def values_greater_than_second(number_list):
    if(len(number_list) < 2):
        return False
    new_list = []
    for number in number_list:
        print(number)
        if number > number_list[1]:
            new_list.append(number)
    print(len(new_list))
    if(len(new_list) >= 2):
        return new_list
    else:
        return False

# 5 This Length, That Value
# write a function that accepts to integers and returns a list of length 1st int of values equal to 2nd int
def length_and_value(length_fx, value_fx):
    new_list = []
    for i in range(length_fx):
        new_list.append(value_fx)
    return new_list
