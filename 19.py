def psort(**kwargs):
    sorted_params = [value for key, value in sorted(kwargs.items())]
    return sorted_params

# Пример использования
print(psort(c=21, a=22, ac=17, b=16))  # [22, 17, 16, 21]
# Пример использования

""""Реализовать функцию psort, которая принимает на вход набор заранее неизвестных
поименованных параметров. Функция возвращает список значений параметров
отсортированный по именам параметров. Пример: psort(c=21, a=22, ac=17, b=16) ->
[22, 17, 16, 21] """""
