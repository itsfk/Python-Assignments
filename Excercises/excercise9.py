# 9.1
# class resturant():
#     def __init__(self,name,cousine):
#         self.name=name
#         self.cousine=cousine
#     def describe_resturant(self):
#         print("The person is " +self.name +" His is cousine is "+self.cousine)
#     def open_resturant(self):
#         print("The resturant is open")
# my=resturant("Faiz","Chinese")
# print(my.describe_resturant())
# print(my.open_resturant())
# 9.2
# class resturant():
#     def __init__(self,name,cousine):
#         self.name=name
#         self.cousine=cousine
#     def describe_resturant(self):
#         print("The person is " +self.name +" His is cousine is "+self.cousine)
#     def open_resturant(self):
#         print("The resturant is open")
# my=resturant("Faiz","Chinese")
# my1=resturant("Rohail","Indian")
# my2=resturant("Shoaib","Pakistani")
# print(my.describe_resturant())
# print(my1.describe_resturant())
# print(my2.describe_resturant())
# 9.3
# class User():
#     def __init__(self,first_name,last_name,email):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.email=email
#     def describe_user(self):
#         print("The user First name "+self.first_name)
#         print("The user Last name " + self.last_name)
#         print("The user email " + self.email)
#     def GreetUser(self):
#         print("Hello " + self.first_name)
# user=User("Faiz","Khan","faiz.ggmu@gmail.com")
# user1=User("Shoaib","Silat","shoaib.12@gmail.com")
# print(user.describe_user())
# print(user.GreetUser())
# print(user1.describe_user())
# print(user1.GreetUser())
# 9.4
# class resturant():
#     def __init__(self,name,cousine,number_served=0):
#         self.name=name
#         self.cousine=cousine
#         self.number_served = number_served
#         self.incr=12
#     def set_number_served(self):
#         print("The set number is "+str(self.number_served))
#     def inc(self):
#         self.incr=self.incr+self.number_served
#         print('The increment value is '+ str(self.incr))
#     def describe_resturant(self):
#         print("The person is " +self.name +" His is cousine is "+self.cousine)
#     def open_resturant(self):
#         print("The resturant is open")
# my=resturant("Faiz","Chinese",10)
# print(my.set_number_served())
# print(my.inc())
# 9.5
# class User():
#     def __init__(self,first_name,last_name,email):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.email=email
#         self.login_attempts=0
#     def increment_login(self):
#         self.login_attempts+=1
#     def reset_attempts(self):
#         self.login_attempts = 0
#     def describe_user(self):
#         print("The user First name "+self.first_name)
#         print("The user Last name " + self.last_name)
#         print("The user email " + self.email)
#     def GreetUser(self):
#         print("Hello " + self.first_name)
# user=User("Faiz","Khan","faiz.ggmu@gmail.com")
# user.increment_login()
# user.increment_login()
# user.increment_login()
# user.increment_login()
# print(" Log in Attempts: " + str(user.login_attempts))
# user.reset_attempts()
# print("Log In attempts: " + str(user.login_attempts))
# 9.6
# class resturant():
#     def __init__(self,name,cousine):
#         self.name=name
#         self.cousine=cousine
#     def describe_resturant(self):
#         print("The person is " +self.name +" His is cousine is "+self.cousine)
#     def open_resturant(self):
#         print("The resturant is open")
# class IceCream(resturant):
#     def __init__(self,name,cousine,flavours):
#         super().__init__(name,cousine)
#         self.flavours=flavours
#     def describe_ice_flv(self):
#         print("The ice cream has following flavors: ")
#         for ab in self.flavours:
#           print(ab.title())
#
# iceRest = IceCream('BBQ tonight' , 'BBQ', ['chocolate' , 'pista' , 'blue berry'])
# print(iceRest.describe_ice_flv())
# 9.8
# class User():
#     def __init__(self,first_name,last_name,email):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.email=email
#         self.login_attempts=0
#     def increment_login(self):
#         self.login_attempts+=1
#     def reset_attempts(self):
#         self.login_attempts = 0
#     def describe_user(self):
#         print("The user First name "+self.first_name)
#         print("The user Last name " + self.last_name)
#         print("The user email " + self.email)
#     def GreetUser(self):
#         print("Hello " + self.first_name)
# class Admin(User):
#     def __init__(self,first_name,last_name,email):
#         super().__init__(first_name,last_name,email)
#         self.right=Privilages()
#
#
# class Privilages():
#     def __init__(self,privilage=['it can add post', 'it can delete post', 'it can be user']):
#         self.privilage=privilage
#
#     def show_privileges(self):  # method for admin's right(defined in a list)
#         print("The admin has the following rights: ")
#         for ab in self.privilage:
#             print(ab.title())
# my=Admin("Yousuf","Khan","Qutub")
# print(my.right.show_privileges())
