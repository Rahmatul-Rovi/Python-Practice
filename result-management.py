# result_management.py

def calculate_grade(marks):
    if marks >= 80: return "A+"
    elif marks >= 70: return "A"
    elif marks >= 60: return "B"
    elif marks >= 50: return "C"
    elif marks >= 40: return "D"
    else: return "F"

def main():
    student_data = {}
    
    print("--- 🎓 Student Result System ---")
    student_name = input("Enter Student Name: ")
    num_subjects = int(input("How many subjects? "))

    total_marks = 0

    for i in range(num_subjects):
        sub_name = input(f"Enter Subject {i+1} Name: ")
        marks = float(input(f"Enter marks for {sub_name}: "))
        
        student_data[sub_name] = {
            "marks": marks,
            "grade": calculate_grade(marks)
        }
        total_marks += marks

    average = total_marks / num_subjects
    
    print(f"\n================================")
    print(f"       REPORT CARD: {student_name}")
    print(f"================================")
    
    for sub, info in student_data.items():
        print(f"{sub:15}: {info['marks']} ({info['grade']})")
    
    print(f"--------------------------------")
    print(f"Total Marks:   {total_marks}")
    print(f"Average:       {average:.2f}")
    print(f"Final Status:  {'PASSED' if average >= 40 else 'FAILED'}")
    print(f"================================")

if __name__ == "__main__":
    main()