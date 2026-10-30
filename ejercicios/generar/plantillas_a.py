"""Plantillas de F01–F04 (ecuaciones lineales, varias incógnitas, sistemas y métodos elementales)."""

from fractions import Fraction as F

import sympy as sp

from algebra import (
    Ejercicio, M, aug, det, fila_vec, lin, mat, pasos_gauss, pasos_tex, resolver, rref, sistema, t, ts, vec,
)


def nz(r, lo, hi):
    return r.choice([v for v in range(lo, hi + 1) if v != 0])


def ecuacion(a, b, c, d=None) -> str:
    """a x + b = c (o a x + b = c x + d)."""
    izq = lin([a], ["x"]) + (f" + {t(b)}" if b > 0 else (f" - {t(-b)}" if b < 0 else ""))
    if d is None:
        return f"{izq} = {t(c)}"
    der = lin([c], ["x"]) + (f" + {t(d)}" if d > 0 else (f" - {t(-d)}" if d < 0 else ""))
    return f"{izq} = {der}"


# ----------------------------------------------------------------------------- F01
def f01_ax_b(r):
    x0, a, b = nz(r, -6, 6), nz(r, -7, 7), nz(r, -9, 9)
    if abs(a) == 1:
        a *= 2
    c = a * x0 + b
    return Ejercicio(
        "C", 1, "Una ecuación de primer grado", "despejar la incógnita en $ax + b = c$.",
        f"Resuelve ${ecuacion(a, b, c)}$ y comprueba la solución.",
        f"Se pasa $b$ al otro miembro: ${lin([a], ['x'])} = {t(c)} {'-' if b > 0 else '+'} {t(abs(b))} = {t(c - b)}$. Se divide por ${t(a)}$: $x = {t(F(c - b, a))}$.\n\n"
        f"Comprobación: ${ecuacion(a, b, c).split('=')[0].replace('x', '(' + t(x0) + ')')}= {t(a * x0 + b)}$, que coincide con ${t(c)}$.",
        ["Deja el término con $x$ solo en un miembro.", "Primero se suma o resta el término independiente; luego se divide por el coeficiente de $x$."],
        "Cambiar el signo de $b$ solo en un miembro, o dividir solo uno de los términos.",
    )


def f01_ax_b_cx_d(r):
    x0 = nz(r, -6, 6)
    a, c = nz(r, -6, 6), nz(r, -6, 6)
    while a == c:
        c = nz(r, -6, 6)
    b = nz(r, -8, 8)
    d = a * x0 + b - c * x0
    return Ejercicio(
        "C", 2, "Incógnita en los dos miembros", "reunir los términos con $x$ a un lado y los números al otro.",
        f"Resuelve ${ecuacion(a, b, c, d)}$.",
        f"Se reúnen las $x$ a la izquierda y los números a la derecha: ${lin([a - c], ['x'])} = {t(d - b)}$, es decir, $x = {t(F(d - b, a - c))}$.\n\n"
        f"Comprobación: izquierda $= {t(a * x0 + b)}$; derecha $= {t(c * x0 + d)}$.",
        ["Resta $" + lin([c], ['x']) + "$ en los dos miembros.", "Después pasa el término independiente de la izquierda a la derecha."],
        "Olvidar cambiar el signo de un término al pasarlo al otro miembro.",
    )


def f01_fracciones(r):
    x0 = nz(r, -5, 5)
    p, s = nz(r, -4, 4), nz(r, -4, 4)
    q, u = r.choice([2, 3, 4]), r.choice([3, 5, 6])
    w = F(x0 + p, q) + F(x0 - s, u)
    m = q * u // __import__("math").gcd(q, u)
    izq = f"\\frac{{x {'+' if p > 0 else '-'} {abs(p)}}}{{{q}}} + \\frac{{x {'+' if -s > 0 else '-'} {abs(s)}}}{{{u}}} = {t(w)}"
    return Ejercicio(
        "C", 3, "Ecuación con fracciones", "quitar denominadores multiplicando por el mínimo común múltiplo.",
        f"Resuelve ${izq}$.",
        f"El mínimo común múltiplo de {q} y {u} es {m}. Multiplicando por {m}: ${t(m // q)}(x {'+' if p > 0 else '-'} {abs(p)}) + {t(m // u)}(x {'+' if -s > 0 else '-'} {abs(s)}) = {t(w * m)}$. "
        f"Reduciendo, ${lin([F(m // q + m // u)], ['x'])} = {t(w * m - (m // q) * p + (m // u) * s)}$ y $x = {t(x0)}$.",
        [f"Multiplica los dos miembros por {m}.", "Recuerda repartir el factor entre los dos sumandos del paréntesis."],
        "Multiplicar solo la fracción y no el segundo miembro.",
    )


POOL_LINEALES = [
    ("2x + 3y = 5", True, "es de la forma $ax + by = c$"),
    ("xy = 4", False, "tiene el producto $xy$ de dos incógnitas"),
    ("x^2 + y = 1", False, "$x$ aparece al cuadrado"),
    ("3x - \\frac{y}{2} = 7", True, "$\\frac{y}{2} = \\frac12 y$ es un coeficiente por $y$"),
    ("\\sqrt{x} + y = 2", False, "$x$ aparece dentro de una raíz"),
    ("5 = 2x", True, "una incógnita con coeficiente $2$"),
    ("\\frac{x}{y} = 3", False, "una incógnita divide a otra"),
    ("0{,}5x + 0{,}25y = 1", True, "los coeficientes pueden ser decimales"),
    ("\\sin x + y = 0", False, "$x$ aparece dentro de una función no lineal"),
    ("x + y + z = 0", True, "tres incógnitas, grado 1, sin productos"),
    ("2^x = 8", False, "la incógnita está en un exponente"),
    ("\\frac{1}{x} + y = 3", False, "$x$ está en un denominador"),
]


def f01_identificar(r):
    elegidas = r.sample(POOL_LINEALES, 5)
    lista = "\n".join(f"{chr(97 + i)}) ${e[0]}$" for i, e in enumerate(elegidas))
    sol = "\n".join(f"{chr(97 + i)}) {'Lineal' if e[1] else 'No lineal'}: {e[2]}." for i, e in enumerate(elegidas))
    return Ejercicio(
        "K", 1, "¿Es lineal?", "reconocer cuándo una ecuación es lineal.",
        "Indica cuáles de estas ecuaciones son lineales en sus incógnitas:\n\n" + lista,
        sol,
        ["Una ecuación es lineal si cada término es un número o un número por una sola incógnita elevada a $1$."],
        "Creer que una ecuación con decimales o fracciones numéricas deja de ser lineal.",
    )


def f01_parametro(r, tipo=None):
    k0 = nz(r, -4, 4)
    m = nz(r, -4, 4)
    inf = r.choice([True, False]) if tipo is None else tipo == "inf"
    k1 = k0 if inf else k0 + nz(r, -2, 2)
    # (k - k0) x = m (k - k1)
    kk0 = f"k {'-' if k0 > 0 else '+'} {abs(k0)}"
    kk1 = f"k {'-' if k1 > 0 else '+'} {abs(k1)}"
    const = -m * k1
    izq = f"kx {'-' if k0 > 0 else '+'} {abs(k0)}x"
    der = lin([m], ["k"]) + (f" + {const}" if const > 0 else (f" - {-const}" if const < 0 else ""))
    if inf:
        sol = (f"Se agrupa: $({kk0})\\,x = {t(m)}({kk1})$. Si $k \\ne {k0}$ hay una única solución, $x = {t(m)}$. "
               f"Si $k = {k0}$ queda $0\\cdot x = 0$: infinitas soluciones (todo $x$ real sirve).")
    else:
        sol = (f"Se agrupa: $({kk0})\\,x = {t(m)}({kk1})$. Si $k \\ne {k0}$ hay una única solución, $x = \\dfrac{{{t(m)}({kk1})}}{{{kk0}}}$. "
               f"Si $k = {k0}$ queda $0\\cdot x = {t(m * (k0 - k1))} \\ne 0$: no tiene solución.")
    return Ejercicio(
        "C", 4, "Ecuación con un parámetro", "discutir el número de soluciones según el parámetro.",
        f"Discute según el valor de $k$ el número de soluciones de ${izq} = {der}$.",
        sol,
        ["Agrupa los términos con $x$ y saca factor común $x$.", "Mira para qué valor de $k$ se anula el coeficiente de $x$ y qué queda entonces."],
        f"Dividir por $k {'-' if k0 > 0 else '+'} {abs(k0)}$ sin estudiar antes el caso en que vale cero.",
    )


def f01_problema(r):
    forma = r.choice(["numero", "rectangulo", "compra"])
    if forma == "numero":
        p, q = r.choice([(2, 3), (3, 5), (2, 5), (4, 7)])
        x0 = nz(r, 3, 12)
        a = r.randint(1, (q - p) * x0 - 1)
        bprime = (q - p) * x0 - a
        enun = f"Hallar un número tal que {p} veces el número más {a} sea igual a {q} veces el número menos {bprime}."
        sol = (f"Sea $x$ el número: ${p}x + {a} = {q}x - {bprime}$. Entonces ${lin([q - p], ['x'])} = {a + bprime}$, luego $x = {t(F(a + bprime, q - p))}$. "
               f"Comprobación: ${p}\\cdot {x0} + {a} = {p * x0 + a}$ y ${q}\\cdot {x0} - {bprime} = {q * x0 - bprime}$.")
        return Ejercicio("C", 3, "Un número desconocido", "traducir un enunciado a una ecuación.", enun, sol,
                         ["Llama $x$ al número y escribe cada frase como una expresión."], "Leer «menos» al revés al escribir la ecuación.")
    if forma == "rectangulo":
        ancho = nz(r, 3, 15)
        d = nz(r, 2, 8)
        P = 2 * (ancho + ancho + d)
        enun = f"El largo de un rectángulo mide {d} cm más que su ancho y el perímetro es {P} cm. Halla sus dimensiones."
        sol = f"Con ancho $x$ y largo $x + {d}$: $2x + 2(x + {d}) = {P}$, es decir, $4x + {2 * d} = {P}$, $x = {t(F(P - 2 * d, 4))}$. Ancho {ancho} cm y largo {ancho + d} cm (perímetro $2({ancho} + {ancho + d}) = {P}$)."
        return Ejercicio("C", 3, "Perímetro de un rectángulo", "plantear una ecuación a partir de una figura.", enun, sol,
                         ["El perímetro es la suma de los cuatro lados."], "Olvidar que hay dos lados de cada medida.")
    n = nz(r, 2, 9)
    precio = nz(r, 3, 15)
    libro = nz(r, 10, 40)
    total = n * precio + libro
    enun = f"Ana compra cuadernos a ${precio} cada uno y un libro de ${libro}. En total paga ${total}. ¿Cuántos cuadernos compró?"
    sol = f"Con $x$ cuadernos: ${precio}x + {libro} = {total}$, luego ${precio}x = {total - libro}$ y $x = {n}$ cuadernos."
    return Ejercicio("C", 2, "Una compra", "traducir una situación a una ecuación lineal.", enun, sol,
                     ["Gasto total = precio de los cuadernos + precio del libro."], "Sumar el precio del libro a cada cuaderno.")


def f01_error(r):
    a, b, c, d = nz(r, 2, 5), nz(r, 1, 6), nz(r, 1, 4), nz(r, 1, 9)
    while a == c:
        c = nz(r, 1, 4)
    mal = F(d + b, a - c)
    bien = F(d + a * b, a - c)
    return Ejercicio(
        "K", 4, "Encuentra el error", "detectar una propiedad distributiva mal aplicada.",
        f"Un estudiante resuelve ${a}(x - {b}) = {c}x + {d}$ así: «${a}x - {b} = {c}x + {d}$, luego ${lin([a - c], ['x'])} = {d + b}$ y $x = {t(mal)}$». ¿Dónde está el error? Da la solución correcta.",
        f"El error está en el primer paso: el factor ${a}$ multiplica a todo el paréntesis, así que ${a}(x - {b}) = {a}x - {a * b}$ (no ${a}x - {b}$). "
        f"Lo correcto es ${a}x - {a * b} = {c}x + {d}$, luego ${lin([a - c], ['x'])} = {d + a * b}$ y $x = {t(bien)}$.\n\nComprobación: izquierda ${a}({t(bien)} - {b}) = {t(a * (bien - b))}$; derecha ${c}\\cdot {ts(bien)} + {d} = {t(c * bien + d)}$.",
        ["Revisa el primer paso, el de quitar el paréntesis."],
        "Repartir el factor solo sobre el primer término del paréntesis.",
    )


# ----------------------------------------------------------------------------- F02
def f02_puntos(r):
    a, b = nz(r, 1, 5), nz(r, -5, 5)
    x1, y1 = nz(r, -4, 4), nz(r, -4, 4)
    c = a * x1 + b * y1
    ptos = [(x1, y1), (x1 + b, y1 - a), (x1 + 1, y1), (0, F(c, b)) if c % b == 0 else (x1 - b, y1 + a)]
    ptos = [(F(p[0]), F(p[1])) for p in ptos]
    r.shuffle(ptos)
    filas = []
    for (p, q) in ptos:
        v = a * p + b * q
        filas.append(f"$({t(p)}, {t(q)})$: ${t(a)}\\cdot {ts(p)} + {ts(b)}\\cdot {ts(q)} = {t(v)}$ " + ("✓ es solución." if v == c else f"≠ {t(c)}: no es solución."))
    return Ejercicio(
        "C", 1, "¿Es solución?", "comprobar una solución sustituyendo.",
        f"¿Cuáles de estos puntos son solución de ${lin([a, b], ['x', 'y'])} = {c}$?\n\n" + ",  ".join(f"$({t(p)}, {t(q)})$" for p, q in ptos),
        "\n\n".join(filas),
        ["Sustituye $x$ e $y$ por las coordenadas y mira si sale el término independiente."], "Sustituir las coordenadas en el orden contrario.",
    )


def f02_recta(r):
    a, b = nz(r, 1, 6), nz(r, -6, 6)
    c = nz(r, 1, 4) * a * b if a * b != 0 else 6
    return Ejercicio(
        "C", 2, "Cortes, pendiente y solución general", "describir el conjunto de soluciones de una ecuación con dos incógnitas.",
        f"Para la ecuación ${lin([a, b], ['x', 'y'])} = {c}$: a) halla los cortes con los ejes; b) la pendiente; c) escribe todas las soluciones con un parámetro; d) da tres soluciones.",
        f"a) Con $y = 0$: $x = {t(F(c, a))}$, punto $({t(F(c, a))}, 0)$. Con $x = 0$: $y = {t(F(c, b))}$, punto $(0, {t(F(c, b))})$.\n\n"
        f"b) Despejando, $y = {t(F(-a, b))}x + {t(F(c, b))}$: pendiente ${t(F(-a, b))}$.\n\n"
        f"c) Con $x = s$ libre: $y = {t(F(c, b))} {'+' if -a / b > 0 else '-'} {t(abs(F(a, b)))}s$; las soluciones son $(s, {t(F(c, b))} {'+' if -a / b > 0 else '-'} {t(abs(F(a, b)))}s)$.\n\n"
        f"d) Por ejemplo, con $s = 0, 1, 2$: " + ", ".join(f"$({t(F(s))}, {t(F(c, b) - F(a, b) * s)})$" for s in (0, 1, 2)) + ".",
        ["Para el corte con el eje $x$ haz $y = 0$.", "Despeja $y$ para ver la pendiente."], "Confundir el signo de la pendiente al despejar.",
    )


def f02_plano(r):
    a, b, c3 = nz(r, 1, 4), nz(r, 1, 4), nz(r, 1, 4)
    d = a * b * c3 * nz(r, 1, 2)
    p = [F(d, a), F(d, b), F(d, c3)]
    return Ejercicio(
        "C", 2, "Un plano en el espacio", "hallar los cortes con los ejes y puntos de un plano.",
        f"Sea el plano ${lin([a, b, c3], ['x', 'y', 'z'])} = {d}$. Halla sus cortes con los tres ejes y comprueba que el punto $({t(p[0])}, 0, 0)$ le pertenece.",
        f"Con $y = z = 0$: $x = {t(p[0])}$. Con $x = z = 0$: $y = {t(p[1])}$. Con $x = y = 0$: $z = {t(p[2])}$. Los cortes son $({t(p[0])},0,0)$, $(0,{t(p[1])},0)$ y $(0,0,{t(p[2])})$.\n\n"
        f"Comprobación: ${a}\\cdot {ts(p[0])} + 0 + 0 = {t(a * p[0])} = {d}$.",
        ["En cada eje, las otras dos coordenadas valen cero."], "Dividir por un coeficiente equivocado.",
    )


def f02_k(r):
    a, p, q = nz(r, 1, 5), nz(r, -3, 3), nz(r, 1, 4)
    c = nz(r, -8, 8)
    k = F(c - a * p, q)
    return Ejercicio(
        "C", 3, "Un coeficiente desconocido", "usar un punto dado para hallar un coeficiente.",
        f"Halla $k$ para que el punto $({p}, {q})$ sea solución de ${lin([a], ['x'])} + ky = {c}$.",
        f"Sustituyendo: ${a}\\cdot {ts(p)} + k\\cdot {q} = {c}$, es decir, ${t(a * p)} + {q}k = {c}$; luego $k = {t(k)}$.",
        ["Sustituye $x = " + str(p) + "$ e $y = " + str(q) + "$ y despeja $k$."], "Sustituir solo una de las coordenadas.",
    )


POOL_PARAM = [
    ("una ecuación con 2 incógnitas", "1 parámetro libre", "una recta en el plano"),
    ("una ecuación con 3 incógnitas", "2 parámetros libres", "un plano en el espacio"),
    ("una ecuación con 4 incógnitas", "3 parámetros libres", "un «hiperplano» de dimensión 3 (no se puede dibujar)"),
    ("dos ecuaciones independientes con 3 incógnitas", "1 parámetro libre", "una recta en el espacio"),
    ("dos ecuaciones independientes con 4 incógnitas", "2 parámetros libres", "un plano dentro del espacio de 4 dimensiones"),
    ("tres ecuaciones independientes con 3 incógnitas", "0 parámetros libres", "un único punto"),
]


def f02_conceptual(r):
    elegidas = r.sample(POOL_PARAM, 3)
    return Ejercicio(
        "K", 3, "Parámetros libres y geometría", "relacionar incógnitas, ecuaciones independientes y dimensión del conjunto solución.",
        "Para cada caso indica cuántos parámetros libres tiene el conjunto solución y qué objeto geométrico es:\n\n" + "\n".join(f"{chr(97 + i)}) {e[0]}." for i, e in enumerate(elegidas)),
        "\n\n".join(f"{chr(97 + i)}) {e[1]}: {e[2]}." for i, e in enumerate(elegidas)) + "\n\nRegla: parámetros libres $=$ incógnitas $-$ ecuaciones independientes.",
        ["Cada ecuación independiente quita un grado de libertad."], "Contar ecuaciones que son combinación de otras.",
    )


def f02_dos_parametros(r):
    a, b, c3 = nz(r, 1, 3), nz(r, -3, 3), nz(r, -3, 3)
    d = nz(r, -6, 6)
    y0, z0 = nz(r, -2, 2), nz(r, -2, 2)
    x0 = F(d - b * y0 - c3 * z0, a)
    return Ejercicio(
        "C", 4, "Solución general con dos parámetros", "describir un plano con dos parámetros y hallar una solución concreta.",
        f"Escribe la solución general de ${lin([a, b, c3], ['x', 'y', 'z'])} = {d}$ con dos parámetros y halla la solución con $y = {y0}$, $z = {z0}$.",
        f"Con $y = s$, $z = u$ libres: $x = {t(F(d, a))} {'+' if -b / a > 0 else '-'} {'' if abs(F(b, a)) == 1 else t(abs(F(b, a)))}s {'+' if -c3 / a > 0 else '-'} {'' if abs(F(c3, a)) == 1 else t(abs(F(c3, a)))}u$. "
        f"Con $s = {y0}$, $u = {z0}$ sale $x = {t(x0)}$; la solución es $({t(x0)}, {y0}, {z0})$. Comprobación: ${a}\\cdot {ts(x0)} + {ts(b)}\\cdot {ts(y0)} + {ts(c3)}\\cdot {ts(z0)} = {t(a * x0 + b * y0 + c3 * z0)}$.",
        ["Despeja $x$ y deja $y$, $z$ libres."], "Dar solo un parámetro cuando hay dos libres.",
    )


# ----------------------------------------------------------------------------- F03
def sistema_con_solucion(r, n=2, lo=-4, hi=4, coef=(-4, 4)):
    for _ in range(200):
        A = [[F(r.randint(*coef)) for _ in range(n)] for _ in range(n)]
        if det(A) != 0 and all(any(v != 0 for v in f) for f in A):
            x0 = [F(nz(r, lo, hi)) if r.random() < 0.8 else F(0) for _ in range(n)]
            b = [sum(a * x for a, x in zip(f, x0)) for f in A]
            return A, b, x0
    raise RuntimeError


def f03_clasificar2x2(r):
    tipo = r.choice(["unico", "unico", "paralelas", "coincidentes"])
    if tipo == "unico":
        A, b, x0 = sistema_con_solucion(r, 2)
        sol = f"Las pendientes son distintas (el determinante ${t(det(A))}$ no es cero): las rectas se cortan en un punto. Resolviendo, $({t(x0[0])}, {t(x0[1])})$.\n\nComprobación: " + ", ".join(
            f"${ts(f[0])}\\cdot {ts(x0[0])} + {ts(f[1])}\\cdot {ts(x0[1])} = {t(bb)}$" for f, bb in zip(A, b))
        clas = "compatible determinado"
    else:
        a1, b1 = nz(r, 1, 4), nz(r, -4, 4)
        c1 = nz(r, -6, 6)
        m = nz(r, 2, 3)
        A = M([a1, b1], [m * a1, m * b1])
        if tipo == "paralelas":
            b = [F(c1), F(m * c1 + nz(r, 1, 4))]
            sol = f"La segunda fila de coeficientes es ${m}$ veces la primera, pero el término independiente no: ${t(b[1])} \\ne {m}\\cdot {c1}$. Rectas paralelas distintas: no hay solución (incompatible)."
            clas = "incompatible"
        else:
            b = [F(c1), F(m * c1)]
            sol = f"La segunda ecuación es ${m}$ veces la primera: son la misma recta. Infinitas soluciones, todos los puntos de ${lin(A[0], ['x', 'y'])} = {c1}$ (compatible indeterminado)."
            clas = "compatible indeterminado"
    return Ejercicio(
        "C", 2, "Clasifica y resuelve el sistema 2×2", "clasificar sin graficar y dar la posición de las rectas.",
        f"Sin dibujar, clasifica y, si procede, resuelve: ${sistema(A, b)}$. ¿Cómo son las rectas?",
        f"Clasificación: {clas}.\n\n" + sol,
        ["Compara las razones entre coeficientes de las dos ecuaciones."], "Decir «sin solución» cuando las rectas coinciden.",
    )


def f03_3x3(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    return Ejercicio(
        "C", 3, "Tres planos, un punto", "resolver un sistema 3×3 por eliminación y reconocer los tres planos que se cortan en un punto.",
        f"Resuelve ${sistema(A, b)}$ y di cómo se cortan los tres planos.",
        pasos_tex(A, b, False) + f"\nSustituyendo hacia atrás: $({t(x0[0])}, {t(x0[1])}, {t(x0[2])})$. Los tres planos se cortan en un único punto (compatible determinado).",
        ["Elimina $x$ de las ecuaciones 2 y 3 usando la primera."], "Equivocarse en el signo al restar filas.",
    )


POOL_K3 = [
    ("¿Pueden dos rectas del plano cortarse en exactamente dos puntos?", "No: dos rectas distintas se cortan como mucho en un punto; si comparten dos puntos, coinciden."),
    ("¿Puede un sistema lineal tener exactamente dos soluciones?", "No: si tiene dos soluciones distintas, tiene infinitas (cualquier punto de la recta que las une)."),
    ("Tres planos son paralelos dos a dos. ¿Cuántas soluciones tiene el sistema?", "Ninguna: no hay punto común a los tres."),
    ("¿Puede un sistema de 3 ecuaciones y 2 incógnitas tener solución única?", "Sí: por ejemplo $x = 1$, $y = 2$, $x + y = 3$ (tres rectas que pasan por un mismo punto)."),
    ("Un sistema homogéneo, ¿puede ser incompatible?", "No: $\\mathbf{0}$ siempre es solución."),
    ("Dos planos distintos y no paralelos en el espacio, ¿cómo se cortan?", "En una recta (un parámetro libre)."),
]


def f03_conceptual(r):
    e = r.sample(POOL_K3, 3)
    return Ejercicio(
        "K", 3, "Preguntas de geometría de sistemas", "razonar sobre el número de soluciones sin calcular.",
        "Responde y justifica:\n\n" + "\n".join(f"{chr(97 + i)}) {q}" for i, (q, _) in enumerate(e)),
        "\n\n".join(f"{chr(97 + i)}) {a}" for i, (_, a) in enumerate(e)),
        ["Piensa en la figura geométrica de cada ecuación."], "Responder por intuición sin un contraejemplo.",
    )


def f03_parametro(r):
    s = r.choice([2, 3, 4])
    c = r.choice([s, -s, s + 1])
    k = sp.symbols("k")
    Ak = sp.Matrix([[1, k], [k, s * s]])
    bk = sp.Matrix([1, c])
    gen = sp.simplify(Ak.LUsolve(bk))
    def clasif(kv):
        Av = M([1, kv], [kv, s * s])
        return resolver(Av, [F(1), F(c)])
    lineas = []
    for kv in (s, -s):
        res = clasif(kv)
        lineas.append(f"Si $k = {kv}$: " + {"SI": "incompatible (no hay solución)", "SCI": "infinitas soluciones", "SCD": "solución única"}[res[0]] + ".")
    return Ejercicio(
        "C", 4, "Sistema 2×2 con parámetro", "discutir un sistema con un parámetro usando el determinante.",
        f"Discute según $k$: $\\begin{{cases}} x + ky = 1 \\\\ kx + {s * s}y = {c} \\end{{cases}}$",
        f"El determinante de los coeficientes es $\\begin{{vmatrix}} 1 & k \\\\ k & {s * s} \\end{{vmatrix}} = {s * s} - k^2$, que se anula para $k = \\pm {s}$. Si $k \\ne \\pm {s}$ hay solución única "
        f"$(x, y) = ({sp.latex(sp.simplify(gen[0]))}, {sp.latex(sp.simplify(gen[1]))})$.\n\n" + "\n\n".join(lineas),
        ["Calcula el determinante y busca los valores que lo anulan.", "Para cada valor crítico, sustituye en el sistema y escalona."], "Olvidar estudiar los valores críticos por separado.",
    )


# ----------------------------------------------------------------------------- F04
def sistema_con_unitario(r):
    """2x2 con solución entera y un coeficiente 1 en la primera ecuación (para despejar fácil)."""
    while True:
        a1, b1 = r.choice([(1, nz(r, -4, 4)), (nz(r, -4, 4), 1)])
        a2, b2 = nz(r, -4, 4), nz(r, -4, 4)
        if a1 * b2 - a2 * b1 != 0:
            break
    x0, y0 = nz(r, -4, 4), nz(r, -4, 4)
    return M([a1, b1], [a2, b2]), [F(a1 * x0 + b1 * y0), F(a2 * x0 + b2 * y0)], [F(x0), F(y0)]


def f04_sustitucion(r):
    A, b, x0 = sistema_con_unitario(r)
    (a1, b1), (a2, b2) = A
    c1, c2 = b
    if a1 == 1:  # x = c1 - b1 y
        pas = (f"De la primera, $x = {t(c1)} {'-' if b1 > 0 else '+'} {t(abs(b1))}y$. Sustituyendo en la segunda: ${t(a2)}({t(c1)} {'-' if b1 > 0 else '+'} {t(abs(b1))}y) + {ts(b2)}y = {t(c2)}$, "
               f"es decir, ${lin([b2 - a2 * b1], ['y'])} = {t(c2 - a2 * c1)}$ y $y = {t(x0[1])}$. Entonces $x = {t(c1)} - {ts(b1)}\\cdot {ts(x0[1])} = {t(x0[0])}$.")
    else:  # y = c1 - a1 x
        pas = (f"De la primera, $y = {t(c1)} {'-' if a1 > 0 else '+'} {t(abs(a1))}x$. Sustituyendo en la segunda: ${t(a2)}x + {ts(b2)}({t(c1)} {'-' if a1 > 0 else '+'} {t(abs(a1))}x) = {t(c2)}$, "
               f"es decir, ${lin([a2 - b2 * a1], ['x'])} = {t(c2 - b2 * c1)}$ y $x = {t(x0[0])}$. Entonces $y = {t(c1)} - {ts(a1)}\\cdot {ts(x0[0])} = {t(x0[1])}$.")
    return Ejercicio(
        "C", 2, "Por sustitución", "aplicar el método de sustitución con un coeficiente unitario.",
        f"Resuelve por sustitución: ${sistema(A, b)}$.",
        pas + f"\n\nSolución: $({t(x0[0])}, {t(x0[1])})$.",
        ["Despeja la incógnita que tiene coeficiente $1$ en la primera ecuación."], "Olvidar poner paréntesis al sustituir una expresión con signo negativo.",
    )


def f04_igualacion(r):
    A, b, x0 = sistema_con_solucion(r, 2, coef=(-4, 4))
    (a1, b1), (a2, b2) = A
    c1, c2 = b
    if a1 == 0 or a2 == 0:
        return f04_igualacion(r)
    e1, e2 = lambda y: (c1 - b1 * y) / a1, lambda y: (c2 - b2 * y) / a2
    y0 = x0[1]
    return Ejercicio(
        "C", 2, "Por igualación", "despejar la misma incógnita en las dos ecuaciones e igualar.",
        f"Resuelve por igualación: ${sistema(A, b)}$.",
        f"Despejando $x$: $x = \\dfrac{{{t(c1)} - {ts(b1)}y}}{{{t(a1)}}}$ y $x = \\dfrac{{{t(c2)} - {ts(b2)}y}}{{{t(a2)}}}$. Igualando y multiplicando en cruz: ${t(a2)}({t(c1)} - {ts(b1)}y) = {t(a1)}({t(c2)} - {ts(b2)}y)$, "
        f"de donde ${lin([a1 * b2 - a2 * b1], ['y'])} = {t(a1 * c2 - a2 * c1)}$ y $y = {t(y0)}$. Entonces $x = {t(e1(y0))}$.\n\nComprobación: ${t(a2)}\\cdot {ts(x0[0])} + {ts(b2)}\\cdot {ts(y0)} = {t(c2)}$.",
        ["Despeja $x$ en las dos ecuaciones.", "Iguala las dos expresiones de $x$."], "No multiplicar todo el miembro al quitar denominadores.",
    )


def f04_reduccion(r):
    A, b, x0 = sistema_con_solucion(r, 2, coef=(-4, 4))
    while A[0][0] == 0 or A[1][0] == 0:
        A, b, x0 = sistema_con_solucion(r, 2, coef=(-4, 4))
    (a1, b1), (a2, b2) = A
    c1, c2 = b
    return Ejercicio(
        "C", 2, "Por reducción", "eliminar una incógnita combinando las ecuaciones.",
        f"Resuelve por reducción: ${sistema(A, b)}$.",
        f"Para eliminar $x$: se multiplica la primera por ${t(a2)}$ y la segunda por ${t(a1)}$ y se restan: $({t(a2)})\\cdot E_1 - ({t(a1)})\\cdot E_2$ da "
        f"${lin([a2 * b1 - a1 * b2], ['y'])} = {t(a2 * c1 - a1 * c2)}$, luego $y = {t(x0[1])}$. Sustituyendo en una ecuación: $x = {t(x0[0])}$.\n\nComprobación: ${t(a1)}\\cdot {ts(x0[0])} + {ts(b1)}\\cdot {ts(x0[1])} = {t(c1)}$.",
        ["Multiplica cada ecuación por el coeficiente de $x$ de la otra."], "Olvidar multiplicar el término independiente.",
    )


def f04_reduccion3x3(r):
    A, b, x0 = sistema_con_solucion(r, 3, coef=(-3, 3))
    return Ejercicio(
        "C", 3, "Reducción en un sistema 3×3", "eliminar incógnitas una a una en un sistema de tres ecuaciones.",
        f"Resuelve por reducción: ${sistema(A, b)}$.",
        pasos_tex(A, b, False) + f"\nSolución: $({t(x0[0])}, {t(x0[1])}, {t(x0[2])})$.",
        ["Elimina $x$ de la segunda y la tercera ecuaciones; después $y$ de la tercera."], "Perder una fila al copiar la matriz.",
    )


def f04_elegir(r):
    a, b = nz(r, 2, 6), nz(r, 2, 6)
    s1 = f"\\begin{{cases}} x + {a}y = {nz(r, 3, 9)} \\\\ {nz(r, 2, 5)}x - y = {nz(r, 1, 6)} \\end{{cases}}"
    s2 = f"\\begin{{cases}} {a}x + {b}y = {nz(r, 5, 20)} \\\\ {a}x - {b}y = {nz(r, 1, 9)} \\end{{cases}}"
    s3 = f"\\begin{{cases}} y = {a}x - {b} \\\\ y = -{nz(r, 1, 4)}x + {nz(r, 1, 9)} \\end{{cases}}"
    return Ejercicio(
        "K", 3, "Elige el método", "decidir qué método conviene según la forma del sistema.",
        f"Sin resolverlos, di qué método (sustitución, igualación o reducción) te parece más cómodo en cada sistema y por qué:\n\na) ${s1}$\n\nb) ${s2}$\n\nc) ${s3}$",
        "a) Sustitución: hay coeficientes $1$ ($x$ en la primera, $y$ en la segunda), fáciles de despejar sin fracciones.\n\n"
        "b) Reducción: los coeficientes de $x$ son iguales y los de $y$ son opuestos; sumando o restando se elimina una incógnita directamente.\n\n"
        "c) Igualación: ya están despejadas las dos $y$; basta igualar los segundos miembros.",
        ["Mira si alguna incógnita ya está despejada o tiene coeficiente $1$.", "Mira si hay coeficientes iguales u opuestos."], "Elegir un método que obliga a trabajar con fracciones sin necesidad.",
    )


# ----------------------------------------------------------------------------- registro
PLAN = {
    "F01": [(f01_ax_b, 5), (f01_ax_b_cx_d, 5), (f01_fracciones, 4), (f01_identificar, 4), (f01_parametro, 4), (f01_problema, 3), (f01_error, 2)],
    "F02": [(f02_puntos, 4), (f02_recta, 4), (f02_plano, 4), (f02_k, 3), (f02_conceptual, 3), (f02_dos_parametros, 2)],
    "F03": [(f03_clasificar2x2, 8), (f03_3x3, 5), (f03_conceptual, 4), (f03_parametro, 4)],
    "F04": [(f04_sustitucion, 8), (f04_igualacion, 7), (f04_reduccion, 8), (f04_reduccion3x3, 4), (f04_elegir, 4)],
}
