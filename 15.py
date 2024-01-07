original_string = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'
nested_list = [[char for char in word if char != ';'] for word in original_string.split()]  # Создаем вложенный список символов для каждого слова
print(nested_list)


""""На основе строки, представляющей из себя предложение, построить вложенный
список, содержащий символы всех слов в предложении. Пример: строка 'Eeny, meeny,
miney, moe; Catch a tiger by his toe.' будет преобразована в: [['E', 'e', 'n', 'y'], ['m', 'e', 'e',
'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e'], ['C', 'a', 't', 'c', 'h'], ['a'], ['t', 'i', 'g', 'e', 'r'], ['b', 'y'], ['h',
'i', 's'], ['t', 'o', 'e']]"""""
