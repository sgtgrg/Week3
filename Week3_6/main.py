from database import create_tables
from yoobee_manager import (
    add_student, view_students, delete_student,
    add_lecturer, view_lecturers, delete_lecturer,
    add_course, view_courses, delete_course,
    add_class, view_classes, delete_class
)

def print_rows(rows):
    if not rows:
        print("(no rows)")
        return
    for r in rows:
        print(r)

def menu():
    print("\n==== Yoobee College DB ====")
    print("1.  Add Student")
    print("2.  View Students")
    print("3.  Delete Student")
    print("4.  Add Lecturer")
    print("5.  View Lecturers")
    print("6.  Delete Lecturer")
    print("7.  Add Course")
    print("8.  View Courses")
    print("9.  Delete Course")
    print("10. Add Class")
    print("11. View Classes")
    print("12. Delete Class")
    print("0.  Exit")

def main():
    create_tables()

    while True:
        menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            address = input("Student address: ").strip()
            add_student(name, address)

        elif choice == "2":
            print("\n--- Students ---")
            print_rows(view_students())

        elif choice == "3":
            try:
                sid = int(input("Student_ID to delete: "))
                delete_student(sid)
            except ValueError:
                print("Invalid ID.")

        elif choice == "4":
            name = input("Lecturer name: ").strip()
            email = input("Lecturer email (or leave blank): ").strip() or None
            add_lecturer(name, email)

        elif choice == "5":
            print("\n--- Lecturers ---")
            print_rows(view_lecturers())

        elif choice == "6":
            try:
                lid = int(input("Lecturer_ID to delete: "))
                delete_lecturer(lid)
            except ValueError:
                print("Invalid ID.")

        elif choice == "7":
            name = input("Course name: ").strip()
            dpt = input("Course department: ").strip()
            intake = input("Course intake (e.g., 2025-Feb): ").strip()
            add_course(name, dpt, intake)

        elif choice == "8":
            print("\n--- Courses ---")
            print_rows(view_courses())

        elif choice == "9":
            try:
                cid = int(input("Course_ID to delete: "))
                delete_course(cid)
            except ValueError:
                print("Invalid ID.")

        elif choice == "10":
            try:
                room_no_raw = input("Room No (or blank): ").strip()
                room_no = int(room_no_raw) if room_no_raw else None
            except ValueError:
                room_no = None

            schedule = input("Schedule (e.g., Mon 10-12) or blank: ").strip() or None

            course_id_raw = input("Course_ID (or blank for none): ").strip()
            course_id = int(course_id_raw) if course_id_raw else None

            lecturer_id_raw = input("Lecturer_ID (or blank for none): ").strip()
            lecturer_id = int(lecturer_id_raw) if lecturer_id_raw else None

            add_class(room_no, schedule, course_id, lecturer_id)

        elif choice == "11":
            print("\n--- Classes (joined) ---")
            print_rows(view_classes())

        elif choice == "12":
            try:
                class_id = int(input("Class_ID to delete: "))
                delete_class(class_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
