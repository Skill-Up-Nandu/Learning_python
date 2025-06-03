# MASTER TUPLE UNPACKING CHALLENGE

# A list of employee records:
# Format: (employee_id, (first_name, last_name), (basic_pay, hra, bonus), department)
# Output : "Employee #101: Alice Wong from Finance earns ₹37000"

employees = [
    (101, ("Alice", "Wong"), (30000, 5000, 2000), "Finance"),
    (102, ("Bob", "Smith"), (28000, 4500, 1500), "HR"),
    (103, ("Charlie", "Davis"), (32000, 6000, 2500), "Engineering"),
]
print(f"Query :, {employees}\n")
# function which converts the list into sentenes inside dictinary
def emp_dict():
    emp_report = {
        enroll: f"Employee #{enroll}: {' '.join(name)} from {department} earns ₹{sum(salary)}" for (enroll, name, salary, department) in employees
        }
    print(f"Solved : {emp_report}")

emp_dict()

