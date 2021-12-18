# write a lambda function to find a square of any number

# square = lambda a: a ** 2
# print(square(5))

######################################################################
# write a lambda function to find a cube of any number

# square = lambda a: a ** 3
# print(square(5))


######################################################################
# write a lambda function to get last element of iterable

# iterable = lambda s: s[-1]
# print(iterable('hello'))


######################################################################
# output of the expression a^2 + b^2 + 2ab

# output = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
# print(output(3, 4))



######################################################################
# write a lambda function to check wheather given number is even or odd

# num = lambda a: a % 2 == 0
# print(num(3))

# num = lambda a: "even" if a % 2 == 0 else "odd"
# print(num(3))


######################################################################
# write a lambda function to check if the given string is palindrome or not

# palindrome = lambda string: "string is palindrome" if string.lower() == string.lower()[::-1] else "string is not palindrome"
# print(palindrome("MalayalaM"))


######################################################################
# l1 = ["hello", "malayalam", "mom", "dad"]
#
# l2 = list(map(lambda string: "string is palindrome" if string.lower() == string.lower()[::-1] else "string is not palindrome", l1))
# print(l2)

# list_ = [2, 4, 56, 76, 89, 76, 67]
# even = list(map(lambda num: "even" if num % 2 == 0 else "odd", list_))
# print(even)



############################################################################
# write a program to sqaure and cube of every number in given list  of integer using map

# square
# l1 = [1, 2, 3, 4, 5]
#
# l2 = list(map(lambda num: num ** 2, l1))
# print(l2)

# cube
# l1 = [1, 2, 3, 4, 5]
#
# l2 = list(map(lambda num: num ** 3, l1))
# print(l2)


############################################################################
# write a python program to return the list of elements raised to the power of the indices using map

# l1 = [1, 2, 3, 4, 5]

# l2 = list(map(lambda num: num ** l1.index(num), l1))
# print(l2)

# l2 = list(map(lambda num: num[1] ** num[0], enumerate(l1)))
# print(l2)


############################################################################
# write a python program to convert negative number in the list into positive numbers
#
# l1 = [1, -2, 3, -4, -5]
#
# l2 = list(map(lambda num: abs(num), l1))
# print(l2)

############################################################################
# write a map function to add elements in the both the list

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8, 9]

# l3 = list(map(lambda num: num[0] + num[1], zip(l1, l2)))
# print(l3)
#
# l3 = list(map(lambda a, b: a + b, l1, l2))
# print(l3)



###############################################################################
# write a program to filter out only even numbers from the list

# l1 = [i for i in range(1, 20)]
# using map we can't filter the numbers it will give both true and false
# l2 = list(map(lambda num: num if num % 2 == 0 else , l1)
# print(l2)

# l1 = [i for i in range(1, 20)]
# l2 = list(filter(lambda num: not num % 2, l1))
# print(l2)
#

###############################################################################
# build a list with only even length string using filter function
# s = "hello good morning everyone welcome to python"
# l1 = s.split()
# l2 = list(filter(lambda str_: len(str_) % 2 == 0, l1))
# print(l2)


###########################################################################
# write a program to return the string if string is starting with vowel

# s = "hello good morning everyone welcome to python"
# l1 = s.split()
# l2 = list(filter(lambda str_: str_[0] in "aeiouAEIOU", l1))
# print(l2)


##############################################################################
# write a program to extract only the negative number from the list

# l1 = [i for i in range(5, -10, -1)]
# l2 = list(filter(lambda num: num < 0, l1))
# print(l2)



##############################################################################
# write a program to print prime number from 1 to 50 using filter

# def prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % 2 == 0:
#                 return 0
#         else:
#             return 1
#

# prime_num = list(filter(prime, range(50)))
# print(prime_num)



##############################################################################
# write a program to calculate sum positive and negative numbers in the given list

# l1 = [i for i in range(10, -10, -1)]
# l2 = sum(list(filter(lambda n: n < 0, l1)))
# l3 = sum(list(filter(lambda n: n > 0, l1)))
# print(l2)
# print(l3)
#
# def sum_pos(x):
#     sum = 0
#     if x > 0:
#         sum += x
#         return 1
#
#     else:
#         return 0

# def sum_neg(x):
#     sum = 0
#     if x < 0:
#         sum += x
#         return 1
#     else:
#         return 0
#
# l2 = list(filter(sum_pos, l1))
# print(sum(l2))
#
# l3 = list(filter(sum_neg, l1))
# print(sum(l3))




##############################################################################
# write a function to search for a charachter in the given string and return it's corresponding index if character is duplicated return it's first occurance index
# s = "hello world"

# using builtin method
# def find_chr(x):
#     if s.find(x) >= 0:
#         # print(s.find(x))
#         return s.find(x)
#     else:
#         return 'charchter is not present'
#
#
# print(find_chr("z"))


# def find_chr(x):
#     if x in s:
#         return s.index(x)
#
#
# print(find_chr("l"))

# without using inbuilt method
# def find_chr(x, c):
#     for index, item in enumerate(s):
#         if c == item:
#             return index
#
#
# print(find_chr(s, "l"))



########################################################################################################################
# write a program to search for a character in the given string and return corresponding index if the character is duplicated return all the indices

# s = "hello world"
# def search_chr(x, c):
#     for index, item in enumerate(s):
#         if item == c:
#             print(index, item)
#         if s.find(c) > 1:
#             print(index, item)
#
#
# search_chr(s, "l")


# s = "hello world"
# def search_chr(x, c):
#     for index, item in enumerate(s):
#         if item == c:
#             print(index, item)
#
#
#
# search_chr(s, "l")



##############################################################################
# l1 = [0, 1]
# l2 = [l1.append(l1[-2] + l1[-1]) for i in range(20)]
# print(l1)
##############################################################################
# write a function to print the below output
# func("TRACXN", 0)   should print RCN
# func("TRACXN", 1)   should print TAX



# s = "TRACXN"
#
#
# def disp(x, n):
#     if n == 0:
#         return x[1::2]
#     elif n == 1:
#         return x[::2]
#
#
# print(disp(s, 1))

########################################################################################################################
# write a  function that returns the last digit of an integer
#
# n = 1234
# #
# #
# def last_digit(x):
#     return str(x)[-1]
#     # return x % 10
#
#
# print(last_digit(n))



########################################################################################################################
