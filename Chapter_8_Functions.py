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
# # Return Values

# # returning a simple value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
##############################################################################
# # making an argument optional
# def get_formatted_name(first_name, last_name, middle_name = ''):
#     """ Return a full name, neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('stevie', 'vaughan', 'ray')
# print(musician)
##############################################################################
# # returning a dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('jimi', 'hendrix')
# print(musician)
# ##############################################################################
# def build_person(first_name, last_name, age = None):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age = 27)
# print(musician)
# ##############################################################################
# # Using a function with a while loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# # This is an infinite loop
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}!")

# # function with a while loop with quit condition:
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(Enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}!")
# ##############################################################################
# # Try it Yourself

# # 8-6
# def city_country(city, country):
#     """Returns whatever argument is given for the paramaters city and country"""
#     location = f"{city}, {country}"
#     return location.title()

# place_1 = city_country('paris', 'france')
# place_2 = city_country('berlin', 'germany')
# place_3 = city_country('london', 'england')

# total_place = [place_1, place_2, place_3]

# for place in total_place:
#     print(f"\n{place}")
##############################################################################
# # 8-7
# def make_album(artist_name, album_title, number_of_songs = None):
#     """ Returning a dictionary containing an artist name and their\
#      album title"""
#     album = {'name': artist_name.title(), 'album title': album_title.title()}

#     if number_of_songs:
#         album['number of songs'] = number_of_songs
    
#     return album

# album_1 = make_album('kanye west', 'graduation', 13 )
# album_2 = make_album('john mayer', 'continuum')

# albums = [album_1, album_2]
# for album in albums:
#     print(album)
# ##############################################################################
# # 8-8
# def make_album(artist_name, album_title, number_of_songs = None):
#     """ Returning a dictionary containing an artist name and their\
#      album title"""
#     album = {'name': artist_name.title(), 'album title': album_title.title()}

#     if number_of_songs:
#         album['number of songs'] = number_of_songs
    
#     return album

# while True:
#     print("Welcome to  the record store!!!")
#     print("If you are don't need any help, please write 'done': ")

#     artist = input("What is the name of the artist? ")

#     if artist == 'done':

#         print("Thank You for shopping at the record store.")
#         break

#     album = input(f"What is the name of the {artist.title()}'s album? ")

#     if album == 'done':

#         print("Thank You for shopping at the record store!")
#         break

#     catalog = make_album(artist, album)
    
#     print(catalog)
# ##############################################################################
# # Passing a list
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)
# ##############################################################################
# # modifying a list without using functions
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing models: {current_design}")
    
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
# # ##############################################################################
# # modifying a list in a function using functions
# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed models after printing
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing models: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# """ you can past the list with [:] extension in the funciton so it takes the
# copy of that list and saves the original"""
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# # the original is still intact because [:] was used when passing the list
# print(unprinted_designs)
# ##############################################################################
# # try it yourself
# # 8-9
# def text_history(short_texts):
#     """Prints out the texts within a list given as argument"""
#     for text in short_texts:
#         print(text)

# short_texts = ['hi', 'hello', 'how are you?', 'bye', 'good morning']
# text_history(short_texts)
# ##############################################################################
# # 8-10
# short_texts = ['hi', 'hello', 'how are you?', 'bye', 'good morning']
# sent_messages = []

# def send_messages(message_sent, message_received):
#     """
#     prints out the messages being sent and moves the messages from send list to
#     sent list
#     """
#     while message_sent:
#         text = message_sent.pop()
#         print(text)
#         message_received.append(text)

# send_messages(short_texts, sent_messages)
# print('short texts =',short_texts)
# print('sent messages =',sent_messages)
# ##############################################################################
# # 8-11
# short_texts = ['hi', 'hello', 'how are you?', 'bye', 'good morning']
# sent_messages = []

# def send_messages(message_sent, message_received):
#     """
#     prints out the messages being sent and moves the messages from send list to
#     sent list
#     """
#     while message_sent:
#         text = message_sent.pop()
#         print(text)
#         message_received.append(text)

# send_messages(short_texts[:], sent_messages)
# print('short texts =',short_texts)
# print('sent messages =',sent_messages)
# ##############################################################################
# # Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ##############################################################################
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ##############################################################################
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# ##############################################################################
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user"""
#     user_info['first_name'] = first.title()
#     user_info['last_name'] = last.title()
#     return user_info

# user_profile = build_profile('albert', 'einstein', location = 'princeton',\
# field = 'physics')

# print(user_profile)
# ##############################################################################
# # Try it yourself
# # 8-12
# def sandwich_toppings(*toppings):
#     """collects and prints out the toppings you want in your sandwich"""
#     print("\nThe following toppings in your sandwich include:")
#     for topping in toppings:
#         print(f"- {topping.title()}")

# sandwich_toppings('turkey', 'ham', 'lettuce', 'tomato', 'bacon', 'nine-grain\
#  bread')
# sandwich_toppings('tuna', 'mayo', 'lettuce', 'provolone', 'whole wheat')
# ##############################################################################
# # 8-13
# def build_profile(first_name, last_name, **user_info):
#     """Build a dictionary containing my personal info"""
#     user_info['first_name'] = first_name.title()
#     user_info['last_name'] = last_name.title()
#     for key, value in user_info.items():
#         print(f"{key}: {value}")
#     return user_info

# user_profile = build_profile('michael', 'jordan', year_born = 1963,\
# Net_Worth = '2.1 billion')

# print(user_profile)
# ##############################################################################
# # 8-14
# def make_car(manufacturer, model_name, **car_info):
#     car_info['manufacturer'] = manufacturer.title()
#     car_info['model_name'] = model_name.upper()
#     return car_info

# car = make_car('toyota', 'prius', MPG = 54, color = 'Electric Blue',\
# safety_rating = '*****')

# print(car)
# ##############################################################################
