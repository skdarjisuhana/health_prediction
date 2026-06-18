import sqlite3

def create_table():
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        dob TEXT,
        email TEXT,
        glucose REAL,
        haemoglobin REAL,
        cholesterol REAL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_patient(name, dob, email, glucose,
                haemoglobin, cholesterol, remarks):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (full_name,dob,email,glucose,haemoglobin,cholesterol,remarks)
    VALUES (?,?,?,?,?,?,?)
    """,
    (name,dob,email,glucose,
     haemoglobin,cholesterol,remarks))

    conn.commit()
    conn.close()


def view_patients():
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()
    conn.close()

    return rows


def delete_patient(id):
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()


def update_patient(id, remarks):
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients
    SET remarks=?
    WHERE id=?
    """,(remarks,id))

    conn.commit()
    conn.close()