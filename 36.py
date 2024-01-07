# Создаем словарь для хранения результатов группы
group_results = {}


# Функция для вычисления среднего балла
def average_score(scores):
    return sum(scores) / len(scores)


# Заполняем словарь результатами студентов
group_results["Иванов"] = [4, 5, 3]
group_results["Петров"] = [5, 4, 4]
group_results["Сидоров"] = [3, 3, 2]

# Выводим таблицу с результатами экзаменов
print("Фамилия\t\tИстория\tМатематика\tИнформатика")
for student, scores in group_results.items():
    print(f"{student}\t\t{scores[0]}\t\t{scores[1]}\t\t{scores[2]}")

# Вычисляем средний балл по каждой дисциплине
history_scores = [scores[0] for scores in group_results.values()]
math_scores = [scores[1] for scores in group_results.values()]
informatics_scores = [scores[2] for scores in group_results.values()]

print(f"Средний балл по Истории: {average_score(history_scores)}")
print(f"Средний балл по Математике: {average_score(math_scores)}")
print(f"Средний балл по Информатике: {average_score(informatics_scores)}")

# Вычисляем средний балл для каждого студента
for student, scores in group_results.items():
    print(f"Средний балл для {student}: {average_score(scores)}")

"""". Результат сессии, состоящей из 3 экзаменов (История, Математика, Информатика),
для студента задается в виде списка, содержащего фамилию студента и 3 оценки по
пятибалльной системе (0-неявка, 2-неудовл., 3-удовл., 4-хорошо, 5-отлично).
Результаты группы сохраняются в виде словаря. Для группы выведите на экран:
таблицу с результатами экзаменов; средний балл по каждой дисциплин; средний балл
для каждого студента."""""
