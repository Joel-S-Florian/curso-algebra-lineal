"""Plantillas de F15 (problemas integradores) y lista de F16 (demostraciones)."""

from fractions import Fraction as F
from math import gcd

import sympy as sp

from algebra import (
    Ejercicio, M, aug, base_columnas, columnas, det, fila_vec, mat, mul, nucleo, pasos_tex, por_vec, rango, resolver, rref, sistema, t, trans, ts, vec,
    solucion_general_tex,
)
from plantillas_a import nz, sistema_con_solucion
from plantillas_c import NOMBRE, clasifica_rf, fuera_de_columna, matriz_rango, sistema_tipo


# ----------------------------------------------------------------------------- F15
def f15_ficha(r, tam=None):
    m, n = tam or r.choice([(3, 4), (4, 4), (3, 5)])
    rg = 2 if (m, n) == (3, 4) else r.randint(2, min(m, n) - 1)
    A = matriz_rango(r, m, n, rg)
    x0 = [F(r.randint(-2, 3)) for _ in range(n)]
    b = por_vec(A, x0)
    if r.random() < 0.35:
        b = fuera_de_columna(A, b)
    red, piv = rref(A)
    ra, rab, cl = clasifica_rf(A, b)
    base_n = nucleo(A)
    cols = columnas(A)
    s = f"**a)** Reduciendo, ${mat(A)} \\to {mat(red)}$: pivotes en las columnas {', '.join(str(p + 1) for p in piv)}, luego $\\operatorname{{rg}}(A) = {len(piv)}$.\n\n"
    s += f"**b)** $\\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = {rab}$. " + ("Los rangos coinciden" if ra == rab else "Los rangos son distintos") + f": {NOMBRE[cl]}.\n\n"
    if cl != "SI":
        res = resolver(A, b)
        s += f"Solución general: ${solucion_general_tex(res[1], res[2]) if cl == 'SCI' else fila_vec(res[1])}$.\n\n"
    s += f"**c)** Base de $\\ker A$: " + ", ".join(f"${fila_vec(v)}$" for v in base_n) + f" (dimensión {len(base_n)}).\n\n"
    s += f"**d)** Base de $\\operatorname{{Col}}(A)$ (columnas pivote de $A$): " + ", ".join(f"${fila_vec(cols[p])}$" for p in piv) + f" (dimensión {len(piv)}). " + (f"Además $\\mathbf{{b}} \\in \\operatorname{{Col}}(A)$." if cl != "SI" else "Además $\\mathbf{b} \\notin \\operatorname{Col}(A)$.") + "\n\n"
    s += f"**e)** $\\operatorname{{rg}} + \\operatorname{{nul}} = {len(piv)} + {len(base_n)} = {n} = n$ ✓."
    return Ejercicio(
        "C", 4, "Ficha completa de una matriz", "reunir rango, clasificación, solución, núcleo y espacio columna de un mismo problema.",
        f"Sea $A = {mat(A)}$ y $\\mathbf{{b}} = {vec(b)}$. a) Calcula la forma reducida y el rango de $A$. b) Clasifica $A\\mathbf{{x}} = \\mathbf{{b}}$ y, si es compatible, da la solución general. c) Halla una base de $\\ker A$. d) Halla una base de $\\operatorname{{Col}}(A)$ y decide si $\\mathbf{{b}} \\in \\operatorname{{Col}}(A)$. e) Comprueba el teorema del rango y la nulidad.",
        s, ["Una sola reducción de $A$ (y de $[A \\mid \\mathbf{b}]$) contesta casi todo."], "Tomar las columnas de la reducida como base de $\\operatorname{Col}(A)$.",
    )


def f15_mezcla(r):
    A = [[F(r.randint(1, 5)) for _ in range(3)] for _ in range(3)]
    while det(A) == 0:
        A = [[F(r.randint(1, 5)) for _ in range(3)] for _ in range(3)]
    x0 = [F(r.randint(1, 6)) for _ in range(3)]
    b = por_vec(A, x0)
    nombres = r.choice([("pienso A", "pienso B", "pienso C"), ("aleación 1", "aleación 2", "aleación 3"), ("mezcla P", "mezcla Q", "mezcla R")])
    rasgos = r.choice([("proteínas", "grasas", "fibra"), ("cobre", "estaño", "zinc"), ("nitrógeno", "fósforo", "potasio")])
    tabla = "\n".join(f"- 1 kg de {nombres[j]} aporta " + ", ".join(f"{t(A[i][j])} g de {rasgos[i]}" for i in range(3)) + "." for j in range(3))
    return Ejercicio(
        "C", 3, "Mezclas", "modelar con un sistema $3\\times 3$ y resolverlo.",
        f"Se mezclan tres productos. Por kilogramo:\n\n{tabla}\n\nSe quiere una mezcla con {t(b[0])} g de {rasgos[0]}, {t(b[1])} g de {rasgos[1]} y {t(b[2])} g de {rasgos[2]}. ¿Cuántos kg de cada producto hay que mezclar?",
        f"Con $x, y, z$ los kg de {nombres[0]}, {nombres[1]} y {nombres[2]}: ${sistema(A, b)}$.\n\n" + pasos_tex(A, b, False) + f"\nSolución: $({', '.join(t(v) for v in x0)})$ kg. Todas las cantidades son positivas, así que es una mezcla posible.",
        ["Una ecuación por cada rasgo; una incógnita por cada producto."], "Poner los rasgos en las columnas en lugar de en las filas.",
    )


def f15_trafico(r):
    x0 = [r.randint(1, 8) for _ in range(4)]
    a, b, c, d = x0[0] + x0[1], x0[1] + x0[2], x0[2] + x0[3], x0[3] + x0[0]
    A = M([1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1])
    bb = [F(a), F(b), F(c), F(d)]
    res = resolver(A, bb)
    dirn = res[2][0]
    xp = res[1]
    # x = xp + s*dirn con todas las componentes >= 0
    cotas_inf, cotas_sup = [], []
    for xi, di in zip(xp, dirn):
        if di > 0:
            cotas_inf.append(-xi / di)
        elif di < 0:
            cotas_sup.append(-xi / di)
    lo, hi = max(cotas_inf), min(cotas_sup)
    return Ejercicio(
        "C", 4, "Flujo de tráfico en una rotonda", "modelar un balance de flujos y discutir el rango admisible.",
        f"Cuatro tramos de una rotonda llevan $x_1, x_2, x_3, x_4$ vehículos por minuto. En las cuatro entradas deben cumplirse $x_1 + x_2 = {a}$, $x_2 + x_3 = {b}$, $x_3 + x_4 = {c}$, $x_4 + x_1 = {d}$. Resuelve el sistema y halla qué valores son posibles si ningún flujo puede ser negativo.",
        f"Sistema: ${sistema(A, bb, ['x_1', 'x_2', 'x_3', 'x_4'])}$.\n\n" + pasos_tex(A, bb, False, maximo=0) + f"\nRango $3 < 4$: una variable libre. Solución general: ${solucion_general_tex(xp, [dirn])}$ (con $s$ el parámetro).\n\nPara que todas las componentes sean $\\ge 0$ se necesita ${t(lo)} \\le s \\le {t(hi)}$. Por ejemplo $s = {t(lo)}$ da $({', '.join(t(p + lo * d_) for p, d_ in zip(xp, dirn))})$.",
        ["El sistema tiene una ecuación redundante: la suma de las ecuaciones 1 y 3 es igual a la de las 2 y 4."], "Aceptar valores del parámetro que dan flujos negativos.",
    )


ESPECIES = {
    "CH_4": {"C": 1, "H": 4}, "C_2H_6": {"C": 2, "H": 6}, "C_3H_8": {"C": 3, "H": 8}, "C_4H_{10}": {"C": 4, "H": 10},
    "C_2H_5OH": {"C": 2, "H": 6, "O": 1}, "O_2": {"O": 2}, "CO_2": {"C": 1, "O": 2}, "H_2O": {"H": 2, "O": 1},
    "Fe": {"Fe": 1}, "Fe_2O_3": {"Fe": 2, "O": 3}, "Al": {"Al": 1}, "Al_2O_3": {"Al": 2, "O": 3},
    "N_2": {"N": 2}, "H_2": {"H": 2}, "NH_3": {"N": 1, "H": 3},
}
REACCIONES = [
    (["CH_4", "O_2"], ["CO_2", "H_2O"]), (["C_2H_6", "O_2"], ["CO_2", "H_2O"]), (["C_3H_8", "O_2"], ["CO_2", "H_2O"]),
    (["C_4H_{10}", "O_2"], ["CO_2", "H_2O"]), (["C_2H_5OH", "O_2"], ["CO_2", "H_2O"]), (["Fe", "O_2"], ["Fe_2O_3"]),
    (["Al", "O_2"], ["Al_2O_3"]), (["N_2", "H_2"], ["NH_3"]),
]


def f15_quimica(r):
    reac, prod = r.choice(REACCIONES)
    especies = reac + prod
    elementos = sorted({e for s_ in especies for e in ESPECIES[s_]})
    A = [[F(ESPECIES[s_].get(e, 0) * (1 if s_ in reac else -1)) for s_ in especies] for e in elementos]
    base = nucleo(A)
    assert len(base) == 1
    v = base[0]
    den = 1
    for x in v:
        den = den * x.denominator // gcd(den, x.denominator)
    v = [x * den for x in v]
    g = 0
    for x in v:
        g = gcd(g, int(x))
    v = [x / g for x in v]
    if v[0] < 0:
        v = [-x for x in v]
    assert all(x > 0 for x in v)
    letras = "abcd"[: len(especies)]
    ecuaciones = ", ".join(f"{e}: " + " + ".join(f"{ESPECIES[s_].get(e, 0) * (1 if s_ in reac else -1)}{letras[i]}" for i, s_ in enumerate(especies) if ESPECIES[s_].get(e, 0)).replace("+ -", "- ") + " = 0" for e in elementos)
    ec_tex = " + ".join(reac) + r" \longrightarrow " + " + ".join(prod)
    ajust = " + ".join(f"{int(c) if c != 1 else ''}{s_}" for c, s_ in zip(v[: len(reac)], reac)) + r" \longrightarrow " + " + ".join(f"{int(c) if c != 1 else ''}{s_}" for c, s_ in zip(v[len(reac):], prod))
    return Ejercicio(
        "C", 4, "Balanceo de una reacción química", "plantear un sistema homogéneo y hallar su solución entera mínima.",
        f"Ajusta la reacción ${ec_tex}$ planteando un sistema lineal con un coeficiente por sustancia ({', '.join(letras)}).",
        f"Se plantea un balance por elemento (reactivos positivos, productos negativos): {ecuaciones}. Es un sistema homogéneo con $\\operatorname{{nul}} = 1$: el núcleo es una recta, generada por ${fila_vec(v)}$ (con los enteros positivos más pequeños). "
        f"Reacción ajustada: ${ajust}$.",
        ["Una ecuación por cada elemento químico.", "La solución es única salvo múltiplos: busca la entera más pequeña con todos los coeficientes positivos."], "Dejar coeficientes fraccionarios o no comprobar el balance de cada elemento.",
    )


def f15_interpolacion(r):
    xs = sorted(r.sample(range(-3, 4), 3))
    c0, c1, c2 = F(nz(r, -4, 4)), F(r.randint(-4, 4)), F(nz(r, -3, 3))
    ys = [c0 + c1 * x + c2 * x * x for x in xs]
    A = [[F(1), F(x), F(x * x)] for x in xs]
    sol = resolver(A, ys)[1]
    assert sol == [c0, c1, c2]
    return Ejercicio(
        "C", 3, "Parábola por tres puntos", "plantear y resolver un sistema de interpolación.",
        f"Halla la parábola $y = c_0 + c_1x + c_2x^2$ que pasa por {', '.join('$(' + str(x) + ', ' + t(y) + ')$' for x, y in zip(xs, ys))}.",
        f"Cada punto da una ecuación: ${sistema(A, ys, ['c_0', 'c_1', 'c_2'])}$.\n\n" + pasos_tex(A, ys, False) + f"\nSolución: $c_0 = {t(c0)}$, $c_1 = {t(c1)}$, $c_2 = {t(c2)}$: $y = {t(c0)} {'+' if c1 >= 0 else '-'} {t(abs(c1))}x {'+' if c2 >= 0 else '-'} {t(abs(c2))}x^2$.",
        ["Sustituye cada punto en $y = c_0 + c_1x + c_2x^2$: las incógnitas son los $c_i$."], "Tomar $x, y$ como incógnitas en lugar de los coeficientes.",
    )


def f15_param_completo(r):
    a = sp.symbols("a")
    forma = r.choice([0, 1, 2])
    if forma == 0:
        Aa, bs = sp.Matrix([[1, 1, 1], [1, a, 1], [1, 1, a]]), [1, 1, 1]
        txt = "\\begin{cases} x + y + z = 1 \\\\ x + ay + z = 1 \\\\ x + y + az = 1 \\end{cases}"
    elif forma == 1:
        Aa, bs = sp.Matrix([[1, 1, 1], [1, 2, a], [1, 4, a * a]]), [1, 1, 1]
        txt = "\\begin{cases} x + y + z = 1 \\\\ x + 2y + az = 1 \\\\ x + 4y + a^2 z = 1 \\end{cases}"
    else:
        Aa, bs = sp.Matrix([[1, 1, a], [1, a, 1], [a, 1, 1]]), [1, 1, 1]
        txt = "\\begin{cases} x + y + az = 1 \\\\ x + ay + z = 1 \\\\ ax + y + z = 1 \\end{cases}"
    raices = [rr for rr in sp.solve(Aa.det(), a) if rr.is_rational]
    lineas = []
    for rr in raices:
        Av = [[F(int(sp.Rational(v.subs(a, rr)).p), int(sp.Rational(v.subs(a, rr)).q)) for v in Aa.row(i)] for i in range(3)]
        bv = [F(v) for v in bs]
        ra, rab, cl = clasifica_rf(Av, bv)
        extra = ""
        if cl == "SCI":
            res = resolver(Av, bv)
            extra = f" Solución general: ${solucion_general_tex(res[1], res[2])}$; núcleo de dimensión {len(res[2])}."
        lineas.append(f"$a = {sp.latex(rr)}$: $\\operatorname{{rg}}(A) = {ra}$, $\\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = {rab}$, {NOMBRE[cl]}." + extra)
    return Ejercicio(
        "C", 5, "Discusión completa con parámetro", "discutir, resolver y describir el núcleo para cada valor del parámetro.",
        f"Discute y resuelve según $a$: ${txt}$. Para los valores en que haya infinitas soluciones, escribe la solución general con una base del núcleo.",
        f"$\\det A = {sp.latex(sp.factor(Aa.det()))}$, que se anula en $a \\in \\{{{', '.join(sp.latex(rr) for rr in raices)}\\}}$. Si $a$ es otro valor, $\\operatorname{{rg}}(A) = \\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = 3$: solución única.\n\n" + "\n\n".join(lineas),
        ["Primero el determinante; después, un caso por cada valor crítico, comparando rangos."], "No resolver los casos en que hay infinitas soluciones.",
    )


POOL_VF = [
    ("Un sistema con más incógnitas que ecuaciones siempre tiene infinitas soluciones.", False, "Falso: puede ser incompatible, por ejemplo $x + y = 1$, $x + y = 2$ (con 3 incógnitas, si se añade $z$)."),
    ("Un sistema homogéneo con más incógnitas que ecuaciones siempre tiene infinitas soluciones.", True, "Verdadero: $\\mathbf{0}$ es solución y $\\operatorname{rg} \\le m < n$ deja variables libres."),
    ("Si $\\operatorname{rg}(A) = n$ (columnas), $A\\mathbf{x} = \\mathbf{b}$ tiene solución para todo $\\mathbf{b}$.", False, "Falso: eso da unicidad si existe solución; la existencia para todo $\\mathbf{b}$ exige $\\operatorname{rg}(A) = m$."),
    ("Si $\\operatorname{rg}(A) = m$ (filas), $A\\mathbf{x} = \\mathbf{b}$ tiene solución para todo $\\mathbf{b}$.", True, "Verdadero: entonces $\\operatorname{Col}(A) = \\mathbb{R}^m$."),
    ("El producto de matrices es conmutativo.", False, "Falso: en general $AB \\ne BA$ (a veces ni siquiera tienen el mismo tamaño)."),
    ("Si $AB = 0$, entonces $A = 0$ o $B = 0$.", False, "Falso: $\\begin{bmatrix} 1&0\\\\0&0 \\end{bmatrix}\\begin{bmatrix} 0&0\\\\0&1 \\end{bmatrix} = 0$."),
    ("El núcleo de una matriz $m \\times n$ es un subespacio de $\\mathbb{R}^n$.", True, "Verdadero: contiene a $\\mathbf{0}$ y es cerrado bajo suma y múltiplos."),
    ("El espacio columna de una matriz $m \\times n$ es un subespacio de $\\mathbb{R}^n$.", False, "Falso: las columnas tienen $m$ componentes, así que $\\operatorname{Col}(A) \\subseteq \\mathbb{R}^m$."),
    ("Las operaciones elementales por filas conservan el espacio columna.", False, "Falso: conservan el núcleo y el espacio fila, no el espacio columna."),
    ("Las operaciones elementales por filas conservan el núcleo.", True, "Verdadero: $A\\mathbf{x} = \\mathbf{0} \\iff R\\mathbf{x} = \\mathbf{0}$."),
    ("Toda matriz invertible admite $A = LU$ sin intercambios de filas.", False, "Falso: $\\begin{bmatrix} 0&1\\\\1&0 \\end{bmatrix}$ es invertible y su primer pivote es $0$."),
    ("Toda matriz cuadrada invertible admite $PA = LU$ con $P$ de permutación.", True, "Verdadero: siempre hay una fila con elemento no nulo que se puede llevar a la posición del pivote."),
    ("Si $A\\mathbf{x} = \\mathbf{b}$ tiene solución única, entonces $A\\mathbf{x} = \\mathbf{0}$ solo tiene la solución trivial.", True, "Verdadero: otra solución del homogéneo daría otra solución del sistema ($\\mathbf{x} + \\mathbf{n}$)."),
    ("$\\operatorname{rg}(A) + \\operatorname{nul}(A) = m$.", False, "Falso: la suma es $n$, el número de columnas."),
    ("Tres vectores de $\\mathbb{R}^2$ son siempre linealmente dependientes.", True, "Verdadero: la matriz $2 \\times 3$ tiene rango $\\le 2 < 3$."),
    ("Dos vectores de $\\mathbb{R}^3$ pueden generar todo $\\mathbb{R}^3$.", False, "Falso: el rango de una matriz $3 \\times 2$ es a lo sumo $2 < 3$."),
    ("Un sistema de 3 ecuaciones con 3 incógnitas siempre tiene solución única.", False, "Falso: puede no tener solución o tener infinitas (rango menor que $3$)."),
    ("Si $A\\mathbf{x}_p = \\mathbf{b}$, el conjunto solución de $A\\mathbf{x} = \\mathbf{b}$ es $\\mathbf{x}_p + \\ker A$.", True, "Verdadero: es el teorema de la estructura de las soluciones."),
    ("El conjunto solución de $A\\mathbf{x} = \\mathbf{b}$ con $\\mathbf{b} \\ne \\mathbf{0}$ es un subespacio.", False, "Falso: no contiene a $\\mathbf{0}$ (es un núcleo trasladado)."),
    ("$\\operatorname{rg}(A) = \\operatorname{rg}(A^T)$.", True, "Verdadero: el número de pivotes coincide con la dimensión del espacio fila y la del espacio columna."),
]


def f15_vf(r):
    e = r.sample(POOL_VF, 4)
    return Ejercicio(
        "K", 4, "Verdadero o falso (con justificación)", "decidir y justificar afirmaciones sobre sistemas, rango, núcleo y matrices.",
        "Di si cada afirmación es verdadera o falsa y justifícalo (con una demostración corta o un contraejemplo):\n\n" + "\n".join(f"{chr(97 + i)}) {x[0]}" for i, x in enumerate(e)),
        "\n\n".join(f"{chr(97 + i)}) {x[2]}" for i, x in enumerate(e)),
        ["Para decidir si es falsa, busca un contraejemplo pequeño ($2 \\times 2$)."], "Responder sin justificar o con un solo ejemplo para una afirmación verdadera general.",
    )


# ----------------------------------------------------------------------------- F16
def D(nivel, titulo, enunciado, solucion, pistas, objetivo=None):
    return Ejercicio("D", nivel, titulo, objetivo or titulo[0].lower() + titulo[1:] + ".", enunciado, solucion, pistas, "")


DEMOS = [
    D(3, "Un sistema lineal no tiene exactamente dos soluciones", "Prueba que un sistema lineal tiene $0$, $1$ o infinitas soluciones; en particular no puede tener exactamente dos.",
      "Si $\\mathbf{x}$ e $\\mathbf{y}$ son soluciones distintas, para cada $t \\in \\mathbb{R}$ el vector $\\mathbf{z}_t = \\mathbf{x} + t(\\mathbf{y} - \\mathbf{x})$ cumple $A\\mathbf{z}_t = A\\mathbf{x} + t(A\\mathbf{y} - A\\mathbf{x}) = \\mathbf{b} + t(\\mathbf{b} - \\mathbf{b}) = \\mathbf{b}$. Como los $\\mathbf{z}_t$ son todos distintos (porque $\\mathbf{y} \\ne \\mathbf{x}$), hay infinitas soluciones. $\\blacksquare$",
      ["Si hay dos soluciones, prueba que toda la recta que las une es solución."]),
    D(3, "El homogéneo es cerrado bajo suma y múltiplos", "Si $A\\mathbf{x} = \\mathbf{0}$ y $A\\mathbf{y} = \\mathbf{0}$, prueba que $A(\\mathbf{x} + \\mathbf{y}) = \\mathbf{0}$ y $A(c\\mathbf{x}) = \\mathbf{0}$.",
      "Por linealidad, $A(\\mathbf{x} + \\mathbf{y}) = A\\mathbf{x} + A\\mathbf{y} = \\mathbf{0} + \\mathbf{0} = \\mathbf{0}$ y $A(c\\mathbf{x}) = c\\,A\\mathbf{x} = c\\,\\mathbf{0} = \\mathbf{0}$. $\\blacksquare$",
      ["Usa que el producto matriz-vector es lineal."]),
    D(3, "Traspuesta de un producto", "Prueba que $(AB)^T = B^TA^T$.",
      "La entrada $(i, j)$ de $(AB)^T$ es la entrada $(j, i)$ de $AB$: $\\sum_k a_{jk}b_{ki}$. La entrada $(i, j)$ de $B^TA^T$ es $\\sum_k (B^T)_{ik}(A^T)_{kj} = \\sum_k b_{ki}a_{jk}$. Coinciden para todo $(i, j)$. $\\blacksquare$",
      ["Compara las entradas $(i, j)$ de los dos miembros."]),
    D(3, "Las operaciones elementales son reversibles", "Prueba que cada operación elemental por filas se deshace con otra operación elemental.",
      "$R_i \\leftrightarrow R_j$ se deshace repitiéndola. $R_i \\leftarrow cR_i$ ($c \\ne 0$) se deshace con $R_i \\leftarrow \\frac1c R_i$. $R_i \\leftarrow R_i + cR_j$ ($i \\ne j$) se deshace con $R_i \\leftarrow R_i - cR_j$, porque la fila $j$ no cambió. $\\blacksquare$",
      ["Para cada tipo, busca la operación inversa."]),
    D(3, "Homogéneo con más incógnitas que ecuaciones", "Prueba que un sistema homogéneo con $m < n$ tiene soluciones no triviales.",
      "El rango cumple $\\operatorname{rg}(A) \\le m < n$, así que al menos una columna no tiene pivote y hay una variable libre. Dando a esa variable el valor $1$ y a las otras libres el valor $0$, se obtiene una solución distinta de $\\mathbf{0}$. $\\blacksquare$",
      ["Cuenta pivotes y variables libres."]),
    D(4, "Las operaciones elementales conservan las soluciones", "Prueba que si $[A' \\mid \\mathbf{b}']$ se obtiene de $[A \\mid \\mathbf{b}]$ por operaciones elementales, ambos sistemas tienen las mismas soluciones.",
      "Basta una operación. Si $\\mathbf{x}$ resuelve el sistema original, cumple las ecuaciones $E_i$; la nueva ecuación es una combinación de ellas ($E_i + cE_j$, $cE_i$ o un intercambio) y $\\mathbf{x}$ la cumple. Recíprocamente, la operación es reversible (ejercicio anterior), así que las ecuaciones originales son combinación de las nuevas y toda solución del nuevo sistema resuelve el original. $\\blacksquare$",
      ["Prueba las dos inclusiones; usa la reversibilidad para la segunda."]),
    D(4, "$\\operatorname{rg}(A) \\le \\min(m, n)$", "Prueba que el rango de una matriz $m \\times n$ no supera $m$ ni $n$.",
      "El rango es el número de pivotes. Hay a lo sumo un pivote por fila, luego $\\le m$, y a lo sumo un pivote por columna, luego $\\le n$. $\\blacksquare$",
      ["Un pivote ocupa su fila y su columna."]),
    D(4, "Rango de la matriz aumentada", "Prueba que $\\operatorname{rg}(A) \\le \\operatorname{rg}[A \\mid \\mathbf{b}] \\le \\operatorname{rg}(A) + 1$.",
      "Al escalonar $[A \\mid \\mathbf{b}]$ se escalona $A$ con las mismas operaciones: los pivotes de $A$ son pivotes de $[A \\mid \\mathbf{b}]$, luego el primer rango es $\\le$ el segundo. La columna $\\mathbf{b}$ es una sola y añade a lo sumo un pivote (hay a lo sumo uno por columna). $\\blacksquare$",
      ["Piensa en los pivotes de las primeras $n$ columnas."]),
    D(4, "Producto de triangulares inferiores unitarias", "Prueba que el producto de dos matrices triangulares inferiores con unos en la diagonal es triangular inferior con unos en la diagonal.",
      "Si $L_1, L_2$ son triangulares inferiores, $(L_1L_2)_{ij} = \\sum_k (L_1)_{ik}(L_2)_{kj}$. Para $i < j$ cada sumando tiene $(L_1)_{ik} \\ne 0$ solo si $k \\le i$ y $(L_2)_{kj} \\ne 0$ solo si $k \\ge j$; como $i < j$ no hay $k$ posible: la entrada es $0$. Para $i = j$ solo sobrevive $k = i$: $(L_1)_{ii}(L_2)_{ii} = 1\\cdot 1 = 1$. $\\blacksquare$",
      ["Mira qué índices $k$ hacen no nulos los dos factores."]),
    D(4, "Núcleo trivial y columnas independientes", "Prueba que $\\ker A = \\{\\mathbf{0}\\}$ si y solo si las columnas de $A$ son linealmente independientes.",
      "$A\\mathbf{x} = x_1\\mathbf{a}_1 + \\dots + x_n\\mathbf{a}_n$. Entonces $\\ker A = \\{\\mathbf{0}\\}$ significa que la única combinación de columnas igual a $\\mathbf{0}$ es la trivial, que es la definición de independencia. $\\blacksquare$",
      ["Lee $A\\mathbf{x}$ por columnas."]),
    D(4, "El espacio columna y la existencia de solución", "Prueba que $\\operatorname{Col}(A)$ es un subespacio de $\\mathbb{R}^m$ y que $A\\mathbf{x} = \\mathbf{b}$ tiene solución si y solo si $\\mathbf{b} \\in \\operatorname{Col}(A)$.",
      "$\\operatorname{Col}(A) = \\{A\\mathbf{x}\\}$. Contiene a $\\mathbf{0} = A\\mathbf{0}$; si $\\mathbf{u} = A\\mathbf{x}$ y $\\mathbf{v} = A\\mathbf{y}$, entonces $\\mathbf{u} + \\mathbf{v} = A(\\mathbf{x} + \\mathbf{y})$ y $c\\mathbf{u} = A(c\\mathbf{x})$: es un subespacio de $\\mathbb{R}^m$. Que $A\\mathbf{x} = \\mathbf{b}$ tenga solución es, por definición, que $\\mathbf{b} = A\\mathbf{x}$ para algún $\\mathbf{x}$, es decir, $\\mathbf{b} \\in \\operatorname{Col}(A)$. $\\blacksquare$",
      ["Usa $\\operatorname{Col}(A) = \\{A\\mathbf{x}\\}$."]),
    D(4, "Solución única para todo $\\mathbf{b}$", "Sea $A$ cuadrada $n \\times n$ con $\\operatorname{rg}(A) = n$. Prueba que $A\\mathbf{x} = \\mathbf{b}$ tiene solución única para todo $\\mathbf{b}$.",
      "Con $\\operatorname{rg}(A) = n$ todas las filas y columnas tienen pivote: la reducida de $A$ es $I$. Entonces la reducida de $[A \\mid \\mathbf{b}]$ es $[I \\mid \\mathbf{c}]$, sin filas contradictorias y sin variables libres: hay una única solución $\\mathbf{x} = \\mathbf{c}$. $\\blacksquare$",
      ["Escribe la reducida de $[A \\mid \\mathbf{b}]$."]),
    D(4, "Diferencia de soluciones", "Prueba que si $\\mathbf{x}_1, \\mathbf{x}_2$ son soluciones de $A\\mathbf{x} = \\mathbf{b}$, entonces $\\mathbf{x}_1 - \\mathbf{x}_2 \\in \\ker A$; y que la solución es única si y solo si $\\ker A = \\{\\mathbf{0}\\}$ (cuando hay alguna).",
      "$A(\\mathbf{x}_1 - \\mathbf{x}_2) = \\mathbf{b} - \\mathbf{b} = \\mathbf{0}$. Si $\\ker A = \\{\\mathbf{0}\\}$, la diferencia es $\\mathbf{0}$ y hay una sola solución. Si hay $\\mathbf{n} \\ne \\mathbf{0}$ en $\\ker A$ y $\\mathbf{x}_p$ es solución, $\\mathbf{x}_p + \\mathbf{n}$ es otra solución distinta. $\\blacksquare$",
      ["Resta las dos ecuaciones."]),
    D(5, "Teorema de Rouché-Frobenius", "Prueba: $A\\mathbf{x} = \\mathbf{b}$ es compatible si y solo si $\\operatorname{rg}(A) = \\operatorname{rg}[A \\mid \\mathbf{b}]$; y en ese caso la solución es única si y solo si el rango es $n$.",
      "Se escalona $[A \\mid \\mathbf{b}]$. Los rangos son distintos exactamente cuando hay un pivote en la última columna, es decir, una fila $[0 \\dots 0 \\mid c]$ con $c \\ne 0$, que es la ecuación imposible $0 = c$: incompatible. Si los rangos coinciden, no hay tal fila y se resuelve hacia atrás: el sistema es compatible. Las variables libres son las $n - \\operatorname{rg}(A)$ columnas sin pivote; hay solución única si y solo si no hay libres, es decir, $\\operatorname{rg}(A) = n$. $\\blacksquare$",
      ["Fíjate en si hay un pivote en la columna de $\\mathbf{b}$."]),
    D(5, "Teorema del rango y la nulidad", "Prueba que $\\operatorname{rg}(A) + \\operatorname{nul}(A) = n$ para una matriz $m \\times n$.",
      "Sea $r$ el número de pivotes. Las $r$ columnas con pivote de la reducida son $\\mathbf{e}_1, \\dots, \\mathbf{e}_r$ y las demás son combinación de ellas; como $A$ y la reducida tienen las mismas relaciones entre columnas, las $r$ columnas pivote de $A$ son una base de $\\operatorname{Col}(A)$: $\\dim\\operatorname{Col}(A) = r$. Cada una de las $n - r$ variables libres aporta un vector a una base de $\\ker A$ (generan, y son independientes por los unos y ceros en las posiciones libres): $\\dim\\ker A = n - r$. Suman $n$. $\\blacksquare$",
      ["Cuenta columnas con y sin pivote."]),
    D(5, "Las columnas pivote son una base de $\\operatorname{Col}(A)$", "Prueba que las columnas de $A$ en las posiciones de los pivotes de su reducida $R$ son una base de $\\operatorname{Col}(A)$.",
      "Escribe $R = EA$ con $E$ invertible. Para cualquier $\\mathbf{x}$: $A\\mathbf{x} = \\mathbf{0} \\iff R\\mathbf{x} = \\mathbf{0}$, es decir, $A$ y $R$ tienen las mismas relaciones lineales entre sus columnas. En $R$, las columnas pivote ($\\mathbf{e}_1, \\dots, \\mathbf{e}_r$) son independientes y cada columna libre es combinación de ellas. Esas dos propiedades pasan a $A$: sus columnas pivote son independientes y generan las demás, luego generan $\\operatorname{Col}(A)$. $\\blacksquare$",
      ["Compara $\\ker A$ y $\\ker R$."]),
    D(5, "Un generador es mayor que un independiente", "Si $\\mathbf{v}_1, \\dots, \\mathbf{v}_k$ generan un subespacio $S$ y $\\mathbf{w}_1, \\dots, \\mathbf{w}_m \\in S$ son independientes, prueba que $m \\le k$.",
      "Cada $\\mathbf{w}_j$ es combinación de los $\\mathbf{v}_i$: $\\mathbf{w}_j = \\sum_i a_{ij}\\mathbf{v}_i$. Sea $B = (a_{ij})$, de tamaño $k \\times m$. Si $m > k$, el sistema homogéneo $B\\mathbf{c} = \\mathbf{0}$ tiene una solución $\\mathbf{c} \\ne \\mathbf{0}$ (más incógnitas que ecuaciones). Entonces $\\sum_j c_j\\mathbf{w}_j = \\sum_i \\big(\\sum_j a_{ij}c_j\\big)\\mathbf{v}_i = \\mathbf{0}$ con $\\mathbf{c} \\ne \\mathbf{0}$, contradiciendo la independencia. Luego $m \\le k$. $\\blacksquare$",
      ["Escribe cada $\\mathbf{w}_j$ con los $\\mathbf{v}_i$ y mira el sistema que resulta."]),
    D(5, "Todas las bases tienen el mismo número de vectores", "Prueba que dos bases de un mismo subespacio tienen el mismo número de vectores.",
      "Sean $\\{\\mathbf{v}_1, \\dots, \\mathbf{v}_k\\}$ y $\\{\\mathbf{w}_1, \\dots, \\mathbf{w}_m\\}$ bases de $S$. Los $\\mathbf{v}$ generan y los $\\mathbf{w}$ son independientes: $m \\le k$ (ejercicio anterior). Intercambiando los papeles, $k \\le m$. Luego $k = m$. $\\blacksquare$",
      ["Aplica el resultado anterior dos veces."]),
    D(5, "El rango por filas y por columnas coincide", "Prueba que $\\operatorname{rg}(A) = \\operatorname{rg}(A^T)$.",
      "Las operaciones por filas no cambian el espacio generado por las filas (cada fila nueva es combinación de las antiguas y, por reversibilidad, al revés). En la reducida, las $r$ filas no nulas son independientes (cada una tiene un $1$ en una columna pivote donde las demás tienen $0$): son una base del espacio fila, que tiene dimensión $r$. Pero $r$ es también $\\operatorname{rg}(A)$ (número de pivotes). Como el espacio fila de $A$ es el espacio columna de $A^T$, resulta $\\operatorname{rg}(A^T) = r = \\operatorname{rg}(A)$. $\\blacksquare$",
      ["Las operaciones por filas conservan el espacio fila."]),
    D(5, "Existencia para todo $\\mathbf{b}$", "Prueba que $A\\mathbf{x} = \\mathbf{b}$ tiene solución para todo $\\mathbf{b} \\in \\mathbb{R}^m$ si y solo si $\\operatorname{rg}(A) = m$.",
      "($\\Leftarrow$) Si $\\operatorname{rg}(A) = m$, la reducida de $A$ no tiene filas nulas, así que $[A \\mid \\mathbf{b}]$ nunca produce una fila $[0 \\dots 0 \\mid c]$ con $c \\ne 0$: es compatible. ($\\Rightarrow$) Si $\\operatorname{rg}(A) < m$, la reducida tiene una fila nula; deshaciendo las operaciones, existe $\\mathbf{b}$ cuyo sistema reducido tiene esa fila $[0 \\dots 0 \\mid 1]$ (basta tomar $\\mathbf{b} = E^{-1}\\mathbf{e}_m$), que es incompatible. $\\blacksquare$",
      ["Recuerda que existencia equivale a $\\operatorname{Col}(A) = \\mathbb{R}^m$, es decir, $\\dim\\operatorname{Col}(A) = m$."]),
    D(5, "Unicidad de $A = LU$", "Si $A$ es invertible y $A = L_1U_1 = L_2U_2$ con $L_i$ triangulares inferiores con unos en la diagonal y $U_i$ triangulares superiores, prueba que $L_1 = L_2$ y $U_1 = U_2$.",
      "Como $A$ es invertible, $L_i$ y $U_i$ también lo son (determinantes no nulos). De $L_1U_1 = L_2U_2$ se tiene $L_2^{-1}L_1 = U_2U_1^{-1}$. El miembro izquierdo es triangular inferior con unos en la diagonal (producto e inversa de matrices así); el derecho es triangular superior. Una matriz a la vez triangular inferior y superior es diagonal, y con unos en la diagonal es $I$. Luego $L_2^{-1}L_1 = I$, es decir, $L_1 = L_2$, y entonces $U_1 = U_2$. $\\blacksquare$",
      ["Despeja para que a un lado queden las $L$ y al otro las $U$."]),
    D(5, "Coste de la factorización $LU$", "Prueba que factorizar una matriz $n \\times n$ sin intercambios cuesta $\\frac{n^3 - n}{3}$ multiplicaciones y divisiones.",
      "En el paso $k$ ($k = 1, \\dots, n-1$) hay $n - k$ filas por debajo del pivote. Para cada una se calcula un multiplicador (1 división) y se actualizan $n - k$ entradas (1 multiplicación cada una): $(n - k)(n - k + 1)$ operaciones. Con $j = n - k$ recorriendo $1, \\dots, n - 1$: $\\sum_{j=1}^{n-1} j(j+1) = \\sum j^2 + \\sum j = \\frac{(n-1)n(2n-1)}{6} + \\frac{(n-1)n}{2} = \\frac{(n-1)n(n+1)}{3} = \\frac{n^3 - n}{3}$. $\\blacksquare$",
      ["Cuenta las operaciones de cada paso y suma con $\\sum j$ y $\\sum j^2$."]),
    D(5, "La reducida conserva las relaciones", "Si $R = EA$ con $E$ invertible, prueba que $\\ker R = \\ker A$ y que $\\operatorname{Col}(R)$ no tiene por qué ser igual a $\\operatorname{Col}(A)$.",
      "$R\\mathbf{x} = \\mathbf{0} \\iff EA\\mathbf{x} = \\mathbf{0} \\iff A\\mathbf{x} = \\mathbf{0}$ (multiplicando por $E^{-1}$ para la implicación inversa): los núcleos coinciden. Contraejemplo para el espacio columna: $A = \\begin{bmatrix} 1&1\\\\1&1 \\end{bmatrix}$ tiene $\\operatorname{Col}(A) = \\operatorname{gen}\\{(1,1)\\}$, pero su reducida $R = \\begin{bmatrix} 1&1\\\\0&0 \\end{bmatrix}$ tiene $\\operatorname{Col}(R) = \\operatorname{gen}\\{(1,0)\\}$. $\\blacksquare$",
      ["Multiplica por $E^{-1}$ para la implicación inversa."]),
    D(5, "Un sistema compatible determinado para un $\\mathbf{b}$ lo es para todos", "Sea $A$ cuadrada. Si $A\\mathbf{x} = \\mathbf{b}_0$ tiene solución única para algún $\\mathbf{b}_0$, prueba que $A\\mathbf{x} = \\mathbf{b}$ tiene solución única para todo $\\mathbf{b}$.",
      "Si $A\\mathbf{x} = \\mathbf{b}_0$ tiene solución única, por el ejercicio sobre la diferencia de soluciones $\\ker A = \\{\\mathbf{0}\\}$, es decir, $\\operatorname{nul}(A) = 0$ y por rango-nulidad $\\operatorname{rg}(A) = n$. Como $A$ es cuadrada, $\\operatorname{rg}(A) = n = m$ y por el ejercicio de existencia hay solución para todo $\\mathbf{b}$; es única porque el núcleo es trivial. $\\blacksquare$",
      ["Convierte la hipótesis en una afirmación sobre $\\ker A$ y usa rango-nulidad."]),
    D(5, "Coeficientes racionales, solución racional", "Prueba que un sistema con coeficientes racionales que tiene alguna solución real tiene también una solución racional.",
      "Al escalonar $[A \\mid \\mathbf{b}]$ solo se usan sumas, productos y cocientes de racionales, así que la forma reducida tiene entradas racionales y los mismos rangos. Si el sistema es compatible, poniendo las variables libres iguales a $0$ y leyendo las básicas en la última columna de la reducida se obtiene una solución cuyas componentes son racionales. $\\blacksquare$",
      ["¿Qué números aparecen al hacer eliminación?"]),
]

assert len(DEMOS) == 25


def hacer(e):
    return lambda r: e


PLAN = {
    "F15": [(f15_ficha, 8), (f15_mezcla, 2), (f15_trafico, 2), (f15_quimica, 2), (f15_interpolacion, 2), (f15_param_completo, 3), (f15_vf, 6), (f15_ficha, 5)],
    "F16": [(hacer(e), 1) for e in DEMOS],
}


def f15_ficha3(r):
    """Misma ficha con matrices 3x4 de rango 2 (nivel N3)."""
    e = f15_ficha(r, tam=(3, 4))
    e.nivel = 3
    e.titulo = "Ficha de una matriz 3×4"
    return e


def f15_vf5(r):
    e = f15_vf(r)
    e.nivel = 5
    return e


PLAN["F15"] = [(f15_ficha, 8), (f15_mezcla, 2), (f15_trafico, 2), (f15_quimica, 2), (f15_interpolacion, 2), (f15_param_completo, 3), (f15_vf, 4), (f15_vf5, 2), (f15_ficha3, 5)]
