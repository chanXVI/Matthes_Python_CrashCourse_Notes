# # Chapter 9
# # Classes
# # Creating and Using a Class

# # creating the dog class

# class Dog:
#     """A simple attempt to model a dog"""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")

#     # making an instance from a class
# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
    
#     # accesing attributes
# print(my_dog.name.upper())
    
#     # calling methods
# my_dog.sit()
# my_dog.roll_over()
# ##############################################################################
# # creating multiple instances
# class Dog:
#     """A simple attempt to model a dog"""

#     def __init__(self, name, age):
#         """Initialize name and attributes"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name.title()} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name.title()} rolled over!")


# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)

# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name.title()}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
# ##############################################################################
# # try it yourself

# # 9-1, 9-2
# class Restaurant:
#     """ A description of a Restaurant"""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Restaurant name and type"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """two piece of information about the restaurant"""
#         print(f"{self.restaurant_name.title()} is located in Chicago.")
#         print(f"{self.restaurant_name.title()} serves\
#  {self.cuisine_type.title()} cuisine.")

#     def open_restaurant(self):
#         """indicate that the restaurant is open"""
#         print(f"{self.restaurant_name.upper()} is OPEN.\n")


# restaurant_1 = Restaurant('sabri', 'indian and pakistani')
# restaurant_2 = Restaurant("giordanos", 'classic italian')
# restaurant_3 = Restaurant("fireside lounge", 'cajun-spiced')

# # print(f"The name of the restaurant is {restaurant_1.restaurant_name.title()}.")
# # restaurant_1.describe_restaurant()
# # restaurant_1.open_restaurant()

# # print(f"The name of the restaurant is {restaurant_2.restaurant_name.title()}.")
# # restaurant_2.describe_restaurant()
# # restaurant_2.open_restaurant()

# # print(f"The name of the restaurant is {restaurant_3.restaurant_name.title()}.")
# # restaurant_3.describe_restaurant()
# # restaurant_3.open_restaurant()

#             # same as above but lost easier by listing the instances
# food_places = [restaurant_1, restaurant_2, restaurant_3]

# for places in food_places:
#     print(f"The name of the restaurant is {places.restaurant_name.title()}.")
#     places.describe_restaurant()
#     places.open_restaurant()
# ##############################################################################
# # 9-3
# class User:
#     """A description of a group of NBA players"""

#     def __init__(self, first_name, last_name, number, team, all_star):
#         """ Detailed info regarding the players"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.number = number
#         self.team = team
#         self.all_star = all_star

#     def describe_user(self):
#         print(f"{self.first_name.title()} {self.last_name.title()} plays\ for the
#  {self.team.title()}.")

#         if self.all_star == True:
#             print(f"{self.first_name.title()} made the All Star Team this year.")
#         else:
#             print(f"{self.first_name.title()} didn't made the All Star Team\
#  this year.")

#     def jersey_number(self):
#         print(f"{self.first_name.title()} {self.last_name.title()} wears jersey\
#  number: {self.number}\n")

# player_1 = User('lebron', 'james', 23, 'lakers', True) 
# player_2 =User('luka', 'doncic', 77, 'dallas mavericks', True)
# player_3 =User('john', 'wall', 11, 'wizards', False)

# players = [player_1, player_2, player_3]


# print(f"The following players surveyed were:")
# for player in players:
#     print(f"-{player.first_name.upper()} {player.last_name.upper()}")
# print('')
# for player in players:
#     player.describe_user()
#     player.jersey_number()
# ##############################################################################
# page 162: Working with classes and instances
