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
# # working with classes and instances
# class Car: 
# 	"""A simple attempt to represent a car"""

# 	def __init__(self, manufacturer, model, year):
# 		"""Initialize attributes to describe a car"""
# 		self.manufacturer = manufacturer
# 		self.model = model
# 		self.year = year
# 		# setting a default value for a attribute
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		"""Return a neatly formatted descriptive name"""
# 		long_name = f"{self.year} {self.manufacturer} {self.model}"
# 		return long_name.title()

# 	def read_odomenter(self):
# 		"""Print a statement showing the car's milage"""
# 		print(f"This car has {self.odometer_reading} miles on it.")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odomenter()

# # modifying attrubutes value
# 	# modifying an attribute value directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odomenter()
# ##############################################################################
# # modifying an attribute's value through a method
# class Car: 
# 	"""A simple attempt to represent a car"""

# 	def __init__(self, manufacturer, model, year):
# 		"""Initialize attributes to describe a car"""
# 		self.manufacturer = manufacturer
# 		self.model = model
# 		self.year = year
# 		# setting a default value for a attribute
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		"""Return a neatly formatted descriptive name"""
# 		long_name = f"{self.year} {self.manufacturer} {self.model}"
# 		return long_name.title()

# 	def read_odomenter(self):
# 		"""Print a statement showing the car's milage"""
# 		print(f"This car has {self.odometer_reading} miles on it.")

# 	def update_odometer(self, milage):
# 		"""
# 		Set the odometer reading to the given value.
# 		Reject the change if it attempts to roll the odometer back.
# 		"""
# 		if milage >= self.odometer_reading:
# 			self.odometer_reading = milage
# 		else:
# 			print("You can't roll back an odometer!")


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odomenter()

# my_new_car.update_odometer(20)
# my_new_car.read_odomenter()

# my_new_car.update_odometer(25)
# my_new_car.read_odomenter()
# ##############################################################################
# # incrementing an attribute's value through a method
# class Car: 
# 	"""A simple attempt to represent a car"""

# 	def __init__(self, manufacturer, model, year):
# 		"""Initialize attributes to describe a car"""
# 		self.manufacturer = manufacturer
# 		self.model = model
# 		self.year = year
# 		# setting a default value for a attribute
# 		self.odometer_reading = 0


# 	def get_descriptive_name(self):
# 		"""Return a neatly formatted descriptive name"""
# 		long_name = f"{self.year} {self.manufacturer} {self.model}"
# 		return long_name.title()


# 	def read_odomenter(self):
# 		"""Print a statement showing the car's milage"""
# 		print(f"This car has {self.odometer_reading} miles on it.")


# 	def update_odometer(self, milage):
# 		"""
# 		Set the odometer reading to the given value.
# 		Reject the change if it attempts to roll the odometer back.
# 		"""
# 		if milage >= self.odometer_reading:
# 			self.odometer_reading = milage
# 		else:
# 			print("You can't roll back an odometer!")


# 	def increment_odometer(self, miles):
# 		""" 
# 		Add the given amount to the odometer reading.
# 		Reject the change if it attempts to roll the odometer back.
# 		"""
# 		if miles >= 0:
# 			self.odometer_reading += miles
# 		else:
# 			print("You can't roll back an odometer!")


# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odomenter()

# my_used_car.increment_odometer(100)
# my_used_car.read_odomenter()

# my_used_car.increment_odometer(-50)
# my_used_car.read_odomenter()
# ##############################################################################
# # try it yourself
# # 9-4
# class Restaurant:
# 	"""A description of a restaurant"""

# 	def __init__(self, restaurant_name, cuisine_type):
# 		"""the name of the restaurant and it's cuisine type"""
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
# 		self.number_served = 0


# 	def describe_restaurant(self):
# 		"""two piece of information about restaurant"""
# 		print(f"{self.restaurant_name.title()} is located in the United States.")
# 		print(f"They offer dine-in, takeout and delivery.")


# 	def open_restaurant(self):
# 		"""print a message indicating that the restaurant is open"""
# 		print(f"{self.restaurant_name.title()} is currently open.")


# 	def set_number_served(self, customers_served):
# 		self.number_served = customers_served

# 	def increment_number_served(self, customers_served_this_order):
# 		if customers_served_this_order >= 0:
# 			self.number_served += customers_served_this_order

# 		else:
# 			print("You can't serve a negative amount of customers")



# restaurant_1 = Restaurant('sabri', 'indian and pakistani')
# print(restaurant_1.number_served)
# restaurant_1.number_served = 4
# print(restaurant_1.number_served)


# restaurant_1.set_number_served(5)
# print(restaurant_1.number_served)

# restaurant_1.increment_number_served(5)
# restaurant_1.increment_number_served(2)
# restaurant_1.increment_number_served(3)

# print(f"Today we served a total of {restaurant_1.number_served} customers.")
# ##############################################################################
# 9-5
