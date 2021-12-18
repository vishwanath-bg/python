from package1.module1 import a, b

print("file2 name:", __name__)


def mul_num(n1, n2):
    print("multiplication of two numbers")
    return n1 * n2


print(mul_num(a, b))
