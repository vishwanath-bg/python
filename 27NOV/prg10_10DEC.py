''' object oriented programming '''


# class Car:
#     fname = "vishwanath"
#     lname = "b g"
#
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def disp(self):
#         print("hello welcome to object oriented program")
#         print(self.name, self.age)
#
#
# Creating object/instance
# ob1 = Car('vishwa', 22)
# accessing class variable using objects
# print(ob1.fname)
# print(ob1.lname)
# ob1.disp()

# accessing class variable using class
# print(Car.fname)
# print(Car.lname)

# __dict__
# print(Car.__dict__)


#############################################################################################################
# creating methods

# class Employee:
#     fname = "Test Yantra"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f"Company: {self.fname}")
#
#
# emp1 = Employee("steve", 22)
# emp2 = Employee("google", 20)
# emp1.display()
# print(f'Employee Name: {emp1.name}, Employee Age: {emp1.age}')
# emp2.display()
# print(f'Employee Name: {emp2.name}, Employee Age: {emp2.age}')


#############################################################################################################
# constructing object values with class attributes

# class Employee:
#     fname = "Test Yantra"
#     age = 30
#
#     def __init__(self, name, age):
#         self.fname = name
#         self.age = age
#
#     def display(self):
#         print(f"Company: {self.fname}")
#
#
# emp1 = Employee("steve", 22)
# emp2 = Employee("google", 20)
# emp1.display()
# print(f'Employee Name: {emp1.fname}, Employee Age: {emp1.age}')  # Employee Name: steve, Employee Age: 22
# print(f'Employee Name: {emp2.fname}, Employee Age: {emp2.age}')  # Employee Name: google, Employee Age: 20
# print(Employee.fname, Employee.age)     # Test Yantra 30



#############################################################################################################


# class Number:
#     a = 10
#     b = 3
#
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def display(self):
#         print(f"the class variables are {Number.a,Number.b}")
#         print(f"object variables are {self.a, self.b, self.c,self.d} ")
#
#
# obj1 = Number(5, 6)
# obj1.display()
# Number.a = 9
# Number.a = 6
# obj1.display()


# Calling a method using ClassName
# Number.display()    # error: Number.display() missing 1 required positional argument: 'self'
# Number.display(obj1)

'''

    as self takes the address of currently invoking object only objects can call any methods directly but if we want 
    to call it by class name the self argument must be full filled by passing any object
    
    Note: the modification done in class will always reflect in object address only if the connection is present or if 
    there is no over riding
    
    Note: when the modification takes place with respect to object the changes will be limited to objects address that 
    means neither the class nor other object will be affected by this change.

 '''

################################################################################
# create a class name sample which has two variables and write a method to add those two variables

# class Addition:
#     a = 10
#     b = 90
#
#     def add(self):
#         print(f"addition of {self.a} and {self.b} is {self.a + self.b}")
#
#
# sum = Addition()
# sum.add()

'''

        -----------------
        |  Addition     |
        |               |
        ----------------
        |    a          |
        |               |
        |    b          |
        ----------------
        |               |
        |  add()        |
        -----------------
'''



##########################################################################################################
# create a class name student and get the student name , Id and date of birth as a user input and check weather the student is over 18 years

# class Student:
#
#     def __init__(self, sname, sid, sdob):
#         self.sname = sname
#         self.sid = sid
#         self.sdob = sdob
#
#     def age(self):
#         date, month, year = self.sdob.split("/")
#
#         if abs(2021 - int(year)) > 18:
#             print(f"Student name: {self.sname}, Student ID: {self.sid}, Date of Birth: {self.sdob}")
#
#
# s1 = Student("varun", 1234, "06/04/1999")
# s2 = Student("vinay", 3344, "07/06/2004")
# s1.age()
# s2.age()


'''

        -----------------
        |  Student      |
        |               |
        ----------------
        |   sname       |
        |   sid         |
        |   sdob        |
        ----------------
        |               |
        |  age()        |
        -----------------
        
        
'''


##############################################################################################################

'''
        ------------------
        |  Bank account  |
        |                |
        ------------------
        |owner : string  |
        |Balance : Dollar|
        |                |
        ------------------
        |  deposit       |
        |(amount:Dollars)|
        |  withdrawal    |
        |(amount:Dollars)|
        ------------------
'''
# class BankAccount:
#     owner = "vishwa"
#     balance = 0
#
#     def deposit(self, dollars):
#         self.balance += dollars
#         print(f"after amount deposited {self.balance}")
#
#     def withdrawal(self, dollars):
#         if not self.balance-dollars >= 0:
#             print("insufficient balance please try later....!")
#         else:
#             self.balance -= dollars
#             print(f"after withdrawal amount balance is {self.balance}")
#
#
# a1 = BankAccount()
# print(a1.owner)
# a1.deposit(1000)
# a1.withdrawal(1000)
#
# print(a1.balance)
##############################################################################################################

'''
        ----------------------
        |   Circle           |
        |                    |
        ----------------------
        |x_co: float         |
        |y_co: float         |
        |radius: float       |
        ----------------------
        |find_area           |
        |find_circumference()|
        ----------------------
'''

# class Circle:
#     x_co = 0.0
#     y_co = 0.0
#     radius = 0.0
#
#     def find_area(self):
#         print(f"radius of circle is {3.142 * self.radius ** 2}")
#
#     def find_circumference(self):
#         print(f"circumference of circle is {2 * 3.142 * self.radius}")
#
#
# data1 = Circle()
# data1.radius = 5
# data1.find_area()
# data1.radius = 5
# data1.find_circumference()


##############################################################################################################

'''
        ----------------------
        |   ListData         |
        |                    |
        ----------------------
        |list_: list         |
        |                    |
        ----------------------
        |add_data(element)   |
        |delete_data(element)|
        |find_length()       |
        |find_data(element)  |
        |                    |
        ----------------------
       
'''


# class ListData:
#     list_ = [1, 2, 3, 4, 5, 6]
#
#     def add_data(self, element):
#         self.list_.append(element)
#         print(self.list_)
#
#     def delete_data(self, element):
#         if element in self.list_:
#             self.list_.remove(element)
#         else:
#             print("no such element")
#         print(self.list_)
#
#     def find_length(self):
#         print(len(self.list_))
#
#     def find_data(self, element):
#         if element in self.list_:
#             self.list_.index(element)
#         else:
#             print("no such element")
#         print(self.list_)
#
#
# data = ListData()
# data.add_data(5)
# data.delete_data(5)
# data.find_data(5)
# data.find_length()


######################################################################################################################
'''
        ----------------------
        |   Books            |
        |                    |
        ----------------------
        |book_data: dict     |
        | book_id: int       |
        |book_name: str      |
        |book_author: str    |
        |year_of_publish: str|
        |price: float        |
        |                    |
        ----------------------
        |add_new_book(book)  |
        |delete_book(book)   |
        |display_book(book)  |
        |inquire_book(book)  |
        |                    |
        ----------------------

'''

#
# class Books:
#     book_data = {"Harry potter": {"book_id": 123,
#                                    "book_name": "Harry Potter",
#                                    "book_author": "dinesh",
#                                    "year_of_publish": "2000",
#                                    "price": 101.00
#                                  }
#                  }
#
#     def add_new_book(self):
#         while True:
#             choice = int(input("press 1 to add a book \npress 2 to end the process\n "))
#             if choice == 1:
#                 book = input("Enter a book: ")
#                 if book not in self.book_data:
#                     bookid = int(input("Enter book Id: "))
#                     bookname = input("enter book name: ")
#                     bookauthor  = input("enter book author: ")
#                     yearofpublish = input("enter a year: ")
#                     price = float(input("enter a price: "))
#                     # Method 1
#                     details = dict([("book_id", bookid), ("book_name", bookname), ("book_author", bookauthor), ("year_of_publish", yearofpublish), ("price", price)])
#                     self.book_data[book] = details
#                      # Method 2
#                     # self.book_data[book] = dict.fromkeys(["book_id", "book_name", "book_author", "year_of_publish", "price"])
#                     print(self.book_data)
#                 else:
#                     print("book is already in your cart")
#             elif choice == 2:
#                 print("Completed")
#                 break
#             else:
#                 print("invalid request")
#     def delete_book(self, book):
#         if book in self.book_data:
#             self.book_data.pop(book)
#         else:
#             print("oops...! book is not available in your cart")
#         print(self.book_data)
#
#     def display_book(self, book):
#         if book in self.book_data:
#             print(book, self.book_data[book])
#         else:
#             print("book is not present in you library....!")
#
#     def inquire_book(self, book):
#         if book in self.book_data:
#             print("book is available.....")
#         else:
#             print("book is not available")
#
#
# book1 = Books()
# book1.add_new_book()
# book1.delete_book('Harry potter')
# book1.display_book("two states")
# book1.inquire_book("two states")



################################################################################################################
'''
        ----------------------
        |                    |
        |        person      |
        ----------------------
        |name: str           |
        |birthdate: str      |
        ----------------------
        |get_name(): str     |
        |set_name(name): None|
        |is_birthday(): bool |
        ----------------------

'''

# class Person:
#     name = "dinesh"
#     birthdate = "11/12/2000"
#
#     def get_name(self):
#         print(self.name)
#
#     def set_name(self, name):
#         Person.name = name
#         print(Person.name)
#
#     def is_birthday(self):
#         date, month, year = self.birthdate.split("/")
#         if date == "13" and month == '12':
#             print(True)
#         else:
#             print(False)
#
#
# obj1 = Person()
# obj1.get_name()
# obj1.set_name("vivek")
# obj1.set_name(None)
# obj1.is_birthday()



##################################################################################################################
# 14/12/2021


# class ChiefMinister:
#     current_cm = "yediyurappa"
#
#     def display(self):
#         print(self.current_cm)
#
#     def replacement(self, votes):
#         if votes > 50:
#             self.current_cm = "bommai"
#
#
# bjp = ChiefMinister()
# bjp.replacement(51)
# bjp.display()       # bommai
# com_people = ChiefMinister()
# com_people.display()        # yediyurappa
# opposition = ChiefMinister()
# opposition.display()        # yediyurappa



''' using inbuilt @classmethod to directly point to class address '''

# class ChiefMinister:
#     current_cm = "yediyurappa"
#
#     def display(self):
#         print(self.current_cm)
#
#     @classmethod
#     def replacement(cls, votes):
#         if votes > 50:
#             cls.current_cm = "bommai"
#
#
# bjp = ChiefMinister()
# bjp.replacement(51)
# bjp.display()       # bommai
# com_people = ChiefMinister()
# com_people.display()        # bommai
# opposition = ChiefMinister()
# opposition.display()        # bommai

##################################################################################################################
''' creating object inside the class'''
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(self.name, self.salary)
#
#     @classmethod
#     def spam(cls):
#         e1 = cls("shyam", 10000)
#         e1.display()
#
#
# e = Employee("ram", 20000)
# e.display()             #  "ram", 20000
# e.spam()              #   "shyam", 10000



''' static method for unbound the methods with main class and objects '''
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def display(self):
#         print(self.name, self.salary)
#
#     @staticmethod
#     def addition(a, b):
#         return a + b
#
#
# e = Employee("ram", 20000)
# print(e.addition(3, 2))
# print(Employee.addition(1, 2))


###############################################################################################################

# def display_message(f):
#     def wrapper(*args, **kwargs):
#         print("hello everyone")
#         f(*args, **kwargs)
#     return wrapper
#
#
# @display_message
# def display():
#     print("in display")
#
#
# display()



####################################################################################################################

# class Employee:
#
#     def __init__(self):
#         self.a = 10
#
#     def __call__(self):
#         print("in call function")
#
#
# e = Employee()
# print(callable(Employee))
# print(callable(e))
# e()

####################################################################################################################
# create a class to call the object inorder to print log message hello everyone


# class Message:
#
#     def __call__(self):
#         print('hello everyone')
#
#
# m1 = Message()
# m1()


####################################################################################################################
# passing arguments to callable object

# class Message:
#
#     def __call__(self, name):
#         print(f'hello {name}')
#
#
# m1 = Message()
# m1("ram")

####################################################################################################################
# to create a callable object to check if the number is even or odd

# class Message:
#
#     def __call__(self, a):
#         if a % 2 == 0:
#             return 'even'
#         return 'odd'
#
#
# m1 = Message()
# print(m1(3))
# print(m1(2))


####################################################################################################################
# create a callable object to check if the given two strings are anagrams or not

# class Anangrams:
#
#     def __call__(self, a, b):
#         if sorted(a) == sorted(b):
#             return "strings are anagrams"
#         return "strings are not anagrams"
#
#
# a1 = Anangrams()
# print(a1('hello', 'lloeh'))


####################################################################################################################
# Normal function decorator

# def outer(f):
#     def wrapper():
#         print('hello everyone')
#         f()
#     return wrapper
#
#
# @outer
# def display():
#     print("welcome")
#
#
# display()



# to create class decorator with same examaple decorating the main function using internally created object
'''
        log()
          |
          v 
      log_object
          |
          v 
display = log_object(display)

'''

# class log:
#     def __call__(self, func):
#         def wrapper():
#             print('hello everyone')
#             func()
#         return wrapper
#
#
# @log()
# def display():
#     print("welcome")
#
#
# display()


####################################################################################################################
# write a class decorator to print a message after executing any function

# def outer(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print("hello everyone")
#     return wrapper
#
#
# @outer
# def display():
#     print("hello world")
#
#
# display()



''' using class decorator '''

# class Log:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             print("hello every one")
#         return wrapper
#
#
# @Log()
# def display():
#     print("hello world")
#
#
# display()


###########################################################################################################
# write a class decorator to execute a function for 3 times
# def repeat(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return outer
#
#
# @repeat(6)
# def add(a, b):
#     print(a+b)
#
#
# add(9, 4)


'''using class decorator'''

# class Repeat:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(self.n):
#                 func(*args, **kwargs)
#         return wrapper
#
#
# @Repeat(5)
# def addition(a, b):
#     print(a + b)
#
#
# addition(3, 5)


################################################################################################################
# write a class decorator to print good afternoon message if user didn't gave any input

# def log(msg="hello good afternoon"):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             print(msg)
#             func(*args, **kwargs)
#         return wrapper
#     return outer
#
#
# @log("hi there")
# def spam():
#     print('displays')
#
#
# spam()



''' using class decorator '''

# class Message:
#     def __init__(self, n="hello good afternoon"):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(self.n)
#             func(*args, **kwargs)
#         return wrapper
#
#
# @Message(6)
# def display():
#     print('message is displays')
#
#
# display()



#####################################################################################################################
# ALL FUNCTION DECORATORS TO CLASS DECORATORS WRITE
#####################################################################################################################

# write a class decorator to reverse a string

# class Reverse:
#     def __init__(self, string):
#         self.string = string
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             print(self.string[::-1])
#         return wrapper
#
#
# @Reverse("hello")
# def string(a):
#     pass
#
#

####################################################################################
# write a class decorator that counts the number of arguments given to main function

# class Count:
#     def __call__(self, f):
#         def wrapper(*args, **kwargs):
#             f(*args, **kwargs)
#             num = len(args) + len(kwargs)
#             print(num)
#         return wrapper
#
#
# @Count()
# def display(a, b, v, c):
#     print(a, b, c, v)
#
#
# @Count()
# def display1(u, v, x, y, z):
#     print(u, v, x, y, z)
#
#
# display(1, 2, 3, c=9)
# display1(5, 6, x=90, y=80, z=10)


#####################################################################################################
# write a class decorator function which checks if the given parameters are integer type

# class Check_type:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             for i in args:
#                 if isinstance(i, int):
#                     print(f"{i} is integer type")
#                 else:
#                     print(f"{i} is not integer type")
#         return wrapper
#
#
# @Check_type()
# def values(a, b, c, d, e, f):
#     print(a, b, c, d, e, f)
#
#
# values(1, 2, 3, '4', 5, 6)


##########################################################################################################


# class Hello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             s = ""
#             for i in args:
#                 for j in list(i):
#                     s = j + s
#             return s
#         return wrapper
#
#
# @Hello()
# def reverse(string):
#     print("additional function")
#
#
# print(reverse('hello'))

################################################################################################################
# write a program to create a dictionary of key as a first character and word as value

# from collections import defaultdict
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         d = defaultdict(str)
#         func(*args, **kwargs)
#         # for i in args:
#         a = "".join(args).split()
#         # print(a)
#         for j in a:
#             d[j[0]] = j
#         print(d)
#
#     return wrapper
#
#
# @outer
# def string(x):
#     print(x)
#
#
# string("welcome to python vishwa")
#


