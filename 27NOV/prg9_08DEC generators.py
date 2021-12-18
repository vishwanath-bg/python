# write a generator expression to extract name starting with vowel

# s = "hello world welcome a elephant"
# l1 = s.split()
#
# l2 = (item for item in l1 if item[0] in 'aeiouAEIOU')
# print(list(l2))

#############################################################################################
# write a generator expression to extract the names which are of even length

# l1 = ['vishwa', 'ramya', 'vidya', 'badhri', 'roshan', 'dinesh']
#
#
# def names(x):
#     for item in x:
#         if len(item) % 2 == 0:
#             yield item
#
#
# res = names(l1)
# print(list(res))


# l1 = ['vishwa', 'ramya', 'vidya', 'badhri', 'roshan', 'dinesh']
# l2 = (item for item in l1 if len(item) % 2 == 0)
# print(list(l2))

#############################################################################################
# write a generator expression to create a list of names ending with vowels

# l1 = ['vishwa', 'ramya', 'vidya', 'badhri', 'roshan', 'dinesh']
#
#
# def names_(x):
#     for item in x:
#         if item[-1] in 'aeiouAEIOU':
#             yield item
#
#
# res = names_(l1)
# print(next(res))
# print(list(res))


# l2 = (item for item in l1 if item[-1] in 'aeiouAEIOU')
# print(list(l2))

#############################################################################################
# write a generator expression to create a list of tuples of word and it's length pair

# l1 = ['vishwa', 'ramya', 'vidya', 'badhri', 'roshan', 'dinesh']
#
#
# def name_lenpair(x):
#     for item in x:
#         yield (item, len(item))
#
#
# res = name_lenpair(l1)
# print(next(res))
# print(list(res))

# l1 = ['vishwa', 'ramya', 'vidya', 'badhri', 'roshan', 'dinesh']
# l2 = ((item, len(item)) for item in l1)
# print(list(l2))

#############################################################################################
# write a generator  to countdown generator

# def num_():
#     for num in range(1, 11):
#         yield num
#
#
# res = num_()
# print(next(res))
# print(list(res))



# gen = (num for num in range(1, 11))
# print(list(gen))


#############################################################################################
# write a generator expression to yield  the even numbers from 1 to 50

# def even_num():
#     for num in range(1, 51):
#         if num % 2 == 0:
#             yield num
#
#
# res = even_num()
# print(next(res))
# print(list(res))


# even_num = (num for num in range(1, 51) if num % 2 == 0)
# print(list(even_num))



#############################################################################################
# write a generator expression to yield one line at a time from a file

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\file1.txt"
#
# with open(f_path) as f:
#     gen = (line for line in f)
#     print(next(gen))
#     print(next(gen))


# def read_line(file_path):
#     with open(file_path) as f:
#         for l
#         ine in f:
#             yield line
#
#
# res = read_line(f_path)
# print(list(res))



# def spam(func):             # outer function
#     def wrapper():          # inner function
#         print('hello')
#         func()
#     return wrapper
#
# @spam
# def display():
#     print(2+3)
#
# @spam
# def display1():
#     print(2-3)
#
#
# display()
# display1()



#############################################################################################
# write a decorator to print function name before decorate

# def name(func):
#     def wrapper():
#         print(func.__name__)
#     return wrapper
#
# @name
# def add():
#     print("adding")
#
#
# add()


# delay using decorator

# import time
#
#
# def delay(n):
#     def log(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return log
#
#
# @delay(5)
# def add(a, b, c):
#     return a + b + c
#
# @delay(3)
# def sub(a, b):
#     return a - b
#
#
# print(add(1, 2, 3))
# print(sub(2, 3))


#############################################################################################
# write a decorator to how many functions are present in it

# count = 0
# def log(func):
#     def wrapper(*args, **kwargs):
#         global count
#         count += 1
#         res = func(*args, **kwargs)
#         return res
#     return wrapper



# @log
# def add(a, b, c):
#     return a + b + c
#
# @log
# def sub(a, b):
#     return a - b
#
# @log
# def mul(a, b):
#     return a * b
#
#
# print(add(1, 2, 3))
# print(sub(2, 3))
# print('number of function calls', count)



# create a decorator function to count individual function call along with function name in a program

''' using count method '''
# d = {}
# def log(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         res = func(*args, **kwargs)
#         d[func.__name__] = count
#         return res
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# @log
# def sub(a, b):
#     return a - b
#
#
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
# print(sub(1, 2))
# print(sub(1, 2))
# print(sub(1, 2))
# print(d)


''' using dictionary method '''
# d = {}
# def log(func):
#     def wrapper(*args, **kwargs):
#         f_name = func.__name__
#         if f_name not in d:
#             d[f_name] = 1
#         else:
#             d[f_name] += 1
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# @log
# def sub(a, b):
#     return a - b
#
#
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
# print(sub(1, 2))
# print(sub(1, 2))
# print(sub(1, 2))
# print(d)


''' using default dict method '''
# from collections import defaultdict
# d = defaultdict(int)
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         f_name = func.__name__
#         d[f_name] += 1
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# @log
# def sub(a, b):
#     return a - b
#
#
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
# print(add(1, 2))
# print(sub(1, 2))
# print(sub(1, 2))
# print(sub(1, 2))
# print(d)






#######################################################################################################################
# 09/12/2021

# write a program to create a list of cubes for the prime numbers 1 to 20

# n = 11
# l1 = []

# for i in range(2, n):
#     if n % i != 0:
#         l1.append(True)
#     else:
#         l1.append(False)
#
# print(l1)
# print(all(l1))
# print(any(l1))

# prime_num = (True if n % i != 0 else False for i in range(2, n))
# print(list(prime_num))


# using generator function
# def prime_num():
#     for num in range(1, 21):
#         if num > 1 and all([num % i != 0 for i in range(2, num)]):
#             yield num ** 3
#
#
# print(list(prime_num()))

# using generator expression

# prime = (num ** 2 for num in range(1, 21) if num > 1 and all([num % i != 0 for i in range(2, num)]))
# print(list(prime))

##################################################################################################################
# DECORATORS

# def f_name(func):
#     def wrapper():
#         print(func.__name__)
#         print("decorator")
#         func()
#         return wrapper
#
#
#
# @f_name
# def add():
#     print( 1 + 2 )
#
# @f_name
# def sub():
#     print( 1 - 2 )
#
# add()
# sub()

##########################################################################################################
# write a decorator to reverse a string


# def reverse_(f):
#     def wrapper(*args, **kwargs):
#         res = f(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
#
# @reverse_             # retrun_string = reverse_(return_string)
# def return_string(string):
#     return string
#
#
# print(return_string("hello"))



##########################################################################################################
# write a decorator that counts the number of arguments given to main function

# def count_arg(f):
#     def wrapper(*args, **kwargs):
#         num = len(args) + len(kwargs)
#         print("number of arguments", num)
#         res = f(*args, **kwargs)
#         return res
#     return wrapper
#
#
# @count_arg
# def function(a, b, c, d):
#     return a + b + c + d
#
# print(function(1, 2, 3, 4 ))


##########################################################################################################
# write a decorator function which checks if the given parameters are integer type


# def check_value(f):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if not isinstance(i, int):
#                 break
#         else:
#             print("integer argument")
#             res = f(*args, **kwargs)
#         # for i in kwargs:
#         #     if isinstance(kwargs, int):
#         #         print("integer argument")
#             return res
#     return wrapper
#
#
# @check_value
# def function(a, b):
#     return a + b
#
#
# print(function(2, 4))


##########################################################################################################
# number of time each function to execute


# def n_time(n):
#     def f_name(f):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 print(f(*args, **kwargs))
#         return wrapper
#     return f_name
#
#
# @n_time(3)
# def add(a, b):
#     return a + b
#
#
# @n_time(2)
# def sub(a, b):
#     return a - b
#
#
# add(4, 3)
# sub(4, 3)



##########################################################################################################
# write a decorator function to validate type of arguments given to the main function with the user input datatypes

# def type_check(*args1):
#     def f_name(f):
#         def wrapper(*args, **kwargs):
#             res = f(*args, **kwargs)
#             for i, j in zip(args, args1):
#                 if not isinstance(i, j):
#                     print("datatpyes not matched")
#                     return res
#             else:
#                 print("datatypes are matched")
#                 return res
#         return wrapper
#     return f_name
#
#
# @type_check(int, str)
# def disp_value(a, b):
#     print(a, b)
#
#
# @type_check(str)
# def disp_2(c):
#     print(c)
#
# @type_check(str, int, str)
# def disp_3(a, b, c):
#     print(a, b, c)
#
#
# disp_value(1, 2)
# disp_2('hello')
# disp_3('h', '8', 'l')


#############################################################################################################
class a:
    """printing some message"""
    def __init__(self):
        pass
    def display(self):
        print("hello welcome to python")


print(a.__doc__)
