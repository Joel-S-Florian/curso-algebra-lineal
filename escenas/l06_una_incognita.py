"""Lección 6 — Ecuaciones lineales con una incógnita: ax = b.

Escenas (un video cada una):
    DespejeJustificado, LosTresCasos

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l06_una_incognita.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ejes_iguales, recta_recortada, resolver_paso_a_paso  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def decimal(v: float) -> str:
    """Número con un decimal como mucho (2 -> "2", 0.5 -> "0.5")."""
    v = round(v, 1) + 0.0  # + 0.0 convierte -0.0 en 0.0
    return str(int(v)) if v == int(v) else str(v)


class DespejeJustificado(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 6 · Parte 1", "Resolver una ecuación lineal\ncon una incógnita")

        titulo = self.encabezado("Un primer ejemplo, justificando cada paso")
        self.decir("Resolvamos tres equis más cuatro igual a diez, justificando cada paso. Restamos cuatro en ambos lados: regla uno. Queda tres equis igual a seis. Dividimos entre tres, que no es cero: regla dos. Equis igual a dos.")
        bloque = resolver_paso_a_paso(
            self,
            [("3x + 4", "10"), ("3x", "6"), ("x", "2")],
            ["restar 4 en ambos lados (regla 1)", "dividir entre 3, que no es 0 (regla 2)"],
        )
        self.play(bloque.animate.shift(UP * 1))
        verificacion = MathTex(r"3\cdot(2) + 4 = 10\ \checkmark", font_size=44, color=COLOR_SOLUCION).next_to(bloque, DOWN, buff=0.7)
        self.decir("Y verificamos: tres por dos, más cuatro, diez. Correcto.")
        self.play(Write(verificacion))
        self.decir("Cada paso se puede deshacer, así que la ecuación final tiene exactamente las mismas soluciones que la inicial.")
        self.pie("Cada paso es reversible: la ecuación final tiene exactamente las mismas soluciones que la inicial.", espera=3)
        self.limpiar(titulo)

        # Receta general.
        titulo = self.cambiar_encabezado(titulo, "Receta: llegar a la forma  ax = b")
        receta = VGroup(
            Text("1.  Quitar paréntesis (distributiva) y denominadores\n     (multiplicando ambos lados por un número no nulo).", font_size=TAM_NOTA + 2, line_spacing=1.1),
            Text("2.  Términos con x a un lado y números al otro (regla 1).", font_size=TAM_NOTA + 2),
            Text("3.  Agrupar: queda  a·x = b.", font_size=TAM_NOTA + 2),
            Text("4.  Si a no es 0, dividir entre a (regla 2):  x = b / a.", font_size=TAM_NOTA + 2, color=COLOR_PIVOTE),
            Text("5.  Verificar en la ecuación ORIGINAL.", font_size=TAM_NOTA + 2, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        self.decir("Esta es la receta para cualquier ecuación lineal con una incógnita. Uno: quitar paréntesis y denominadores. Dos: las equis a un lado y los números al otro. Tres: agrupar, hasta llegar a a equis igual a be. Cuatro: si a no es cero, dividir entre a. Y cinco: verificar en la ecuación original.")
        for r in receta:
            self.play(FadeIn(r, shift=RIGHT * 0.2))
            self.wait(1.2)
        self.decir("Fíjate en el paso cuatro: solo se puede dividir entre a si a no es cero. ¿Y si a vale cero? Lo veremos en el siguiente video.")
        self.pie("El paso 4 tiene una condición: ¿y si a vale 0? Lo veremos en el siguiente video.", espera=3)
        self.limpiar(titulo)

        # Con fracciones.
        titulo = self.cambiar_encabezado(titulo, "Con fracciones")
        self.decir("Con fracciones: dos tercios de equis menos uno, igual a equis medios más un tercio. Multiplicamos ambos lados por seis, y desaparecen todos los denominadores: cuatro equis menos seis igual a tres equis más dos. Restamos tres equis y sumamos seis: equis igual a ocho.")
        bloque = resolver_paso_a_paso(
            self,
            [(r"\tfrac{2}{3}x - 1", r"\tfrac{x}{2} + \tfrac{1}{3}"), ("4x - 6", "3x + 2"), ("x", "8")],
            ["multiplicar ambos lados por 6", "restar 3x y sumar 6 en ambos lados"],
        )
        self.play(bloque.animate.shift(UP * 1))
        verificacion = MathTex(
            r"\tfrac{2}{3}\cdot 8 - 1 = \tfrac{13}{3} \qquad \tfrac{8}{2} + \tfrac{1}{3} = \tfrac{13}{3}\ \checkmark",
            font_size=42,
            color=COLOR_SOLUCION,
        ).next_to(bloque, DOWN, buff=0.7)
        self.decir("Verificamos: los dos lados valen trece tercios.")
        self.play(Write(verificacion))
        self.decir("¿Por qué seis? Porque es múltiplo de tres y de dos.")
        self.pie("¿Por qué 6? Es múltiplo de 3 y de 2: al multiplicar, desaparecen todos los denominadores.", espera=4)
        self.limpiar(titulo)

        # Con paréntesis.
        titulo = self.cambiar_encabezado(titulo, "Con paréntesis")
        self.decir("Con paréntesis, cuidado con los signos. Cinco menos dos por equis menos tres: el menos dos multiplica a equis y a menos tres, y menos dos por menos tres es más seis. Queda once menos dos equis igual a tres equis más uno. Sumamos dos equis y restamos uno: diez igual a cinco equis. Dividimos entre cinco: equis igual a dos.")
        bloque = resolver_paso_a_paso(
            self,
            [("5 - 2(x - 3)", "3(x + 1) - 2"), ("11 - 2x", "3x + 1"), ("10", "5x"), ("x", "2")],
            ["distributiva (¡el -2 multiplica al -3!)", "sumar 2x y restar 1", "dividir entre 5"],
            font_size=42,
        )
        self.play(bloque.animate.shift(UP * 0.8))
        verificacion = MathTex(r"5 - 2(-1) = 7 \qquad 3(3) - 2 = 7\ \checkmark", font_size=42, color=COLOR_SOLUCION)
        verificacion.next_to(bloque, DOWN, buff=0.6)
        self.decir("Verificamos: los dos lados valen siete.")
        self.play(Write(verificacion))
        self.wait(3)

        self.ejercicio_propuesto(
            "F01-N2-01",
            VGroup(
                MathTex(r"4(x - 1) - (2x + 3) = \frac{x}{2}", font_size=56),
                Text("Resuélvela justificando cada paso y verifica.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Toda ecuación lineal con una incógnita se lleva a la forma ax = b.",
                "Cada paso usa la regla 1 o la regla 2 de la Lección 2.",
                "Si a no es 0, la única solución es x = b / a.",
                "Siempre se verifica en la ecuación original.",
            ],
            "qué pasa cuando a = 0.",
            voz="En resumen: toda ecuación lineal con una incógnita se lleva a la forma a equis igual a be. Cada paso usa la regla uno o la regla dos de la lección dos. Si a no es cero, la única solución es be entre a. Y siempre se verifica en la ecuación original. Siguiente: qué pasa cuando a es cero.",
        )


class LosTresCasos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 6 · Parte 2", "ax = b: una, infinitas o ninguna solución")
        titulo = self.encabezado("Resolver ax = b es cortar dos rectas")
        sistema = ejes_iguales((-4, 4), (-3, 5), unidad=0.65).to_edge(LEFT, buff=0.7).shift(DOWN * 0.2)
        a, b = ValueTracker(2), ValueTracker(4)

        def caso():
            if abs(a.get_value()) > 1e-3:
                return "una"
            return "todas" if abs(b.get_value()) < 1e-3 else "ninguna"

        izquierda = always_redraw(lambda: recta_recortada(sistema, a.get_value(), 0, color=COLOR_COEFICIENTE, stroke_width=5))
        derecha = always_redraw(lambda: recta_recortada(sistema, 0, b.get_value(), color=COLOR_TERMINO_INDEP, stroke_width=3))

        def solucion():
            if caso() == "una":
                x = b.get_value() / a.get_value()
                if not sistema.x_range[0] <= x <= sistema.x_range[1]:
                    return VGroup()
                punto = Dot(sistema.c2p(x, b.get_value()), color=COLOR_PIVOTE, radius=0.09)
                caida = DashedLine(sistema.c2p(x, b.get_value()), sistema.c2p(x, 0), color=COLOR_PIVOTE)
                return VGroup(punto, caida, Dot(sistema.c2p(x, 0), color=COLOR_SOLUCION, radius=0.11))
            if caso() == "todas":
                return Line(sistema.c2p(-4, 0), sistema.c2p(4, 0), color=COLOR_SOLUCION, stroke_width=10)
            return VGroup()

        def lectura():
            ecuacion = MathTex(rf"{decimal(a.get_value())}\,x = {decimal(b.get_value())}", font_size=54)
            texto = {
                "una": (r"una solución: x = b/a", COLOR_SOLUCION),
                "todas": (r"infinitas: todo x es solución", COLOR_SOLUCION),
                "ninguna": (r"ninguna solución", COLOR_ERROR),
            }[caso()]
            return VGroup(ecuacion, Text(texto[0], font_size=TAM_TEXTO, color=texto[1])).arrange(DOWN, buff=0.4).to_edge(RIGHT, buff=1).shift(UP * 1.5)

        leyenda = VGroup(
            MathTex(r"y = a\,x", color=COLOR_COEFICIENTE, font_size=40),
            MathTex(r"y = b", color=COLOR_TERMINO_INDEP, font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=1.2).shift(DOWN * 1.2)
        self.decir("Resolver a equis igual a be es buscar dónde la recta ye igual a a equis alcanza la altura be.")
        self.play(Create(sistema))
        self.play(Create(izquierda), Create(derecha), FadeIn(leyenda))
        marca, panel = always_redraw(solucion), always_redraw(lectura)
        self.play(FadeIn(marca), FadeIn(panel))
        self.pie("Las soluciones de ax = b son los x donde la recta y = ax alcanza la altura b.", espera=3)

        # Recorrido por los casos.
        self.decir("Mientras la recta esté inclinada, corta a la horizontal exactamente una vez, aunque a sea muy pequeño. Pero si a vale cero, la recta ye igual a cero por equis es el eje horizontal. Si be es uno, nunca se cortan: ninguna solución. Si be también es cero, coinciden: todos los equis son solución.")
        for valor_a, valor_b, nota in (
            (2, -2, "Con a distinto de 0 la recta inclinada siempre corta a la horizontal: una solución."),
            (0.5, 1, "Aunque a sea pequeño, mientras no sea 0 hay un único corte."),
            (0, 1, "Si a = 0, la recta y = 0·x es el eje: paralela a y = 1. No hay corte."),
            (0, 0, "Si además b = 0, las dos rectas coinciden: TODOS los x son solución."),
        ):
            self.play(a.animate.set_value(valor_a), b.animate.set_value(valor_b), run_time=2)
            self.pie(nota, espera=3)
        self.limpiar(titulo)

        # Tabla resumen.
        titulo = self.cambiar_encabezado(titulo, "Los tres casos")
        filas = [
            (r"a \neq 0", r"x = \dfrac{b}{a}", "una solución", COLOR_SOLUCION),
            (r"a = 0,\ b = 0", r"0x = 0", "infinitas: todos los reales", COLOR_LIBRE),
            (r"a = 0,\ b \neq 0", r"0x = b", "ninguna (conjunto vacío)", COLOR_ERROR),
        ]
        tabla = VGroup()
        for cond, ec, texto, color in filas:
            tabla.add(MathTex(cond, font_size=44), MathTex(ec, font_size=44), Text(texto, font_size=TAM_TEXTO, color=color))
        tabla.arrange_in_grid(rows=3, cols=3, buff=(1.2, 0.7), col_alignments="lcl")
        self.decir("Una solución si a no es cero. Infinitas si a y be son cero. Ninguna si a es cero y be no.")
        for i in range(3):
            self.play(*[FadeIn(m) for m in tabla[3 * i: 3 * i + 3]])
            self.wait(1.5)
        self.decir("Una, infinitas o ninguna: son exactamente los mismos tres casos que tendrán los sistemas de ecuaciones.")
        self.pie("Una, infinitas o ninguna: los mismos tres casos que tendrán los sistemas (Lección 11).", espera=4)
        self.limpiar(titulo)

        # Con un parámetro.
        titulo = self.cambiar_encabezado(titulo, "Cuando el coeficiente tiene un parámetro")
        ecuacion = MathTex(r"(m - 2)\,x = m - 2", font_size=56).shift(UP * 1.8)
        ecuacion[0][1].set_color(COLOR_LIBRE)
        ecuacion[0][7].set_color(COLOR_LIBRE)
        self.decir("Cuando el coeficiente depende de un parámetro, hay que separar casos. Por ejemplo, eme menos dos, por equis, igual a eme menos dos.")
        self.play(Write(ecuacion))
        ramas = VGroup(
            Tex(r"Si $m \neq 2$: \ $m - 2 \neq 0$, se puede dividir: \ $x = 1$ \ (una solución).", font_size=40, color=COLOR_SOLUCION),
            Tex(r"Si $m = 2$: \ queda $0x = 0$: \ todo $x$ es solución.", font_size=40, color=COLOR_LIBRE),
            Tex(r"Error: dividir entre $m - 2$ sin separar el caso $m = 2$.", font_size=40, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(ecuacion, DOWN, buff=0.8)
        self.decir("Si eme no es dos, se puede dividir, y equis vale uno. Si eme es dos, queda cero igual a cero, y todo equis es solución. Dividir sin separar ese caso es el error más común.")
        for r in ramas:
            self.play(FadeIn(r))
            self.wait(2.5)
        self.pie("Discutir una ecuación es estudiar por separado los valores del parámetro que anulan el coeficiente.", espera=4)

        self.ejercicio_propuesto(
            "F01-N4-02",
            VGroup(
                Text("Discute según el valor de k:", font_size=TAM_TEXTO),
                MathTex(r"(k^2 - 1)\,x = k + 1", font_size=56),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "a distinto de 0: una solución, x = b/a.",
                "a = 0 y b = 0: infinitas (todo número real).",
                "a = 0 y b distinto de 0: ninguna.",
                "Con parámetros, separar los casos que anulan el coeficiente.",
            ],
            "Lección 7 — ecuaciones con dos y tres incógnitas.",
            voz="En resumen: si a es distinto de cero, hay una solución, be entre a. Si a y be son cero, infinitas: todo número real. Si a es cero y be no, ninguna. Y con parámetros, hay que separar los casos que anulan el coeficiente. Siguiente: lección siete, ecuaciones con dos y tres incógnitas.",
        )
