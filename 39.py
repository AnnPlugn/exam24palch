def add_positive_numbers(a, b):
    assert a >= 0, "Первое число должно быть положительным"
    assert b >= 0, "Второе число должно быть положительным"
    return a + b


# Пример использования:
try:
    result = add_positive_numbers(5, 3)
    print(result)  # Вывод: 8
    result = add_positive_numbers(-2, 4)  # Здесь будет вызвано исключение AssertionError
except AssertionError as e:
    print("Ошибка:", e)