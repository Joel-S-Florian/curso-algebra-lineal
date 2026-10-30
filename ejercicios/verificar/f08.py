"""Comprueba con aritmética exacta los resultados de F08 (eliminación de Gauss, Unidad 4)
y los datos de las escenas L24–L30.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f08.py
"""

from fractions import Fraction as F


def M(*filas):
    return [[F(v) for v in fila] for fila in filas]


def intercambio(m, i, j):
    m = [f[:] for f in m]
    m[i], m[j] = m[j], m[i]
    return m


def escalar(m, i, k):
    assert k != 0
    m = [f[:] for f in m]
    m[i] = [k * v for v in m[i]]
    return m


def sumar(m, i, j, k):
    """R_i <- R_i + k R_j."""
    assert i != j
    m = [f[:] for f in m]
    m[i] = [a + k * b for a, b in zip(m[i], m[j])]
    return m


def pivotes(a):
    """Posiciones (fila, columna) de las primeras entradas no nulas de cada fila."""
    return [(i, next(j for j, v in enumerate(f) if v != 0)) for i, f in enumerate(a) if any(v != 0 for v in f)]


def es_escalonada(a):
    nulas = [all(v == 0 for v in f) for f in a]
    if nulas != sorted(nulas):  # alguna fila nula por encima de una no nula
        return False
    columnas = [c for _, c in pivotes(a)]
    return all(x < y for x, y in zip(columnas, columnas[1:]))


def escalonar(m):
    """Eliminación hacia adelante con intercambio si el pivote es 0. Devuelve la matriz escalonada."""
    m = [f[:] for f in m]
    fila = 0
    for col in range(len(m[0]) - 1):
        candidata = next((r for r in range(fila, len(m)) if m[r][col] != 0), None)
        if candidata is None:
            continue
        m = intercambio(m, fila, candidata)
        for r in range(fila + 1, len(m)):
            m = sumar(m, r, fila, -m[r][col] / m[fila][col])
        fila += 1
    return m


def clasificar(m):
    """('SI' | 'SCD' | 'SCI', número de variables libres) de la matriz aumentada m."""
    e = escalonar(m)
    n = len(m[0]) - 1
    if any(c == n for _, c in pivotes(e)):
        return "SI", None
    libres = n - len(pivotes(e))
    return ("SCD" if libres == 0 else "SCI"), libres


def cumple(m, x):
    return all(sum(a * v for a, v in zip(f[:-1], x)) == f[-1] for f in m)


def eq(m, *filas):
    return m == M(*filas)


# ---------------------------------------------------------------- escenas L24
S = M([0, 3, 6], [1, 1, 3])
assert eq(intercambio(S, 0, 1), [1, 1, 3], [0, 3, 6]) and cumple(S, (1, 2))
S0 = M([2, 4, 10], [3, -1, 1])
S1 = escalar(S0, 0, F(1, 2))
S2 = sumar(S1, 1, 0, -3)
S3 = escalar(S2, 1, F(-1, 7))
assert eq(S1, [1, 2, 5], [3, -1, 1]) and eq(S2, [1, 2, 5], [0, -7, -14]) and eq(S3, [1, 2, 5], [0, 1, 2])
assert all(cumple(s, (1, 2)) for s in (S0, S1, S2, S3))
assert cumple(M([1, 2, 5], [0, 0, 0]), (5, 0)) and not cumple(S1, (5, 0))  # 0·R2 añade soluciones
assert sumar(S2, 1, 0, 3) == S1  # ida y vuelta
assert (3 * 1 - 2) - 3 * (1 + 4) == 1 - 3 * 5 == -14  # combinación en (1, 2)

# F08-N1-01
A = M([2, -1, 3], [1, 4, 6])
assert cumple(A, (2, 1))
assert eq(intercambio(A, 0, 1), [1, 4, 6], [2, -1, 3])
assert eq(escalar(A, 1, 3), [2, -1, 3], [3, 12, 18])
assert eq(sumar(A, 1, 0, -2), [2, -1, 3], [-3, 6, 0])
assert all(cumple(x, (2, 1)) for x in (intercambio(A, 0, 1), escalar(A, 1, 3), sumar(A, 1, 0, -2)))

# F08-N2-01
N = M([1, 3, 2], [0, -5, 1])
Morig = sumar(N, 1, 0, 2)
assert eq(Morig, [1, 3, 2], [2, 1, 5]) and sumar(Morig, 1, 0, -2) == N
sol = (F(13, 5), F(-1, 5))
assert cumple(N, sol) and cumple(Morig, sol)

# F08-N4-01: c) R2 <- 2R2 + R1 es escalar por 2 y luego sumar R1 (reversible); d) y e) no
assert sumar(escalar(A, 1, 2), 1, 0, 1) == M([2, -1, 3], [4, 7, 15]) and cumple(M([2, -1, 3], [4, 7, 15]), (2, 1))
assert not cumple(M([3, 0, 4], [1, 4, 6]), (2, 1))  # d) R1 + 1 cambia las soluciones

# F08-N5-01: el intercambio se obtiene con reemplazos y un escalado
X = M([1, 2, 3], [4, 5, 6])
Y = escalar(sumar(sumar(sumar(X, 0, 1, 1), 1, 0, -1), 0, 1, 1), 1, -1)
assert Y == intercambio(X, 0, 1)

# F08-N5-02: R_i <- a R_i + b R_j con a = 0 puede añadir soluciones
B = M([1, 1, 2], [1, -1, 0])
assert clasificar(B) == ("SCD", 0) and clasificar(M([1, 1, 2], [1, 1, 2])) == ("SCI", 1)  # R2 <- 0R2 + R1

# ---------------------------------------------------------------- L25
assert es_escalonada(M([1, 1, 1, 6], [0, -2, 0, -4], [0, 0, -2, -6]))
ejemplos = [([[1, 3, 2], [0, 0, 4], [0, 0, 0]], True), ([[1, 2, 3], [0, 0, 0], [0, 4, 5]], False),
            ([[2, 1, 0], [1, 3, 1], [0, 0, 1]], False), ([[0, 1, 2], [0, 0, 3], [0, 0, 0]], True)]
assert all(es_escalonada(M(*a)) == v for a, v in ejemplos)
E = M([1, 2, 0, -1, 3], [0, 0, 2, 4, 2], [0, 0, 0, 0, 0])
assert es_escalonada(E) and pivotes(E) == [(0, 0), (1, 2)]
# Camino A y camino B
ruta_a = sumar(S0, 1, 0, F(-3, 2))
ruta_b = sumar(intercambio(S0, 0, 1), 1, 0, F(-2, 3))
assert eq(ruta_a, [2, 4, 10], [0, -7, -14]) and eq(ruta_b, [3, -1, 1], [0, F(14, 3), F(28, 3)])
assert pivotes(ruta_a) == pivotes(ruta_b) and cumple(ruta_a, (1, 2)) and cumple(ruta_b, (1, 2))

# F08-N1-02
casos = {"a": ([[3, 1, 0], [0, 0, 2], [0, 0, 0]], True), "b": ([[1, 2], [0, 0], [0, 5]], False),
         "c": ([[0, 4, 1], [0, 0, 0]], True), "d": ([[1, 0, 2], [1, 3, 0], [0, 0, 4]], False)}
assert all(es_escalonada(M(*a)) == v for a, v in casos.values())
assert pivotes(M(*casos["a"][0])) == [(0, 0), (1, 2)] and pivotes(M(*casos["c"][0])) == [(0, 1)]

# F08-N2-02
P = M([2, 6, 4], [1, 4, 3])
pa = sumar(P, 1, 0, F(-1, 2))
pb = sumar(intercambio(P, 0, 1), 1, 0, -2)
assert eq(pa, [2, 6, 4], [0, 1, 1]) and eq(pb, [1, 4, 3], [0, -2, -2])
assert pivotes(pa) == pivotes(pb) and cumple(P, (-1, 1)) and cumple(pa, (-1, 1)) and cumple(pb, (-1, 1))

# ---------------------------------------------------------------- L26
G2 = M([2, 3, 8], [4, -1, 2])
assert eq(sumar(G2, 1, 0, -2), [2, 3, 8], [0, -7, -14]) and cumple(G2, (1, 2))
G2b = M([2, 3, 8], [3, 1, 5])
assert eq(sumar(G2b, 1, 0, F(-3, 2)), [2, 3, 8], [0, F(-7, 2), -7]) and cumple(G2b, (1, 2))
assert eq(sumar(escalar(G2b, 1, 2), 1, 0, -3), [2, 3, 8], [0, -7, -14])  # R2 <- 2R2 - 3R1
G3 = M([1, 2, -1, -3], [2, 3, 1, 1], [-1, 1, 2, 2])
g = sumar(sumar(G3, 1, 0, -2), 2, 0, 1)
assert eq(g, [1, 2, -1, -3], [0, -1, 3, 7], [0, 3, 1, -1])
g = sumar(g, 2, 1, 3)
assert eq(g, [1, 2, -1, -3], [0, -1, 3, 7], [0, 0, 10, 20]) and cumple(G3, (1, -1, 2)) and cumple(g, (1, -1, 2))

# F08-N2-03
assert eq(sumar(M([3, 2, 7], [6, -1, 4]), 1, 0, -2), [3, 2, 7], [0, -5, -10]) and cumple(M([3, 2, 7], [6, -1, 4]), (1, 2))
# F08-N2-04
H = M([1, 1, 2, 3], [2, 3, 1, 2], [-1, 2, 3, -1])
h = sumar(sumar(sumar(H, 1, 0, -2), 2, 0, 1), 2, 1, -3)
assert eq(h, [1, 1, 2, 3], [0, 1, -3, -4], [0, 0, 14, 14]) and cumple(H, (2, -1, 1))
# F08-N3-01
K = M([2, 1, 1, 3], [1, -1, 2, 3], [3, 0, 1, 2])
k = intercambio(K, 0, 1)
k = sumar(sumar(k, 1, 0, -2), 2, 0, -3)
assert eq(k, [1, -1, 2, 3], [0, 3, -3, -3], [0, 3, -5, -7])
k = sumar(k, 2, 1, -1)
assert eq(k, [1, -1, 2, 3], [0, 3, -3, -3], [0, 0, -2, -4]) and cumple(K, (0, 1, 2))

# ---------------------------------------------------------------- L27
Z = M([1, 1, 1, 3], [2, 2, 1, 5], [1, 2, 3, 6])
z = sumar(sumar(Z, 1, 0, -2), 2, 0, -1)
assert eq(z, [1, 1, 1, 3], [0, 0, -1, -1], [0, 1, 2, 3])
z = intercambio(z, 1, 2)
assert es_escalonada(z) and cumple(Z, (1, 1, 1))
W = sumar(M([1, 2, 1, 4], [0, 0, 3, 3], [0, 0, 1, 1]), 2, 1, F(-1, 3))
assert eq(W, [1, 2, 1, 4], [0, 0, 3, 3], [0, 0, 0, 0]) and pivotes(W) == [(0, 0), (1, 2)]
R = M([1, 1, 3], [1, -1, 1], [3, 1, 7])
r = sumar(sumar(sumar(R, 1, 0, -1), 2, 0, -3), 2, 1, -1)
assert eq(r, [1, 1, 3], [0, -2, -2], [0, 0, 0]) and cumple(R, (2, 1))
assert [2 * a + b for a, b in zip(R[0], R[1])] == R[2]  # E3 = 2E1 + E2
assert clasificar(M([1, 1, 3], [1, -1, 1], [3, 1, 8]))[0] == "SI"  # con 8: [0 0 | 1]

# F08-N2-05
Q = M([1, 2, 1, 4], [2, 4, 3, 9], [1, 3, 2, 6])
q = sumar(sumar(Q, 1, 0, -2), 2, 0, -1)
assert eq(q, [1, 2, 1, 4], [0, 0, 1, 1], [0, 1, 1, 2]) and es_escalonada(intercambio(q, 1, 2)) and cumple(Q, (1, 1, 1))
# F08-N3-02
T = M([1, 2, 4], [2, -1, 3], [4, 3, 11])
assert [2 * a + b for a, b in zip(T[0], T[1])] == T[2] and cumple(T, (2, 1)) and clasificar(T) == ("SCD", 0)
t = sumar(sumar(sumar(T, 1, 0, -2), 2, 0, -4), 2, 1, -1)
assert eq(t, [1, 2, 4], [0, -5, -5], [0, 0, 0])

# ---------------------------------------------------------------- L28
C8 = M([1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, 8])
c = sumar(sumar(sumar(C8, 1, 0, -1), 2, 0, -2), 2, 1, -1)
assert eq(c, [1, 1, 1, 2], [0, 1, 2, 3], [0, 0, 0, 1]) and clasificar(C8)[0] == "SI"
assert [a - b - d for a, b, d in zip(C8[2], C8[0], C8[1])] == [0, 0, 0, 1]  # E3 - E1 - E2: 0 = 1
C7 = M([1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, 7])
assert clasificar(C7) == ("SCI", 1)
for tt in map(F, (-3, 0, 1, F(5, 2), 7)):
    assert cumple(C7, (-1 + tt, 3 - 2 * tt, tt))
for s_, tt in ((0, 0), (1, 2), (F(-1, 3), 4)):
    assert cumple(M([1, 2, -1, 3]), (3 - 2 * s_ + tt, s_, tt))  # dos libres

# F08-N2-06 y F08-N3-03
I6 = M([1, 2, -1, 1], [2, 3, 1, 4], [3, 5, 0, 6])
i6 = sumar(sumar(I6, 1, 0, -2), 2, 0, -3)
assert eq(i6, [1, 2, -1, 1], [0, -1, 3, 2], [0, -1, 3, 3]) and eq(sumar(i6, 2, 1, -1)[2:], [0, 0, 0, 1])
assert [a - b - d for a, b, d in zip(I6[2], I6[0], I6[1])] == [0, 0, 0, 1] and clasificar(I6)[0] == "SI"
I5 = M([1, 2, -1, 1], [2, 3, 1, 4], [3, 5, 0, 5])
assert clasificar(I5) == ("SCI", 1)
for tt in map(F, (-2, 0, 1, F(1, 3))):
    assert cumple(I5, (5 - 5 * tt, -2 + 3 * tt, tt))

# F08-N4-02
assert clasificar(M([1, 2, -1, 3], [0, 1, 4, 2], [0, 0, 0, 5]))[0] == "SI"
assert clasificar(M([1, 2, -1, 3], [0, 0, 1, 2], [0, 0, 0, 0])) == ("SCI", 1)
assert clasificar(M([2, 1, 1], [0, 3, 0])) == ("SCD", 0)
assert clasificar(M([1, -1, 2, 0, 1], [0, 0, 1, 3, 4])) == ("SCI", 2)

# F08-N5-03 (ejemplo): sin fila [0 ... 0 | c], sustituir hacia atrás con libres arbitrarias funciona
assert cumple(M([1, 2, -1, 3], [0, 0, 1, 2]), (3 - 2 * 5 + 2, 5, 2))

# ---------------------------------------------------------------- L29 (parámetro a: valores de prueba)
muestras = [F(v) for v in (-7, -3, F(-1, 2), 0, F(1, 3), 3, 5, 10)]


def sistema_l29_1(a):
    return M([1, 1, 1], [2, a, 3])


assert clasificar(sistema_l29_1(2))[0] == "SI"
for a in muestras:
    if a != 2:
        assert clasificar(sistema_l29_1(a)) == ("SCD", 0) and cumple(sistema_l29_1(a), ((a - 3) / (a - 2), 1 / (a - 2)))
assert cumple(sistema_l29_1(3), (0, 1))


def sistema_l29_2(a):
    return M([1, 1, 1, 1], [1, 2, 2, 2], [1, 2, a * a + 1, a + 1])


for a in muestras + [F(2)]:
    m2 = sumar(sumar(sumar(sistema_l29_2(a), 1, 0, -1), 2, 0, -1), 2, 1, -1)
    assert m2[2] == [0, 0, a * a - 1, a - 1]
    if a not in (1, -1):
        assert clasificar(sistema_l29_2(a)) == ("SCD", 0) and cumple(sistema_l29_2(a), (0, a / (a + 1), 1 / (a + 1)))
assert clasificar(sistema_l29_2(F(1))) == ("SCI", 1) and clasificar(sistema_l29_2(F(-1)))[0] == "SI"
assert all(cumple(sistema_l29_2(F(1)), (0, 1 - tt, tt)) for tt in map(F, (-1, 0, 2)))
assert cumple(sistema_l29_2(F(0)), (0, 0, 1))


# F08-N4-03
def n4_03(a):
    return M([1, 2, 3], [2, a, 6])


assert clasificar(n4_03(F(4))) == ("SCI", 1) and all(cumple(n4_03(F(4)), (3 - 2 * tt, tt)) for tt in map(F, (0, 1, -2)))
assert all(clasificar(n4_03(a)) == ("SCD", 0) and cumple(n4_03(a), (3, 0)) for a in muestras if a != 4)


# F08-N4-04
def n4_04(a):
    return M([1, 1, 1, 1], [1, 2, 2, 3], [1, 2, a * a - 2, a + 1])


for a in muestras:
    if a not in (2, -2):
        assert clasificar(n4_04(a)) == ("SCD", 0) and cumple(n4_04(a), (-1, (2 * a + 3) / (a + 2), 1 / (a + 2)))
assert clasificar(n4_04(F(2))) == ("SCI", 1) and all(cumple(n4_04(F(2)), (-1, 2 - tt, tt)) for tt in map(F, (0, 1, 5)))
assert clasificar(n4_04(F(-2)))[0] == "SI"
assert sumar(sumar(sumar(n4_04(F(-2)), 1, 0, -1), 2, 0, -1), 2, 1, -1)[2] == [0, 0, 0, -4]


# F08-N4-05
def n4_05(a):
    return M([1, a, 1], [a, 1, 1])


assert clasificar(n4_05(F(1))) == ("SCI", 1) and clasificar(n4_05(F(-1)))[0] == "SI"
for a in muestras:
    if a not in (1, -1):
        assert clasificar(n4_05(a)) == ("SCD", 0) and cumple(n4_05(a), (1 / (1 + a), 1 / (1 + a)))
assert sumar(n4_05(F(3)), 1, 0, F(-3)) == M([1, 3, 1], [0, -8, -2])  # [0, 1 - a^2 | 1 - a] con a = 3

# ---------------------------------------------------------------- L30
V = M([1, -2, 3], [3, -4, 5])
assert eq(sumar(V, 1, 0, -3), [1, -2, 3], [0, 2, -4]) and cumple(V, (-1, -2))
mal = M([1, -2, 3], [0, -10, -4])
x_mal = (F(19, 5), F(2, 5))
assert cumple(mal, x_mal) and not cumple(V, x_mal) and 3 * x_mal[0] - 4 * x_mal[1] == F(49, 5)
assert [v + 3 for v in M([1, 1, 2])[0]] == [4, 4, 5] and not cumple(M([4, 4, 5]), (1, 1))  # R1 + 3 no es elemental
D = M([1, 1, 2], [1, -1, 0])
simultaneo = [[a - b for a, b in zip(D[0], D[1])], [b - a for a, b in zip(D[0], D[1])]]
assert simultaneo == M([0, 2, 2], [0, -2, -2]) and clasificar(simultaneo) == ("SCI", 1) and clasificar(D) == ("SCD", 0)
assert cumple(D, (1, 1))
en_orden = sumar(sumar(D, 0, 1, -1), 1, 0, -1)  # F08-N4-06: de una en una
assert eq(en_orden, [0, 2, 2], [1, -3, -2]) and cumple(en_orden, (1, 1)) and clasificar(en_orden) == ("SCD", 0)
# F08-N3-04
U = M([2, 1, 5], [4, -3, 5])
assert eq(sumar(U, 1, 0, -2), [2, 1, 5], [0, -5, -5]) and cumple(U, (2, 1)) and not cumple(U, (0, 5))
# F08-N4-06 (escena: dos operaciones a la vez) — mismos datos que D
# F08-N4-07
L = M([1, 1, 1, 6], [1, -1, 2, 5], [2, 1, -1, 1])
assert not cumple(L, (2, 1, 3)) and cumple(L, (1, 2, 3))
l = sumar(sumar(L, 1, 0, -1), 2, 0, -2)
assert eq(l, [1, 1, 1, 6], [0, -2, 1, -1], [0, -1, -3, -11])
l = sumar(l, 2, 1, F(-1, 2))
assert eq(l, [1, 1, 1, 6], [0, -2, 1, -1], [0, 0, F(-7, 2), F(-21, 2)])

print("F08: todas las comprobaciones son correctas.")
