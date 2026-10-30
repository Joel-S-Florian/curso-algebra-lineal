"""Comprueba con aritmética exacta los resultados de F05, F06 y F07 (Unidad 3).

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f05_f07.py
"""

from fractions import Fraction as F


def mul(a, b):
    assert len(a[0]) == len(b), "dimensiones incompatibles"
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def suma(a, b, c=1, d=1):
    return [[c * x + d * y for x, y in zip(fa, fb)] for fa, fb in zip(a, b)]


def col(*v):
    return [[x] for x in v]


# F05
B = [[3, -2, 0], [1, 7, -5]]
assert (len(B), len(B[0])) == (2, 3) and (B[0][1], B[1][0], B[1][2]) == (-2, 1, -5)  # N1-01
A = [[4, -1], [0, 2], [-3, 5]]
assert suma(A, [[-4, 6], [1, 1], [3, -5]]) == [[0, 5], [1, 3], [0, 0]]  # N1-04
u, v = col(2, -1, 3), col(-1, 4, 0)
assert suma(u, v) == col(1, 3, 3) and suma(u, u, 3, 0) == col(6, -3, 9)  # N2-01 a, b
assert suma(u, v, 2, -3) == col(7, -14, 6) and suma(u, u, 1, -1) == col(0, 0, 0)  # N2-01 c, d
A, B = [[2, 0], [-1, 3]], [[1, -4], [5, 2]]
assert suma(A, B, 2, -3) == [[1, 12], [-17, 0]]  # N2-02 a
X = [[F(-1, 2), -2], [3, F(-1, 2)]]
assert suma(A, X, 1, 2) == B  # N2-02 b
x, y = 3, 2
assert (x + y, x - y) == (5, 1)  # N2-03
a, b = F(25, 7), F(-6, 7)
assert suma(col(1, 2), col(3, -1), a, b) == col(1, 8)  # N3-01

# F06
assert mul([[2, -1], [0, 3], [1, 1]], col(4, 5)) == col(3, 15, 9)  # N1-01 a
assert mul([[1, 0, 2]], col(3, -1, 4)) == [[11]]  # N1-01 b
D = [[3, 0], [0, 1]]
assert [mul(D, col(*p)) for p in ((1, 0), (0, 1), (1, 1), (-2, 3))] == [col(3, 0), col(0, 1), col(3, 1), col(-6, 3)]  # N1-02
A = [[2, -1, 3], [0, 4, 1]]
assert mul(A, col(1, 2, -1)) == col(-3, 7)  # N2-01
assert suma(suma(col(2, 0), col(-1, 4), 1, 2), col(3, 1), 1, -1) == col(-3, 7)  # N2-01 por columnas
A, B = [[1, -1], [2, 0], [3, 1]], [[2, 1, 0], [-1, 4, 2]]
assert mul(A, B) == [[3, -3, -2], [4, 2, 0], [5, 7, 2]] and mul(B, A) == [[4, -2], [13, 3]]  # N2-02
A, B, I = [[2, 0], [1, 3]], [[1, 4], [0, -1]], [[1, 0], [0, 1]]
assert mul(A, B) == [[2, 8], [1, 1]] and mul(B, A) == [[6, 12], [-1, -3]] and mul(A, I) == A  # N3-01
S = suma(A, B)
derecha = suma(suma(mul(A, A), mul(A, B), 1, 2), mul(B, B))
assert mul(S, S) == [[13, 20], [5, 8]] and derecha == [[9, 16], [7, 12]]  # N3-01: (A + B)^2 distinto
R = [[0, -1], [1, 0]]
assert mul(R, col(3, 2)) == col(-2, 3)  # N3-02
A = [[1, 1], [1, 1]]
assert mul(A, [[1, 0], [0, 0]]) == mul(A, [[0, 0], [1, 0]])  # N4-01: AB = AC con B distinto de C
assert mul([[1, 1], [1, 1]], [[1, -1], [-1, 1]]) == [[0, 0], [0, 0]]  # escena L20
assert mul([[1, 1], [2, 0]], col(2, 5)) == col(7, 4)  # N5-01: T(2, 5) = (7, 4)

# F07
A, b = [[1, 2], [3, -1], [0, 4]], col(5, 1, 8)
assert mul(A, col(1, 2)) == b  # N2-01
assert mul([[1, 3], [2, 1]], col(2, 1)) == col(5, 5)  # N2-02
fila2 = [3 - 3 * 1, 1 - 3 * 2, 0 - 3 * 5]
assert fila2 == [0, -5, -15] and mul([[1, 2], [3, 1]], col(-1, 3)) == col(5, 0)  # N3-01
assert mul([[2, -1], [1, -1]], col(-3, -3)) == col(-3, 0)  # N4-01: x = y = -3 cumple 2x + 3 = y y x - y = 0

# Datos de las escenas de la Unidad 3
assert mul([[1, 2, 0], [3, -1, 4]], col(2, 1, -1)) == col(4, 1)  # L19
assert mul([[1, 2, 0], [-1, 3, 1]], [[2, 1], [0, -1], [4, 2]]) == [[2, -1], [2, -2]]  # L20
assert mul([[1, 1], [0, 1]], [[1, 0], [1, 1]]) == [[2, 1], [1, 1]] and mul([[1, 0], [1, 1]], [[1, 1], [0, 1]]) == [[1, 1], [1, 2]]  # L20
assert mul([[1, 1], [0, 1]], col(1, 2)) == col(3, 2) and mul([[2, -1], [1, 1]], col(1, 2)) == col(0, 3)  # L21
A3 = [[2, 1, -1], [1, -3, 2], [4, 0, 1]]
assert mul(A3, col(1, 1, 1)) == col(2, 0, 5) and mul(A3, col(1, 0, 1)) == col(1, 3, 5)  # L22
assert mul([[1, 1, 1], [1, -1, 1], [1, 1, -1]], col(1, 2, 3)) == col(6, 2, 0)  # L23
assert mul([[1, 1, 1], [0, -2, 0], [0, 0, -2]], col(1, 2, 3)) == col(6, -4, -6)  # L23
assert suma(col(1, 2), col(3, -1), 2, 1) == col(5, 3)  # L17

print("F05-F07: todas las comprobaciones son correctas.")
