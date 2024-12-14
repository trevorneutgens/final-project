
import sqlite3


# this function initializes the SQLite database
def create_student_database():


    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    # the code below (lines 11-21) creates the students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        dob TEXT NOT NULL,
        major TEXT NOT NULL,
        gpa REAL NOT NULL,
        phone_number TEXT NOT NULL
    )
    ''')


    # list that contains our data (data is not accurate)
    predefined_students = [
        ("1", "Trevor", "Neutgens", "03-12-2007", "Undecided", 3.9, "763-234-5678"),
        ("2", "Caiden", "Nelson", "11-22-2006", "Electrical Engineering", 3.8, "555-234-5678")
    ]


    # add us to the database
    for student in predefined_students:
        cursor.execute('''
        INSERT OR IGNORE INTO students (student_id, first_name, last_name, dob, major, gpa, phone_number)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', student)


    # always commit changes and close the connection
    conn.commit()
    conn.close()


# this function displays all student records currently in the students.db
def display_records():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()


    if not rows:
        print("No records found.")
    else:
        print("\nStudent ID\tFirst Name\tLast Name\tDate of Birth\tMajor\tGPA\tPhone #")
        print("-" * 80)
        for row in rows:
            print("\t".join(map(str, row)))


    conn.close()


# this function adds a new student record
def add_student():
    student_id = input("Enter student ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    dob = input("Enter date of birth (MM-DD-YYYY): ")
    major = input("Enter major: ")
    gpa = input("Enter gpa: ")
    phone_number = input("Enter phone number (xxx-xxx-xxxx): ")


    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    # check if student ID already exists to prevent duplicates
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    if cursor.fetchone():
        print(f"Student ID {student_id} already exists. Try again with a different ID.")
        conn.close()
        return


    cursor.execute('''
    INSERT INTO students (student_id, first_name, last_name, dob, major, gpa, phone_number)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (student_id, first_name, last_name, dob, major, gpa, phone_number))


    conn.commit()
    conn.close()
    print("Student record added.")


# this function updates an existing student record
def update_student():

    student_id = input("Enter the student ID of the student you wish to update: ")


    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()


    if not student:
        print("Student ID not found.")
        conn.close()
        return


    print(f"Current record associated with that ID: {student}")
    field = input(
        "Which field do you wish to update? (first_name, last_name, dob, major, gpa, phone_number): ").lower()


    if field == "first_name":
        new_value = input("Enter new first Name: ")
        cursor.execute("UPDATE students SET first_name = ? WHERE student_id = ?", (new_value, student_id))
    elif field == "last_name":
        new_value = input("Enter new last Name: ")
        cursor.execute("UPDATE students SET last_name = ? WHERE student_id = ?", (new_value, student_id))
    elif field == "dob":
        new_value = input("Enter new date of birth (MM-DD-YYYY): ")
        cursor.execute("UPDATE students SET dob = ? WHERE student_id = ?", (new_value, student_id))
    elif field == "major":
        new_value = input("Enter new major: ")
        cursor.execute("UPDATE students SET major = ? WHERE student_id = ?", (new_value, student_id))
    elif field == "gpa":
        new_value = input("Enter new gpa: ")
        cursor.execute("UPDATE students SET gpa = ? WHERE student_id = ?", (new_value, student_id))
    elif field == "phone_number":
        new_value = input("Enter new phone number (xxx-xxx-xxxx): ")
        cursor.execute("UPDATE students SET phone_number = ? WHERE student_id = ?", (new_value, student_id))
    else:
        print("The field you have chosen to update is spelt incorrectly or does not exist.")
        conn.close()
        return


    conn.commit()
    conn.close()
    print("Student record updated.")


# this function deletes a student record
def delete_student():
    student_id = input("Enter the student ID of the student you wish to delete: ")


    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()


    if not student:
        print("That student ID does not exist.")
        conn.close()
        return


    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("Student record deleted.")


# this function displays the options a user is given when running our program
def display_menu():
    print("\nMenu Options:")
    print("1. Display student records")
    print("2. Add a new student record")
    print("3. Update an existing student record")
    print("4. Delete a student record")
    print("5. Exit")


# main function
def main():
    # initialize the database with us so that there are a couple students already in the database
    create_student_database()


    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_records()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Program ended.")
            break
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()
