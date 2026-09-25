"""
Student Management System:

Stores student records (roll number, name, marks) in a CSV file and
provides CRUD operations:
    - Add a student
    - Delete a student (by roll number)
    - Search a student (by roll number or name)
    - Update marks
    - List all students
All changes are saved permanently back to the CSV file.
"""

import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["roll_no", "name", "marks"]


#File handling

def load_students():
    """Load all student records from the CSV file into a list of dicts."""
    students = []
    if not os.path.exists(CSV_FILE):
        return students

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                roll_no = int(row["roll_no"].strip())
            except (ValueError, TypeError):
                print(f"Skipping invalid row in CSV: {row}")
                continue

            students.append(
                {
                    "roll_no": roll_no,
                    "name": row["name"].strip(),
                    "marks": float(row["marks"]),
                }
            )
    return students


def save_students(students):
    """Write all student records permanently to the CSV file."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for student in students:
            writer.writerow(
                {
                    "roll_no": student["roll_no"],
                    "name": student["name"],
                    "marks": student["marks"],
                }
            )
    print(f"Changes saved to '{CSV_FILE}'.")


#CRUD operations

def read_roll_no(prompt):
    """Ask for a roll number and return it as an int, or None if invalid."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Roll Number must be a number.\n")
        return None


def add_student(students):
    """Add a new student record, then save the file."""
    roll_no = read_roll_no("Enter roll number: ")
    if roll_no is None:
        return

    if find_by_roll(students, roll_no):
        print(f"A student with roll number {roll_no} already exists.\n")
        return

    try:
        name = str(input("Enter student name: ").strip().title())
    except ValueError:
        print("Enterd Invalid name!")
        return
    
    if not name:
        print("Name cannot be empty.\n")
        return

    try:
        marks = float(input("Enter marks (0-100): ").strip())
    except ValueError:
        print("Marks must be a number.\n")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.\n")
        return

    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    save_students(students)
    print(f"Student '{name}' added successfully.\n")


def find_by_roll(students, roll_no):
    """Return the student dict matching a roll number, or None."""
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def delete_student(students):
    """Delete a student by roll number, then save the file."""
    roll_no = read_roll_no("Enter roll number to delete: ")
    if roll_no is None:
        return

    student = find_by_roll(students, roll_no)

    if student is None:
        print(f"No student found with roll number {roll_no}.\n")
        return

    students.remove(student)
    save_students(students)
    print(f"Student '{student['name']}' (roll {roll_no}) deleted.\n")


def search_student(students):
    """Search students by roll number or by name (partial match allowed)."""
    query = input("Enter roll number or name to search: ").strip()
    if not query:
        print("Search value cannot be empty.\n")
        return

    roll_no = int(query) if query.isdigit() else None
    matches = [
        student
        for student in students
        if student["roll_no"] == roll_no or query.lower() in student["name"].lower()
    ]

    if matches:
        print(f"\nFound {len(matches)} match(es):")
        print_records(matches)
    else:
        print(f"No student found matching '{query}'.\n")


def update_marks(students):
    """Update the marks of an existing student, then save the file."""
    roll_no = read_roll_no("Enter roll number to update: ")
    if roll_no is None:
        return

    student = find_by_roll(students, roll_no)

    if student is None:
        print(f"No student found with roll number {roll_no}.\n")
        return

    try:
        new_marks = float(input(f"Enter new marks for {student['name']}: ").strip())
    except ValueError:
        print("Marks must be a number.\n")
        return

    if not 0 <= new_marks <= 100:
        print("Marks must be between 0 and 100.\n")
        return

    student["marks"] = new_marks
    save_students(students)
    print(f"Marks updated for {student['name']}.\n")


def list_students(students):
    """Display all student records sorted by roll number."""
    if not students:
        print("No student records found.\n")
        return

    sorted_students = sorted(students, key=lambda s: s["roll_no"])
    print(f"\n--- All Students ({len(sorted_students)}) ---")
    print_records(sorted_students)


def print_records(records):
    """Print a table of student records."""
    print(f"{'Roll No':<10} {'Name':<20} {'Marks':>7} {'Grade':^7}")
    print("-" * 48)
    for student in records:
        print(
            f"{student['roll_no']:<10} "
            f"{student['name']:<20} "
            f"{student['marks']:>7.2f} "
            f"{grade_for(student['marks']):^7}"
        )
    print()


def grade_for(marks):
    """Return a letter grade for a marks value."""
    if marks >= 90:
        return "A+"
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


#Main menu

def main():
    students = load_students()
    print(f"Loaded {len(students)} student record(s) from '{CSV_FILE}'.")

    menu = (
        "\n===== Student Management System =====\n"
        "1. Add Student\n"
        "2. Delete Student\n"
        "3. Search Student\n"
        "4. Update Marks\n"
        "5. List All Students\n"
        "6. Save & Exit\n"
    )

    while True:
        print(menu)
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_marks(students)
        elif choice == "5":
            list_students(students)
        elif choice == "6":
            save_students(students)
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
