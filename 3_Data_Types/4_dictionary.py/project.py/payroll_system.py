# 💼 Project Title: EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM

print(f"\n------- EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM -------\n")

emp_data = {}
def show_menu() : 
    print(f"\n------------------- Choose an Option -----------------\n")
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
    department = input("Department Name : ")
    daily_wages = float(input("Daily Wages : "))
    
    emp_data[emp_id] = {
            'name' : name ,
            'dept' : department ,
            'daily_wages' : daily_wages ,
        }
    return emp_id , daily_wages , department
    
def update_bonus_deduct() :
    print(f"\n------------- BONUS / DEDUCTION -------------\n")
    bonus = float(input(f"Enter Bonus (if any) : "))
    deduction = float(input(f"Enter Deduction (if any) :"))
    return bonus , deduction

def gen_sal() : 
    print(f"\n------------- SALARY CALCULATION -------------\n")
    total_present = float(attendance.count('p'))
    print(f"Total Presents : {total_present} Days")
    print(f"Total Absents : {float(attendance.count('a'))} Days")
    print(f"(Working_days\t*\tDaily_wages)")
    print(f"{total_present}\t\t*\t{daily_wages}")

    print(f"---------------------------------------------")
    gross_sal = total_present*daily_wages
    print(f"Gross Salary :\t{gross_sal}")
    print(f"Bonus :\t\t  {bonus}")
    print(f"Deductions :\t -({deduction})")

    print(f"---------------------------------------------")
    net_sal = (gross_sal + bonus)-deduction
    print(f"Net Salary : \t {net_sal}\n")
    return net_sal , total_present

def view_summary() :
    print(f"\n------------------Employee Summary --------------")
    for idx , (emp_id , details) in enumerate(emp_data.items(), 1):
        name = details.get('name', 'N/A')
        dept = details.get('department', 'N/A')
        daily_wages = details.get('daily_wages', 'N/A')
        bonus = details.get('bonus', 'N/A')
        dedcution = details.get('deduction', 'N/A')
        salary = details.get('salary', 'N/A')

        print(f"\nSr No . {idx}\n")
        print(f"* Employee : {name} ({emp_id})")
        print(f"* Department : {dept}")
        print(f"* Days Worked : {total_present}")
        print(f"* Daily Wages : {daily_wages}")
        print(f"* Bonus : ₹{bonus}")
        print(f"* Deduction : ₹{deduction}")
        print(f"* Monthly Salary : ₹{salary}")
    
while True :
    option = show_menu()    
    if option == 1 :
        emp_id , daily_wages , department = add_emp()
    elif option == 2 :
        attendance = mark_attendance()
        emp_data[emp_id]['attendance'] = attendance
    elif option == 3 :
        bonus, deduction = update_bonus_deduct()
        emp_data[emp_id]['bonus'] = bonus
        emp_data[emp_id]['deduction'] = deduction
    elif option == 4 :
        net_salary , total_present = gen_sal()
        emp_data[emp_id]['salary'] = net_salary
    elif option == 5 :
        view_summary()
    




