import random
import numpy


print("""
Лабораторна робота 1 з МОПЕ
Варіант: 327 (min((Y - Yэт)^2))
Виконав: Яблоновський А.О
Перевірив: Регіда П.Г
""")

a0, a1, a2, a3 = 2, 4, 6, 8

x1, x2, x3 = [random.randint(1, 20) for i in range(8)], [random.randint(1, 20) for i in range(8)], [random.randint(1, 20) for i in range(8)]

x_matrix = numpy.array([x1, x2, x3])

Y = [a0 + (a1 * x1[i]) + (a2 * x2[i]) + (a3 * x3[i]) for i in range(8)]

x01, x02, x03 = (max(x1) + min(x1)) / 2, (max(x2) + min(x2)) / 2, (max(x3) + min(x3)) / 2

dx1, dx2, dx3 = x01 - min(x1), x02 - min(x2), x03 - min(x3)

xn1, xn2, xn3 = [(x1[i] - x01) / dx1 for i in range(8)], [(x2[i] - x02) / dx2 for i in range(8)], [(x3[i] - x03) / dx3 for i in range(8)]

xn_matrix = numpy.array([xn1, xn2, xn3])

Yet = a0 + (a1 * x01) + (a2 * x02) + (a3 * x03)

result = min([(Y[i] - Yet) ** 2 for i in range(8)])

print("X1 X2 X3:" + "\n", x_matrix.transpose())
print("Y: ", Y)
print("x01, x02, x03: ", x01, x02, x03)
print("dx1, dx2, dx3: ", dx1, dx2, dx3)
print("Xn1, Xn2, xn3:" + "\n", xn_matrix.transpose())
print("Yет:", Yet)

print(result)
