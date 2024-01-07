def repl(s, **kwargs):
    words = s.split()  # Разбиваем входную строку на слова
    for i, word in enumerate(words):
        if word in kwargs:  # Если слово является именем параметра
            words[i] = kwargs[word]  # Заменяем его на значение параметра
    return ' '.join(words)  # Объединяем слова обратно в строку и возвращаем результат

result = repl('replace my val abc', my='s1', abc='fff')
print(result)  # Выведет: 'replace s1 val fff'

""""Реализовать функцию repl, которая принимает на вход строку и набор заранее
неизвестных параметров. Результатом функции является строка, в которой слова
совпадающие с именами параметров заменены на значения параметров. Пример:
строка: 'replace my val abc', параметры my='s1', abc='fff' -> Результат: 'replace s1 val fff'
 """""
