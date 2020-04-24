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

# #Finish Page 42 try it yourself
