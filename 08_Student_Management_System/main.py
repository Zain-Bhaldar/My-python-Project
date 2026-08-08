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
def calculate_grades(average):
    if average >= 90:
        return'A+'
    elif average >= 80:
        return'A'
    elif average >= 70:
        return 'B'
    else:
        return 'C'
    
def add_student_info():
    roll_no = int(input("Enter the Roll Number: "))
    name = input("Enter the name of the student: ")
    maths = int(input("Enter Maths Marks: "))
    physics = int(input("Enter Physics Marks: "))
    chemistry = int(input("Enter Chemistry Marks: "))

    total = maths+physics+chemistry
    average = total/3
    grade = calculate_grades(average)
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

def display_student(index, student):
    print(
        f"{index}. "
        f"Roll No: {student['roll_no']}, "
        f"Name: {student['name']}, "
        f"Maths: {student['maths']}, "
        f"Physics: {student['physics']}, "
        f"Chemistry: {student['chemistry']}, "
        f"Total: {student['total']}, "
        f"Average: {student['average']:.2f}, "
        f"Grade: {student['grade']}"
    )

def view_all_student():
    if not students:
        print("Student not found.")
        return
    print("Student list")
    for index, student in enumerate(students, 1):
        display_student(index, student)

def search_student():
    search_student_name = input("Enter The Name you want to search:").lower()
    found_student = [
        student for student in students
        if search_student_name in student['name'].lower()
    ]
    return found_student


def update_marks():
    found_student = search_student()
    if found_student:
        print("Found student")
        for index, student in enumerate(found_student, 1):
            display_student(index, student)
            try:
                choice = int(input("Enter the student name you want to edit"))
            except ValueError:
                print(("Please enter a valid number."))
                return
            if 1 <= choice <=len(found_student):
                index = choice - 1
                student = found_student[index]
                print(f"Updating student info: {student['name']}") 
                new_maths = input("Enter new marks(Press enter to keep current marks: )")
                if new_maths == "":
                    maths = student['maths']
                else:
                    maths = int(new_maths)
                new_physics = input("Enter new marks(Press enter to keep current marks: )")
                if new_physics == "":
                    physics = student['physics']
                else:
                    physics = int(new_physics)
                new_chemistry = input("Enter new marks(Press enter to keep current marks: )")
                if new_chemistry == "":
                    chemistry = student['chemistry']
                else:
                    chemistry = int(new_chemistry)
                total = maths+ physics+chemistry
                average = total/3
                grade = calculate_grades(average)
                student['maths'] = maths
                student['physics'] = physics
                student['chemistry'] = chemistry
                student['total'] = total
                student['average'] = average
                student['grade'] = grade
                print(f"{student['name']}'s marks updated successfully.")
            else:
                print("Invalid choice.")
    else:
        print("Student Info not Found")

def delete_student_info():
    found_student = search_student()
    if found_student:
        print("Found student")
        for index, student in enumerate(found_student, 1):
            display_student(index, student)
            try:
                choice = int(input("Enter the student number you want to edit"))
            except ValueError:
                print(("Please enter a valid number.")) 
                return
            if 1 <= choice <= len(found_student):
                index = choice -1
                student = found_student[index]
                students.remove(student)
                print(f"Student Info of {student['name']}deleted Succesfully")
            else:
                print("Invalid Choice.")
    else:
        print("Student info not found.")



def show_topper():
    if not students:
        print("Student not found.")
        return
    topper = students[0]
    for student in students:
        if student['average'] > topper['average']:
            topper = student

    print("\nTopper:")
    display_student(1, topper)

def show_class_average():
    if not students:
            print("Student not found.")
            return
    total = 0
    for student in students:
        total += student['average']

    class_average = total/len(students)
    print(f"Class average is {class_average:.2f}")

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
            found_student = search_student()
            if found_student:
                print("Found student")
                for index, student in enumerate(found_student, 1):
                    display_student(index, student)
            else:
                print("No student found")
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student_info()
        elif choice == '6':
            show_topper()
        elif choice == '7':
            show_class_average()
        elif choice == '8':
            print("Thank You!")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()