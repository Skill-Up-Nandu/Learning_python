# 💼 Project Title: EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM

print(f"\n------- EMPLOYEE ATTENDANCE AND PAYROLL SYSTEM -------\n")

emp_data = {}
attendance = []
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


def add_emp() :
    print(f"\n------------- Add Employee Details -------------\n")

    if not emp_data :
        print(f"\nAdd your first employee's details : \n")
    emp_id = input("Employee Id : ").upper()
    name = input("Employee Name : ").title()
    department = input("Department Name : ").title()
    try :
        daily_wages = float(input("Daily Wages : "))
    except ValueError :    
        print(f"Invalid Wages !")
    emp_data[emp_id] = {
            'name' : name ,
            'department' : department ,
            'daily_wages' : daily_wages ,
        }
    
    print("\nDetails Added Successfully ! Go and mark attendance. ")
    return emp_id , daily_wages , department

def mark_attendance() :
    print(f"---------- WEEKLY ATTENDANCE -------------\n")

    if not emp_data :
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
        return
    while True : 
        try :
            print(f"Present : 'P'\t\tAbsent : 'A'\n")
            print(f"Mon\tTue\tWed\tThu\tFri")
            print(f"------------------------------------------")

            weekly_attend = input().lower()
            weekly_attend = weekly_attend.replace('\t', '')

            if len(weekly_attend) != 5 :
                raise ValueError("Please Enter Exactly 5 Days of Attendance")
            
            for day in weekly_attend :
                if day not in ('p' , 'a'):
                    raise ValueError(f"\nInvalid Input only 'P' and 'A' are exceptable.")
                
            attendance = [x for x in weekly_attend.strip().split()]
            emp_data[emp_id]['attendance'] = attendance
            print(f"\n{emp_id}'s Attendance Marked Successfully !")

            return attendance
        except ValueError as vs:
            print(f"\nError : {vs}")

            
    
def update_bonus_deduct() :
    print(f"\n------------- BONUS / DEDUCTION -------------\n")

    if not emp_data :
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
    
    else :   
        bonus = float(input(f"Enter Bonus (if any) : "))
        deduction = float(input(f"Enter Deduction (if any) :"))

        print(f"Updation has done. Generate Salary !")

        emp_data[emp_id]['bonus'] = bonus
        emp_data[emp_id]['deduction'] = deduction

        return bonus , deduction



def gen_sal() : 
    print(f"\n------------- SALARY CALCULATION -------------\n")
    if not emp_data :
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
    elif not attendance : 
        print(f"You have to add Attendance First .")
    else : 
        print(f"Total Presents : {float(attendance.count('p'))} Days")
        print(f"Total Absents : {float(attendance.count('a'))} Days")
        print(f"(Working_days\t*\tDaily_wages)")
        print(f"{float(attendance.count('p'))}\t\t*\t{daily_wages}/-")

        print(f"---------------------------------------------")
        gross_sal = float(attendance.count('p')*daily_wages)
        print(f"Gross Salary :\t{gross_sal}/-")
        print(f"Bonus :\t\t  {bonus}/-")
        print(f"Deductions :\t -({deduction})")

        print(f"---------------------------------------------")
        net_salary = (gross_sal + bonus)-deduction
        print(f"Net Salary : \t {net_salary}/-\n")

        emp_data[emp_id]['salary'] = net_salary

        print(f"\nSalary Generated Successfully !")
        return net_salary 

def view_summary() :
    print(f"\n------------------Employee Summary --------------")
    if not emp_data :
        print(f"\nNO RECORD to show! ADD Employee's Details first.")
    
    for idx , (emp_id , details) in enumerate(emp_data.items(), 1):
        print(f"\nSr No . {idx}\n")
        print(f"* Employee : {details.get('name', '-')} ({emp_id})")
        print(f"* Department : {details.get('department', '-')}")
        print(f"* Days Worked : {details.get('attendance', '-').count('p')}")
        print(f"* Daily Wages : {details.get('daily_wages', '-')}/-")
        print(f"* Bonus : {details.get('bonus', '-')}/-")
        print(f"* Deduction : {details.get('deduction', '-')}/-")
        print(f"* Monthly Salary : {details.get('salary', '-')}/-")
    
def delete_emp() :
    print(f"\n------------- LIST OF EMPLOYEES -------------\n")
    if not emp_data :
        print("We don't have any employee.")
    else : 
        for idx , (emp_id , details) in enumerate(emp_data.items() , 1) : 
            print(f"{idx}. {emp_id} {details.get('name')}")
        del_emp = input(f"\nChoose Employee Id To Remove : ").strip().upper()

        if del_emp in emp_data :
            removed = emp_data.pop(del_emp)
            print(f"{removed.get('name')} Removed Successfully ! ")
        else :
            print(f"Incorrect Employee - Id")
    


while True :
    option = show_menu() 
    try :    
        if option == 1 :
            emp_id , daily_wages , department = add_emp()

        elif option == 2 :
            attendance = mark_attendance()
        
        elif option == 3 :
            bonus , deduction = update_bonus_deduct()
        
        elif option == 4 :
            net_salary  = gen_sal()
        
        elif option == 5 :
            view_summary()

        elif option == 6 :
            delete_emp()
        
    




