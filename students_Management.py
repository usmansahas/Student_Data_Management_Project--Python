"""
To Add,To Update,To Delete,To View & Exit
"""
students={}

def Add(name, marks):
    try:
        marks = float(marks)
        students[name] = marks
        print(f"{name} and {marks} were added")
    except ValueError:
        print("Please enter valid marks.")

def Update(name, marks):
    if name in students:
        try:
            marks = float(marks)
            students[name] = marks
            print(f"{marks} marks were updated to {name} ")
        except ValueError:
            print("Please enter valid marks.")
    else:
        print("Student not found. Please enter a valid name.")

def Delete(name):
    if name in students:
        del students[name]
        print(f"{name} was deleted.")
    else:
        print("Student not found. Please enter a valid name.")

def View():
    if students:
        print("\n--- Student Records ---")
        for name, marks in students.items():
            print(f"{name}: {marks}")
        print("------------------------\n")
    else:
        print("No students found.")

def main():
    while True:
        print("STUDENT DATA MANAGEMENT")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        try:
            choice = int(input("Select an option (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            Add(name, marks)

        elif choice == 2:
            name = input("Enter Name: ")
            marks = input("Enter New Marks: ")
            Update(name, marks)

        elif choice == 3:
            name = input("Enter Name: ")
            Delete(name)

        elif choice == 4:
            View()

        elif choice == 5:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose between 1 and 5.")
        print()

main()



