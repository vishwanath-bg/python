# 17/12/2021

# ABSTRACTION

# from abc import ABC, abstractmethod
#
#
# class Bank:
#     def __init__(self):
#         self.bal = 20000
#
#     @abstractmethod
#     def withdraw(self, amount):
#         pass
#
#     @abstractmethod
#     def deposit(self, amount):
#         pass
#
#     @abstractmethod
#     def balance(self):
#         pass
#
#
# class SBI(Bank):
#
#     def withdraw(self, amount):
#         self.bal -= amount
#         self.balance()
#
#     def deposit(self, amount):
#         self.bal += amount
#         self.balance()
#
#     def balance(self):
#         print("bank balance is ", self.bal)
#
#
# a = SBI()
# a.withdraw(1000)
# a.deposit(2000)



######################################################################################################

# polymorphism with methods
# class SBI:
#
#     def balance(self):
#         print("SBI balance")
#
#     def withdraw(self):
#         print("SBI withdraw")
#
#
# class ICICI:
#
#     def balance(self):
#         print("ICICI balance")
#
#     def withdraw(self):
#         print("ICICI withdraw")
#
#
# s = SBI()
# i = ICICI()
#
# # s.balance()
# # i.balance()
# # s.withdraw()
# # i.withdraw()
# object = (s, i)
# for obj in object:
#     obj.balance()
#     obj.withdraw()

#############################################################################################
# polymorphism with inheritance

# class SBI:
#
#     def balance(self):
#         print("SBI balance")
#
#     def withdraw(self):
#         print("SBI withdraw")
#
#
# class ICICI(SBI):
#
#     def balance(self):
#         print("ICICI balance")
#         super().balance()
#
#     def withdraw(self):
#         print("ICICI withdraw")
#         super().withdraw()
#
#
# sbi = SBI()
# icici = ICICI()
# object = (sbi, icici)
# for obj in object:
#     obj.balance()
#     obj.withdraw()


##############################################################################################

#  Regular Expresions
# s = "sony12pvt43ltd798"
# sum = 0
#
# for i in s:
#     if i.isnumeric():
#        sum += int(i)
#
# print(sum)
# l = []
# n = ""
# for i in s:
#
#     if i.isnumeric():
#         a = s.index(i)+1
#         if a < len(s)-1:
#             if s[a].isnumeric() and s[a].isalpha():
#                 continue
#     else:
#         n += i
#         l.append(i)
# print(l)


# s = "hi hello, how are you"
# l_ = list(s)
# print(l_.count(" "))
# or
# print(list(s).count(" "))


############################################################################################
# write a program to count the number of white spaces present in a file


# with open("file1.txt") as f:
#     count_ = 0
#     for line in f:
#         if line.strip():
#             s = list(line).count(" ")
#             count_ += s
#     print(count_)

# import re
#
# with open("file1.txt") as f:
#     count_ = 0
#     for line in f:
#         if line.strip():
#             a = re.findall(r"\s", line)
#             count_ += a.count(" ")
#     print(count_)




############################################################################################
# write a program to count the number of occurances of a particular word in a string

# s = "hello how are you hello"
# l = s.split()
# count = 0
# for i in l:
#     if i == "hello":
#         count += 1
#     else:
#         count = 1
# print(count)
#
#
# using regular expression

import re
#
# s = "hello how are you hello"
# print(len(re.findall("hello", s)))



############################################################################################
# write a program to count the number of occurances of a particular word in a file

# import re
#
# with open("file1.txt") as f:
#     count = 0
#     for line in f:
#         a = len(re.findall("how", line, re.IGNORECASE))
#         count += a
#     print(count)

############################################################################################
# write a program to count the number of occurances of non special characters in the given string
#         ''' s = "hello@world!! welcome!!! to& python*** '''
# import re
# s = "hello@world!! welcome!!! to& python***"
# list_ = re.findall(r"[a-zA-z0-9]", s)
# d = {}
# for i in list_:
#     d[i] = list_.count(i)
#
# print(d)


############################################################################################
#   for the same same string count the number of special character in the above string

# import re
# s = "hello@world!! welcome!!! to& python***"
# print(len(re.findall(r"\W", s)))

############################################################################################
# filter only those characters except digits
#           'sony@12pvt%%43ltd##798!!!'
#
# import re
#
# s = 'sony@12pvt%%43ltd##798!!!'
# print(re.findall(r"\D", s))


############################################################################################
# write a program to count the number of characters in each word and create a dictionary of word and it's length pair
# (ignore special characters)
# ''' s = "hello@ world:) welcome!!! to python:):)'''

# import re
#
# s = "hello@ world:) welcome!!! to python:):)"
# list_ = re.findall(r"\w+", s)
# d = {}
# for i in list_:
#     d[i] = len(i)
# print(d)



# write a program to count number of upper case and lower case characters in string

# import re
#
# s = "Hi hello, How Are You"
# ptr = "[a-z]"
# ptr1 = "[A-Z]"
# for i in (ptr, ptr1):
#     print(len(re.findall(i, s)))


# s = "python is programming language, programming skills needed"
# a = s.find("programming")
#
# while a != -1:
#     print(a)
#     a = s.find("programming", a+len("programming"))

import re
#
# with open("file1.txt", 'r+') as f, open("python.txt", 'w') as f2:
#     for line in f:
#         # print(re.sub("python", "java", line))
#         f2.write(re.sub("python", "java", line))

# write a program to print only the words starting with vowel
s = "hello welcome to python a army is great"
print(re.findall(r"\b[aeiou]\w*", s))
