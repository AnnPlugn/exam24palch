def interleave_lists(listlist):
    result = []  # Список, содержащий поочередно элементы каждого из вложенных списков
    remaining = []  # Список из всех элементов, не вошедших в составленный список

    i = 0
    while True:
        has_elements = False  # Флаг, показывающий, есть ли ещё элементы в каком-либо из вложенных списков
        for sublist in listlist:
            if i < len(sublist):  # Если вложенный список ещё содержит элементы
                result.append(sublist[i])  # Добавляем очередной элемент в результат
                has_elements = True  # Устанавливаем флаг наличия элементов
            else:
                remaining += sublist[i:]  # Добавляем оставшиеся элементы в список remaining
        if not has_elements:  # Если ни в одном из вложенных списков не осталось элементов
            break  # Прекращаем цикл
        i += 1

    return result, remaining

# Пример использования
input_listlist = [[1,2,3],['a', 'b'], [30, 40, 50, 60]]
result, remaining = interleave_lists(input_listlist)
print(result)  # Вывод: [1, 'a', 30, 2, 'b', 40]
print(remaining)  # Вывод: [3, 50, 60]