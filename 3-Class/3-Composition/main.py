class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        self.ID = Student.count;
        Student.count += 1

    def __str__(self):
        return "Name: {} \nID:{}".format(self.name, self.ID)


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def __str__(self):
        str = ""
        for student in self.students:
            str += student.__str__()
        return str

    def add_student(self, student):
        self.students.append(student)


if __name__ == '__main__':
    student_a = Student("Adam")
    student_y = Student("Yasser")

    s1 = School("Salam")
    s1.add_student(student_a)
    print(s1)
    s1.students[0].name = "Ad"

    print(s1)
    print(student_a)
