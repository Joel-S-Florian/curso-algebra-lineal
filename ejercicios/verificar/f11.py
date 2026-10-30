"""Comprueba con aritmética exacta los resultados de F11 (rango y Rouché-Frobenius, Unidad 7)
y los datos de las escenas L39–L42.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f11.py
"""

import random
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


def clasificar(aug):
    """Rouché-Frobenius sobre [A | b]: 'SI', 'SCD' o 'SCI'."""
    n = len(aug[0]) - 1
    r_a = rango([f[:-1] for f in aug])
    r_ab = rango(aug)
    if r_a != r_ab:
        return "SI"
    return "SCD" if r_a == n else "SCI"


def satisface(aug, x):
    return all(sum(f[j] * x[j] for j in range(len(x))) == f[-1] for f in aug)


# ---------------------------------------------------------------- L39
a = M([1, 2, 3], [2, 4, 6], [1, 1, 1])
assert rango(a) == 2 and rref(a)[0] == M([1, 0, -1], [0, 1, 2], [0, 0, 0])
assert rango([[F(0)] * 3] * 2) == 0 and rango(M([1, 0, 0], [0, 1, 0], [0, 0, 1])) == 3
l28_si = M([1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, 8])
l28_sci = M([1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, 7])
assert (rango([f[:-1] for f in l28_si]), rango(l28_si)) == (2, 3)
assert (rango([f[:-1] for f in l28_sci]), rango(l28_sci)) == (2, 2)
assert clasificar(l28_si) == "SI" and clasificar(l28_sci) == "SCI"
sis3 = M([1, 1, 3], [1, -1, 1], [2, 0, 4])           # tercera = primera + segunda
assert rref(sis3)[0] == M([1, 0, 2], [0, 1, 1], [0, 0, 0]) and clasificar(sis3) == "SCD"
# rg(A) <= rg[A|b] <= rg(A) + 1 y rg <= min(m, n), con matrices aleatorias
random.seed(7)
for _ in range(500):
    m, n = random.randint(1, 5), random.randint(1, 5)
    aug = [[F(random.randint(-2, 2)) for _ in range(n + 1)] for _ in range(m)]
    r_a, r_ab = rango([f[:-1] for f in aug]), rango(aug)
    assert r_a <= r_ab <= r_a + 1 and r_a <= min(m, n)
# N1-01
assert rango(M([1, 0, 2], [0, 1, 3], [0, 0, 0])) == 2 and rango(M([0, 1, 0, 5], [0, 0, 1, 6])) == 2
# N2-01
n201 = M([1, 3, 2], [2, 6, 5], [1, 3, 3])
assert rango(n201) == 2 and rref(n201)[0] == M([1, 3, 0], [0, 0, 1], [0, 0, 0])
# N2-02
n202 = M([1, 2, 1, 4], [2, 4, 2, 7], [1, 1, 3, 5])
assert (rango([f[:-1] for f in n202]), rango(n202)) == (2, 3) and clasificar(n202) == "SI"
# N3-01
n301 = M([1, 1, 1, 1], [2, 2, 2, 2], [1, -1, 0, 0], [3, 1, 2, 2])
assert rango(n301) == 2 and rango([f[:-1] for f in n301]) == 2
assert n301[1] == [2 * v for v in n301[0]] and n301[3] == [2 * x + y for x, y in zip(n301[0], n301[2])]

# ---------------------------------------------------------------- L40
ejemplos_rf = [
    (M([1, 1, 1, 6], [1, -1, 1, 2], [1, 1, -1, 0]), "SCD", (3, 3)),
    (M([1, 1, 1, 1, 4], [1, 2, 3, 4, 10], [2, 3, 4, 5, 14]), "SCI", (2, 2)),
    (M([1, 1, 2], [1, -1, 0], [2, 1, 4]), "SI", (2, 3)),
    (M([1, 1, 1, 1], [1, 1, 1, 3]), "SI", (1, 2)),
]
for aug, esperado, (r_a, r_ab) in ejemplos_rf:
    assert clasificar(aug) == esperado and (rango([f[:-1] for f in aug]), rango(aug)) == (r_a, r_ab)
assert satisface(ejemplos_rf[0][0], [1, 2, 3])
assert rref(M([1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, 7]))[0] == M([1, 0, -1, -1], [0, 1, 2, 3], [0, 0, 0, 0])
for t in (F(0), F(2), F(-3, 2)):
    assert satisface(M([1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, 7]), [-1 + t, 3 - 2 * t, t])
# N2-03
n203 = M([1, 2, 1, 4], [2, 4, 3, 9], [3, 6, 4, 13])
assert clasificar(n203) == "SCI" and rref(n203)[0] == M([1, 2, 0, 3], [0, 0, 1, 1], [0, 0, 0, 0])
for t in (F(0), F(1), F(-5, 3)):
    assert satisface(n203, [3 - 2 * t, t, 1])
# N3-06: homogéneo
assert clasificar(M([1, 2, 0], [2, 4, 0])) == "SCI"
for t in (F(1), F(-2)):
    assert satisface(M([1, 2, 0], [2, 4, 0]), [-2 * t, t])
random.seed(3)
for _ in range(300):
    m, n = random.randint(1, 4), random.randint(1, 4)
    hom = [[F(random.randint(-2, 2)) for _ in range(n)] + [F(0)] for _ in range(m)]
    assert clasificar(hom) != "SI"
    assert (clasificar(hom) == "SCD") == (rango([f[:-1] for f in hom]) == n)
# criterio general: coincide con contar soluciones por la forma reducida
for _ in range(300):
    m, n = random.randint(1, 4), random.randint(1, 4)
    aug = [[F(random.randint(-2, 2)) for _ in range(n + 1)] for _ in range(m)]
    red, piv = rref(aug)
    compatible = n not in piv
    assert (clasificar(aug) != "SI") == compatible
    if compatible:
        x = [F(0)] * n
        for i, j in enumerate(piv):
            x[j] = red[i][-1]
        assert satisface(aug, x)                              # N4-01: con rangos iguales se construye una solución
        assert (clasificar(aug) == "SCD") == (len(piv) == n)
# N4-02: 4 ecuaciones, 5 incógnitas, rg(A) = 3 -> 2 parámetros; si rg[A|b] = 4, SI
assert 5 - 3 == 2

# ---------------------------------------------------------------- L41
assert clasificar(M([1, 2, -1, 1], [2, 4, -2, 2])) == "SCI" and clasificar(M([1, 2, 3], [2, 4, 7])) == "SI"
assert clasificar(M([1, 1, 1], [1, -1, 3], [2, 1, 3])) == "SCD" and satisface(M([1, 1, 1], [1, -1, 3], [2, 1, 3]), [2, -1])
for s_, t_ in ((F(0), F(0)), (F(3), F(-2))):
    assert satisface(M([1, 2, -1, 1], [2, 4, -2, 2]), [1 - 2 * s_ + t_, s_, t_])
# N3-04: 3 x 5 nunca SCD; 5 x 3 admite los tres tipos
random.seed(5)
for _ in range(300):
    aug = [[F(random.randint(-2, 2)) for _ in range(6)] for _ in range(3)]
    assert clasificar(aug) != "SCD"
tipos = {clasificar(M([1, 0, 0, 1], [0, 1, 0, 2], [0, 0, 1, 3], [1, 1, 0, 3], [0, 1, 1, 5])),
         clasificar(M([1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [1, 1, 1, 1], [4, 4, 4, 4])),
         clasificar(M([1, 0, 0, 1], [1, 0, 0, 2], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0]))}
assert tipos == {"SCD", "SCI", "SI"}

# ---------------------------------------------------------------- L42
def sistema_a(a_, b_):
    return M([1, 1, 1], [1, a_, b_])


for a_ in (F(-3), F(0), F(2), F(5, 2)):
    for b_ in (F(1), F(-1), F(4)):
        assert clasificar(sistema_a(a_, b_)) == "SCD"
        x = (a_ - b_) / (a_ - 1)
        y = (b_ - 1) / (a_ - 1)
        assert satisface(sistema_a(a_, b_), [x, y])
assert clasificar(sistema_a(F(1), F(1))) == "SCI"
for b_ in (F(0), F(2), F(-7)):
    assert clasificar(sistema_a(F(1), b_)) == "SI"
# N3-05: m x + y = 1, x + m y = m
for m_ in (F(-3), F(0), F(2), F(1, 2)):
    assert clasificar(M([m_, 1, 1], [1, m_, m_])) == "SCD"
assert clasificar(M([1, 1, 1], [1, 1, 1])) == "SCI" and clasificar(M([-1, 1, 1], [1, -1, -1])) == "SCI"
# L42 y N4-05: x+y+z=1, x+2y+3z=m, x+3y+5z=k  ->  compatible si y solo si k = 2m - 1
for m_ in (F(2), F(0), F(-1), F(7, 3)):
    for k_ in (F(-4), F(0), F(3), 2 * m_ - 1, F(10)):
        c = clasificar(M([1, 1, 1, 1], [1, 2, 3, m_], [1, 3, 5, k_]))
        assert c == ("SCI" if k_ == 2 * m_ - 1 else "SI")
for t in (F(0), F(1), F(-2)):
    assert satisface(M([1, 1, 1, 1], [1, 2, 3, 2], [1, 3, 5, 3]), [t, 1 - 2 * t, t])
# N4-06: x + y = 1, x + a y = b
for a_ in (F(-1), F(0), F(3)):
    assert clasificar(M([1, 1, 1], [1, a_, 2])) == "SCD"
assert clasificar(M([1, 1, 1], [1, 1, 1])) == "SCI" and clasificar(M([1, 1, 1], [1, 1, 5])) == "SI"
# N5-01: cuadrada no invertible
asq = M([1, 1], [1, 1])
assert rango(asq) == 1 and clasificar(M([1, 1, 1], [1, 1, 3])) == "SI" and clasificar(M([1, 1, 1], [1, 1, 1])) == "SCI"

print("F11: todas las comprobaciones son correctas.")
