from datetime import datetime

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = {}
        self.attendance = {}
        self.grade = None

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def calculate_grade(self):
        if not self.marks:
            self.grade = "N/A"
        else:
            avg = sum(self.marks.values()) / len(self.marks)
            if avg >= 90:
                self.grade = "A"
            elif avg >= 75:
                self.grade = "B"
            elif avg >= 50:
                self.grade = "C"
            else:
                self.grade = "F"
        return self.grade

    def add_attendance(self, date, present: bool):
        if isinstance(date, datetime):
            date = date.date()
        self.attendance[str(date)] = "Present" if present else "Absent"

    def __str__(self):
        return f"{self.name} (Roll {self.roll}) | Grade: {self.grade}"
