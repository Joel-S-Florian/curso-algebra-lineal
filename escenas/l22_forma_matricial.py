"""Lección 22 — De sistema a Ax = b.

Escenas (un video cada una):
    ConstruirAxb, AxReproduceLasEcuaciones

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l22_forma_matricial.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, animar_productos, matriz, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A = [[2, 1, -1], [1, -3, 2], [4, 0, 1]]
B = [[2], [0], [5]]
COEF = [COLOR_COEFICIENTE] * 3


def sistema_ordenado(font_size=44) -> VGroup:
    """El sistema de la lección con cada término en su columna: x, y, z alineadas."""
    filas = [
        ("2x", "+", "y", "-", "z", "=", "2"),
        ("x", "-", "3y", "+", "2z", "=", "0"),
        ("4x", "+", "0y", "+", "z", "=", "5"),
    ]
    tabla = VGroup(*[MathTex(t, font_size=font_size) for fila in filas for t in fila])
    tabla.arrange_in_grid(rows=3, cols=7, buff=(0.25, 0.35), col_alignments="rcrcrcl")
    return VGroup(Brace(tabla, LEFT), tabla)


class ConstruirAxb(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 22 · Parte 1", "De un sistema a la forma Ax = b")
        titulo = self.encabezado("Paso 0: ordenar el sistema")
        original = sistema_con_llave(("2x + y - z", "=", "2"), ("x - 3y + 2z", "=", "0"), ("z", "=", "5 - 4x"), font_size=44, colores=False)
        original.shift(LEFT * 3.5)
        self.decir("Para escribir un sistema en forma matricial, primero lo ordenamos.")
        self.play(Write(original))
        self.decir("Todas las incógnitas a la izquierda, en el mismo orden: equis, ye, zeta. Y los números a la derecha.")
        self.play(Indicate(original[1][2], color=COLOR_PIVOTE))
        self.pie("Todas las incógnitas a la izquierda, en el MISMO orden (x, y, z), y los números a la derecha.", espera=2)
        ordenado = sistema_ordenado().shift(RIGHT * 2.8)
        flecha = Arrow(original.get_right(), ordenado.get_left(), buff=0.4)
        self.decir("La tercera ecuación, zeta igual a cinco menos cuatro equis, pasa a cuatro equis más zeta igual a cinco.")
        self.play(GrowArrow(flecha), FadeIn(ordenado))
        tabla = ordenado[1]
        cero = tabla[14 + 2]
        self.decir("Y como no aparece ye, escribimos cero ye: su coeficiente es cero.")
        self.play(cero.animate.set_color(COLOR_PIVOTE), Indicate(cero, color=COLOR_PIVOTE))
        self.pie("z = 5 − 4x pasa a 4x + z = 5. Y como no aparece y, escribimos 0y: su coeficiente es 0.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Tres piezas: A, x y b")
        ordenado = sistema_ordenado(font_size=40).to_edge(LEFT, buff=0.8).shift(UP * 0.6)
        tabla = ordenado[1]
        self.decir("El sistema se separa en tres piezas.")
        self.play(FadeIn(ordenado))
        coeficientes = VGroup(*[tabla[7 * i + j] for i in range(3) for j in (0, 2, 4)])
        a = matriz([["2", "1", "-1"], ["1", "-3", "2"], ["4", "0", "1"]], colores_columnas=COEF)
        x = matriz([["x"], ["y"], ["z"]])
        b = matriz(B, colores_columnas=[COLOR_TERMINO_INDEP])
        piezas = VGroup(a, x, MathTex("=", font_size=52), b).arrange(RIGHT, buff=0.35).to_edge(RIGHT, buff=0.7).shift(UP * 0.6)
        self.decir("La matriz a recoge los coeficientes: cada ecuación en una fila, y cada incógnita en una columna, con su signo.")
        self.play(coeficientes.animate.set_color(COLOR_COEFICIENTE))
        self.pie("A: los coeficientes, cada ecuación en una fila y cada incógnita en una columna (¡con su signo!).", espera=1)
        self.play(FadeIn(a.get_brackets()), *[TransformFromCopy(c, e) for c, e in zip(coeficientes, a.get_entries())], run_time=2)
        self.consolidar(a)
        self.wait(1.5)
        self.decir("Equis es el vector de incógnitas, en el orden elegido.")
        self.pie("x: el vector de incógnitas, en el orden elegido.", espera=1)
        self.play(FadeIn(x))
        self.wait(1)
        terminos = VGroup(*[tabla[7 * i + 6] for i in range(3)])
        self.decir("Y be, el vector de términos independientes.")
        self.play(terminos.animate.set_color(COLOR_TERMINO_INDEP))
        self.pie("b: el vector de términos independientes.", espera=1)
        self.play(FadeIn(piezas[2]), FadeIn(b.get_brackets()), *[TransformFromCopy(t, e) for t, e in zip(terminos, b.get_entries())])
        self.consolidar(b)
        dims = VGroup(
            MathTex(r"3\times 3", font_size=32, color=COLOR_SECUNDARIO).next_to(a, DOWN),
            MathTex(r"3\times 1", font_size=32, color=COLOR_SECUNDARIO).next_to(x, DOWN),
            MathTex(r"3\times 1", font_size=32, color=COLOR_SECUNDARIO).next_to(b, DOWN),
        )
        self.decir("A es de tres por tres; equis y be, de tres por uno.")
        self.play(FadeIn(dims))
        compacto = MathTex(r"A\mathbf{x} = \mathbf{b}", font_size=72, color=COLOR_PIVOTE).next_to(VGroup(ordenado, piezas), DOWN, buff=0.9)
        self.decir("El sistema entero cabe en tres símbolos: a equis igual a be. Con eme ecuaciones y ene incógnitas, a es de eme por ene, equis tiene ene componentes y be tiene eme.")
        self.play(Write(compacto))
        self.pie("Un sistema de m ecuaciones y n incógnitas: A es m × n, x tiene n componentes y b tiene m.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes al construir A")
        errores = VGroup(
            Tex(r"Olvidar el 0 de una incógnita que no aparece (la fila quedaría con 2 números).", font_size=36),
            Tex(r"Perder el signo: el coeficiente de $-z$ es $-1$, no $1$.", font_size=36),
            Tex(r"Cambiar el orden de las incógnitas en una ecuación (la columna 2 debe ser siempre la de $y$).", font_size=36),
            Tex(r"No pasar antes todas las incógnitas a la izquierda.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes al construir a: olvidar el cero de una incógnita que no aparece; perder el signo, porque el coeficiente de menos zeta es menos uno; cambiar el orden de las incógnitas en una ecuación; y no pasar antes todas las incógnitas a la izquierda.")
        for e in errores:
            self.play(FadeIn(e, shift=RIGHT * 0.2))
            self.wait(1.8)

        self.ejercicio_propuesto(
            "F07-N1-01",
            VGroup(
                Text("Escribe A, x y b:", font_size=TAM_TEXTO),
                sistema_con_llave(("3x_1 - x_3", "=", "4"), ("x_2 + 2x_1", "=", "-1"), ("x_3", "=", "x_2 + 7"), font_size=44, colores=False),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Ordenar: incógnitas a la izquierda, siempre en el mismo orden.",
                "A = coeficientes (0 si falta una incógnita); x = incógnitas; b = términos independientes.",
                "Dimensiones: A es m × n, x es n × 1 y b es m × 1.",
            ],
            "por qué Ax reproduce el sistema.",
            voz="En resumen: primero se ordena el sistema, con las incógnitas a la izquierda, siempre en el mismo orden. A recoge los coeficientes, con un cero si falta una incógnita; equis, las incógnitas; y be, los términos independientes. A es de eme por ene, equis de ene por uno y be de eme por uno. Siguiente: por qué a equis reproduce el sistema.",
        )


class AxReproduceLasEcuaciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 22 · Parte 2", "¿Por qué Ax = b ES el sistema?")
        titulo = self.encabezado("Multipliquemos A por x")
        a = matriz([["2", "1", "-1"], ["1", "-3", "2"], ["4", "0", "1"]], colores_columnas=COEF)
        x = matriz([["x"], ["y"], ["z"]])
        r = matriz([["2x + y - z"], ["x - 3y + 2z"], ["4x + 0y + z"]])
        b = matriz(B, colores_columnas=[COLOR_TERMINO_INDEP])
        igual = MathTex("=", font_size=52)
        # Toda la fila se coloca desde el principio; igual y b aparecen más tarde.
        producto = VGroup(a, x, MathTex("=", font_size=52), r).arrange(RIGHT, buff=0.35)
        VGroup(producto, igual, b).arrange(RIGHT, buff=0.35).shift(UP * 1.0)
        self.decir("Multipliquemos a por el vector de incógnitas.")
        self.play(FadeIn(a), FadeIn(x), FadeIn(producto[2]), FadeIn(r.get_brackets()))
        self.decir("Cada fila de a por equis produce exactamente el lado izquierdo de una ecuación, término por término: dos equis más ye menos zeta; equis menos tres ye más dos zeta; cuatro equis más cero ye más zeta.")
        animar_productos(
            self,
            pares=[(a.get_rows()[i], x.get_columns()[0]) for i in range(3)],
            destinos=list(r.get_entries()),
            cuentas=[r"2\cdot x + 1\cdot y + (-1)\cdot z", r"1\cdot x + (-3)\cdot y + 2\cdot z", r"4\cdot x + 0\cdot y + 1\cdot z"],
            posicion=DOWN * 1.7,
            espera=1.2,
        )
        self.consolidar(r)
        self.pie("Cada fila de A por x es exactamente el lado izquierdo de una ecuación, término por término.", espera=3)
        self.decir("Igualamos ese vector a be.")
        self.play(FadeIn(igual), FadeIn(b))
        sistema = sistema_con_llave(("2x + y - z", "=", "2"), ("x - 3y + 2z", "=", "0"), ("4x + z", "=", "5"), font_size=40).shift(DOWN * 1.9)
        self.decir("Dos vectores son iguales si lo son componente a componente: a equis igual a be son las tres ecuaciones a la vez.")
        self.play(TransformFromCopy(VGroup(r, b), sistema), run_time=2)
        self.pie("Dos vectores son iguales si lo son componente a componente: Ax = b son las 3 ecuaciones a la vez.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La mirada por columnas")
        columnas = MathTex(
            "x", r"\begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix}", "+", "y", r"\begin{bmatrix} 1 \\ -3 \\ 0 \end{bmatrix}", "+", "z", r"\begin{bmatrix} -1 \\ 2 \\ 1 \end{bmatrix}",
            "=", r"\begin{bmatrix} 2 \\ 0 \\ 5 \end{bmatrix}", font_size=48,
        ).shift(UP * 0.8)
        for k, idx in enumerate((1, 4, 7)):
            columnas[idx].set_color(COLORES_ECUACIONES[k])
        columnas[9].set_color(COLOR_TERMINO_INDEP)
        self.decir("Por columnas: equis por la primera columna, más ye por la segunda, más zeta por la tercera, igual a be.")
        self.play(Write(columnas), run_time=2)
        lectura = Tex(r"Resolver $A\mathbf{x} = \mathbf{b}$ = encontrar los \textbf{pesos} $x, y, z$ que combinan\\ las columnas de $A$ para obtener $\mathbf{b}$ (Lección 17).", font_size=38)
        lectura.next_to(columnas, DOWN, buff=0.7)
        self.decir("Resolver el sistema es encontrar los pesos equis, ye, zeta que combinan las columnas de a para obtener be.")
        self.play(FadeIn(lectura))
        self.wait(4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Comprobar una solución es multiplicar")
        bloque = VGroup(
            MathTex(r"A\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 + 1 - 1 \\ 1 - 3 + 2 \\ 4 + 0 + 1 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \\ 5 \end{bmatrix} = \mathbf{b}\ \checkmark", font_size=44, color=COLOR_SOLUCION),
            MathTex(r"A\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \neq \mathbf{b}", font_size=44, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.7)
        self.decir("Y comprobar una solución es multiplicar: a por uno, uno, uno da dos, cero, cinco, que es be. En cambio, a por uno, cero, uno da uno, tres, cinco: no es be.")
        for x_ in bloque:
            self.play(Write(x_))
            self.wait(2.2)
        self.pie("(1, 1, 1) es solución; (1, 0, 1) no. Verificar es calcular Ax y compararlo con b.", espera=4)

        self.ejercicio_propuesto(
            "F07-N2-01",
            VGroup(
                MathTex(r"\begin{bmatrix} 1 & 2 \\ 3 & -1 \\ 0 & 4 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \\ 8 \end{bmatrix}", font_size=48),
                Tex(r"a) Escribe el sistema. \ b) ¿Cuántas ecuaciones e incógnitas tiene? \ c) ¿Es $(1, 2)$ solución?", font_size=38),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Fila i de A por x = lado izquierdo de la ecuación i.",
                "Ax = b es el sistema completo: una igualdad de vectores.",
                "Por columnas: b debe ser combinación de las columnas de A con pesos x.",
                "Verificar una solución = calcular Ax y comparar con b.",
            ],
            "Lección 23 — la matriz aumentada.",
            voz="En resumen: la fila i de a por equis es el lado izquierdo de la ecuación i. A equis igual a be es el sistema completo: una igualdad de vectores. Por columnas, be debe ser una combinación de las columnas de a con pesos equis. Y verificar una solución es calcular a equis y compararlo con be. Siguiente: lección veintitrés, la matriz aumentada.",
        )
