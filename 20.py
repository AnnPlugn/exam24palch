def psort(**kwargs):
    sorted_params = [key for key, value in sorted(kwargs.items(), key=lambda item: item[1])]
    return sorted_params

# Пример использования
print(psort(c=21, a=22, ac=17, b=16))  # ['b', 'ac', 'c', 'a']

""""Реализовать функцию psort, которая принимает на вход набор заранее неизвестных
поименованных параметров. Функция возвращает список имен параметров,
отсортированный по значениям параметров. Пример: psort(c=21, a=22, ac=17, b=16) -
> [b, ac, c, a] """""
