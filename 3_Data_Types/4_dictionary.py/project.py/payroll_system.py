# 💼 Project Title: EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM

print(f"\n------- EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM -------\n")

emp_data = {}
def show_menu() : 
    print(f" 1. Add Employee.")
    print(f" 2. Mark Attendance.")
    print(f" 3. Update Bonus / Deductions.")
    print(f" 4. Generate Salary Report.")
    print(f" 5. View Employee Summary.")
    print(f" 6. Delete Employee.")
    print(f" 7. Exit.")
    option = int(input((f"\nChoose an option (1-7) : \n")))
    return option

def add_emp() :
    print(f"\n------------- Add Employee Details -------------")

    emp_id = input("Employee Id : ")
    name = input("Employee Name : ")
    dept = input("Department Name : ")
    daily_wages = float(input("Daily Wages : "))
    attendace = list(input("Attendance (P- 1 / A- 0) "))
    bonus = float(input("Bonus if any : "))
    deduct = float(input("Deduction if any : "))
    salary = ( (attendace.count(1) * daily_wages) + bonus ) - deduct 
    
    emp_data[emp_id] = {
            'name' : name ,
            'dept' : dept ,
            'daily_wages' : daily_wages ,
            'attendance' : attendace ,
            'bonus' : bonus ,
            'deduct' : deduct ,
            'salary' : salary 
        }
    
while True :
    option = show_menu()    
    if option == 1 :
        add_emp()




