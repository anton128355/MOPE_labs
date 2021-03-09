import numpy as np
import random
from numpy.linalg import solve

print("""Лабораторна робота 3 з МОПЕ
Варіант: 327
Виконав: Яблоновський А.О
Перевірив: Регіда П.Г """)

x_range = [(10, 60), (-35, 10), (-30, 45)]
x_aver_max = (60 + 10 + 45) / 3
x_aver_min = (10 - 35 - 30) / 3
y_max = 200 + int(x_aver_max)
y_min = 200 + int(x_aver_min)
odnoridna = 0
neodnoridna = 0


def regression(x, b):
    y = sum([x[i] * b[i] for i in range(len(x))])
    return y


def plan_matrix(n, m):
    y = np.zeros(shape=(n, m))
    for i in range(n):
        for j in range(m):
            y[i][j] = random.randint(y_min, y_max)
    x_norm = np.array([[1, -1, -1, -1],
                       [1, -1, 1, 1],
                       [1, 1, -1, 1],
                       [1, 1, 1, -1],
                       [1, -1, -1, 1],
                       [1, -1, 1, -1],
                       [1, 1, -1, -1],
                       [1, 1, 1, 1]])
    x_norm = x_norm[:len(y)]

    x = np.ones(shape=(len(x_norm), len(x_norm[0])))
    for i in range(len(x_norm)):
        for j in range(1, len(x_norm[i])):
            if x_norm[i][j] == -1:
                x[i][j] = x_range[j - 1][0]
            else:
                x[i][j] = x_range[j - 1][1]

    return x, y, x_norm


def find_coefficient(x, y_aver, n):
    mx1 = sum(x[:, 1]) / n
    mx2 = sum(x[:, 2]) / n
    mx3 = sum(x[:, 3]) / n
    my = sum(y_aver) / n
    a12 = sum([x[i][1] * x[i][2] for i in range(len(x))]) / n
    a13 = sum([x[i][1] * x[i][3] for i in range(len(x))]) / n
    a23 = sum([x[i][2] * x[i][3] for i in range(len(x))]) / n
    a11 = sum([i ** 2 for i in x[:, 1]]) / n
    a22 = sum([i ** 2 for i in x[:, 2]]) / n
    a33 = sum([i ** 2 for i in x[:, 3]]) / n
    a1 = sum([y_aver[i] * x[i][1] for i in range(len(x))]) / n
    a2 = sum([y_aver[i] * x[i][2] for i in range(len(x))]) / n
    a3 = sum([y_aver[i] * x[i][3] for i in range(len(x))]) / n

    X = [[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]]
    Y = [my, a1, a2, a3]
    B = [round(i, 2) for i in solve(X, Y)]

    return B


def s_kv(y, y_aver, n, m):
    res = []
    for i in range(n):
        s = sum([(y_aver[i] - y[i][j]) ** 2 for j in range(m)]) / m
        res.append(s)
    return res


def kriteriy_cochrena(y, y_aver, n, m):
    S_kv = s_kv(y, y_aver, n, m)
    Gp = max(S_kv) / sum(S_kv)
    return Gp


def bs(x, y_aver, n):
    res = [sum(1 * y for y in y_aver) / n]
    for i in range(3):
        b = sum(j[0] * j[1] for j in zip(x[:, i], y_aver)) / n
        res.append(b)
    return res


def cohren(f1, f2, q=0.05):
    from scipy.stats import f
    q1 = q / f1
    fisher_value = f.ppf(q=1 - q1, dfn=f2, dfd=(f1 - 1) * f2)
    return fisher_value / (fisher_value + f1 - 1)


def main(n, m):
    global odnoridna, neodnoridna
    f1 = m - 1
    f2 = n
    G_kr = cohren(f1, f2)
    x, y, x_norm = plan_matrix(n, m)
    y_aver = [round(sum(i) / len(i), 2) for i in y]

    Gp = kriteriy_cochrena(y, y_aver, n, m)
    if Gp < G_kr:
        odnoridna += 1
    else:
        neodnoridna += 1



if __name__ == '__main__':
    for i in range(100):
        main(4, 4)
    print("\nОднорідних дисперсій: ", odnoridna)
    print("Неоднорідних дисперсій: ", neodnoridna)
