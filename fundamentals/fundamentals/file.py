num1 = 42 # VD (variable declaration), PD (primitive datatype) - initialize number
num2 = 2.3 # VD, PD - initialize number
boolean = True # VD, PD - initialize boolean
string = 'Hello World' # VD, PD - initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # CD - initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # CD - initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # CD - initialize tuple
print(type(fruit)) # LS (log statement), type check
print(pizza_toppings[1]) # LS, CD (composite datatype) - access list value
pizza_toppings.append('Mushrooms') # CD - add list value
print(person['name']) # LS, CD - access dictionary value
person['name'] = 'George' # CD - change dictionary value
person['eye_color'] = 'blue' # CD - add dictionary value
print(fruit[2]) # LS, CD - access tuple value

if num1 > 45: # conditional if,
    print("It's greater") # LS
else: # conditional else
    print("It's lower") # LS

if len(string) < 5: # length check, conditional if
    print("It's a short word!") # LS
elif len(string) > 15:  # length check, conditional else if
    print("It's a long word!") # LS
else: # conditional else
    print("Just right!") # LS

for x in range(5): # for loop - loop for 5 times [0,1,2,3,4] (start: 0, stop: 5, increment: 1)
    print(x) # LS
for x in range(2,5): # for loop - loop for 3 times [2,3,4] (start: 2, stop: 5, increment: 1)
    print(x) # LS
for x in range(2,10,3): # for loop - loop for 3 times [2,5,8] (start: 2, stop: 10, increment: 3) 
    print(x) # LS
x = 0 #VD, PD - initialize number
while(x < 5): # while loop start
    print(x) # LS
    x += 1 # while loop - increment

pizza_toppings.pop() # CD, access list value/delete value 
pizza_toppings.pop(1) # CD, access list value/delete value

print(person) # LS
person.pop('eye_color') # CD, access dictionary value/delete value
print(person) # LS

for topping in pizza_toppings: # for loop - loop for len(pizza_toppings) many times
    if topping == 'Pepperoni': # conditional if
        continue # continue for loop
    print('After 1st if statement') # LS
    if topping == 'Olives': # conditional if
        break # break for loop

def print_hello_ten_times(): # define function with no parameters
    for num in range(10): # for loop - loop for 10 times
        print('Hello') # LS

print_hello_ten_times() # call function

def print_hello_x_times(x): # define function with parameter x
    for num in range(x): # for loop - loop for x times
        print('Hello') # LS

print_hello_x_times(4) # call function with argument 4 passed to parameter x

def print_hello_x_or_ten_times(x = 10): # define function with parameter x given default argument set to 10
    for num in range(x): # for loop - loop for x times
        print('Hello') # LS

print_hello_x_or_ten_times() # call function with default argument 10 as parameter x
print_hello_x_or_ten_times(4) # call function with argument 4 passed to parameter x


""" # comment multiline
Bonus section
"""

# print(num3) # comment single line, NameError: name 'num3' is not defined
# num3 = 72 # comment single line
# fruit[0] = 'cranberry' # comment single line, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # comment single line, KeyError: 'favorite_team'
# print(pizza_toppings[7]) # comment single line, IndexError: list index out of range
#   print(boolean) # comment single line, IndentationError: unexpected indent
# fruit.append('raspberry') # comment single line, AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # comment single line, AttributeError: 'tuple' object has no attribute 'pop'