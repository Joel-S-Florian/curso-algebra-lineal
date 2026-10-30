"""Álgebra lineal exacta (Fraction) y formato LaTeX para generar la segunda parte de los bancos de ejercicios.

Todo lo que se escribe en una solución sale de estas funciones, no de cuentas a mano.
"""

from dataclasses import dataclass, field
from fractions import Fraction as F
from math import gcd


# ------------------------------------------------------------------ ejercicio
@dataclass
class Ejercicio:
    tipo: str  # "C", "K" o "D"
    nivel: int  # 1..5
    titulo: str
    objetivo: str
    enunciado: str
    solucion: str
    pistas: list = field(default_factory=list)
    errores: str = ""


# ------------------------------------------------------------------ formato
def t(x) -> str:
    """Número (int o Fraction) en LaTeX."""
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    return ("-" if x < 0 else "") + r"\frac{" + str(abs(x.numerator)) + "}{" + str(x.denominator) + "}"


def ts(x) -> str:
    """Número con paréntesis si es negativo o fracción (para multiplicar)."""
    x = F(x)
    return f"({t(x)})" if x < 0 or x.denominator != 1 else t(x)


def termino(c, v, primero: bool) -> str:
    """Un sumando c·v con su signo (omite el signo + si es el primero)."""
    c = F(c)
    if c == 0:
        return ""
    mag = abs(c)
    cuerpo = v if mag == 1 else (t(mag) + v)
    if c < 0:
        return ("-" if primero else " - ") + cuerpo
    return cuerpo if primero else " + " + cuerpo


def lin(coefs, variables) -> str:
    """a1 x1 + a2 x2 + ... en LaTeX; todo cero da «0»."""
    s, primero = "", True
    for c, v in zip(coefs, variables):
        parte = termino(c, v, primero)
        if parte:
            s += parte
            primero = False
    return s or "0"


def sistema(A, b, variables=None) -> str:
    n = len(A[0])
    variables = variables or (["x", "y", "z", "w"][:n] if n <= 4 else [f"x_{{{i + 1}}}" for i in range(n)])
    filas = [f"{lin(f, variables)} = {t(bb)}" for f, bb in zip(A, b)]
    return r"\begin{cases} " + r" \\ ".join(filas) + r" \end{cases}"


def mat(M) -> str:
    return r"\begin{bmatrix} " + r" \\ ".join(" & ".join(t(v) for v in f) for f in M) + r" \end{bmatrix}"


def vec(v) -> str:
    return r"\begin{bmatrix} " + r" \\ ".join(t(x) for x in v) + r" \end{bmatrix}"


def fila_vec(v) -> str:
    return "(" + ", ".join(t(x) for x in v) + ")"


def aug(A, b=None) -> str:
    """[A | b] (si b es None, solo A)."""
    if b is None:
        return mat(A)
    n = len(A[0])
    filas = [" & ".join(t(v) for v in f) + " & " + t(bb) for f, bb in zip(A, b)]
    return r"\left[\begin{array}{" + "c" * n + r"|c} " + r" \\ ".join(filas) + r" \end{array}\right]"


def M(*filas):
    return [[F(v) for v in f] for f in filas]


# ------------------------------------------------------------------ operaciones básicas
def por_vec(A, x):
    return [sum(a * xi for a, xi in zip(f, x)) for f in A]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def trans(A):
    return [list(f) for f in zip(*A)]


def ident(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return sum((-1) ** j * A[0][j] * det([f[:j] + f[j + 1:] for f in A[1:]]) for j in range(n))


def rref(A):
    a = [f[:] for f in A]
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


def rango(A):
    return len(rref(A)[1])


def nucleo(A):
    r, piv = rref(A)
    n = len(A[0])
    base = []
    for libre in (j for j in range(n) if j not in piv):
        v = [F(0)] * n
        v[libre] = F(1)
        for fila, p in enumerate(piv):
            v[p] = -r[fila][libre]
        base.append(v)
    return base


def de_columnas(vs):
    return [[v[i] for v in vs] for i in range(len(vs[0]))]


def columnas(A):
    return [[f[j] for f in A] for j in range(len(A[0]))]


def comb(coefs, vs):
    return [sum(c * v[i] for c, v in zip(coefs, vs)) for i in range(len(vs[0]))]


def en_columna(A, b):
    return rango(A) == rango([f + [bb] for f, bb in zip(A, b)])


def base_columnas(A):
    """Índices de las columnas pivote."""
    return rref(A)[1]


def resolver(A, b):
    """('SCD', x) | ('SCI', xp, base_nucleo) | ('SI',)."""
    n = len(A[0])
    Ab = [f + [bb] for f, bb in zip(A, b)]
    r, piv = rref(Ab)
    if n in piv:
        return ("SI",)
    xp = [F(0)] * n
    for fila, p in enumerate(piv):
        xp[p] = r[fila][n]
    base = nucleo(A)
    return ("SCD", xp) if not base else ("SCI", xp, base)


def solucion_general_tex(xp, base, params=("s", "t", "u")) -> str:
    s = fila_vec(xp)
    for p, v in zip(params, base):
        s += f" + {p}\\,{fila_vec(v)}"
    return s


# ------------------------------------------------------------------ pasos de Gauss / Gauss-Jordan
def _op_tex(tipo, i, j=None, c=None) -> str:
    if tipo == "swap":
        return f"R_{i + 1} \\leftrightarrow R_{j + 1}"
    if tipo == "esc":
        return f"R_{i + 1} \\leftarrow {ts(c)}R_{i + 1}" if c not in (1,) else ""
    signo = "+" if c > 0 else "-"
    mag = abs(c)
    coef = "" if mag == 1 else t(mag)
    return f"R_{i + 1} \\leftarrow R_{i + 1} {signo} {coef}R_{j + 1}"


def pasos_gauss(A, b, jordan=False):
    """Lista de (operación_tex, matriz_aumentada_tras_operar) y la forma final.

    Eliminación hacia adelante (con intercambio si el pivote es 0). Con jordan=True sigue
    hasta la forma reducida (pivotes 1, ceros arriba y abajo).
    """
    a = [f[:] + [bb] for f, bb in zip(A, b)]
    m, n = len(a), len(A[0])
    pasos, fila = [], 0
    pivotes = []
    for col in range(n):
        if fila >= m:
            break
        p = next((i for i in range(fila, m) if a[i][col] != 0), None)
        if p is None:
            continue
        if p != fila:
            a[fila], a[p] = a[p], a[fila]
            pasos.append((_op_tex("swap", fila, p), [f[:] for f in a]))
        if jordan and a[fila][col] != 1:
            c = 1 / a[fila][col]
            a[fila] = [v * c for v in a[fila]]
            pasos.append((_op_tex("esc", fila, c=c), [f[:] for f in a]))
        rango_filas = range(m) if jordan else range(fila + 1, m)
        for i in rango_filas:
            if i == fila or a[i][col] == 0:
                continue
            c = -a[i][col] / a[fila][col]
            a[i] = [x + c * y for x, y in zip(a[i], a[fila])]
            pasos.append((_op_tex("sum", i, fila, c), [f[:] for f in a]))
        pivotes.append((fila, col))
        fila += 1
    return pasos, a, pivotes


def pasos_tex(A, b, jordan=False, maximo=9) -> str:
    """Pasos de Gauss como líneas «operación ⇒ matriz» (si hay más de `maximo`, solo las operaciones)."""
    pasos, final, _ = pasos_gauss(A, b, jordan)
    if len(pasos) > maximo:
        ops = ",\\ ".join(p[0] for p in pasos)
        return f"Operaciones: ${ops}$.\n\nResultado: $${aug([f[:-1] for f in final], [f[-1] for f in final])}$$"
    s = f"$$ {aug(A, b)} $$\n"
    for op, m_ in pasos:
        s += f"$$\\xrightarrow{{{op}}} {aug([f[:-1] for f in m_], [f[-1] for f in m_])}$$\n"
    return s


def sustitucion_atras(A, b):
    """Resuelve un sistema ya escalonado cuadrado con pivotes no nulos; devuelve los pasos en texto."""
    n = len(A)
    x = [F(0)] * n
    lineas = []
    nombres = ["x", "y", "z", "w"][:n]
    for i in range(n - 1, -1, -1):
        resto = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - resto) / A[i][i]
        lineas.append(f"${nombres[i]} = {t(x[i])}$")
    return x, lineas[::-1]


# ------------------------------------------------------------------ LU
def lu(A):
    """A = LU sin intercambios (None si aparece un pivote nulo)."""
    n = len(A)
    U = [f[:] for f in A]
    L = ident(n)
    for k in range(n):
        if U[k][k] == 0:
            return None
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            U[i] = [x - L[i][k] * y for x, y in zip(U[i], U[k])]
    return L, U


def plu(A):
    """PA = LU con pivoteo parcial por magnitud; devuelve P, L, U."""
    n = len(A)
    U = [f[:] for f in A]
    L = [[F(0)] * n for _ in range(n)]
    P = ident(n)
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(U[i][k]))
        if U[p][k] == 0:
            continue
        if p != k:
            U[k], U[p] = U[p], U[k]
            P[k], P[p] = P[p], P[k]
            L[k], L[p] = L[p], L[k]
        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]
            U[i] = [x - L[i][k] * y for x, y in zip(U[i], U[k])]
    for i in range(n):
        L[i][i] = F(1)
    return P, L, U


def sust_adelante(L, b):
    y = []
    for i in range(len(L)):
        y.append(b[i] - sum(L[i][j] * y[j] for j in range(i)))
    return y


def sust_atras(U, y):
    n = len(U)
    x = [F(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x
