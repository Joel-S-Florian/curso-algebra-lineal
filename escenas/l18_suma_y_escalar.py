"""Lección 18 — Suma de matrices y producto por un escalar.

Escenas (un video cada una):
    SumaDeMatrices, ProductoPorEscalarYPropiedades

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l18_suma_y_escalar.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def ecuacion_matricial(*partes) -> VGroup:
    """Fila «A  +  B  =  C» con matrices y símbolos ya colocados."""
    return VGroup(*partes).arrange(RIGHT, buff=0.35)


class SumaDeMatrices(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 18 · Parte 1", "Suma de matrices")
        titulo = self.encabezado("Se suman las posiciones correspondientes")
        a = matriz([[1, -2, 3], [0, 4, -1]], h_buff=1.1)
        b = matriz([[2, 5, -3], [1, -4, 2]], h_buff=1.1)
        c = matriz([[3, 3, 0], [1, 0, 1]], h_buff=1.1)
        fila = ecuacion_matricial(a, MathTex("+", font_size=52), b, MathTex("=", font_size=52), c).shift(UP * 0.6)
        a.get_entries().set_color(COLOR_COEFICIENTE)
        b.get_entries().set_color(COLOR_TERMINO_INDEP)
        self.decir("Para sumar dos matrices, se suman los números que ocupan la misma posición.")
        self.play(FadeIn(a), FadeIn(fila[1]), FadeIn(b), FadeIn(fila[3]), FadeIn(c.get_brackets()))
        posicion_cuenta = DOWN * 1.6
        self.decir("Uno más dos, tres. Menos dos más cinco, tres. Tres más menos tres, cero. Y así con cada posición.")
        for k, (ea, eb, ec) in enumerate(zip(a.get_entries(), b.get_entries(), c.get_entries())):
            marcos = VGroup(SurroundingRectangle(ea, color=COLOR_PIVOTE, buff=0.08), SurroundingRectangle(eb, color=COLOR_PIVOTE, buff=0.08))
            cuenta = MathTex(ea.get_tex_string(), "+", f"({eb.get_tex_string()})", "=", ec.get_tex_string(), font_size=44).move_to(posicion_cuenta)
            rapido = k >= 2  # las dos primeras despacio; el resto más deprisa
            self.play(Create(marcos), FadeIn(cuenta), run_time=0.5 if rapido else 1)
            self.play(TransformFromCopy(cuenta[4], ec), FadeOut(marcos), FadeOut(cuenta), run_time=0.6 if rapido else 1.2)
        self.consolidar(c)
        formula = MathTex(r"(A + B)_{ij} = a_{ij} + b_{ij}", font_size=48, color=COLOR_PIVOTE).move_to(posicion_cuenta)
        self.decir("Cada elemento de a más be es la suma de los elementos de a y de be que ocupan esa misma posición.")
        self.play(Write(formula))
        self.pie("Cada elemento de A + B es la suma de los elementos de A y B que ocupan esa misma posición.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Solo con la misma dimensión")
        a = matriz([[1, -2, 3], [0, 4, -1]])
        d = matriz([[5, 2], [1, 0]])
        fila = ecuacion_matricial(a, MathTex("+", font_size=52), d, MathTex(r"= \ ?", font_size=52)).shift(UP * 0.6)
        dims = VGroup(MathTex(r"2\times 3", font_size=36).next_to(a, DOWN), MathTex(r"2\times 2", font_size=36).next_to(d, DOWN))
        self.decir("Pero si las matrices tienen distinta dimensión, como dos por tres y dos por dos…")
        self.play(FadeIn(fila), FadeIn(dims))
        sobra = SurroundingRectangle(a.get_columns()[2], color=COLOR_ERROR)
        self.decir("…algún número se queda sin pareja: la tercera columna de a no tiene con quién sumarse. La suma no está definida.")
        self.play(Create(sobra))
        self.pie("La tercera columna de A no tiene pareja en la otra matriz: la suma NO ESTÁ DEFINIDA.", COLOR_ERROR, espera=3)
        self.play(Create(Cross(fila[3], stroke_color=COLOR_ERROR)))
        self.wait(2)

        self.ejercicio_propuesto(
            "F05-N1-04",
            VGroup(
                MathTex(r"A = \begin{bmatrix} 4 & -1 \\ 0 & 2 \\ -3 & 5 \end{bmatrix}, \ B = \begin{bmatrix} -4 & 6 \\ 1 & 1 \\ 3 & -5 \end{bmatrix}, \ C = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}", font_size=42),
                Tex(r"Calcula $A + B$. ¿Está definida $A + C$? ¿Por qué?", font_size=40),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "A + B: se suman los elementos que ocupan la misma posición.",
                "Solo está definida si A y B tienen la misma dimensión.",
                "El resultado tiene esa misma dimensión.",
            ],
            "multiplicar una matriz por un número.",
            voz="En resumen: para sumar a y be, se suman los elementos que ocupan la misma posición. Solo está definida si a y be tienen la misma dimensión, y el resultado tiene esa misma dimensión. Siguiente: multiplicar una matriz por un número.",
        )


class ProductoPorEscalarYPropiedades(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 18 · Parte 2", "Producto por un escalar y propiedades")
        titulo = self.encabezado("Multiplicar cada elemento por el número")
        a = matriz([[1, -2, 3], [0, 4, -1]])
        r = matriz([[3, -6, 9], [0, 12, -3]])
        fila = ecuacion_matricial(MathTex("3", font_size=60, color=COLOR_PIVOTE), a, MathTex("=", font_size=52), r).shift(UP * 0.8)
        self.decir("Multiplicar una matriz por un número es multiplicar cada elemento por ese número: tres por uno, tres; tres por menos dos, menos seis; y así.")
        self.play(FadeIn(fila[:3]), FadeIn(r.get_brackets()))
        for ea, er in zip(a.get_entries(), r.get_entries()):
            self.play(TransformFromCopy(VGroup(fila[0], ea), er), run_time=0.6)
        self.consolidar(r)
        formula = MathTex(r"(cA)_{ij} = c\,a_{ij}", font_size=48, color=COLOR_PIVOTE).shift(DOWN * 0.8)
        self.decir("En general, el elemento i jota de ce por a es ce por a i jota.")
        self.play(Write(formula))
        self.wait(1.5)
        especiales = VGroup(
            MathTex(r"-A = (-1)A = \begin{bmatrix} -1 & 2 & -3 \\ 0 & -4 & 1 \end{bmatrix}", font_size=40),
            MathTex(r"A - B = A + (-1)B", font_size=40),
        ).arrange(RIGHT, buff=1.0).next_to(formula, DOWN, buff=0.6)
        self.decir("Con menos uno obtenemos la matriz opuesta.")
        self.play(FadeIn(especiales[0]))
        self.wait(1.5)
        self.decir("Y restar es sumar la opuesta, igual que con los números.")
        self.play(FadeIn(especiales[1]))
        self.pie("−A es la matriz opuesta: A + (−A) = O. Restar es sumar la opuesta, igual que con números.", espera=4)
        self.limpiar(titulo)

        # Propiedades.
        titulo = self.cambiar_encabezado(titulo, "Propiedades (A, B, C de la misma dimensión; c, d números)")
        props = [
            (r"A + B = B + A", "conmutativa"),
            (r"(A + B) + C = A + (B + C)", "asociativa"),
            (r"A + O = A, \qquad A + (-A) = O", "neutro y opuesto"),
            (r"c(A + B) = cA + cB, \qquad (c + d)A = cA + dA", "distributivas"),
            (r"c(dA) = (cd)A, \qquad 1A = A", ""),
        ]
        tabla = VGroup()
        for formula, nombre in props:
            tabla.add(MathTex(formula, font_size=40), Text(nombre, font_size=TAM_NOTA, color=COLOR_SECUNDARIO))
        tabla.arrange_in_grid(rows=len(props), cols=2, buff=(0.9, 0.35), col_alignments="ll")
        ajustar_al_encuadre(tabla)
        self.decir("Estas operaciones cumplen las mismas propiedades que los números: conmutativa, asociativa, neutro y opuesto, y las distributivas. Es así porque se hacen posición a posición.")
        for i in range(len(props)):
            self.play(FadeIn(tabla[2 * i]), FadeIn(tabla[2 * i + 1]))
            self.wait(1.2)
        self.pie("Son las propiedades de los números reales (Lección 1), aplicadas posición a posición.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Demostración de la conmutativa")
        prueba = VGroup(
            MathTex(r"(A + B)_{ij} = a_{ij} + b_{ij}", font_size=48),
            MathTex(r"= b_{ij} + a_{ij}", font_size=48),
            MathTex(r"= (B + A)_{ij}", font_size=48),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(LEFT * 1.5)
        razones = VGroup(
            Text("definición de suma", font_size=TAM_NOTA, color=COLOR_OPERACION),
            Text("conmutativa de los números reales", font_size=TAM_NOTA, color=COLOR_OPERACION),
            Text("definición de suma", font_size=TAM_NOTA, color=COLOR_OPERACION),
        )
        self.decir("Para demostrar la conmutativa miramos una posición cualquiera, i jota. Por la definición de suma, es a i jota más be i jota. Por la conmutativa de los números reales, es be i jota más a i jota. Y eso es el elemento i jota de be más a.")
        for linea, razon in zip(prueba, razones):
            razon.next_to(linea, RIGHT, buff=0.8)
            self.play(Write(linea), FadeIn(razon))
            self.wait(1.5)
        cierre = Tex(r"Para \textbf{todas} las posiciones $(i, j)$: $A + B = B + A$. \quad $\blacksquare$", font_size=40, color=COLOR_SOLUCION)
        cierre.next_to(prueba, DOWN, buff=0.8).set_x(0)
        self.decir("Como vale en todas las posiciones, las dos matrices son iguales. Así se demuestran todas las propiedades.")
        self.play(FadeIn(cierre))
        self.pie("Así se demuestran todas: se comprueba la igualdad en una posición cualquiera (i, j).", espera=4)

        self.ejercicio_propuesto(
            "F05-N2-02",
            VGroup(
                MathTex(r"A = \begin{bmatrix} 2 & 0 \\ -1 & 3 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & -4 \\ 5 & 2 \end{bmatrix}", font_size=46),
                MathTex(r"\text{a) } 2A - 3B \qquad \text{b) Halla } X \text{ tal que } A + 2X = B", font_size=42),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "cA: se multiplica cada elemento por c.",
                "−A es la opuesta; A − B = A + (−1)B.",
                "Suma y producto por escalar cumplen las propiedades de los números,\nporque se calculan posición a posición.",
            ],
            "Lección 19 — multiplicar una matriz por un vector.",
            voz="En resumen: ce por a multiplica cada elemento por ce. Menos a es la opuesta, y a menos be es a más menos uno por be. La suma y el producto por un escalar cumplen las propiedades de los números, porque se calculan posición a posición. Siguiente: lección diecinueve, multiplicar una matriz por un vector.",
        )
