name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
address = input("Enter your address: ")
contact = input("Enter your contact number: ")
email = input("Enter your email address: ")

with open("info.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Gender: {gender}\n")
    f.write(f"Address: {address}\n")
    f.write(f"Contact: {contact}\n")
    f.write(f"Email: {email}\n")

f=open("info.txt", "r")
    lines = f.readlines()
    for line in lines:
        if "Name" in line or "Email" in line:
            print(line.strip())