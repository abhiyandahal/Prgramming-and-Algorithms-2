def maximum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

def minimum(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

while True:
    print("Select option:")
    print("1. Maximum")
    print("2. Minimum")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        result = maximum(num1, num2, num3)
        print("Maximum: ", result)
    elif choice == '2':
        result = minimum(num1, num2, num3)
        print("Minimum: ", result)
    elif choice == '3':
        break
    else:
        print("Invalid option")