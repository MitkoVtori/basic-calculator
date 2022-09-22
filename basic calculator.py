print("Welcome to calculator!")
print("I hope you're not using it to cheat!")
print("__________________________________________")
print("Version 1.0")
print("The amount of numbers you can use is 2")


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_degree(a, b):
    return a ** b


def subtract_degree(a, b):
    return a // b


print("Choose between")
print()
print("X  |  /  |  +")
print("-  |  X' |  /'")

list_allowed_usage = ["X", "/", "+", "-", "X'", "/'"]

print("choose \"end\" to stop the calculator, say anything else to continue using it.")
usage = input()
while usage != "end":
    if usage not in list_allowed_usage:
        print("Sorry, I don't understand.")
    else:
        print("What your numbers are?")
        a = float(input())
        b = float(input())
        if usage == "X":
            print(multiply(a, b))
        elif usage == "/":
            print(divide(a, b))
        elif usage == "+":
            print(add(a, b))
        elif usage == "-":
            print(subtract(a, b))
        elif usage == "X'":
            print(add_degree(a, b))
        else:
            print(subtract_degree(a, b))

print("I hope I'll see you tomorrow!")
