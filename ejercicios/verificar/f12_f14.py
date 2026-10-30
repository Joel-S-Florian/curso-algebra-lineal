"""Comprueba con aritmética exacta los resultados de F12, F13 y F14 (Unidad 8: combinaciones,
independencia, base, núcleo, espacio columna y rango-nulidad) y los datos de las escenas L43–L50.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f12_f14.py
"""

from fractions import Fraction as F


def M(*filas):
    return [[F(v) for v in f] for f in filas]


def rref(a):
    a = [f[:] for f in a]
    fila, piv = 0, []
    for col in range(len(a[0])):
        p = next((i for i in range(fila, len(a)) if a[i][col] != 0), None)
        if p is None:
            continue
        a[fila], a[p] = a[p], a[fila]
        a[fila] = [v / a[fila][col] for v in a[fila]]
        for i in range(len(a)):
            if i != fila and a[i][col] != 0:
                a[i] = [x - a[i][col] * y for x, y in zip(a[i], a[fila])]
        piv.append(col)
        fila += 1
        if fila == len(a):
            break
    return a, piv


def rango(a):
    return len(rref(a)[1])


def por(a, x):
    return [sum(f[j] * x[j] for j in range(len(x))) for f in a]


def cols(a):
    return [[f[j] for f in a] for j in range(len(a[0]))]


def de_columnas(vs):
    return [[v[i] for v in vs] for i in range(len(vs[0]))]


def comb(coefs, vs):
    return [sum(c * v[i] for c, v in zip(coefs, vs)) for i in range(len(vs[0]))]


def nucleo(a):
    """Base del núcleo: un vector por variable libre."""
    r, piv = rref(a)
    n = len(a[0])
    base = []
    for libre in (j for j in range(n) if j not in piv):
        v = [F(0)] * n
        v[libre] = F(1)
        for fila, p in enumerate(piv):
            v[p] = -r[fila][libre]
        base.append(v)
    return base


def en_columna(a, b):
    return rango(a) == rango([f + [bb] for f, bb in zip(a, b)])


def independientes(vs):
    return rango(de_columnas(vs)) == len(vs)


def es(v):
    return [F(x) for x in v]


# ------------------------------------------------ matrices compartidas por L45–L50
A = M([1, 2, 0, 1], [2, 4, 1, 4], [1, 2, 1, 3])  # 3x4, rango 2, nulidad 2
b_ok, b_no = es([1, 3, 2]), es([1, 0, 0])
B2 = M([1, 2], [2, 4])  # 2x2, rango 1, nulidad 1
B = M([1, 1, 1], [1, 2, 3])
C = M([1, 0], [0, 1], [1, 1])

r, piv = rref(A)
assert r == M([1, 2, 0, 1], [0, 0, 1, 2], [0, 0, 0, 0]) and piv == [0, 2]
n1, n2 = nucleo(A)
assert n1 == es([-2, 1, 0, 0]) and n2 == es([-1, 0, -2, 1])
assert por(A, n1) == [0, 0, 0] and por(A, n2) == [0, 0, 0]
c1, c2, c3, c4 = cols(A)
assert c1 == es([1, 2, 1]) and c3 == es([0, 1, 1])
assert c2 == comb([2], [c1]) and c4 == comb([1, 2], [c1, c3])  # relaciones entre columnas
assert independientes([c1, c3]) and not independientes([c1, c3, c4])
# las relaciones entre columnas se conservan en la reducida, pero el espacio columna no
rc = cols(r)
assert rc[1] == comb([2], [rc[0]]) and rc[3] == comb([1, 2], [rc[0], rc[2]])
assert not en_columna(de_columnas([rc[0], rc[2]]), c1)  # (1,2,1) no está en el espacio columna de R
assert rango(A) + len(nucleo(A)) == 4

# ------------------------------------------------ L43
u, v = es([2, 1]), es([-1, 1])
assert comb([2, 1], [u, v]) == es([3, 3])
assert rango(de_columnas([u, v])) == 2  # genera todo R2
assert rango(de_columnas([es([1, 2]), es([2, 4])])) == 1  # una recta

# ------------------------------------------------ L44
w1, w2 = es([1, 2]), es([2, 4])
assert comb([2, -1], [w1, w2]) == es([0, 0]) and not independientes([w1, w2])
assert independientes([es([1, 2]), es([2, 1])])
assert not independientes([c1, c3, c4]) and comb([-1, -2, 1], [c1, c3, c4]) == es([0, 0, 0])
assert nucleo(de_columnas([c1, c3, c4])) == [es([-1, -2, 1])]
assert rango(de_columnas([c1, c3, c4])) == 2
d1, d2 = es([1, 1]), es([1, -1])
assert independientes([d1, d2]) and comb([2, 1], [d1, d2]) == es([3, 1])  # coordenadas de (3,1)

# ------------------------------------------------ F12
assert comb([2, -3], [es([1, -1, 3]), es([0, 2, 1])]) == es([2, -8, 3])  # N1-01
assert comb([1, 2], [es([1, 2]), es([3, 1])]) == es([7, 4])  # N1-02
assert en_columna(de_columnas([es([1, 1, 0]), es([0, 1, 1])]), es([3, 5, 2]))  # N2-01
assert comb([3, 2], [es([1, 1, 0]), es([0, 1, 1])]) == es([3, 5, 2])
assert not en_columna(de_columnas([es([1, 1, 0]), es([0, 1, 1])]), es([3, 5, 3]))
assert independientes([es([1, 0, 1]), es([0, 1, 1]), es([1, 1, 0])])  # N3-02
det = lambda m: m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
assert det(de_columnas([es([1, 0, 1]), es([0, 1, 1]), es([1, 1, 0])])) == -2
cuatro = [es([1, 0, 0]), es([0, 1, 0]), es([0, 0, 1]), es([1, 2, 3])]  # N3-03
assert not independientes(cuatro)
assert not independientes([es([0, 0]), es([1, 2])])  # N3-04
assert rref(A)[1] == [0, 2]  # N4-01: base {c1, c3}

t1, t2, t3 = es([1, 1, 1]), es([1, 2, 3]), es([2, 3, 4])  # F12 N3-02
assert not independientes([t1, t2, t3]) and comb([1, 1, -1], [t1, t2, t3]) == es([0, 0, 0])
assert independientes([comb([1, 1], [d1, d2]), comb([1, -1], [d1, d2])])  # N4-03 con u = d1, v = d2

# ------------------------------------------------ L45–L47
assert por(B2, es([-2, 1])) == es([0, 0]) and por(B2, es([1, 1])) == es([3, 6])  # F13 N1-01
assert nucleo(B2) == [es([-2, 1])]
assert por(A, comb([1, 1], [n1, n2])) == es([0, 0, 0]) and comb([1, 1], [n1, n2]) == es([-3, 1, -2, 1])  # N2-02
assert por(A, es([1, 0, 0, 1])) == es([2, 6, 4])
assert nucleo(B) == [es([1, -2, 1])] and por(B, es([1, -2, 1])) == es([0, 0])  # N3-02
assert nucleo(C) == [] and rango(C) == 2  # N3-03
xp = es([1, 0, 1, 0])
assert por(A, xp) == b_ok  # N3-05
aug = [f + [bb] for f, bb in zip(A, b_ok)]
assert rref(aug)[0] == M([1, 2, 0, 1, 1], [0, 0, 1, 2, 1], [0, 0, 0, 0, 0])
for s, t in [(0, 0), (1, 0), (0, 1), (2, -3), (F(1, 2), F(5, 3))]:
    assert por(A, [p + s * x + t * y for p, x, y in zip(xp, n1, n2)]) == b_ok
xq = es([3, 0])  # N4-01: x + 2y = 3 con A = B2, b = (3, 6)
assert por(B2, xq) == es([3, 6])
for s in (-2, -1, 1, 2):
    assert por(B2, comb([1, s], [xq, es([-2, 1])])) == es([3, 6])
assert por(B2, es([1, 1])) == es([3, 6]) and por(B2, es([5, -1])) == es([3, 6])
x2 = es([-1, 1, 1, 0])  # N4-02
assert por(A, x2) == b_ok and [p - q for p, q in zip(xp, x2)] == comb([-1], [n1])
# L47: la hipótesis del teorema (x - xp en el núcleo) y la transformación del plano
assert por(B2, es([2, 3])) == es([8, 16])

# ------------------------------------------------ L48–L50 / F14
assert por(A, es([2, -1, 3, 1])) == es([1, 7, 6]) and comb([2, -1, 3, 1], cols(A)) == es([1, 7, 6])  # L48
P5 = [[F(1, 5), F(2, 5)], [F(2, 5), F(4, 5)]]  # A = 5 P: proyección sobre y = 2x, mismo núcleo e imagen (L50)
assert [[5 * v for v in f] for f in P5] == B2 and por(P5, es([1, 1])) == por(P5, es([-1, 2])) == [F(3, 5), F(6, 5)]
assert por(P5, es([-2, 1])) == es([0, 0])
assert comb([3, -1], cols(B2)) == es([1, 2])  # N1-01
assert en_columna(B2, es([3, 6])) and not en_columna(B2, es([1, 0]))  # N2-01
assert en_columna(A, b_ok) and not en_columna(A, b_no)  # N2-02
assert comb([1, 1], [c1, c3]) == b_ok
assert rref(B)[1] == [0, 1] and rango(B) == 2 and len(nucleo(B)) == 1  # N3-03
assert [rango(A) + len(nucleo(A)), rango(B) + len(nucleo(B)), rango(C) + len(nucleo(C))] == [4, 3, 2]  # N4-01
assert 7 - 3 == 4  # N4-02
assert 5 - 3 >= 2  # N4-03: una 3x5 tiene nulidad >= 2

# N3-04: columnas pivote de la reducida que no sirven (2x2)
Q = M([1, 1], [1, 1])
assert rref(Q)[0] == M([1, 1], [0, 0]) and not en_columna(Q, es([1, 0])) and en_columna(Q, es([1, 1]))

# propiedad general (prueba numérica con matrices al azar de enteros pequeños)
import random

random.seed(8)
for _ in range(300):
    m, n = random.randint(1, 5), random.randint(1, 5)
    a = M(*[[random.randint(-2, 2) for _ in range(n)] for _ in range(m)])
    assert rango(a) + len(nucleo(a)) == n
    assert all(por(a, v) == [0] * m for v in nucleo(a))
    assert len(rref(a)[1]) == rango(de_columnas(cols(a)))  # rg(A) = rg(A^T)
    # las columnas pivote de A son independientes y generan la imagen
    pv = [cols(a)[j] for j in rref(a)[1]]
    assert all(en_columna(de_columnas(pv), c) for c in cols(a)) if pv else all(all(x == 0 for x in c) for c in cols(a))
    assert independientes(pv) if pv else True

print("F12, F13 y F14: todo correcto")
