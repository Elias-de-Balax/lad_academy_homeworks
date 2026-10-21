"""5. Словарь с defaultdict. Дан список кортежей [(имя, предмет, оценка), ...]. Используя defaultdict(list),
    сгруппируйте оценки по именам студентов, а затем через defaultdict(list) или Counter выведите для каждого студента
    список его предметов и средний балл. (Подумайте: как посчитать средний балл, имея список оценок?)"""

from collections import defaultdict

student_list = [("Иван", "Математика", 5),
                ("Максим", "Математика", 3),
                ("Максим", "Физика", 4),
                ("Василий", "Физика", 5),
                ("Иван", "Химия", 4)]

student_groups1 = defaultdict(list)
student_groups2 = defaultdict(list)
for student in student_list:
    student_groups1[student[0]].append(student[2])
    student_groups2[student[0]].append(student[1])

new_list = {key: (value, student_groups1.get(key, [])) for key, value in student_groups2.items()}

#print(student_groups1)
#print(student_groups2)
#print()

for key, value in new_list.items():
    print(f"{key}: предметы: {value[0]}, средний балл: {round(sum(value[1])/len(value[1]), 2) if value[1] else 0}")



