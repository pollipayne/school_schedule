from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, transportation):
        super().__init__(name, grade, classes = None)
        self.transportation = transportation
