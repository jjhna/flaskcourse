# Note that double quotes " are mainly used for quotes and for interpolation such as {} or other special functions such as {}

# Here are some string features such as the f string format, the 'f' allows embeded values like {name} to be used in the string
# name = 'Bob'
# print(f'Hi ther me name is {name}')

# greeting = 'Hi ther {} my name is {}'

# formatted = greeting.format(name, 'Jef')
# print(formatted)

# input - note that input only returns a string for whatever input that you enter in
# urname = input('Enter in ur name boi: ')
# print('so ur name isa', urname)

# ursize = input('what isa ur siza? ')
# urnewsize = int(ursize)
# urfloaty = urnewsize / 10.2
# print('ur new siza is', ursize, ' also the floaty isa: {urfloaty:.2f} ok?')
# print(f'my new siza isa {urfloaty:.2f}')

# list - similar to an array
# list = ['bob', 'ray', 'ann']

#tuple - similar to a list but you cannot add or remove elements from a tupple after runtime
# tupple = ('bob', 'ray', 'ann')

#set - like a list but it doesn't keep the same order - in other words it has no order  and duplicates aren't allowed
# set = {'bob', 'ray', 'ann'}

# list[0] = 'sid'
# list.append("mat")
# list.remove('ray')
# print(list)

# set.add('sid')
# print(set)

# Here are some advance methods for sets
# friends = {'bob', 'mat', 'pat'}
# abroad = {'bob', 'pat'}

# to find any set elements that are not in either sets, use .diference, so it will remove any set elements from friends that were in abroad set
# localfriends = friends.difference(abroad)

# meanwhile the .union function will unite both sets, from the abroad set into the friends set, remember no duplicates will be removed or not allowed
# localfriends = friends.union(abroad)

# # .intersection is a function that finds any relationships or similar elements in both sets
# localfriends = friends.intersection(abroad)

# print(localfriends)

# booleans 
# friends = ['bob', 'ann']
# abroad = ['bob', 'ann']

# print(friends == abroad) # should print true, the elements inside each list are the same
# print(friends is abroad) # should print false, because its 2 different lists

# if statements
# whatday = input('what number day? ').lower() # will turn any input into a lower case variant making Monday = monday5


# if whatday == '5':
#     print('itsa true')
# elif whatday == '4':
#     print('4 u picka 4???')
# else:
#     print('way way go away')

# the 'in' keyword that checks if a var or input is inside a list, similar to an if statement but for lists, sets, etc
# movies = {'the order', 'doesnt', 'matter'}
# whatmovie = input('what movie: ')
# print(whatmovie in movies)
# if whatmovie in movies:
#     print('its a true')
# else:
#     print('its a false')

# num = 7
# userinput = input('enter in y: ').lower()

# # examples still using 'in'
# if userinput == 'y':
#     usernum = int(input('enter in a number: '))
#     if usernum == num:
#         print('u got it rite')
#     elif (usernum - num) in (1, -1): # so the if statement checks if the usernum - num is either 1 or -1 in the tuple 
#         print('u were off my 1')
#     else:
#         print('way off bud')

# using While loops
# while True:
#     userinput = input('enter in y: ').lower()
#     if userinput == 'n':
#         break
#     usernum = int(input('enter in a number: '))
#     if usernum == num:
#         print('u got it rite')
#     elif (usernum - num) in (1, -1): # so the if statement checks if the usernum - num is either 1 or -1 in the tuple 
#         print('u were off my 1')
#     else:
#         print('way off bud')

# For Loops
# fwiends = ['bob', 'mat', 'pat', 'ann']

# for friend in fwiends:
#     print(f'the name is {friend}')

# for friend in range(4): # range allows you to repeat the code in the nest loop for a certain amount of times 
#     print(f'the name is {friend}')

# other functions such as sum() gets the sum of a list and len() gets the length of a list for easy access

# To compress a for loop into a list
# friends = ['rof', 'bob', 'sam', 'ann', 'san', 'sid']
# startswith = []

# for friend in friends:
#     if friend.startswith('s'): # startswith() will find if the first char in the string starts with a certain char
#         startswith.append(friend) # note that append() will add in the element into the list 

# the variable below is the exact same for loop from above, so the first friend is the element that you plan to add into the 
# startswith list if the variable starts with an 's' in the for loop of the friends list 
# startswith = [friend for friend in friends if friend.startswith('s')]
# print (startswith)
# print(id(startswith)) # this is the id or address that the list is stored at

# Dictionaries - key, value
# students = {'rat': 24, 'bob': 22, 'ann': 69}
# longstudents = [
#     {'rat': 24, 'bob': 22, 'ann': 69}, 
#     {'rat': 24, 'bob': 22, 'ann': 69},
#     {'rat': 24, 'bob': 22, 'ann': 69}
#     ]
# print(longstudents[1]['rat'])


# thevalues = students.values() # to just print out the values of the dictionary
# print(thevalues)

# for student in students:
    # print(student) # prints out only the keys 
    # print(f'{student}: {students[student]}')

# or you can print by using:
# for student, studentinfo in students.items():
#     print(f'{student}: {studentinfo}')

# desturcting variables - brackets aren't techncially necessary just to define between tuples and lists
# t = 11, 5
# x, y = t
# print(x, y)

# person = ('bob', 42, 'worker')
# name, _, job = person
# print(name, _, job)

# head, *tail = [1, 2, 3, 4, 5]
# print(head)
# print(tail)

# Functions - use def to define a function, must call functions, functions are read from top to bottom so they need to be defined at the top
# def hello():
#     print('hello')
# hello()

# pass = means to do nothing in python
# def add():
#     pass

# arguments and parameters in functions
# def add(one, two = 2):
#     print(one + two)
# add(2, two=3)
# note you need to state the positional arguments first before the keyword arguments, so add(one=2, 2) will not work
# the opposite goes for the default parameter value where two = 2

# returning values from functions, note that you can end up accidently returning back none
# def add(one, two):
#     return one + two
# print(add(2,2))

# lambda functions - functions that don't have a name and is only used to return values, mostly used for inputs and outputs 
# sequence = [1, 2, 3, 4, 5] # this function just doubles all the values in the list using a lambda functjion
# doubled = list(map(lambda x: x * 2, sequence)) # you need to use a list because the map only returns a map object
# print(doubled)

# Additional Dictionary comprhensions
# users = [
#     (0, 'bob', 'passw0rd'),
#     (1, 'ann', 'muhpaass'),
#     (2, 'mat', 'pissw9rd')
# ]

# usermapping = {user[1]: user for user in users} # so your stating that your grabbing the 2nd value from the dictionary to be used as a key for the tuples
# _, username, password = usermapping['bob'] # define the values inside the list of tuples 

# if password == 'passw0rd':
#     print('correct')
# else:
#     print('wong')

# * the star is a special argument that can take a tuple of arguments of any amount or type to be used by the function
# def multiply(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     # print(total)
#     return total

# multiply(1, 2, 3) # so 1 * 2 * 3 = 6
# listnums = [1, 2, 3] 
# multiply(*listnums) # note for list you need to pass the arument as a star as well, so multiply(*list)
# def add(x, y):
#     return x + y
# nums = {'x': 15, 'y': 30}
# print(add(**nums)) # note for nums you need to pass the arument with 2 stars instead, so multiply(**dic)

# You can also Unpack arguments such as tuples but you need to decide wheter to pass it as a tuple or different data type, it just depends on your prefrence
# def apply(*args, operator):
#     if operator == '*':
#         return multiply(*args) # note if you remove the * from the args the same must be done for the multiply function
#     elif operator == '+':
#         return sum(args) # this doesnt need a start because the sum() is a built in function with a *argument already
#     else:
#         return 'error alert'
# print(apply(1, 2, 3, 4, 5, operator = '*')) # multiply all the arguments

# Unpacking keywords arguments - similar to unpacking multiple keyword arguments but being used as dictionaries
# def named(**kwargs):
#     print(kwargs)
# named(name='bob', age=25) # this will end up printing out a dictionary

# Classes start with class
# class Student:
#     # Remember that functions inside a class is a method not a function
#     def __init__(self, name): # special methods: similar to a constructor, so you need to define any variables when you initalize the class
#         self.name = name
#     # def __str__(self): # a special method that will return a string when the class is intalized
#     #     return 'hello w0rld'
#     def __repr__(self): # a special method that will returnr a string that allows the dev to recreate the object, note that str must be commented out for repr to work
#         return f'<Student({self.name})>'

# student = Student('bob')
# print(student)

# Instance method - the first method in a class that use the object as the first parameter, so if it uses self as a parameter
# class Test:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight

#     def instancem(self):
#         print('self test')

#     @classmethod # a class method doesn't require an object being intailaized so it can be called just using: Test.classm()
#     # commonly used to create a new object inside a class, also known as a factory method
#     def classm(cls, name, weight):
#         print('print the cls')
#         return cls(name, weight)

#     @staticmethod # just a function without a class, just to place a method in a class
#     def staticm():
#         print('static method')
#         # return '{}, total stock price: {}'.format(test.name, int(test.stock_price()))

# test = Test('bob', 55)
# test.instancem()
# Test.classm('mat', 25)
# Test.staticm()

# Inheritance example:
# class Tester(Test):
#     def __init__(self, name, weights, capacity):
#         super().__init__(name, weights)
#         self.capacity = capacity
    
#     def __str__(self):
#         return f'{super().__str__()} ({self.capacity} pages remaining)'

# tested = Tester('bob', 69, 55)
# print(tested)

# Class Composition - when you have a class that contains a bunch of classes
# class Bookshelf:
#     def __init__(self, *books):
#         self.books = books
#     def __str__(self):
#         return f"Bookshelf with {len(self.books)} books"

# class Book:
#     def __init__(self, name: str): # another example of type hinting
#         self.name = name
#     def __str__(self) -> str: # an example of type hinting, where the dev is notified that they must use a string for this parameter
#         return f'Book {self.name}'

# book = Book('Harrymuhboi')
# book2 = Book('Urawizzard')
# shelf = Bookshelf(book, book2) # here we pass our two books which are objects/classes to be used as arguments for the Bookshelf class
# print(shelf)

# note this function is utilized by lesson1.1.py filew
# def divide(num: int, num2: int):
#     return num/num2

# You can also perform relative imports by using stack/continous imports, such as:
# from libs.operations import operator
# from .libs import mylib

# Handling errors by creating a traceback by rasing the errors
# def divide(num1, num2):
#     if num2 == 0:
#         raise ZeroDivisionError('num2 cannot be a 0')
#     return num1/num2

# try:
#     average = divide(1/0)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(f'the avg grade is {average}')
# finally:
#     print('thx')

# First class functions are just functions that are just variables: result = calc(20, 4, 5, operator=divide), print(result)

# Decorators - functions that take another function as an argument and returns another function. It allows the extension of an existing function
# defining a decorator
# def hello_decorator(func):
#     # inner1 is a Wrapper function in
#     # which the argument is called
     
#     # inner function can access the outer local
#     # functions like in this case "func"
#     def inner1():
#         print("Hello, this is before function execution")
#         # calling the actual function now
#         # inside the wrapper function.
#         func()
#         print("This is after function execution")
#     return inner1

# # defining a function, to be called inside wrapper
# def function_to_be_used():
#     print("This is inside the function !!")

# # passing 'function_to_be_used' inside the
# # decorator to control its behavior
# function_to_be_used = hello_decorator(function_to_be_used)

# # calling the function
# function_to_be_used()

# Mutable - when objects have the ability to change their values, such as: lists, sets, and dictionaries
# Immutable - are the opposite of mutable such as ints, strings, and tuples