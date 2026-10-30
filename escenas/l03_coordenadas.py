"""Lección 3 — Coordenadas: la recta, el plano y el espacio.

Escenas (un video cada una):
    ParesOrdenados, GraficaComoConjuntoDePuntos, PendienteDeUnaRecta, EspacioTresCoordenadas

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l03_coordenadas.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, recta_recortada  # noqa: E402
from curso.componentes import ejes_iguales as ejes  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def decimal(v: float) -> str:
    return f"{v:.1f}".replace("-0.0", "0.0")  # evita mostrar "-0.0"


class ParesOrdenados(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 3 · Parte 1", "El plano cartesiano y los pares ordenados")

        # De la recta al plano.
        titulo = self.encabezado("De la recta al plano")
        plano = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=5,
            background_line_style={"stroke_opacity": 0.25},
        ).shift(DOWN * 0.6)
        horizontal = NumberLine(x_range=[-6, 6, 1], length=10).move_to(plano.c2p(0, 0))
        self.decir("Una recta numérica sirve para ubicar un número.")
        self.play(Create(horizontal))
        self.pie("Una recta numérica sirve para ubicar un número...", espera=1.5)
        vertical = horizontal.copy()
        self.decir("Si cruzamos dos rectas perpendiculares en el cero, podemos ubicar cualquier punto del plano. El cruce es el origen.")
        self.play(Rotate(vertical, PI / 2, about_point=plano.c2p(0, 0)), run_time=1.5)
        self.play(FadeIn(plano), FadeOut(horizontal), FadeOut(vertical))
        rot_x = MathTex("x", font_size=40).next_to(plano.c2p(6, 0), DOWN + LEFT, buff=0.15)
        rot_y = MathTex("y", font_size=40).next_to(plano.c2p(0, 3), LEFT + DOWN, buff=0.15)
        origen = Dot(plano.c2p(0, 0), color=COLOR_PIVOTE)
        rot_origen = Tex(r"origen $(0, 0)$", font_size=32, color=COLOR_PIVOTE).next_to(origen, DL, buff=0.1)
        self.play(Write(rot_x), Write(rot_y), FadeIn(origen), FadeIn(rot_origen))
        self.pie("...y dos rectas perpendiculares sirven para ubicar un punto del plano.", espera=2.5)
        self.play(FadeOut(rot_origen))

        # El punto (3, 2).
        punto = Dot(plano.c2p(0, 0), color=COLOR_PIVOTE, radius=0.1)
        ida_x = DashedLine(plano.c2p(0, 0), plano.c2p(3, 0), color=COLOR_COEFICIENTE)
        ida_y = DashedLine(plano.c2p(3, 0), plano.c2p(3, 2), color=COLOR_TERMINO_INDEP)
        self.add(punto)
        self.decir("Para llegar al punto tres, dos, avanzamos tres en horizontal y subimos dos. La primera coordenada siempre es la horizontal, equis; la segunda, la vertical, ye.")
        self.play(Create(ida_x), punto.animate.move_to(plano.c2p(3, 0)))
        self.play(Create(ida_y), punto.animate.move_to(plano.c2p(3, 2)))
        etiqueta = MathTex("(", "3", ",", "2", ")", font_size=44).next_to(punto, UR, buff=0.1)
        etiqueta[1].set_color(COLOR_COEFICIENTE)
        etiqueta[3].set_color(COLOR_TERMINO_INDEP)
        self.play(Write(etiqueta))
        self.pie(
            "Primera coordenada (x): cuánto a la derecha. Segunda coordenada (y): cuánto hacia arriba.",
            espera=3,
        )

        # El orden importa.
        otro = Dot(plano.c2p(2, 3), color=COLOR_LIBRE, radius=0.1)
        rot_otro = MathTex("(2, 3)", font_size=44, color=COLOR_LIBRE).next_to(otro, UL, buff=0.1)
        self.decir("Dos, tres es otro punto. Por eso hablamos de pares ordenados: el orden importa.")
        self.play(FadeIn(otro, scale=2), Write(rot_otro))
        self.pie("(2, 3) es OTRO punto: en un par ordenado, el orden importa.", espera=3)
        self.play(*[FadeOut(m) for m in (ida_x, ida_y, otro, rot_otro)])

        # Coordenadas negativas y cuadrantes.
        ejemplos = [((-4, 1), "(-4, 1)"), ((-2, -2), "(-2, -2)"), ((2, -2), "(2, -2)")]
        marcas = VGroup()
        for (x, y), tex in ejemplos:
            d = Dot(plano.c2p(x, y), color=COLOR_PIVOTE, radius=0.1)
            marcas.add(VGroup(d, MathTex(tex, font_size=40).next_to(d, UR if x > 0 else UL, buff=0.1)))
        self.decir("Los números negativos significan ir a la izquierda o hacia abajo.")
        self.play(LaggedStart(*[FadeIn(m) for m in marcas], lag_ratio=0.5))
        cuadrantes = VGroup(
            *[
                MathTex(t, font_size=34, color=COLOR_SECUNDARIO).move_to(plano.c2p(x, y))
                for t, x, y in (
                    (r"\text{I}\ (+,+)", 5, 1.0),
                    (r"\text{II}\ (-,+)", -4.5, 2.4),
                    (r"\text{III}\ (-,-)", -4.5, -2.4),
                    (r"\text{IV}\ (+,-)", 4.5, -2.4),
                )
            ]
        )
        self.decir("Los ejes dividen el plano en cuatro cuadrantes, según los signos de las coordenadas.")
        self.play(FadeIn(cuadrantes))
        self.pie("Los ejes dividen el plano en cuatro cuadrantes, según los signos de x e y.", espera=4)
        self.limpiar(titulo)

        # Notación.
        titulo = self.cambiar_encabezado(titulo, "El plano R²")
        notacion = MathTex(
            r"\mathbb{R}^2 = \text{conjunto de todos los pares } (x, y) \text{ de números reales}", font_size=44
        )
        conexion = Tex(
            r"Una solución de una ecuación con dos incógnitas es un par $(x, y)$:\\ un \textbf{punto} del plano.",
            font_size=40,
            color=COLOR_SOLUCION,
        )
        VGroup(notacion, conexion).arrange(DOWN, buff=1)
        self.decir("Al conjunto de todos los pares de números reales lo llamamos erre dos.")
        self.play(Write(notacion))
        self.wait(2)
        self.decir("La idea clave: una solución de una ecuación con dos incógnitas es un par, es decir, un punto del plano.")
        self.play(FadeIn(conexion))
        self.wait(4)

        self.ejercicio_propuesto(
            "F00-N1-07",
            Tex(
                r"Dibuja $A(2, -1)$, $B(-3, 2)$, $C(0, 4)$ y $D(-1, 0)$.\\"
                r"¿En qué cuadrante (o en qué eje) está cada uno?",
                font_size=42,
            ),
        )
        self.resumen(
            [
                "Un punto del plano se describe con un par ordenado (x, y).",
                "x: desplazamiento horizontal; y: desplazamiento vertical.",
                "El orden importa: (3, 2) y (2, 3) son puntos distintos.",
                "Soluciones de ecuaciones con dos incógnitas = puntos del plano.",
            ],
            "la gráfica de una ecuación.",
            voz="En resumen: un punto del plano se describe con un par ordenado, equis coma ye. Equis es el desplazamiento horizontal, y ye, el vertical. El orden importa: tres, dos y dos, tres son puntos distintos. Y las soluciones de una ecuación con dos incógnitas son puntos del plano. Siguiente: la gráfica de una ecuación.",
        )


class GraficaComoConjuntoDePuntos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 3 · Parte 2", "La gráfica de una ecuación")
        titulo = self.encabezado("¿Qué puntos cumplen x + y = 3?")
        sistema = ejes((-2, 5), (-2, 5), unidad=0.75).to_edge(LEFT, buff=0.7).shift(UP * 0.1)
        self.decir("¿Qué puntos cumplen equis más ye igual a tres? Probemos.")
        self.play(Create(sistema))

        pruebas = [(1, 2), (0, 3), (2, 2), (4, -1), (-1, 4), (3, 0)]
        panel = VGroup()
        buenos = VGroup()
        self.decir("Uno, dos: sí, suma tres. Cero, tres: sí. Dos, dos: no, suma cuatro. Cuatro, menos uno: sí.")
        for x, y in pruebas:
            cumple = x + y == 3
            color = COLOR_SOLUCION if cumple else COLOR_ERROR
            signo = r"\checkmark" if cumple else r"\neq 3"
            linea = MathTex(rf"({x}, {y}):\quad {x} + ({y}) = {x + y}\ {signo}", font_size=36, color=color)
            if panel:
                linea.next_to(panel, DOWN, aligned_edge=LEFT, buff=0.25)
            else:
                linea.to_edge(RIGHT, buff=1.2).shift(UP * 2.2)
            panel.add(linea)
            punto = Dot(sistema.c2p(x, y), color=color, radius=0.09)
            self.play(Write(linea), FadeIn(punto, scale=2), run_time=1.2)
            if cumple:
                buenos.add(punto)
            else:
                self.wait(0.5)
                self.play(FadeOut(punto))
            self.wait(0.6)
        self.decir("Los puntos que cumplen la ecuación parecen estar alineados.")
        self.pie("Los puntos que cumplen la ecuación parecen estar alineados...", espera=2)

        # Muchos más puntos: se ve la recta.
        xs = np.arange(-1.5, 4.51, 0.25)
        muchos = VGroup(*[Dot(sistema.c2p(x, 3 - x), color=COLOR_SOLUCION, radius=0.05) for x in xs])
        self.decir("Si dibujamos muchísimos puntos que la cumplen, aparece una recta. La gráfica de una ecuación es el conjunto de todos los puntos que la cumplen.")
        self.play(LaggedStart(*[FadeIn(d) for d in muchos], lag_ratio=0.05), run_time=2)
        recta = recta_recortada(sistema, -1, 3, color=COLOR_SOLUCION)
        self.play(Create(recta), run_time=1.5)
        self.pie(
            "La GRÁFICA de una ecuación es el conjunto de TODOS los puntos que la cumplen.\n"
            "Para x + y = 3, la gráfica es una recta.",
            espera=4,
        )
        criterio = Tex(
            r"Un punto está en la gráfica \textbf{si y solo si}\\ sus coordenadas cumplen la ecuación.",
            font_size=34,
            color=COLOR_PIVOTE,
        ).next_to(panel, DOWN, buff=0.6).to_edge(RIGHT, buff=0.5)
        self.decir("Un punto está en la gráfica si y solo si sus coordenadas cumplen la ecuación.")
        self.play(FadeIn(criterio))
        self.wait(4)

        # No toda ecuación da una recta.
        self.play(*[FadeOut(m) for m in (panel, buenos, muchos, recta, criterio)])
        titulo = self.cambiar_encabezado(titulo, "No toda ecuación da una recta: y = x²")
        parabola = sistema.plot(lambda x: x**2, x_range=[-2, 2.2], color=COLOR_LIBRE)
        puntos = VGroup(*[Dot(sistema.c2p(x, x * x), color=COLOR_LIBRE) for x in (-2, -1, 0, 1, 2)])
        tabla = MathTex(r"(-2, 4),\ (-1, 1),\ (0, 0),\ (1, 1),\ (2, 4)", font_size=36, color=COLOR_LIBRE)
        tabla.to_edge(RIGHT, buff=0.8).shift(UP * 1.5)
        self.decir("No toda ecuación da una recta: ye igual a equis al cuadrado da una curva, una parábola.")
        self.play(LaggedStart(*[FadeIn(p, scale=2) for p in puntos], lag_ratio=0.3), Write(tabla))
        self.play(Create(parabola), run_time=2)
        self.decir("Las ecuaciones cuyas gráficas son rectas, o planos, son las ecuaciones lineales: las protagonistas del curso.")
        self.pie(
            "Estos puntos no están alineados: la gráfica es una curva (una parábola).\n"
            "Las ecuaciones que siempre dan rectas son las LINEALES: las estudiamos en la Lección 5.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F00-N2-05",
            Tex(
                r"¿Cuáles de los puntos $(2, 0)$, $(0, -4)$, $(3, 2)$, $(1, 1)$ están\\ en la gráfica de $2x - y = 4$?\\"
                r"Encuentra otros dos puntos de esa gráfica.",
                font_size=40,
            ),
        )
        self.resumen(
            [
                "La gráfica de una ecuación = todos los puntos que la cumplen.",
                "Comprobar si un punto está en la gráfica = sustituir sus coordenadas.",
                "x + y = 3 da una recta; y = x² da una curva.",
            ],
            "pendiente de una recta.",
            voz="En resumen: la gráfica de una ecuación es el conjunto de todos los puntos que la cumplen. Para comprobar si un punto está en la gráfica, se sustituyen sus coordenadas. Equis más ye igual a tres da una recta; ye igual a equis al cuadrado da una curva. Siguiente: la pendiente de una recta.",
        )


class PendienteDeUnaRecta(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 3 · Parte 3", "Pendiente y ordenada en el origen")
        titulo = self.encabezado("La recta y = mx + n")
        sistema = ejes((-4, 4), (-3, 4), unidad=0.7).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        self.decir("Veamos la recta ye igual a eme equis más ene.")
        self.play(Create(sistema))

        m, n = ValueTracker(2), ValueTracker(1)
        recta = always_redraw(lambda: recta_recortada(sistema, m.get_value(), n.get_value(), color=COLOR_COEFICIENTE))

        def escalon():
            # Desde (0, n): un paso a la derecha y m hacia arriba.
            a = sistema.c2p(0, n.get_value())
            b = sistema.c2p(1, n.get_value())
            c = sistema.c2p(1, n.get_value() + m.get_value())
            return VGroup(
                Line(a, b, color=COLOR_PIVOTE, stroke_width=5),
                Line(b, c, color=COLOR_LIBRE, stroke_width=5),
                MathTex("1", font_size=30, color=COLOR_PIVOTE).next_to(Line(a, b), DOWN, buff=0.1),
                MathTex("m", font_size=30, color=COLOR_LIBRE).next_to(Line(b, c), RIGHT, buff=0.1),
            )

        triangulo = always_redraw(escalon)
        corte = always_redraw(lambda: Dot(sistema.c2p(0, n.get_value()), color=COLOR_TERMINO_INDEP, radius=0.09))
        lectura = always_redraw(
            lambda: MathTex(
                rf"y = {decimal(m.get_value())}\,x + ({decimal(n.get_value())})", font_size=44
            ).to_edge(RIGHT, buff=0.8).shift(UP * 2.3)
        )
        self.play(Create(recta), FadeIn(corte), Write(lectura))
        explica_n = Tex(
            r"$n$: valor de $y$ cuando $x = 0$\\(donde la recta corta al eje $y$)",
            font_size=34,
            color=COLOR_TERMINO_INDEP,
        ).next_to(lectura, DOWN, buff=0.5)
        self.decir("El número ene es la altura a la que la recta corta al eje vertical: la ordenada en el origen. Si cambiamos ene, la recta se desplaza sin girar.")
        self.play(FadeIn(explica_n))
        for valor in (-1, 3, 1):
            self.play(n.animate.set_value(valor), run_time=1.3)
        self.wait(1)
        explica_m = Tex(
            r"$m$ (pendiente): cuánto sube $y$\\cuando $x$ avanza $1$",
            font_size=34,
            color=COLOR_LIBRE,
        ).next_to(explica_n, DOWN, buff=0.5)
        self.decir("El número eme dice cuánto sube la recta cuando avanzamos una unidad a la derecha. Es la pendiente.")
        self.play(Create(triangulo), FadeIn(explica_m))
        self.wait(1.5)
        for valor in (0.5, 0, -1, 2):
            self.play(m.animate.set_value(valor), run_time=1.5)
            self.wait(0.6)
        self.decir("Con eme positiva, la recta sube; con eme cero, es horizontal; con eme negativa, baja.")
        self.pie("m > 0: la recta sube. m = 0: horizontal. m < 0: baja.", espera=4)
        self.limpiar(titulo, sistema)

        # La pendiente a partir de dos puntos.
        titulo = self.cambiar_encabezado(titulo, "Pendiente a partir de dos puntos")
        p, q = (1, 1), (2, 3)
        dp, dq = Dot(sistema.c2p(*p), color=COLOR_PIVOTE), Dot(sistema.c2p(*q), color=COLOR_PIVOTE)
        rot_p = MathTex("(1, 1)", font_size=34).next_to(dp, RIGHT, buff=0.15)
        rot_q = MathTex("(2, 3)", font_size=34).next_to(dq, LEFT, buff=0.15)
        avance = Line(sistema.c2p(1, 1), sistema.c2p(2, 1), color=COLOR_PIVOTE)
        subida = Line(sistema.c2p(2, 1), sistema.c2p(2, 3), color=COLOR_LIBRE)
        self.decir("Si conocemos dos puntos de la recta, la pendiente es lo que sube dividido entre lo que avanza.")
        self.play(FadeIn(dp), FadeIn(dq), Write(rot_p), Write(rot_q))
        self.play(Create(avance), Create(subida))
        formula = VGroup(
            MathTex(r"m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{3 - 1}{2 - 1} = \frac{2}{1} = 2", font_size=42),
            MathTex(r"n:\ \ 1 = 2\cdot 1 + n \;\Rightarrow\; n = -1", font_size=42),
            MathTex(r"y = 2x - 1", font_size=48, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.7)
        nota_sub = Text("(los subíndices 1 y 2 solo numeran los dos puntos)", font_size=TAM_NOTA - 4, color=COLOR_SECUNDARIO)
        nota_sub.next_to(formula, UP, buff=0.4)
        self.decir("Diferencia de alturas entre diferencia de abscisas.")
        self.play(Write(formula[0]), FadeIn(nota_sub))
        self.wait(2)
        self.decir("Luego, sustituyendo uno de los puntos, obtenemos ene.")
        self.play(Write(formula[1]))
        self.play(Write(formula[2]), Create(recta_recortada(sistema, 2, -1, color=COLOR_SOLUCION)))
        self.wait(3)
        self.limpiar(titulo, sistema)

        # Rectas verticales y la forma general ax + by = c.
        titulo = self.cambiar_encabezado(titulo, "Rectas verticales y la forma ax + by = c")
        vertical = Line(sistema.c2p(2, -3), sistema.c2p(2, 4), color=COLOR_COEFICIENTE)
        self.decir("Una recta vertical no avanza: tendríamos que dividir entre cero. No tiene pendiente, y no se puede escribir como ye igual a eme equis más ene.")
        self.play(Create(vertical))
        textos = VGroup(
            MathTex(r"(2, -1),\ (2, 3):\quad m = \frac{3 - (-1)}{2 - 2} = \frac{4}{0}", font_size=40),
            Tex(r"No existe: dividir entre 0 no está definido.", font_size=36, color=COLOR_ERROR),
            Tex(r"Pero la recta sí tiene ecuación: $x = 2$,\\ es decir, $1\cdot x + 0\cdot y = 2$.", font_size=36),
            Tex(r"Forma general: $ax + by = c$\\ describe \textbf{todas} las rectas.", font_size=40, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.6)
        for t in textos:
            self.play(FadeIn(t))
            self.wait(2)
        self.wait(1)
        self.play(FadeOut(textos), FadeOut(vertical))
        despeje = VGroup(
            MathTex(r"2x + 3y = 6", font_size=44),
            MathTex(r"3y = -2x + 6", font_size=44),
            MathTex(r"y = -\tfrac{2}{3}x + 2", font_size=44, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.4).to_edge(RIGHT, buff=1.2)
        self.decir("Pero sí se puede escribir en la forma a equis más be ye igual a ce, que sirve para todas las rectas. Será la que usemos en los sistemas.")
        self.play(Write(despeje[0]))
        self.play(Write(despeje[1]))
        self.play(Write(despeje[2]), Create(recta_recortada(sistema, -2 / 3, 2, color=COLOR_SOLUCION)))
        self.decir("Si be es distinto de cero, se puede despejar ye: la pendiente es menos a entre be, y la ordenada en el origen, ce entre be.")
        self.pie("Si b es distinto de 0, se puede despejar y: pendiente -a/b y ordenada en el origen c/b.", espera=4)
        self.limpiar(titulo, sistema)

        # Rectas paralelas: anticipo de los sistemas sin solución.
        titulo = self.cambiar_encabezado(titulo, "Rectas paralelas")
        r1 = recta_recortada(sistema, 1, 1, color=COLOR_COEFICIENTE)
        r2 = recta_recortada(sistema, 1, -2, color=COLOR_TERMINO_INDEP)
        etiquetas = VGroup(
            MathTex(r"y = x + 1", font_size=44, color=COLOR_COEFICIENTE),
            MathTex(r"y = x - 2", font_size=44, color=COLOR_TERMINO_INDEP),
        ).arrange(DOWN, buff=0.4).to_edge(RIGHT, buff=1.5).shift(UP * 1)
        self.decir("Dos rectas con la misma pendiente y distinta altura nunca se cortan: son paralelas.")
        self.play(Create(r1), Write(etiquetas[0]))
        self.play(Create(r2), Write(etiquetas[1]))
        self.decir("Recuérdalo: en la lección ocho descubriremos que eso significa un sistema sin solución.")
        self.pie(
            "Misma pendiente y distinta ordenada en el origen: nunca se cortan.\n"
            "En la Lección 8 veremos que esto corresponde a un sistema SIN solución.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F00-N2-06",
            Tex(
                r"Halla la pendiente, la ordenada en el origen y la ecuación\\"
                r"de la recta que pasa por $(-1, 4)$ y $(2, -2)$.",
                font_size=42,
            ),
        )
        self.resumen(
            [
                "En y = mx + n: m es la pendiente y n la ordenada en el origen.",
                "Con dos puntos: m = (y2 - y1) / (x2 - x1).",
                "Las rectas verticales no tienen pendiente;\nla forma ax + by = c sirve para todas.",
                "Misma pendiente y distinta n: rectas paralelas.",
            ],
            "el espacio de tres coordenadas.",
            voz="En resumen: en ye igual a eme equis más ene, eme es la pendiente y ene la ordenada en el origen. Con dos puntos, la pendiente es la diferencia de alturas entre la diferencia de abscisas. Las rectas verticales no tienen pendiente; la forma a equis más be ye igual a ce sirve para todas. Y misma pendiente con distinta ene: rectas paralelas. Siguiente: el espacio de tres coordenadas.",
        )


class EspacioTresCoordenadas(EscenaCurso, ThreeDScene):
    def construct(self):
        self.mostrar_portada("Lección 3 · Parte 4", "El espacio de tres coordenadas")
        titulo = self.encabezado("Ternas ordenadas (x, y, z)")

        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES, zoom=0.8)
        espacio = ThreeDAxes(
            x_range=[-1, 4, 1], y_range=[-1, 4, 1], z_range=[-1, 4, 1], x_length=5, y_length=5, z_length=5
        )
        espacio.shift(-espacio.c2p(1.5, 1.5, 1.8))  # centra en pantalla la zona positiva, que es la que se usa
        rotulos = VGroup(
            MathTex("x").move_to(espacio.c2p(4.4, 0, 0)),
            MathTex("y").move_to(espacio.c2p(0, 4.4, 0)),
            MathTex("z").move_to(espacio.c2p(0, 0, 4.4)),
        )
        for r in rotulos:
            self.add_fixed_orientation_mobjects(r)
        self.decir("En el espacio necesitamos tres números, porque hay tres direcciones: equis, ye y zeta.")
        self.play(Create(espacio), FadeIn(rotulos))

        # El punto (2, 1, 3) se alcanza en tres movimientos.
        tramos = [((0, 0, 0), (2, 0, 0), COLOR_COEFICIENTE), ((2, 0, 0), (2, 1, 0), COLOR_TERMINO_INDEP), ((2, 1, 0), (2, 1, 3), COLOR_LIBRE)]
        punto = Dot3D(espacio.c2p(0, 0, 0), color=COLOR_PIVOTE, radius=0.1)
        self.add(punto)
        self.decir("Para llegar al punto dos, uno, tres, avanzamos dos en la dirección equis, uno en la dirección ye, y subimos tres.")
        for a, b, color in tramos:
            self.play(Create(DashedLine(espacio.c2p(*a), espacio.c2p(*b), color=color)), punto.animate.move_to(espacio.c2p(*b)))
        etiqueta = MathTex("(2, 1, 3)", font_size=40, color=COLOR_PIVOTE).move_to(espacio.c2p(2.3, 1, 3.5))
        self.add_fixed_orientation_mobjects(etiqueta)
        self.play(FadeIn(etiqueta))
        self.decir("Al conjunto de todas las ternas de números reales lo llamamos erre tres.")
        self.pie("2 en la dirección x, 1 en la dirección y, 3 hacia arriba (z). El conjunto de todas las ternas es R³.", espera=4)

        # Una ecuación con tres incógnitas: un plano.
        titulo = self.cambiar_encabezado(titulo, "x + y + z = 3 es un plano")
        trozo = Polygon(
            espacio.c2p(3, 0, 0), espacio.c2p(0, 3, 0), espacio.c2p(0, 0, 3),
            fill_color=COLOR_COEFICIENTE, fill_opacity=0.45, stroke_color=COLOR_COEFICIENTE,
        )
        self.decir("Las soluciones de equis más ye más zeta igual a tres forman un plano.")
        self.play(FadeIn(trozo))
        centro = Dot3D(espacio.c2p(1, 1, 1), color=COLOR_SOLUCION, radius=0.1)
        rot_centro = MathTex(r"(1,1,1)\colon\ 1+1+1 = 3\ \checkmark", font_size=34, color=COLOR_SOLUCION)
        rot_centro.to_corner(DR, buff=0.8).shift(UP * 0.6)
        self._fijar(rot_centro)
        self.decir("El punto uno, uno, uno está en él, porque uno más uno más uno es tres.")
        self.play(FadeIn(centro), FadeIn(rot_centro))
        self.decir("Dibujamos solo el trozo que cae en la zona positiva: el plano real es infinito.")
        self.pie("Dibujamos solo el trozo que cae en la zona positiva: el plano real es infinito.", espera=2)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.limpiar()

        # Más de tres incógnitas.
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1)
        titulo = self.encabezado("¿Y con cuatro o más incógnitas?")
        ideas = VGroup(
            MathTex(r"(x_1, x_2, x_3, x_4) \in \mathbb{R}^4", font_size=54),
            Text("Es simplemente una lista de 4 números.", font_size=TAM_TEXTO),
            Text("No se puede dibujar, pero el álgebra funciona exactamente igual.", font_size=TAM_TEXTO),
            Text("Los dibujos en 2D y 3D ayudan a la intuición;\nno son una demostración.", font_size=TAM_TEXTO, color=COLOR_PIVOTE, line_spacing=1.1),
        ).arrange(DOWN, buff=0.5)
        self._fijar(ideas)
        self.decir("¿Y con cuatro incógnitas? Una solución es una lista de cuatro números. No podemos dibujarla, pero el álgebra funciona exactamente igual. Los dibujos nos ayudan a entender; no son demostraciones.")
        for i in ideas:
            self.play(FadeIn(i))
            self.wait(2)
        self.wait(2)

        self.ejercicio_propuesto(
            "F00-N5-03",
            Tex(
                r"a) ¿Están $(1, 2, 0)$ y $(2, 2, 1)$ en el plano $x + y + z = 3$?\\"
                r"b) Encuentra el punto donde el plano $x + 2y - z = 4$ corta a cada eje.",
                font_size=40,
            ),
        )
        self.resumen(
            [
                "Un punto del espacio es una terna (x, y, z).",
                "Una ecuación lineal con tres incógnitas tiene por gráfica un plano.",
                "Con n incógnitas, una solución es una lista de n números,\naunque no se pueda dibujar.",
            ],
            "Lección 4 — el lenguaje matemático: conjuntos, subíndices y lógica.",
            voz="En resumen: un punto del espacio es una terna, equis, ye, zeta. Una ecuación lineal con tres incógnitas tiene por gráfica un plano. Y con ene incógnitas, una solución es una lista de ene números, aunque no se pueda dibujar. Siguiente: lección cuatro, el lenguaje matemático.",
        )
