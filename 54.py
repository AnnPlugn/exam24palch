import math

# Функция, возвращающая кортеж (p, q)
def reduce_fraction_tuple(n, m):
    gcd = math.gcd(n, m)
    return (n // gcd, m // gcd)

# Функция, изменяющая список [n, m]
def reduce_fraction_list(fraction):
    n, m = fraction
    gcd = math.gcd(n, m)
    fraction[0] //= gcd
    fraction[1] //= gcd
    return fraction

# Использование функции, возвращающей кортеж
n, m = 12, 18
reduced_tuple = reduce_fraction_tuple(n, m)
print(reduced_tuple)  # Выведет (2, 3)

# Использование функции, изменяющей список
fraction_list = [12, 18]
reduce_fraction_list(fraction_list)
print(fraction_list)  # Выведет [2, 3]