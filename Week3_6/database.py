import sqlite3

DB_NAME = "yoobee.db"

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def create_tables():
    conn = create_connection()
    cur = conn.cursor()

    # Student table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_name   TEXT NOT NULL,
            Student_address TEXT NOT NULL
        );
    """)

    # Lecturer table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Lecturer (
            Lecturer_ID    INTEGER PRIMARY KEY AUTOINCREMENT,
            Lecturer_name  TEXT NOT NULL,
            Lecturer_email TEXT UNIQUE
        );
    """)

    # Course table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            Course_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
            Course_name   TEXT NOT NULL UNIQUE,
            Course_dpt    TEXT NOT NULL,
            Intake        TEXT NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Class (
            Class_ID     INTEGER PRIMARY KEY AUTOINCREMENT,
            Room_No      INTEGER,
            Schedule     TEXT,
            Course_ID    INTEGER,
            Lecturer_ID  INTEGER,
            FOREIGN KEY (Course_ID)  REFERENCES Course(Course_ID)   ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID) ON DELETE SET NULL ON UPDATE CASCADE
        );
    """)

    conn.commit()
    conn.close()
