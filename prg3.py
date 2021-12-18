x = input("Enter a string: ")[0]

# if x in 'aeiouAEIOU':
#     print(x)
# else:
#     print("character is not vowel")
##############################################################################
# if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#     dict_ = dict([(x, ord(x))])
#     print(dict_)
# elif x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
#     dict_ = dict([(x, ord(x))])
#     print(dict_)
# else:
#     print(f"{x} is not vowel")
##############################################################################
# if x in 'aeiouAEIOU':
#     dict_ = dict([(x, ord(x))])
#     print(dict_)
# else:
#     print("character is not vowel")
##############################################################################
dict_ = {}
if x.lower() in "aeiou":
    dict_[x] = ord(x)
    print(dict_)
else:
    print("character is not vowel")
