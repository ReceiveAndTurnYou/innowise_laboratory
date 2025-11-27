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

    except KeyError:
        print("Needed key not found")
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
                choice_grade = int(input(f"Enter grade for {student_name} [0,100]:"))

                if 0 <= choice_grade <= 100:
                    student["grades"].append(choice_grade)
                else:
                    print("type corrent number! [0-100]")
        else:
            print("No student was found with that name")

    except KeyError:
        print("Needed key not found")
    except ValueError:
        print("Enter a valid name or a number")


def show_students():
    print("Printing all students")
    print(students)

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
    elif(choice == CONST_MENU_ADDGRADES):
        add_student_grade()
    elif(choice ==CONST_MENU_SHOWREPORT):
        show_students()
    elif(choice==CONST_MENU_FINDTOPPERFORMER):
        print("")
    else: print("No such choice")
