s = 'abcd'
transformed_list = [char * (i+1) for i, char in enumerate(s)]
print(transformed_list)


"""". Используя генератор списков (и не используя код вне него) преобразовать строку по
следующей логике: для каждого символа исходной строки создать в итоговом списке
строку, содержащую копии символа в количестве, равном номеру символа в исходной
строки. Пример: 'abcd' -> ['a', 'bb', 'ccc', 'dddd']"""""
