# # DICTIONARIES
# # A simple Dictionary
# # alien.py
# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# # accessing values in a dictionary
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# # adding key-value pairs
# print('\n',alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# # starting with an empty dictionary
# alien_0 = {}
# print(alien_0)

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# # modify values in a dictionary
# alien_0 = {'x_position': 0, 'y_position': 25}
# alien_0['speed'] = 'medium'

# print(f"original position: {alien_0['x_position']}")

# #move the alien to the right (how far depends on the speed)
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] += x_increment

# print(f"New position: {alien_0['x_position']}")


# # removing key value pairs
# print(alien_0)

# del alien_0['y_position']
# print(alien_0)

# # favorite_languages.py

# favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 
# 'phil': 'python'}

# language = favorite_languages['sarah'].title()

# print(f"Sarah's favorite language is {language}.")

# ron_answer = favorite_languages.get('ron', 'User was not asked this specific\
#  question?')
# jen_answer = favorite_languages.get('jen', 'User was not asked this specific\
# question?')

# print(ron_answer.title())
# print(jen_answer.title())

# # try it yourself
# # 6-1
# person_1 = {'first_name': 'lebron', 'last_name': 'james', 'age': 34,  'city': 'cleveland'}

# print(person_1['first_name'].title())
# print(person_1['last_name'].title())
# print(person_1['age'])
# print(person_1['city'].upper())

# # 6-2

# jersey_num = {}

# jersey_num['dame lillard'] = 0
# jersey_num['lebron james'] = 23
# jersey_num['klay thompson'] = 11
# jersey_num['steph curry'] = 30
# jersey_num['michael jordan'] = 23

# for name, num in jersey_num.items() :
#     print (name.title(),':', num)
###################################################
# # looping through a dictionary

# # user.py
# user_0 = {}
# user_0['username'] = 'efermi'
# user_0['first'] = 'enrico'
# user_0['last'] = 'fermi'
# print(user_0)

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")
# ########################################################
# favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby',\
# 'phil': 'python'}

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.\n")

# for name in favorite_languages.keys():
#     print(name.title())
# print('')

# print("The following languages have been mentioned:")
# for languages in favorite_languages.values():
#     print(languages.upper())

# print("")
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}.")
#     ################################################################
# print('')
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")
# print('')
# for language in set(favorite_languages.values()):
#     print(language.title())
# ###########################################################
# #sets , results in non repetitive valuse
# language = {'python', 'java', 'c', 'java'}
# x = 0
# for var in language:
#     print(x)
#     x += 1
############################################################
# # try it yourself
# # 6-5

# river_border = {'amazon': 'brazil', 'nile': 'egypt', 'yangtze': 'china'}

# for river, country in sorted(river_border.items()):
#     print(f"The {river.title()} runs through {country.title()}.")
# print('')
# print('The rivers examined include:')
# for river in sorted(river_border.keys()):
#     print(river.title())
# print('')
# print("The countries examined include:")
# for country in sorted(river_border.values()):
#     print(country.upper())
#############################################################
# # 6-6
# favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby',\
# 'phil': 'python'}

# poll_takers = ['alex', 'raj', 'sarah', 'brian', 'phil', 'leonard']

# for participants in poll_takers:
#     if participants in favorite_languages.keys():
#         language = favorite_languages[participants].title()
#         print(f"{participants.title()}, thank you for taking the poll!")
#         print(f"\tI see you love {language}.\n")
#     else:
#         print(f"{participants.title()}, please finish you poll!!!\n")
##########################################################################
# # Nesting
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# # Make an empty list for storing aliens
# aliens = []

#     # make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

#     # show the first five aliens

# for alien in aliens[:5]:
#     print(alien)
# print('...')

#     # show how many aliens have been created:
# print(f"Number of aliens created: {len(aliens)}")

#     # each alien might be the same but are considered a seperate object
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# for alien in aliens[:5]:
#     print(alien)
########################################################
# # A list inside a dictionary
# # pizza.py
# pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese']}

#     # summarze the order
# print(f"You ordered a {pizza['crust']}-crust pizza "
#      "with the following topptings:")
# for toppings in pizza['toppings']:
#     print('\t'+toppings)

# # favorite_languages.py
# favorite_languages = {'jen': ['python', 'ruby'], 'sarah': ['c'],'edward': \
#                     ['ruby', 'go'], 'phil': ['python', 'haskell'],}

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")

#     for language in languages:
#         if len(languages) >= 2:
#             print(f"\t{language.upper()}")
#         else:
#             print(f"\t{language.lower()}")
################################################################
# # A Dictionary in Dictionary
# # many_users.py
# users = {
#     'aeinstein': {
#     'first': 'albert',
#     'last': 'einstein',
#     'location': 'princeton',
#     },
#     'mcurie': {
#     'first': 'marie',
#     'last': 'curie',
#     'location': 'paris',
#     }
# }

# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
#     location = f"{user_info['location'].upper()}"

#     print(f"Full Name: {full_name}")
#     print(f"location: {location}")
#####################################################################
# # Try It Yourself
# # 6-7 People:
# person_1 = {
#             'first_name': 'lamelo',
#             'last_name': 'ball',
#             'age': 19,
#             'college': 'international',
#             }
# person_2 = {
#             'first_name': 'james',
#             'last_name': 'wiseman',
#             'age': 19,
#             'college': 'memphis',
#             }
# person_3 = {
#             'first_name': 'ethan',
#             'last_name': 'happ',
#             'age': 21,
#             'college': 'wisconsin',
#             }
# people = [person_1, person_2, person_3]

# for person in people:
#     print(f"{person['first_name'].title()} {person['last_name'].title()} \
# is currently attending {person['college'].upper()}.")
#     print(f"He is {person['age']} years old.")
#####################################################################
# # 6-8 Pets:

# pet_1 = {
#         'animal': 'dog',
#         'owner_name': 'emily',
#         }
# pet_2 = {
#         'animal': 'cat',
#         'owner_name': 'matt',
#         }

# pet_3 = {'animal': 'hamster',
#         'owner_name': 'richard'
#         }
# pets = [pet_1, pet_2, pet_3]

# for pet in pets:
#     print(f"The owner {pet['owner_name'].title()} has a pet {pet['animal']}.")
################################################################################
# # 6-9 Favorite Places:
# favorite_places =   {
#                     'max': ['tokyo', 'kyoto', 'seoul'],
#                     'tim': ['kyoto', 'san francisco', 'new york'],
#                     'ryan': ['melbourne'],
#                      }

# for name, places in favorite_places.items():
#     print(f"\nThere are {name.title()}'s favorite places:")

#     for place in places:
#         (print(f"\t{place.upper()}"))
################################################################################
# # 6-10
# jersey_numbers =   {
#                     'lebron': [6, 23],
#                     'garnett': [21, 5, 2],
#                     'howard': [12, 8, 21, 39],
#                      }

# for name, numbers in jersey_numbers.items():
#     print(f"\nThere are {name.title()}'s jersey numbers:")

#     for num in numbers:
#         (print(f"\t{num}"))
################################################################################
# # 6-11 Cities:
# cities = {
#     'pokhara': {
#             'country': 'nepal',
#             'population': 264_991,
#             'fact': 'Pokhara is one of the best travel destinations in Nepal', 
#             },
#     'milwaukee': {
#             'country': 'united states',
#             'population': 592_025,
#             'fact': 'Milwaukee is home to the worlds largest music\
#  festival', 
#              },
#     'new york city': {
#             'country': 'united states',
#             'population': 8_399_000,
#             'fact': 'New York City is the most populous city in the United Stat\
# es',
#             },
#         }               

# for city, some_facts in cities.items():
#     print(f"{city.title()} is one of the three cities we have done our research\
#  on today.\n")
#     country = f"{some_facts['country'].title()}"
#     population = f"{some_facts['population']}"
#     fact = f"{some_facts['fact']}"

#     print(f"This particular city is located in {country}. It has a population of\
#  {population}. {fact}. \n")
