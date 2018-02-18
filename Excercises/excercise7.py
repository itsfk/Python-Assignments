# 7.1
# car=input("What type of rental car you want")
# print("Let me see if we can find a " +car)
# 7.2
# users=int(input("How many people are in the dinner group"))
# if users>8:
#     print("You will have to wait")
# else:
#     print("Table is ready")
# 7.3
# a=int(input("Enter any number"))
# if a %10==0:
#     print("Multiple of 10")
# else:
#     print("Not a multiple")
# 7.4
# while True:
#     a=input("Enter Pizza toppings")
#     if a=="quit":
#         break
#     else:
#         print(a)
# 7.5
# while True:
#     a=int(input("enter age"))
#     if a<3:
#         print("The ticket is free")
#     elif a>=3 and a<=12:
#         print("The ticket is 10$")
#     elif a>12:
#         print("The ticket is 15$")
#  7.6
# while True:
#     a=(input("enter age"))
#     if a=="quit":
#         break
#     a=int(a)
#     if a<3:
#         print("The ticket is free")
#     elif a>=3 and a<=12:
#         print("The ticket is 10$")
#     elif a>12:
#         print("The ticket is 15$")
#     elif a=="quit":
#         break
# 7.7
# msg = "How old are you?"
# msg += "\nEnter ok when you are finished. "
# while msg:
#   print(msg)
# 7.8
# sandwichOrders=["Tuna fish","BBQ","Club"]
# finishedSandwich=[]
# while sandwichOrders:
#     removes=sandwichOrders.pop()
#     finishedSandwich.append(removes)
#     print("I made your "+removes)
# for finishedSandwich in finishedSandwich:
#     print("Done with order")
# 7.9
# sandwich_orders = ['chicken' , 'pastrami' , 'club' , 'mayo', 'pastrami' , 'vegetable' , 'pastrami' ]
# finished_sandwiches = []
#
# print("Deli has run out of pastrami")
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#     print("")
# while sandwich_orders:
#     ordering_sandwiches = sandwich_orders.pop()
#     finished_sandwiches.append(ordering_sandwiches)
#     print("You sandwiche "+ordering_sandwiches.title()+"is making...\n")
#
# for finished_sandwiche in finished_sandwiches:
# print("New sandwiches are: "+finished_sandwiche)
# 7.10
# tour = {}
#
# polling =True
#
# while polling:
#     person_name = input("What is your name: ")
#     desried_place = input("Where do you want to go: ")
#
#     tour[person_name] = desried_place
#
#     more_place = input("Do you want to add more place(yes/no) ")
#     if more_place =='no':
#         polling =False
#
#     for key , value in tour.items():
# print("Person "+key+ " want to go "+value+ " for tour")
