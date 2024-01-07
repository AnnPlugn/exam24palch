s = 'SIX,SEVEN,EIGHT,NINE,TEN'
words = s.split(',')
result = ','.join(filter(lambda x: words.index(x) % 2 == 0, words))
print(result)

"""1. В строке содержащей последовательность слов, разделенных запятыми удалить все
нечетные слова. Ответ представить в виде строки. Пример: строка
 'SIX,SEVEN,EIGHT,NINE,TEN' будет преобразована в: 'SIX,EIGHT,TEN'."""