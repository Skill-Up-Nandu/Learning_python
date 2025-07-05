# using nested dictionary print all student name and thier average marks

results = {
  "John": {"math": 85, "science": 92},
  "Sara": {"math": 78, "science": 89}
}

def print_results():
    print(f"\nThe results of individual srudent : \n")
    for stu , marks in results.items():
        avg_marks = sum(marks.values())/len(marks)
        print(f"{stu} : {avg_marks}")

print_results()
        
