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

def mark_attendance() :
    print(f"---------- WEEKLY ATTENDANCE -------------\n")
    print(f"Present : 'P'\t\tAbsent : 'A'\n")
    print(f"Mon\tTue\tWed\tThu\tFry")
    print(f"------------------------------------------")
    user_attendance = input().lower()
    attendance = [x for x in user_attendance.strip().split()]
    return attendance

def add_emp() :
    print(f"\n------------- Add Employee Details -------------")

    emp_id = input("Employee Id : ")
    name = input("Employee Name : ")
    dept = input("Department Name : ")
    daily_wages = float(input("Daily Wages : "))
    # bonus = float(input("Bonus if any : "))
    # deduct = float(input("Deduction if any : "))
    # salary = ( (attendance.count('p') * daily_wages) + bonus ) - deduct 
    
    emp_data[emp_id] = {
            'name' : name ,
            'dept' : dept ,
            'daily_wages' : daily_wages ,
        }
    return emp_id
    
    
while True :
    option = show_menu()    
    if option == 1 :
        emp_id = add_emp()
    elif option == 2 :
        attendance = mark_attendance()
        emp_data[emp_id]['attendance'] = attendance




