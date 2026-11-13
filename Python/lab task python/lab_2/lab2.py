name = input("Enter Employee Name: ")
employee_id = int(input("Enter Employee ID: "))
salary = float(input("Enter Salary: "))
department = input("Enter Department: ")
active = input("Is the employee active? (yes/no): ")

# Convert yes/no into True or False
active = active.lower() == "yes"

# Display employee details
print("\n--- Employee Details ---")
print("Name       :", name)
print("ID         :", employee_id)
print("Salary     :", salary)
print("Department :", department)
print("Active     :", active)