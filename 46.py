def cyclic_shift_words(sentence, shift):
    words = sentence.split()  # Разбиваем строку на список слов
    shifted_words = words[shift % len(words):] + words[:shift % len(words)]  # Выполняем циклический сдвиг
    shifted_sentence = ' '.join(shifted_words)  # Соединяем слова обратно в строку
    return shifted_sentence

# Пример использования
input_sentence = "один два три четыре пять шесть семь"
shift_amount = 3
result = cyclic_shift_words(input_sentence, shift_amount)
print(result)  # Вывод: "четыре пять шесть семь один два три"