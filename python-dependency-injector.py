from dependency_injector import containers, providers
import sys


class School:
    def __init__(self, school_name, city, board):
        self.school_name = school_name
        self.city = city
        self.board = board

    def get_school_name(self):
        print(f"name of school is: {self.school_name}")


class Student:
    def __init__(self, name, age, school):
        self.student_name = name
        self.student_age = age
        self.school = school

    def get_student_detail(self):
        print(f"Student Detail are here:"
              f"Name: {self.student_name}"
              f"School Name {self.school.school_name}")


class Container(containers.DeclarativeContainer):
    school = providers.Singleton(
        School
    )

    student = providers.Factory(
        Student
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    school = container.school("NDC", "Motejheel", "Dhaka")
    student = container.student("Manan Chakma", 23, school)
    student.get_student_detail()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
