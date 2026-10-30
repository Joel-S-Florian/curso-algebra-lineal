"""Lección 7 — Ecuaciones lineales con dos y tres incógnitas: rectas y planos.

Escenas (un video cada una):
    InfinitasSolucionesDeUnaEcuacion, EcuacionComoRecta, EcuacionComoPlano, ParametrizarUnaRecta

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l07_dos_y_tres_incognitas.py -a
"""

import sys
from fractions import Fraction
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ejes_iguales, plano_3d, recta_general  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def tex_fraccion(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else rf"\tfrac{{{q.numerator}}}{{{q.denominator}}}"


class InfinitasSolucionesDeUnaEcuacion(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 7 · Parte 1", "Una ecuación con dos incógnitas:\ninfinitas soluciones")
        titulo = self.encabezado("x + 2y = 4: elige y, despeja x")
        sistema = ejes_iguales((-2, 7), (-2, 3), unidad=0.65).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.3)
        despeje = MathTex(r"x = 4 - 2y", font_size=48, color=COLOR_COEFICIENTE).to_edge(LEFT, buff=1).shift(UP * 2.2)
        self.decir("Tomemos equis más dos ye igual a cuatro. Si elegimos el valor de ye, despejamos equis: equis es cuatro menos dos ye.")
        self.play(Create(sistema), Write(despeje))
        filas, puntos = VGroup(), VGroup()
        self.decir("Elegimos ye cero: equis vale cuatro. Ye uno: equis vale dos. Ye dos: equis vale cero. Ye menos uno: equis vale seis. Y ye un medio: equis vale tres.")
        for y in (Fraction(0), Fraction(1), Fraction(2), Fraction(-1), Fraction(1, 2)):
            x = 4 - 2 * y
            fila = MathTex(
                rf"y = {tex_fraccion(y)}", r"\ \Rightarrow\ ", rf"x = 4 - 2\cdot({tex_fraccion(y)}) = {tex_fraccion(x)}",
                font_size=36,
            )
            fila[0].set_color(COLOR_LIBRE)
            if filas:
                fila.next_to(filas, DOWN, aligned_edge=LEFT, buff=0.3)
            else:
                fila.next_to(despeje, DOWN, aligned_edge=LEFT, buff=0.5)
            filas.add(fila)
            punto = Dot(sistema.c2p(float(x), float(y)), color=COLOR_SOLUCION)
            self.play(Write(fila), FadeIn(punto, scale=2), run_time=1.2)
            puntos.add(punto)
            self.wait(0.5)
        self.decir("Cada valor de ye da un único equis, así que hay tantas soluciones como valores de ye: infinitas.")
        self.pie("Cada valor de y da exactamente un valor de x: hay tantas soluciones como valores de y.", espera=3)
        muchos = VGroup(*[Dot(sistema.c2p(4 - 2 * y, y), radius=0.04, color=COLOR_SOLUCION) for y in np.arange(-1, 3.01, 0.125)])
        self.decir("Todas juntas forman una recta.")
        self.play(LaggedStart(*[FadeIn(d) for d in muchos], lag_ratio=0.03))
        self.play(Create(recta_general(sistema, 1, 2, 4, color=COLOR_SOLUCION)))
        self.pie("Infinitas soluciones, todas sobre una recta.", espera=2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "En general")
        bloque = VGroup(
            MathTex(r"a x + b y = c", font_size=60),
            Tex(r"Si $a \neq 0$: se elige $y$ libremente y se despeja $x = \dfrac{c - b y}{a}$.", font_size=40),
            Tex(r"Si $a = 0$ pero $b \neq 0$: al revés, $x$ es libre e $y = \dfrac{c}{b}$.", font_size=40),
            Tex(r"Si $a = b = 0$: el caso degenerado de la Lección 5 ($0 = c$).", font_size=40, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.5)
        self.decir("Siempre que a o be no sean cero, podemos elegir una incógnita libremente y despejar la otra.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.decir("Una sola ecuación con dos incógnitas nunca fija un único punto: para eso harán falta más ecuaciones, es decir, un sistema.")
        self.pie(
            "Conclusión: si a y b no son ambos 0, una ecuación lineal con dos incógnitas tiene INFINITAS soluciones.\n"
            "Por eso, para fijar un único punto, harán falta más ecuaciones: un sistema.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F02-N1-01",
            Tex(r"Encuentra cuatro soluciones de $3x - y = 6$, una de ellas con $x = \tfrac13$.", font_size=44),
        )
        self.resumen(
            [
                "Una ecuación lineal con dos incógnitas (no degenerada) tiene infinitas soluciones.",
                "Se obtienen eligiendo una incógnita libre y despejando la otra.",
                "Todas esas soluciones forman una recta.",
            ],
            "la recta, con sus cortes con los ejes.",
        )


class EcuacionComoRecta(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 7 · Parte 2", "ax + by = c es una recta")
        titulo = self.encabezado("Dibujar una recta con sus cortes con los ejes")
        sistema = ejes_iguales((-2, 5), (-2, 5), unidad=0.75).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        self.decir("Para dibujar dos equis más ye igual a cuatro, buscamos dónde corta a los ejes.")
        self.play(Create(sistema))
        pasos = VGroup(
            MathTex(r"2x + y = 4", font_size=52, color=COLOR_COEFICIENTE),
            MathTex(r"x = 0:\ y = 4 \ \to\ (0, 4)", font_size=42),
            MathTex(r"y = 0:\ 2x = 4,\ x = 2 \ \to\ (2, 0)", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(RIGHT, buff=0.8).shift(UP * 1.2)
        self.play(Write(pasos[0]))
        self.decir("Con equis igual a cero, ye vale cuatro. Con ye igual a cero, equis vale dos.")
        for paso, punto in zip(pasos[1:], ((0, 4), (2, 0))):
            self.play(Write(paso), FadeIn(Dot(sistema.c2p(*punto), color=COLOR_PIVOTE), scale=2))
            self.wait(1)
        self.decir("Dos puntos determinan la recta: basta encontrar dos soluciones.")
        self.play(Create(recta_general(sistema, 2, 1, 4, color=COLOR_COEFICIENTE)))
        self.pie("Dos puntos determinan una recta: basta encontrar dos soluciones.", espera=3)
        self.limpiar(titulo, sistema)

        # Rectas verticales y horizontales.
        titulo = self.cambiar_encabezado(titulo, "Si falta una incógnita")
        vertical = recta_general(sistema, 2, 0, 4, color=COLOR_COEFICIENTE)
        horizontal = recta_general(sistema, 0, 3, 6, color=COLOR_TERMINO_INDEP)
        textos = VGroup(
            MathTex(r"2x + 0y = 4 \;\Rightarrow\; x = 2", font_size=42, color=COLOR_COEFICIENTE),
            Text("y libre: recta vertical", font_size=TAM_NOTA, color=COLOR_COEFICIENTE),
            MathTex(r"0x + 3y = 6 \;\Rightarrow\; y = 2", font_size=42, color=COLOR_TERMINO_INDEP),
            Text("x libre: recta horizontal", font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.8)
        textos[2].shift(DOWN * 0.3)
        textos[3].shift(DOWN * 0.3)
        self.decir("Si falta una incógnita, esa incógnita es libre: dos equis igual a cuatro es la recta vertical equis igual a dos, para cualquier ye.")
        self.play(Write(textos[0]), Create(vertical))
        self.play(FadeIn(textos[1]))
        self.wait(1.5)
        self.decir("Y si falta equis, como en tres ye igual a seis, equis es libre: la recta horizontal ye igual a dos.")
        self.play(Write(textos[2]), Create(horizontal))
        self.play(FadeIn(textos[3]))
        self.wait(3)
        self.limpiar(titulo, sistema)

        # Ecuaciones proporcionales: la misma recta.
        titulo = self.cambiar_encabezado(titulo, "Ecuaciones proporcionales: la misma recta")
        r1 = recta_general(sistema, 2, 1, 4, color=COLOR_COEFICIENTE, stroke_width=8)
        r2 = DashedVMobject(recta_general(sistema, 4, 2, 8, color=COLOR_TERMINO_INDEP, stroke_width=4), num_dashes=30)
        textos = VGroup(
            MathTex(r"2x + y = 4", font_size=46, color=COLOR_COEFICIENTE),
            MathTex(r"4x + 2y = 8", font_size=46, color=COLOR_TERMINO_INDEP),
            Tex(r"La segunda es la primera multiplicada por 2\\(regla 2): mismas soluciones.", font_size=36),
        ).arrange(DOWN, buff=0.4).to_edge(RIGHT, buff=0.8)
        self.decir("Multiplicar toda la ecuación por dos no cambia sus soluciones.")
        self.play(Write(textos[0]), Create(r1))
        self.play(Write(textos[1]), Create(r2))
        self.decir("Es la misma recta, escrita de otra forma. Una recta tiene infinitas ecuaciones: todas las proporcionales a una de ellas.")
        self.play(FadeIn(textos[2]))
        self.pie("Una recta tiene infinitas ecuaciones: todas las proporcionales a una de ellas.", espera=4)

        self.ejercicio_propuesto(
            "F02-N2-01",
            VGroup(
                Tex(r"Dibuja usando los cortes con los ejes: \ a) $x - 2y = 4$ \quad b) $3y = 6$ \quad c) $x = -1$", font_size=40),
                Tex(r"¿Cuál no corta al eje $x$? ¿Cuál no corta al eje $y$?", font_size=40),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Si a y b no son ambos 0, ax + by = c es una recta.",
                "Para dibujarla bastan dos soluciones (por ejemplo, los cortes con los ejes).",
                "b = 0: recta vertical; a = 0: recta horizontal.",
                "Ecuaciones proporcionales describen la misma recta.",
            ],
            "ecuaciones con tres incógnitas: planos.",
            voz="En resumen: si a y be no son los dos cero, a equis más be ye igual a ce es una recta. Para dibujarla bastan dos soluciones, por ejemplo los cortes con los ejes. Si be es cero, la recta es vertical; si a es cero, horizontal. Y ecuaciones proporcionales describen la misma recta. Siguiente: ecuaciones con tres incógnitas, planos.",
        )


class EcuacionComoPlano(EscenaCurso, ThreeDScene):
    def construct(self):
        self.mostrar_portada("Lección 7 · Parte 3", "ax + by + cz = d es un plano")
        titulo = self.encabezado("x + 2y + z = 4")
        espacio, rotulos = self.espacio_3d(rango=(-1, 5), centro=(1.8, 1.4, 2.0), zoom=0.9)
        self.decir("Con tres incógnitas: equis más dos ye más zeta igual a cuatro.")
        self.play(Create(espacio), FadeIn(rotulos))

        cortes = [((4, 0, 0), "(4,0,0)"), ((0, 2, 0), "(0,2,0)"), ((0, 0, 4), "(0,0,4)")]
        marcas = VGroup()
        self.decir("Anulamos dos incógnitas para encontrar cada corte con los ejes: cuatro en el eje equis, dos en el eje ye, y cuatro en el eje zeta.")
        for p, tex in cortes:
            punto = Dot3D(espacio.c2p(*p), color=COLOR_PIVOTE, radius=0.09)
            rotulo = MathTex(tex, font_size=32, color=COLOR_PIVOTE).move_to(espacio.c2p(*p) + OUT * 0.4)
            self.add_fixed_orientation_mobjects(rotulo)
            self.play(FadeIn(punto, scale=2), FadeIn(rotulo))
            marcas.add(punto, rotulo)
        self.pie("Cortes con los ejes: se anulan dos incógnitas y se despeja la tercera.", espera=2)
        triangulo = Polygon(*[espacio.c2p(*p) for p, _ in cortes], fill_color=COLOR_COEFICIENTE, fill_opacity=0.5, stroke_color=COLOR_COEFICIENTE)
        self.decir("Los tres puntos determinan un plano. El triángulo es solo un trozo de él.")
        self.play(FadeIn(triangulo))
        self.pie("Los tres puntos determinan un plano. Este triángulo es solo un trozo de él.", espera=2)
        plano = plano_3d(espacio, 1, 2, 1, 4, rango_u=(-0.5, 2.5), rango_v=(-0.5, 4.5), color=COLOR_COEFICIENTE, opacidad=0.25)
        self.play(Create(plano), run_time=2)
        prueba = Dot3D(espacio.c2p(1, 1, 1), color=COLOR_SOLUCION, radius=0.1)
        texto_prueba = MathTex(r"(1, 1, 1):\ 1 + 2 + 1 = 4\ \checkmark", font_size=36, color=COLOR_SOLUCION).to_corner(DR, buff=0.8).shift(UP * 0.5)
        self._fijar(texto_prueba)
        self.decir("El punto uno, uno, uno también está: uno más dos más uno, cuatro.")
        self.play(FadeIn(prueba, scale=2), Write(texto_prueba))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.limpiar()

        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1)
        titulo = self.encabezado("Dos incógnitas libres")
        bloque = VGroup(
            MathTex(r"x + 2y + z = 4 \quad\Longrightarrow\quad x = 4 - 2y - z", font_size=48),
            Tex(r"Elegimos $y$ y $z$ libremente; $x$ queda determinada.", font_size=40),
            Tex(r"Dos valores libres: un plano. \quad Uno libre (Lección anterior): una recta.", font_size=40, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.6)
        self._fijar(bloque)
        self.decir("Ahora hay dos incógnitas libres: elegimos ye y zeta, y despejamos equis. Dos libres, un plano; una libre, una recta.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)

        self.ejercicio_propuesto(
            "F02-N2-02",
            Tex(r"Halla los cortes con los ejes del plano $2x + 3y + 6z = 12$\\y otros tres puntos de ese plano.", font_size=42),
        )
        self.resumen(
            [
                "Una ecuación lineal con tres incógnitas (no degenerada) es un plano.",
                "Sus soluciones tienen dos incógnitas libres.",
                "Los cortes con los ejes ayudan a dibujarlo.",
            ],
            "describir todas las soluciones con parámetros.",
        )


class ParametrizarUnaRecta(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 7 · Parte 4", "Parámetros: escribir todas las soluciones")
        titulo = self.encabezado("Un nombre para el valor libre")
        sistema = ejes_iguales((-3, 7), (-2, 4), unidad=0.65).to_edge(LEFT, buff=0.6).shift(DOWN * 0.4)
        self.decir("Volvamos a la recta equis más dos ye igual a cuatro.")
        self.play(Create(sistema), Create(recta_general(sistema, 1, 2, 4, color=COLOR_COEFICIENTE)))
        formula = VGroup(
            MathTex(r"x + 2y = 4", font_size=48, color=COLOR_COEFICIENTE),
            MathTex(r"y = t \ \Rightarrow\ x = 4 - 2t", font_size=44),
            MathTex(r"(x, y) = (4 - 2t,\ t)", font_size=48, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.8).shift(UP * 1.6)
        self.decir("Llamemos te al valor libre de ye. Entonces equis vale cuatro menos dos te.")
        for f in formula:
            self.play(Write(f))
            self.wait(1)
        t = ValueTracker(0)
        punto = always_redraw(lambda: Dot(sistema.c2p(4 - 2 * t.get_value(), t.get_value()), color=COLOR_PIVOTE, radius=0.1))
        lectura = always_redraw(
            lambda: MathTex(
                rf"t = {t.get_value():.1f}\ \to\ ({4 - 2 * t.get_value():.1f},\ {t.get_value():.1f})".replace("-0.0", "0.0"),
                font_size=40,
                color=COLOR_LIBRE,
            ).next_to(formula, DOWN, buff=0.7)
        )
        self.decir("Al mover te, el punto recorre toda la recta: cada te da un punto, y cada punto viene de algún te.")
        self.play(FadeIn(punto), FadeIn(lectura))
        for valor in (2, -1, 3, 1):
            self.play(t.animate.set_value(valor), run_time=2)
            self.wait(0.6)
        self.decir("Te es un parámetro: un número libre que recorre todas las soluciones.")
        self.pie(
            "Cada valor de t da un punto de la recta, y cada punto se obtiene con algún t.\n"
            "A t se le llama PARÁMETRO; la fórmula, una PARAMETRIZACIÓN de las soluciones.",
            espera=5,
        )
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La parametrización no es única")
        bloque = VGroup(
            MathTex(r"y = t:\quad (4 - 2t,\ t)", font_size=46),
            MathTex(r"x = s:\quad \left(s,\ \tfrac{4 - s}{2}\right)", font_size=46),
            Tex(r"El punto $(2, 1)$ se obtiene con $t = 1$ en la primera y con $s = 2$ en la segunda.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.6)
        self.decir("Podríamos haber llamado ese al valor de equis: otra fórmula, pero el mismo conjunto de soluciones.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.pie("Distintas fórmulas, mismo conjunto de soluciones.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Contar parámetros")
        bloque = VGroup(
            MathTex(r"x + 2y + z = 4:\quad (x, y, z) = (4 - 2s - t,\ s,\ t)", font_size=44),
            Tex(r"Dos parámetros ($s$ y $t$): un plano.", font_size=40, color=COLOR_LIBRE),
            Tex(r"Ecuación lineal no degenerada con $n$ incógnitas: $n - 1$ parámetros.", font_size=40, color=COLOR_PIVOTE),
            Tex(r"Más adelante, cada ecuación \emph{nueva} de un sistema quitará un parámetro.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.55)
        self.decir("Para un plano hacen falta dos parámetros. En general, con ene incógnitas y una ecuación no degenerada, hacen falta ene menos uno parámetros.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F02-N3-01",
            Tex(
                r"Parametriza las soluciones de $2x - 3y = 6$ de dos formas:\\"
                r"tomando $x$ como parámetro y tomando $y$ como parámetro.\\"
                r"Comprueba que $(3, 0)$ aparece en ambas.",
                font_size=42,
            ),
        )
        self.resumen(
            [
                "Un parámetro es un número libre que recorre todas las soluciones.",
                "x + 2y = 4: (x, y) = (4 − 2t, t).",
                "La parametrización no es única.",
                "n incógnitas y 1 ecuación (no degenerada): n − 1 parámetros.",
            ],
            "Lección 8 — sistemas de dos ecuaciones con dos incógnitas.",
            voz="En resumen: un parámetro es un número libre que recorre todas las soluciones. Para equis más dos ye igual a cuatro, las soluciones son cuatro menos dos te, coma, te. La parametrización no es única. Y con ene incógnitas y una ecuación no degenerada, hay ene menos uno parámetros. Siguiente: lección ocho, sistemas de dos ecuaciones con dos incógnitas.",
        )
