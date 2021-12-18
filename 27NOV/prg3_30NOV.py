# a = "hello world"
# for i in enumerate(a):
#     print(list(i), end=" ")
#
# for j in enumerate(a):
#     print(j[0], j[1], sep=" : ")

# for index, item in enumerate(a):
#     print(index, item)


############################################################################
# a = "hello world"
# for item in range(len(a)):
#     if a[item] in 'aeiouAEIOU':
#         print(item, a[item])

# for index, item in enumerate(a):
#     if item.lower() in 'aeiou':
#         print(index, ':', item)


##################################################################
# write a program print keys in dictionary

# d = {'a': 1, 'b': 2, 'c': 3}

# for key in d:
#     print(key, end=" ")
#
# for key in d.keys():
#     print(key, end=" ")
#
# for key, value in d.items():
#     print(key, end=" ")


##################################################################
# write a program to print all the values in dictionary

# d = {'a': 1, 'b': 2, 'c': 3}
#
# for key in d:
#     print(d[key])
#
# for key in d.keys():
#     print(d[key])
#
# for key, value in d.items():
#     print(value)



##################################################################
# write a program to index a dictionary

# d = {'a': 'apple', 'b':'ball', 'c': 'cat'}
#
# for key in enumerate(d):
#     print(key)
# for key in enumerate(d.items()):
#     print(key)


##################################################################
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a, b, c, *d = l1
# print(a, b, c, d)




#########################################################
# l1 = ['a', 'b', 'c', 'd']
# l2 = [1, 2, 3]
#
# for item in zip(l1, l2):
#     print(item)


######################################################################
# reversing the string
# 1st method
# s = "hello"
# s1 = ""
# print(s[::-1])

# 2nd method
# for i in range(len(s)):
#     s1 = s[i] + s1
# print(s1)

# for i in s:
#     s1 = i + s1
# print(s1)

# 3rd method
# l1 = list(s)
# l1.reverse()
# print("".join(l1))

# 4th method
# for item in reversed(s):
#     print(item, end="")


######################################################################
#
# s = 'hello'
# d = {}

# for index, item in enumerate(s):
#     d[index] = item
# print(d)

# for item in range(len(s)):
#     d[item] = s[item]
# print(d)

# d2 = dict(enumerate(s))
# print(d2)

######################################################################
# write a program to create a list of element raised to the power of thier indicies

# l1 = [12, 3, 4, 5, 8]
# l2 = []
# for index, item in enumerate(l1):
#     l2.append(item ** index)
# print(l2)
# print(l1)
# l3 = []
# for i in zip(l1, l2):
#     l3.append(i)
# print(l3)


######################################################################
# write a program to create a dictionary of character and its count pair

# s = "hello bro how are you and where are you from"
# d = {}
# count = 0
# count1 = 0
# for index, item in enumerate(s):
#     d[item] = s.count(item)
#     count += 1
# print(d)
#
# s1 = set(s)
# for item in s1:
#     d[item] = s.count(item)
#     count1 += 1
# print(d)
#
# print(count)
# print(count1)



###############################################################################################
# write a program to print the vowels in the given string

# s = "python is awesome"
#
# for char in s:
#     if char.lower() in 'aeiou':
#         print(char, end=" ")

# using while loop
# i = 0
# while i < len(s):
#         if s[i] in 'aeiou':
#             print(s[i], end=" ")
#         i +=1

###############################################################################################
# write a program to print only numbers in the string

# s = "sony123pvt45ltd76"

# for i in s:
#     if i.isnumeric():
#         print(i, end=" ")

# for i in range(len(s)):
#     if s[i].isdigit():
#         print(s[i], end=" ")

# i = 0
# while i < len(s):
#     if s[i] in '1234567890':
#         print(s[i], end=" ")
#     i += 1



###############################################################################################
# write a program to add all the numbers in the string

# s = "sony123pvt45ltd76"
# sum = 0

# for i in s:
#     if i.isnumeric():
#         sum += int(i)
# print(sum)

# i = 0
# while i < len(s):
#     if s[i] in '1234567890':
#         sum += int(s[i])
#     i += 1
# print(sum)



###############################################################################################
# write a program to print each character in a string in reverse order

# s = "hello"

# for i in s[::-1]:
#     print(i, end=" ")

# for i in reversed(s):
#     print(i, end=" ")

# for i in range(1, len(s)+1):
#     print(s[len(s)-i], end=" ")



####################################################################################
# write a program to count number of digits in the string

# s = "sony123pvt45ltd76"
# count = 0
#
# for i in s:
#     if i.isnumeric():
#         count += 1
# print(count)



####################################################################################
# write a program to count vowels in string
# s = "sony123pvt45ltd76"
# count = 0
#
# for i in s:
#     if i.isalpha():
#         if i not in 'aeiou':
#             print(i, end=" ")

####################################################################################
# s1 = "hai"
# s2 = "bye"
#
# for i, j in zip(s1, s2):
#     print(i, j)



####################################################################################
# write a program to get below output(if vowel is present in any one of the sting print it)
# s1 = 'hai world'
# s2 = 'bye hello'
# a  y
# i  e
# o  e
# d  o

# s1 = 'hai world'
# s2 = 'bye hello'
#
# for i, j in zip(s1, s2):
#     if i.lower() in 'aeiou' or j.lower() in 'aeiou':
#         print(i, j)



####################################################################################
# write a program to print the index as well as character in the given string only if the character is present in odd indicies

# s = "hello world"
#
# for index, value in enumerate(s):
#     if index % 2 != 0:
#         print(index, value)


####################################################################################
# write a program to print the item and it's corespondense index in the list

# l1 = ['apple', 'google', 'flipkart', 'walmart', 'amazon']
#
# for index, value in enumerate(l1):
#     print(index, ":", value)



####################################################################################
# write a program to print the element and it's corresponding index only if the element has even length charachters

# l1 = ['apple', 'google', 'flipkart', 'walmart', 'amazon']
#
# for index, item in enumerate(l1):
#     if len(item) % 2 == 0:
#         print(index, ":", item)



####################################################################################
# write a program to print which are starting with vowel

# l1 = ['apple', 'google', 'flipkart', 'walmart', 'amazon']
# vowel = 'aeiou'
# for i in l1:
#     if i[0].lower() in vowel:
#         print(i)


####################################################################################
# reversing the each word

# s = "hi friends welcome"
# temp = s.split()
# l1 = []
# s1 = ""
# for i in temp:
#     l1.append(i[::-1])
#     s1 = " ".join(l1)
# print(s1)



####################################################################################
# write a program to print only the palindromes from the list
#
# l1 = ['apple', 'mom', 'flipkart', 'dad', 'amazon']
#
# for i in l1:
#     temp = i[::-1]
#     if i == temp:
#         print(i)



####################################################################################
# write a program to create a list of elements such that if the element is of even length store it as it is if it is not then reverse it and store

# l1 = ['apple', 'mom', 'flipkart', 'dad', 'amazon']
# l2 = []
# for i in l1:
#     if len(i) % 2 != 0:
#         l2.append(i)
#     else:
#         l2.append(i[::-1])
# print(l2)
#
#

####################################################################################
# write a program to print only the integers in the given list

# l1 = ['apple', 10, 'flipkart', 20, 'amazon']
#
# for i in l1:
#     if isinstance(i, int):
#         print(i)


####################################################################################
# write a program to print the values other than strings in the given list
#
# l1 = ['apple', 10, 'flipkart', [1, 2, 3], 1.25]
# for i in l1:
#     if not isinstance(i, str):
#         print(i)


####################################################################################
# write a program to print only the extension in the given list

# l1 = ['facebook.com', 'gmail.txt', 'yahoo.pdf']
#
# for i in l1:
#     temp = i.split(".")
#     print(temp[1])

# using unpacking

# for i in l1:
#     filename, ext = i.split('.')
#     print(ext)



#####################################################################################
# write a program to build list of tuples with element and its length pair

# l1 = ['facebook.com', 'gmail.txt', 'yahoo.pdf']
# l2 = []

# for i in l1:
#     l2.append(len(i))
# print(list(zip(l1, l2)))
#
# for i in l1:
#     l2.append((i, len(i)))
# print(l2)



#####################################################################################

# s = input("Enter your mail id: ")
# username = ""
#
# temp = s.split('@')
#
# for i in temp[0]:
#     if i.isalpha():
#         username += i
# d = temp[1]
# temp1 = d.split('.')
# ext = temp1[-1]
# application = temp1[0]
# print(f' Username : {username} \n Extenstion : {ext} \n application : {application}')