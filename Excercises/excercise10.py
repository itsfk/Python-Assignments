# 10.1
# with open('learning_python.txt') as file_object:
#   line=file_object.read()
  # print(line)
  # for lines in line:
  #     print(lines)
# pi_string=""
# for lines in line:
#     pi_string+=lines
# print(len(pi_string))
# 10.2
# with open('learning_python.txt') as file_object:
#   line=file_object.read()
#   print(line.replace("python","C"))
# 10.3
# filename = 'new.txt'
# ab = input("Enter your name: ")
# with open(filename, 'w') as file:
#  file.write(ab) # write 'ab' user input in above file
# 10.4
# filename = 'new.txt'
# while True:
#     ab=input("Enter your name: ")
#     print("Grreting " + ab)  # printing greeting message to each user(multiple times ask for input due to 'while' loop)
#     with open(filename, 'a') as file_object:  # use open func in which passes arguments of file name and 'a'(to append)
#      file_object.write(ab + "\n")  # 'append' every input into a new line
# 10.6
# try:
#   input1=int(input("Enter Number 1"))
#   input2=int(input("Enter Number 2"))
# except ValueError:
#     print("Please Enter a number")
# else:
#     print(input1+input2)
# 10.7
# print("Press q to quit")
#
# while True:
#     try:
#         first_num = input("Enter first number: ")  # prompts user for input either text(later convert into int) or 'q' for exit'
#
#         if first_num == 'q':
#             break
#         first_num = int(first_num) # converting input into string because user can give 'q' for exit which cannot be quit because it reads as text
#
#         second_num = int(input("Enter second number: "))
#
#         if second_num == 'q':
#             break
#
#         second_num = int(second_num)
#     except ValueError:
#      print("Sorry, pleas enter a number")
#
#     else:
#         answer = int(first_num) + int(second_num)  # adding two numbers and assign it into a var 'answer'
#         print("The result of two number is: " + str(answer) + "\n" )  # print the result 'answer'
# 10.10
# file_path="learning_python.txt"
# try:
#     with open(file_path) as f_obj:
#         content = f_obj.read()
#         print(content)
#
# except:
#     message = "The file, " + file_path + " does not exist."
#
#
# else:
#     line = content
#     line.count('the')
