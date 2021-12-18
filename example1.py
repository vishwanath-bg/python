x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
#
# if x > y:
#     print("x is greater number")
#
# if y > x:
#     print("y is greater number")
#######################################################################################################################
# x = int(input("Enter the value of x: "))
# y = int(input("Enter the value of y: "))
#
# if x > y:
#     print("x is greater number")
#
# else:
#     print("y is greater number")
#######################################################################################################################
# inline if statement
# if x > y: print("x is greater")


# if block(True block)    if condition else   else block(False block)

# print("x is greater" if x > y else "y is greater")
#######################################################################################################################
z = int(input("enter the value of z: "))

if x > y and x > z:
    print(f"x={x} is greater than y and z")

elif y > z:
    print(f"y={y} is greater than x and z")

else:
    print(f"z={z} is greater than x and y")
