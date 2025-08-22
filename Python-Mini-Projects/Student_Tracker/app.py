import streamlit as st
from student import Student
from utils import log_function_call
from datetime import datetime

# Store students in session_state
if "students" not in st.session_state:
    st.session_state.students = []

@log_function_call
def add_student_ui():
    st.subheader("➕ Add Student")
    name = st.text_input("Name")
    roll = st.number_input("Roll Number", min_value=1, step=1)

    n = st.number_input("Number of Subjects", min_value=1, step=1)
    subject_marks = {}
    for i in range(int(n)):
        subject = st.text_input(f"Subject {i+1}")
        mark = st.number_input(f"Mark for {subject}", min_value=0, max_value=100, step=1, key=f"mark_{i}")
        if subject:
            subject_marks[subject] = mark

    if st.button("Add Student"):
        student = Student(name, roll)
        for subject, mark in subject_marks.items():
            student.add_mark(subject, mark)
        student.calculate_grade()
        st.session_state.students.append(student)
        st.success(f"✅ Added {name} (Roll {roll})")

@log_function_call
def mark_attendance_ui():
    st.subheader("📅 Mark Attendance")
    if not st.session_state.students:
        st.warning("No students available.")
        return

    student = st.selectbox("Select Student", st.session_state.students, format_func=lambda x: f"{x.name} (Roll {x.roll})")
    date = st.date_input("Date", datetime.now())
    present = st.radio("Status", ["Present", "Absent"])

    if st.button("Save Attendance"):
        student.add_attendance(date, present == "Present")
        st.success(f"✅ Attendance marked for {student.name} on {date}")

@log_function_call
def view_students_ui():
    st.subheader("📋 Student List")
    if not st.session_state.students:
        st.warning("No students available.")
        return
    for student in st.session_state.students:
        st.write(str(student))
        st.json({"Marks": student.marks, "Attendance": student.attendance})

# -------- Streamlit App Layout --------
st.title("🎓 Student Tracker (Streamlit)")

menu = st.sidebar.radio("Menu", ["Add Student", "Mark Attendance", "View Students"])

if menu == "Add Student":
    add_student_ui()
elif menu == "Mark Attendance":
    mark_attendance_ui()
elif menu == "View Students":
    view_students_ui()
