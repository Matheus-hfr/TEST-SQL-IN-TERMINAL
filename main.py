from db_connection import create_connection, execute_query, insert_data, fetch_data, update_data, delete_data

def main():
    database = "educational_system.db"  # Name of the database file
    connection = create_connection(database)

    if connection:
        # Create the students table if it doesn't exist
        create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
        """
        execute_query(connection, create_students_table)

        while True:
            print("\n=== Student Management System ===")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student Age")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                insert_student_query = "INSERT INTO students (name, age) VALUES (?, ?);"
                insert_data(connection, insert_student_query, (name, age))

            elif choice == "2":
                select_students_query = "SELECT * FROM students;"
                students = fetch_data(connection, select_students_query)
                print("\n--- List of Students ---")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")

            elif choice == "3":
                name = input("Enter the name of the student to update: ")
                new_age = int(input("Enter the new age: "))
                update_student_query = "UPDATE students SET age = ? WHERE name = ?;"
                update_data(connection, update_student_query, (new_age, name))

            elif choice == "4":
                name = input("Enter the name of the student to delete: ")
                delete_student_query = "DELETE FROM students WHERE name = ?;"
                delete_data(connection, delete_student_query, (name,))

            elif choice == "5":
                connection.close()
                print("Connection closed successfully. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
