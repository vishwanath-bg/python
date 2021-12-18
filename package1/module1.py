a = 10
b = 90

print("file1 name:", __name__)


def add_num(x1, x2):
    print("addition of two numbers")
    return x1 + x2


# print(add_num(a, b))
if __name__ == "__main__":
    print(add_num(a, b))
