employee_records = []

for i in range(10):
    print(f"Enter details for employee {i+1}:")
    name = input("Name: ")
    occupation = input("Occupation: ")
    address = input("Address: ")
    employee_records.append({"name": name, "occupation": occupation, "address": address})
    print("Record added successfully.\n")

print("All the employee records:")
for i, record in enumerate(employee_records):
    print(f"Record {i+1}:")
    print(f"\tName: {record['name']}")
    print(f"\tOccupation: {record['occupation']}")
    print(f"\tAddress: {record['address']}\n")
    