# # Working with lists

# # Looping through an entire list
# nfl_teams = ['bears', 'raiders', 'jets', 'giants']
# for team in nfl_teams:
#     print(team)

# for team in nfl_teams:
#     print(f'{team.title()}, will probably not make the playoffs this year.')
#     print(f'Therefore {team.upper()} will most likely get a high draft pick next year.\n')

# print('The teams above will tank for the first four picks :(')
# # # Try it Yourself 
# # 4-1
# top_pizza_flavors = ['pepporoni', 'cheese', 'sausage']
# for pizza in top_pizza_flavors:
# 	print(f'I like {pizza.upper()} pizza.\n')

# print('These are my favorite pizza flavors.')

# #4-2
# pets = ['dog', 'cat', 'rabbit']

# for pet in pets:
# 	print(f'\nA {pet.title()} would make a great pet.')

# print('\nAny of these animals would make a great pet!')
# ###################################################################

# # Using range function
# for num in range(1,6):
# 	print(num)

# # Using range() to make a list of numbers
# numbers = list(range(0,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# ##########################################
# squares = []
# for num in range(1, 11):
# 	square = num ** 2
# 	squares.append(square)

# print(squares)

# # can also write the code above more concisely
# squares = []
# for value in range(1,11):
# 	squares.append(value**2)

# print(squares)

# # list comprehension , helps do the same action (create and append) in one single line
# squidward = [x**2 for x in range(1,11)]
# print('\n',squidward)


# # simple stats with a list of numbers

# digits = [1,2,3,4,5,6,7,8,9,0]

# print(f'\n{min(digits)}\n')
# print(f'{max(digits)}\n')
# print(f'{sum(digits)}')

# # Try it yourself
# # 4-3
# for x in range(1,21):
#   print(x)

# # 4-4
# big_list = []
# for num in range (2,1_000_000):
#   big_list.append(num)
# print(big_list)

# # list comprehension to do the same thing above
# big_list = [x for x in range(1,1_000_001)]

# for x in big_list:
#   print(x)

# # 4-5
# big_list = [x for x in range(1,1_000_001)]
# print(min(big_list))
# print(max(big_list))
# print(sum(big_list))

# # 4-6
# odd_list = [x for x in range(1,20,2)]
# print(odd_list)
# for y in odd_list:
#     print (y)

# # 4-7
# mult_3_list = [x for x in range(3,31,3)]
# print(mult_3_list)

# # 4-8 and 4-9

# #doing the cube using list comprehension
# cube_list = [x**3 for x in range(1,11)]
# print(cube_list)

# # doing the cube using the long way
# cube_list2 = []
# for num in range (1,11):
#    cube_list2.append(num**3)
# print(cube_list2)

# # Slicing a List
# mlb_teams = ['brewers', 'reds', 'cubs', 'pirates', 'yankees']
# print(mlb_teams[0:3])
# print(mlb_teams[-3:])

# # looping through a slice
# nba_team = ['bulls', 'bucks', 'knicks', 'thunder', 'warriors']

# print('My top three basketball teams are:')
# for team in nba_team[:3]:
#     print(team.title())

# # copying a list
# shaq_teams = ['magic', 'lakers']
# dwight_teams = shaq_teams[:]
# print('Shaq has played for')
# print(shaq_teams)
# print('\nDwight has also played for')
# print(dwight_teams)

# shaq_teams.append('heat')
# dwight_teams.append('rockets')

# print('\nShaq has played for')
# print(shaq_teams)
# print('\nDwight has played for')
# print(dwight_teams)

# # 4-10
# baseball_player = []
# baseball_player.append('jeter')
# baseball_player.append('arod')
# baseball_player.append('big_papi')
# baseball_player.append('manny')
# baseball_player.append('braun')
# baseball_player.append('prince')
# baseball_player.append('griffey')
# baseball_player.append('dimmagio')
# baseball_player.append('aaron')
# baseball_player.append('mantle')


# print('The first three items in the list are:')
# for player in baseball_player[:3]:
#     print(player)

# print('Three player from the middle of the list are:')
# for player in baseball_player[4:7]:
#     print(player)

# print('The last three items in the list are:')
# for player in baseball_player[-3:]:
#     print(player)

# # 4-11

# pizza = ['pep', 'sausage', 'bacon']
# friends_pizza = pizza[:]

# pizza.append('pineapple')
# friends_pizza.append('anchovies')

# print('My favorite pizza are:')
# for flavor in pizza:
#     print(flavor)

# print("\nMy friend's favorite pizza are:")
# for flavor in friends_pizza:
#     print(flavor)

# # TUPLES
# # Defining a Tuple
# # Dimentions.py

# dimention = (200, 50)
# print(dimention[0])
# print(dimention[1])

# my_t = (1,)
# print(type(my_t))

# for size in dimention:
#     print(size)

# # writing over a tuple
# dimentions = (200, 50)
# print('Original dimentions:')
# for dimention in dimentions:
#     print(dimention)

# dimentions = (400, 100)
# print("\nModified dimentions:")
# for dimention in dimentions:
#     print(dimention)

# # 4-13
# buffet_staple = ('rice', 'chicken', 'soy sause', 'broccoli', 'fortune cookie')
# for food in buffet_staple:
#     print(food)
# print('\n')
# buffet_staple = ('rice', 'beef', 'soy sause', 'noodles', 'fortune cookie')
# for food in buffet_staple:
#     print(food)
