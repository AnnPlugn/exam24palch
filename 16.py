original_string = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'
nested_list = [[char for char in word if char != ';' and char != '.' and char != ',' and char not in 'aeyuio'] for word in original_string.split()]  # Создаем вложенный список символов для каждого слова
print(nested_list)


""""Реализовать однонаправленный связанный список. Преобразовать строку 'Eeny,
meeny, miney, moe; Catch a tiger by his toe.' в связный список символов строки и
удалить из него все элементы содержащие гласные буквы."""""
