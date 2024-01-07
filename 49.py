def process_lists(listlist):
    res = []
    for sublist in listlist:
        if len(sublist) > 3:  # Проверяем длину списка
            removed_elements = sublist[3:] # Сохраняем удаленные элементы
            sublist = sublist[:3]
            # Оставляем только первые три элемента
            sublist[2] += sum(removed_elements)
            res.append(sublist)# Прибавляем к третьему элементу сумму удаленных элементов
        else:
            res.append(sublist)
    return res

# Пример использования
input_listlist = [[1,2], [3,4,4,3,1], [4,1,4,5]]
result = process_lists(input_listlist)
print(result)  # Вывод: [[1, 2], [3, 4, 8], [4, 1, 9]]