class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course_in_progress(self, course):
        self.courses_in_progress.append(course)

    def add_finished_course(self, course):
        self.finished_courses.append(course)

    def avg_grade(self):
        grades_sum = 0
        grades_count = 0
        for course_grades in self.grades.values():
            grades_count += len(course_grades)
            for course_grade in course_grades:
                grades_sum += course_grade
        return round(grades_sum / grades_count, 1)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Используйте 10-балльную систему')
                return
        else:
            return 'Ошибка'

    def __str__(self):
        str_courses_in_progress = ', '.join(self.courses_in_progress)
        str_finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.avg_grade()} \n' \
               f'Курсы в процессе изучения: {str_courses_in_progress} \n' \
               f'Завершенные курсы: {str_finished_courses} \n'

    def __lt__(self, another):
        if not (isinstance(self, Student) and isinstance(another, Student)):
            return 'Укажите учеников'
        if self.avg_grade() > another.avg_grade():
            return f'Cредняя оценка выше у лектора: {self.name} {self.surname}'
        else:
            return f'Cредняя оценка выше у лектора: {another.name} {another.surname}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course_attached(self, course):
        self.courses_attached.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def add_course_attached(self, course):
        self.courses_attached.append(course)

    def avg_grade(self):
        grades_sum = 0
        grades_count = 0
        for course_grades in self.grades.values():
            grades_count += len(course_grades)
            for course_grade in course_grades:
                grades_sum += course_grade
        return round(grades_sum / grades_count, 1)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.avg_grade()}'

    def __lt__(self, another):
        if not (isinstance(self, Lecturer) and isinstance(another, Lecturer)):
            return 'Укажите лекторов'
        if self.avg_grade() > another.avg_grade():
            return f'Cредняя оценка выше у лектора: {self.name} {self.surname}'
        else:
            return f'Cредняя оценка выше у лектора: {another.name} {another.surname}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def add_course_attached(self, course):
        self.courses_attached.append(course)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print('Используйте 10-балльную систему')
                return
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}'


# Reviewers:
first_reviewer = Reviewer('Petr', 'Petrov')
first_reviewer.add_course_attached('Python')
first_reviewer.add_course_attached('Git')
second_reviewer = Reviewer('Inna', 'Petrova')
second_reviewer.add_course_attached('Python')
second_reviewer.add_course_attached('Git')

# Students:
first_student = Student('Ivan', 'Ivanov', 'male')
first_student.add_finished_course('Введение в программирование')
first_student.add_course_in_progress('Python')
first_student.add_course_in_progress('Git')
second_student = Student('Olesya', 'Ivanova', 'female')
second_student.add_finished_course('Введение в программирование')
second_student.add_course_in_progress('Python')
second_student.add_course_in_progress('Git')

# Lecturers:
first_lecturer = Lecturer('Petr', 'Petrov')
first_lecturer.add_course_attached('Python')
first_lecturer.add_course_attached('Git')
second_lecturer = Lecturer('Inna', 'Petrova')
second_lecturer.add_course_attached('Python')
second_lecturer.add_course_attached('Git')

# Reviewers rate_hw Students:
first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Git', 6)
first_reviewer.rate_hw(first_student, 'Git', 3)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Git', 9)
first_reviewer.rate_hw(second_student, 'Git', 5)
second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Git', 10)
second_reviewer.rate_hw(first_student, 'Git', 6)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Git', 9)
second_reviewer.rate_hw(second_student, 'Git', 5)
print('----Проверка на баг при оценке----')
first_reviewer.rate_hw(first_student, 'Python', 11)
print('----------------------------------')

# Students rate_hw Lecturers:
first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(first_lecturer, 'Python', 4)
first_student.rate_hw(first_lecturer, 'Git', 5)
first_student.rate_hw(first_lecturer, 'Git', 6)
first_student.rate_hw(second_lecturer, 'Python', 7)
first_student.rate_hw(second_lecturer, 'Python', 10)
first_student.rate_hw(second_lecturer, 'Git', 9)
first_student.rate_hw(second_lecturer, 'Git', 5)
second_student.rate_hw(first_lecturer, 'Python', 6)
second_student.rate_hw(first_lecturer, 'Python', 5)
second_student.rate_hw(first_lecturer, 'Git', 9)
second_student.rate_hw(first_lecturer, 'Git', 6)
second_student.rate_hw(second_lecturer, 'Python', 9)
second_student.rate_hw(second_lecturer, 'Python', 7)
second_student.rate_hw(second_lecturer, 'Git', 9)
second_student.rate_hw(second_lecturer, 'Git', 5)
print('----Проверка на баг при оценке----')
first_student.rate_hw(first_lecturer, 'Python', 11)
print('----------------------------------')

# avg_grade
print(first_student.avg_grade())
print(second_student.avg_grade())
print(first_lecturer.avg_grade())
print(second_lecturer.avg_grade())
print('-----------------------')

# __str__
print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print('-----------------------')

# __lt__
print(first_student > second_student)
print(first_lecturer < second_lecturer)
print('----Проверка на баг при сравнении----')
print(first_lecturer < second_student)
print(first_student < second_lecturer)
print('-------------------------------------')

students_list = [first_student, second_student]
lecturers_list = [first_lecturer, second_lecturer]


def avg_course_students_grade(students, course):
    grades_sum = 0
    grades_count = 0
    for student in students:
        for student_course, grades_list in student.grades.items():
            if student_course == course:
                grades_sum += sum(grades_list)
                grades_count += len(grades_list)
    return round(grades_sum / grades_count, 1)


def avg_course_lecturers_grade(lecturers, course):
    grades_sum = 0
    grades_count = 0
    for lecturer in lecturers:
        for lecturer_course, grades_list in lecturer.grades.items():
            if lecturer_course == course:
                grades_sum += sum(grades_list)
                grades_count += len(grades_list)
    return round(grades_sum / grades_count, 1)


print(avg_course_students_grade(students_list, 'Git'))
print(avg_course_lecturers_grade(lecturers_list, 'Python'))
