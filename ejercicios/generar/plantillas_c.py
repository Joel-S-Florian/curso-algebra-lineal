"""Plantillas de F09–F14 (Gauss-Jordan, LU, rango y Rouché-Frobenius, combinaciones/base, núcleo, espacio columna)."""

from fractions import Fraction as F

import sympy as sp

from algebra import (
    Ejercicio, M, aug, base_columnas, columnas, comb, de_columnas, det, en_columna, fila_vec, lin, lu, mat, mul, nucleo, pasos_gauss,
    pasos_tex, plu, por_vec, rango, resolver, rref, sistema, sust_adelante, sust_atras, t, trans, ts, vec, solucion_general_tex,
)
from plantillas_a import nz, sistema_con_solucion
from plantillas_b import mat_azar


def matriz_rango(r, m, n, rg, lo=-2, hi=3):
    """Matriz m×n de enteros pequeños con rango exacto rg (producto de dos matrices al azar)."""
    for _ in range(500):
        P = [[F(r.randint(lo, hi)) for _ in range(rg)] for _ in range(m)]
        Q = [[F(r.randint(lo, hi)) for _ in range(n)] for _ in range(rg)]
        A = mul(P, Q)
        filas_distintas = len({tuple(f) for f in A}) == len(A)
        columnas_no_nulas = all(any(f[j] != 0 for f in A) for j in range(n))
        if rango(A) == rg and all(abs(v) <= 9 for f in A for v in f) and all(any(v != 0 for v in f) for f in A) and (filas_distintas or rg == 1) and columnas_no_nulas:
            return A
    raise RuntimeError("no hay matriz de ese rango")


def sistema_tipo(r, m, n, tipo, rg=None):
    """Sistema m×n del tipo pedido ('SCD', 'SCI' o 'SI'); devuelve A, b."""
    if tipo == "SCD":
        rg = n
    elif tipo == "SCI":
        rg = rg or r.randint(1, n - 1)
    else:
        rg = rg or r.randint(1, min(m, n) - 1 if min(m, n) > 1 else 1)
        rg = min(rg, m - 1)
    A = matriz_rango(r, m, n, rg)
    x0 = [F(r.randint(-3, 3)) for _ in range(n)]
    b = por_vec(A, x0)
    if tipo == "SI":
        y = nucleo(trans(A))[0]
        i = next(k for k, v in enumerate(y) if v != 0)
        b = b[:]
        b[i] += 1
    return A, b


def fuera_de_columna(A, b):
    """b con una componente cambiada de forma que ya no está en el espacio columna de A (usa un vector del núcleo izquierdo)."""
    y = nucleo(trans(A))[0]
    i = next(k for k, v in enumerate(y) if v != 0)
    b = b[:]
    b[i] += 1
    return b


def clasifica_rf(A, b):
    n = len(A[0])
    ra, rab = rango(A), rango([f + [bb] for f, bb in zip(A, b)])
    if ra != rab:
        return ra, rab, "SI"
    return ra, rab, ("SCD" if ra == n else "SCI")


NOMBRE = {"SCD": "compatible determinado (solución única)", "SCI": "compatible indeterminado (infinitas soluciones)", "SI": "incompatible (sin solución)"}


# ----------------------------------------------------------------------------- F09
def f09_reducida(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    return Ejercicio(
        "C", 2, "Gauss-Jordan hasta la reducida", "llevar $[A \\mid \\mathbf{b}]$ a su forma escalonada reducida y leer la solución.",
        f"Resuelve por Gauss-Jordan ${sistema(A, b)}$.",
        pasos_tex(A, b, True, maximo=12) + f"\nLa reducida tiene la identidad a la izquierda: la solución se lee en la última columna, $({', '.join(t(v) for v in x0)})$.",
        ["Convierte cada pivote en $1$ y haz ceros también por encima."], "Dejar sin anular las entradas por encima de un pivote.",
    )


def f09_indeterminado(r):
    A, b = sistema_tipo(r, 3, 4, "SCI", rg=r.choice([2, 2, 3]) if False else 2)
    res = resolver(A, b)
    rr, piv = rref([f + [bb] for f, bb in zip(A, b)])
    libres = [j + 1 for j in range(4) if j not in piv]
    return Ejercicio(
        "C", 3, "Leer la solución en la reducida", "identificar variables básicas y libres y escribir la solución general.",
        f"Halla, por Gauss-Jordan, la reducida de ${aug(A, b)}$ y escribe la solución general.",
        pasos_tex(A, b, True, maximo=0) + f"\nVariables libres: {', '.join('$x_' + str(j) + '$' for j in libres)}. Solución general: ${solucion_general_tex(res[1], res[2])}$ (parámetros reales).\n\nComprobación con los parámetros en cero: $A\\mathbf{{x}}_p = {fila_vec(por_vec(A, res[1]))} = {fila_vec(b)}$.",
        ["Las columnas sin pivote son las variables libres."], "Olvidar que las variables libres también forman parte del vector solución.",
    )


def f09_incompatible(r):
    A, b = sistema_tipo(r, 3, 3, "SI", rg=2)
    return Ejercicio(
        "C", 3, "Una reducida con pivote en la última columna", "reconocer el pivote en la columna de $\\mathbf{b}$.",
        f"Reduce ${aug(A, b)}$ y clasifica el sistema.",
        pasos_tex(A, b, True, maximo=0) + "\nHay un pivote en la columna de términos independientes (fila $[\\,0\\,0\\,0 \\mid 1\\,]$): la ecuación $0 = 1$ es imposible. Incompatible.",
        ["Mira si queda una fila $[0\\ \\dots\\ 0 \\mid c]$ con $c \\ne 0$."], "Declarar compatible un sistema con una fila contradictoria.",
    )


POOL_REDUCIDA = [
    (M([1, 0, 2], [0, 1, 3]), True, ""),
    (M([1, 2, 0], [0, 0, 1]), True, ""),
    (M([2, 0, 1], [0, 1, 0]), False, "el primer pivote vale $2$, no $1$"),
    (M([1, 1, 0], [0, 1, 0]), False, "hay un elemento no nulo por encima del segundo pivote"),
    (M([0, 1, 0], [1, 0, 0]), False, "el pivote de la fila 2 está a la izquierda del de la fila 1"),
    (M([1, 0, 0], [0, 0, 0], [0, 0, 1]), False, "una fila de ceros está encima de una fila no nula"),
    (M([1, 0, 3, 0], [0, 1, 2, 0], [0, 0, 0, 1]), True, ""),
]


def f09_es_reducida(r):
    e = r.sample(POOL_REDUCIDA, 4)
    return Ejercicio(
        "K", 2, "¿Está en forma reducida?", "recordar las condiciones de la forma escalonada reducida.",
        "Indica cuáles de estas matrices están en forma escalonada reducida y, si no lo están, por qué:\n\n" + "\n\n".join(f"{chr(97 + i)}) ${mat(m_[0])}$" for i, m_ in enumerate(e)),
        "\n\n".join(f"{chr(97 + i)}) " + ("Sí lo está." if m_[1] else f"No: {m_[2]}.") for i, m_ in enumerate(e)),
        ["Condiciones: pivotes $1$, escalonada, ceros por encima y por debajo de cada pivote, filas nulas abajo."], "Olvidar los ceros por encima de los pivotes.",
    )


def f09_cuentas(r):
    n = r.choice([3, 4, 5, 6, 8, 10])
    gauss = F(n ** 3 + 3 * n ** 2 - n, 3)
    jordan = F(n ** 3 + n ** 2, 2)
    return Ejercicio(
        "C", 3, "Gauss frente a Gauss-Jordan", "comparar el número de operaciones con las fórmulas.",
        f"Para un sistema cuadrado $n = {n}$, calcula con $\\frac{{n^3 + 3n^2 - n}}{{3}}$ (Gauss con sustitución hacia atrás) y $\\frac{{n^3 + n^2}}{{2}}$ (Gauss-Jordan) el número de multiplicaciones y divisiones, y la razón entre ambos.",
        f"Gauss: $\\frac{{{n ** 3} + {3 * n ** 2} - {n}}}{{3}} = {t(gauss)}$. Gauss-Jordan: $\\frac{{{n ** 3} + {n ** 2}}}{{2}} = {t(jordan)}$. La razón es ${t(jordan / gauss)}\\approx {float(jordan / gauss):.2f}$: Gauss-Jordan cuesta {'más' if jordan > gauss else 'menos'} (y la razón tiende a $3/2$ cuando $n$ crece).",
        ["Sustituye $n$ en cada fórmula."], "Contar solo las operaciones hacia adelante.",
    )


def f09_rango_deficiente(r):
    A = matriz_rango(r, 4, 4, r.choice([2, 3]))
    b = por_vec(A, [F(r.randint(-2, 3)) for _ in range(4)])
    res = resolver(A, b)
    return Ejercicio(
        "C", 3, "Reducir una matriz 4×4 con filas dependientes", "reducir y contar variables libres.",
        f"Lleva ${aug(A, b)}$ a su forma reducida y di cuántas variables libres hay.",
        pasos_tex(A, b, True, maximo=0) + f"\nVariables libres: {4 - rango(A)}. Solución general: ${solucion_general_tex(res[1], res[2])}$.",
        ["Algunas filas desaparecerán (se vuelven nulas)."], "Contar las filas nulas como variables libres.",
    )


def f09_basicas(r):
    A, b = sistema_tipo(r, 3, 5, "SCI", rg=3)
    Rr, piv = rref([f + [bb] for f, bb in zip(A, b)])
    return Ejercicio(
        "K", 2, "Básicas y libres", "identificar variables básicas y libres a partir de la reducida.",
        f"La forma reducida de un sistema es ${aug([f[:-1] for f in Rr], [f[-1] for f in Rr])}$. ¿Cuáles son las variables básicas y cuáles las libres? ¿Cuántos parámetros tiene la solución?",
        f"Básicas (columnas con pivote): {', '.join('$x_' + str(j + 1) + '$' for j in piv)}. Libres: {', '.join('$x_' + str(j + 1) + '$' for j in range(5) if j not in piv)}. Parámetros: {5 - len(piv)}.",
        ["Una variable es básica si su columna tiene pivote."], "Contar la columna de $\\mathbf{b}$ entre las variables.",
    )


# ----------------------------------------------------------------------------- F10
def lu_azar(r, n=3):
    while True:
        L = [[F(1) if i == j else (F(r.randint(-3, 3)) if i > j else F(0)) for j in range(n)] for i in range(n)]
        U = [[F(r.choice([1, 2, 3, -1, -2])) if i == j else (F(r.randint(-3, 3)) if j > i else F(0)) for j in range(n)] for i in range(n)]
        A = mul(L, U)
        if lu(A) is not None and all(abs(v) <= 12 for f in A for v in f):
            return A, L, U


def f10_factorizar(r):
    A, L, U = lu_azar(r)
    L2, U2 = lu(A)
    assert L2 == L and U2 == U
    mult = [(i + 1, j + 1, L[i][j]) for j in range(3) for i in range(j + 1, 3)]
    return Ejercicio(
        "C", 3, "Factorización $A = LU$", "obtener $L$ y $U$ guardando los multiplicadores.",
        f"Factoriza $A = LU$ (sin intercambios): $A = {mat(A)}$.",
        "Multiplicadores: " + ", ".join(f"$\\ell_{{{i}{j}}} = {t(v)}$" for i, j, v in mult) + f".\n\n$L = {mat(L)}$, $U = {mat(U)}$.\n\nComprobación: $LU = {mat(mul(L, U))} = A$.",
        ["El multiplicador $\\ell_{ik}$ es (entrada a eliminar) / (pivote).", "$U$ es la matriz escalonada que resulta de eliminar."], "Guardar el multiplicador con el signo contrario en $L$.",
    )


def f10_resolver(r):
    A, L, U = lu_azar(r)
    x0 = [F(r.randint(-3, 3)) for _ in range(3)]
    b = por_vec(A, x0)
    y = sust_adelante(L, b)
    x = sust_atras(U, y)
    assert x == x0
    return Ejercicio(
        "C", 3, "Resolver con $LU$", "resolver $A\\mathbf{x} = \\mathbf{b}$ con dos sustituciones.",
        f"Dado $A = LU$ con $L = {mat(L)}$ y $U = {mat(U)}$, resuelve $A\\mathbf{{x}} = {vec(b)}$.",
        f"Primero $L\\mathbf{{y}} = \\mathbf{{b}}$ (hacia adelante): $\\mathbf{{y}} = {fila_vec(y)}$. Después $U\\mathbf{{x}} = \\mathbf{{y}}$ (hacia atrás): $\\mathbf{{x}} = {fila_vec(x)}$.\n\nComprobación: $A\\mathbf{{x}} = {fila_vec(por_vec(A, x))}$.",
        ["Llama $\\mathbf{y} = U\\mathbf{x}$.", "Resuelve primero con $L$, empezando por la primera fila."], "Resolver con $U$ antes que con $L$.",
    )


def f10_plu(r):
    while True:
        A = mat_azar(r, 3, 3, -4, 4)
        if det(A) != 0 and lu(A) is None:
            break
    P, L, U = plu(A)
    assert mul(P, A) == mul(L, U)
    return Ejercicio(
        "C", 4, "$PA = LU$ con pivoteo", "factorizar con una matriz de permutación cuando aparece un pivote nulo.",
        f"Esta matriz no admite $A = LU$ sin intercambios. Halla $P$, $L$, $U$ con $PA = LU$ (pivoteo parcial): $A = {mat(A)}$.",
        f"Eligiendo en cada columna el pivote de mayor valor absoluto: $P = {mat(P)}$, $L = {mat(L)}$, $U = {mat(U)}$.\n\nComprobación: $PA = {mat(mul(P, A))}$ y $LU = {mat(mul(L, U))}$ coinciden.",
        ["Si el pivote es cero, intercambia con una fila inferior; los multiplicadores viajan con su fila."], "Olvidar intercambiar también los multiplicadores ya guardados en $L$.",
    )


def f10_falla(r):
    a, b, c = nz(r, 1, 4), nz(r, 1, 4), nz(r, 1, 4)
    A = M([0, a, b], [c, 1, 2], [1, 2, 3])
    return Ejercicio(
        "K", 3, "¿Existe $A = LU$?", "reconocer cuándo falla la factorización sin intercambios.",
        f"¿Admite la matriz $A = {mat(A)}$ una factorización $A = LU$ sin permutaciones? ¿Y $PA = LU$?",
        "No admite $A = LU$: el primer pivote es $0$ y, sin intercambiar filas, no se puede eliminar la primera columna. Sí admite $PA = LU$ (si $A$ es invertible siempre se puede con una permutación adecuada): "
        f"su determinante es ${t(det(A))}" + ("\\ne 0$." if det(A) != 0 else "= 0$.") + "",
        ["Mira la entrada $(1,1)$."], "Pensar que una matriz invertible siempre tiene $LU$ directa.",
    )


POOL_K10 = [
    ("¿Cuántas operaciones cuesta factorizar $A = LU$ para $n = 10$, con la fórmula $\\frac{n^3 - n}{3}$?", "$\\frac{1000 - 10}{3} = 330$ multiplicaciones y divisiones."),
    ("Para resolver con 5 lados derechos distintos, ¿conviene factorizar una vez o hacer Gauss cinco veces?", "Factorizar una vez: el coste $\\frac{n^3 - n}{3}$ se paga una sola vez y cada lado derecho solo cuesta $n^2$."),
    ("¿Qué forma tiene la diagonal de $L$ en $A = LU$?", "Son unos: $L$ es triangular inferior con unos en la diagonal."),
]


def f10_conceptual(r):
    return Ejercicio(
        "K", 3, "Preguntas sobre $LU$", "recordar el coste y la forma de las matrices de la factorización.",
        "\n\n".join(f"{chr(97 + i)}) {q}" for i, (q, _) in enumerate(POOL_K10)),
        "\n\n".join(f"{chr(97 + i)}) {a}" for i, (_, a) in enumerate(POOL_K10)),
        ["Recuerda las fórmulas de coste de la lección 33 y la lección 38."], "Confundir el coste de la factorización con el de resolver con $L$ y $U$.",
    )


# ----------------------------------------------------------------------------- F11
def f11_rango(r):
    m, n = r.choice([(3, 3), (3, 4), (4, 3), (4, 4)])
    rg = r.randint(1, min(m, n) - 1) if r.random() < 0.7 else min(m, n)
    A = matriz_rango(r, m, n, rg)
    red, piv = rref(A)
    ops = ", ".join(op for op, _ in pasos_gauss(A, [F(0)] * m)[0])
    return Ejercicio(
        "C", 2, "Calcular el rango", "escalonar y contar pivotes.",
        f"Calcula el rango de $A = {mat(A)}$.",
        (f"Operaciones por filas: ${ops}$.\n\n" if ops else "") + f"La forma reducida es ${mat(red)}$, con pivotes en las columnas {', '.join(str(p + 1) for p in piv)}: $\\operatorname{{rg}}(A) = {len(piv)}$.",
        ["Cuenta los pivotes de una forma escalonada."], "Contar las filas no nulas de la matriz original en lugar de la escalonada.",
    )


def f11_clasificar(r):
    m, n = r.choice([(3, 3), (3, 4), (4, 3), (3, 3)])
    tipo = r.choice(["SCD", "SCI", "SI"])
    if tipo == "SCD" and m == 3 and n == 4:
        tipo = "SCI"
    A, b = sistema_tipo(r, m, n, tipo)
    ra, rab, cl = clasifica_rf(A, b)
    assert cl == tipo
    extra = f" Número de parámetros libres: $n - r = {n} - {ra} = {n - ra}$." if cl == "SCI" else ""
    return Ejercicio(
        "C", 3, "Clasificar con Rouché-Frobenius", "clasificar sin resolver comparando rangos.",
        f"Sin resolverlo, clasifica ${sistema(A, b)}$.",
        f"$\\operatorname{{rg}}(A) = {ra}$, $\\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = {rab}$, $n = {n}$ incógnitas. " + (
            "Los rangos son distintos: " if cl == "SI" else f"Los rangos coinciden" + (f" y valen $n$: " if cl == "SCD" else f" pero son menores que $n$: ")
        ) + NOMBRE[cl] + "." + extra,
        ["Calcula los dos rangos escalonando $[A \\mid \\mathbf{b}]$."], "Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.",
    )


def f11_parametro(r):
    a = sp.symbols("a")
    forma = r.choice([0, 1, 2])
    if forma == 0:
        Aa, bs = sp.Matrix([[1, 1, 1], [1, a, 1], [1, 1, a]]), [1, r.choice([1, 2]), 1]
        txt = f"\\begin{{cases}} x + y + z = 1 \\\\ x + ay + z = {bs[1]} \\\\ x + y + az = 1 \\end{{cases}}"
    elif forma == 1:
        Aa, bs = sp.Matrix([[1, 1, 1], [1, 2, a], [1, 4, a * a]]), [1, r.choice([0, 1, 2]), r.choice([0, 1, 4])]
        txt = f"\\begin{{cases}} x + y + z = 1 \\\\ x + 2y + az = {bs[1]} \\\\ x + 4y + a^2 z = {bs[2]} \\end{{cases}}"
    else:
        Aa, bs = sp.Matrix([[1, 1, a], [1, a, 1], [a, 1, 1]]), [1, 1, r.choice([1, 0])]
        txt = f"\\begin{{cases}} x + y + az = 1 \\\\ x + ay + z = 1 \\\\ ax + y + z = {bs[2]} \\end{{cases}}"
    raices = [rr for rr in sp.solve(Aa.det(), a) if rr.is_rational]
    lineas = []
    for rr in raices:
        Av = [[F(int(sp.Rational(v.subs(a, rr)).p), int(sp.Rational(v.subs(a, rr)).q)) for v in Aa.row(i)] for i in range(3)]
        ra, rab, cl = clasifica_rf(Av, [F(v) for v in bs])
        lineas.append(f"$a = {sp.latex(rr)}$: $\\operatorname{{rg}}(A) = {ra}$, $\\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = {rab}$, {NOMBRE[cl]}.")
    return Ejercicio(
        "C", 4, "Discusión con Rouché-Frobenius", "discutir según un parámetro usando rangos.",
        f"Discute según $a$, con Rouché-Frobenius: ${txt}$",
        f"$\\det A = {sp.latex(sp.factor(Aa.det()))}$, que se anula en $a \\in \\{{{', '.join(sp.latex(rr) for rr in raices)}\\}}$. Si $a$ es distinto de esos valores, $\\operatorname{{rg}}(A) = \\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = 3 = n$: solución única.\n\n" + "\n\n".join(lineas),
        ["El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.", "Para cada valor crítico, calcula $\\operatorname{rg}(A)$ y $\\operatorname{rg}[A \\mid \\mathbf{b}]$."], "Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\\mathbf{b}$.",
    )


POOL_K11 = [
    ("$\\operatorname{rg}(A) = 3$, $\\operatorname{rg}[A \\mid \\mathbf{b}] = 3$ y hay 4 incógnitas.", "Compatible indeterminado con $4 - 3 = 1$ parámetro libre."),
    ("$\\operatorname{rg}(A) = 2$ y $\\operatorname{rg}[A \\mid \\mathbf{b}] = 3$.", "Incompatible: el rango de la aumentada es mayor."),
    ("$\\operatorname{rg}(A) = \\operatorname{rg}[A \\mid \\mathbf{b}] = n$.", "Compatible determinado (solución única)."),
    ("Un sistema homogéneo con 3 ecuaciones y 5 incógnitas.", "Siempre compatible; como $\\operatorname{rg} \\le 3 < 5$, es indeterminado, con al menos $2$ parámetros libres."),
    ("¿Puede ser $\\operatorname{rg}[A \\mid \\mathbf{b}] < \\operatorname{rg}(A)$?", "No: la aumentada tiene una columna más, y $\\operatorname{rg}(A) \\le \\operatorname{rg}[A \\mid \\mathbf{b}] \\le \\operatorname{rg}(A) + 1$."),
    ("Un sistema con más ecuaciones que incógnitas, ¿puede ser compatible determinado?", "Sí, si las ecuaciones sobrantes son combinación de las demás (rango $= n$)."),
]


def f11_conceptual(r):
    e = r.sample(POOL_K11, 3)
    return Ejercicio(
        "K", 3, "Clasificar con datos de rango", "clasificar a partir de los rangos, sin calcular.",
        "Clasifica y justifica, para cada caso:\n\n" + "\n".join(f"{chr(97 + i)}) {q}" for i, (q, _) in enumerate(e)),
        "\n\n".join(f"{chr(97 + i)}) {a}" for i, (_, a) in enumerate(e)),
        ["Compara $\\operatorname{rg}(A)$, $\\operatorname{rg}[A \\mid \\mathbf{b}]$ y $n$."], "No contar la columna de $\\mathbf{b}$.",
    )


def f11_libres(r):
    m, n = r.choice([(3, 5), (4, 6), (2, 4), (5, 3)])
    rg = r.randint(1, min(m, n) - 1)
    return Ejercicio(
        "K", 2, "Contar parámetros libres", "usar $n - \\operatorname{rg}(A)$ en un sistema compatible.",
        f"Un sistema compatible tiene {m} ecuaciones, {n} incógnitas y $\\operatorname{{rg}}(A) = {rg}$. ¿Cuántos parámetros libres tiene la solución y de qué tipo es?",
        f"$n - \\operatorname{{rg}}(A) = {n} - {rg} = {n - rg}$ parámetros libres: compatible indeterminado.",
        ["Parámetros libres = incógnitas − rango."], "Restar el rango del número de ecuaciones.",
    )


# ----------------------------------------------------------------------------- F12
def vec_azar(r, n, lo=-3, hi=3):
    return [F(r.randint(lo, hi)) for _ in range(n)]


def f12_pertenencia(r):
    n = 3
    u, v = vec_azar(r, n), vec_azar(r, n)
    while rango(de_columnas([u, v])) < 2:
        u, v = vec_azar(r, n), vec_azar(r, n)
    si = r.random() < 0.55
    c1, c2 = nz(r, -3, 3), nz(r, -3, 3)
    b = comb([c1, c2], [u, v])
    if not si:
        b = fuera_de_columna(de_columnas([u, v]), b)
    A = de_columnas([u, v])
    sol = (f"Hay que resolver $c_1\\mathbf{{u}} + c_2\\mathbf{{v}} = \\mathbf{{b}}$. " +
           (f"Sale $c_1 = {t(c1)}$, $c_2 = {t(c2)}$: sí, $\\mathbf{{b}} = {ts(c1)}\\mathbf{{u}} + {ts(c2)}\\mathbf{{v}}$." if si else
            f"Los rangos son $\\operatorname{{rg}}[\\mathbf{{u}}\\ \\mathbf{{v}}] = 2$ y $\\operatorname{{rg}}[\\mathbf{{u}}\\ \\mathbf{{v}}\\mid\\mathbf{{b}}] = 3$: el sistema es incompatible, $\\mathbf{{b}}$ no es combinación lineal."))
    return Ejercicio(
        "C", 2, "¿Es combinación lineal?", "decidir pertenencia al espacio generado con un sistema.",
        f"¿Es $\\mathbf{{b}} = {vec(b)}$ combinación lineal de $\\mathbf{{u}} = {vec(u)}$ y $\\mathbf{{v}} = {vec(v)}$?",
        sol, ["Plantea $c_1\\mathbf{u} + c_2\\mathbf{v} = \\mathbf{b}$ componente a componente."], "Resolver solo con dos componentes y no comprobar la tercera.",
    )


def f12_independencia(r):
    k = r.choice([3, 3, 3, 4])
    n = r.choice([3, 4]) if k == 3 else 3
    dep = r.random() < 0.5
    if dep:
        vs = [vec_azar(r, n) for _ in range(k - 1)]
        c = [nz(r, -2, 2) for _ in range(k - 1)]
        vs.append(comb(c, vs))
        r.shuffle(vs)
    else:
        vs = [vec_azar(r, n) for _ in range(k)]
    V = de_columnas(vs)
    rg = rango(V)
    ns = nucleo(V)
    lista = ", ".join(f"$\\mathbf{{v}}_{i + 1} = {fila_vec(v)}$" for i, v in enumerate(vs))
    sol = f"Con los vectores por columnas, $\\operatorname{{rg}}(V) = {rg}$ y hay $k = {k}$ vectores. "
    if rg == k:
        sol += "El rango es igual al número de vectores: son **independientes**."
    else:
        rel = ns[0]
        sol += f"El rango es menor que {k}: son **dependientes**. Una relación: $" + " + ".join(f"{ts(c)}\\mathbf{{v}}_{i + 1}" for i, c in enumerate(rel) if c != 0) + " = \\mathbf{0}$."
    return Ejercicio(
        "C", 3, "Independencia lineal", "decidir con el rango y, si es dependiente, dar una relación.",
        f"¿Son linealmente independientes {lista}? Si no, da una relación entre ellos.",
        sol, ["Forma la matriz con los vectores por columnas y escalónala."], "Creer que basta que ningún par sea proporcional.",
    )


def f12_base(r):
    m, n = r.choice([(3, 4), (3, 5), (4, 4)])
    rg = r.randint(2, min(m, n) - 1)
    A = matriz_rango(r, m, n, rg)
    piv = base_columnas(A)
    cols = columnas(A)
    return Ejercicio(
        "C", 3, "Base del espacio generado", "extraer una base con las columnas pivote de la matriz original.",
        f"Halla una base y la dimensión del espacio generado por las columnas de $A = {mat(A)}$.",
        f"La reducida tiene pivotes en las columnas {', '.join(str(p + 1) for p in piv)}. Una base son las columnas de $A$ (la original): " + ", ".join(f"${fila_vec(cols[p])}$" for p in piv) + f". Dimensión: {len(piv)}.",
        ["Reduce $A$ y mira dónde están los pivotes."], "Tomar las columnas de la matriz reducida.",
    )


def f12_geometria(r):
    n = r.choice([2, 3])
    k = r.choice([1, 2, 2, 3]) if n == 3 else r.choice([1, 2])
    vs = [vec_azar(r, n, -2, 2) for _ in range(k)]
    if r.random() < 0.4 and k >= 2:
        vs[-1] = [2 * x for x in vs[0]]
    rg = rango(de_columnas(vs))
    obj = {0: "solo el origen", 1: "una recta por el origen", 2: ("todo el plano $\\mathbb{R}^2$" if n == 2 else "un plano por el origen"), 3: "todo $\\mathbb{R}^3$"}[rg]
    return Ejercicio(
        "K", 2, "¿Qué es el espacio generado?", "relacionar el rango con la figura geométrica generada.",
        f"Describe geométricamente el espacio generado por {', '.join('$' + fila_vec(v) + '$' for v in vs)} en $\\mathbb{{R}}^{n}$.",
        f"La matriz con esos vectores por columnas tiene rango {rg}: el espacio generado es {obj} (dimensión {rg}).",
        ["Su dimensión es el rango de la matriz con los vectores por columnas."], "Contar los vectores en vez de los independientes.",
    )


POOL_K12 = [
    ("¿Pueden cuatro vectores de $\\mathbb{R}^3$ ser linealmente independientes?", "No: el rango de una matriz $3 \\times 4$ es a lo sumo $3 < 4$."),
    ("¿Puede un conjunto linealmente independiente contener al vector nulo?", "No: $1\\cdot\\mathbf{0} = \\mathbf{0}$ es una combinación no trivial."),
    ("¿Cuántos vectores tiene cualquier base de $\\mathbb{R}^3$?", "Tres: todas las bases tienen el mismo número de vectores, la dimensión $3$."),
    ("¿Genera $\\mathbb{R}^3$ un conjunto de dos vectores?", "No: el rango de una matriz $3 \\times 2$ es a lo sumo $2 < 3$."),
]


def f12_conceptual(r):
    e = r.sample(POOL_K12, 2)
    return Ejercicio(
        "K", 3, "Preguntas de base y dimensión", "razonar con rangos sobre independencia y generadores.",
        "\n\n".join(f"{chr(97 + i)}) {q}" for i, (q, _) in enumerate(e)),
        "\n\n".join(f"{chr(97 + i)}) {a}" for i, (_, a) in enumerate(e)),
        ["Piensa en el rango de la matriz que forman los vectores."], "Confundir independencia con generar.",
    )


# ----------------------------------------------------------------------------- F13
def f13_base_nucleo(r):
    m, n = r.choice([(3, 4), (2, 4), (3, 5), (2, 3), (3, 4)])
    rg = r.randint(1, min(m, n) - 1) if min(m, n) > 1 else 1
    A = matriz_rango(r, m, n, rg)
    base = nucleo(A)
    red, piv = rref(A)
    assert all(por_vec(A, v) == [0] * m for v in base)
    return Ejercicio(
        "C", 3, "Base del núcleo", "resolver $A\\mathbf{x} = \\mathbf{0}$ y dar una base con las variables libres.",
        f"Halla una base de $\\ker A$ y su dimensión para $A = {mat(A)}$.",
        f"La reducida es ${mat(red)}$, con pivotes en las columnas {', '.join(str(p + 1) for p in piv)}. Variables libres: {', '.join('$x_' + str(j + 1) + '$' for j in range(n) if j not in piv)}. "
        "Base: " + ", ".join(f"${fila_vec(v)}$" for v in base) + f". $\\operatorname{{nul}}(A) = {len(base)} = {n} - {rg}$.",
        ["Reduce $A$ y despeja las variables básicas en función de las libres."], "Olvidar un vector de la base por cada variable libre.",
    )


def f13_pertenece(r):
    m, n = 3, 4
    A = matriz_rango(r, m, n, 2)
    base = nucleo(A)
    s, u = nz(r, -2, 2), nz(r, -2, 2)
    dentro = comb([s, u], base)
    fuera = dentro[:]
    j = next(k for k in range(n) if any(A[i][k] != 0 for i in range(m)))
    fuera[j] += 1
    cand = [dentro, fuera]
    r.shuffle(cand)
    return Ejercicio(
        "C", 2, "¿Está en el núcleo?", "comprobar pertenencia multiplicando.",
        f"Con $A = {mat(A)}$, ¿cuáles de $\\mathbf{{x}}_1 = {fila_vec(cand[0])}$ y $\\mathbf{{x}}_2 = {fila_vec(cand[1])}$ están en $\\ker A$?",
        "\n\n".join(f"$A\\mathbf{{x}}_{i + 1} = {fila_vec(por_vec(A, c))}$: " + ("sí está en el núcleo." if all(v == 0 for v in por_vec(A, c)) else "no está en el núcleo.") for i, c in enumerate(cand)),
        ["Calcula $A\\mathbf{x}$ y mira si es el vector nulo."], "Comprobar solo una fila.",
    )


def f13_solucion_general(r):
    A, b = sistema_tipo(r, 3, 4, "SCI", rg=2)
    res = resolver(A, b)
    return Ejercicio(
        "C", 3, "Solución general: particular más núcleo", "escribir $\\mathbf{x} = \\mathbf{x}_p + \\ker A$.",
        f"Resuelve ${sistema(A, b)}$ y escribe la solución como $\\mathbf{{x}}_p + $ combinación de una base de $\\ker A$.",
        f"Solución particular (libres $= 0$): $\\mathbf{{x}}_p = {fila_vec(res[1])}$. Base del núcleo: " + ", ".join(f"${fila_vec(v)}$" for v in res[2]) + f". Solución general: ${solucion_general_tex(res[1], res[2])}$.\n\n"
        f"Comprobación: $A\\mathbf{{x}}_p = {fila_vec(por_vec(A, res[1]))}$ y cada vector de la base cumple $A\\mathbf{{n}} = \\mathbf{{0}}$.",
        ["Escalona $[A \\mid \\mathbf{b}]$ y pon las libres a cero para $\\mathbf{x}_p$."], "Olvidar sumar $\\mathbf{x}_p$ y dar solo el núcleo.",
    )


def f13_nulidad(r):
    m, n = r.choice([(3, 5), (4, 4), (5, 3), (2, 6), (4, 7)])
    rg = r.randint(1, min(m, n))
    return Ejercicio(
        "K", 2, "Nulidad con el rango", "usar $\\operatorname{nul} = n - \\operatorname{rg}$.",
        f"Una matriz $A$ de tamaño ${m}\\times {n}$ tiene rango {rg}. ¿Cuál es la dimensión de $\\ker A$? ¿Es $\\ker A = \\{{\\mathbf{{0}}\\}}$?",
        f"$\\operatorname{{nul}}(A) = n - \\operatorname{{rg}}(A) = {n} - {rg} = {n - rg}$. " + ("Como la nulidad es $0$, $\\ker A = \\{\\mathbf{0}\\}$." if n == rg else "Como la nulidad es positiva, $\\ker A \\ne \\{\\mathbf{0}\\}$."),
        ["Las columnas de $A$ son $n$."], "Restar el rango de $m$ (filas) en vez de $n$.",
    )


POOL_K13 = [
    ("¿Puede el núcleo de una matriz $3 \\times 5$ ser $\\{\\mathbf{0}\\}$?", "No: $\\operatorname{nul} = 5 - \\operatorname{rg} \\ge 5 - 3 = 2$."),
    ("Si $A\\mathbf{x} = \\mathbf{b}$ tiene dos soluciones distintas, ¿qué sabes de $\\ker A$?", "Su diferencia está en el núcleo y es no nula: $\\ker A \\ne \\{\\mathbf{0}\\}$ (y hay infinitas soluciones)."),
    ("¿Es el conjunto de soluciones de $A\\mathbf{x} = \\mathbf{b}$, con $\\mathbf{b} \\ne \\mathbf{0}$, un subespacio?", "No: no contiene a $\\mathbf{0}$ (es el núcleo trasladado, un «subespacio afín»)."),
]


def f13_conceptual(r):
    return Ejercicio(
        "K", 3, "Preguntas sobre el núcleo", "razonar sobre el núcleo sin calcular.",
        "\n\n".join(f"{chr(97 + i)}) {q}" for i, (q, _) in enumerate(POOL_K13)),
        "\n\n".join(f"{chr(97 + i)}) {a}" for i, (_, a) in enumerate(POOL_K13)),
        ["Usa $\\operatorname{nul} = n - \\operatorname{rg}$ y la estructura $\\mathbf{x}_p + \\ker A$."], "Pensar que el conjunto solución siempre contiene a $\\mathbf{0}$.",
    )


# ----------------------------------------------------------------------------- F14
def f14_base_col(r):
    m, n = r.choice([(3, 4), (4, 4), (3, 5), (4, 5)])
    rg = r.randint(2, min(m, n) - 1)
    A = matriz_rango(r, m, n, rg)
    piv = base_columnas(A)
    cols = columnas(A)
    red = rref(A)[0]
    otros = [j for j in range(n) if j not in piv]
    rel = []
    for j in otros:
        coefs = [red[i][j] for i in range(len(piv))]
        rel.append(f"$\\mathbf{{a}}_{j + 1} = " + " + ".join(f"{ts(c)}\\mathbf{{a}}_{piv[i] + 1}" for i, c in enumerate(coefs) if c != 0) + "$" if any(coefs) else f"$\\mathbf{{a}}_{j + 1} = \\mathbf{{0}}$")
    return Ejercicio(
        "C", 3, "Base del espacio columna", "tomar las columnas pivote de la matriz original.",
        f"Halla una base de $\\operatorname{{Col}}(A)$ y escribe las demás columnas con ella: $A = {mat(A)}$.",
        f"Pivotes en las columnas {', '.join(str(p + 1) for p in piv)}. Base: " + ", ".join(f"${fila_vec(cols[p])}$" for p in piv) + f"; $\\dim\\operatorname{{Col}}(A) = \\operatorname{{rg}}(A) = {rg}$. Relaciones (leídas en la reducida): " + "; ".join(rel) + ".",
        ["Las columnas con pivote de la reducida indican qué columnas de $A$ tomar."], "Usar las columnas de la reducida.",
    )


def f14_existe(r):
    m, n = 3, 4
    A = matriz_rango(r, m, n, 2)
    x0 = [F(r.randint(-2, 3)) for _ in range(n)]
    b_ok = por_vec(A, x0)
    b_no = fuera_de_columna(A, b_ok)
    b = r.choice([b_ok, b_no])
    ra, rab, cl = clasifica_rf(A, b)
    return Ejercicio(
        "C", 2, "¿Está $\\mathbf{b}$ en $\\operatorname{Col}(A)$?", "decidir la existencia de solución con rangos.",
        f"Con $A = {mat(A)}$, ¿tiene solución $A\\mathbf{{x}} = {vec(b)}$?",
        f"$\\operatorname{{rg}}(A) = {ra}$ y $\\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = {rab}$. " + ("Coinciden: $\\mathbf{b} \\in \\operatorname{Col}(A)$ y el sistema tiene solución." if cl != "SI" else "No coinciden: $\\mathbf{b} \\notin \\operatorname{Col}(A)$ y el sistema es incompatible."),
        ["$\\mathbf{b} \\in \\operatorname{Col}(A)$ si y solo si añadir $\\mathbf{b}$ no crea un pivote nuevo."], "Comparar $\\operatorname{rg}(A)$ con el número de filas.",
    )


def f14_rango_nulidad(r):
    m, n = r.choice([(3, 4), (2, 5), (4, 3), (3, 3), (4, 5)])
    rg = r.randint(1, min(m, n))
    A = matriz_rango(r, m, n, rg) if rg < min(m, n) or True else None
    rg = rango(A)
    base_n = nucleo(A)
    assert rg + len(base_n) == n
    return Ejercicio(
        "C", 3, "Comprobar rango + nulidad", "verificar $\\operatorname{rg}(A) + \\operatorname{nul}(A) = n$ en un ejemplo.",
        f"Para $A = {mat(A)}$ halla $\\operatorname{{rg}}(A)$, una base de $\\ker A$ y comprueba que $\\operatorname{{rg}}(A) + \\operatorname{{nul}}(A) = n$.",
        f"$\\operatorname{{rg}}(A) = {rg}$. Base de $\\ker A$: " + (", ".join(f"${fila_vec(v)}$" for v in base_n) if base_n else "vacía (núcleo trivial)") + f". $\\operatorname{{nul}}(A) = {len(base_n)}$. Suma: ${rg} + {len(base_n)} = {n} = n$.",
        ["El rango es el número de pivotes; la nulidad, el de variables libres."], "Olvidar que $n$ es el número de columnas, no de filas.",
    )


def f14_imagen(r):
    A = matriz_rango(r, 2, 2, r.choice([1, 2])) if r.random() < 0.5 else matriz_rango(r, 3, 2, 2)
    m, n = len(A), len(A[0])
    rg = rango(A)
    base = [columnas(A)[j] for j in base_columnas(A)]
    return Ejercicio(
        "C", 3, "Imagen y núcleo de una transformación", "describir la imagen y el núcleo de $T(\\mathbf{x}) = A\\mathbf{x}$.",
        f"Para $T : \\mathbb{{R}}^{n} \\to \\mathbb{{R}}^{m}$, $T(\\mathbf{{x}}) = A\\mathbf{{x}}$ con $A = {mat(A)}$, describe $\\operatorname{{Im}}(T)$ y $\\ker T$ (dimensión y una base).",
        f"$\\operatorname{{Im}}(T) = \\operatorname{{Col}}(A)$ tiene base " + ", ".join(f"${fila_vec(v)}$" for v in base) + f" y dimensión {rg}. "
        + (f"$\\ker T$ tiene dimensión ${n - rg}$ y base " + ", ".join(f"${fila_vec(v)}$" for v in nucleo(A)) + "." if n > rg else "$\\ker T = \\{\\mathbf{0}\\}$: $T$ es inyectiva.") + f" Comprobación: ${rg} + {n - rg} = {n}$.",
        ["La imagen es el espacio columna."], "Confundir el espacio de llegada con la imagen.",
    )


POOL_K14 = [
    ("Una matriz $5\\times 7$ tiene rango 3. ¿Cuál es la nulidad y en qué espacio vive $\\operatorname{Col}(A)$?", "$\\operatorname{nul} = 7 - 3 = 4$; $\\operatorname{Col}(A) \\subseteq \\mathbb{R}^5$ con dimensión $3$."),
    ("¿Puede una matriz $3\\times 5$ tener $\\ker A = \\{\\mathbf{0}\\}$?", "No: $\\operatorname{nul} \\ge 5 - 3 = 2$."),
    ("¿Puede $A\\mathbf{x} = \\mathbf{b}$ tener solución para todo $\\mathbf{b}$ si $A$ es $5\\times 3$?", "No: $\\operatorname{rg} \\le 3 < 5$, luego $\\operatorname{Col}(A) \\ne \\mathbb{R}^5$."),
    ("Si $A$ es cuadrada $n\\times n$ con $\\operatorname{rg}(A) = n$, ¿qué pasa con $\\ker A$ y con $\\operatorname{Col}(A)$?", "$\\ker A = \\{\\mathbf{0}\\}$ y $\\operatorname{Col}(A) = \\mathbb{R}^n$: hay solución única para todo $\\mathbf{b}$."),
    ("Las operaciones por filas, ¿conservan $\\ker A$? ¿Y $\\operatorname{Col}(A)$?", "Conservan el núcleo ($A\\mathbf{x} = \\mathbf{0} \\iff R\\mathbf{x} = \\mathbf{0}$) pero no el espacio columna; por eso la base de $\\operatorname{Col}(A)$ se toma de la matriz original."),
    ("¿Es posible que $\\dim\\operatorname{Col}(A) > m$ para una matriz $m \\times n$?", "No: $\\operatorname{Col}(A) \\subseteq \\mathbb{R}^m$, así que su dimensión es a lo sumo $m$."),
]


def f14_conceptual(r):
    e = r.sample(POOL_K14, 3)
    return Ejercicio(
        "K", 3, "Preguntas de rango y nulidad", "razonar con rango-nulidad sin calcular.",
        "\n\n".join(f"{chr(97 + i)}) {q}" for i, (q, _) in enumerate(e)),
        "\n\n".join(f"{chr(97 + i)}) {a}" for i, (_, a) in enumerate(e)),
        ["Usa $\\operatorname{rg} + \\operatorname{nul} = n$ y $\\operatorname{rg} \\le \\min(m, n)$."], "Mezclar $m$ y $n$.",
    )


# ----------------------------------------------------------------------------- registro
PLAN = {
    "F09": [(f09_reducida, 4), (f09_indeterminado, 6), (f09_incompatible, 2), (f09_es_reducida, 3), (f09_cuentas, 3), (f09_rango_deficiente, 3), (f09_basicas, 2)],
    "F10": [(f10_factorizar, 8), (f10_resolver, 5), (f10_plu, 4), (f10_falla, 3)],
    "F11": [(f11_rango, 10), (f11_clasificar, 10), (f11_parametro, 6), (f11_conceptual, 3), (f11_libres, 5)],
    "F12": [(f12_pertenencia, 6), (f12_independencia, 8), (f12_base, 6), (f12_geometria, 5), (f12_conceptual, 2)],
    "F13": [(f13_base_nucleo, 10), (f13_pertenece, 4), (f13_solucion_general, 7), (f13_nulidad, 3), (f13_conceptual, 1), (f13_nulidad, 2)],
    "F14": [(f14_base_col, 7), (f14_existe, 6), (f14_rango_nulidad, 5), (f14_imagen, 3), (f14_conceptual, 5)],
}
