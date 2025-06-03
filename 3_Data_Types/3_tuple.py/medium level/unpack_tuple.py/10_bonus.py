# MASTER TUPLE UNPACKING CHALLENGE

# A list of student records, each as a tuple:
# Format: (name, (math_score, science_score, english_score), age, *hobbies)
# output : "Alice (20 yrs) scored an average of 84.33 and enjoys painting, reading"
students = [
    ("Alice", (85, 90, 78), 20, "painting", "reading"),
    ("Bob", (72, 88, 91), 21, "chess"),
    ("Charlie", (95, 92, 89), 19, "football", "gaming", "coding")
]
print(f"\nOriginal Record : {students}")

def solve_list():
    items = [
        f"{name} ({age} yrs) score an average of {sum(score)/len(score):.2f} and enjoys {', '.join(hobbies)}." for (name, score, age, *hobbies) in students
        ]
    print("\nSolved List : \n")
    for idx , item in enumerate(items, start=1):
        print(f"{idx}. {item}")

solve_list()
