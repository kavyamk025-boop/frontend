import json
import os

FILE_NAME = "students.json"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total = sum(marks.values())
        self.average = round(self.total / len(marks), 2)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 75:
            return "B"
        elif self.average >= 60:
            return "C"
        else:
            return "D"

    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks,
            "total": self.total,
            "average": self.average,
            "grade": self.grade
        }


class ResultManager:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(FILE_NAME):
            return []

        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_students(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        # prevent duplicate names
        for s in self.students:
            if s["name"].lower() == student.name.lower():
                return False

        self.students.append(student.to_dict())
        self.save_students()
        return True

    def view_students(self):
        return self.students

    def get_topper(self):
        if not self.students:
            return None
        return max(self.students, key=lambda x: x["average"])

    def rank_students(self):
        return sorted(self.students, key=lambda x: x["average"], reverse=True)

    def delete_student(self, name):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s["name"].lower() != name.lower()]
        self.save_students()
        return len(self.students) < initial_count

    def search_student(self, name):
        for s in self.students:
            if s["name"].lower() == name.lower():
                return s
        return None
