# class Vehicle:
#     speed = 0
#     passanger = 1
#     fueltype = "disel"
#
#     def go(self):
#         print("vehicle in movement")
#
#     def stop(self):
#         print("vehicle is not in movement")
#
#     def change_direction(self):
#         print("changing direction")
#
#
# class Car(Vehicle):
#     modetype = "auto"
#     doors = 4
#     automaker = "hundai"
#
#     def radio(self):
#         print("no body touches my radio")
#
#     def windshield_wiper(self):
#         print("wiper is on")
#
#     def change_direction(self):
#         print("changing direction to right")
#         super().change_direction()
#
#
# car1 = Car()
# car1.change_direction()



########################################################################################
# class Product:
#
#     def __init__(self, name="Harry potter", price=550, discount_percent=10):
#         self.name = name
#         self.price = price
#         self.discount_percent = discount_percent
#
#     def getdiscount_amount(self):
#         print(self.price // self.discount_percent)
#
#     def getdiscountprice(self):
#         print(self.price - (self.price // self.discount_percent))
#
#     def printdescription(self):
#         print("it is a good book for childrens to know the magic world")
#
#
# class Book(Product):
#
#     def __init__(self, author="dinesh"):
#         self.author = author
#
#     def printdescription(self):
#         print("it is a good book")
#
# class Movie(Product):
#
#
#     def __init__(self, year=2011):
#         self.year = year
#
#     def printdescription(self):
#         print("good movie")
#
#
# obj1 = Movie()
# obj2 = Book()
# Movie.printdescription()

###############################################################################################################

# class PetrolCar:
#     fuellevel = 4
#     tankcapacity = 5
#
#     def fillup(self):
#         if self.fuellevel < 1.5:
#             print("fillup the tank")
#         else:
#             print(f"no need to fillup fuel capacity is {self.fuellevel} liters")
#
#
# class ElectricCar:
#     batterylevel = 9
#     batterycapacity = 100
#
#     def recharge(self):
#         if self.batterylevel < 10:
#             print("Battery Low")
#         else:
#             print(f"Battery level is: {self.batterylevel}")
#
#
# class HybridCar(ElectricCar, PetrolCar):
#     def __init__(self, runningmode):
#         self.runningmode  = runningmode
#
#     def switchmode(self):
#         print(f"curretn mode is {self.runningmode}")
#         if self.runningmode == "petrol":
#             print("switch to batterymode")
#             super().recharge()
#         else:
#             print("switch to petrol mode")
#             super().fillup()
#
#
# car1 = HybridCar('petrol')
# car1.switchmode()
# car1.fillup()
# car1.recharge()
###############################################################################################################
# EXEPTION HANDLING


# write a program to handle key error while count the elements
#
# names = ['apple', 'orange', 'grapes', 'apple', 'apple', 'apple', 'apple']
# d = {}
#
# for name in names:
#     try:
#         d[name] += 1
#
#     except KeyError:
#         d[name] = 1
# print(d)


###############################################################################################################
# write a program to extract first character of all the element in the list

# names = ['apple', 12, 'yahoo', 'gmail', [1.5, 2+3j]]
#
# for ele in names:
#     try:
#         print(ele[0])
#     except TypeError:
#         print("element is not subscriptable")

###############################################################################################################
# write a program to get the first word in each line of a file
# with open("file3.txt", 'r') as f:
#     for line in f:
#         try:
#             a = line.split()[0]
#         except IndexError:
#             print("Line is empty")



#####################################################################################################
# write a program to read a particular line from a file and check if that line is empty or not if the line is empty raise emptyline error or else print the line as it is. count the number of words in the line even if it is empty or not

# class Emptylineerror(Exception):
#     pass
#
# with open('file1.txt') as f:
#     for line in f:
#         if line:
#             a = len(line.split())
#             print(a)
#             if a == 0:
#                 raise Emptylineerror("line is empty")
#         else:
#             print(line)




# try:
#     a = int(input("enter a number: "))
# except ValueError as t:
#     print(t)
#     print("please enter a valid input......!")
# else:
#     print(a)
# finally:
#     print("thank you")

class Parent:
    def __init__(self):
        self.name1 = "virat"

    def display(self):
        print(self.name1)

class Parent1:
    def __init__(self):
        self.name2 = "anushka"

    def display1(self):
        print(self.name2)

class Child(Parent, Parent1):
    name = "son"

    def display2(self):
        Parent.display(self)
        print(self.name2, self.name1, self.name)


p1 = Child()
p1.display2()