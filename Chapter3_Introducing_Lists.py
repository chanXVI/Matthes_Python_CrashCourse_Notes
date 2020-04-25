# #Lists

# #list is a collection of items in a particular order
# # in python, square brackets [] indicate a list

# nfc_north = ['packers', 'vikings', 'bears', 'lions']
# print(nfc_north)

# print(nfc_north[0])
# print(nfc_north[0:-1])

# print(nfc_north[0].title())

# messsage = f"My favorite football team is the {nfc_north[0].upper()}."
# print(messsage)
# #########

# #Try it Yourself

# # 3-1,3-2
# tennis_pros = ['federer', 'nadal', 'djokovic', 'murray']
# print(tennis_pros[0])
# print(tennis_pros[1])
# print(tennis_pros[2])
# print(tennis_pros[3])
# print(f"{tennis_pros[0].title()} has won over 3 grand slams.")
# print(f"{tennis_pros[1].title()} has won over 3 grand slams.")
# print(f"{tennis_pros[2].title()} has won over 3 grand slams.")
# print(f"{tennis_pros[3].title()} has won over 3 grand slams.")

# # 3-3
# mode_of_transport = ['bus', 'car', 'taxi', 'uber']
# print(f"I would like to own a {mode_of_transport[1]} from the toyota manufacturer.")
# print(f"I think {mode_of_transport[3].upper()} being your main source\n\t of transportaion is way too expensive.")
# #################################################################

# # Modifying elements in a list

# nba_team = ['bucks', 'lakers', 'knicks', 'celtics']
# print(nba_team)

# nba_team[1] = 'clippers'
# print(nba_team)

# nba_team.append('rockets')
# print(nba_team)

# # start with empty list and then append to fill it

# lakers_roster = []
# print(lakers_roster)
# lakers_roster.append('James')
# lakers_roster.append('Davis')
# lakers_roster.append('Kuzma')
# lakers_roster.append("Rondo")
# print(lakers_roster)

# # inserting elements in a list
# print(nba_team)

# nba_team.insert(1, 'bulls')
# print(nba_team)

# # removing elements from a list
# print(nba_team)

# del nba_team[0]
# print(nba_team)

# # removing an item using the pop method

# car_manufacturers = ['honda', 'toyota', 'chevy', 'ford']
# print(car_manufacturers)

# pop_car_manufacturers = car_manufacturers.pop()
# print(car_manufacturers)
# print(pop_car_manufacturers)

# # popping items from any position in a list
# first_owed = car_manufacturers.pop(0)
# print(f"The first car I owned was a {first_owed.title()}.")

# # removing an item by value
# top_QB = ['rodgers', 'brady', 'brees', 'mahomes',"brady", 'jackson']
# print(top_QB)

# top_QB.remove("brady")
# print(top_QB)

# too_old = 'brady'
# top_QB.remove(too_old)
# print(top_QB)
# print(f"\n{too_old.title()} is too old to be considered a current top 5 QB.")
##################################################################

# # Try it Yourself
# # 3-4
# guest_list = ['ghandi', 'einstein', 'jordan']
# print(f'{guest_list[0].title()}, you have been invited to attend the\
#  most prestigious dinner featuring individuals who haved shaped our\
#   world to what it is today')

# print(f'{guest_list[1].title()}, you have been invited to attend the\
#  most prestigious dinner\nfeaturing individuals who haved shaped our\
#   world to what it is today')

# print(f'{guest_list[2].title()}, you have been invited to attend the\
#  most prestigious dinner\n\tfeaturing individuals who haved shaped our\
#   world to what it is today')

# # 3-5
# print(guest_list)
# unable_to_attend = guest_list.pop(1)
# print(guest_list)
# print(f'\n{unable_to_attend.upper()} is unable to attend the party :(')
# print(guest_list)
# guest_list[1] = 'edison'
# print(guest_list)
# guest_list.append('tesla')
# print(guest_list)

# print(f'{guest_list[0].upper()}, this is the final invite to the party')

# print(f'{guest_list[1].upper()}, this is the final invite to the party')

# print(f'{guest_list[2].upper()}, this is the final invite to the party')

# # 3-6
# print (' A bigger dinner table has been found')
# guest_list.insert(0, 'Gates')
# guest_list.insert(2, 'Buffet')
# guest_list.append('Churchhill')

# print(f'{guest_list[0].upper()}, this is the FINAL invite to the party')
# print(f'{guest_list[1].upper()}, this is the FINAL invite to the party')
# print(f'{guest_list[2].upper()}, this is the FINAL invite to the party')
# print(f'{guest_list[3].upper()}, this is the FINAL invite to the party')
# print(f'{guest_list[4].upper()}, this is the FINAL invite to the party')
# print(f'{guest_list[5].upper()}, this is the FINAL invite to the party')

# # 3-7

# print ('\n Unfortunately the new table won"t arrive in time therefore only\
#  two invitees can attend :( ')
# church = guest_list.pop()
# print(f'{church.title()}, you are never invited brotha!!')
# print(guest_list)

# church = guest_list.pop()
# print(f'{church.title()}, you are never invited brotha!!')
# print(guest_list)

# church = guest_list.pop()
# print(f'{church.title()}, you are never invited brotha!!')
# print(guest_list)

# church = guest_list.pop()
# print(f'{church.title()}, you are never invited brotha!!')
# print(guest_list)

# print(f'\n{guest_list[0].upper()}, You still invited!')
# print(f'{guest_list[1].upper()}, You still invited!')

# del guest_list[0]
# print(guest_list)

# del guest_list[0]
# print(guest_list)
# #######################################################################

# # Organizing a list
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse = True)
# print(cars)

# print(len(cars))

# cars.reverse()
# print(cars)

# print("Here is the original list:")
# cars.append('lambo')
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original list again:")
# print(cars)
# #############################################################
