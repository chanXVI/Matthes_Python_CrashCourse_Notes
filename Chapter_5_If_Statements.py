# # If Statements
# # cars.py
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# # toppings.py
# requested_toppings = 'chicken'

# if requested_toppings != 'bacon':
#     print('Hold the bacon!')

# # numbers.py
# answer = 18

# if answer != 21:
#     print('Thay is not the correct answer. Please try again!')

# # banned_users.py
# banned_users = ['andrew', 'carolina', 'david']
# user = 'Andrew'

# if user.lower() in banned_users:
#     print('This account is barrred from posting responses.')
# else:
#     print(f"{user.title()}, you can post a response if you wish!")

# # 5-1
# car = 'honda'
# print("Is car == 'honda'? I predict True")
# print(car == 'honda')

# print("\nIs car == 'toyota'? I predict False")
# print(car == 'toyota')


# nfc_north = ['packers', 'bears', 'vikings', 'lions']

# team = 'PACKERS'

# if team.lower() in nfc_north:
#     print(f"{team.title()} are in the NFC north.")
# else:
#     print (f"The {team.upper()} are not in the nfc north division.")
#
# # 5-3, 5-4, 5-5
# alien_color = ['green', 'yellow', 'red', 'yellow']

# color = 'GREEN'

# if color.lower() in alien_color:
#     print('You have earned five points.')

# else:
#     print('Not one of the colors.')


# color = 'YeLLow'

# if color.lower() in alien_color:
# 	if color.lower() == 'green':
# 		print('You have earned five points.')
# 	elif color.lower() == 'yellow':
# 		print('You have earned 10 points.')
# 	elif color.lower() == 'red':
# 		print('You have earned 15 points.')
# else:
# 	print('You didn"t shoot the alien')

# # 5-6
# age = 3

# if age < 2:
# 	print('The person is a baby.')
# elif 2 <= age < 4:
# 	print('The person is a toddler.')
# elif 4 <= age < 13:
# 	print('The person is a kid.')
# elif 13 <= age < 20:
# 	print('The person is a teenager.')
# elif 20 <= age < 65:
# 	print('The person is an adult.')
# elif 65 <= age:
# 	print('This person is an elder.')

# # 5-7
# favorite_fruits = ['bananas', 'mango', 'watermelon']

# fruit = 'Watermelon'

# if fruit.lower() in favorite_fruits:
# 	print(f'I really love {fruit.upper()}.')
# else:
# 	print(f"I don't really like {fruit.title()}.")

# # toppings.py
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
# 	if requested_topping == 'green peppers':
# 		print("Sorry we are out of green peppers right now.")
# 	else:
# 		print(f"Adding {requested_topping}.")

# print("\nFinished making your pizza.")
# #########################################
# requested_toppings = ['bacon', 'sausage', 'peppers']
# #########################################
# requested_toppings = []

# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		print(f"Adding {requested_topping}.") 
# 	print("\nFinished making your pizza!")
# else:
# 	print("Are you sure you want a plain pizza?")

# # Using Multiple Lists
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni','\
# pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'pineapple']

# for requested_topping in requested_toppings:
# 	if requested_topping in available_toppings:
# 		print(f"Adding {requested_topping.title()}")
# 	else:
# 		print(f"Sorry we don't have {requested_topping.upper()}.")
# print("\nFinished making your pizza!")

# # 5-8
# usernames = ['john', 'ryAn186', 'Admin', 'jsmOove', 'chriscarter']\
# # 5-9
# usernames = []
# if usernames:
# 	for user in usernames:
# 		if user.lower() == 'admin':
# 			print (f"Hello {user.upper()}, would you like to see a status report? ")
# 		else:
# 			print(f"Hello {user}, thank you for logging in again.")
# else:
# 	print ("We need to find some users!")

# # 5-10
# current_users = ['jomboy', 'rayallen20', 'dwade3', 'UD40', 'lDON77', 'Bron6']

# new_users = ['ad3', 'Bron6', 'iverson3', 'shaq34', 'UD40']

# for user in new_users:
# 	if user in current_users:
# 		print(f"Username {user} has already been used.\n\
# Please try a different one :(\n") 
# 	else:
# 		print(f"Username {user} is available!\n")

# # 5-10 taking case sensitive letter into account 
# current_users = ['jomboy', 'rayallen20', 'dwade3', 'UD40', 'lDON77', 'Bron6']

# for x in range(len(current_users)):
# 	current_users[x] = current_users[x].lower()

# new_users = ['ad3', 'BRON6', 'iverson3', 'shaq34', 'ud40']

# for user in new_users:
# 	if user.lower() in current_users:
# 		print(f"Username {user} has already been used.\n\
# Please try a different one :(\n") 
# 	else:
# 		print(f"Username {user} is available!\n")

# # 5-11
# num_list = [num for num in range(1,10)]

# for value in num_list:
# 	if value == 1:
# 		print(f"{value}st\n")
# 	elif value == 2:
# 		print(f"{value}nd\n")
# 	elif value == 3:
# 		print(f"{value}rd\n")
# 	else:
# 		print(f"{value}th\n")
