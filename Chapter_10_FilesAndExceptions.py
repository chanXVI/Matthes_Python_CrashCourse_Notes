# # Chapter 10

# # file paths
# with open('text_files/pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents)
# ##############################################################################
# # reading line by line
# filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
# 	for line in file_object:
# 		print(line, end='')
# ##############################################################################
# # making a list of lines from a file
# filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# for line in lines:
# 	print(line, end='')
# ##############################################################################
# # working with a file's contents
# filename = 'text_files/pi_digits.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))
##############################################################################
# # large files: one million digits
# filename = 'text_files/chapter_10/pi_million_digits.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))
# ##############################################################################
# # is your birthday contained in Pi?
# filename = 'text_files/chapter_10/pi_million_digits.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
# 	print("Your birthday appears in the first million digits of pi!")
# else:
# 	print("our birthday does not appear in the first million digits of pi.")
# ##############################################################################
# # try it yourself
# # 10-1
# filename = 'learning_python.txt'

# with open(filename) as file_object:
# 	lines = file_object.read()
# 	print(lines)
# #######################################

# filename = 'learning_python.txt'

# with open(filename) as file_object:
# 	for line in file_object:
#  		print(line, end='')
# ######################################
# filename = 'learning_python.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# for line in lines:
# 	print(line.strip())
# print(len(lines))
# ##############################################################################
# filename = 'learning_python.txt'

# with open(filename) as file_object:
# 	lines = file_object.readlines()

# paragraph = ''
# for line in lines:
# 	paragraph += line.strip()

# print(paragraph)
# draft_1 = paragraph.replace('python', 'C')
# print('')
# print(draft_1)
# ######################################
# filename = 'learning_python.txt'

# with open(filename) as file_object:
# 	paragraph = file_object.read()
# 	print(paragraph)

# draft_1 = paragraph.replace('python', 'C')
# print('')
# print(draft_1)
# ##############################################################################
# # writing to a file

# # writing to an empty file
# # writing multiple lines
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
# 	file_object.write("I love programming.\n")
# 	file_object.write("I love creating new games.\n")
	
# # appending to a file
# with open(filename, 'a') as file_object:
# 	file_object.write("I also love finding meaning in large datasets.\n")
# 	file_object.write("I also love creating apps that run in a browser.\n")

# with open(filename, 'r') as file_object:
# 	trial = file_object.read()
# 	print(trial)
# ##############################################################################
# # try it yourself

# # 10-3
# name = input("What is your full name?  ")

# filename = 'guest.txt'
# with open(filename, 'w') as file_object:
#  	file_object.write(name.title()+'\n')
# ##############################################################################
# # 10-4
# print("Enter 'quit' when you're finished." )
# filename = 'guest.txt'
# while True:
# 	name = input("What is your full name?  ")
# 	if name == 'quit':
# 		break
# 	else:
# 		with open(filename, 'a') as file_object:
#  			file_object.write(name.title()+'\n')
# 		print(f"Hi {name.title()}, you've been added to the guest book.")
# ##############################################################################
# # 10-5
# print("Enter 'quit' when you're out of reasons")
# filename = 'programming.txt'

# while True:
# 	answer = input("What do you like about programming?  ")
# 	if answer == 'quit':
# 		break
# 	else:
# 		with open(filename, 'a') as file_object:
# 			file_object.write(answer+'\n')
# ##############################################################################
# # Exceptions
# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")
# ##############################################################################
# # using exceptions to prevent crashes
# # the else block

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
# 	first_number = input("\nFirst number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("Second number: ")
# 	if second_number == 'q':
# 		break

# 	try:
# 		answer = int(first_number) / int(second_number)
# 	except ZeroDivisionError:
# 		print("You can't divide by 0!")
# 	else:
# 		print(answer)
# ##############################################################################
# # handling the FileNotFoundError exception

# filename = 'alice.txt'
# try:
# 	with open(filename, encoding='utf-8') as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	print(f"Sorry, the file {filename} does not exist.")
# ##############################################################################
# # analyzing text

# title = "Alice in Wonderland"
# analyze_text = title.split()
# print(analyze_text)
######################################
# filename = 'text_files/chapter_10/alice.txt'

# try:
# 	with open(filename, encoding='utf-8') as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	print(f"Sorry, the file {filename} does not exist.")
# else:
# 	# Count to approximate number of words in a file.
# 	words = contents.split()
# 	num_words = len(words)
# 	print(f"The file {filename} has about {num_words} words.")
# ##############################################################################
# # working with multiple files
# # failing silently (using pass)

# def count_words(filename):
# 	"""Count the approximate number of words in a file."""
# 	try:
# 		with open(filename, encoding='utf-8') as f:
# 			contents = f.read()
# 	except FileNotFoundError:
# 		pass
# 	else:
# 		# Count to approximate number of words in a file.
# 		words = contents.split()
# 		num_words = len(words)
# 		print(f"The file {filename} has about {num_words} words.")

# filename = 'text_files/chapter_10/alice.txt'
# count_words(filename)
# print('')

# filenames = ['text_files/chapter_10/alice.txt',
# 			'text_files/chapter_10/siddartha.txt',
# 			'text_files/chapter_10/moby_dick.txt',
# 			'text_files/chapter_10/little_women.txt']
# for filename in filenames:
# 	count_words(filename)
# ##############################################################################
# # try it yourself
# # 10-6, 10-7
# while True:
# 	try:
# 		first_number = int(input("\nFirst number: "))
# 		second_number = int(input("\nSecond number: "))
# 		print(first_number + second_number)
# 	except ValueError:
# 		print("One of your inputs is not an interger")
# ##############################################################################
# # 10-8
# cat_name = 'garfield'
# filename = 'cats.txt'
# with open(filename, 'w') as file_object:
# 	file_object.write(cat_name+'\n')

# while True:
# 	cat_name = input("What is a cat's name?  ")
# 	if cat_name == 'quit':
# 		break
# 	else:
# 		with open(filename, 'a') as file_object:
#  			file_object.write(cat_name+'\n')
# 		print(f"Cat name {cat_name} has been added to cats.txt")

# dog_name = 'clifford'
# filename = 'dogs.txt'

# with open(filename, 'w') as file_object:
# 	file_object.write(dog_name+'\n')

# while True:
# 	dog_name = input("Name a dog: ")
# 	if dog_name == 'quit':
# 		break
# 	else:
# 		with open(filename, 'a') as file_object:
# 			file_object.write(dog_name+'\n')
# 		print(f"Dog named {dog_name} has been added to dogs.txt")
        ################################

# filenames = ['dogs.txt', 'cats.txt']
# for filename in filenames:
# 	print("\nReading file: " + filename)
# 	try:
# 		with open(filename) as file_object:
# 			contents = file_object.read()
# 			print(contents)

# 	except FileNotFoundError:
# 		print("  Sorry, I can't find that file.")
        ################################

# def animal_names(filename):
# 	"""Print the name of animals in a file"""
# 	try:
# 		with open(filename, 'r+') as file_object:
# 			contents = file_object.read()
# 	except FileNotFoundError:
# 		pass
# 	else:
# 		# print the name of the animals in the file
# 		print("\nReading file: " + filename)
# 		print(contents)

# filename = 'dogs.txt'
# animal_names(filename)

# filename = 'cats.txt'
# animal_names(filename)
# ##############################################################################
# # finding how many times the world spermacetti is in the file mobydick
# filename = 'text_files/chapter_10/moby_dick.txt'

# with open(filename, 'r+') as file_object:
# 	contents = file_object.read()
# 	common_word = contents.lower().count('spermacetti')
# 	print(common_word)
# ##############################################################################
# # start page 202 : STORING DATA
# # using json.dump() and json.load()

# import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = 'numbers.json'
# with open(filename, 'w') as f:
# 	json.dump(numbers, f)
# ###########################################
# import json

# filename = 'numbers.json'
# with open(filename, 'r') as f:
# 	numbers = json.load(f)

# print(numbers)
# ##############################################################################
# # saving and reading user-generated data
# import json

# username = input("What is your name?  ")

# filename = 'username.json'
# with open(filename, 'w') as f:
# 	json.dump(username, f)
# 	print(f"We will remember you when you come back, {username}!")
# # ##################################
# import json

# filename = 'username.json'
# with open(filename, 'r+') as f:
# 	username = json.load(f)
# 	print(f"Welcome back, {username.title()}!")
# ##############################################################################
# import json

# # load the username if it has been stored properly
# # otherwise prompt for the username and store it
# filename = 'username.json'

# try:
# 	with open(filename, 'r+') as f:
# 		username = json.load(f)
# except FileNotFoundError:
# 	username = input("What is your name? ")

# 	with open(filename, 'w') as f:
# 		json.dump(username, f)
# 		print(f"We will remember you when you come back, {username}!")
# else:
# 	print(f"Welcome back, {username.title()}!")
# ##############################################################################
# # refactoring
# import json

# def greet_user():
# 	"""Greet the user by name"""
# 	filename = 'username.json'

# 	try:
# 		with open(filename, 'r+') as f:
# 			username = json.load(f)
# 	except FileNotFoundError:
# 		username = input("What is your name? ")

# 		with open(filename, 'w') as f:
# 			json.dump(username, f)
# 			print(f"We will remember you when you come back, {username}!")
# 	else:
# 		print(f"Welcome back, {username.title()}!")

# greet_user()
# ##############################################################################
# # 10-13 verify user portion was added here
# import json

# def get_stored_username():
# 	"""Get stored username if available"""
# 	filename = 'username.json'
# 	try:
# 		with open(filename, 'r+') as f:
# 			username = json.load(f)
# 	except FileNotFoundError:
# 		return None
# 	else:
# 		return username
# 			#################################

# def get_new_username():
# 	"""Prompt for a new username"""
# 	username = input("What is your name?  ")
# 	filename = 'username.json'
# 	with open(filename, 'w') as f:
# 		json.dump(username, f)

# 	return username

# 			#################################
# def greet_user():
# 	"""Greet the user by name"""
# 	username = get_stored_username()
# 	while username:
# 		verify = input(f"Is you user name {username}?('yes' or 'no')")
# 		if verify.lower() == 'yes':
# 			print(f"Welcome back, {username.title()}!")
# 			break
# 		else:
# 			username = get_new_username()
# 			print(f"We'll remember you when you come back, {username.title()}.")
# 			break


# greet_user()
# ##############################################################################
# # try it yourself
# # 10-11

# import json

# favorite_number = int(input("What is you favorite number?  "))
# filename = 'favorite_number.json'

# with open(filename, 'w') as f:
# 	json.dump(favorite_number, f)
# # ########################################
# import json

# filename = 'favorite_number.json'

# with open(filename, 'r+') as f:
# 	num = json.load(f)
# 	print(f"I know your favorite number! It's {num}.")
# ##############################################################################
# # 10-12
# import json
# filename = 'favorite_number.json'
# try:
# 	with open(filename, 'r+') as f:
# 		num = json.load(f)
# except FileNotFoundError:
# 	favorite_number = input("What is your favorite number?  ")

# 	with open(filename, 'w') as f:
# 		json.dump(favorite_number, f)
# else:
# 	print(f"I know your favorite number! It's {num}.")
# ##############################################################################
