class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rating(self):
        summ = 0
        count = 0
        for value in self.grades.values():
            summ += sum(value)
            count += len(value)

        if count == 0:
            return 0
        else:
            return round(summ / count, 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.__average_rating()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, student):
        if isinstance(student, Student):
            return self.__average_rating() == student.__average_rating()
        else:
            return 'Ошибка'

    def __lt__(self, student):
        if isinstance(student, Student):
            return self.__average_rating() < student.__average_rating()
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_rating(self):
        summ = 0
        count = 0
        for value in self.grades.values():
            summ += sum(value)
            count += len(value)
        if count == 0:
            return 0
        else:
            return round(summ / count, 1)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.__average_rating()}')

    def __eq__(self, lector):
        if isinstance(lector, Lecturer):
            return self.__average_rating() == lector.__average_rating()
        else:
            return 'Ошибка'

    def __lt__(self, lector):
        if isinstance(lector, Lecturer):
            return self.__average_rating() < lector.__average_rating()
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student1 = Student('Sergei', 'Kapustin', 'man')
student1.finished_courses += ['Вводный курс']
student1.courses_in_progress += ['Python', 'Java', 'CSS']
student2 = Student('Vasya', 'Pupkin', 'man')
student2.finished_courses += ['Вводный курс']
student2.courses_in_progress += ['Python', 'Java', 'CSS', 'HTML']
# print(student1.courses_in_progress, student1.finished_courses)
# print(student2.courses_in_progress, student1.finished_courses)

lecturer1 = Lecturer('John', 'Rambo')
lecturer1.courses_attached += ['Python', 'CSS', 'HTML']
lecturer2 = Lecturer('Jackie', 'Chan')
lecturer2.courses_attached += ['Java', 'CSS', 'HTML']
# print(lecturer1.courses_attached)
# print(lecturer2.courses_attached)

reviewer1 = Reviewer('Dolph', 'Lundgren')
reviewer1.courses_attached += ['Java', 'CSS']
reviewer2 = Reviewer('John', 'Travolta')
reviewer2.courses_attached += ['Python', 'HTML']
# print(reviewer1.courses_attached)
# print(reviewer2.courses_attached)

student1.rate_hw(lecturer1, 'Python', 8)
student1.rate_hw(lecturer2, 'Java', 8)
student2.rate_hw(lecturer1, 'CSS', 9)
student2.rate_hw(lecturer2, 'HTML', 7)

reviewer1.rate_hw(student1, 'Java', 10)
reviewer1.rate_hw(student2, 'CSS', 9)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'HTML', 7)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)
print()
print(student1 < student2)
print(student1 > student2)
print(student1 == student2)
print()
print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)


