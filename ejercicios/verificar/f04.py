"""Comprueba con aritmética exacta los resultados de ejercicios/F04_metodos_elementales.md.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f04.py
"""

from fractions import Fraction as F


def cumple(coeficientes, b, punto):
    return sum(a * x for a, x in zip(coeficientes, punto)) == b


def resolver_2x2(a1, b1, c1, a2, b2, c2):
    """Solución única de a1 x + b1 y = c1, a2 x + b2 y = c2 (regla de Cramer, solo para comprobar)."""
    d = F(a1 * b2 - a2 * b1)
    assert d != 0
    return (c1 * b2 - c2 * b1) / d, (a1 * c2 - a2 * c1) / d


# L13 Sustitución
assert resolver_2x2(2, 1, 8, 1, -1, 1) == (3, 2)  # N1-01
assert resolver_2x2(1, 3, 10, 2, -1, 6) == (4, 2)  # N1-02
assert resolver_2x2(3, 2, 12, 4, -5, -7) == (2, 3)  # N2-01
for t in (0, 1, F(-2, 3)):
    assert cumple((1, -3), 2, (2 + 3 * t, t)) and cumple((-2, 6), -4, (2 + 3 * t, t))  # N3-01 a
assert -2 * 2 == -4 and -2 * 2 != 1  # N3-01 b: tras sustituir, -4 = 1 es falso
assert resolver_2x2(1, 1, 5, 2, -1, 1) == (2, 3)  # N4-03
assert resolver_2x2(3, -2, 4, 1, 1, 3) == (2, 1)  # N4-04
assert not cumple((3, -2), 4, (3 - F(5, 3), F(5, 3)))  # N4-04: la solución del error no verifica

# L14 Igualación
assert resolver_2x2(-3, 1, -2, 1, 1, 6) == (2, 4)  # N1-03: y = 3x - 2, y = -x + 6
assert resolver_2x2(1, 2, 7, 3, -1, 7) == (3, 2)  # N2-02
g = 6
assert 10 + 2 * g == 4 + 3 * g == 22 and 10 + 2 * 8 < 4 + 3 * 8  # N3-02

# L15 Reducción
assert resolver_2x2(1, 1, 7, 1, -1, 3) == (5, 2)  # N1-04
assert resolver_2x2(4, 3, 10, 6, -5, -4) == (1, 2)  # N2-03
x, y = 3, F(9, 2)
assert x / F(2) + y / 3 == 3 and x / F(4) - y / 6 == 0  # N2-04
s = (1, 2, -1)
assert cumple((1, 1, 1), 2, s) and cumple((1, -1, 2), -3, s) and cumple((2, 1, -1), 5, s)  # N2-05
assert resolver_2x2(-2, 1, 1, 3, 1, 11) == (2, 5)  # N3-03 a: y = 2x + 1, 3x + y = 11
assert resolver_2x2(5, 2, 1, 3, -2, 15) == (2, F(-9, 2))  # N3-03 b
assert resolver_2x2(1, 1, 4, -2, 1, -5) == (3, 1)  # N3-03 c: y = 4 - x, y = 2x - 5
assert resolver_2x2(1, 1, 30, 2, 4, 84) == (18, 12)  # N3-04
assert resolver_2x2(2, 1, 5, 1, -1, 1) == (2, 1) and not cumple((2, 1), 5, (0, 2))  # N4-01
for a in (0, 1, 3, F(1, 2)):  # N4-02: a != 2
    for b in (0, 2, 5):
        yv = F(b - 2) / (4 - 2 * a)
        assert cumple((1, a), 1, (1 - a * yv, yv)) and cumple((2, 4), b, (1 - a * yv, yv))
for t in (0, 3):  # N4-02: a = 2, b = 2 -> (1 - 2t, t)
    assert cumple((1, 2), 1, (1 - 2 * t, t)) and cumple((2, 4), 2, (1 - 2 * t, t))

# Datos de las escenas de la Unidad 2
assert resolver_2x2(3, 1, 11, 1, -2, -1) == (3, 2)  # L13 ejemplo
assert resolver_2x2(2, 3, 7, 5, -4, 6) == (2, 1)  # L13 fracciones
assert all(cumple(c, b, (1, 2, 3)) for c, b in (((1, 1, 1), 6), ((1, -1, 1), 2), ((1, 1, -1), 0)))  # L13 / L15 3x3
assert resolver_2x2(2, -1, 1, 1, 3, 11) == (2, 3)  # L14 ejemplo
assert resolver_2x2(-2, 1, 3, -1, 1, 7) == (4, 11)  # L14 taxis
assert resolver_2x2(3, 2, 7, 5, -2, 9) == (2, F(1, 2))  # L15 ejemplo 1
assert resolver_2x2(2, 3, 8, 3, -4, -5) == (1, 2)  # L15 ejemplo 2
for k in (F(-3), F(-1), F(1, 2), F(3)):  # L15: E2 + k E1 pasa siempre por (2, 1)
    assert cumple((1 + k, k - 1), 1 + 3 * k, (2, 1))

print("F04: todas las comprobaciones son correctas.")
