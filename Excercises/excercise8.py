# 8.1
# def displayMessage():
#     print("I am learning about functions")
# displayMessage()
# 8.2
# def favouriteBook(title):
#     print("My favourite book is "+ title)
# favouriteBook("Alice in Wonderland")
# 8.3
# def make_shirt(size,message):
#     print("The shirt size is "+str(size)+ " The message on the shirt should be "+message)
# make_shirt(16,"Cool!")
# make_shirt(message="Pakistan Zinadabad",size=18)
# 8.4
# def make_shirt(message,size="large"):
#     print("The shirt size is "+size+ " The message on the shirt is "+message)
# make_shirt("I love Python")
# make_shirt("I love Javascript",size="medium")
# 8.5
# def describeCity(city,country="Pakistan"):
#     print(city+" is in "+country)
# describeCity("Karachi")
# describeCity("London",country="England")
# 8.6
# def city_country(city1,country1, city2,country2, city3,country3):
#     print(city1.title() + ", " + country1.title() +"\n" + city2.title() + ", " + country2.title() +"\n" + city3.title() + ", " + country3.title())
# city_country('karachi' , 'pakistan' , 'mumbai' , 'india' , 'kabul' , 'afghanistan')
# 8.7
# def makeAlbum(name1,title1,name2,title2,name3,title3):
#     dict={}
#     dict1={}
#     dict2={}
#     dict[name1]=title1
#     dict1[name2]=title2
#     dict2[name3]=title3
#     albums = str(dict) + "\n" + str(dict1) + "\n" + str(dict2)
#     return albums
# a=makeAlbum("Abc","xyz","adc","afd","def","ffd")
# print(a)
# 8.8
# def makeAlbum():
#  while True:
#     dict={}
#     a=input("Enter album")
#     b=input("Enter title")
#     if a and b =="quit":
#         break
#     dict[a]=b
#     return dict
# c=makeAlbum()
# print(c)
# 8.9
# list=["abc","ad","ae"]
# def showMagican(list):
#     for list in list:
#         print(list)
# showMagican(list)
# 8.10
# list=["abc","ad","ae"]
# def make_great(great_magician_lists):                      #declare a new function and pass argument magician_lists
#     for magician_list in great_magician_lists:                      #use for loop for eaccessing each element ij list
#         print("Great "+magician_list.title())                       #printing the message
#
#     return magician_list
# make_great(list)
# 8.12
# def make_sandiwches(*types):
#     print("Making sandwiches with following flavor:")
#     for type in types:
#         print("-" + type)
# make_sandiwches('checiken','veetable','club sandwiches')
# make_sandiwches('simple')
# make_sandiwches('BBQ')
# 8.13
# def make_profile(first, last , **user_info):
#     profile = {}
#     profile['First Name'] = first
#     profile['Last Name'] = last
#     for ab , cd in user_info.items():
#         profile[ab] = cd
#     return profile
# profile  = make_profile('Muhammad ' , 'Umer' , Religion = 'Islam' , Age = 22 , City = 'Karachi' , Country = 'Pakistan')
# print(profile)
# 8.14
# def make_car(manufacturer, model , **other_info):
#     car = {}
#     car['Manufacturer'] = manufacturer
#     car['Model'] = model
#
#     for key , value in other_info.items():
#         car[key] = value
#     return car
#
# car = make_car('subaru' , 'outback', color = 'blue' , tow_package =True)
# print(car)