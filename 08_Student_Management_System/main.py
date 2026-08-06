'''
====== Student Management System ======

1. Add Student
2. View All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Show Topper
7. Show Class Average
8. Exit
'''
students = []
def add_student_info():
    roll_no = int(input("Enter the Roll Number: "))
    name = input("Enter the name of the student: ")
    maths = int(input("Enter Maths Marks: "))
    physics = int(input("Enter Maths Marks: "))
    chemistry = int(input("Enter Maths Marks: "))

    total = maths+physics+chemistry
    average = total/3
    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    else:
        grade = 'C'
    student = {
        "roll_no": roll_no,
        "name": name,
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry,
        "total": total,
        "average": average,
        "grade": grade,
    }
    students.append(student)
    print(f"Student {name} added succesfully")

def view_all_student():
    if not students:
        print("Student not found.")
        return
    print("Student list")
    for index, student in enumerate(students):
        print(f"{index +1}. Roll Number: {student['roll_no']}, Name: {student['name']}, Maths Marks:{student['maths']}, Physics marks{student['physics']},Chemistry marks: {student['chemistry']}, Total marks: {student['total']}, Average marks: {student['average']}, Grade: {student['grade']} ")

def search_student():
    search_student_name = input("Enter The Name you want to search:").lower()
    found_student = [student for student in found_student if search_student_name in student['name'].lower()]
    if found_student:
        print("Found student")
        for index, student in enumerate(students):
            print(f"{index +1}. Roll Number: {student['roll_no']}, Name: {student['name']}, Maths Marks:{student['maths']}, Physics marks{student['physics']},Chemistry marks: {student['chemistry']}, Total marks: {student['total']}, Average marks: {student['average']}, Grade: {student['grade']} ")
    else:
        print("No student found")

def update_marks():
    search_student_name = input("Enter The Name you want to search:").lower
    found_student = [student for student in students if search_student_name in student['name'].lower()]
    if found_student:
        print("Found student")
        for index, student in enumerate(students):
            print(f"{index +1}. Roll Number: {student['roll_no']}, Name: {student['name']}, Maths Marks:{student['maths']}, Physics marks{student['physics']},Chemistry marks: {student['chemistry']}, Total marks: {student['total']}, Average marks: {student['average']}, Grade: {student['grade']} ")
            choice = input("Enter the stdent name you want to edit")
            if choice.lower() and 1 <= int(choice) <= len(found_student):
                index = int(choice) -1
                student = found_student[index]
                print(f"Updating student info: {student['name']}")
                maths = int(input("Enter new marks(Press enter to keep current marks: )")) or student['maths']
                physics = int(input("Enter new marks(Press enter to keep current marks: )")) or student['physics']
                chemistry = int(input("Enter new marks(Press enter to keep current marks: )")) or student['chemistry']
                total = maths+physics+chemistry
                average = total/3
                if average >= 90:
                    grade = 'A+'
                elif average >= 80:
                    grade = 'A'
                elif average >= 70:
                    grade = 'B'
                else:
                    grade = 'C'
                print(f"Stuent info of {student['name']}")
            else:
                print("Invalid choice.")
    else:
        print("Student Info not Found")

def delete_student_info():
    search_student_name = input("Enter The Name you want to search:").lower
    found_student = [student for student in students if search_student_name in student['name'].lower()]
    if found_student:
        print("Found student")
        for index, student in enumerate(students):
            print(f"{index +1}. Roll Number: {student['roll_no']}, Name: {student['name']}, Maths Marks:{student['maths']}, Physics marks{student['physics']},Chemistry marks: {student['chemistry']}, Total marks: {student['total']}, Average marks: {student['average']}, Grade: {student['grade']} ")
            choice = input("Enter the stdent name you want to edit")
            if choice.lower() and 1 <= int(choice) <= len(found_student):
                index = int(choice) -1
                student = found_student[index]
                students.remove(student)
                print(f"Student Info of {student['name']}deleted Succesfully")
            else:
                print("Invalid Choice.")
    else:
        print("Student info not found.")



def menu():     
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Show Class Average")
        print("8. Exit")

        choice = input("Enter Your Choice (1-8)")
        if choice == '1':
            add_student_info()
        elif choice == '2':
            view_all_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student_info()
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == '8':
            print("Thank You!")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()