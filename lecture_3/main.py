
def display_menu(): #function that displays user menu
    print("\t 1. Add a new student")
    print("\t 2. Add a grades for a student")
    print("\t 3. Show report (all students)")
    print("\t 4. Find top performer")
    print("\t 5. Exit")

CONST_MENU_EXIT = 5

students = [] #list of dictionaries

choice = 0
while choice!=CONST_MENU_EXIT:
    display_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Incorrect choice!")
        choice = 0

    