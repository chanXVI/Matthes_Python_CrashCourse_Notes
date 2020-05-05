# Chapter 7
# User input and while loops

# # how the input function works
# # parrot.py
# message = input("Tell me somethin, and I will repeat it back to you: ")
# print(message)

# # Writing Clear Prompts
# # greeter.py
# name = input("Please enter your name: ")
# print(f"Hello {name.title()}!")
# ##
# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"Hello {name.title()}!")

# # Using int() to Accept numerical input
# age = int(input('How old are you? '))
# # age = int(age)
# print (age >= 18)
# print('herro')

# # rollercoaster.py
# height = int(input("How tall are you, in inches? "))

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# # even_or_odd.py
# number = int(input("Enter a number, and I'll tell you if it's odd or even: "))

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# # Try it yourself
# # 7-1
# rental_car = input("What kind of rental car would you like? ")
# print(f"\nLet me see if I can find you a {rental_car.title()}.")

# # 7-2
# seating_avl = int(input("Table for how many individuals? "))

# if seating_avl > 8:
#     print('\nSorry, you will have to wait 20 more minutes.')
# else:
#     print("\nYour table is ready!!")

# # 7-3

# num = int(input("Please provide a number: "))
# if num % 10 == 0:
#     print(f"\nThe number: {num} is in fact a multiple of ten.")
# else:
#     print(f"\nThe number: {num} isn't a multiple of ten.")
###############################################################################
# # Introducing While Loops
# # counting.py
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# # letting the user choose when to quit
# # parrot.py
# prompt = "\nTell me something, and I will repear it back to you: "
# prompt += "\n Enter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message.upper())

# # Using a Flag
# # parrot.py
# prompt = "\nTell me something, and I will repear it back to you: "
# prompt += "\n Enter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#         print("Game Over")
#     else:
#         print(message)

# # Using Break to exit a loop:
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# # Using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# # Avoiding Infinite loops:
# x = 1
# while x < 5:
#     print(x)
#     x += 1
# ##########################
# x = 1
# while x < 5:
#     print(x)
############################
# # Try it yourself
# # 7-4 Pizza Toppings:
# prompt = "\nEnter the toppings you want to add to your pizza!"
# prompt += "\n(Enter 'quit' when you are done): "

# cooking = True
# while cooking:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         cooking = False
#         print("Thank You for your order.\nYour pizza will be ready in 10-15\
#  min")
#     else:
#         print(f"{toppings.title()} is being added!")
######################################################################
# # 7-5 Movie Tickets:
# prompt = "What is your age?"
# prompt += "(Write 'done' when you don't want any more tickets): "
# buy_tickets = True

# while buy_tickets:
#     ticket = input(prompt)
#     if ticket == 'done':
#         buy_tickets = False
#         print("Thank You for buying our tickets!")
#     else:
#         age = int(ticket)

#         if age < 3:
#             print("Your ticket is free!!")
#         elif age >= 3 and age <= 12:
#             print("Your ticket is $10!")
#         else:
#             print("Your ticket is $15!")
# #####################################################################
# # 7-6 Three exits
# # part 1
# prompt = "What is your age?"
# prompt += "(Write 'done' when you don't want any more tickets): "
# age = input(prompt)

# while age != 'done':
#     age = int(age)

#     if age < 3:
#         print("Your ticket is free!!")
#     elif age >= 3 and age <= 12:
#         print("Your ticket is $10!")
#     else:
#         print("Your ticket is $15!")

#     age = input(prompt)
######################################
# # part 3
# prompt = "What is your age?"
# prompt += "(Write 'done' when you don't want any more tickets): "
# while True:
#     ticket = input(prompt)

#     if ticket == 'done':
#         print("Thank You for buying our tickets!")
#         break
#     else:
#         age = int(ticket)
#         if age < 3:
#             print("Your ticket is free!!")
#         elif age >= 3 and age <= 12:
#             print("Your ticket is $10!")
#         else:
#             print("Your ticket is $15!")
################################################################################
# # Using a While loop with lists and dictionaries:
# # moving items from one list to another to another:
# # confirmed_users.py
# unconfirmed_users = ['alice', 'brian', 'candice']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
########################################################
# # Removing all instances of specific values from a list
# # pets.py
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)
############################
# # Filling a Dictionary with User Input
# # mountain_poll.py
# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     responses[name] = response

#     repeat = input(" Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n---Poll Results---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response.title()}.")
# print(responses)
######################################################################
# # Try it yourself
# # 7-8 
# sandwich_orders = ['tuna', 'meatball', 'blt', 'italian', 'philly steak']
# finished_sandwiches = []

# while sandwich_orders:
#     current_order = sandwich_orders.pop()

#     print(f"I made your {current_order.upper()} Sandwich.")
#     finished_sandwiches.append(current_order)

# print ("\nThe following sandwich has been made:")
# for sandwich in finished_sandwiches:
#     print(sandwich)
#############################################################
# # 7-9
# sandwich_orders = ['tuna', 'pastrami','meatball', 'pastrami', 'blt', 'italian\
# ', 'philly steak', 'pastrami']

# print("The deli has run out of pastrami!")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
############################################################
# # 7-10
# prompt = "If you could visit one place in the world, where would you go? "

# while True:
#     dream_vacation = input(prompt)
#     print(dream_vacation)
    
#     if dream_vacation == 'done':
#         break
