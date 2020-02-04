# students = []

# def get_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titlecase.append(student["name"].title())
#     return students_titlecase

# def print_student_tc():
#     students_tc = get_students_titlecase()
#     print(students_tc) 


# def add_student(name, student_id=322):
#     student = {"name": name, "student_id": student_id}
#     students.append(student)


# def save_file(student):
#     try:
#         f = open("students.txt", "a")  #<- access mode "w" - writing, "r" - reading, "a" - appending, "rb" - reading a binary file, "wb" - writing a binary file
#         f.write(student + "\n")
#         f.close()
#     except Exception:
#         print("Could not save file")


# def read_file():
#     try:
#         f = open("students.txt", "r")
#         for student in f.readlines():
#             add_student(student)
#         f.close()
#     except Exception:
#         print("Could not read file")


# read_file()
# print_student_tc()

# student_name = input("Enter student name: ")
# student_id = input("Enter student ID: ")

# add_student(student_name, student_id)
# save_file(student_name)

students = []

class Student:

    school_name = "Springfield Elementary"


    def __init__(self, name, lastname, student_id=322):
        self.name = name
        self.lastname = lastname
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name + " " + self.lastname

    def get_name_caps(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
        


