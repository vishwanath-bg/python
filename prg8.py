d = {}

str_ = input('Enter the string: ')
if str_.isalpha():
    d[str_[0]] = str_

###############################################################
# for i in range(5):
#     str_ = input('Enter the string: ')
#     if str_.isalpha():
#         d[str_[0]] = str_
#     elif str_.isnumeric():
#         d[str_] = 0

print(d)
