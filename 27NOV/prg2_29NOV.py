# write a program to print the statement hello world for 5 times

# s = 'hello'
#
# for _ in range(5):
#     print(s, end=" ")


################################################################

# write a program to print the even numbers from 0 to 10

# for i in range(0, 11, 2):
#     print(i, end=" ")

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=' ')


################################################################

# write a program to print the odd numbers between the range 20 to 40

# for i in range(21, 40, 2):
#     print(i, end=" ")

# for i in range(21, 40):
#     if i % 2 != 0: # if i%2:     if not i%2 ==0
#         print(i, end=' ')


################################################################

# write a program to print the numbers which are divisible by 4 in the range 1 to 50
#
# for i in range(1, 50):
#     if i % 4 == 0:
#         print(i, end=" ")


################################################################

# write a program to which are divisible by 4 and 7 range from 1 to 50

# for i in range(1, 50):
#     if i % 4 == 0 and i % 7 == 0:
#         print(i, end=" ")

################################################################

# write a program to check wheather the number given by the user is prime or not

# n = 11
# flag = 0
# for i in range(2, n):
#     if n % i ==0:
#         flag = 1
#         break
# if flag == 0:
#     print("it is a prime")
# else:
#     print("it's not a prime")

# n = 11
# flag = 0
# for i in range(2, n):
#     if n % i == 0:
#         flag = 1
#         break
#     else:
#         continue #or pass
#
# if flag == 0:
#     print("It is a prime")
# else:
#     print("It's not a prime")

# n = 6
# for i in range(2, n):
#     if n % i == 0:
#         print("it is not a prime")
#         break
# else:
#     print("it is a prime")

# printing prime numbers for given range
# for n in range(2, 50):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=" ")


################################################################

# write a program to print first 10 even numbers
# i = 0
# count = 0
#
# while count < 10:
#     if i % 2 == 0:
#         print(i, end=" ")
#         count += 1
#     i += 1


################################################################

# write a program to print first 10 prime numbers

# n = 2
# count = 0
# while count < 10:
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=" ")
#         count += 1
#     n += 1


################################################################

s = 'hello'
# print("using sequence")
# for i in s:
#     print(i)
# print("using range")
# for i in range(len(s)):
#     print(i, s[i])

# l1 = ['h', 'e', 'l', 'l', 'o']
# print("using sequence")
# for i in l1:
#     print(l1.index(i), i)
# print("using range")
# for i in range(len(l1)):
#     print(i, l1[i])


#############################################################################
# Activity
# Even Numbers
# for i in range(21):
#     if i % 2 == 0:
#         print(i)
# Odd Numbers
# for i in range(21):
#     if i % 2 != 0:
#         print(i)


#############################################################################
# Prime numbers range of 1 to 30
# for i in range(1, 30):
#     for j in range(2, i):
#         if i % 2 == 0:
#             break
#     else:
#         print(i, end=" ")


#############################################################################
# Printing -10 to -1
# for i in range(-10, 0, 1):
#     print(i, end=" ")
# Using While loop
# n = 0
# count = 0
# while count < 10:
#     print(n-10, end=" ")
#     count += 1
#     n += 1


#############################################################################
# ASCII values of string
# s = 'ViShWa'
# for i in range(len(s)):
#     print(s[i], ':', ord(s[i]))


#############################################################################
# s1 = 'hAi goOd mornIng'
# s2 = ""
# for i in range(len(s1)):
#     if s1[i] in 'aeiouAEIOU':
#         s2 += s1[i].swapcase()
#     else:
#         s2 += s1[i]
# print(s2)


#############################################################################
# for i in range(5):
#     print(i, end=" ")
# Using While loop
# count = 0
# n = 0
# while count < 5:
#     print(n, end=" ")
#     count += 1
#     n += 1


#############################################################################
# for i in range(0, 30):
#     if i % 2 ==0:
#         print(i)

# While loop
# n = 0
# while n < 30:
#     print(n)
#     n += 2


#############################################################################
# for i in range(1, 11):
#     print(i, end=" ",)

# for j in range(10, 0, -1):
#     print(j, end=" ")
# Using While loop
# n = 1
# while n <= 10:
#     print(n)
#     n += 1

#############################################################################
# for i in range(10, 0, -2):
#     print(i, end=" ")


#############################################################################
# s = "python is awesome"
# for i in range(5):
#     print(s)
# Using while loop
# s = "python is awesome"
# count = 0
# while count < 5:
#     print(s)
#     count += 1


#############################################################################
# for i in range(-10, 0):
#     print(i, end="")
# for i in range(-1, -11):
#     print(i, end="")


#############################################################################
# for i in range(10, -2, -1):
#     print(i, end=" ")


############################################################################
# l1 = []
# l2 = []
# if l1:
#     for i in range(len(l1)):
#         print(l1[i])
# else:
#     l2.append(1)
#     print(l2)


########################################################################
# i = 0
# count = 0
# sum = 0
#
# while count < 10:
#     if i % 2 == 0:
#         # print(i, end = " ")
#         count += 1
#         sum += i
#     i += 1
# print(sum)



########################################################################
# s1 = "hello welcome to python"
# s2 = ''
# for i in s1:
#     s2 += i.upper()
# print(s2)

# s1 = "HELLO WELCOME TO PYTHON"
# s2 = ''
# for i in s1:
#     s2 += i.lower()
# print(s2)



########################################################################
# l1 = ['hello', 'hi', 10, '12', 12, 19, 6.2]
# l2 = []
# for i in l1:
#     if isinstance(i, (int, float)) or i.isnumeric():
#         l2.append(i)
# print(l2)


##########################################################################
# s1 = 'python selenium'
#
# for i in s1:
#     if i.lower() in 'aeiou':
#         print(i, end=" ")

##########################################################################
# s1 = 'python selenium'
#
# for i in s1:
#     if i.lower() not in 'aeiou ':
#         print(i, end=" ")


##########################################################################
# s1 = "hi"
# s2 = ''
# if s1:
#     for i in range(len(s1)):
#         print(s1[i], end="")
# else:
#     s2 += "hello"
#     print(s2)

################################################################################
# d1 = {'a': 3, 'b': 4}
#
# if d1:
#     print(d1)
# else:
#     d1['a'] = 1
#     print(d1)


################################################################################
# s1 = set()
#
# if s1:
#     print(s)
# else:
#     s1.add('hi')
#     print(s1)


###################################################################################
