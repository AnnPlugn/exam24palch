original_dict = {(2, 4): 'a', (1, 11, 1): 'b', (2, 3): 'c'}
transformed_dict = {min(key): value for key, value in original_dict.items()}
print(transformed_dict)

""""Используя генератор словарей (и не используя код вне него) преобразовать словарь в
котором ключами являются кортежи из целых чисел в словарь в котором ключем
является минимальное значение из чисел исходного ключа, значение оставить
прежним. Пример: {(2,4):'a', (1,2,3):'b', (12,3):'c'} -> {2:'a', 1:'b', 2:'c'}"""""
