import csv

import random

# Генерация тестовых данных
data = [
    {'Id': 1, 'First Name': 'Иван', 'Last Name': 'Иванов', 'Age': 25, 'Phone': '123-456'},
    {'Id': 2, 'First Name': 'Петр', 'Last Name': 'Петров', 'Age': 30, 'Phone': '789-012'},
    {'Id': 3, 'First Name': 'Алексей', 'Last Name': 'Сидоров', 'Age': 28, 'Phone': '345-678'},
    # Добавьте больше данных по вашему усмотрению
]

# Запись данных в CSV-файл
file_path = 'data37.csv'
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Id', 'First Name', 'Last Name', 'Age', 'Phone'])
    writer.writeheader()
    writer.writerows(data)

print(f"Тестовый CSV-файл создан: {file_path}")
def find_by_name(file_path, *names):
    result = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for name in names:
                if name in row['First Name']:
                    result.append([row['Id'], row['First Name'], row['Last Name'], row['Age'], row['Phone']])
    return result

# Пример использования функции
file_path = 'data37.csv'  # Путь к вашему CSV-файлу
result = find_by_name(file_path, 'Иван', 'Петр')
for row in result:
    print(row)

"""". Реализовать функцию find_by_name, в которую можно передать произвольное
количество параметров, в результате функция вернет данные (в виде списка списков)
только по людям, у которых в столбце 'First Name' содержатся указанные имена.
Заголовок csv-файла выглядит следующим образом: Id, First Name, Last Name, Age,
Phone"""""
