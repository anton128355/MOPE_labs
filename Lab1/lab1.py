import random
import numpy


print("""
Лабораторна робота 1 з МОПЕ
Варіант: 327 (min((Y - Yэт)^2))
Виконав: Яблоновський А.О
Перевірив: Регіда П.Г
""")

a = [2, 4, 6, 8]

x = [[random.randint(1, 20) for i in range(8)], 
	 [random.randint(1, 20) for i in range(8)], 
	 [random.randint(1, 20) for i in range(8)]]

x_matrix = numpy.array([x[0], x[1], x[2]])

Y = [a[0] + (a[1] * x[0][i]) + (a[2] * x[1][i]) + (a[3] * x[2][i]) for i in range(8)]

x0 = [(max(x[0]) + min(x[0])) / 2, 
	  (max(x[1]) + min(x[1])) / 2, 
	  (max(x[2]) + min(x[2])) / 2]

dx = [x0[0] - min(x[0]),
      x0[1] - min(x[1]), 
      x0[2] - min(x[2])]

xn = [[(x[0][i] - x0[0]) / dx[0] for i in range(8)],
	  [(x[1][i] - x0[1]) / dx[1] for i in range(8)],
	  [(x[2][i] - x0[2]) / dx[2] for i in range(8)]]

xn_matrix = numpy.array([xn[0], xn[1], xn[2]])

Yet = a[0] + (a[1] * x0[0]) + (a[1] * x0[1]) + (a[2] * x0[2])

result = min([(Y[i] - Yet) ** 2 for i in range(8)])

print("X1 X2 X3:" + "\n", x_matrix.transpose())
print("Y: ", Y)
print("x01, x02, x03: ", x0[0], x0[1], x0[2])
print("dx1, dx2, dx3: ", dx[0], dx[1], dx[2])
print("Xn1, Xn2, xn3:" + "\n", xn_matrix.transpose())
print("Yет:", Yet)

print("min((Y - Yэт)^2 = ", result)
