def par_val(**kwargs):
    result = []
    for key, value in kwargs.items():
        if ' ' in value:
            result.append(key)
    return result

# Пример использования
print(par_val(pp='abba war', fan='oneword', zr='a x') )# ['pp', 'zr']

""""Реализовать функцию par_val, которая принимает на вход заранее неизвестное
количество именованных параметров (значения параметров - строки) и возвращает
список имен параметров, которым соответствуют строки, содержащие более двух
слов. Пример: par_val(pp='abba war', fan='oneword', zr='a x') -> [pp, zr]"""""
