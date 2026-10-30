"""Lección 19 — Producto de una matriz por un vector: dos miradas.

Escenas (un video cada una):
    FilaPorColumna, ComoCombinacionDeColumnas

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l19_matriz_por_vector.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, animar_productos, flecha, matriz  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A = [[1, 2, 0], [3, -1, 4]]
X = [[2], [1], [-1]]
AX = [[4], [1]]
COLORES_COLUMNAS = COLORES_ECUACIONES  # columna 1 azul, 2 naranja, 3 rosa


class FilaPorColumna(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 19 · Parte 1", "Matriz por vector: fila por columna")

        # Producto escalar.
        titulo = self.encabezado("Primero: fila por columna (producto escalar)")
        fila = matriz([[1, 2, 0]]).scale(1.1)
        columna = matriz(X).scale(1.1)
        grupo = VGroup(fila, MathTex(r"\cdot", font_size=60), columna).arrange(RIGHT, buff=0.4).shift(UP * 1.7)
        self.decir("Empecemos por multiplicar una fila por una columna.")
        self.play(FadeIn(grupo))
        pares = VGroup()
        for k, (ef, ec) in enumerate(zip(fila.get_entries(), columna.get_entries())):
            par = VGroup(SurroundingRectangle(ef, color=COLORES_COLUMNAS[k]), SurroundingRectangle(ec, color=COLORES_COLUMNAS[k]))
            pares.add(par)
        self.decir("Emparejamos primero con primero, segundo con segundo y tercero con tercero.")
        self.play(LaggedStart(*[Create(p) for p in pares], lag_ratio=0.5))
        cuenta = MathTex(r"1\cdot 2", "+", r"2\cdot 1", "+", r"0\cdot(-1)", "=", "4", font_size=50).next_to(grupo, DOWN, buff=0.5)
        for k, idx in enumerate((0, 2, 4)):
            cuenta[idx].set_color(COLORES_COLUMNAS[k])
        self.decir("Multiplicamos cada pareja y sumamos: uno por dos, más dos por uno, más cero por menos uno. Cuatro.")
        self.play(Write(cuenta), run_time=2)
        self.pie("Primero con primero, segundo con segundo, tercero con tercero; se multiplican y se suman.", espera=2)
        general = MathTex(r"\begin{bmatrix} a_1 & \cdots & a_n \end{bmatrix} \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} = a_1x_1 + \cdots + a_nx_n = \sum_{j=1}^{n} a_j x_j", font_size=40)
        general.next_to(cuenta, DOWN, buff=0.5)
        self.decir("El resultado es un solo número. Exige que la fila y la columna tengan la misma longitud. Y fíjate: es el lado izquierdo de una ecuación lineal.")
        self.play(Write(general))
        self.pie("Resultado: UN número. Exige que fila y columna tengan la misma longitud. ¡Es el lado izquierdo de una ecuación lineal!", espera=4)
        self.limpiar(titulo)

        # Matriz por vector.
        titulo = self.cambiar_encabezado(titulo, "Matriz por vector: cada fila por la columna")
        a = matriz(A)
        x = matriz(X)
        r = matriz(AX)
        producto = VGroup(a, x, MathTex("=", font_size=52), r).arrange(RIGHT, buff=0.35).shift(UP * 1.0)
        dims = VGroup(
            MathTex(r"2\times 3", font_size=34, color=COLOR_SECUNDARIO).next_to(a, DOWN),
            MathTex(r"3\times 1", font_size=34, color=COLOR_SECUNDARIO).next_to(x, DOWN),
            MathTex(r"2\times 1", font_size=34, color=COLOR_SECUNDARIO).next_to(r, DOWN),
        )
        self.decir("Para multiplicar una matriz por un vector, cada fila de la matriz se multiplica por el vector.")
        self.play(FadeIn(a), FadeIn(x), FadeIn(producto[2]), FadeIn(r.get_brackets()), FadeIn(dims[:2]))
        self.decir("La fila uno por equis da la primera componente: cuatro. La fila dos por equis, la segunda: seis menos uno menos cuatro, uno.")
        animar_productos(
            self,
            pares=[(a.get_rows()[i], x.get_columns()[0]) for i in range(2)],
            destinos=list(r.get_entries()),
            cuentas=[r"1\cdot 2 + 2\cdot 1 + 0\cdot(-1) = 4", r"3\cdot 2 + (-1)\cdot 1 + 4\cdot(-1) = 1"],
            posicion=DOWN * 1.6,
        )
        self.consolidar(r)
        self.decir("Una matriz de dos por tres, por un vector de tres componentes, da un vector de dos componentes.")
        self.play(FadeIn(dims[2]))
        self.pie("Fila 1 de A por x da la entrada 1 del resultado; fila 2 por x, la entrada 2.", espera=3)
        formula = MathTex(r"(A\mathbf{x})_i = \sum_{j=1}^{n} a_{ij}\,x_j", font_size=50, color=COLOR_PIVOTE).shift(DOWN * 1.6)
        self.decir("En general, la componente i de a equis es la fila i de a por equis.")
        self.play(Write(formula))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Cuándo se puede multiplicar?")
        regla = VGroup(
            MathTex(r"\underbrace{A}_{m\times n}\ \underbrace{\mathbf{x}}_{n\times 1} = \underbrace{A\mathbf{x}}_{m\times 1}", font_size=56),
            Tex(r"El número de \textbf{columnas} de $A$ debe ser igual al número de \textbf{componentes} de $\mathbf{x}$.", font_size=38),
            Tex(r"El resultado tiene tantas componentes como \textbf{filas} tiene $A$.", font_size=38),
            MathTex(r"\begin{bmatrix} 1 & 2 & 0 \\ 3 & -1 & 4 \end{bmatrix}\begin{bmatrix} 5 \\ 7 \end{bmatrix} \ \text{no está definido: la fila tiene 3 números y la columna 2}", font_size=36, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.55)
        ajustar_al_encuadre(regla)
        self.decir("El número de columnas de a debe coincidir con el número de componentes de equis, y el resultado tiene tantas componentes como filas tiene a. Si no coinciden, el producto no está definido.")
        for b in regla:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F06-N1-01",
            VGroup(
                Text("Calcula, si está definido:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \begin{bmatrix} 2 & -1 \\ 0 & 3 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 4 \\ 5 \end{bmatrix} \qquad"
                    r"\text{b) } \begin{bmatrix} 1 & 0 & 2 \end{bmatrix}\begin{bmatrix} 3 \\ -1 \\ 4 \end{bmatrix} \qquad"
                    r"\text{c) } \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}",
                    font_size=42,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Fila por columna: se multiplican posición a posición y se suma. Da un número.",
                "Ax: cada fila de A por x da una componente del resultado.",
                "(m × n)(n × 1) = m × 1: columnas de A = componentes de x.",
            ],
            "la segunda mirada: combinación de columnas.",
            voz="En resumen: fila por columna se multiplica posición a posición y se suma, y da un número. En a por equis, cada fila de a por equis da una componente del resultado. Y una matriz de eme por ene, por un vector de ene componentes, da un vector de eme componentes. Siguiente: la segunda mirada, combinación de columnas.",
        )


class ComoCombinacionDeColumnas(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 19 · Parte 2", "Matriz por vector: combinación de columnas")
        titulo = self.encabezado("Las componentes de x son pesos de las columnas")
        a = matriz(A, colores_columnas=COLORES_COLUMNAS)
        x = matriz(X, colores_columnas=[COLOR_PIVOTE])
        producto = VGroup(a, x).arrange(RIGHT, buff=0.3).to_edge(UP, buff=1.3)
        self.decir("Otra forma de ver el mismo producto.")
        self.play(FadeIn(producto))
        expansion = MathTex(
            "=", "2", r"\begin{bmatrix} 1 \\ 3 \end{bmatrix}", "+", "1", r"\begin{bmatrix} 2 \\ -1 \end{bmatrix}", "+", "(-1)", r"\begin{bmatrix} 0 \\ 4 \end{bmatrix}",
            font_size=46,
        ).next_to(producto, RIGHT, buff=0.3)
        for k, (peso, col) in enumerate(((1, 2), (4, 5), (7, 8))):
            expansion[peso].set_color(COLOR_PIVOTE)
            expansion[col].set_color(COLORES_COLUMNAS[k])
        VGroup(producto, expansion).set_x(0)
        self.decir("Las componentes de equis son pesos para las columnas de a: dos veces la primera columna, una vez la segunda, y menos una vez la tercera.")
        self.play(FadeIn(expansion[0]))
        for k, (peso, col) in enumerate(((1, 2), (4, 5), (7, 8))):
            self.play(
                TransformFromCopy(x.get_entries()[k], expansion[peso]),
                TransformFromCopy(a.get_columns()[k], expansion[col]),
                *([FadeIn(expansion[col - 2])] if k > 0 else []),
            )
        resultado = MathTex(
            r"= \begin{bmatrix} 2 \\ 6 \end{bmatrix} + \begin{bmatrix} 2 \\ -1 \end{bmatrix} + \begin{bmatrix} 0 \\ -4 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}", font_size=46
        ).next_to(expansion, DOWN, buff=0.5).align_to(expansion, LEFT)
        self.decir("El resultado es el mismo: cuatro, uno. A por equis es una combinación lineal de las columnas de a, con pesos equis uno, equis dos y equis tres.")
        self.play(Write(resultado))
        self.pie("¡El mismo resultado (4, 1)! Ax es una COMBINACIÓN LINEAL de las columnas de A con pesos x₁, x₂, x₃.", espera=4)
        self.limpiar(titulo)

        # Dibujo.
        titulo = self.cambiar_encabezado(titulo, "En el dibujo: encadenar las columnas")
        p = NumberPlane(x_range=[-1, 6, 1], y_range=[-1, 7, 1], x_length=4.9, y_length=5.6, background_line_style={"stroke_opacity": 0.3})
        p.to_edge(LEFT, buff=0.8).shift(DOWN * 0.4)
        self.decir("En el dibujo, encadenamos las columnas.")
        self.play(Create(p))
        pasos = [((0, 0), (2, 6), COLORES_COLUMNAS[0], r"2\cdot(1, 3)"), ((2, 6), (2, -1), COLORES_COLUMNAS[1], r"1\cdot(2, -1)"), ((4, 5), (0, -4), COLORES_COLUMNAS[2], r"(-1)\cdot(0, 4)")]
        leyenda = VGroup()
        self.decir("Dos veces la primera columna, el uno, tres. Luego una vez la segunda, el dos, menos uno. Y menos una vez la tercera, el cero, cuatro.")
        for desde, (dx, dy), color, tex in pasos:
            f = flecha(p, dx, dy, color, desde=desde)
            rot = MathTex(tex, font_size=38, color=color)
            leyenda.add(rot)
            rot.to_edge(RIGHT, buff=1.5).shift(UP * (2 - 0.8 * (len(leyenda) - 1)))
            self.play(GrowArrow(f), Write(rot))
            self.wait(0.8)
        total = flecha(p, 4, 1, COLOR_SOLUCION)
        rot_total = MathTex(r"A\mathbf{x} = (4, 1)", font_size=42, color=COLOR_SOLUCION).next_to(leyenda, DOWN, buff=0.6).align_to(leyenda, LEFT)
        self.decir("Cada columna estirada por su peso, una tras otra, nos lleva a a por equis.")
        self.play(GrowArrow(total), Write(rot_total))
        self.pie("Cada columna se estira según su peso y se colocan una tras otra: se llega a Ax.", espera=4)
        self.limpiar(titulo)

        # Las dos miradas.
        titulo = self.cambiar_encabezado(titulo, "Dos miradas, un mismo producto")
        filas = VGroup(
            Text("Por filas", font_size=TAM_TEXTO, weight="BOLD", color=COLOR_COEFICIENTE),
            MathTex(r"A\mathbf{x} = \begin{bmatrix} \text{fila}_1 \cdot \mathbf{x} \\ \text{fila}_2 \cdot \mathbf{x} \end{bmatrix}", font_size=44),
            Text("cada componente es un\nproducto escalar", font_size=TAM_NOTA, line_spacing=1.1),
        ).arrange(DOWN, buff=0.4)
        columnas = VGroup(
            Text("Por columnas", font_size=TAM_TEXTO, weight="BOLD", color=COLOR_TERMINO_INDEP),
            MathTex(r"A\mathbf{x} = x_1\,\mathbf{a}_1 + x_2\,\mathbf{a}_2 + x_3\,\mathbf{a}_3", font_size=44),
            Text("combinación lineal de las\ncolumnas a₁, a₂, a₃", font_size=TAM_NOTA, line_spacing=1.1),
        ).arrange(DOWN, buff=0.4)
        VGroup(filas, columnas).arrange(RIGHT, buff=1.4, aligned_edge=UP).shift(UP * 0.6)
        self.decir("Por filas, cada componente es un producto escalar.")
        self.play(FadeIn(filas))
        self.wait(1.5)
        self.decir("Por columnas, el resultado es una combinación lineal de las columnas.")
        self.play(FadeIn(columnas))
        porque = MathTex(
            r"(A\mathbf{x})_i = a_{i1}x_1 + a_{i2}x_2 + a_{i3}x_3 = x_1 a_{i1} + x_2 a_{i2} + x_3 a_{i3}",
            font_size=40,
        ).next_to(VGroup(filas, columnas), DOWN, buff=0.8)
        self.decir("Las dos son la misma suma, ordenada de otra manera. Por filas es más cómodo para calcular; por columnas, para entender.")
        self.play(Write(porque))
        self.pie(
            "Es la misma suma leída de dos formas: por filas sirve para CALCULAR;\n"
            "por columnas sirve para ENTENDER (Lecciones 21 y 48).",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F06-N2-01",
            VGroup(
                MathTex(r"A = \begin{bmatrix} 2 & -1 & 3 \\ 0 & 4 & 1 \end{bmatrix}, \qquad \mathbf{x} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}", font_size=46),
                Text("Calcula Ax por filas y por columnas, y comprueba que coinciden.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Ax = x₁·(columna 1) + x₂·(columna 2) + … : combinación lineal de las columnas.",
                "Por filas o por columnas se obtiene el mismo resultado.",
                "Filas para calcular; columnas para interpretar.",
            ],
            "Lección 20 — el producto de dos matrices.",
            voz="En resumen: a por equis es equis uno por la columna uno, más equis dos por la columna dos, y así: una combinación lineal de las columnas. Por filas o por columnas se obtiene el mismo resultado. Filas para calcular; columnas para interpretar. Siguiente: lección veinte, el producto de dos matrices.",
        )
