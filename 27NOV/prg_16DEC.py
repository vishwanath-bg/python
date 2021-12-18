# __doc__ magic method for printing author name or message of what class is doing

# class a:
#     """printing some message"""
#     def __init__(self):
#         pass
#     def display(self):
#         print("hello welcome to python")
#
#
# print(a.__doc__)

####################################################################################################
# ITTERATORS

# l = [1, 2, 3, 4]
#
# a = iter(l)
# print(a)
# print(dir(l))
# print(dir(a))
#

####################################################################################################
# create a class which can return one element at a time from the list

# names = ["roshan", "dinesh", "vidya", "ramya"]
#
# class Sample:
#     def __init__(self, iterable):
#         self.names = iterable
#         self.iter_ = iter(self)
#
#     def __iter__(self):
#         return iter(self.names)
#
#     def __next__(self):
#         try:
#             return next(self.iter_)
#         except:
#             return "No elements"


# s = Sample(names)
# print(dir(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))



####################################################################################################
# create a class which has iteration capability

# names = ["roshan", "dinesh", "vidya", "ramya"]
#
# class Sample:
#     def __init__(self, iterable):
#         self.names = iterable
#
#     def __iter__(self):
#         return iter(self.names)
#
#
# s = Sample(names)
# for i in s:
#     print(i)



####################################################################################################
# create a class which acts as both iterable and iterator

# names = ["1", "2", "3", "4", "5"]
#
# class Sample1:
#     def __init__(self, names):
#         self.names = names
#         self.iter_ = iter(names)
#
#     def __iter__(self):
#         return iter(self.names)
#
#     def __next__(self):
#         try:
#             return next(self.iter_)
#         except:
#             return "No Elements"
#
#
# s = Sample1(names)
# for i in s:
#     print(i)

# print(next(s))

###################################################################################################################
# create a custom iterator to print numbers from 1 to 10


# class Number:
#     def __init__(self):
#         self.start = 0
#         self.end = 10
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             self.start += 1
#             return self.start
#         else:
#             raise StopIteration
#
#
# n = Number()
# for i in n:
#     print(i)
# print(next(n))


###################################################################################################################
# create a custom iterator print numbers from 10 to 1


# class ReverseNumber:
#     def __init__(self):
#         self.start = 11
#         self.end = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             self.start -= 1
#             return self.start
#         else:
#             raise StopIteration
#
#
# r = ReverseNumber()

# for i in r:
#     print(i)

# print(next(r))
# print(next(r))
# print(next(r))

###################################################################################################################
# create a custom iterator to print the elements of the list in reversed order

# l1 = [1, 2, 3, 4, 5]
#
#
# class Reversed:
#     def __init__(self, l1):
#         self.l1 = l1
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             self.index -= 1
#             return self.l1[self.index]
#         except IndexError:
#             raise StopIteration
#
#
# rl = Reversed(l1)
# for i in rl:
#     print(i)

###################################################################################################################
# create a custom iterator to print squares of the list of given numbers
l1 = [1, 2, 3, 4, 5, 6]


# class Squares:
#     def __init__(self, list_):
#         self.list_ = list_
#         self.index = 0
#         self.iter_ = iter(list_)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.list_) - 1:
#             return next(self.iter_) ** 2
#         else:
#             raise StopIteration
#
#
# s = Squares(l1)
# for i in s:
#     print(i)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))



#######################################################################################################################
# write a custom iterator to print prime numbers from  1 to 50

# n = 0
# while n <= 50:
#     for i in range(2, n):
#         if n % i == 0:
#             # print("not prime")
#             break
#     else:
#         print(n)
#     n += 1


# class Prime:
#     def __init__(self, end):
#         self.start = 2
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             x = self.start
#             if x > 1:
#                 self.start += 1
#                 for i in range(2, x):
#                     if x % i == 0:
#                         break
#                 else:
#                     return x
#         else:
#             raise StopIteration
#
#
# p = Prime(100)
# for i in p:
#     if i:
#         print(i)



#######################################################################################################################
#  ENCAPSULATION

# public


# class Parent:
#     def __init__(self):
#         self.name = "dad"
#
#     def display(self):
#         print("in parent class")
#
#
# class Child(Parent):
#     name1 = "son"
#
#     def display1(self):
#         print(self.name," is father of child ", self.name1)
#
#
# o = Child()
# o.display()
# o.display1()


#################################################################################################################
# PROTECCTED


# class Protected:
#     def __init__(self):
#         self._name = "surya"
#         self._age = 22
#
#     def display(self):
#         print(f"Name: {self._name} \nAge: {self._age}")
#
#
# # Accessing protected attributes in child class
# class Child(Protected):
#     def display1(self):
#         print(f"Name: {self._name} \nAge: {self._age}")
#
#
# # Accessing protected attributes outside the class
# p = Child()
# p.display()
# p.display1()
# print(p.age)        # Attribute Error



####################################################################################################
# PRIVATE


# class Private:
#     def __init__(self):
#         self.__mobileno = 9035864199
#         self.__pin = 67676
#
#     def display(self):
#         print(self.__pin, self.__mobileno)
#
#
# p = Private()
# # dictionary of private attribute in which it is stored in _private format
# print(p.__dict__)
# # {'_Private__mobileno': 9035864199, '_Private__pin': 67676}
# # print(p.__mobileno)       # Attribute Error
#
# print(p._Private__pin)    # Accessing the pin outside of the class
# print(p._Private__mobileno)



#############################################################################################################
# creating private variables with the same name in both parent class and child class

# class BankAccount:
#     __roi = 4.5
#
#     def display(self):
#         print("roi in BankAccount: ", self.__roi)
#
#
# class SavingsAccount(BankAccount):
#     roi = 2.5
#
#     def display1(self):
#         print("roi in savings account is : ", self._BankAccount__roi)
#
#
# b = SavingsAccount()
# b.display()
# b.display1()


#############################################################################################################

# class Student:
#     def __init__(self):
#         self.name = "surya"
#         self.__marks = 60
#
#     def get_marks(self):          # getter method
#         return self.__marks
#
#     def set_marks(self, new_marks):        # setter method
#         self.__marks = new_marks
#
#     def delete_marks(self):           # deleter method
#         del self.__marks
#
#     marks = property(get_marks, set_marks, delete_marks)  # creating a properties
#
#
# s1 = Student()
# print(s1.get_marks())
# s1.marks = 90
# print(s1.get_marks())
# # s1.set_marks(100)         # Attribute Error
# s1.delete_marks()
# print(s1.get_marks())


#############################################################################################################

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks
#
#     @property
#     def marks(self):
#         return self.__marks
#
#     @marks.setter
#     def marks(self, new_value):
#         self.__marks = new_value
#
#     @marks.deleter
#     def marks(self):
#         del self.__marks
#
# s1 = Student("surya", 80)
# s1.marks = 90
# print(s1.marks)

##############################################################################################################################
# create a class name account with bank name, balance, account number as variables and give only readability access to balance and account number


# class Bank:
#     def __init__(self, bank, balance, account_no):
#         self.bank = bank
#         self.__balance = balance
#         self.__account_no = account_no
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, new_balance):
#         raise TypeError("Access Denied...!!")
#
#     @property
#     def account_no(self):
#         return self.__account_no
#
#     @account_no.setter
#     def account_no(self, new_value):
#         raise TypeError("you don't have access")
#
#
# a1 = Bank("SBI", 10000, 35032617959)
# print(a1.account_no)
# # a1.account_no = 123
# print(a1.balance)
# # a1.balance = 90


##############################################################################################################################
#
# class Student:
#     def __init__(self, s_name, phy_marks, che_marks, bio_marks):
#         self.__s_name = s_name
#         self.__phy_marks = phy_marks
#         self.__che_marks = che_marks
#         self.__bio_marks = bio_marks
#
#     @property
#     def s_name(self):
#         print("*" * 50)
#         return self.__s_name
#
#     @s_name.setter
#     def s_name(self, new_student):
#         self.__s_name = new_student
#
#     @property
#     def phy_marks(self):
#         return self.__phy_marks
#
#     @phy_marks.setter
#     def phy_marks(self, new_phymarks):
#         self.__phy_marks = new_phymarks
#
#     @property
#     def che_marks(self):
#         return self.__che_marks
#
#     @che_marks.setter
#     def che_marks(self, new_chemarks):
#         self.__che_marks = new_chemarks
#
#     @property
#     def bio_marks(self):
#         return self.__bio_marks
#
#     @bio_marks.setter
#     def bio_marks(self, new_biomarks):
#         self.__phy_marks = new_biomarks
#
#     @property
#     def percentage(self):
#         print(f"Physics: {self.__phy_marks} | Chemistry: {self.__che_marks} | Biology: {self.__bio_marks}")
#         total = self.__phy_marks + self.__bio_marks + self.__che_marks
#         percentage = total // 3
#         return f"{percentage}% scored by {self.__s_name}"
#
#
# s1 = Student("surya", 80, 70, 60)
# print("before updating: ", s1.s_name)
# print("physics: ", s1.phy_marks)
# print("chemistry: ", s1.che_marks)
# print("biology", s1.bio_marks)
# print(s1.percentage)
# s1.s_name = "vijay"
# print("after updating: ", s1.s_name)
# s1.phy_marks = 50
# print("physics: ", s1.phy_marks)
# s1.che_marks = 60
# print("chemistry: ", s1.che_marks)
# s1.bio_marks = 80
# print("biology", s1.bio_marks)
# print(s1.percentage)



# create a custom iterator to print fibnochi series from range 1 to 50
# fibonacci

# class Fibnochi:
#     def __init__(self, start, end):
#         self.start = start
#         self.second = start + 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.start > self.end:
#             raise StopIteration
#         else:
#             a = self.start
#             temp = self.start + self.second
#             self.start = self.second
#             self.second = temp
#
#             return a
#
#
#
# f = Fibnochi(0, 50)
# for i in f:
#     print(i)
# print(next(f))
# print(next(f))
# print(next(f))
