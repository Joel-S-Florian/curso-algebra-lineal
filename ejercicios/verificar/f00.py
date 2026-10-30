"""Comprueba con aritmética exacta los resultados numéricos de ejercicios/F00_preliminares.md.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f00.py
"""

from fractions import Fraction as F

# L01
assert (-4) * (-5) - 3 * (-2) == 26  # N1-02 a
assert -(2**2) + (-2) ** 2 == 0  # N1-02 b
assert 7 - (-3) - (+5) == 5  # N1-02 c
assert -(-(-6)) == -6 and -(3 - 5) == 2 and -((-2) ** 3) == 8  # N1-03 a-c
assert (-1) ** 10 == 1 and -(1**10) == -1  # N1-03 d
assert (-4) * F(-1, 4) == 1 and F(2, 3) * F(3, 2) == 1  # N1-04 c
assert F(2, 3) - F(5, 6) + F(1, 4) == F(1, 12)  # N2-01 a
assert F(3, 5) / F(-9, 10) == F(-2, 3)  # N2-01 b
assert 2 + F(4 * (5 - 3) ** 2, 8) == 4  # N2-02 a
assert 7 * (10 + 3) == 7 * 10 + 7 * 3 == 91  # N2-02 b
assert 12 / (2 + 4) != 12 / 2 + 12 / 4  # N3-01 c
assert F(3, 4) + F(1, 4) == 1 and F(2 + 3, 2) == F(5, 2)  # N4-01
a, b = F(1, 3), F(1, 2)
assert a < (a + b) / 2 < b  # N5-01 (ejemplo)
for p in range(1, 31):  # N5-05 a: comprobación, no prueba
    assert (p * p % 3 == 0) == (p % 3 == 0)

# L02
x, y, z = 1, -2, 3
assert 4 * x - y + 7 - 2 * z == 7  # N1-05 d
x = -1
assert 2 * (x - 3) - (4 - x) == 3 * x - 10 == -13  # N1-06 b
assert [v for v in (-2, 0, 4) if 3 * v - 2 == v + 6] == [4]  # N2-03
assert 3 * 3 - 5 == 7 - 3  # N2-04
assert 2 * (-4) + 3 == -4 - 1 and 5 * 0 == 0  # N3-02 c, d
assert F(6, 2) + F(6, 3) == 5  # N3-05 a
x = F(-5, 3)
assert 2 * (x + 1) - 3 == 5 * x + 4  # N3-05 b
assert all(v * v == 3 * v for v in (0, 3))  # N4-02 a

# L03
assert [p for p in ((2, 0), (0, -4), (3, 2), (1, 1)) if 2 * p[0] - p[1] == 4] == [(2, 0), (0, -4), (3, 2)]  # N2-05
assert 2 * 4 - 4 == 4 and 2 * (-1) - (-6) == 4  # N2-05 nuevos puntos
m = F(-2 - 4, 2 - (-1))
n = 4 - m * (-1)
assert (m, n) == (-2, 2) and m * 2 + n == -2  # N2-06
assert 3 * 0 + 2 * 3 == 6 and 3 * 2 + 2 * 0 == 6  # N3-03
assert 2 * 1 + 1 == 3 and 1 + 3 == 4  # N4-03 c: (1, 3)
assert 1 + 2 + 0 == 3 and 2 + 2 + 1 != 3  # N5-03 a
assert all(px + 2 * py - pz == 4 for px, py, pz in ((4, 0, 0), (0, 2, 0), (0, 0, -4)))  # N5-03 b

# L04
assert 3 * 2 - 1 == 5  # N1-08 a
assert sum(2 * k - 1 for k in range(1, 6)) == 25  # N2-07 a
assert sum(aj * xj for aj, xj in zip((2, -1, 3), (1, 4, -2))) == -8  # N2-07 b
assert sum(3 * k for k in range(1, 5)) == 3 + 6 + 9 + 12  # N2-07 c
A = [[2, -1, 0], [4, 3, -5], [1, 7, 6]]
assert (A[1][2], A[2][1]) == (-5, 7)  # N2-08 a (índices de Python empiezan en 0)
assert sum(A[1][j] * xj for j, xj in enumerate((1, 2, -1))) == 15  # N2-08 b
assert sum(A[i][i] for i in range(3)) == 11  # N2-08 c
assert (1 + 1) ** 2 != 1**2 + 1**2 and (-3) ** 2 > 1**2  # N4-04 c, d

# Escena ComoSeDemuestraAlgo: n² + n + 41 es primo para n = 0..39 y no para n = 40.
def es_primo(k):
    return k > 1 and all(k % d for d in range(2, int(k**0.5) + 1))


assert all(es_primo(k * k + k + 41) for k in range(40)) and 40 * 40 + 40 + 41 == 41 * 41

print("F00: todas las comprobaciones son correctas.")
