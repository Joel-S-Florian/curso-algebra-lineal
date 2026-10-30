"""Comprueba con aritmética exacta los resultados de F01, F02 y F03.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f01_f03.py
"""

from fractions import Fraction as F


def cumple(coeficientes, b, punto):
    return sum(a * x for a, x in zip(coeficientes, punto)) == b


# F01
assert cumple((4, -2, 1), 3, (1, 1, 1)) and 4 * 1 == 2 * 1 - 1 + 3  # N1-01 a
assert cumple((2, -4, -1), -7, (0, 0, 7))  # N1-03
assert 4 * F(-3, 2) + 7 == 1 and 4 * F(3, 2) + 7 != 1  # N1-04
x = F(14, 3)
assert 4 * (x - 1) - (2 * x + 3) == x / 2  # N2-01
x = F(18, 5)
assert 3 * (2 * x - 1) - 2 * (x + 4) == 5 - (x - 2)  # N2-02
x = -9
assert F(x - 1, 4) - F(2 * x + 1, 6) == F(1, 3)  # N2-03
assert 3 * 10 - (10 - 4) == 2 * (10 + 2)  # N3-01 b (cualquier x)
assert 14 + F(14, 2) == 21  # N3-02
assert (1 - 2) * (1 + 2) == 1**2 + (-4) and 0 == 3 * (-1) + 3  # N4-01 a, b
for k in (3, -2, F(1, 2), 5):  # N4-02: x = 1/(k - 1) cuando k != ±1
    assert (k * k - 1) * F(1, k - 1) == k + 1

# F02
assert all(3 * px - py == 6 for px, py in ((0, -6), (2, 0), (1, -3), (F(1, 3), -5)))  # N1-01
assert [p for p in ((3, 2), (0, 4), (6, -1), (-3, 6)) if cumple((2, 3), 12, p)] == [(3, 2), (0, 4), (-3, 6)]  # N1-02
assert all(cumple((2, 3, 6), 12, p) for p in ((6, 0, 0), (0, 4, 0), (0, 0, 2), (3, 2, 0), (0, 2, 1), (3, 0, 1)))  # N2-02
for t in (0, 3, F(5, 2)):
    assert cumple((2, -3), 6, (t, F(2 * t - 6, 3))) and cumple((2, -3), 6, (F(6 + 3 * t, 2), t))  # N3-01
for s, t in ((0, 0), (1, 0), (0, 1), (2, -3)):
    assert cumple((1, -1, 2), 5, (5 + s - 2 * t, s, t))  # N3-02
assert not cumple((1, 2), 4, (2, 2 - 2))  # N4-02: (t, 2 - t) con t = 2 falla

# F03
assert [p for p in ((1, 2), (2, 0), (4, 3)) if cumple((2, 1), 4, p) and cumple((1, -3), -5, p)] == [(1, 2)]  # N1-01
p = (F(10, 3), F(-1, 3))
assert cumple((1, 4), 2, p) and cumple((2, -1), 7, p)  # N2-01 b
assert cumple((1, -2), 3, (5, 1)) and cumple((-2, 4), -6, (5, 1))  # N2-02
assert cumple((1, 1), 1, (2, -1)) and cumple((1, -1), 3, (2, -1))  # N3-01 a
assert cumple((1, 1), 4, (3, 1)) and cumple((1, -1), 2, (3, 1))  # N2-05
for a in (0, 1, 3, -7):
    assert cumple((1, a), 2, (2, 0)) and cumple((2, 6), 4, (2, 0))  # N3-04
assert all(cumple(c, b, (2, -1, 3)) for c, b in (((1, 1, 1), 4), ((2, -1, 1), 8), ((1, 3, -1), -4)))  # N1-02
assert not cumple((2, -1, 1), 8, (1, 0, 3))
for t in (0, 5, F(-1, 2)):
    q = (1 + t, 2 - t, t)
    assert cumple((1, 1, 0), 3, q) and cumple((0, 1, 1), 2, q) and cumple((1, 0, -1), 1, q)  # N2-03
s = (5, 1, -1, 4)
assert cumple((2, -1, 4, -1), 1, s) and cumple((1, 0, 5, 0), 0, s) and cumple((0, -1, 1, 2), 6, s)  # N1-03
for u in ((2, -1, 1), (4, -2, 2), (-2, 1, -1), (0, 0, 0)):
    assert cumple((1, 1, -1), 0, u) and cumple((2, 3, -1), 0, u)  # N2-04
assert cumple((1, 1, 1), 0, (1, 1, -2)) and cumple((1, -1, 0), 0, (1, 1, -2))  # N3-03 d
for punto in ((1, 2), (3, -2), (5, -6), (-1, 6), (2, 0)):
    assert cumple((2, 1), 4, punto)  # N5-01 a
assert F(1, 4) + F(1, 4) != 1  # N5-01 c
assert cumple((1, 2), 5, (1, 2)) and cumple((3, -1), 1, (1, 2)) and cumple((2, 3), 8, (1, 2))  # N4-02
assert cumple((1, 1, -1), 2, (2, 1, 1)) and cumple((2, 2, -2), 4, (2, 1, 1))  # N4-03
assert all(cumple(c, b, (1, 1)) for c, b in (((1, 1), 2), ((1, -1), 0), ((2, 1), 3)))  # N4-04 c

# Datos de las escenas de la Unidad 1
assert all(cumple(c, b, (1, 2, 3)) for c, b in (((1, 1, 1), 6), ((1, -1, 1), 2), ((1, 1, -1), 0)))  # L09 punto
for t in (0, 1, 2):
    q = (2 - t, 1, t)
    assert cumple((1, 1, 1), 3, q) and cumple((1, -1, 1), 1, q) and cumple((1, 0, 1), 2, q)  # L09 recta
assert cumple((1, 2, -1), 4, (1, 1, -1)) and cumple((3, -1, 2), 0, (1, 1, -1))  # L10 ejemplo m = 2, n = 3
assert cumple((2, -1), 1, (2, 3)) and cumple((1, 3), 11, (2, 3))  # L08 rectas que se cortan

print("F01-F03: todas las comprobaciones son correctas.")
