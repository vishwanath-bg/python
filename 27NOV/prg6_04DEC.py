# write a program to create a list of duplicate characters
# s = "hello world"
# l1 = []
# for i in set(s):
#     if s.count(i) > 1:
#         l1.append(i)
#
# print(l1)

# l1 = [i for i in set(s) if s.count(i) > 1]
# print(l1)

###############################################################################
# write a program to create a list of non duplicate characters

# s = "hello world"
# l1 = []
# for i in set(s):
#     if not s.count(i) > 1:
#         l1.append(i)
# print(l1)

# l1 = [i for i in set(s) if not s.count(i) > 1]
# print(l1)

###############################################################################################
# write a program to create a dict of word and character pair only if the last character is vowel

# s = "hai hello how are you"
# l1 = s.split()
#
# l2 = {i: i[-1] for i in l1 if i[-1] in 'aeiouAEIOU'}
# print(l2)


###############################################################################################
# write a program to remove duplicate from string
#
# s = "helloohhhhhho"
# s1 = ""
# for i in s:
#     if i not in s1:
#         s1 += i
# print(s1)

# s = "helloohhhhhho"
# s1 = set(s)
# print("".join(s1))


###############################################################################################
# write a program to replace duplicate character by "_"

# s = "hello world"
# s1 = ""
#
# for i in s:
#     if s.count(i) > 1:
#         s1 = s1 + "_"
#     else:
#         s1 += i
#
# print(s1)

###############################################################################################
# write a function to print length of any iterables without using any builtin functions


# def len_iterable(x):
#     count = 0
#     for _ in x:
#         count += 1
#     return count
#
#
# i = [1, 2, 3, 4, 5, 6]
# print(len_iterable(i))


###############################################################################################
# write a program to reverse a string without using any any inbuilt function

# s = "hello world"
# s1 = ""
# for i in s:
#     s1 = i + s1
# print(s1)

# s = "hello world"


# def reverse_str(x):
#     s = ""
#     for i in x:
#         s = i + s
#     return s
#
#
# print(reverse_str("hello"))





###############################################################################################
# write a program to convert a string to  a list vice versa

# string to list
# s = "hello world"
# l1 = s.split()
# print(l1)
#

# without using builtin function
# s = "hello world"
# l1 = []
# for i in s:
#     l1.append(i)
# print(l1)

# list to string

# s = "hello world"
# l1 = s.split()
# s1 = "".join(l1)
# print(s1)

# without using builtin function
# l = ['h', 'e', 'l', 'l', 'o']
# s1 = ""
# for i in l:
#     s1 += i
# print(s1)


###############################################################################################
# write a program to "," separated words in the string

# s = "hello welcome to python"
# l = s.split()
# s1 = ",".join(l)
# print(s1)

# print(s.replace(" ", ","))

###############################################################################################
# write a program to create a dictionary to create a character and ascii value

# s = "hello world"
#
# d = {i: ord(i) for i in s}
# print(d)

# def dict1(n):
#     d = {}
#     for char in n:
#         d[char] = ord(char)
#     return d
#
# print(dict1("hai"))


###############################################################################################
# write a function to convert upper case string to lower case or vice versa without inbuilt methods


# def case_conversion(x):
#     s1 = ''
#     for i in x:
#         if ord(i) > ord('a') and ord(i) < ord('z'):
#             temp = ord(i) - 32
#             s1 += chr(temp)
#         elif ord(i) > ord('A') and ord(i) < ord('Z'):
#             temp = ord(i) + 32
#             s1 += chr(temp)
#         else:
#             s1 += i
#     return s1
#
#
# print(case_conversion("hEllO9"))



###############################################################################################
# write a function to check given string is palindrome or not

# def palindrome_str(x):
#     x = x.lower()
#     if x == x[::-1]:
#         return 'palindrome'
#     return "not palindrome"
#
#
# print(palindrome_str("Malayalam"))


###############################################################################################
# write a program to search for a character and return it's corresponding index

# s = "hello"
#
#
# def search_ch(x, y):
#     for index, char in enumerate(x):
#         if y in char:
#             print(index, char)
#
#
# search_ch(s, "l")


#################################################################################################
# write a function it takes list of strings if the item is string it should print as it is if the item is type of int or float it should reverse it

# l1 = ["apple", "yahoo", "1234", 100, 123.76, "26.23"]
# l2 = []
#
# l1 = ["apple", "yahoo", "1234", 100, 123.76, "26.23"]
# l2 = []
#
#
# def disp(x):
#     for i in x:
#         if isinstance(i, int):
#             l2.append(int(str(i)[::-1]))
#         elif isinstance(i, float):
#             l2.append(float(str(i)[::-1]))
#         else:
#             l2.append(i)
#     return l2
#
#
# print(disp(l1))

#################################################################################################
# write a program to print below output
# s = 'hi how are you'
# o/p1 = "ih woh era uoy "
# o/p2 = "uoy era woh ih"


# s = 'hi how are you'
# print(s[::-1])

# s = 'hi how are you'
# l = s.split()
# s1 = []
# for i in l:
#     print(i[::-1], end=" ")

# for i in l:
#     s1.append(i[::-1])
# print(" ".join(s1))


#################################################################################################
# write a program to reverse values in dictionary if the value is of type string

# d = {'a': "hello", 'b': 100, 'c': 10.1, 'd': 'world'}
#
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
# print(d)


#################################################################################################
# write a program to count number of words in a sentence

# s = "hi hello every one"
# l = s.split()
#
# print(f"number of word in sentence is {len(l)}")


#################################################################################################
# write a program to get the output
# t = ('1', '2', '3', '4')
# o/p: 1234

# t = ('1', '2', '3', '4')
#
# for i in t:
#     print(i, end="")

# t = ('1', '2', '3', '4')
# print("".join(t))

#################################################################################################
# write a program to find longest word in the sentence

# s = "hello world good morning"
# l = s.split()
# l.sort(key=len)
# print(l[-1])

# s = "hello world good morning"
# l = s.split()
# word = max(l, key=len)
# print(word)

# s = "hello world good morning"
# l = s.split()
# max_word = ""
# for i in l:
#     if len(i) > len(max_word):
#         max_word = i
#
# print(max_word)


#################################################################################################
# create a dictionary of word and it's length pair in a sentence and find least word in the dictionary

# s = "hello world welcome to python"
# l = s.split()
# d = {}
#
# for i in l:
#     d[i] = len(i)
# s1 = min(d.items(), key=lambda item: item[-1])
#
# print(s1)
# print(d)



