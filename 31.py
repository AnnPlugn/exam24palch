import math

A = [float(i) for i in range(int(-math.pi), int(math.pi), 1)]
B = [float(2*math.sin(j)) for j in A]
C = [float(math.cos(2*j)) for j in A]
print(A)
print(B)
print(C)
"""".С помощью генератора создать в цикле список значений х от -π до +π (с небольшим
произвольным шагом). Для заданного списка рассчитать значения функций 𝑦1 =
2𝑠𝑖𝑛𝑥 и 𝑦2 = 𝑐𝑜𝑠2𝑥.
 """""