"""Lección 20 — Producto de matrices.

Escenas (un video cada una):
    DimensionesYProcedimiento, NoConmutatividadEIdentidad

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l20_producto_matricial.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, animar_productos, matriz  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A = [[1, 2, 0], [-1, 3, 1]]
B = [[2, 1], [0, -1], [4, 2]]
AB = [[2, -1], [2, -2]]


class DimensionesYProcedimiento(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 20 · Parte 1", "El producto de dos matrices")

        titulo = self.encabezado("¿Cuándo se pueden multiplicar?")
        dims = MathTex("(", "m", r"\times", "n", ")", r"\,", "(", "n", r"\times", "p", ")", "=", "m", r"\times", "p", font_size=72).shift(UP * 0.8)
        self.decir("¿Cuándo se pueden multiplicar dos matrices? Una de eme por ene, y otra de ene por pe.")
        self.play(Write(dims[:11]))
        interior = VGroup(dims[3], dims[7])
        exterior = VGroup(dims[1], dims[9])
        self.decir("Los números de dentro deben coincidir: las columnas de la primera, con las filas de la segunda.")
        self.play(interior.animate.set_color(COLOR_PIVOTE), Indicate(interior, color=COLOR_PIVOTE))
        self.pie("Los números «de dentro» deben coincidir: columnas de A = filas de B.", espera=2)
        self.decir("Los de fuera dan la dimensión del resultado: filas de la primera por columnas de la segunda.")
        self.play(exterior.animate.set_color(COLOR_SOLUCION))
        self.play(TransformFromCopy(dims[1], dims[12]), TransformFromCopy(dims[9], dims[14]), FadeIn(dims[11]), FadeIn(dims[13]))
        self.pie("Los «de fuera» dan la dimensión del resultado: filas de A por columnas de B.", espera=3)
        ejemplos = VGroup(
            MathTex(r"(2\times 3)(3\times 2) = 2\times 2", font_size=44, color=COLOR_SOLUCION),
            MathTex(r"(3\times 2)(2\times 3) = 3\times 3", font_size=44, color=COLOR_SOLUCION),
            MathTex(r"(2\times 3)(2\times 3):\ \text{no definido}", font_size=44, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.4).next_to(dims, DOWN, buff=0.8)
        self.decir("Dos por tres, por tres por dos, da dos por dos. Tres por dos, por dos por tres, da tres por tres. Y dos por tres, por dos por tres, no está definido.")
        for e in ejemplos:
            self.play(FadeIn(e))
            self.wait(1.3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Elemento (i, j) = fila i de A por columna j de B")
        a, b = matriz(A), matriz(B)
        c = matriz(AB)
        producto = VGroup(a, b, MathTex("=", font_size=52), c).arrange(RIGHT, buff=0.35).shift(UP * 0.9)
        self.decir("¿Cómo se calcula?")
        self.play(FadeIn(a), FadeIn(b), FadeIn(producto[2]), FadeIn(c.get_brackets()))
        filas, cols = a.get_rows(), b.get_columns()
        destinos = c.get_rows()
        self.decir("El elemento i jota del producto es la fila i de a por la columna jota de be. Así, entrada a entrada.")
        animar_productos(
            self,
            pares=[(filas[0], cols[0]), (filas[0], cols[1]), (filas[1], cols[0]), (filas[1], cols[1])],
            destinos=[destinos[0][0], destinos[0][1], destinos[1][0], destinos[1][1]],
            cuentas=[
                r"c_{11} = 1\cdot 2 + 2\cdot 0 + 0\cdot 4 = 2",
                r"c_{12} = 1\cdot 1 + 2\cdot(-1) + 0\cdot 2 = -1",
                r"c_{21} = (-1)\cdot 2 + 3\cdot 0 + 1\cdot 4 = 2",
                r"c_{22} = (-1)\cdot 1 + 3\cdot(-1) + 1\cdot 2 = -2",
            ],
            posicion=DOWN * 1.5,
            espera=1.2,
        )
        self.consolidar(c)
        formula = MathTex(r"(AB)_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj}", font_size=50, color=COLOR_PIVOTE).shift(DOWN * 1.5)
        self.decir("En fórmula: la suma de a i ka por be ka jota.")
        self.play(Write(formula))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Otra forma de verlo: columna a columna")
        bloque = VGroup(
            MathTex(r"AB = A\begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 \end{bmatrix} = \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 \end{bmatrix}", font_size=50),
            MathTex(r"A\begin{bmatrix} 2 \\ 0 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}, \qquad A\begin{bmatrix} 1 \\ -1 \\ 2 \end{bmatrix} = \begin{bmatrix} -1 \\ -2 \end{bmatrix}", font_size=44),
            Tex(r"Cada columna de $AB$ es $A$ por la columna correspondiente de $B$ (Lección 19).", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.7)
        self.decir("Otra forma de verlo: cada columna del producto es a por la columna correspondiente de be, como en la lección diecinueve.")
        for x in bloque:
            self.play(FadeIn(x))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F06-N2-02",
            VGroup(
                MathTex(r"A = \begin{bmatrix} 1 & -1 \\ 2 & 0 \\ 3 & 1 \end{bmatrix}, \qquad B = \begin{bmatrix} 2 & 1 & 0 \\ -1 & 4 & 2 \end{bmatrix}", font_size=46),
                Tex(r"Indica la dimensión de $AB$ y de $BA$, y calcula ambos productos.", font_size=40),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "(m × n)(n × p) = m × p: columnas de A = filas de B.",
                "(AB)_ij = fila i de A por columna j de B.",
                "Columna j de AB = A · (columna j de B).",
            ],
            "propiedades: lo que cambia respecto de los números.",
            voz="En resumen: una matriz de eme por ene, por otra de ene por pe, da una de eme por pe: las columnas de la primera deben coincidir con las filas de la segunda. El elemento i jota del producto es la fila i de a por la columna jota de be. Y la columna jota de a be es a por la columna jota de be. Siguiente: propiedades, lo que cambia respecto de los números.",
        )


class NoConmutatividadEIdentidad(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 20 · Parte 2", "AB y BA: el orden importa")
        titulo = self.encabezado("En general, AB y BA son distintas")
        a = MathTex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}", font_size=48)
        b = MathTex(r"B = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}", font_size=48)
        VGroup(a, b).arrange(RIGHT, buff=1.5).shift(UP * 1.6)
        self.decir("Tomemos estas dos matrices, a y be.")
        self.play(FadeIn(a), FadeIn(b))
        productos = VGroup(
            MathTex(r"AB = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}", font_size=48, color=COLOR_COEFICIENTE),
            MathTex(r"BA = \begin{bmatrix} 1 & 1 \\ 1 & 2 \end{bmatrix}", font_size=48, color=COLOR_TERMINO_INDEP),
        ).arrange(RIGHT, buff=1.5).next_to(VGroup(a, b), DOWN, buff=0.8)
        self.decir("A por be da dos, uno; uno, uno.")
        self.play(Write(productos[0]))
        self.wait(1)
        self.decir("Pero be por a da uno, uno; uno, dos. Mismas matrices, distinto orden, distinto resultado: el producto de matrices no es conmutativo.")
        self.play(Write(productos[1]))
        self.pie("Mismas matrices, distinto orden, distinto resultado. El producto de matrices NO es conmutativo.", espera=3)
        dims = Tex(r"Y a veces ni siquiera tienen la misma dimensión: $(2\times 3)(3\times 2)$ es $2\times 2$, pero $(3\times 2)(2\times 3)$ es $3\times 3$.", font_size=34)
        dims.next_to(productos, DOWN, buff=0.7)
        self.decir("Y a veces ni siquiera tienen la misma dimensión: dos por tres, por tres por dos, da dos por dos; pero en el otro orden, da tres por tres.")
        self.play(FadeIn(dims))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que sí se cumple")
        props = [
            (r"(AB)C = A(BC)", "asociativa"),
            (r"A(B + C) = AB + AC, \quad (A + B)C = AC + BC", "distributivas"),
            (r"c(AB) = (cA)B = A(cB)", "escalares"),
            (r"I_m A = A = A\,I_n \quad (A \text{ de } m\times n)", "la identidad es neutra"),
        ]
        tabla = VGroup()
        for f, n in props:
            tabla.add(MathTex(f, font_size=42), Text(n, font_size=TAM_NOTA, color=COLOR_SECUNDARIO))
        tabla.arrange_in_grid(rows=len(props), cols=2, buff=(0.9, 0.45), col_alignments="ll")
        ajustar_al_encuadre(tabla)
        self.decir("Pero sí se cumplen otras propiedades: la asociativa, las distributivas, la de los escalares, y la identidad hace el papel del uno.")
        for i in range(len(props)):
            self.play(FadeIn(tabla[2 * i]), FadeIn(tabla[2 * i + 1]))
            self.wait(1.5)
        self.pie("(Siempre que las dimensiones permitan hacer los productos.)", espera=2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La identidad, en acción")
        i2 = matriz([[1, 0], [0, 1]], colores_columnas=[COLOR_PIVOTE, COLOR_PIVOTE])
        m = matriz([[3, -2], [5, 7]])
        r = matriz([[3, -2], [5, 7]])
        fila = VGroup(i2, m, MathTex("=", font_size=52), r).arrange(RIGHT, buff=0.35).shift(UP * 0.6)
        self.decir("Veamos la identidad en acción.")
        self.play(FadeIn(i2), FadeIn(m), FadeIn(fila[2]), FadeIn(r.get_brackets()))
        self.decir("Los ceros de la identidad anulan todos los términos menos uno: tres, menos dos; cinco, siete.")
        animar_productos(
            self,
            pares=[(i2.get_rows()[0], m.get_columns()[0]), (i2.get_rows()[1], m.get_columns()[1])],
            destinos=[r.get_rows()[0][0], r.get_rows()[1][1]],
            cuentas=[r"1\cdot 3 + 0\cdot 5 = 3", r"0\cdot(-2) + 1\cdot 7 = 7"],
            posicion=DOWN * 1.5,
            espera=1,
        )
        self.play(FadeIn(r.get_rows()[0][1]), FadeIn(r.get_rows()[1][0]))
        self.consolidar(r)
        self.decir("Cada fila queda igual: la identidad hace el papel del uno.")
        self.pie("Los ceros de I anulan todo menos un término: cada fila queda igual. I hace el papel del 1.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cuidado: dos errores frecuentes")
        bloque = VGroup(
            MathTex(r"\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}", font_size=46),
            Tex(r"$AB = O$ \textbf{no} implica $A = O$ o $B = O$ (con números sí: $ab = 0 \Rightarrow a = 0$ o $b = 0$).", font_size=36, color=COLOR_ERROR),
            Tex(r"$(AB)_{ij} \neq a_{ij}\,b_{ij}$: no se multiplica posición a posición.", font_size=36, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.6)
        self.decir("Cuidado con dos errores frecuentes. Un producto puede ser la matriz nula sin que ningún factor lo sea. Y el producto no se hace posición a posición.")
        for x in bloque:
            self.play(FadeIn(x))
            self.wait(2.4)
        self.decir("Por eso, con matrices, no se puede simplificar como con números: a be igual a a ce no implica be igual a ce.")
        self.pie("Por eso, con matrices, no se puede «simplificar» como con números: AB = AC no implica B = C.", espera=4)

        self.ejercicio_propuesto(
            "F06-N3-01",
            VGroup(
                MathTex(r"A = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}, \qquad B = \begin{bmatrix} 1 & 4 \\ 0 & -1 \end{bmatrix}", font_size=46),
                Tex(r"Calcula $AB$, $BA$ y $AI_2$. ¿Es $AB = BA$? ¿Es $(A + B)^2 = A^2 + 2AB + B^2$?", font_size=38),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "En general AB y BA son distintas: el orden importa.",
                "Asociativa y distributivas sí se cumplen; I es el neutro.",
                "AB = O no implica A = O ni B = O.",
            ],
            "Lección 21 — la matriz como transformación del plano.",
            voz="En resumen: en general, a be y be a son distintas: el orden importa. La asociativa y las distributivas sí se cumplen, y la identidad es el neutro. Y a be igual a cero no implica que a o be sean cero. Siguiente: lección veintiuno, la matriz como transformación del plano.",
        )
