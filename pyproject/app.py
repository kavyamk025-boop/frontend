from student import Student, ResultManager


def get_valid_marks():
    while True:
        try:
            subjects = int(input("How many subjects? "))
            if subjects <= 0:
                print("Subjects must be greater than 0.")
                continue

            marks = {}
            for _ in range(subjects):
                subject = input("Subject name: ").strip()
                score = int(input("Marks (0-100): "))

                if score < 0 or score > 100:
                    raise ValueError("Marks must be between 0 and 100.")

                marks[subject] = score

            return marks

        except ValueError as e:
            print("Invalid input:", e)


def print_student(student):
    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Grade:", student["grade"])
    print("-" * 40)


def main():
    manager = ResultManager()

    while True:
        print("\n===== STUDENT RESULT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Show Topper")
        print("5. Show Rankings")
        print("6. Delete Student")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            marks = get_valid_marks()
            student = Student(name, marks)

            if manager.add_student(student):
                print("Student added successfully!")
            else:
                print("Student with this name already exists.")

        elif choice == "2":
            students = manager.view_students()
            if not students:
                print("No students found.")
            for s in students:
                print_student(s)

        elif choice == "3":
            name = input("Enter name to search: ")
            student = manager.search_student(name)
            if student:
                print_student(student)
            else:
                print("Student not found.")

        elif choice == "4":
            topper = manager.get_topper()
            if topper:
                print("\n🏆 Topper:")
                print_student(topper)
            else:
                print("No students available.")

        elif choice == "5":
            ranking = manager.rank_students()
            if not ranking:
                print("No students available.")
            else:
                print("\n📊 Rankings:")
                for i, s in enumerate(ranking, 1):
                    print(f"{i}. {s['name']} - {s['average']}")

        elif choice == "6":
            name = input("Enter student name to delete: ")
            if manager.delete_student(name):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "7":
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
