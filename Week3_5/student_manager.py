from database import create_connection

def add_student(name, address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (Stu_name, Stu_address) VALUES (?, ?)", (name, address))
    conn.commit()
    conn.close()
    print("Student added successfully.")

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_sample_students():
    conn = create_connection()
    cursor = conn.cursor()

    # Check if already inserted
    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("INSERT INTO students (Stu_name, Stu_address) VALUES (?, ?)", 
                       ("Alice", "123 Main Street"))
        cursor.execute("INSERT INTO students (Stu_name, Stu_address) VALUES (?, ?)", 
                       ("Bob", "456 Oak Avenue"))
        conn.commit()
        print("Sample students inserted.")
    else:
        print("Students table already has records.")

    conn.close()
