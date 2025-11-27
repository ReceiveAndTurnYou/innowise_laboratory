students = [] #list of dictionaries

def display_menu(): #function that displays user menu
    print("\t --- Student Grade Analyzer ---")
    print("\t 1. Add a new student")
    print("\t 2. Add a grades for a student")
    print("\t 3. Show report (all students)")
    print("\t 4. Find top performer")
    print("\t 5. Exit")

def add_student(): #function that adds new student
    try:
        student_name = input("Enter name of a new student:")

        student_name = student_name.title() # for beauty purposes

        #check if student with given name exists in students list of dictionaries
        has_even = any(student.get("name") == student_name for student in students)

        if has_even:
            print(f"Student with that name ({student_name}) already exists")
        else:
            student_dict = {
                "name": student_name,
                "grades": []
            }
            students.append(student_dict)

    except KeyError as e:
        print(f"Needed key {e} was not found")
    except ValueError:
        print("Not valid name")
        student_name=""

def add_student_grade():
    try:
        student_name = input("Enter student name:")
        student_name = student_name.title()

        exists = False
        for student in students:
            if student.get("name") == student_name:
                exists = True
                break

        if exists:

            choice_grade="!"
            while choice_grade != "done":
                print("Type 'done' when ready")
                choice_grade = int(input(f"Enter grade (or 'done' to finish) [0,100]:"))

                if 0 <= choice_grade <= 100:
                    student["grades"].append(choice_grade)
                else:
                    print("type corrent number! [0-100]")
        else:
            print("No student was found with that name")

    except KeyError as e:
        print(f"Needed key {e} was not found")
    except ValueError:
        print("Invalid input. Please enter a number")

def show_students():

    if not students:
        print("No students found")
        return
    try:

        student_with_grades = 0
        overall_average = 0
        max_average = None
        min_average = None
        total_average = 0

        for student in students:
            print(f"Student Name: {student['name']}")
            print(f"Student Grades: {student['grades']}")

            if student['grades']:

                grade_total = 0
                average = 0

                for grade in student['grades']:
                    grade_total+=grade

                average = grade_total/len(student['grades'])

                if max_average is None or average > max_average:
                    max_average = average
                    best_student = student['name']

                if min_average is None or average < min_average:
                    min_average = average
                    worst_student = student['name']

                total_average += average

                student_with_grades +=1

                print(f"{student['name']} average grade is: {average}")

            else:
                print("No grades were found")
                print("Average: N/A")

        if student_with_grades > 0:
            print(f"Max average: {max_average}")
            print(f"Min average: {min_average}")
            print(f"Overall average: {total_average/student_with_grades}")


    except KeyError as e:
        print(f"No {e} key was found")
    except ZeroDivisionError:
        print("Student has no grades")

#menu options
CONST_MENU_ADDSTUDENT = 1
CONST_MENU_ADDGRADES = 2
CONST_MENU_SHOWREPORT = 3
CONST_MENU_FINDTOPPERFORMER=4
CONST_MENU_EXIT = 5


choice = 0
while choice!=CONST_MENU_EXIT:
    display_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Incorrect choice!")
        choice = 0

    if choice == CONST_MENU_ADDSTUDENT:
        add_student()
    elif choice == CONST_MENU_ADDGRADES:
        add_student_grade()
    elif choice ==CONST_MENU_SHOWREPORT:
        show_students()
    elif choice==CONST_MENU_FINDTOPPERFORMER:
        print("")
    else: print("No such choice")
