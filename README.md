def add(a, b):
    return a + b

def substract(a: int, b: int):
    return a - b

def multiplication(a: int, b: int):
    return a * b

def divide(a: int, b: int):
    return a / b

print("Welcom in the simple calculator. You can use this tool to perform basic math operations "
      "like substract or multiplication by two. In the next window you will choose which calculator you want to use"
      "Calculator add is available under 1, Susctract")

a = int(input("zadeklaruj a "))
b = int(input("zadeklaruj b "))

while True:
    choice = int(input("Enter your choice (1-4): "))
    if choice >= 1 and choice <= 4:
        break
    print("Invalid choice. Please enter a number between 1 and 4.")

print("You chose option", choice)

if choice == 1:
    print("You chose option 1.")
    result = add(a,b)
    print("Result:", result)
elif choice == 2:
    print("You chose option 2.")
elif choice == 3:
    print("You chose option 3.")
else:
    print("You chose an invalid option.")
# simple_calculator