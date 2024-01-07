import ast

# Чтение данных из файла
with open('data59.csv', 'r') as file:
    data = file.read()
    print(data)

# Десериализация данных из файла в Python объект
array = ast.literal_eval(data)
print(array)
# Сортировка чисел по возрастанию
numbers = sorted([x for x in array if isinstance(x, (int, float))])
non_numbers = [x for x in array if not isinstance(x, (int, float))]

# Объединение отсортированных чисел и нечисловых элементов
sorted_array = numbers + non_numbers

# Запись результирующего массива обратно в файл
with open('myfile.txt', 'w') as file:
    file.write(str(sorted_array))

# Вывод результата на экран
print(sorted_array)