import math

# Лямбда-функция для вычисления радиуса по площади круга
radius_from_area = lambda area: math.sqrt(area / math.pi)

# Лямбда-функция для вычисления длины окружности по площади круга
circumference_from_area = lambda area: 2 * math.pi * math.sqrt(area / math.pi)

# Пример использования лямбда-функций
circle_area = int(input())
print(f"Радиус круга с площадью {circle_area}: {radius_from_area(circle_area)}")
print(f"Длина окружности круга с площадью {circle_area}: {circumference_from_area(circle_area)}")

"""".. Разработать лямбда-функции вычисления по известной площади круга его радиуса и
длины окружности.
 """""