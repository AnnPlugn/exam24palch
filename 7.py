original_dict = {(2, 4): 'a', (1, 11, 1): 'b', (2, 3): 'c'}
transformed_dict = {max(key): value for key, value in original_dict.items()}
print(transformed_dict)

""""7. Используя генератор словарей (и не используя код вне него) преобразовать словарь в
котором ключами являются кортежи из целых чисел в словарь в котором ключом
является максимальное значение из чисел исходного ключа, значение оставить
прежним. Пример: {(2,4):'a', (1,11,1):'b', (2,3):'c'} -> {4:'a', 11:'b', 3:'c'}"""""
