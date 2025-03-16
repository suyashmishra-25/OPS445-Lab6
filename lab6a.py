#!/usr/bin/env python3

# Author ID: SMISHRA27 / 137285227

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure student number is stored as a string
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            return f'GPA of student {self.name} is 0.0'

        total_grades = sum(self.courses.values())
        num_courses = len([grade for grade in self.courses.values() if grade > 0.0])

        return f'GPA of student {self.name} is {total_grades / max(num_courses, 1)}'

    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    student1 = Student('John', 13454900)
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
