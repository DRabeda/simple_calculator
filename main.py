def add(a, b):
    return a + b


def substract(a: int, b: int):
    return a - b


def multiplication(a: int, b: int):
    return a * b


def divide(a: int, b: int):
    return a / b


print("Welcome in the simple calculator. You can use this tool to perform basic math operations "
      "like substract or multiplication by two. In the next window you will choose which calculator you want to use "
      "Calculator add is available under 1, substract under 2, multiplication under 3 and divide under 4")

a = int(input("declare a "))
b = int(input("declare b "))

while True:
    choice = int(input("Enter your choice (1-4): "))
    if choice >= 1 and choice <= 4:
        break
    print("Invalid choice. Please enter a number between 1 and 4.")


def simple_calculator (a,b, choice):
    if choice == 1:
        print("You chose option 1.")
        result = add(a, b)
    elif choice == 2:
        print("You chose option 1.")
        result = substract(a, b)
    elif choice == 3:
        print("You chose option 3.")
        result = multiplication(a, b)
    elif choice == 4:
        print("You chose option 4.")
        result = divide(a, b)
    else:
        print("You chose an invalid option.")
    return (f"The results is: {result}")

print(simple_calculator(a,b,choice))
