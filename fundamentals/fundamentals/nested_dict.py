# 1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] = 15
# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
# 1.3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
# 1.4 Change the value 20 in z to 30
z[0]['y'] = 30


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# 2 Iterate Through a List of Dictionaries
def iterate_dictionary(some_list):
    for student in some_list:
        temp_line = ''
        for key, val in student.items():
            temp_line += key+' - '+val+', '
        print(temp_line[:-2])

iterate_dictionary(students) # returns formatted to match bonus challenge

# 3 Get Values From a List of Dictionaries
def iterate_dictionary_2(key_name, some_list):
    for student in some_list:
        print(student[key_name])

iterate_dictionary_2('first_name', students)
iterate_dictionary_2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


# 4 Iterate Through a Dictionary with List Values
def print_info(some_dict):
    for key, values in some_dict.items():
        print(str(len(values)),key)
        for val in values:
            print(val)

print_info(dojo)
