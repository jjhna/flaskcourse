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
students = {'rat': 24, 'bob': 22, 'ann': 69}
# longstudents = [
#     {'rat': 24, 'bob': 22, 'ann': 69}, 
#     {'rat': 24, 'bob': 22, 'ann': 69},
#     {'rat': 24, 'bob': 22, 'ann': 69}
#     ]
# print(longstudents[1]['rat'])


# thevalues = students.values() # to just print out the values of the dictionary
# print(thevalues)

print()