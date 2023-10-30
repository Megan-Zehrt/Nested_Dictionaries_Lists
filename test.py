#1

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

x[1][0] = 15  # [1] selects the 'second' array inside of the x array. [0] selects for first number inside the second array.
print(x)
print('*'*20)  # '*' is what I want it to print out, *20 is how many times I want it to print out

students[0]['last_name'] = 'Bryant'  # [0] selects the first array inside of "students" and ['last_name'] selects the key I want it to "print" and "= 'Bryant'" is what I want changed in the "last name"
print(students[0]) # I only want it to print out the first array under "students" so I put [0] after "students"
print('*'*20)

sports_directory['soccer'][0] = 'Andres' # sports_directory is the dictionary I want it to select and ['soccer'] is the array I want it to select, [0] is the first name in the array and "= 'Andres'" is the name I want it to change the first name in the array to
print(sports_directory) # I printed "sports_directory" so It will print out both the basketball and the soccer array
print('*'*20)


z[0]['y'] = 30 # z is the array that I want to select, [0] is the array inside of z and 'y' is which key I want it to select, "= 30" changes what y equals.
print(z)
print('*'*20)

#2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},  #list
         {'first_name' : 'John', 'last_name' : 'Rosales'},    #list
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},    #list
         {'first_name' : 'KB', 'last_name' : 'Tonel'}         #list
    ]

def iterateDictionary(group):
    first_name = group[0]['first_name']  # I made a varieble called first_name and equaled it to group[0]['first/last_name]
    last_name = group[0]['last_name']
    for lists in group:                    # The list is the entire array which the function will go through
        for key in lists:                   # the key will go through each letter/number inside of the list (array)
            print(f"{key} - {lists[key]}")  #prints the key (first/last_name) and the name (jordan, michael, tonel, KB etc.)

print(iterateDictionary(students))  # calls the iterateDictionary fucntion and the array that the function is used for..."students"

#3

def iterateDictionary2(key, group_list):  #key is given for the "first_name" (see line 55) and group_list is used to call the array that it will go through
    for groupobj in group_list: # groupobj is used to go through the group_list (the array).
        print(groupobj[key])   # groupobj is the varieble used to go through the array, and [key] is what the function returned from the array (first_name)

print(iterateDictionary2('first_name', students))   # calls the iterateDictionary2 function and the key, first_name and the array used for this function "students"

def iterateDictionary2(keys, group_list):
    for groupobj in group_list:
        print(groupobj[keys])

print(iterateDictionary2('last_name', students))

#4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(the_dict):  #the_dict is used to call the array
    for key in the_dict:  # the key is used to go through the array 
        print(f"{len(the_dict[key])} {key}")  #len is used for the function to go through the length of the array. key what is returned from the array (the_dict)
        for index in (the_dict[key]): # use index to go through the_dict and return the key
            print(f"{index}") # this returns what the data for the_dict

print(printinfo(dojo))   # calls on the printinfo function and dojo is the array used for this function (called the _dict in the function)

