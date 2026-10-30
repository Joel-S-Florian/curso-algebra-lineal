"""Plantillas de F05–F08 (matrices y vectores, producto, forma matricial y eliminación de Gauss)."""

from fractions import Fraction as F

import sympy as sp

from algebra import (
    Ejercicio, M, aug, det, fila_vec, lin, mat, mul, pasos_gauss, pasos_tex, por_vec, rango, resolver, rref, sistema, t, trans, ts, vec,
    solucion_general_tex,
)
from plantillas_a import nz, sistema_con_solucion


def mat_azar(r, m, n, lo=-4, hi=5):
    return [[F(r.randint(lo, hi)) for _ in range(n)] for _ in range(m)]


def suma(A, B, s=1):
    return [[a + s * b for a, b in zip(f, g)] for f, g in zip(A, B)]


def esc(c, A):
    return [[c * v for v in f] for f in A]


# ----------------------------------------------------------------------------- F05
def f05_suma(r):
    m, n = r.choice([(2, 2), (2, 3), (3, 2), (3, 3)])
    A, B = mat_azar(r, m, n), mat_azar(r, m, n)
    s = r.choice([1, -1])
    op = "+" if s == 1 else "-"
    return Ejercicio(
        "C", 1, "Suma y resta de matrices", "operar matrices del mismo tamaño entrada a entrada.",
        f"Calcula $A {op} B$ con $A = {mat(A)}$ y $B = {mat(B)}$.",
        f"Se opera entrada a entrada: $A {op} B = {mat(suma(A, B, s))}$.",
        ["Las matrices tienen el mismo tamaño ${}\\times {}$: se pueden sumar o restar.".format(m, n)], "Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.",
    )


def f05_escalar(r):
    m, n = r.choice([(2, 2), (2, 3), (3, 3)])
    A, B = mat_azar(r, m, n, -3, 4), mat_azar(r, m, n, -3, 4)
    c, d = nz(r, -3, 4), nz(r, -3, 4)
    R = suma(esc(c, A), esc(d, B))
    return Ejercicio(
        "C", 2, "Combinación de matrices", "multiplicar por escalares y sumar.",
        f"Calcula ${lin([c, d], ['A', 'B'])}$ con $A = {mat(A)}$ y $B = {mat(B)}$.",
        f"${t(c)}A = {mat(esc(c, A))}$ y ${t(d)}B = {mat(esc(d, B))}$. Sumando: ${mat(R)}$.",
        ["Multiplica cada matriz por su escalar antes de sumar."], "Multiplicar solo una fila por el escalar.",
    )


def f05_traspuesta(r):
    m, n = r.choice([(2, 3), (3, 2), (3, 3), (2, 4)])
    A, B = mat_azar(r, m, n), mat_azar(r, m, n)
    return Ejercicio(
        "C", 2, "Traspuesta", "calcular la traspuesta y comprobar $(A + B)^T = A^T + B^T$.",
        f"Con $A = {mat(A)}$ y $B = {mat(B)}$: a) halla $A^T$ y su tamaño; b) comprueba que $(A + B)^T = A^T + B^T$.",
        f"a) $A^T = {mat(trans(A))}$, de tamaño ${n}\\times {m}$.\n\nb) $A + B = {mat(suma(A, B))}$, luego $(A + B)^T = {mat(trans(suma(A, B)))}$. Además $A^T + B^T = {mat(suma(trans(A), trans(B)))}$: coinciden.",
        ["Las filas de $A$ pasan a ser las columnas de $A^T$."], "Escribir las filas como columnas en otro orden.",
    )


def f05_tamano(r):
    (m, n), (p, q) = r.choice([((2, 3), (2, 3)), ((2, 3), (3, 2)), ((3, 3), (3, 3)), ((2, 2), (2, 3))])
    suma_ok = (m, n) == (p, q)
    prod_ok = n == p
    lineas = [
        f"a) $A + B$: " + (f"sí, de tamaño ${m}\\times {n}$." if suma_ok else "no, los tamaños son distintos."),
        f"b) $3A$: sí, de tamaño ${m}\\times {n}$.",
        f"c) $A^T$: sí, de tamaño ${n}\\times {m}$.",
        f"d) $AB$: " + (f"sí, de tamaño ${m}\\times {q}$ (columnas de $A$ = filas de $B$ = {n})." if prod_ok else f"no, $A$ tiene {n} columnas y $B$ tiene {p} filas."),
    ]
    return Ejercicio(
        "K", 2, "¿Qué operaciones se pueden hacer?", "razonar con tamaños antes de calcular.",
        f"$A$ es de tamaño ${m}\\times {n}$ y $B$ de tamaño ${p}\\times {q}$. Di cuáles de estas operaciones están definidas y qué tamaño tiene el resultado: a) $A + B$; b) $3A$; c) $A^T$; d) $AB$.",
        "\n\n".join(lineas), ["Para sumar, los tamaños deben coincidir; para multiplicar, columnas de la primera = filas de la segunda."], "Creer que se puede multiplicar cuando los tamaños no encajan.",
    )


def f05_vectores(r):
    n = r.choice([2, 3, 4])
    u, v, w = [[F(r.randint(-4, 5)) for _ in range(n)] for _ in range(3)]
    a, b, c = nz(r, -3, 4), nz(r, -3, 4), nz(r, -2, 3)
    R = comb3(a, u, b, v, c, w)
    return Ejercicio(
        "C", 1, "Combinación de vectores", "operar vectores componente a componente.",
        f"Con $\\mathbf{{u}} = {vec(u)}$, $\\mathbf{{v}} = {vec(v)}$ y $\\mathbf{{w}} = {vec(w)}$, calcula ${t(a)}\\mathbf{{u}} + {ts(b)}\\mathbf{{v}} + {ts(c)}\\mathbf{{w}}$.",
        f"Componente a componente: ${vec(R)}$.",
        ["Multiplica cada vector por su número y suma las componentes que ocupan la misma posición."], "Sumar componentes de posiciones distintas.",
    )


def comb3(a, u, b, v, c, w):
    return [a * x + b * y + c * z for x, y, z in zip(u, v, w)]


def f05_tipos(r):
    n = 3
    d = [nz(r, -3, 4) for _ in range(n)]
    diag = [[F(d[i]) if i == j else F(0) for j in range(n)] for i in range(n)]
    sup = [[F(r.randint(1, 5)) if j >= i else F(0) for j in range(n)] for i in range(n)]
    sim = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            sim[i][j] = sim[j][i] = F(r.randint(-3, 5))
    cand = [("diagonal", diag), ("triangular superior", sup), ("simétrica", sim)]
    elegida = r.sample(cand, 3)
    def clasifica(Mx):
        etiquetas = []
        if all(Mx[i][j] == 0 for i in range(n) for j in range(n) if i != j):
            etiquetas.append("diagonal")
        if all(Mx[i][j] == 0 for i in range(n) for j in range(i)):
            etiquetas.append("triangular superior")
        if Mx == trans(Mx):
            etiquetas.append("simétrica")
        return etiquetas
    lista = "\n\n".join(f"{chr(97 + i)}) ${mat(e[1])}$" for i, e in enumerate(elegida))
    sol = "\n\n".join(f"{chr(97 + i)}) " + (", ".join(clasifica(e[1])) or "ninguna de las tres") + "." for i, e in enumerate(elegida))
    return Ejercicio(
        "K", 2, "Tipos de matrices", "reconocer matrices diagonales, triangulares y simétricas.",
        "Indica de qué tipo(s) es cada matriz: diagonal, triangular superior, simétrica (puede ser más de uno).\n\n" + lista,
        sol, ["Una matriz es simétrica si $A = A^T$; triangular superior si todo lo que hay bajo la diagonal es cero."], "Olvidar que toda matriz diagonal también es triangular y simétrica.",
    )


def f05_notacion(r):
    regla, f = r.choice([
        ("i + j", lambda i, j: i + j), ("i - j", lambda i, j: i - j), ("i \\cdot j", lambda i, j: i * j),
        ("2i - j", lambda i, j: 2 * i - j), ("i^2 - j", lambda i, j: i * i - j), ("\\max(i, j)", lambda i, j: max(i, j)),
    ])
    m, n = r.choice([(2, 3), (3, 3), (3, 2)])
    A = [[F(f(i + 1, j + 1)) for j in range(n)] for i in range(m)]
    return Ejercicio(
        "C", 1, "Matriz a partir de una regla", "usar la notación $a_{ij}$ (fila $i$, columna $j$).",
        f"Escribe la matriz $A$ de tamaño ${m}\\times {n}$ con $a_{{ij}} = {regla}$.",
        f"Se calcula cada entrada con $i$ = fila y $j$ = columna: $A = {mat(A)}$. Por ejemplo, $a_{{{m}{n}}} = {t(A[m - 1][n - 1])}$.",
        ["El primer índice es la fila y el segundo la columna."], "Intercambiar fila y columna.",
    )


def f05_geometria(r):
    P, Q = [F(r.randint(-5, 5)) for _ in range(3)], [F(r.randint(-5, 5)) for _ in range(3)]
    PQ = [q - p for p, q in zip(P, Q)]
    medio = [(p + q) / 2 for p, q in zip(P, Q)]
    return Ejercicio(
        "C", 2, "Vector entre dos puntos", "usar la resta de vectores y la media.",
        f"Dados $P = {fila_vec(P)}$ y $Q = {fila_vec(Q)}$, halla el vector $\\overrightarrow{{PQ}}$ y el punto medio del segmento $PQ$.",
        f"$\\overrightarrow{{PQ}} = Q - P = {fila_vec(PQ)}$. El punto medio es $\\frac{{P + Q}}{{2}} = {fila_vec(medio)}$.",
        ["El vector de $P$ a $Q$ es «llegada menos salida»."], "Restar en el orden contrario ($P - Q$).",
    )


# ----------------------------------------------------------------------------- F06
def f06_matriz_vector(r):
    m, n = r.choice([(2, 2), (3, 3), (2, 3), (3, 2)])
    A = mat_azar(r, m, n, -3, 4)
    x = [F(r.randint(-3, 4)) for _ in range(n)]
    y = por_vec(A, x)
    detalle = "; ".join("$" + " + ".join(f"{ts(a)}\\cdot {ts(xi)}" for a, xi in zip(f, x)) + f" = {t(v)}$" for f, v in zip(A, y))
    return Ejercicio(
        "C", 1, "Matriz por vector", "calcular $A\\mathbf{x}$ fila por columna.",
        f"Calcula $A\\mathbf{{x}}$ con $A = {mat(A)}$ y $\\mathbf{{x}} = {vec(x)}$.",
        f"Cada componente es una fila de $A$ por $\\mathbf{{x}}$: {detalle}. Luego $A\\mathbf{{x}} = {vec(y)}$ (un vector de $\\mathbb{{R}}^{m}$).",
        ["Cada fila de $A$ da una componente del resultado."], "Multiplicar por columnas en lugar de por filas sin sumar.",
    )


def f06_producto(r):
    A, B = mat_azar(r, 2, 2, -3, 4), mat_azar(r, 2, 2, -3, 4)
    P = mul(A, B)
    return Ejercicio(
        "C", 2, "Producto de matrices 2×2", "multiplicar fila por columna.",
        f"Calcula $AB$ con $A = {mat(A)}$ y $B = {mat(B)}$.",
        f"La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = {mat(P)}$. "
        f"Por ejemplo, la entrada $(1,1)$: ${ts(A[0][0])}\\cdot {ts(B[0][0])} + {ts(A[0][1])}\\cdot {ts(B[1][0])} = {t(P[0][0])}$.",
        ["Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$."], "Multiplicar entrada con entrada, como en la suma.",
    )


def f06_producto_rect(r):
    A, B = mat_azar(r, 2, 3, -2, 3), mat_azar(r, 3, 2, -2, 3)
    P = mul(A, B)
    return Ejercicio(
        "C", 2, "Producto rectangular", "comprobar que se puede multiplicar y calcular el tamaño del resultado.",
        f"Calcula $AB$ y $BA$ con $A = {mat(A)}$ ($2\\times 3$) y $B = {mat(B)}$ ($3\\times 2$). ¿Qué tamaño tienen?",
        f"$AB$ es $2\\times 2$: ${mat(P)}$. $BA$ es $3\\times 3$: ${mat(mul(B, A))}$. Los productos son distintos hasta en tamaño.",
        ["Mira el tamaño: $(2\\times 3)(3\\times 2)$ da $2\\times 2$."], "Dar el mismo tamaño a $AB$ y $BA$.",
    )


def f06_no_conmuta(r):
    A, B = mat_azar(r, 2, 2, -2, 3), mat_azar(r, 2, 2, -2, 3)
    while mul(A, B) == mul(B, A):
        A, B = mat_azar(r, 2, 2, -2, 3), mat_azar(r, 2, 2, -2, 3)
    return Ejercicio(
        "K", 3, "El producto no conmuta", "comprobar con un ejemplo que $AB \\ne BA$.",
        f"Con $A = {mat(A)}$ y $B = {mat(B)}$, calcula $AB$ y $BA$ y comprueba que son distintos.",
        f"$AB = {mat(mul(A, B))}$ y $BA = {mat(mul(B, A))}$. Son distintas: el producto de matrices no es conmutativo.",
        ["Calcula los dos productos por separado."], "Suponer que $AB = BA$ por analogía con los números.",
    )


def f06_definido(r):
    (m, n), (p, q) = r.choice([((2, 3), (3, 4)), ((3, 2), (3, 2)), ((4, 2), (2, 2)), ((1, 3), (3, 1)), ((2, 2), (3, 3))])
    ab = n == p
    ba = q == m
    return Ejercicio(
        "K", 2, "¿Está definido el producto?", "decidir con los tamaños si $AB$ y $BA$ existen.",
        f"$A$ es de tamaño ${m}\\times {n}$ y $B$ de tamaño ${p}\\times {q}$. ¿Están definidos $AB$ y $BA$? Si lo están, ¿de qué tamaño son?",
        f"$AB$: " + (f"sí, ${m}\\times {q}$." if ab else f"no ($A$ tiene {n} columnas y $B$ tiene {p} filas).") + f"\n\n$BA$: " + (f"sí, ${p}\\times {n}$." if ba else f"no ($B$ tiene {q} columnas y $A$ tiene {m} filas)."),
        ["Compara las columnas de la primera matriz con las filas de la segunda."], "Mirar filas con filas.",
    )


def f06_transformacion(r):
    nombre, T, desc = r.choice([
        ("giro de $90^\\circ$", M([0, -1], [1, 0]), "gira $90^\\circ$ en sentido antihorario"),
        ("reflexión en el eje $x$", M([1, 0], [0, -1]), "refleja respecto del eje $x$"),
        ("reflexión en el eje $y$", M([-1, 0], [0, 1]), "refleja respecto del eje $y$"),
        ("escala", M([2, 0], [0, 3]), "multiplica $x$ por $2$ e $y$ por $3$"),
        ("cizalla", M([1, 2], [0, 1]), "desplaza horizontalmente en proporción a $y$ (cizalla)"),
        ("proyección en el eje $x$", M([1, 0], [0, 0]), "proyecta sobre el eje $x$"),
    ])
    ptos = [[F(1), F(0)], [F(0), F(1)], [F(r.randint(-3, 3)), F(r.randint(1, 3))]]
    imgs = [por_vec(T, p) for p in ptos]
    return Ejercicio(
        "C", 2, "Efecto de una transformación", "ver una matriz $2\\times 2$ como transformación del plano.",
        f"La matriz $T = {mat(T)}$ define $\\mathbf{{x}} \\mapsto T\\mathbf{{x}}$. Halla la imagen de {', '.join(f'$' + fila_vec(p) + '$' for p in ptos)} y describe qué hace $T$.",
        "Imágenes: " + ", ".join(f"$T{fila_vec(p)} = {fila_vec(q)}$" for p, q in zip(ptos, imgs)) + f".\n\nLas columnas de $T$ son las imágenes de $(1,0)$ y $(0,1)$. Es un {nombre}: {desc}.",
        ["Las columnas de $T$ son las imágenes de la base canónica."], "Multiplicar el punto por la matriz en el orden contrario.",
    )


def f06_composicion(r):
    A, B = mat_azar(r, 2, 2, -2, 3), mat_azar(r, 2, 2, -2, 3)
    x = [F(r.randint(-3, 3)), F(r.randint(-3, 3))]
    BA = mul(B, A)
    return Ejercicio(
        "C", 3, "Composición de transformaciones", "ver el producto de matrices como composición.",
        f"$S$ tiene matriz $A = {mat(A)}$ y $T$ tiene matriz $B = {mat(B)}$. a) Halla la matriz de $T \\circ S$ (primero $S$, luego $T$). b) Compruébalo con $\\mathbf{{x}} = {fila_vec(x)}$.",
        f"a) La matriz es $BA = {mat(BA)}$ (la primera transformación se escribe a la derecha).\n\nb) $A\\mathbf{{x}} = {fila_vec(por_vec(A, x))}$ y $B(A\\mathbf{{x}}) = {fila_vec(por_vec(B, por_vec(A, x)))}$; por otro lado $(BA)\\mathbf{{x}} = {fila_vec(por_vec(BA, x))}$. Coinciden.",
        ["$T(S(\\mathbf{x})) = B(A\\mathbf{x}) = (BA)\\mathbf{x}$."], "Escribir $AB$ en lugar de $BA$.",
    )


# ----------------------------------------------------------------------------- F07
def f07_a_matricial(r):
    n = r.choice([2, 3, 3])
    A, b, x0 = sistema_con_solucion(r, n, coef=(-3, 3))
    incog = "\\\\ ".join(["x", "y", "z"][:n])
    return Ejercicio(
        "C", 1, "Del sistema a $A\\mathbf{x} = \\mathbf{b}$", "escribir un sistema en forma matricial.",
        f"Escribe en la forma $A\\mathbf{{x}} = \\mathbf{{b}}$ el sistema ${sistema(A, b)}$.",
        f"${mat(A)}\\begin{{bmatrix}} {incog} \\end{{bmatrix}} = {vec(b)}$, con $A = {mat(A)}$ (coeficientes) y $\\mathbf{{b}} = {vec(b)}$ (términos independientes).",
        ["Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas."], "Meter el término independiente dentro de $A$.",
    )


def f07_aumentada(r):
    n = r.choice([2, 3, 3])
    A, b, x0 = sistema_con_solucion(r, n, coef=(-3, 3))
    return Ejercicio(
        "C", 1, "Matriz aumentada", "escribir $[A \\mid \\mathbf{b}]$ a partir del sistema.",
        f"Escribe la matriz aumentada de ${sistema(A, b)}$.",
        f"Se pegan los coeficientes y, tras una barra, los términos independientes: ${aug(A, b)}$.",
        ["Una fila por ecuación, una columna por incógnita y una última columna para los números."], "Olvidar la última columna o ponerla con el signo cambiado.",
    )


def f07_a_sistema(r):
    n = r.choice([2, 3, 3])
    A, b, x0 = sistema_con_solucion(r, n, coef=(-3, 3))
    comprobaciones = ", ".join(
        "$" + " + ".join(ts(a) + "\\cdot " + ts(xi) for a, xi in zip(f, x0)) + f" = {t(sum(a * xi for a, xi in zip(f, x0)))}$" for f in A
    )
    return Ejercicio(
        "C", 1, "De la matriz aumentada al sistema", "leer un sistema a partir de $[A \\mid \\mathbf{b}]$.",
        f"Escribe el sistema que representa ${aug(A, b)}$ (incógnitas {', '.join(['x', 'y', 'z'][:n])}) y comprueba que $({', '.join(t(v) for v in x0)})$ es solución.",
        f"El sistema es ${sistema(A, b)}$. Comprobación: {comprobaciones}.",
        ["La fila $[a\\ b\\ c \\mid d]$ es la ecuación $ax + by + cz = d$."], "Leer las columnas como si fueran filas.",
    )


def f07_tamanos(r):
    m, n = r.choice([(2, 3), (3, 3), (4, 3), (3, 4), (2, 2)])
    return Ejercicio(
        "K", 2, "Tamaños en $A\\mathbf{x} = \\mathbf{b}$", "relacionar ecuaciones e incógnitas con los tamaños de $A$, $\\mathbf{x}$ y $\\mathbf{b}$.",
        f"Un sistema tiene {m} ecuaciones y {n} incógnitas. ¿Qué tamaño tienen $A$, $\\mathbf{{x}}$, $\\mathbf{{b}}$ y $[A \\mid \\mathbf{{b}}]$?",
        f"$A$ es ${m}\\times {n}$; $\\mathbf{{x}}$ es ${n}\\times 1$; $\\mathbf{{b}}$ es ${m}\\times 1$; $[A \\mid \\mathbf{{b}}]$ es ${m}\\times {n + 1}$. El producto $A\\mathbf{{x}}$ está definido: $({m}\\times {n})({n}\\times 1)$ da ${m}\\times 1$.",
        ["Filas de $A$ = ecuaciones; columnas de $A$ = incógnitas."], "Intercambiar ecuaciones e incógnitas.",
    )


def f07_comprobar(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    falso = [v + 1 for v in x0]
    candidatos = [x0, falso]
    r.shuffle(candidatos)
    res = [por_vec(A, c) for c in candidatos]
    return Ejercicio(
        "C", 2, "¿Es solución? con $A\\mathbf{x} = \\mathbf{b}$", "comprobar candidatos calculando $A\\mathbf{x}$.",
        f"Para $A = {mat(A)}$ y $\\mathbf{{b}} = {vec(b)}$, ¿cuáles de los vectores {', '.join('$' + fila_vec(c) + '$' for c in candidatos)} cumplen $A\\mathbf{{x}} = \\mathbf{{b}}$?",
        "\n\n".join(f"${fila_vec(c)}$: $A\\mathbf{{x}} = {vec(y)}$ " + ("= $\\mathbf{b}$ ✓." if y == b else "≠ $\\mathbf{b}$: no es solución.") for c, y in zip(candidatos, res)),
        ["Calcula $A\\mathbf{x}$ para cada candidato y compáralo con $\\mathbf{b}$."], "Comprobar solo una ecuación.",
    )


# ----------------------------------------------------------------------------- F08
def f08_unica(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    return Ejercicio(
        "C", 3, "Gauss en un sistema 3×3", "escalonar $[A \\mid \\mathbf{b}]$ y resolver hacia atrás.",
        f"Resuelve por eliminación gaussiana ${sistema(A, b)}$ y comprueba el resultado.",
        pasos_tex(A, b, False) + f"\nSustitución hacia atrás: $({', '.join(t(v) for v in x0)})$. Comprobación en la primera ecuación: ${' + '.join(ts(a) + chr(92) + 'cdot ' + ts(x) for a, x in zip(A[0], x0))} = {t(b[0])}$.",
        ["Haz ceros bajo el primer pivote y luego bajo el segundo."], "Aplicar la operación a la matriz pero no a la columna de $\\mathbf{b}$.",
    )


def f08_con_intercambio(r):
    while True:
        A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
        A = [f[:] for f in A]
        if A[0][0] != 0 and any(A[i][0] != 0 for i in range(1, 3)):
            # intercambiar para forzar un 0 en la posición (1,1): se hace con las filas 0 y 1 si A[1][0] == 0 tras construcción
            pass
        # forzamos a_11 = 0 poniendo una fila con cero primero
        f0 = [F(0), F(nz(r, -3, 3)), F(nz(r, -3, 3))]
        A2 = [f0, A[1], A[2]]
        if det(A2) != 0:
            b2 = por_vec(A2, x0)
            return Ejercicio(
                "C", 3, "Pivote nulo: hay que intercambiar", "intercambiar filas cuando el primer pivote es cero.",
                f"Resuelve ${sistema(A2, b2)}$ por eliminación gaussiana. ¿Por qué hay que intercambiar filas?",
                "El coeficiente de $x$ en la primera ecuación es $0$, así que no puede ser pivote: se intercambia con una fila que tenga $x$.\n\n" + pasos_tex(A2, b2, False) + f"\nSolución: $({', '.join(t(v) for v in x0)})$.",
                ["Si el pivote es cero, busca debajo una fila con un elemento no nulo en esa columna."], "Dividir entre el pivote cero.",
            )


def f08_incompatible(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    f3 = [A[0][j] + A[1][j] for j in range(3)]
    A = [A[0], A[1], f3]
    b = [b[0], b[1], b[0] + b[1] + nz(r, 1, 4)]
    return Ejercicio(
        "C", 3, "Sistema sin solución", "reconocer una fila contradictoria.",
        f"Resuelve ${sistema(A, b)}$.",
        pasos_tex(A, b, False) + "\nLa última fila queda $[\\,0\\ 0\\ 0 \\mid c\\,]$ con $c \\ne 0$: es la ecuación $0 = c$, imposible. El sistema es incompatible (no tiene solución).",
        ["Mira si la tercera ecuación es combinación de las otras dos en los coeficientes."], "Seguir operando después de encontrar $0 = c$.",
    )


def f08_indeterminado(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    f3 = [A[0][j] + A[1][j] for j in range(3)]
    A = [A[0], A[1], f3]
    b = [b[0], b[1], b[0] + b[1]]
    res = resolver(A, b)
    return Ejercicio(
        "C", 3, "Infinitas soluciones", "reconocer una fila nula y escribir la solución con un parámetro.",
        f"Resuelve ${sistema(A, b)}$.",
        pasos_tex(A, b, False) + f"\nQueda una fila de ceros y una variable libre. Solución general: ${solucion_general_tex(res[1], res[2])}$ con $s \\in \\mathbb{{R}}$ (compatible indeterminado).",
        ["Una ecuación es suma de las otras dos."], "Decir que no hay solución porque aparece una fila de ceros.",
    )


def f08_error(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    while A[0][0] == 0 or A[1][0] == 0:
        A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    c = -A[1][0] / A[0][0]
    mal = [A[1][j] + c * A[0][j] for j in range(3)] + [b[1]]
    bien = [A[1][j] + c * A[0][j] for j in range(3)] + [b[1] + c * b[0]]
    op = f"R_2 \\leftarrow R_2 {'+' if c > 0 else '-'} {t(abs(c)) if abs(c) != 1 else ''}R_1"
    return Ejercicio(
        "K", 4, "Encuentra el error en la eliminación", "detectar una operación aplicada solo a los coeficientes.",
        f"Para ${sistema(A, b)}$ un estudiante aplica ${op}$ y obtiene la segunda fila $\\left[\\begin{{array}}{{ccc|c}} {' & '.join(t(v) for v in mal[:3])} & {t(mal[3])} \\end{{array}}\\right]$. ¿Es correcto? Corrígelo.",
        f"No: la operación hay que aplicarla a la fila entera, columna de $\\mathbf{{b}}$ incluida. El estudiante dejó $b_2 = {t(b[1])}$ sin cambiar. Lo correcto es $b_2 + ({t(c)})\\,b_1 = {t(bien[3])}$, es decir, la fila "
        f"$\\left[\\begin{{array}}{{ccc|c}} {' & '.join(t(v) for v in bien[:3])} & {t(bien[3])} \\end{{array}}\\right]$.",
        ["Una operación elemental actúa sobre todas las entradas de la fila de $[A \\mid \\mathbf{b}]$."], "Operar solo sobre la parte de coeficientes.",
    )


def f08_parametro(r):
    a = sp.symbols("a")
    forma = r.choice([0, 1])
    if forma == 0:
        Aa = sp.Matrix([[1, 1, 1], [1, a, 1], [1, 1, a]])
        bs = [1, r.choice([1, 2]), 1]
        etiqueta = f"\\begin{{cases}} x + y + z = 1 \\\\ x + ay + z = {bs[1]} \\\\ x + y + az = 1 \\end{{cases}}"
    else:
        k = nz(r, 1, 3)
        Aa = sp.Matrix([[1, 1, 1], [1, 2, a], [1, 4, a * a]])
        bs = [1, r.choice([0, 1, 2]), r.choice([0, 1, 4])]
        etiqueta = f"\\begin{{cases}} x + y + z = 1 \\\\ x + 2y + az = {bs[1]} \\\\ x + 4y + a^2 z = {bs[2]} \\end{{cases}}"
    d = sp.factor(Aa.det())
    raices = sorted(sp.solve(Aa.det(), a), key=lambda v: (not v.is_real, v))
    raices = [rr for rr in raices if rr.is_rational]
    lineas = []
    for rr in raices:
        Av = [[F(int(sp.Rational(v.subs(a, rr)).p), int(sp.Rational(v.subs(a, rr)).q)) for v in Aa.row(i)] for i in range(3)]
        res = resolver(Av, [F(v) for v in bs])
        texto = {"SI": "incompatible (sin solución)", "SCD": "solución única", "SCI": f"infinitas soluciones ({3 - rango(Av)} parámetro libre)"}[res[0]]
        lineas.append(f"Si $a = {sp.latex(rr)}$: {texto}.")
    return Ejercicio(
        "C", 4, "Sistema 3×3 con parámetro", "discutir un sistema con un parámetro: determinante y valores críticos.",
        f"Discute el sistema según los valores de $a$: ${etiqueta}$",
        f"El determinante de la matriz de coeficientes es $\\det A = {sp.latex(d)}$. Se anula para $a \\in \\{{{', '.join(sp.latex(rr) for rr in raices)}\\}}$. Para los demás valores de $a$ hay solución única.\n\n" + "\n\n".join(lineas),
        ["Calcula el determinante o escalona dejando $a$ como letra.", "Los valores críticos son los que anulan un pivote."], "No estudiar por separado cada valor crítico.",
    )


# ----------------------------------------------------------------------------- registro
PLAN = {
    "F05": [(f05_suma, 6), (f05_escalar, 4), (f05_traspuesta, 4), (f05_tamano, 4), (f05_vectores, 7), (f05_tipos, 5), (f05_notacion, 4), (f05_geometria, 6)],
    "F06": [(f06_matriz_vector, 6), (f06_producto, 6), (f06_producto_rect, 3), (f06_no_conmuta, 3), (f06_definido, 4), (f06_transformacion, 5), (f06_composicion, 3)],
    "F07": [(f07_a_matricial, 6), (f07_aumentada, 5), (f07_a_sistema, 5), (f07_tamanos, 4), (f07_comprobar, 3)],
    "F08": [(f08_unica, 10), (f08_con_intercambio, 4), (f08_incompatible, 3), (f08_indeterminado, 4), (f08_error, 3), (f08_parametro, 4)],
}
