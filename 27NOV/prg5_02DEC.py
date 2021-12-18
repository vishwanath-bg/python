# functions

#######################################################################

# s = "hello"
# count = 0
# for i in s:
#     count += 1
# print(count)
#######################################################################
# s = "hello world"
# l = [1, 2, 3, 4, 5, 6, 7]


# def iterable_length(x):   # parameters or formal arguments
#     count1 = 0
#     for i in x:
#         count1 += 1
#     print(count1)
#
#
# iterable_length(s)   # arguments or actual arguments
# iterable_length(l)   # arguments or actual arguments


#######################################################################

# s = "hello world"
# l = [1, 2, 3, 4, 5, 6, 7]
#
#
# def iterable_length(x):   # parameters or formal arguments
#     count1 = 0
#     for i in x:
#         count1 += 1
#
#     # return count1
#     return 1, 2, 3
#
#
# res = iterable_length(s)   # arguments or actual arguments
# res1 = iterable_length(l)   # arguments or actual arguments
#
# print(res, res1)



################################################################################################################

# positional arguments
# def greet(name, age):
#     print(f"hai {name}, your age is {age}")
#
#
# greet("vishwa", 22)

# keyword arguments
# def greet(name, age):
#     print(f"hai {name}, your age is {age}")
#
#
# greet(age=22, name="vishwa")

# combination


# def greet(name, age):
#     print(f"hai {name}, your age is {age}")
#
#
# greet("john", age=22)
# greet(name="john", 22)  # Syntax  error
# greet("sita", name="john)   # Type error
# greet("sita", age=30)

######################################################################################################################
# keyword and only positional arguments


# def add(a, b, c, /):
#     return a + b + c


# print(add(1, 2, 3))
# print(add(a=1, b=2, c=3))    # Type error

#
# def add(a, /, b, c):
#     return a + b + c
#
#
# print(add(1, b=2, c=3))

# Keyword only argument
# def add(*, a, b, c):
#     return a + b + c


# print(add(a=1, b=2, c=3))
# def add(*, a, b, c):
#     return a + b + c
#
#
# print(add(a=1, b=2, c=3))

# variable number of positional arguments

# def add(*args):
#     print(args)
#     return sum(args)
#
#
# print(add(1, 2, 4, 5))

# variable number of keyword arguments
# def add(**kwargs):
#     return kwargs
#     # return sum(kwargs)
#
#
# print(add(a=1, b=2, c=3))

######################################################################################################################
# x = 10
#
#
# def add(a, b=x):   # default parameter
#     return a + b
#
#
# print(add(1))  # 11
# print(add(1, 7)) # 8

#
# x = 12
#
#
# def add(a, b=x):   # default parameter
#     return a + b
#
#
# x = 10
# print(add(1))  # 13

# NOTE: if a default value is assigned to a parameter at the time of function defination then the changed value will not affect the parameter unless it is passed explictly

########################################################################################################################
# function annotations


# def greet(name: str, age: int) -> str:
#     print(f"hai {name}, your age is {age}")
#
#
# greet("john", 30)
# greet("john", "30")
# greet(20, 30)
#


########################################################################################################################
# write a function to count the number of positional and keyword arguments passed to it

# def length(*args, **kwrgs):
#     return len(args), len(kwrgs)
#
#
# print(length(1, 2, 3, a=10))
########################################################################################################################
# write a function to print message "Hai Everyone" if the user input is not present
# x = "hai everyone"
#
#
# def func(a=x):
#     return a
#
#
# print(func())

########################################################################################################################
# a function takes variable number of positional arguments as input how to check if the arguments that are passed are more than 5

# def iterable_count(*args):
#     if len(args) > 5:
#         print("postional arguments are more than 5")
#
#
# iterable_count(1, 2, 3, 4, 4, 5)


########################################################################################################################
# Recursion

# count = 10
# while count > 0:
#     print(count)
#     count -= 1

# def countdown(count):
#
#     if not count > 0:
#         return
#
#     print(count)
#     countdown(count-1)
#
#
# countdown(10)




########################################################################################################################
# factorial of a  number using while loop and recursion


# i = 5
# fact = 1
#
# while i != 1:
#     fact *= i
#     i -= 1
# print(fact)

# def factorial(n, fact):
#
#     if n == 0:
#         return fact
#     fact *= n
#
#     return factorial(n-1, fact)
#
#
# print(factorial(5, 1))

# def factorial_(n):
#     if n == 1:
#         return 1
#
#     return n*factorial_(n-1)
#
#
# print(factorial_(5))
#

########################################################################################################################
# write a recursion program to calculate sum of first 10 numbers
# i = 1
# count = 10
# sum = 0
#
# while count > 0:
#     sum = sum + i
#     count -= 1
#     i += 1
# print(sum)

# def sum_(x, sum=0):
#     if x == 0:
#         return sum
#     sum += x
#     return (x-1,sum)
#
#
# sum_(5)


########################################################################################################################
# write a recurion program to reverse a string

# s = "string"
# i = len(s)
# n = ""
# while i > 0:
#     n += s[i-1]
#     i -= 1
# print(n)



# def reverse(x, n=""):
#     if i > 0:
#         return n
#
#     n += x[i-1]
#     return reverse(x, i-1, n)
#
#
# print(reverse("hello"))


#####################################################################################################
# 0, 1, 1, 2, 3, 5, 8, 13

# n1 = 0
# n2 = 1
# count = 10
#
# while count > 0:
#     temp = n1 + n2
#     n2 = n1
#     n1 = temp
#     count -= 1
#     print(n1, end=" ")

# def fibinochi(n1, n2, count = 10):
#     if not count > 0:
#         return n1
#     temp = n1 + n2
#     print(temp, end=" ")
#     return fibinochi(temp, n1, count-1)


# fibinochi(0, 1)
# print(fibinochi(0, 1))
####################################################################################################################
#write a recursion program to find numbers of digits in numbers

# num = 8998
# temp = str(num)
# le = len(temp)
# count = 0
# while le > 0:
#     count += 1
#     le -= 1
# print(count)


#
# def digits(num, l2 , count = 0):
#     if not l2 > 0:
#         return count
#     return digits(num, l2-1, count + 1)
#
#
# num = int(input())
# l2 = len(str(num))
# res = digits(num, l2)
# print(res)


#######################################################################################################################


# num = 8998
# n = num
# temp = 0
# count = 0
# while n > 0:
#     rem = n % 10
#     temp += rem * 10
#     n = n // 10
#     count += 1
# print(count)


# def digits(num, count = 0, temp= 0):
#     n = num
#     if not n > 0:
#         return count
#     rem = n % 10
#     temp += rem * 10
#     count += 1
#     return digits(num//10, count, temp)
#
#
# res = digits(8998)
# print(res)

##################################################################################################################

# a = "123456"
# def count(n):
#     if len(n) == 1:
#         return 1
#     else:
#         return count(n[1::]) + 1
# print(count(a))


#######################################################################################################################
# write a program to print Banglore 10 time without using any loops
# c = "banglore"


# def disp(x, n):
#     if not n == 0:
#         return x
#     print(x)
#     disp(x, n-1)
#
#
# print(disp(c, 5))

# print("banglore\n"*5)