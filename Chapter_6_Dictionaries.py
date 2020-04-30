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
#start page 106
