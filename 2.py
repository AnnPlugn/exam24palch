lists = [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e']]
words = ', '.join(["".join(lst) for lst in lists])
print(words)

# OR
# s = [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m', 'o', 'e']]
# b = []
# for i in range(len(s)):
# b.append(''.join(s[i]))
# print(','.join(b))

"""""2. Из списка списков элементами которого являются текстовые символы собрать строку,
в которой вложенные списки объединены в слова, а слова через запятую объединены
в строку. Пример список вида [['E', 'e', 'n', 'y'], ['m', 'e', 'e', 'n', 'y'], ['m', 'i', 'n', 'e', 'y'], ['m',
'o', 'e']] будет преобразован в строку ‘Eeny,meeny,miney,moe’
"""""
