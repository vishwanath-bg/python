# sorting

# s = {"a", "b", "e", "c"}
# a = sorted(s)
# print("".join(a))
#
# s1 = ["a", "c", "e", "h", "g"]
# b = sorted(s1)
# print("".join(b))
#
# s2 = "hello world"
# c = sorted(s2)
# print("".join(c))
#
# s3 = ('1', '2', '5', '6', '4')
# d = sorted(s3)
# print("".join(d))
#
# s4 = {'a': 1, "b": 2, "d": 5, "c": 4}
# e = sorted(s4)
# print("".join(e))

########################################################################################################################
# write a program to sort list based on length of each name

# l = ["vidya", "arun", "dinesh", "mahesh", "sachin", "prajwal"]
# print(sorted(l, key=len))


########################################################################################################################
# write a program to sort list based on last character of the name
# l = ["vidya", "arun", "dinesh", "mahesh", "sachin", "prajwal"]
#
# def last_char(char):
#     return char[-1]
# print(sorted(l, key=last_char))

# using lambda function
# l = ["vidya", "arun", "dinesh", "mahesh", "sachin", "prajwal"]
# print(sorted(l, key=lambda item: item[-1]))


########################################################################################################################
# write a program to sort based on middle character of each element

# l1 = ("vidya", "arun", "dinesh", "mahesh", "sachin", "prajwal")
# res = sorted(l1, key=lambda item: item[len(item) // 2])
# print(res)


########################################################################################################################
# sorting dictionaries
# d = {"apple": 5, "google": 6, "walmart": 3, "flipkart": 7}

# sorting keys based on first character
# res = sorted(d)
# print(res)
#
# res1 = sorted(d.keys())
# print(res1)
#
# res2 = sorted(d.values())
# print(res2)
#
# res3 = sorted(d.items())
# print(dict(res3))


# sorting the dictionaries based on key's last character
# d = {"apple": 5,  "walmart": 3, "flipkart": 7, "google": 6}

# op1
# print(sorted(d, key=lambda key: key[-1]))

# op2
# print(sorted(d.keys(), key=lambda key: key[-1]))

# op3 for getting dictionary back
# print(sorted(d.items(), key=lambda key: key[0][-1]))


# sorting values in dictionary

# d = {"apple": 5,  "walmart": 3, "flipkart": 7, "google": 6}
#
# res = sorted(d.values())
# print(res)
#
# res1 = sorted(d.items(), key=lambda item: item[1])
# print(res1)

########################################################################################################################
# sort the below list based on the last character of each element

# items = ['bv', 'aw', 'dt', 'cu']
# res = sorted(items, key=lambda item: item[-1])
# print(res)


########################################################################################################################
# sort the below list based on temperature

# temp = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
# print(sorted(temp, key=lambda item: item[-1]))
#
# temp = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
# min_, *rest, max_ = sorted(temp, key=lambda item: item[-1])
# print(f'Least temperature in {min_}')
# print(f"Maximum temperature in {max_}")


########################################################################################################################
# sort based on the first value of the inner list

# items = [[2, 7], [7, 3], [3, 8], [8, 7], [4, 9]]
# print(sorted(items))

########################################################################################################################
# sort the below list based on share prices and print maximum share price with its

# prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
#
# *rest, max_ = sorted(prices.items(), key=lambda value: value[-1])
# print(max_)


########################################################################################################################
# write a program to get the most repeated word in the sentence

# s = 'hi how are you how is your health'
# l1 = s.split()
# d = {}
# for i in l1:
#      d[i] = l1.count(i)
#
# *res, max_ = sorted(d.items(), key=lambda item: item[-1])
# print(max_)


########################################################################################################################
# write a program to find the longest word along with it's length

# s = "python is a programming language and programming is fun"
# l1 = s.split()
# d = {}
#
# for i in l1:
#     d[i] = len(i)
# *res, longest = sorted(d.items(), key=lambda item: item[-1])
# print(longest)


########################################################################################################################
# write a program to find the longest word along with it's length which is not repeated


# s = "python is a programming language and programming is fun"
# l1 = s.split()
# d = {}
#
# for i in l1:
#     if l1.count(i) == 1:
#         d[i] = len(i)
# *res, longest = sorted(d.items(), key=lambda item: item[-1])
# print(longest)


########################################################################################################################
# sorting a list of dictionary based on names

# students = [
#     {"name": 'vishwa', "grade": "A", "age": 22},
#     {"name": 'akash', "grade": "B", "age": 27},
#     {"name": 'hemanth', "grade": "C", "age": 21}
# ]
#
# print(sorted(students, key=lambda item: item["name"]))


########################################################################################################################
# sorting a list of dictionary based on age

# students = [
#     {"name": 'vishwa', "grade": "A", "age": 22},
#     {"name": 'akash', "grade": "B", "age": 27},
#     {"name": 'hemanth', "grade": "C", "age": 21}
# ]
#
# print(sorted(students, key=lambda item: item["age"]))


########################################################################################################################
# file handling

# without context manager

# f = open('file1.txt', "w")
# print(f.write("hello world"))
# print(f.closed)
# f.close()
# print(f.closed)

# with context manager

# with open('file1.txt') as f:
#     print(f.closed)
# print(f.closed)


########################################################################################################################
# f = "file1.txt"
#
# with open(f, "r+") as fi:
#     print(fi.writable())
#     print(fi.readable())




########################################################################################################################
'''                                  reading from a file                                       '''

# f = "file1.txt"
# #
# with open(f, "r") as fi:
#     # print(fi.writable())
#     # print(fi.readable())
#     print(fi.read())
#
# with open(f, "r") as fi:
#     # fi.seek(6)
#     fi.seekable()
#     print(fi.readline())
#
# with open(f, "r") as fi:
#     fi.seek(12)
#     print(fi.readlines())

# with open(f, "r") as fi:
#     for line in fi:
#         print(line)



# f = "file1.txt"
# #
# with open(f, "r") as fi:
#     # print(fi.writable())
#     # print(fi.readable())
#     print(fi.read(4))

# with open(f, "r") as fi:
#     # fi.seek(6)
#     fi.seekable()
#     print(fi.readline(3)
#
# with open(f, "r") as fi:
#     fi.seek(0)
#     print(fi.readlines(6))

'''  readlines() read the entire sentence if the specified integer is in between the length of the line. if it exceeds 
the length then the next line will be printed '''

# with open(f, "r") as fi:
#     for line in fi:
#         print(line)

######################################################################################################################
''' write mode '''

# with open("file1.txt", "w") as f:
#     print(f.write("hello\n"))
#     f.writelines(['hello\n', "how\n", "are\n"])


######################################################################################################################
# write a program to count number of words in a file

# with open("file1.txt") as f:
#     count = 0
#     for line in f:
#         a = line.split()
#         # print(a)
#         count += len(a)
#         # print(count)
#     print(count)



######################################################################################################################
# count the lines present in a file

# with open("file1.txt") as f:
#     count = 0
#     for line in f:
#         count += 1
#     print(count)


######################################################################################################################
# write a program to read the lines along with a line number

# with open("file1.txt") as f:
#     for num, line in enumerate(f, start=1):
#         if line.strip():
#             print(num, line)

# with open("file1.txt") as f:
#     count = 0
#     for line in f:
#         if line.strip():    # checks for empty lines
#             count += 1
#     print(count)


######################################################################################################################
# write a program to read the file in reversed order

# with open("file1.txt") as f:
#     for lines in reversed(list(f)):
#         print(lines)



######################################################################################################################
# write a program to read 10 characters at a time
#
# with open('file1.txt') as f:
#     for line in f:
#          print(f.read(10))


######################################################################################################################
# write a program to find the number of characters in each line

# with open('files/file1.txt') as f:
#     for i in f:
#         count = 0
#         for j in i:
#             count += 1
#         print(count)



######################################################################################################################
# write a program to extract IP addresses from access-log.txt file

# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\access-log.txt'
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             print(a[0])


######################################################################################################################
# write a program to extract unique IP addresses from access-log.txt file

# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\access-log.txt'
# with open(f_path) as f:
#     l1 = []
#     for line in f:
#         if line.strip():
#              a = line.split()
#              l1.append(a[0])
#
# print(set(l1))


######################################################################################################################
# create a dictionary of IP address and it's count pair

# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\access-log.txt'
# with open(f_path) as f:
#     d = {}
#     l1 = []
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[0])
#             d[a[0]] = l1.count(a[0])
#     print(d)


###############################################################################################
# extract date time and timezone form the access-log.txt file and create a dictionary of it's with count pair
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\access-log.txt'
# with open(f_path) as f:
#     l1 = []
#     d1 = {}
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[3] + a[4])
#             # l1.append(a)
#             d1[a[3] + a[4]] = l1.count(a[3] + a[4])
#     print(d1)



######################################################################################################################
# in the above dictionary print the most occured and least occured IP address

# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\access-log.txt'
# with open(f_path) as f:
#     d = {}
#     l1 = []
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[0])
#             d[a[0]] = l1.count(a[0])
#     least_IP, *res, most_IP = sorted(d.items(), key=lambda value: value[-1])
#     print(least_IP)
#     print(most_IP)


######################################################################################################################
# write a program to count the number of occurances of IP address in the access log file using default dict and also without using count method

# from collections import defaultdict
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\access-log.txt'
# with open(f_path) as f:
#     l1 = []
#     d = defaultdict(int)
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[0])
#             d[a[0]] += 1
#     print(d)


######################################################################################################################
# write  a program to extract the messages from sample.log file

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.log"
#
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#         print(a[2])



######################################################################################################################
# write a program to print the most occuring and least occuring message in the log file( use count method , default dict, without using default dict)

'''using count method'''

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.log"
# with open(f_path) as f:
#     l1 = []
#     d = {}
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[2])
#             d[a[2]] = l1.count(a[2])
#     least_occ, *res, most_occ = sorted(d.items(), key=lambda value: value[-1])
#     print(d)
#     print(most_occ)
#     print(least_occ)

''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''
'''without using default dict and count method'''

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.log"
# with open(f_path) as f:
#     l1 = []
#     d = {}
#
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[2])
#             if a[2] not in d:
#                 d[a[2]] = 1
#             else:
#                 d[a[2]] += 1
#     least_occ, *res, most_occ = sorted(d.items(), key=lambda item: item[-1])
#     print(d)
#     print(least_occ)
#     print(most_occ)

''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''
'''using default dict'''

# from collections import defaultdict
# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.log"
# with open(f_path) as f:
#     l1 = []
#     d = defaultdict(int)
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l1.append(a[2])
#             d[a[2]] += 1
#     least_occ, *res, most_occ = sorted(d.items(), key=lambda value: value[-1])
#     print(d)
#     print(least_occ)
#     print(most_occ)




#####################################################################################################################
#
