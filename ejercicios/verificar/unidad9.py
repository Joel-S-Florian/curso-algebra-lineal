"""Comprueba con aritmética exacta los datos de las escenas de la Unidad 9 (L51–L55) y de la prueba final.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/unidad9.py
"""

import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generar"))

import algebra as al  # noqa: E402
from algebra import M  # noqa: E402

es = lambda v: [F(x) for x in v]  # noqa: E731

# ---------------------------------------------------------------- L52 · problema 1: mezclas
A = M([1, 2, 1], [2, 1, 3], [1, 1, 2])
b = es([8, 11, 7])
assert al.det(A) == -2 and al.resolver(A, b) == ("SCD", es([3, 2, 1]))
# Gauss con el intercambio de las filas 2 y 3: R2 <- R2 - 2R1, R3 <- R3 - R1, R2 <-> R3, R3 <- R3 - 3R2
f1, f2, f3 = [F(v) for v in (1, 2, 1, 8)], [F(v) for v in (2, 1, 3, 11)], [F(v) for v in (1, 1, 2, 7)]
f2 = [x - 2 * y for x, y in zip(f2, f1)]
f3 = [x - y for x, y in zip(f3, f1)]
assert f2 == es([0, -3, 1, -5]) and f3 == es([0, -1, 1, -1])
f2, f3 = f3, f2
f3 = [x - 3 * y for x, y in zip(f3, f2)]
assert f3 == es([0, 0, -2, -2])

# ---------------------------------------------------------------- L52 · problema 2: rotonda
A2 = M([1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1])
b2 = es([7, 8, 7, 6])
res = al.resolver(A2, b2)
assert res[0] == "SCI" and len(res[2]) == 1
xp, d = res[1], res[2][0]
assert xp == es([6, 1, 7, 0]) and d == es([-1, 1, -1, 1])  # x = (6, 1, 7, 0) + s(-1, 1, -1, 1)
cotas = [(-xi / di) for xi, di in zip(xp, d)]
assert max(c for c, di in zip(cotas, d) if di > 0) == 0 and min(c for c, di in zip(cotas, d) if di < 0) == 6  # 0 <= s <= 6
assert al.por_vec(A2, es([2, 5, 3, 4])) == b2  # el caso x0 = (2, 5, 3, 4) corresponde a s = 4

# ---------------------------------------------------------------- L52 · problema 3: dos lados derechos con LU
A3 = M([1, 2, -1], [2, 3, 1], [-1, 1, 2])
L, U = al.lu(A3)
assert L == M([1, 0, 0], [2, 1, 0], [-1, -3, 1]) and U == M([1, 2, -1], [0, -1, 3], [0, 0, 10])
for x0, b_, y_ in [([1, -1, 2], [-3, 1, 2], None), ([2, 0, 1], [1, 5, 0], [1, 3, 10])]:
    assert al.por_vec(A3, es(x0)) == es(b_)
    y = al.sust_adelante(L, es(b_))
    assert al.sust_atras(U, y) == es(x0)
    if y_:
        assert y == es(y_)

# ---------------------------------------------------------------- L52 · problema 4: parábola por tres puntos
puntos = [(-1, 6), (1, 0), (2, 3)]
V = [[F(1), F(x), F(x * x)] for x, _ in puntos]
assert al.resolver(V, es([y for _, y in puntos])) == ("SCD", es([1, -3, 2]))  # y = 1 - 3x + 2x^2
assert all(1 - 3 * x + 2 * x * x == y for x, y in puntos)
# vértice y cortes con el eje x
assert (F(3, 4), F(1) - 3 * F(3, 4) + 2 * F(9, 16)) == (F(3, 4), F(-1, 8)) and 2 * F(1, 2) ** 2 - 3 * F(1, 2) + 1 == 0

# ---------------------------------------------------------------- L53 · parámetro
def Aa(a):
    return M([1, 1, a], [1, a, 1], [a, 1, 1])


bb = es([1, 1, 1])
for a_, esperado in [(1, "SCI"), (-2, "SI"), (0, "SCD"), (2, "SCD"), (-1, "SCD"), (3, "SCD")]:
    assert al.resolver(Aa(a_), bb)[0] == esperado, a_
assert al.det(Aa(1)) == 0 and al.det(Aa(-2)) == 0
for a_ in (0, 2, -1, 3):
    x = al.resolver(Aa(a_), bb)[1]
    assert x == [F(1, a_ + 2)] * 3
assert al.rango(Aa(1)) == 1 and al.rango(Aa(-2)) == 2
assert al.resolver(Aa(1), bb)[2] == [es([-1, 1, 0]), es([-1, 0, 1])]

# ---------------------------------------------------------------- L53 · núcleo e imagen (la matriz de la Unidad 8)
A6 = M([1, 2, 0, 1], [2, 4, 1, 4], [1, 2, 1, 3])
assert al.resolver(A6, es([1, 3, 2])) == ("SCI", es([1, 0, 1, 0]), [es([-2, 1, 0, 0]), es([-1, 0, -2, 1])])
assert al.resolver(A6, es([1, 0, 0]))[0] == "SI"
assert al.base_columnas(A6) == [0, 2] and al.rango(A6) + len(al.nucleo(A6)) == 4

# ---------------------------------------------------------------- L53 · verdadero o falso
# (a) 2x3 puede ser incompatible; (b) 4x3 de rango 3 no siempre es compatible; (c) núcleo trivial -> a lo sumo una solución
assert al.resolver(M([1, 1, 1], [1, 1, 1]), es([1, 2]))[0] == "SI"
assert al.rango(M([1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1])) == 3 and al.resolver(M([1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]), es([1, 1, 1, 0]))[0] == "SI"
assert al.nucleo(M([1, 0], [0, 1], [1, 1])) == []

print("Unidad 9: todo correcto")
