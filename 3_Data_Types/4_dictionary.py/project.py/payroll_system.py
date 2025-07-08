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


def add_emp() :
    print(f"\n------------- Add Employee Details -------------\n")

    if not emp_data :
        print(f"\nAdd your first employee's details : \n")
    emp_id = input("Employee Id : ")
    name = input("Employee Name : ")
    department = input("Department Name : ")
    daily_wages = float(input("Daily Wages : "))
    
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

    else : 
        print(f"Present : 'P'\t\tAbsent : 'A'\n")
        print(f"Mon\tTue\tWed\tThu\tFri")
        print(f"------------------------------------------")

        user_attendance = input().lower()
        attendance = [x for x in user_attendance.strip().split()]
        emp_data[emp_id]['attendance'] = attendance

        print(f"\nAttendance Marked Successfully. Add Bonus !")

        return attendance
    
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



def gen_sal() : 
    print(f"\n------------- SALARY CALCULATION -------------\n")
    if not emp_data :
        print(f"\nNO RECORD Yet. ADD Employee's Details first.")
    elif "attendance" not in emp_data.keys() : 
        print(f"You have to add Attendance First .")
    else : 
        print(f"Total Presents : {float(attendance.count('p'))} Days")
        print(f"Total Absents : {float(attendance.count('a'))} Days")
        print(f"(Working_days\t*\tDaily_wages)")
        print(f"{float(attendance.count('p'))}\t\t*\t{daily_wages}/-")

        print(f"---------------------------------------------")
        gross_sal = float(attendance.count('p'))*daily_wages
        print(f"Gross Salary :\t{gross_sal}/-")
        print(f"Bonus :\t\t  {emp_data.get('bonus')}/-")
        print(f"Deductions :\t -({emp_data.get('deduction')})")

        print(f"---------------------------------------------")
        net_sal = (gross_sal + emp_data.get('bonus'))-emp_data.get('deduction')
        print(f"Net Salary : \t {net_sal}/-\n")

        emp_data[emp_id]['salary'] = net_salary

        print(f"/nSalary Generated Successfully !")
        return net_sal 

def view_summary() :
    print(f"\n------------------Employee Summary --------------")
    if not emp_data :
        print(f"\nNO RECORD to show! ADD Employee's Details first.")
    
    for idx , (emp_id , details) in enumerate(emp_data.items(), 1):
        print(f"\nSr No . {idx}\n")
        print(f"* Employee : {details.get('name', 'N/A')} ({emp_id})")
        print(f"* Department : {details.get('department', 'N/A')}")
        print(f"* Days Worked : {details.get(attendance).count('p'), 'N/A'}")
        print(f"* Daily Wages : {details.get('daily_wages', 'N/A')}")
        print(f"* Bonus : ₹{details.get('bonus', 'N/A')}")
        print(f"* Deduction : ₹{details.get('deduction', 'N/A')}")
        print(f"* Monthly Salary : ₹{details.get('salary', 'N/A')}")
    
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
    if option == 1 :
        emp_id , daily_wages , department = add_emp()

    elif option == 2 :
        mark_attendance()
        
    elif option == 3 :
        update_bonus_deduct()
        
    elif option == 4 :
        net_salary  = gen_sal()
        
    elif option == 5 :
        view_summary()

    elif option == 6 :
        delete_emp()
    




