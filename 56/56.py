import volume
import per
import pl

a = int(input("Длина параллелепипеда: "))
b = int(input("Ширина параллелепипеда: "))
c = int(input("Высота параллелепипеда: "))

print(f"Площадь параллелепипеда: {pl.pl(a,b,c)}")
print(f"Периметр сторон параллелепипеда: {per.per(a,b,c)}")
print(f"Объем параллелепипеда: {volume.vol(a,b,c)}")