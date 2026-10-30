"""Lección 10 — Sistemas de m ecuaciones con n incógnitas; sistemas homogéneos.

Escenas (un video cada una):
    NotacionGeneral, HiperplanosYLimitesDelDibujo, SistemasHomogeneos

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l10_sistemas_mxn.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, alinear_por_igual, ejes_iguales, sistema_con_llave  # noqa: E402
from curso.componentes import rectas_de_sistema as rectas  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class NotacionGeneral(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 10 · Parte 1", "Sistemas de m ecuaciones\ncon n incógnitas")
        titulo = self.encabezado("La forma general")
        filas = [
            MathTex(f"a_{{{i}1}}x_1", "+", f"a_{{{i}2}}x_2", "+", r"\cdots", "+", f"a_{{{i}n}}x_n", "=", f"b_{i}", font_size=46)
            for i in ("1", "2", "m")
        ]
        alinear_por_igual(*filas, buff=1.0)
        puntos = MathTex(r"\vdots", font_size=46).move_to((filas[1].get_center() + filas[2].get_center()) / 2)
        cuerpo = VGroup(filas[0], filas[1], puntos, filas[2])
        for fila in filas:
            for k in (0, 2, 6):
                fila[k].set_color(COLOR_COEFICIENTE)
            fila[8].set_color(COLOR_TERMINO_INDEP)
        sistema = VGroup(Brace(cuerpo, LEFT), cuerpo).shift(DOWN * 0.2)
        self.decir("Así se escribe un sistema cualquiera.")
        self.play(Write(sistema), run_time=2.5)
        llave_m = Brace(cuerpo, RIGHT)
        rot_m = Text("m ecuaciones", font_size=TAM_NOTA).next_to(llave_m, RIGHT)
        llave_n = Brace(VGroup(filas[0][0], filas[0][6]), UP)
        rot_n = Text("n incógnitas", font_size=TAM_NOTA).next_to(llave_n, UP, buff=0.1)
        self.decir("Tiene eme ecuaciones, una por fila, y ene incógnitas, de equis uno a equis ene.")
        self.play(GrowFromCenter(llave_m), FadeIn(rot_m))
        self.play(GrowFromCenter(llave_n), FadeIn(rot_n))
        self.wait(1.5)
        marca = SurroundingRectangle(filas[1][2], color=COLOR_PIVOTE)
        lectura = Tex(
            r"$a_{ij}$: coeficiente de la incógnita $x_j$ en la ecuación $i$", font_size=36, color=COLOR_PIVOTE
        ).to_edge(DOWN, buff=1.0)
        self.decir("a sub i jota es el coeficiente de la incógnita jota en la ecuación i. Este, por ejemplo, es a dos dos.")
        self.play(Create(marca), FadeIn(lectura))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "En una línea, y qué es una solución")
        bloque = VGroup(
            MathTex(r"\sum_{j=1}^{n} a_{ij}\,x_j = b_i, \qquad i = 1, 2, \dots, m", font_size=50),
            Tex(r"Una \textbf{solución} es una lista $(s_1, s_2, \dots, s_n)$ de $n$ números reales", font_size=38),
            Tex(r"que cumple \textbf{las $m$ ecuaciones} al sustituir $x_1 = s_1, \dots, x_n = s_n$.", font_size=38),
            Tex(r"$m$ y $n$ pueden ser distintos: más ecuaciones que incógnitas, o menos.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45)
        self.decir("Con el sumatorio cabe en una línea: para cada ecuación i, la suma de a i jota por equis jota vale be i. Una solución es una lista de ene números reales que cumple las eme ecuaciones a la vez. Y eme y ene pueden ser distintos.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(1.8)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un ejemplo con m = 2 y n = 3")
        ejemplo = sistema_con_llave(
            ("x_1 + 2x_2 - x_3", "=", "4"), ("3x_1 - x_2 + 2x_3", "=", "0"), font_size=46, colores=False
        ).shift(UP * 1.6)
        self.decir("Un ejemplo con dos ecuaciones y tres incógnitas.")
        self.play(Write(ejemplo))
        datos = MathTex(r"a_{12} = 2,\quad a_{23} = 2,\quad a_{21} = 3,\quad b_2 = 0", font_size=40, color=COLOR_COEFICIENTE)
        datos.next_to(ejemplo, DOWN, buff=0.6)
        self.decir("Aquí, a uno dos vale dos, a dos tres vale dos, a dos uno vale tres, y be dos vale cero.")
        self.play(Write(datos))
        pruebas = VGroup(
            MathTex(r"(1, 1, -1):\quad 1 + 2 + 1 = 4\ \checkmark \qquad 3 - 1 - 2 = 0\ \checkmark", font_size=38, color=COLOR_SOLUCION),
            MathTex(r"(2, 1, 0):\quad 2 + 2 - 0 = 4\ \checkmark \qquad 6 - 1 + 0 = 5 \neq 0", font_size=38, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.4).next_to(datos, DOWN, buff=0.6)
        self.decir("Uno, uno, menos uno cumple las dos ecuaciones. Dos, uno, cero cumple la primera, pero en la segunda da cinco, no cero.")
        for p in pruebas:
            self.play(Write(p))
            self.wait(2)
        self.decir("Así que uno, uno, menos uno es solución, y dos, uno, cero no lo es.")
        self.pie("(1, 1, -1) es solución; (2, 1, 0) no, porque falla la segunda ecuación.", espera=3)

        self.ejercicio_propuesto(
            "F03-N1-03",
            VGroup(
                sistema_con_llave(
                    ("2x_1 - x_2 + 4x_3 - x_4", "=", "1"), ("x_1 + 5x_3", "=", "0"), ("-x_2 + x_3 + 2x_4", "=", "6"),
                    font_size=40, colores=False,
                ),
                Tex(r"a) ¿Cuánto valen $m$ y $n$? \ b) $a_{13}$, $a_{22}$, $a_{34}$, $a_{31}$ y $b_3$. \ c) ¿Es $(5, 1, -1, 4)$ solución?", font_size=36),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Sistema m × n: m ecuaciones, n incógnitas; a_ij es el coeficiente de x_j en la ecuación i.",
                "Forma compacta: para cada ecuación i, la suma de a_ij · x_j vale b_i.",
                "Una solución es una lista de n números que cumple las m ecuaciones.",
            ],
            "qué se puede (y qué no) dibujar.",
            voz="En resumen: un sistema de eme por ene tiene eme ecuaciones y ene incógnitas, y a i jota es el coeficiente de equis jota en la ecuación i. En forma compacta: para cada ecuación i, la suma de a i jota por equis jota vale be i. Y una solución es una lista de ene números que cumple las eme ecuaciones. Siguiente: qué se puede, y qué no, dibujar.",
        )


class HiperplanosYLimitesDelDibujo(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 10 · Parte 2", "Rectas, planos e hiperplanos")
        titulo = self.encabezado("Una ecuación lineal en 1, 2, 3 y 4 incógnitas")
        paneles = VGroup(self.panel_1d(), self.panel_2d(), self.panel_3d(), self.panel_4d()).arrange(RIGHT, buff=0.6)
        paneles.shift(UP * 0.6)
        textos = [("ax = b", "un punto", "0 libres"), ("ax + by = c", "una recta", "1 libre"),
                  ("ax + by + cz = d", "un plano", "2 libres"), ("4 incógnitas", "un hiperplano", "3 libres")]
        self.decir("Una ecuación lineal con una incógnita fija un punto; con dos, una recta, con una incógnita libre; con tres, un plano, con dos libres. Con cuatro, un hiperplano, que ya no podemos dibujar.")
        for panel, (ec, nombre, libres) in zip(paneles, textos):
            rotulos = VGroup(
                Text(ec, font_size=TAM_NOTA - 2, color=COLOR_COEFICIENTE),
                Text(nombre, font_size=TAM_NOTA),
                Text(libres, font_size=TAM_NOTA - 2, color=COLOR_LIBRE),
            ).arrange(DOWN, buff=0.15).next_to(panel, DOWN, buff=0.35)
            self.play(FadeIn(panel), FadeIn(rotulos))
            self.wait(1.2)
        self.decir("Cada incógnita más añade un grado de libertad.")
        self.pie(
            "Con n incógnitas, una ecuación lineal no degenerada describe un HIPERPLANO: un «plano» con n − 1 direcciones libres.\n"
            "Con 4 o más incógnitas ya no podemos dibujarlo, pero sigue existiendo.",
            espera=6,
        )
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cada ecuación nueva quita libertad")
        bloque = VGroup(
            Tex(r"En $\mathbb{R}^3$: \ 1 ecuación $\to$ plano (2 libres)", font_size=40),
            Tex(r"2 ecuaciones $\to$ normalmente una recta (1 libre)", font_size=40),
            Tex(r"3 ecuaciones $\to$ normalmente un punto (0 libres)", font_size=40),
            Tex(r"«Normalmente»: si cada ecuación aporta información nueva. Lo precisaremos con el \textbf{rango} (Lección 39).", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45)
        self.decir("En el espacio, una ecuación deja un plano; dos ecuaciones, normalmente una recta; tres, normalmente un punto. Normalmente significa: si cada ecuación aporta algo nuevo. Lo precisaremos con el rango.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que un dibujo puede y no puede hacer")
        ideas = VGroup(
            Text("Puede: dar intuición en 2 y 3 incógnitas (cortarse, ser paralelos, coincidir).", font_size=TAM_TEXTO, color=COLOR_SOLUCION),
            Text("No puede: representar sistemas con 4 o más incógnitas.", font_size=TAM_TEXTO, color=COLOR_ERROR),
            Text("No puede: demostrar nada ni dar soluciones exactas.", font_size=TAM_TEXTO, color=COLOR_ERROR),
            Text("Por eso necesitamos métodos algebraicos (Gauss) que funcionen en cualquier dimensión.", font_size=TAM_TEXTO, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        ajustar_al_encuadre(ideas)
        self.decir("Los dibujos dan intuición en dos y tres incógnitas, pero no sirven en dimensión alta, ni dan soluciones exactas, ni demuestran nada. Por eso necesitamos métodos algebraicos, como el de Gauss, que funcionen en cualquier dimensión.")
        for i in ideas:
            self.play(FadeIn(i, shift=RIGHT * 0.2))
            self.wait(1.8)

        self.ejercicio_propuesto(
            "F03-N3-02",
            VGroup(
                Tex(r"¿Cuántos parámetros necesitan las soluciones de cada ecuación?", font_size=40),
                MathTex(
                    r"\text{a) } 2x - y + z - 3w = 5 \qquad \text{b) } x_1 + x_2 + \cdots + x_{10} = 1"
                    r"\qquad \text{c) } 0x + 0y + 0z = 0 \qquad \text{d) } 0x + 0y = 3",
                    font_size=38,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Con n incógnitas, una ecuación lineal no degenerada es un hiperplano (n − 1 libres).",
                "n = 2: recta; n = 3: plano; n ≥ 4: no se puede dibujar.",
                "Cada ecuación que aporta información nueva quita un grado de libertad.",
            ],
            "los sistemas homogéneos.",
            voz="En resumen: con ene incógnitas, una ecuación lineal no degenerada es un hiperplano, con ene menos uno incógnitas libres. Con dos incógnitas es una recta; con tres, un plano; con cuatro o más, no se puede dibujar. Y cada ecuación que aporta información nueva quita un grado de libertad. Siguiente: los sistemas homogéneos.",
        )

    def panel_1d(self):
        recta = NumberLine(x_range=[-2, 2, 1], length=2.6)
        return VGroup(recta, Dot(recta.n2p(0.7), color=COLOR_PIVOTE, radius=0.1))

    def panel_2d(self):
        mini = ejes_iguales((-2, 2), (-2, 2), unidad=0.65, numeros=False)
        return VGroup(mini, mini.plot(lambda x: 0.5 - 0.6 * x, x_range=[-2, 2], color=COLOR_PIVOTE))

    def panel_3d(self):
        # Perspectiva dibujada a mano: tres ejes y un paralelogramo que representa el plano.
        o = ORIGIN
        ejes = VGroup(
            Arrow(o, RIGHT * 1.4, buff=0, stroke_width=3),
            Arrow(o, UP * 1.4, buff=0, stroke_width=3),
            Arrow(o, (DOWN + LEFT) * 0.9, buff=0, stroke_width=3),
        )
        plano = Polygon(LEFT * 1.1 + UP * 0.2, RIGHT * 0.6 + UP * 0.9, RIGHT * 1.3 + DOWN * 0.3, LEFT * 0.4 + DOWN * 1.0,
                        fill_color=COLOR_PIVOTE, fill_opacity=0.4, stroke_color=COLOR_PIVOTE)
        return VGroup(ejes, plano)

    def panel_4d(self):
        caja = Square(side_length=2.6, color=COLOR_SECUNDARIO)
        return VGroup(caja, MathTex(r"?", font_size=90, color=COLOR_SECUNDARIO).move_to(caja))


class SistemasHomogeneos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 10 · Parte 3", "Sistemas homogéneos")
        titulo = self.encabezado("Todos los términos independientes son 0")
        ejemplo = sistema_con_llave(("x + 2y - z", "=", "0"), ("3x - y + z", "=", "0"), font_size=48, colores=False).shift(UP * 1.4)
        self.decir("Un sistema es homogéneo si todos sus términos independientes son cero.")
        self.play(Write(ejemplo))
        trivial = VGroup(
            MathTex(r"(0, 0, 0):\quad 0 + 0 - 0 = 0\ \checkmark \qquad 0 - 0 + 0 = 0\ \checkmark", font_size=40, color=COLOR_SOLUCION),
            Tex(r"Sustituir todas las incógnitas por 0 siempre da $0 = 0$:", font_size=38),
            Tex(r"un sistema homogéneo \textbf{siempre} tiene la \textbf{solución trivial} $(0, \dots, 0)$.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Nunca es incompatible: tiene solo la trivial o infinitas soluciones.", font_size=38),
        ).arrange(DOWN, buff=0.4).next_to(ejemplo, DOWN, buff=0.6)
        self.decir("Poner todas las incógnitas a cero siempre funciona: cero igual a cero en cada ecuación. Es la solución trivial. Por eso un sistema homogéneo nunca es incompatible: tiene solo la trivial, o infinitas soluciones.")
        for t in trivial:
            self.play(FadeIn(t))
            self.wait(2)
        self.limpiar(titulo)

        # Geometría: siempre pasan por el origen.
        titulo = self.cambiar_encabezado(titulo, "Rectas que pasan por el origen")
        paneles = VGroup()
        for coef, izquierdas, texto, color in (
            ([(1, 1, 0), (1, -1, 0)], ("x + y", "x - y"), "solo la trivial (0, 0)", COLOR_SOLUCION),
            ([(1, 2, 0), (3, 6, 0)], ("x + 2y", "3x + 6y"), "infinitas: (-2t, t)", COLOR_LIBRE),
        ):
            mini = ejes_iguales((-3, 3), (-3, 3), unidad=0.7)
            sistema = sistema_con_llave(*[(izq, "=", "0") for izq in izquierdas], font_size=36)
            paneles.add(VGroup(sistema, mini, rectas(mini, coef, discontinuas=(1,) if coef[1][0] == 3 else ()),
                               Dot(mini.c2p(0, 0), color=COLOR_PIVOTE), Text(texto, font_size=TAM_NOTA, color=color)))
        self.decir("Con dos incógnitas, sus rectas pasan por el origen. O solo se cortan ahí, y la única solución es la trivial; o coinciden, y hay infinitas soluciones.")
        for panel in paneles:
            panel[0].next_to(panel[1], UP, buff=0.2)
            panel[4].next_to(panel[1], DOWN, buff=0.2)
        paneles.arrange(RIGHT, buff=1.2).shift(DOWN * 0.1)
        for panel in paneles:
            self.play(FadeIn(panel[0]), Create(panel[1]))
            self.play(Create(panel[2]), FadeIn(panel[3]))
            self.play(FadeIn(panel[4]))
            self.wait(1.5)
        self.limpiar(titulo)

        # Sumas y múltiplos de soluciones.
        titulo = self.cambiar_encabezado(titulo, "Una propiedad especial: sumar soluciones")
        bloque = VGroup(
            MathTex(r"x + 2y = 0:\qquad u = (-2, 1),\quad v = (4, -2)", font_size=42),
            MathTex(r"u + v = (2, -1):\ \ 2 + 2(-1) = 0\ \checkmark \qquad 3u = (-6, 3):\ \ -6 + 6 = 0\ \checkmark", font_size=40, color=COLOR_SOLUCION),
            MathTex(r"a(u_1 + v_1) + b(u_2 + v_2) = (a u_1 + b u_2) + (a v_1 + b v_2) = 0 + 0 = 0", font_size=40),
            Tex(r"En un sistema homogéneo, la suma de soluciones y cualquier múltiplo de una solución son soluciones.", font_size=34, color=COLOR_PIVOTE),
            MathTex(r"\text{Falla si } b \neq 0:\ x + y = 2,\ (2, 0) + (0, 2) = (2, 2) \text{ y } 2 + 2 \neq 2", font_size=38, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.45)
        self.decir("Y tienen una propiedad especial. En equis más dos ye igual a cero, u y uve son soluciones. Su suma también lo es, y tres por u también. La razón: la suma de las dos cuentas da cero más cero. En un sistema homogéneo, la suma de soluciones y los múltiplos de una solución son soluciones. Si el término independiente no es cero, falla.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)
        self.pie(
            "Este conjunto de soluciones tendrá nombre propio: el NÚCLEO (Lección 45). Al sistema con los mismos\n"
            "coeficientes y b = 0 se le llama «homogéneo asociado»; será clave en la Lección 47.",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F03-N2-04",
            VGroup(
                sistema_con_llave(("x + y - z", "=", "0"), ("2x + 3y - z", "=", "0"), font_size=44, colores=False),
                Tex(r"a) Comprueba que $(2, -1, 1)$ es solución. \ b) Sin hacer cuentas nuevas, da otras dos soluciones.", font_size=36),
                Tex(r"c) ¿Puede este sistema ser incompatible? ¿Por qué?", font_size=36),
            ).arrange(DOWN, buff=0.45),
        )
        self.resumen(
            [
                "Homogéneo: todos los términos independientes valen 0.",
                "Siempre tiene la solución trivial: nunca es incompatible.",
                "Sumas y múltiplos de soluciones vuelven a ser soluciones.",
            ],
            "Lección 11 — clasificación de los sistemas.",
        )
