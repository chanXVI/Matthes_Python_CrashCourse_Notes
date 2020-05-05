# Chapter 8
# Functions 

# # Defining a Function
# # greeter.py
# def greet_user():
#     """Display a simple greeting"""
#     print("Hello!")

# greet_user()
################################################################################
# # Passing information to a function
# def greet_user(username):
#     """Display a simple greeting"""
#     print(f"Hello {username.title()}!")

# greet_user('jordan')

# greet_user('sarah')
################################################################################
# Arguments and Paramaters

# Try it yourself

#  #8-1
# def display_message():
#     """The function will give info on what I have learned so far in chapter 8"""
#     print("Paramaters are the values inside () when defining a function,\
#  where as Arguments are the values inside () when calling the function\
#  itself.\n")

# display_message()
# ##############################################################################
# # 8-2
# def favorite_book(title):
#     """The function will print out your favorite book title"""
#     print(f"One of my favorite books is {title.title()}.")

# favorite_book('harry potter')
# ##############################################################################
# # Passing Arguments

# # Positional Arguments
#     # order matters in positional arguments
# def describe_pet(animal_type, pet_name):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('dog', 'clifford')
#     # multiple function calls
# describe_pet('cat', 'garfield')
# describe_pet('gold fish', 'nemo')

# # Key word arguments
#     # order doesn't matter as long as there are keywords in the argument
# describe_pet(pet_name = 'buster', animal_type = 'rabbit')

# # default values
# def describe_pet(pet_name, animal_type = 'dog'):
#     """Display info about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('clifford')
# describe_pet(pet_name = 'martha')
# describe_pet('buster', animal_type = 'rabbit')
# describe_pet()
# ##############################################################################
# # Try it yourself

# # 8-3
# def make_shirt(size, message):
#     """Displays the size and the message on the shirt"""
#     print(f"The size of this shirt is {size.title()}. {message.title()} is\
#  the message printed on the shirt.\n")

# make_shirt("large", "just do it")
# make_shirt(message = "Change the game", size = 'Medium')

# # 8-4
# def make_shirt(size = 'large', message = 'I love Python'):
#     """Displays the size and the message on the shirt"""
#     print(f"The size of this shirt is {size.title()}. {message.title()} is\
#  the message printed on the shirt.\n")

# make_shirt()
# make_shirt(size = 'Small')
# make_shirt(message = 'Just do it')
# make_shirt('medium', 'got milk')

# # 8-5
# def describe_city(city, country = 'England'):
#     """Print where the city is located"""
#     print(f"{city.title()} is in {country.title()}.\n")

# describe_city('london')
# describe_city('manchester')
# describe_city('paris')
##############################################################################
# Start return values: page 137
