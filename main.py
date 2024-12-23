class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_avg_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]  # Разворачиваем списки
        if all_grades:  # Проверяем, что список не пуст
            avg_grades = round(sum(all_grades) / len(all_grades), 1)
            return avg_grades
        else:
            return 0

    def __str__(self):
        return (
            f'Имя: {self.name}'
            f'\nФамилия: {self.surname}'
            f'\nСредняя оценка за домашние задания: {self.calculate_avg_grade()}'
            f'\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}'
            f'\nЗавершенные курсы: {', '.join(self.finished_courses)}\n'
        )

    def __eq__(self, other):
        return self.calculate_avg_grade() == other.calculate_avg_grade()

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __gt__(self, other):
        return self.calculate_avg_grade() > other.calculate_avg_grade()

    def __le__(self, other):
        return self.calculate_avg_grade() <= other.calculate_avg_grade()

    def __ge__(self, other):
        return self.calculate_avg_grade() >= other.calculate_avg_grade()

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(grade, int) and 1 <= grade <= 10:
            if (
                isinstance(lecturer, Lecturer)
                and
                course in self.courses_in_progress
                and
                course in lecturer.courses_attached
            ):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка может быть целым числом от 1 до 10'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_avg_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]  # Разворачиваем списки
        if all_grades:  # Проверяем, что список не пуст
            avg_grades = round(sum(all_grades) / len(all_grades), 1)
            return avg_grades
        else:
            return 0

    def __str__(self):
        return (
            f'Имя: {self.name}'
            f'\nФамилия: {self.surname}'
            f'\nСредняя оценка за лекции: {self.calculate_avg_grade()}\n'
        )

    def __eq__(self, other):
        return self.calculate_avg_grade() == other.calculate_avg_grade()

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __gt__(self, other):
        return self.calculate_avg_grade() > other.calculate_avg_grade()

    def __le__(self, other):
        return self.calculate_avg_grade() <= other.calculate_avg_grade()

    def __ge__(self, other):
        return self.calculate_avg_grade() >= other.calculate_avg_grade()


class Reviewer(Mentor):
    def __str__(self):
        return (
            f'Имя: {self.name}'
            f'\nФамилия: {self.surname}\n'
        )

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and
            course in self.courses_attached
            and
            course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Объекты класса Student
student_1 = Student('student_name_1', 'student_surname_1', 'student_gender_1')
student_1.courses_in_progress = ['course_1', 'course_2', 'course_3']
student_1.finished_courses = ['Python', 'Java', 'Ruby']

student_2 = Student('student_name_2', 'student_surname_2', 'student_gender_2')
student_2.courses_in_progress = ['course_1', 'course_2', 'course_3']
student_2.finished_courses = ['Python', 'Java', 'Ruby']

# Объекты класса Lecturer
lecturer_1 = Lecturer('lecturer_name_1', 'lecturer_surname_1')
lecturer_1.courses_attached = ['course_1', 'course_2']

lecturer_2 = Lecturer('lecturer_name_2', 'lecturer_surname_2')
lecturer_2.courses_attached = ['course_1', 'course_2']

# Объекты класса Reviewer
reviewer_1 = Reviewer('reviewer_name_1', 'reviewer_surname_1')
reviewer_1.courses_attached = ['course_1', 'course_2']

reviewer_2 = Reviewer('reviewer_name_2', 'reviewer_surname_2')
reviewer_2.courses_attached = ['course_1', 'course_2']

# Методы класса Student
student_1.rate_lectures(lecturer_1, 'course_1', 7)
student_1.rate_lectures(lecturer_1, 'course_2', 7)
student_1.rate_lectures(lecturer_2, 'course_1', 8)
student_1.rate_lectures(lecturer_2, 'course_2', 8)

student_2.rate_lectures(lecturer_1, 'course_1', 9)
student_2.rate_lectures(lecturer_1, 'course_2', 9)
student_2.rate_lectures(lecturer_2, 'course_1', 10)
student_2.rate_lectures(lecturer_2, 'course_2', 10)

# Методы класса Reviewer
reviewer_1.rate_hw(student_1, 'course_1', 7)
reviewer_1.rate_hw(student_1, 'course_2', 7)
reviewer_1.rate_hw(student_2, 'course_1', 9)
reviewer_1.rate_hw(student_2, 'course_2', 9)

reviewer_2.rate_hw(student_1, 'course_1', 9)
reviewer_2.rate_hw(student_1, 'course_2', 9)
reviewer_2.rate_hw(student_2, 'course_1', 10)
reviewer_2.rate_hw(student_2, 'course_2', 10)

# Вызов магических методов
print('\nВызов магических методов для объектов класса Student:')
print(student_1)
print(student_2)
print(student_1 == student_2)
print(student_1 > student_2)
print(student_1 >= student_2)
print(student_1 < student_2)
print(student_1 <= student_2)

print('\nВызов магических методов для объектов класса Lecturer:')
print(lecturer_1)
print(lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 >= lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 <= lecturer_2)

print('\nВызов магических методов для объектов класса Reviewer:')
print(reviewer_1)
print(reviewer_2)


# Методы для расчета среднего
def calculate_avg_grade_all_student(students_list, course):
    total = 0
    for student in students_list:
        if student.grades[course]:
            total += sum(student.grades[course]) / len(student.grades[course])
        else:
            return 0

    return total


def calculate_avg_grade_all_lecturer(lecturers_list, course):
    total = 0
    for lecturer in lecturers_list:
        if lecturer.grades[course]:
            total += sum(lecturer.grades[course]) / len(lecturer.grades[course])
        else:
            return 0

    return round(total, 1)


print(calculate_avg_grade_all_student([student_1, student_2], 'course_2'))
print(calculate_avg_grade_all_lecturer([lecturer_1, lecturer_2], 'course_2'))
