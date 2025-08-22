from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import add_student, view_students, insert_sample_students

def menu():
    print("\n==== User & Student Manager ====")
    print("1. Add User")
    print("2. View All Users & Students")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Add Student")  # new option

def main():
    create_table()
    insert_sample_students()  # insert Alice & Bob once

    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)

        elif choice == '2':
            print("\n--- Users ---")
            users = view_users()
            for user in users:
                print(user)

            print("\n--- Students ---")
            students = view_students()
            for stu in students:
                print(stu)

        elif choice == '3':
            name = input("Enter user name to search: ")
            users = search_user(name)
            for user in users:
                print(user)

        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        elif choice == '5':
            print("Goodbye!")
            break

        elif choice == '6':  # add student
            stu_name = input("Enter student name: ")
            stu_address = input("Enter student address: ")
            add_student(stu_name, stu_address)

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
