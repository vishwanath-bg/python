dict_ = {'a': 'apple', 'b': 'ball', 'f': 'facebook', 'c': 10, 'd': 1.25}

key = input('Enter the key: ')
if key in dict_:
    if isinstance(dict_[key], str):
        n = dict_[key][::-1]
        dict_[key] = n
else:
    print('key is not found')
################################################################################
# for i in range(len(dict_)):
#     key = input('Enter the key: ')
#     if key in dict_:
#         if isinstance(dict_[key], str):
#             n = dict_[key][::-1]
#             dict_[key] = n
#     else:
#         print('key is not found')
#
print(dict_)
