# num = int(input('Enter a number: '))
#
# if num % 2 == 0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')
# # print(f'{num} is even' if num % 2 == 0 else f'{num} is odd')
# ###########################################################################
# palindrome(string)

# s = input('Enter a string: ').lower()
# temp = s[::-1]
#
# if s == temp:
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} is not palindrome')
#
# # print(f'{s} is palindrome' if s == temp else f'{s} is not palindrome')
#################################################################################
# palindrome(integer)
# n = int(input('Enter a number: '))
#
# if str(n) == str(n)[::-1]:
#     print(f'{n} is palindrome')
# else:
#     print(f'{n} is not palindrome')
## print(f'{n} is palindrome') if str(n) == str(n)[::-1] else print(f'{n} is not palindrome')
###################################################################################
# Leap year
# import calendar
# year = int(input('Enter a year:'))
#
# if year % 4 == 0 and year % 100 != 0: # non century years
#     print(f'{year} is leap year')
# elif year % 400 == 0:   # century years
#     print(f'{year} is leap year')
# else:
#     print(f'{year} is not leap year')
#
# print(calendar.isleap(2100))
###################################################################################
# perfect square
# import math
# n = int(input('Enter a number: '))
# a = math.trunc(n ** 0.5)
# # a = sqrt(n)
# if a * a == n:
#     print('perfect square')
# else:
#     print('not perfect square')
## print('perfect square') if a * a == n else print('not perfect square')
###################################################################################
# s = input('Enter a character: ').lower()
#
# # if s.isalpha():
# #     print('character is alphabet')
# # elif s.isnumeric():
# #     print('character is number')
# # else:
# #     print('character is special character')
# #
# if ord('a') >= ord(s) <= ord('z'):
#     print("character is alphabet")
# elif ord('0') >= ord(s) <= ord('9'):
#     print("character is numbers")
# else:
#     print("character is special character")
##########################################################################################
# m = int(input('Enter a marks:'))
#
# if m > 60:
#     print("First class")
# if 60 < m and m > 35:
#     print('Second class')
# if m < 35:
#     print('Fail')
##############################################################################################
# c = input("Enter a string: ").lower()
#
# if ord(c[0]) == ord('a') or ord(c[0]) == ord('e') or ord(c[0]) == ord('i') or ord(c[0]) == ord('o') or ord(c[0]) == ord('u'):
#     print(f"{c}'s first character is vowel")
# else:
#     print(f"{c}'s first character is not vowel")

# if c[0] in 'aeiou':
#     print(f"{c}'s first character is vowel")
# else:
#     print(f"{c}'s first character is vowel")

#######################################################################################################################

# c = input("Enter a string: ").lower()
#
# # if ord(c[-1]) == ord('a') or ord(c[-1]) == ord('e') or ord(c[-1]) == ord('i') or ord(c[-1]) == ord('o') or ord(c[-1]) == ord('u'):
# #     print(f"{c}'s last character is vowel")
# # else:
# #     print(f"{c}'s last character is not vowel")
#
# if c[-1] in 'aeiou':
#     print(f"{c}'s first character is vowel")
# else:
#     print(f"{c}'s first character is vowel")
####################################################################################
# check if the list has even number of elements

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
#
# if len(l1) % 2 == 0:
#     print('list having even number of elements')
# else:
#     print("list having odd number of elements")
####################################################################################
# n = 2345
# temp = int(str(n)[0])
#
# # if temp % 2 == 0:
# #     print("even")
# # else:
# #     print("odd")
#
# print("1st digit is even" if temp % 2 == 0 else "1st digit is odd")
####################################################################################
# n = 2345
# temp = int(str(n)[-2])
#
# # if temp % 2 != 0:
# #     print("odd")
# # else:
# #     print("not odd")
#
# print("2nd digit is odd" if temp % 2 != 0 else "2nd digit is not odd")
####################################################################################
# d = {'a': 1, 'b': 2, 'c': 3}
#
# if len(d) % 2 != 0:
#     d['d'] = 4
# print(d)
#

