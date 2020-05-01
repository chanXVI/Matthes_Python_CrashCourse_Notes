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

###### PAGE 118: Start learning the while loop #################################
