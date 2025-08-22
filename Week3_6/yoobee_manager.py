from database import create_connection
import sqlite3

# ---------- Student ----------
def add_student(name: str, address: str):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Student (Student_name, Student_address) VALUES (?, ?)", (name, address))
    conn.commit()
    conn.close()
    print("Student added.")

def view_students():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_student(student_id: int):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Student WHERE Student_ID = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted (if existed).")

# ---------- Lecturer ----------
def add_lecturer(name: str, email: str | None):
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO Lecturer (Lecturer_name, Lecturer_email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Lecturer added.")
    except sqlite3.IntegrityError:
        print("Lecturer email must be unique.")
    finally:
        conn.close()

def view_lecturers():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Lecturer ORDER BY Lecturer_ID")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_lecturer(lecturer_id: int):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Lecturer WHERE Lecturer_ID = ?", (lecturer_id,))
    conn.commit()
    conn.close()
    print(" Lecturer deleted (if existed).")

# ---------- Course ----------
def add_course(name: str, dpt: str, intake: str):
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO Course (Course_name, Course_dpt, Intake) VALUES (?, ?, ?)",
                    (name, dpt, intake))
        conn.commit()
        print("Course added.")
    except sqlite3.IntegrityError:
        print("Course name must be unique.")
    finally:
        conn.close()

def view_courses():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Course ORDER BY Course_ID")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_course(course_id: int):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Course WHERE Course_ID = ?", (course_id,))
    conn.commit()
    conn.close()
    print("Course deleted (if existed).")

# ---------- Class ----------
def add_class(room_no: int | None, schedule: str | None, course_id: int | None, lecturer_id: int | None):
    """
    course_id and lecturer_id are optional (nullable). If provided,
    they must reference existing rows due to FK constraints.
    """
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO Class (Room_No, Schedule, Course_ID, Lecturer_ID)
            VALUES (?, ?, ?, ?)
        """, (room_no, schedule, course_id, lecturer_id))
        conn.commit()
        print("Class added.")
    except sqlite3.IntegrityError as e:
        print(f"Could not add class: {e}")
    finally:
        conn.close()

def view_classes():
    conn = create_connection()
    cur = conn.cursor()
    # Join to show Course and Lecturer info as well
    cur.execute("""
        SELECT
            c.Class_ID,
            c.Room_No,
            c.Schedule,
            c.Course_ID,
            co.Course_name,
            co.Course_dpt,
            co.Intake,
            c.Lecturer_ID,
            l.Lecturer_name
        FROM Class c
        LEFT JOIN Course co   ON c.Course_ID = co.Course_ID
        LEFT JOIN Lecturer l  ON c.Lecturer_ID = l.Lecturer_ID
        ORDER BY c.Class_ID
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_class(class_id: int):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Class WHERE Class_ID = ?", (class_id,))
    conn.commit()
    conn.close()
    print("Class deleted (if existed).")
