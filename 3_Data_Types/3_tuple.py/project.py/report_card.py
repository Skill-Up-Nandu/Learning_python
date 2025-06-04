# STUDENT REPORT CRAD GENERATOR USING PYTHON TUPLE

# 📄 Report Card for Alice (Roll No: 101)
# - Scores: Math: 85, Science: 90, English: 78
# - Average: 84.33
# - Hobbies: painting, reading

students = [
    ("Alice", (85, 90, 78), 101, "painting", "reading"),
    ("Bob", (72, 88, 91), 102, "chess"),
    ("Charlie", (95, 92, 89), 103, "football", "gaming")
]
print("\nStudents Report Card Of Class - Xth\n")
max_avg = 0
topper_name = ""

for name, score, enroll , *hobbies in students:
    print(f"\n📄 Report Card for {name} (Roll No: {enroll})")
    math, sci, eng = score
    print(f"- Scores : Maths : {math}, Science : {sci}, English : {eng}")
    avg = (sum(score)/len(score))
    print(f"- Average : {avg:.2f}")
    print(f"- Hobbies : {', '.join(hobbies)}")
    if avg >= max_avg:
        max_avg = avg
        topper_name = name

print("\n--------------------------------------------\n")
print(f"✅ Class Topper : {topper_name} (Average {max_avg})\n")