from collections import defaultdict

class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        sorted_students = [sorted(self.students[key]) for key in sorted(self.students.keys())]
        return [name for names in sorted_students for name in names]

    def grade(self, grade_number):
        if grade_number not in self.students.keys():
            return list()

        return sorted([students for grade, students in self.students.items() if grade == grade_number][0])