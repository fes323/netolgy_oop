def avr_lecturer_grades(lecturer_list, course_name):
    all_grades = 0
    all_counter = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            all_grades += lect.avg_grades
            all_counter += 1
    return all_grades / all_counter

def avr_student_grades(student_list, course_name):
    all_grades = 0
    all_counter = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            all_grades += stud.avg_grades
            all_counter += 1
    return all_grades / all_counter

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades = int()

    def __str__(self):
        grades_count = sum(len(self.grades[k]) for k in self.grades)
        self.avg_grades = sum(map(sum, self.grades.values())) / grades_count
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Пол: {self.gender}\n' f'Средняя оценка дз: {self.avg_grades}\n' f'Курсы в процессе обучения: {courses_in_progress_string}\n' f'Завершенные курсы: {finished_courses_string}'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Невозможно сравнить')
            return
        return self.avg_grades < other.avg_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.avg_grades = int()
        self.grades = {}

    def __str__(self):
        grades_count = sum(len(self.grades[k]) for k in self.grades)
        self.avg_grades = sum(map(sum, self.grades.values())) / grades_count
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Невозможно сравнить')
            return
        return self.avg_grades < other.avg_grades

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_lecturer_1 = Lecturer('Иван', 'Иванов')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Кирилл', 'Кириллов')
best_lecturer_2.courses_attached += ['go']
lecturer_list = [best_lecturer_1, best_lecturer_2]

cool_reviewer_1 = Reviewer('Михаил', 'Михайлов')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['go']

cool_reviewer_2 = Reviewer('Афанасий', 'Афанасьев')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['go']

student_1 = Student('Игорь', 'Иванова', 'м')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['go']

student_2 = Student('Алексей', 'Алёшин', "М")
student_2.courses_in_progress += ['go']
student_2.finished_courses += ['go']

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 1)
student_1.rate_hw(best_lecturer_2, 'Python', 2)
student_1.rate_hw(best_lecturer_2, 'Python', 3)

student_2.rate_hw(best_lecturer_2, 'go', 1)
student_2.rate_hw(best_lecturer_2, 'go', 5)
student_2.rate_hw(best_lecturer_2, 'go', 10)

student_list = [student_1, student_2]

cool_reviewer_1.rate_hw(student_1, 'Python', 10)
cool_reviewer_1.rate_hw(student_1, 'Python', 2)
cool_reviewer_1.rate_hw(student_1, 'Python', 5)

cool_reviewer_2.rate_hw(student_2, 'go', 5)
cool_reviewer_2.rate_hw(student_2, 'go', 5)
cool_reviewer_2.rate_hw(student_2, 'go', 7)

print(f'\nСтуденты:\n{student_1}\n{student_2}')
print(f'\nЛекторы::\n{best_lecturer_1}\n{best_lecturer_2}')
print(f'\nСреднии оценки дз: {student_1.name} {student_1.surname} < {student_2.name} {student_2.surname}')
print(f'\nСреднии оценки лекции: {best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname}')
print(f"\nСредняя оценка студентов, курс {'Python'}: {avr_student_grades(student_list, 'Python')}")
print(f"\nСредняя оценка лекторов, курс: {'Python'}: {avr_lecturer_grades(lecturer_list, 'Python')}")
print(f"\nСредняя оценка студентов, курс {'go'}: {avr_student_grades(student_list, 'go')}")
print(f"\nСредняя оценка лекторов, курс: {'go'}: {avr_lecturer_grades(lecturer_list, 'go')}")