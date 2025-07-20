# 💼 Project Title: EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM

print(f"\n------- EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM -------\n")

emp_data = {}

def show_menu():
    print(f"\n------------------- Choose an Option -----------------\n")
    print(f" 1. Add Employee.")
    print(f" 2. Mark Attendance.")
    print(f" 3. Update Bonus / Deductions.")
    print(f" 4. Generate Salary Report.")
    print(f" 5. View Employee Summary.")
    print(f" 6. Delete Employee.")
    print(f" 7. Exit.")
    try:
        option = int(input((f"\nChoose an option (1-7) : ")))
        return option
    except ValueError:
        print("\nPlease enter a valid number.")
        return 0

def add_emp():
    print(f"\n------------- Add Employee Details -------------\n")
    emp_id = input("Employee Id : ").upper()
    name = input("Employee Name : ").title()
    department = input("Department Name : ").title()
    try:
        daily_wages = float(input("Daily Wages : "))
    except ValueError:
        print(f"Invalid Wages !")
        return None, None, None
    emp_data[emp_id] = {
        'name': name,
        'department': department,
        'daily_wages': daily_wages,
        'attendance': {},
        'bonus': 0.0,
        'deduction': 0.0,
        'salary': 0.0
    }
    print("\nDetails Added Successfully ! Go and mark attendance. ")
    return emp_id, daily_wages, department

def mark_attendance():
    print(f"---------- WEEKLY ATTENDANCE -------------\n")

    if not emp_data:
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
        return

    week_days = ['mon', 'tue', 'wed', 'thur', 'fri']

    for idx , (emp_id , details) in enumerate(emp_data.items() , 1) : 
        print(f"{idx}. {emp_id} {details.get('name')}")

    emp_id = input("Enter Employee Id to mark attendance: ").upper()
    if emp_id not in emp_data:
        print("\nEmployee Id not found!")
        return

    while True:
        try:
            print(f"Present : 'P'\t\tAbsent : 'A'\n")
            print(f"Mon\tTue\tWed\tThu\tFri")
            print(f"------------------------------------------")

            weekly_attend = input().lower().replace('\t', '').replace(' ', '')

            if len(weekly_attend) != 5:
                raise ValueError("Please Enter Exactly 5 Days of Attendance")

            for day in weekly_attend:
                if day not in ('p', 'a'):
                    raise ValueError(f"\nInvalid Input only 'P' and 'A' are acceptable.")

            attendance = {day: status for day, status in zip(week_days, weekly_attend)}
            emp_data[emp_id]['attendance'] = attendance

            print(f"\n{emp_id}'s Attendance Marked Successfully !")
            return

        except ValueError as vs:
            print(f"\nError : {vs}")

def update_bonus_deduct():
    print(f"\n------------- BONUS / DEDUCTION -------------\n")

    if not emp_data:
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
        return


    for idx , (emp_id , details) in enumerate(emp_data.items() , 1) : 
        print(f"{idx}. {emp_id} {details.get('name')}")

    emp_id = input("Enter Employee Id to update Bonus/Deduction: ").upper()
    if emp_id not in emp_data:
        print("\nEmployee Id not found!")
        return

    while True:
        try:
            bonus = float(input(f"Enter Bonus (if any) : "))
            deduction = float(input(f"Enter Deduction (if any) : "))

            emp_data[emp_id]['bonus'] = bonus
            emp_data[emp_id]['deduction'] = deduction

            print(f"\nUpdation has done. Generate Salary !")
            return

        except ValueError as ve:
            print(f"\nError : {ve}")

def gen_sal():
    print(f"\n------------- SALARY CALCULATION -------------\n")
    if not emp_data:
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
        return

    for idx , (emp_id , details) in enumerate(emp_data.items() , 1) : 
        print(f"{idx}. {emp_id} {details.get('name')}")

    emp_id = input("Enter Employee Id to generate salary: ").upper()
    if emp_id not in emp_data:
        print("\nEmployee Id not found!")
        return

    details = emp_data[emp_id]
    attendance = details.get('attendance', {})
    daily_wages = details.get('daily_wages', 0)
    bonus = details.get('bonus', 0)
    deduction = details.get('deduction', 0)

    total_p = list(attendance.values()).count('p')
    total_a = list(attendance.values()).count('a')

    print(f"Total Presents : {total_p} Days")
    print(f"Total Absents : {total_a} Days")
    print(f"(Working_days * Daily_wages)")
    print(f"{total_p} * {daily_wages}/-")

    gross_sal = total_p * daily_wages
    print(f"Gross Salary :\t{gross_sal}/-")
    print(f"Bonus :\t\t  {bonus}/-")
    print(f"Deductions :\t -({deduction})")

    net_salary = (gross_sal + bonus) - deduction
    print(f"Net Salary : \t {net_salary}/-\n")

    emp_data[emp_id]['salary'] = net_salary
    print(f"\nSalary Generated Successfully !")

def view_summary():
    print(f"\n------------------Employee Summary --------------")
    if not emp_data:
        print(f"\nNO RECORD to show! ADD Employee's Details first.")
        return

    for idx, (emp_id, details) in enumerate(emp_data.items(), 1):
        print(f"\nSr No . {idx}\n")
        print(f"* Employee : {details.get('name', '-')} ({emp_id})")
        print(f"* Department : {details.get('department', '-')}')")
        print(f"* Days Worked : {list(details.get('attendance', {}).values()).count('p')}")
        print(f"* Daily Wages : {details.get('daily_wages', '-')}/-")
        print(f"* Bonus : {details.get('bonus', '-')}/-")
        print(f"* Deduction : {details.get('deduction', '-')}/-")
        print(f"* Monthly Salary : {details.get('salary', '-')}/-")

def delete_emp():
    print(f"\n------------- LIST OF EMPLOYEES -------------\n")
    if not emp_data:
        print("We don't have any employee.")
        return

    for idx, (emp_id, details) in enumerate(emp_data.items(), 1):
        print(f"{idx}. {emp_id} - {details.get('name')}")

    del_emp = input(f"\nChoose Employee Id To Remove : ").strip().upper()

    if del_emp in emp_data:
        removed = emp_data.pop(del_emp)
        print(f"{removed.get('name')} Removed Successfully ! ")
    else:
        print(f"Incorrect Employee - Id")

# Main Program Loop
while True:
    option = show_menu()
    if option == 1:
        add_emp()
    elif option == 2:
        mark_attendance()
    elif option == 3:
        update_bonus_deduct()
    elif option == 4:
        gen_sal()
    elif option == 5:
        view_summary()
    elif option == 6:
        delete_emp()
    elif option == 7:
        print(f"\nThanks For Visiting ")
        break
    else:
        print(f"\nChoose Option between 1 - 7 only")
