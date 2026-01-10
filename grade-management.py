
students = {}

print("--- Student Grade System ---")

count = int(input("Koyjon student-er marks add korte chan? "))

for i in range(count):
    name = input(f"\n{i+1} no. Student-er nam: ")
    mark = float(input(f"{name}-er mark likhun: "))
    
    students[name] = mark

print("\n--- Result Sheet ---")

for name, mark in students.items():
    if mark >= 80:
        grade = "A+"
    elif mark >= 40:
        grade = "Pass"
    else:
        grade = "Fail"
    
    print(f"Student: {name} | Mark: {mark} | Result: {grade}")