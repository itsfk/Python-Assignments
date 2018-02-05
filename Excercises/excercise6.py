# 6-1
# dict={"first_name":"Faiz","last_name":"Khan","age":"18"}
# for keys,value in dict.items():
#     print("Key "+ keys)
#     print("value "+value)
# 6.2
# dict={"Faiz":18,"Shoaib":20,"Farwa":30,"Ashir":45,"Zohaib":12}
# for keys,value in dict.items():
#     print("Key "+ keys)
#     print("value "+str(value))
# 6.3
# glossary={'list':'contains set of elements & muteable.','tuple':'contains set of elements & immuteable.','remove':'delete item by value.','delete':'also delete item but permanently.','insert':'insert an element, takes two argument in first index of an item and second contain value.',}
# print(" List meaning : " + glossary['list'] + "\n","Tuple meaning : " + glossary['tuple'] + "\n", "Remove meaning : " + glossary['remove'] + "\n", "Insert meaning : " + glossary['insert'] + "\n",)
# 6.4
# glossary={'list':'contains set of elements & muteable.','tuple':'contains set of elements & immuteable.','remove':'delete item by value.','delete':'also delete item but permanently.','insert':'insert an element, takes two argument in first index of an item and second contain value.',}
# for gloss_key, gloss_value in glossary.items():
# print("The term " + gloss_key + "'s meaning in Python is " + gloss_value.title() + ".")
# 6.5.1
# rivers={"Nile":"Egypt","Indus":"Pakistan","Sutlej":"Pakistan"}
# for key,value in rivers.items():
#     print("The "+ key + " runs through "+value)
# 6.5.2
# rivers={"Nile":"Egypt","Indus":"Pakistan","Sutlej":"Pakistan"}
# for keys in rivers.keys():
#     print("Rivers are " + keys)
# 6.5.3
# rivers={"Nile":"Egypt","Indus":"Pakistan","Sutlej":"Pakistan"}
# for value in rivers.values():
#     print("The countrys are "+ value)
# 6.6
# favorite_languages={'jen':'puthon',
#                     'sarah':'c',
#                     'edward':'ruby',
#                     'phil':'python',}
# people_list=['usama','sarah','ali','zaid','saad']                   #new list(polled members) where we check
#
# for ask_pol in favorite_languages.keys():                           #loop for every element in dict and t will store in "ask_pol"
#
#     if ask_pol in people_list:                                      #checking whether "fav_lang"(ask_pol) member registered or not?
#         print(ask_pol.title()+" you already taken pol!")            #if yes then print"Already taken for poll"
#     else:
#         print(ask_pol.title()+" you are advised to take poll.")
# 6.7
# people=[{"first_name": "Faiz", "last_name": "Khan", "age": "18"},{"first_name": "Shoaib", "last_name": "Silat", "age": "20"},{"first_name": "Farwa", "last_name": "Altaf", "age": "22"}]
# for key,value in people[0].items():
#     print(key,value)
# for key, value in people[1].items():
#         print(key, value)
# for key,value in people[2].items():
#     print(key,value)
# 6.8
# cat = {'kind: ' : 'street' , 'owner: ' : 'faiz' }
# dog = {'kind: ' : 'safety' , 'owner: ' : 'ahmed'}
# lion = {'kind: ' : 'jungle' , 'owner: ' : 'khan'}
#
# my_list = [ cat , dog , lion]
#
# print("The first element of list is Cat which have the following information:")
# for a,b in my_list[0].items():
#     print(str(a).title()+ str(b).title())
#
# print("\nThe second element of list is Dog which have the following information:")
# for x , y in my_list[1].items():
#     print(str(x).title()+str(y).title())
#
# print("\nThe second element of list is Dog which have the following information:")
# for r , s in my_list[2].items():
#     print(str(r).title()+str(s).title())
# 6.9
# favorite_places = {'key_1' : 'mecca' , 'key_2' : 'madina' , 'key_3' : 'sham'}
#
# friend_1 = input("Enter your favorite place: ")                                                                      #prompt user for input
# friend_2 = input("Enter your favorite place: ")                                                                      #prompt user for input
#
# favorite_places = {'saad' : 'mecca' , 'zaid' : 'madina' , 'asad' : 'sham' , 'ali ' : friend_1 ,'umer ' : friend_2}   #dict in which last two keys are prompting(user input)
#
# for re, ve in favorite_places.items():                                                                               #loop re, ve are keys and values respectively
#       print("Friend's name is "+re.title()+" his favorite place is "+ve.title())
# 6.10
# 6.11
# cities = {'karachi' : {'country' : 'pakistan' , 'population' : '17 crores' , 'fact' : 'islamic country'}, 'mumbai' : {'country' : 'india' , 'populatuion' : '115 crores' , 'fact' : '2 largest country by population'} , 'sydney' : {'country' : 'australia' , 'population' : '50 crores' , 'fact' : '9,000 beaches approx.'} , }
#
# #create a dictionary which contains dictionary
#
# for k , v in cities.items():                                                       #loop for dict
#     print("Name of the city is " +k.title())                                       #printing name of city i.e key of "dict(cities)"
# print("belongs from " + v['country'].title() + " its fact is " + v['fact'])