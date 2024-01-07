import math
res = []
x = int(input())
for n in range(1,6):
    k = (-1)**(n+1)
    print(x)
    y = x**(2*n)
    print(y)
    res.append((k*y)/math.factorial(2*n))

print(res)
print(sum(res))
"""".Для произвольного значения x найти сумму первых пяти элементов убывающего ряда:
 """""