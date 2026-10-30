"""Comprueba con aritmética exacta los resultados de F09 (Gauss-Jordan, Unidad 5)
y los datos de las escenas L31–L33.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f09.py
"""

from fractions import Fraction as F


def M(*filas):
    return [[F(v) for v in fila] for fila in filas]


def sumar(m, i, j, k):
    """R_i <- R_i + k R_j."""
    assert i != j
    m = [f[:] for f in m]
    m[i] = [a + k * b for a, b in zip(m[i], m[j])]
    return m


def escalar(m, i, k):
    assert k != 0
    m = [f[:] for f in m]
    m[i] = [k * v for v in m[i]]
    return m


def intercambio(m, i, j):
    m = [f[:] for f in m]
    m[i], m[j] = m[j], m[i]
    return m


def aplicar(m, *ops):
    """Aplica en orden operaciones ("s", i, j, k), ("e", i, k) o ("i", i, j) (filas desde 0)."""
    for op in ops:
        m = {"s": sumar, "e": escalar, "i": intercambio}[op[0]](m, *op[1:])
    return m


def rref(a):
    """Forma escalonada reducida y columnas pivote."""
    a = [f[:] for f in a]
    fila, pivotes = 0, []
    for col in range(len(a[0])):
        p = next((i for i in range(fila, len(a)) if a[i][col] != 0), None)
        if p is None:
            continue
        a[fila], a[p] = a[p], a[fila]
        a[fila] = [v / a[fila][col] for v in a[fila]]
        for i in range(len(a)):
            if i != fila and a[i][col] != 0:
                a[i] = [x - a[i][col] * y for x, y in zip(a[i], a[fila])]
        pivotes.append(col)
        fila += 1
        if fila == len(a):
            break
    return a, pivotes


def es_reducida(a):
    """Escalonada, pivotes 1 y único elemento no nulo de su columna."""
    pivotes = [(i, next(j for j, v in enumerate(f) if v != 0)) for i, f in enumerate(a) if any(v != 0 for v in f)]
    n_nulas = len(a) - len(pivotes)
    if any(any(v != 0 for v in f) for f in a[len(a) - n_nulas:]) or any(not any(v != 0 for v in f) for f in a[:len(pivotes)]):
        return False  # filas nulas arriba
    if [j for _, j in pivotes] != sorted(set(j for _, j in pivotes)):
        return False
    return all(a[i][j] == 1 and all(a[k][j] == 0 for k in range(len(a)) if k != i) for i, j in pivotes)


def satisface(a, x):
    """x cumple todas las ecuaciones de [A | b]."""
    return all(sum(f[j] * x[j] for j in range(len(x))) == f[-1] for f in a)


# ---------------------------------------------------------------- L31: escenas
escalonada = M([1, 2, -1, -3], [0, -1, 3, 7], [0, 0, 10, 20])
reducida = M([1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 2])
assert rref(escalonada)[0] == reducida and es_reducida(reducida) and not es_reducida(escalonada)
assert satisface(M([1, 2, -1, -3], [2, 3, 1, 1], [-1, 1, 2, 2]), [1, -1, 2])  # el sistema de L26

# Parte 1: ¿reducida o no? (las cuatro matrices de la escena)
assert es_reducida(M([1, 0, 2], [0, 1, 3]))
assert not es_reducida(M([1, 0, 2], [0, 2, 3]))
assert not es_reducida(M([1, 2, 0], [0, 1, 3]))
assert es_reducida(M([1, 0, 3, 0], [0, 0, 0, 1], [0, 0, 0, 0]))

# Parte 2: el sistema de L15, con las operaciones exactas del video
s = M([1, 1, 1, 6], [1, -1, 1, 2], [1, 1, -1, 0])
paso = aplicar(s, ("s", 1, 0, F(-1)), ("s", 2, 0, F(-1)))
assert paso == M([1, 1, 1, 6], [0, -2, 0, -4], [0, 0, -2, -6])
paso = aplicar(paso, ("e", 1, F(-1, 2)), ("e", 2, F(-1, 2)))
assert paso == M([1, 1, 1, 6], [0, 1, 0, 2], [0, 0, 1, 3])
paso = aplicar(paso, ("s", 0, 2, F(-1)))
assert paso == M([1, 1, 0, 3], [0, 1, 0, 2], [0, 0, 1, 3])
paso = aplicar(paso, ("s", 0, 1, F(-1)))
assert paso == M([1, 0, 0, 1], [0, 1, 0, 2], [0, 0, 1, 3]) == rref(s)[0]
assert satisface(s, [1, 2, 3])

# Parte 3: dos caminos hasta la misma reducida
base = M([2, 4, 10], [3, -1, 1])
meta = M([1, 0, 1], [0, 1, 2])
camino_a = aplicar(base, ("s", 1, 0, F(-3, 2)), ("e", 1, F(-1, 7)), ("s", 0, 1, F(-4)), ("e", 0, F(1, 2)))
camino_b = aplicar(base, ("i", 0, 1), ("s", 1, 0, F(-2, 3)), ("e", 1, F(3, 14)), ("s", 0, 1, F(1)), ("e", 0, F(1, 3)))
assert camino_a == camino_b == meta == rref(base)[0]
assert aplicar(base, ("s", 1, 0, F(-3, 2)))[1] == [0, -7, -14]
assert aplicar(base, ("i", 0, 1), ("s", 1, 0, F(-2, 3)))[1] == [0, F(14, 3), F(28, 3)]

# ---------------------------------------------------------------- F09: ejercicios de L31
# N1-01: A y B sí; C no.
assert es_reducida(M([1, 0, 5], [0, 1, 2])) and es_reducida(M([1, 3, 0], [0, 0, 1]))
assert not es_reducida(M([1, 0, 0], [0, 1, 0], [0, 0, 2]))

# N1-02
assert rref(M([1, 3, 0, 2], [0, 1, 0, -1]))[0] == M([1, 0, 0, 5], [0, 1, 0, -1])
assert aplicar(M([1, 3, 0, 2], [0, 1, 0, -1]), ("s", 0, 1, F(-3))) == M([1, 0, 0, 5], [0, 1, 0, -1])

# N2-01: x + 2y = 7, 3x - y = 7
n201 = M([1, 2, 7], [3, -1, 7])
assert aplicar(n201, ("s", 1, 0, F(-3)))[1] == [0, -7, -14]
assert aplicar(n201, ("s", 1, 0, F(-3)), ("e", 1, F(-1, 7)), ("s", 0, 1, F(-2))) == M([1, 0, 3], [0, 1, 2]) == rref(n201)[0]
assert satisface(n201, [3, 2])

# N2-02: x + y + z = 2, 2x + 3y + z = 7, x - y + 2z = -3  ->  (1, 2, -1)
n202 = M([1, 1, 1, 2], [2, 3, 1, 7], [1, -1, 2, -3])
p = aplicar(n202, ("s", 1, 0, F(-2)), ("s", 2, 0, F(-1)))
assert p == M([1, 1, 1, 2], [0, 1, -1, 3], [0, -2, 1, -5])
p = aplicar(p, ("s", 2, 1, F(2)))
assert p == M([1, 1, 1, 2], [0, 1, -1, 3], [0, 0, -1, 1])
p = aplicar(p, ("e", 2, F(-1)))
assert p == M([1, 1, 1, 2], [0, 1, -1, 3], [0, 0, 1, -1])
p = aplicar(p, ("s", 1, 2, F(1)), ("s", 0, 2, F(-1)), ("s", 0, 1, F(-1)))
assert p == M([1, 0, 0, 1], [0, 1, 0, 2], [0, 0, 1, -1]) == rref(n202)[0]
assert satisface(n202, [1, 2, -1])

# N3-01: dos caminos para [[0, 2, 4], [1, 1, 3]]
n301 = M([0, 2, 4], [1, 1, 3])
a = aplicar(n301, ("i", 0, 1), ("e", 1, F(1, 2)), ("s", 0, 1, F(-1)))
b = aplicar(n301, ("e", 0, F(1, 2)), ("i", 0, 1), ("s", 0, 1, F(-1)))
assert a == b == M([1, 0, 1], [0, 1, 2]) == rref(n301)[0]

# N3-02: verdadero o falso
assert es_reducida(reducida) and True                                  # a) reducida => escalonada: V
assert not es_reducida(M([1, 2], [0, 1]))                               # b) escalonada con pivotes 1 no basta: F
assert rref(M([1, 2], [0, 1]))[0] == M([1, 0], [0, 1])
assert rref(M([2, 4, 10], [3, -1, 1]))[0] == rref(M([0, 14, 28], [3, -1, 1]))[0]   # c) equivalentes => misma reducida: V

# N3-03: con fracciones en el camino
n303 = M([2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3])
p = aplicar(n303, ("e", 0, F(1, 2)))
assert p[0] == [1, F(1, 2), F(-1, 2), 4]
p = aplicar(p, ("s", 1, 0, F(3)), ("s", 2, 0, F(2)))
assert p == M([1, F(1, 2), F(-1, 2), 4], [0, F(1, 2), F(1, 2), 1], [0, 2, 1, 5])
p = aplicar(p, ("e", 1, F(2)), ("s", 2, 1, F(-2)), ("e", 2, F(-1)))
assert p == M([1, F(1, 2), F(-1, 2), 4], [0, 1, 1, 2], [0, 0, 1, -1])
p = aplicar(p, ("s", 1, 2, F(-1)), ("s", 0, 2, F(1, 2)))
assert p == M([1, F(1, 2), 0, F(7, 2)], [0, 1, 0, 3], [0, 0, 1, -1])
p = aplicar(p, ("s", 0, 1, F(-1, 2)))
assert p == M([1, 0, 0, 2], [0, 1, 0, 3], [0, 0, 1, -1]) == rref(n303)[0]
assert satisface(n303, [2, 3, -1])

# ---------------------------------------------------------------- L32: escenas y ejercicios
lectura = M([1, 2, 0, -1, 3], [0, 0, 1, 4, 2], [0, 0, 0, 0, 0])
assert es_reducida(lectura) and rref(lectura) == (lectura, [0, 2])
sistema_32 = lectura  # x1 + 2 x2 - x4 = 3,  x3 + 4 x4 = 2
for s_, t_ in ((F(1), F(0)), (F(0), F(1)), (F(5, 3), F(-7, 2))):
    assert satisface(sistema_32, [3 - 2 * s_ + t_, s_, 2 - 4 * t_, t_])
assert satisface(sistema_32, [1, 1, 2, 0]) and satisface(sistema_32, [4, 0, -2, 1])

# Tres finales posibles: la columna de b es pivote o no, y cuántas columnas de incógnitas tienen pivote
def clasificar(a):
    r, piv = rref(a)
    n = len(a[0]) - 1
    return "SI" if n in piv else ("SCD" if len(piv) == n else "SCI")

assert clasificar(M([1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 2])) == "SCD"
assert clasificar(M([1, 0, 2, 3], [0, 1, -1, 1], [0, 0, 0, 0])) == "SCI"
assert clasificar(M([1, 0, 2, 3], [0, 1, -1, 1], [0, 0, 0, 1])) == "SI"

# N2-03: x + 2y + z = 3, 2x + 4y + 3z = 8  ->  reducida [[1,2,0,1],[0,0,1,2]], (1 - 2t, t, 2)
n203 = M([1, 2, 1, 3], [2, 4, 3, 8])
assert rref(n203) == (M([1, 2, 0, 1], [0, 0, 1, 2]), [0, 2])
assert aplicar(n203, ("s", 1, 0, F(-2)), ("s", 0, 1, F(-1))) == M([1, 2, 0, 1], [0, 0, 1, 2])
for t_ in (F(0), F(1), F(-3, 2)):
    assert satisface(n203, [1 - 2 * t_, t_, 2])

# N2-04: tres ecuaciones, cuatro incógnitas, una redundante y dos libres
n204 = M([1, 1, 1, 1, 4], [1, 2, 3, 4, 10], [2, 3, 4, 5, 14])
assert rref(n204) == (M([1, 0, -1, -2, -2], [0, 1, 2, 3, 6], [0, 0, 0, 0, 0]), [0, 1])
for s_, t_ in ((F(0), F(0)), (F(1), F(0)), (F(0), F(1)), (F(2, 3), F(-5))):
    assert satisface(n204, [-2 + s_ + 2 * t_, 6 - 2 * s_ - 3 * t_, s_, t_])

# N3-04: a) SCI, b) SCD (5, 3, 0), c) SI
assert clasificar(M([1, 0, 3, 2], [0, 1, -1, 4])) == "SCI"
for t_ in (F(0), F(2), F(-1, 3)):
    assert satisface(M([1, 0, 3, 2], [0, 1, -1, 4]), [2 - 3 * t_, 4 + t_, t_])
assert clasificar(M([1, 0, 0, 5], [0, 1, 0, 3], [0, 0, 1, 0])) == "SCD"
assert clasificar(M([1, 2, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])) == "SI"

# N4-01: homogéneo 3 x 4 con un parámetro, x = -2t
n401 = M([1, 2, -1, 3, 0], [2, 4, 0, 8, 0], [-1, -2, 2, -4, 0])
assert rref(n401) == (M([1, 2, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0]), [0, 2, 3])
for t_ in (F(1), F(-4), F(3, 7)):
    assert satisface(n401, [-2 * t_, t_, 0, 0])

# N4-02: 3 ecuaciones, 5 incógnitas: nunca SCD; con A != 0, SCI tiene entre 2 y 4 parámetros
import itertools, random
random.seed(1)
for _ in range(300):
    a = [[F(random.randint(-2, 2)) for _ in range(6)] for _ in range(3)]
    assert clasificar(a) != "SCD"
    piv = rref(a)[1]
    if clasificar(a) == "SCI" and any(v != 0 for f in a for v in f[:5]):
        assert 2 <= 5 - len(piv) <= 4

# N5-01: SCD <=> n pivotes (y ninguno en b); con una columna sin pivote hay al menos dos soluciones
for _ in range(300):
    a = [[F(random.randint(-2, 2)) for _ in range(4)] for _ in range(3)]
    c = clasificar(a)
    n_piv = len(rref(a)[1])
    assert (c == "SCD") == (3 not in rref(a)[1] and n_piv == 3)

# ---------------------------------------------------------------- L33: conteo de operaciones
def contar_gauss(n):
    a = [[F(1 if i == j else 0) + F(1, i + j + 2) + (n if i == j else 0) for j in range(n)] + [F(i + 1)] for i in range(n)]
    original, ops = [f[:] for f in a], 0
    for k in range(n - 1):
        for i in range(k + 1, n):
            m = a[i][k] / a[k][k]; ops += 1
            for j in range(k + 1, n + 1):
                a[i][j] -= m * a[k][j]; ops += 1
            a[i][k] = F(0)
    x = [F(0)] * n
    for i in range(n - 1, -1, -1):
        suma = F(0)
        for j in range(i + 1, n):
            suma += a[i][j] * x[j]; ops += 1
        x[i] = (a[i][n] - suma) / a[i][i]; ops += 1
    assert satisface(original, x)
    return ops


def contar_jordan(n):
    a = [[F(1 if i == j else 0) + F(1, i + j + 2) + (n if i == j else 0) for j in range(n)] + [F(i + 1)] for i in range(n)]
    original, ops = [f[:] for f in a], 0
    for k in range(n):
        for j in range(k + 1, n + 1):
            a[k][j] /= a[k][k]; ops += 1
        a[k][k] = F(1)
        for i in range(n):
            if i != k:
                f = a[i][k]
                for j in range(k + 1, n + 1):
                    a[i][j] -= f * a[k][j]; ops += 1
                a[i][k] = F(0)
    assert satisface(original, [a[i][n] for i in range(n)])
    return ops


for n in range(2, 13):
    assert contar_gauss(n) == (n**3 + 3 * n**2 - n) // 3, n
    assert contar_jordan(n) == (n**3 + n**2) // 2, n
assert (contar_gauss(3), contar_jordan(3)) == (17, 18)
assert [(n**3 + 3 * n**2 - n) // 3 for n in (4, 5)] == [36, 65] and [(n**3 + n**2) // 2 for n in (4, 5)] == [40, 75]
assert [((n**3 + n**2) // 2, (n**3 + 3 * n**2 - n) // 3) for n in (10, 100, 1000)] == [(550, 430), (505000, 343300), (500500000, 334333000)]
# n(n-1)(2n+5)/6 es la eliminación y n(n+1)/2 la sustitución
assert all(n * (n - 1) * (2 * n + 5) // 6 + n * (n + 1) // 2 == (n**3 + 3 * n**2 - n) // 3 for n in range(1, 50))
# el cociente tiende a 3/2 por debajo
assert all(F(n**3 + n**2, 2) / F(n**3 + 3 * n**2 - n, 3) < F(3, 2) for n in range(2, 200))

print("F09: todas las comprobaciones son correctas.")
