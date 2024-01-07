import matplotlib.pyplot as plt

# Ввод координат точки
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Определение четверти
if x > 0 and y > 0:
    print("Точка принадлежит первой четверти")
    quarter = 1
elif x < 0 and y > 0:
    print("Точка принадлежит второй четверти")
    quarter = 2
elif x < 0 and y < 0:
    print("Точка принадлежит третьей четверти")
    quarter = 3
elif x > 0 and y < 0:
    print("Точка принадлежит четвертой четверти")
    quarter = 4
else:
    print("Точка лежит на одной из осей")
    quarter = 0

# Расчет расстояния от точки до начала координат
distance = (x**2 + y**2)**0.5

# Вывод результата
print(f"Произведение номера четверти ({quarter}) на расстояние от точки до начала координат ({distance}) равно {quarter * distance}")

# Визуализация точки
plt.scatter(x, y, color='red')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.text(x, y, f'({x}, {y})', verticalalignment='bottom', horizontalalignment='right')
plt.show()
"""". Пользователь поочередно вводит координаты точки в декартовой системе координат.
Определить, какой четверти принадлежит данная точка или на какой оси она
находится. Расположение точки вывести на экран. Найти произведение номера
четверти на расстояние от этой точки до начала координат и вывести его на экран.
Если точка лежит на оси, считать, что номер четверти равен 0.
 """""