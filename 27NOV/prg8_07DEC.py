#############################################################################################
# 07/12/2021
#############################################################################################
# to get a messages from sample.log file

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.log"
# with open(f_path) as f:
#     l1 = []
#
#     for line in f:
#         if line.strip():
#             a = line.split(" :")
#             l1.append(a)
#         print(a[1].strip('.'))


# from collections import Counter
# s = "hello world"
# print(Counter(s))


#################################################################################################################
# write a program to count number of spaces in sample.txt file

'''using counter'''
# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.txt"
#
# with open(f_path) as f:
#     count_ = 0
#     for line in f:
#         if line.strip():
#             count_ += line.count(" ")
#     print(count_)


'''without using counter'''
# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.txt"
#
# with open(f_path) as f:
#     count_ = 0
#     for line in f:
#         if line.strip():
#             for i in line:
#                 if i == " ":
#                     count_ += 1
#     print(count_)

'''using Counter'''
# from collections import Counter, defaultdict
# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.txt"
# with open(f_path) as f:
#     d = defaultdict(int)
#     for line in f:
#         if line.strip():
#             for i in line:
#                 if i == " ":
#                     d[i] += 1
#     print(d.values())

''' using Counter method from collections'''
# from collections import Counter
# with open(f_path) as f:
#     d = Counter()
#     for line in f:
#         if line.strip():
#             d += Counter(line)
#     print(d)



##########################################################################################
# write a program to get country names from football.txt file

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\football.txt"
# with open(f_path, encoding='UTF-8') as f:
#     for line in f:
#         if line.strip():
#             a = line.split("\t")
#             print(a[1])

##########################################################################################
# write a program to print most occuring country name along with counts

# from collections import Counter
# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\football.txt"
# with open(f_path, encoding='UTF-8') as f:
#     l1 = []
#     for line in f:
#         if line.strip():
#             a = line.split("\t")
#             l1.append(a[1])
#             count_ = Counter(l1)
#     print(count_.most_common())

##########################################################################################
# write a program to find the line number of a particular word in a file

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.txt"
# s = "python"
# with open(f_path) as f:
#     for line_no, line in enumerate(f, start=1):
#         if s in line:
#             print(line_no, line)

##########################################################################################
# ASSINGMENT
# write a program to copy the content of one file to another file

''' using readlines and writelines'''

# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\content1.txt'
# f1 = open(f_path)
# c = ''
# for line in f1:
#     f1.seek(0)
#     c = f1.readlines()
#
# with open("content2.txt", 'w') as f2:
#     f2.writelines(c)


''' using list method'''

# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\content1.txt'
# f1 = open(f_path)
# a = []
# for line in f1:
#     a.append(line)
# with open("content2.txt", 'w') as f2:
#     f2.writelines(a)
# f1.close()



##########################################################################################
# write a program to write data into one file an copy the same into another file in the same program

with open('file1.txt', 'w+') as f1:
    f1.writelines(['hello\n', 'how\n', 'are\n', 'you\n', 'are\n'])
    f1.seek(0)
    a = f1.read()
f2 = open('file2.txt', 'w')
f2.writelines(a)


##########################################################################################
# Reading CSV files

# import csv
# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.csv"

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.csv"
# with open(f_path) as f:
#     reader_obj = csv.reader(f)
#     for line in reader_obj:
#         print(line)

# f_path = r"C:\Users\admin\PycharmProjects\python\27NOV\files\sample.csv"
# with open(f_path) as f:
#     reader_obj = csv.DictReader(f)
#     for line in reader_obj:
#         print(line)


##########################################################################################
# write a program to extract total_vaccination of all countries

# import csv
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\vaccination_data.csv'
# with open(f_path) as f:
#     d = 0
#     reader_obj = csv.DictReader(f)
#     for line in reader_obj:
#         if line['TOTAL_VACCINATIONS'].strip(','):
#             d += int(line['TOTAL_VACCINATIONS'])
#     print(f'Total vaccination done by all countries is {d}')


##########################################################################################
## write a program to extract total_vaccination by countries

# import csv
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\vaccination_data.csv'
# with open(f_path) as f:
#     reader_obj = csv.reader(f)
#     for line in reader_obj:
#         print(line[5])


##########################################################################################
# write a program to extract country and who_region from vaccination data

# import csv
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\vaccination_data.csv'
# with open(f_path) as f:
#     reader_obj = csv.reader(f)
#     for line in reader_obj:
#         print(line[0], ':', line[2])


##########################################################################################
# write a program to extract countries with less than 10000 vaccinated people

# import csv
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\vaccination_data.csv'
# with open(f_path) as f:
#     reader_obj = csv.DictReader(f)
#     for line in reader_obj:
#         if line['TOTAL_VACCINATIONS'].strip(","):
#             count_ = int(line['TOTAL_VACCINATIONS'])
#             if count_ < 10000:
#                 print(line['COUNTRY'], ":",  line['TOTAL_VACCINATIONS'])


#############################################################################################
# country and persons vaccinated, and get top 3 countries with most vaccinated people

# import csv
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\vaccination_data.csv'
# with open(f_path) as f:
#     l1 = []
#     reader_obj = csv.reader(f)
#     for line in reader_obj:
#         if line[5].isnumeric():
#             l1. append((int(line[5]), line[0]))
#     *res, cnt1, cnt2, cnt3 = sorted(l1)
#     print(cnt1)
#     print(cnt2)
#     print(cnt3)



####################################################################################################
# get the latest updated country with its total vaccinations and numbers of people vaccinated

# import csv
# f_path = r'C:\Users\admin\PycharmProjects\python\27NOV\files\vaccination_data.csv'
# with open(f_path) as f:
#     l1 = []
#     l2 = []
#     reader_obj = csv.reader(f)
#     for line in reader_obj:
#         l2.append(line[4].split('-'))
#         l1.append(line[4].split("-")[-1])
#     print(l1)
#     print(l2)
#     *res, updated_, h = sorted(l1)
#     print(updated_)