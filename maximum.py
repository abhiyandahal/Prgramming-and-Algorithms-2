def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

while True:

    print("Select operation:")
    print("1. Find maximum")
    print("2. Find minimum")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        result = maximum(num1, num2)
        print("Maximum: ", result)
    elif choice == '2':
        result = minimum(num1, num2)
        print("Minimum: ", result)
    elif choice == '3':
        break
    else:
        print("Invalid choice")