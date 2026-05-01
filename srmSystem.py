MAX_STUDENTS = 100

# Function to add a student record
def add_record(records):
    if len(records) >= MAX_STUDENTS:
        print("Maximum number of students reached. Cannot add more records.")
        return
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    subjects = {}
    subjects_names = ["maths", "physics", "chemistry"]


    for subject in subjects_names:
        while True:
            try:
                grade = float(input(f"Enter Student Grade for {subject}: "))
                subjects[subject] = grade
                break
            except ValueError:
                print("Invalid grade. Please enter a number.")
                return

    records.append({"ID": student_id, "Name": name, "Subjects": subjects})
    print("Record added successfully!")

# Function to view all student records
def view_records(records):
    if not records:
        print("No records found.")
    else:
        print("\n--- Student Records ---")
        for student in records:
            print(f"ID: {student['ID']}, Name: {student['Name']}, Subjects and Grades: {student['Subjects']}")

# Function to calculate average grade
def calculate_average(records):
    if not records:
        print("No records to calculate.")
    else:
        total = sum(student["Grade"] for student in records)
        average = total / len(records)
        print(f"\nClass Average Grade: {average:.2f}")

# Function to display menu
def display_menu():
    print("\n--- Menu ---")
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Calculate Average Grade")
    print("4. Exit")

# Main program loop
def main():
    records = []  # list to store student records
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            calculate_average(records)
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()