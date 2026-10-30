"""Comprueba con aritmética exacta los resultados de F10 (factorización LU, Unidad 6)
y los datos de las escenas L34–L38.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/f10.py
"""

from decimal import Context, Decimal as D
from fractions import Fraction as F
from itertools import permutations


def mul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


def M(*filas):
    return [[F(v) for v in f] for f in filas]


def T(X):
    return [list(f) for f in zip(*X)]


def lu(A):
    """A = L U sin pivoteo (falla si aparece un pivote 0). Devuelve (L, U)."""
    n = len(A)
    U = [f[:] for f in A]
    L = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n - 1):
        assert U[k][k] != 0, "pivote 0: hace falta intercambiar filas"
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            U[i] = [a - L[i][k] * b for a, b in zip(U[i], U[k])]
    return L, U


def adelante(L, b):
    y = []
    for i in range(len(L)):
        y.append((b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i])
    return y


def atras(U, y):
    n = len(U)
    x = [F(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x


def resolver(A, b):
    L, U = lu(A)
    return atras(U, adelante(L, b))


def triangular_inf(X):
    return all(X[i][j] == 0 for i in range(len(X)) for j in range(i + 1, len(X)))


def triangular_sup(X):
    return triangular_inf(T(X))


def falla(A):
    try:
        lu(A)
    except AssertionError:
        return True
    return False


# ------------------------------------------------------------ ejemplo común (L26, L34–L36)
A = M([1, 2, -1], [2, 3, 1], [-1, 1, 2])
L = M([1, 0, 0], [2, 1, 0], [-1, -3, 1])
U = M([1, 2, -1], [0, -1, 3], [0, 0, 10])
assert lu(A) == (L, U) and mul(L, U) == A
assert triangular_inf(L) and triangular_sup(U)
b = [F(-3), F(1), F(2)]
y = adelante(L, b)
assert y == [-3, 7, 20] and atras(U, y) == [1, -1, 2] == resolver(A, b)
# entrada (3, 2) de A en la escena: fila 3 de L por columna 2 de U = -2 + 3 + 0 = 1
assert sum(L[2][k] * U[k][1] for k in range(3)) == 1
# matrices elementales de la L34 y su efecto
E21 = M([1, 0, 0], [-2, 1, 0], [0, 0, 1])
E31 = M([1, 0, 0], [0, 1, 0], [1, 0, 1])
E32 = M([1, 0, 0], [0, 1, 0], [0, 3, 1])
assert mul(E21, A) == M([1, 2, -1], [0, -1, 3], [-1, 1, 2])
assert mul(E31, mul(E21, A)) == M([1, 2, -1], [0, -1, 3], [0, 3, 1])
assert mul(E32, mul(E31, mul(E21, A))) == U
# L35: L = producto de las inversas, y el orden contrario da -7
E21i = M([1, 0, 0], [2, 1, 0], [0, 0, 1])
E31i = M([1, 0, 0], [0, 1, 0], [-1, 0, 1])
E32i = M([1, 0, 0], [0, 1, 0], [0, -3, 1])
I3 = M([1, 0, 0], [0, 1, 0], [0, 0, 1])
assert mul(E21, E21i) == mul(E31, E31i) == mul(E32, E32i) == I3
assert mul(E31i, E32i) == M([1, 0, 0], [0, 1, 0], [-1, -3, 1])
assert mul(E21i, mul(E31i, E32i)) == L
assert mul(E32i, mul(E31i, E21i)) == M([1, 0, 0], [2, 1, 0], [-7, -3, 1])
# L36: L^-1 b = y (y es b después de la eliminación)
assert mul(E32, mul(E31, mul(E21, [[v] for v in b]))) == [[-3], [7], [20]]
# ejemplo completo de L36 (y N3-01)
A2 = M([2, 1, 1], [4, -6, 0], [-2, 7, 2])
b2 = [F(5), F(-2), F(9)]
L2, U2 = lu(A2)
assert L2 == M([1, 0, 0], [2, 1, 0], [-1, -1, 1]) and U2 == M([2, 1, 1], [0, -8, -2], [0, 0, 1])
assert adelante(L2, b2) == [5, -12, 2] and atras(U2, adelante(L2, b2)) == [1, 1, 2]
assert mul(A2, [[1], [1], [2]]) == [[5], [-2], [9]]

# ------------------------------------------------------------ F10: ejercicios
# N1-01
assert mul(M([1, 0], [3, 1]), M([2, 1], [0, 4])) == M([2, 1], [6, 7])
# N2-01
assert adelante(M([2, 0], [1, 3]), [F(6), F(5)]) == [3, F(2, 3)]
assert atras(M([1, -1, 2], [0, 4, -1], [0, 0, 2]), [F(3), F(7), F(6)]) == [F(-1, 2), F(5, 2), 3]
# N2-02: R3 <- R3 - 4 R1
E = M([1, 0, 0], [0, 1, 0], [-4, 0, 1])
Ei = M([1, 0, 0], [0, 1, 0], [4, 0, 1])
assert mul(E, Ei) == mul(Ei, E) == I3
assert mul(E, A)[2] == [a - 4 * c for a, c in zip(A[2], A[0])]
# N2-03
assert lu(M([4, 3], [8, 5])) == (M([1, 0], [2, 1]), M([4, 3], [0, -1]))
# N4-01 (con fracciones)
A41 = M([2, 4, -2], [1, 3, 0], [3, 7, 4])
L41, U41 = lu(A41)
assert L41 == M([1, 0, 0], [F(1, 2), 1, 0], [F(3, 2), 1, 1]) and U41 == M([2, 4, -2], [0, 1, 1], [0, 0, 6]) and mul(L41, U41) == A41
# N5-01 (unicidad): con L de unos y U invertible, L1 U1 = L2 U2 obliga a L1 = L2; se comprueba en un caso
assert lu(M([2, 1], [6, 7])) == (M([1, 0], [3, 1]), M([2, 1], [0, 4]))

# L36 N2-04 y N3-03
assert adelante(M([1, 0], [3, 1]), [F(3), F(13)]) == [3, 4]
assert atras(M([2, 1], [0, 4]), [F(3), F(4)]) == [1, 1]
b33 = [F(0), F(1), F(-3)]
assert mul(A, [[2], [-1], [0]]) == [[0], [1], [-3]]
assert adelante(L, b33) == [0, 1, 0] and atras(U, [F(0), F(1), F(0)]) == [2, -1, 0]


# L36 N4-02: operaciones de la factorización (sin b) y de las sustituciones
def contar_lu(n):
    ops = 0
    for k in range(n - 1):
        for i in range(k + 1, n):
            ops += 1                      # multiplicador
            ops += n - k - 1              # a_ij - m a_kj, j = k + 1 .. n
    return ops


for n in range(2, 12):
    assert contar_lu(n) == (n**3 - n) // 3, n
    assert n * (n - 1) // 2 + n * (n + 1) // 2 == n * n
assert contar_lu(3) == 8 and 3 * 2 // 2 == 3 and 3 * 4 // 2 == 6 and 8 + 9 == 17

# L37: PA = LU
A4 = M([1, 1, 1], [2, 2, 5], [4, 6, 8])
assert falla(A4)
P = M([1, 0, 0], [0, 0, 1], [0, 1, 0])
PA = mul(P, A4)
assert PA == M([1, 1, 1], [4, 6, 8], [2, 2, 5])
L4, U4 = lu(PA)
assert L4 == M([1, 0, 0], [4, 1, 0], [2, 0, 1]) and U4 == M([1, 1, 1], [0, 2, 4], [0, 0, 3])
b4 = [F(3), F(9), F(18)]
Pb = [sum(P[i][j] * b4[j] for j in range(3)) for i in range(3)]
assert Pb == [3, 18, 9] and adelante(L4, Pb) == [3, 6, 3] and atras(U4, adelante(L4, Pb)) == [1, 1, 1]
assert mul(A4, [[1], [1], [1]]) == [[3], [9], [18]]
# N2-05
assert falla(M([0, 2], [3, 1]))
assert mul(M([0, 1], [1, 0]), M([0, 2], [3, 1])) == M([3, 1], [0, 2])
# N3-05: matrices de permutación
perm = M([0, 0, 1], [1, 0, 0], [0, 1, 0])
assert mul(perm, A)[0] == A[2] and mul(perm, A)[1] == A[0] and mul(perm, A)[2] == A[1]
assert mul(perm, T(perm)) == I3
assert len(list(permutations(range(4)))) == 24 and len(list(permutations(range(3)))) == 6
for p in permutations(range(4)):
    Pm = [[F(int(p[i] == j)) for j in range(4)] for i in range(4)]
    assert mul(Pm, T(Pm)) == [[F(int(i == j)) for j in range(4)] for i in range(4)]


# pivoteo parcial con 3 cifras significativas
def resolver_3_cifras(a11, a12, b1, a21, a22, b2):
    c = Context(prec=3)
    m = c.divide(a21, a11)
    a22n = c.subtract(a22, c.multiply(m, a12))
    b2n = c.subtract(b2, c.multiply(m, b1))
    y = c.divide(b2n, a22n)
    x = c.divide(c.subtract(b1, c.multiply(a12, y)), a11)
    return x, y


# escena: 0.0001 x + y = 1, x + y = 2 (exacta x = 1.0001, y = 0.9999)
assert resolver_3_cifras(D("0.0001"), D(1), D(1), D(1), D(1), D(2)) == (0, 1)       # sin intercambio: x = 0, erróneo
assert resolver_3_cifras(D(1), D(1), D(2), D("0.0001"), D(1), D(1)) == (1, 1)       # con intercambio
x_ex = (F(1) - F(2)) / (F(1, 10000) - 1)
assert abs(x_ex - F(10001, 10000)) < F(1, 10**4) and abs(2 - x_ex - F(9999, 10000)) < F(1, 10**4)
# N4-03: 0.0002 x + y = 1, x + y = 3 -> exacta (2.0004, 0.9996)
x_ex = (F(1) - F(3)) / (F(2, 10000) - 1)
assert abs(x_ex - F(20004, 10000)) < F(1, 10**3) and abs(3 - x_ex - F(9996, 10000)) < F(1, 10**3)
assert resolver_3_cifras(D("0.0002"), D(1), D(1), D(1), D(1), D(3)) == (0, 1)
assert resolver_3_cifras(D(1), D(1), D(3), D("0.0002"), D(1), D(1)) == (D("2.00"), D("0.999"))

# ------------------------------------------------------------ L38
b3 = [F(2), F(5), F(1)]
assert adelante(L, b3) == [2, 1, 6] and atras(U, [F(2), F(1), F(6)]) == [1, F(4, 5), F(3, 5)]
assert mul(A, [[1], [F(4, 5)], [F(3, 5)]]) == [[2], [5], [1]]
c_lu = lambda n, k: (n**3 - n) // 3 + k * n**2
c_gauss = lambda n, k: k * (n**3 + 3 * n**2 - n) // 3
assert (c_lu(100, 50), c_gauss(100, 50)) == (833300, 17165000) and round(c_gauss(100, 50) / c_lu(100, 50)) == 21
assert c_lu(3, 1) == c_gauss(3, 1) == 17
assert all(c_gauss(n, k) - c_lu(n, k) == (k - 1) * (n**3 - n) // 3 for n in range(2, 30) for k in range(1, 20))
# N2-06: A = [[2,1],[6,7]]; b1 = (3,13) -> (1,1); b2 = (1,-3) -> (5/4, -3/2)
A6 = M([2, 1], [6, 7])
L6, U6 = lu(A6)
assert atras(U6, adelante(L6, [F(3), F(13)])) == [1, 1]
assert adelante(L6, [F(1), F(-3)]) == [1, -6] and atras(U6, [F(1), F(-6)]) == [F(5, 4), F(-3, 2)]
assert mul(A6, [[F(5, 4)], [F(-3, 2)]]) == [[1], [-3]]

print("F10: todas las comprobaciones son correctas.")
