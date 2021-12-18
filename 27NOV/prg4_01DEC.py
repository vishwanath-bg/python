# 01/ 12/ 2021
# Comprehension
######################################################################################################################
# write  program to create a list of tuples with first character and world pair

# l1 = ['amazon', 'flipkart', 'walmart', 'google', 'yahoo']
# l2 = []
# # for i in l1:
# #     l2.append(i[0])
# # d = list(zip(l2, l1))
# # print(d)
#
# for i in l1:
#     l2.append((i[0], i))
# print(l2)

# l2 = [(i[0], i) for i in l1]
# print(l2)
######################################################################################################################
# write a program to print index and item of the dictionary

# d = {'a': 1, 'b': 2}

# for index, item in enumerate(d.items()):        # normal unpacking
#     print(index, item)

# for index, (key, value) in enumerate(d.items()):  # deep unpacking
#     print(index, key, value)


######################################################################################################################
# write a program to create a dictionary using two lists where elements of the first list should be key and element of second list should be value

# l1 = [1, 2, 3, 4, 5]
# l2 = ["a", "b", "c", "d", "e"]
#
# d = dict(zip(l1, l2))
# print(d)


######################################################################################################################
# write a program to flip key and value in a dictionary

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# d1 = {}
#
# for (key, value) in d.items():
#     d1[value] = key
# print(d1)

# d1 = {value: key for (key, value) in d.items()}
# print(d1)
######################################################################################################################
# write a program to create a dictionary of character and it's count pair

# s = "hello world"
# d = {}

# for i in s:
#     d[i] = s.count(i)

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# d = {i: s.count(i) for i in s}
# print(d)

#######################################################################################################################
# write a program to count vowels in a string and create a dictionary

# s = "hi i am vishwa where are you from"


# for i in s:
#     if i in 'aeiouAEIOU':
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
# print(d)


# from collections import defaultdict
# s = "hi i am vishwa where are you from"
# d = defaultdict(int)
# for i in s:
#     if i.lower() in 'aeiou':
#         d[i] += 1
# print(dict(d))

# s = "hi i am vishwa where are you from"
# d = {}
#
# for i in s:
#     if i.lower() in 'aeiou':
#         d[i] = s.count(i)
# print(d)

# s = "hi i am vishwa where are you from"
# d = {i: s.count(i) for i in s if i.lower() in'aeiou' }
# print(d)


##############################################################################################
# write a program to create a dictionary with word and it's count pair

# string = "python is a programming language"
# d = {}
# l1 = string.split()
# for i in l1:
#     d[i] = l1.count(i)
# print(d)

# l2 = {i[0]: string.count(i) for i in string.split()}
# print(l2)
##############################################################################################
# write a program to get the below output
# string = "python is a programming language"
# o/p: {'p': ['python', 'programming], 'i': [is], 'a': [a], 'l': ['language']}

# string = "python is a programming language"
# d = {}
# l1 = string.split()
# for i in l1:
#     if i[0] not in d:
#         d[i[0]] = [i]
#     else:
#         d[i[0]] += [i]

# print(d)

# from collections import defaultdict
# string = "python is a programming language"
# d = defaultdict(list)
# l1 = string.split()
# l2 = []
# for i in l1:
#     d[i[0]] += [i]
# print(d)



##############################################################################################
# Comprahenssion
# write a program to create a list of sqaures from the given list
# l1 = [1, 2, 3, 4]
# l2 = []
# for item in l1:
#     l2.append(item **2)
# print(l2)
#
# l1 = [1, 2, 3, 4]
# l2 = [(item ** 2) for item in l1]
# print(l2)


##############################################################################################
# write a program to create list of even numbers from 1 to 50
# l1 = []
# for item in range(1, 51):
#     if item % 2 ==0:
#           l1.append(item)
# print(l1)

# l1 = [item for item in range(1, 51) if item % 2  == 0 ]
# print(l1)



##############################################################################################
# write a program to create a list of words starting with vowel

# s = 'hello world how are u'
# l1 = s.split()
# l2 = []
# for i in l1:
#     if i[0] in 'aeiouAEIOU':
#         l2.append(i)
# print(l2)

# s = 'hello world how are u'
# l1 = s.split()
# l2 = [i for i in l1 if i[0] in 'AEIOUaeiou']
# print(l2)




######################################################################################################################
# write a program to create a list of words with even length

# s = "Avengers Assemble iron man"
# l1 = s.split()
# l2 = []
# for i in l1:
#     if len(i) % 2 == 0:
#         l2.append(i)
# print(l2)

# s = "hi i am vishwa"
# l1 = s.split()
#
# l2 = [i for i in l1 if len(i) % 2 == 0]
# print(l2)




################################################################################################################
# write a program to filter all the languages starting with p
# languages = ['python', 'java', 'perl', 'php', 'python', 'js', 'c++']
# l1 = []

# for i in languages:
#     if i[0].startswith('p'):
#         l1.append(i)
# print(l1)


# languages = ['python', 'java', 'perl', 'php', 'python', 'js', 'c++']
# l1 = [i for i in languages if i[0].startswith('p')] # list comprehension
# l1 = {i for i in languages if i[0].startswith('p')} # set comprehension
# print(l1)



################################################################################################################
# write a program to create a list of words if the word is of even length store it as it is else reverse and store it

# languages = ['python', 'java', 'perl', 'php', 'python', 'js', 'c++']
# l1 = []
# for i in languages:
#     if len(i) % 2 == 0:
#         l1.append(i)
#     else:
#         l1.append(i[::-1])
# print(l1)

# languages = ['python', 'java', 'perl', 'php', 'python', 'js', 'c++']
# l1 = [i if len(i) % 2 == 0 else i[::-1] for i in languages]
# print(l1)




#######################################################################################################################
#  write a program to create list of tuples of word and it's length pair only if the words are of odd length
# s = "hello world welcome to new era"
# l1 = s.split()
# l2 =[]
# for item in l1:
#     if len(item) % 2 != 0:
#         l2.append((item, len(item)))
# print(l2)

# s = "hello world welcome to new era"
# l1 = s.split()
# l2 = [(item, len(item)) for item in l1 if len(item) % 2 != 0]
# print(l2)



#######################################################################################################################
# create a dictionary of word and it's length pair
# s = "hi hello how are you"
# d = s.split()
# d1 = {}
# for i in d:
#     d1[i] = len(i)
#
# print(d1)

# s = "hi hello how are you"
# d = {i: len(i)for i in s.split()}
# print(d)


#######################################################################################################################
# write a program to create a dictionary of character and it's count pair
# s = "hello world"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# from collections import defaultdict
# s = "hello world"
# d = defaultdict(int)
# for i in s:
#     d[i] += 1
# print(d)

# s = "hello world"
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)

# s = "hello world"
# d = {i: s.count(i) for i in s}
# print(d)




#######################################################################################################################
# write a program to create a dictionary of character and it's asci value pair

# s = 'hello world'
# d = {}
#
# for i in s:
#     if i not in d:
#         d[i] = ord(i)
# print(d)
#
# s = 'hello world'
# d = {}
# for i in set(s):
#     d[i] = ord(i)
#
# s = 'hello world'
# d = {i: ord(i) for i in set(s)}
# print(d)



#################################################################################################################
# write a program to create dictionary using below two list

# d = ['hai', 'hello', 'many', 'how']
# d1 = [1, 2, 3, 4]
# d = {key: item for key, item in zip(d, d1)}
# print(d)

# d = ['hai', 'hello', 'many', 'how']
# d1 = [1, 2, 3, 4]
# d2 = {}
# for key, value in zip(d, d1):
#     d2[key] = value
# print(d2)



#################################################################################################################
# write a program to create a dictionary with word as key if the word is of even length use the same word as value else reverse the word and store it as value
#s = "hello world welcome to new era"
# d = s.split()
# d1 = {}
# for i in d:
#     if len(i) % 2 == 0:
#         d1[i] = i
#     else:
#         d1[i] = i[::-1]
# print(d1)

# d = ['hai', 'hello', 'are', 'you']
# d1 = {i: i if len(i) % 2 == 0 else i[::-1] for i in d}
# print(d1)



#################################################################################################################
# write a program to check wheather value is interger if it is integer reverse the value and print if it is a string print same
# d = {'a': 12, 'b': 24, 'c': 'cat'}
# d1 = {}
# for key, value in d.items():
#     if isinstance(value, int):
#         temp = str(value)[::-1]
#         d1[key] = int(temp)
#     else:
#         d1[key] = value
# print(d1)

# d = {'a': 12, 'b': 24, 'c': 'cat'}
# d1 = {key: str(value)[::-1] if isinstance(value, int) else value for key, value in d.items()}
# print(d1)




#################################################################################################################
# write a  program to add items of two list

# a = [1, 2, 3]
# b = [3, 5, 7]
# c = []
# for i, j in zip(a, b):
#     c.append(i+j)
# print(c)

# a = [1, 2, 3]
# b = [3, 5, 7]
# c = [i + j for i, j in zip(a, b)]
# print(c)



#################################################################################################################
# write a list comprehension to print factorial of given list


# n = 5
# fact =1
#
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# l1 = [1, 2, 3]
# l2 = []
# for i in l1:
#     fact = 1
#     for num in range(1, i+1):
#         fact *= num
#     l2.append(fact)
# print(l2)

# from math import factorial
# l1 = [1, 2, 3]
# l2 = [factorial(i) for i in l1]
# print(l2)



#################################################################################################################
# l = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# l1 = []
# for i in l:
#     l1.extend(i)
# print(l1)

# l = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# l1 = []
# for i in l:    # [1, 2, 3, 4]
#     for j in i: # 1, 2 , 3, 4
#         l1.append(j)
# print(l1)

# l = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# l1 = [j for i in l for j in i]
# print(l1)




#################################################################################################################

# PATTERNS #

#################################################################################################################
# *
# * *
# * * *
# * * * *

# for i in range(4):
#     for j in range(i+1):
#         print('* ', end="")
#     print()

# for i in range(1, 5):
#     print('* ' * i)



#################################################################################################################

# * * * *
# * * *
# * *
# *

# for i in range(4, 0, -1):
#     print('* ' * i)


#################################################################################################################
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1, 5):
#     print('* ' * i)
# for j in range(5, 0, -1):
#     print('* ' * j)

#################################################################################################################
#       *
#     * *
#   * * *
# * * * *
#
# for i in range(1, 5):
#     print(f'{"* " * i:>8}')

#################################################################################################################
#    *
#   * *
#  * * *
# * * * *

# for i in range(1, 5):
#     print(f"{'* ' * i:^8}")

#################################################################################################################
# * * * *
#  * * *
#   * *
#    *

# for i in range(4, 0, -1):
#     print(f"{'* ' * i:^8}")


#################################################################################################################
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# pat = ''
# for i in range(1, 5):
#     pat += str(i) + " "
#     print(pat)


#################################################################################################################
#       1
#     1 2
#   1 2 3
# 1 2 3 4

# pat = ''
# for i in range(1, 5):
#     pat += str(i) + " "
#     print(f"{pat:>8}")
#


#################################################################################################################

# a
# a b
# a b c
# a b c d
# a b c d e

# pat = ""
# for i in range(ord("a"), ord("e")+1):
#     pat += chr(i) + " "
#     print(pat)


#################################################################################################################

#         a
#       a b
#     a b c
#   a b c d
# a b c d e

# pat = ""
# for i in range(ord("a"), ord("e")+1):
#     pat += chr(i) + " "
#     print(f'{pat:>10}')

#################################################################################################################

# a b c d e
# a b c d
# a b c
# a b
# a

# for i in range(4, -1, -1):
#     for j in range(i+1):
#         x = ord("a") + j
#         print(chr(x), end=" ")
#     print()
#
################################################################################################################

# *
# *
# * *
# *
# * * *
# *
# * * * *
# *

# for i in range(1, 5):
#     print('* ' * i)
#     print('*')


################################################################################################################

# for i in range(5):
#     for j in range(i+1):
#         print(ord("a") + j, " ", end="")
#     print()



################################################################################################################
# A  A  A  A  A
# B  B  B  B
# C  C  C
# D  D
# E
#
# x = 65
# for i in range(4, -1, -1):
#     for j in range(i+1):
#         print(chr(x), " ", end="")
#     print()
#     x += 1

##################################################################################################################

#     a
#    a b
#   a b c
#  a b c d
# a b c d e

# ptr = ""
# for i in range(ord('a'), ord('e')+1):
#     ptr += chr(i) + " "
#     print(f"{ptr:^10}")


##################################################################################################################



