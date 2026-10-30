"""Lección 8 — Sistemas de dos ecuaciones con dos incógnitas.

Escenas (un video cada una):
    QueEsUnSistema, RectasQueSeCortan, RectasParalelas, RectasCoincidentes

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l08_sistemas_2x2.py -a

Lección piloto de la narración: cada bloque `with self.narrar(...)` dura lo que su frase.
En la voz, los números y las letras van escritos como se dicen ("equis", "tres, dos").
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ejes_iguales, sistema_con_llave  # noqa: E402
from curso.componentes import rectas_de_sistema as rectas  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

PAUSA = "Pausa el video e inténtalo; la solución está en el banco de ejercicios."


class QueEsUnSistema(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 8 · Parte 1", "¿Qué es un sistema de ecuaciones?",
                             voz="Lección ocho, primera parte: ¿qué es un sistema de ecuaciones?")
        titulo = self.encabezado("Un problema con dos condiciones")
        problema = Text("«Dos números suman 5 y su diferencia es 1. ¿Cuáles son?»", font_size=TAM_TEXTO).shift(UP * 1.8)
        with self.narrar("Dos números suman cinco, y su diferencia es uno. ¿Cuáles son?"):
            self.play(FadeIn(problema))
        sistema = sistema_con_llave(("x + y", "=", "5"), ("x - y", "=", "1"))
        with self.narrar("Cada condición es una ecuación: equis más ye igual a cinco, y equis menos ye igual a uno. "
                         "Las dos deben cumplirse a la vez: eso es un sistema de ecuaciones."):
            self.play(Write(sistema))
            self.pie("Las dos condiciones deben cumplirse A LA VEZ: eso es un sistema de ecuaciones.")
        definiciones = VGroup(
            Tex(r"\textbf{Sistema}: conjunto de ecuaciones que deben cumplirse simultáneamente.", font_size=36),
            Tex(r"\textbf{Solución}: un valor para cada incógnita que cumple \textbf{todas} las ecuaciones.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(sistema, DOWN, buff=0.8)
        frases = (
            "Un sistema es un conjunto de ecuaciones que deben cumplirse simultáneamente.",
            "Y una solución es un valor para cada incógnita que cumple todas las ecuaciones, no solo una.",
        )
        for d, frase in zip(definiciones, frases):
            with self.narrar(frase):
                self.play(FadeIn(d))
        self.wait(1)
        self.limpiar(titulo)

        # Probar candidatos.
        titulo = self.cambiar_encabezado(titulo, "Probar candidatos: hay que mirar TODAS las ecuaciones")
        sistema = sistema_con_llave(("x + y", "=", "5"), ("x - y", "=", "1"), font_size=42).to_edge(LEFT, buff=1).shift(UP * 1.5)
        cabecera = VGroup(*[MathTex(t, font_size=38) for t in ("(x, y)", "x + y", "x - y", r"\text{¿solución?}")])
        filas = [cabecera]
        for (x, y) in ((4, 1), (2, 3), (3, 2)):
            ok1, ok2 = x + y == 5, x - y == 1
            fila = VGroup(
                MathTex(f"({x}, {y})", font_size=38),
                MathTex(rf"{x + y}\ " + (r"\checkmark" if ok1 else r"\times"), font_size=38, color=COLOR_SOLUCION if ok1 else COLOR_ERROR),
                MathTex(rf"{x - y}\ " + (r"\checkmark" if ok2 else r"\times"), font_size=38, color=COLOR_SOLUCION if ok2 else COLOR_ERROR),
                Text("sí" if ok1 and ok2 else "no", font_size=TAM_TEXTO, color=COLOR_SOLUCION if ok1 and ok2 else COLOR_ERROR),
            )
            filas.append(fila)
        tabla = VGroup(*[m for f in filas for m in f]).arrange_in_grid(rows=4, cols=4, buff=(0.9, 0.45))
        tabla.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.3)
        with self.narrar("Probemos algunos candidatos. Para cada pareja calculamos equis más ye, y equis menos ye."):
            self.play(FadeIn(sistema))
            self.play(FadeIn(VGroup(*tabla[:4])))
        frases = (
            "Cuatro, uno: la suma da cinco, bien. Pero la diferencia da tres, no uno. No es solución.",
            "Dos, tres: la suma da cinco, pero la diferencia da menos uno. Tampoco.",
            "Tres, dos: la suma da cinco y la diferencia da uno. Cumple las dos: esta sí es la solución.",
        )
        for k, frase in zip(range(1, 4), frases):
            with self.narrar(frase):
                for m in tabla[4 * k: 4 * k + 4]:
                    self.play(FadeIn(m), run_time=0.5)
        with self.narrar("Cuidado: cuatro, uno cumple la primera ecuación, pero no la segunda. "
                         "Un punto que cumple solo una de las ecuaciones no es solución del sistema."):
            self.pie("(4, 1) cumple la primera pero no la segunda: NO es solución del sistema.")
        self.wait(1)
        self.limpiar(titulo)

        # Geometría.
        titulo = self.cambiar_encabezado(titulo, "Geométricamente: el punto común de dos rectas")
        plano = ejes_iguales((-1, 6), (-2, 6), unidad=0.6).to_edge(LEFT, buff=0.8).shift(UP * 0.1)
        lineas = rectas(plano, [(1, 1, 5), (1, -1, 1)])
        leyenda = sistema_con_llave(("x + y", "=", "5"), ("x - y", "=", "1"), font_size=42).to_edge(RIGHT, buff=1.2).shift(UP * 1.5)
        with self.narrar("Ahora veámoslo en el plano. Cada ecuación con dos incógnitas es una recta."):
            self.play(Create(plano), FadeIn(leyenda))
            self.play(Create(lineas[0]))
            self.play(Create(lineas[1]))
        punto = Dot(plano.c2p(3, 2), color=COLOR_PIVOTE, radius=0.1)
        conjunto = MathTex(r"S = S_1 \cap S_2 = \{(3, 2)\}", font_size=40, color=COLOR_PIVOTE).next_to(leyenda, DOWN, buff=0.8).to_edge(RIGHT, buff=0.7)
        with self.narrar("Las dos rectas se cortan en el punto tres, dos: el único punto que está en las dos. "
                         "El conjunto solución del sistema es la intersección de los conjuntos solución de cada ecuación."):
            self.play(FadeIn(punto, scale=3), Flash(punto, color=COLOR_PIVOTE))
            self.play(Write(conjunto))
        with self.narrar("Cómo encontrar este punto sin probar ni dibujar lo veremos en las lecciones trece a quince."):
            self.pie(
                "Cada ecuación es una recta; el sistema pide estar en las dos: su intersección (Lección 4).\n"
                "Cómo encontrar el punto sin probar ni dibujar: Lecciones 13 a 15.",
            )
        self.wait(2)

        self.ejercicio_propuesto(
            "F03-N1-01",
            VGroup(
                Tex(r"¿Cuáles de $(1, 2)$, $(2, 0)$ y $(4, 3)$ son solución del sistema?", font_size=40),
                sistema_con_llave(("2x + y", "=", "4"), ("x - 3y", "=", "-5"), font_size=44),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: ¿cuáles de estos tres puntos son solución del sistema? " + PAUSA,
            espera=4,
        )
        self.resumen(
            [
                "Un sistema es un conjunto de ecuaciones que se cumplen a la vez.",
                "Una solución debe cumplir TODAS las ecuaciones.",
                "Con dos incógnitas: las soluciones son los puntos comunes de las rectas.",
            ],
            "cuándo dos rectas se cortan en un punto.",
            voz="En resumen: un sistema es un conjunto de ecuaciones que se cumplen a la vez. "
                "Una solución debe cumplir todas las ecuaciones. Y con dos incógnitas, las soluciones son los puntos comunes de las rectas. "
                "En el siguiente video: cuándo dos rectas se cortan en un único punto.",
            espera=2,
        )


class RectasQueSeCortan(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 8 · Parte 2", "Rectas que se cortan: una solución",
                             voz="Segunda parte: rectas que se cortan.")
        titulo = self.encabezado("Pendientes distintas: un único punto común")
        plano = ejes_iguales((-1, 5), (-2, 5), unidad=0.7).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        leyenda = sistema_con_llave(("2x - y", "=", "1"), ("x + 3y", "=", "11"), font_size=44).to_edge(RIGHT, buff=1.4).shift(UP * 2)
        lineas = rectas(plano, [(2, -1, 1), (1, 3, 11)])
        punto = Dot(plano.c2p(2, 3), color=COLOR_PIVOTE, radius=0.1)
        with self.narrar("Tomemos el sistema: dos equis menos ye igual a uno, y equis más tres ye igual a once."):
            self.play(Create(plano), FadeIn(leyenda))
        with self.narrar("Cada ecuación es una recta, y estas dos se cortan en un punto: el dos, tres."):
            self.play(Create(lineas[0]), Create(lineas[1]))
            self.play(FadeIn(punto, scale=3))
        detalles = VGroup(
            MathTex(r"y = 2x - 1:\ \text{pendiente } 2", font_size=36, color=COLORES_ECUACIONES[0]),
            MathTex(r"y = -\tfrac13 x + \tfrac{11}{3}:\ \text{pendiente } -\tfrac13", font_size=36, color=COLORES_ECUACIONES[1]),
            MathTex(r"(2, 3):\ \ 4 - 3 = 1\ \checkmark \quad 2 + 9 = 11\ \checkmark", font_size=36, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(leyenda, DOWN, buff=0.6).to_edge(RIGHT, buff=0.6)
        frases = (
            "Despejando ye, la primera recta tiene pendiente dos.",
            "La segunda tiene pendiente menos un tercio.",
            "Verificamos el punto dos, tres en las dos ecuaciones: cuatro menos tres es uno, y dos más nueve es once. Correcto.",
        )
        for d, frase in zip(detalles, frases):
            with self.narrar(frase):
                self.play(FadeIn(d))
        with self.narrar("Dos rectas con pendientes distintas se cortan exactamente en un punto: el sistema tiene una única solución."):
            self.pie("Dos rectas con pendientes distintas se cortan exactamente en un punto: el sistema tiene UNA solución.")
        self.play(*[FadeOut(m) for m in (lineas[1], detalles, leyenda)])

        # Girar la segunda recta alrededor del punto: el corte sigue siendo único.
        pendiente = ValueTracker(-1 / 3)
        segunda = always_redraw(
            lambda: plano.plot(
                lambda x: 3 + pendiente.get_value() * (x - 2),
                x_range=self.ventana(plano, pendiente.get_value()),
                color=COLORES_ECUACIONES[1],
                stroke_width=4,
            )
        )
        self.add(segunda)
        self.bring_to_front(punto)
        with self.narrar("Giremos la segunda recta alrededor del punto. "
                         "Mientras su pendiente sea distinta de la de la primera, el punto de corte sigue siendo único."):
            for valor in (-2, 0, 0.8, -0.5):
                self.play(pendiente.animate.set_value(valor), run_time=1.5)
            self.pie("Mientras las pendientes sean distintas, el punto de corte es único.")
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Criterio con los coeficientes")
        bloque = VGroup(
            MathTex(r"\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}", font_size=52),
            Tex(r"Pendientes distintas $\Longleftrightarrow$ los pares $(a_1, b_1)$ y $(a_2, b_2)$ \textbf{no} son proporcionales.", font_size=38),
            MathTex(r"(2, -1) \text{ y } (1, 3):\ \ \text{no existe } k \text{ con } (1, 3) = k\,(2, -1)", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.6)
        frases = (
            "En general, escribimos el sistema con coeficientes a, be y ce.",
            "Las pendientes son distintas exactamente cuando los pares de coeficientes de las incógnitas no son proporcionales.",
            "En nuestro ejemplo, ningún número ka multiplicado por el par dos, menos uno, da el par uno, tres.",
        )
        for b, frase in zip(bloque, frases):
            with self.narrar(frase):
                self.play(FadeIn(b))
        with self.narrar("Proporcionales quiere decir que uno es un múltiplo del otro. Este criterio no necesita dibujar."):
            self.pie("Proporcionales quiere decir que uno es un múltiplo del otro. Este criterio no necesita dibujar.")
        self.wait(2)

        self.ejercicio_propuesto(
            "F03-N2-01",
            VGroup(
                Tex(r"Sin resolver, ¿se cortan en un único punto?", font_size=40),
                MathTex(r"\text{a) } \begin{cases} 3x - 2y = 1 \\ 6x - 4y = 5 \end{cases} \qquad \text{b) } \begin{cases} x + 4y = 2 \\ 2x - y = 7 \end{cases}", font_size=44),
                Tex(r"En el caso b), halla el punto y verifícalo.", font_size=40),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: sin resolver, decide si estas rectas se cortan en un único punto. "
                "En el caso be, halla el punto y verifícalo. " + PAUSA,
            espera=4,
        )
        self.resumen(
            [
                "Rectas con pendientes distintas: un único punto común (una solución).",
                "Criterio: (a₁, b₁) y (a₂, b₂) no proporcionales.",
                "Toda solución se verifica en las dos ecuaciones.",
            ],
            "rectas paralelas.",
            voz="En resumen: rectas con pendientes distintas tienen un único punto común, y el sistema tiene una solución. "
                "El criterio: los pares de coeficientes no son proporcionales. Y toda solución se verifica en las dos ecuaciones. "
                "En el siguiente video: rectas paralelas.",
            espera=2,
        )

    @staticmethod
    def ventana(plano: Axes, m: float):
        """Intervalo de x en el que y = 3 + m(x - 2) queda dentro de los ejes."""
        x0, x1 = plano.x_range[:2]
        y0, y1 = plano.y_range[:2]
        if abs(m) > 1e-6:
            cortes = sorted((2 + (y0 - 3) / m, 2 + (y1 - 3) / m))
            x0, x1 = max(x0, cortes[0]), min(x1, cortes[1])
        return [x0, x1]


class RectasParalelas(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 8 · Parte 3", "Rectas paralelas: ninguna solución",
                             voz="Tercera parte: rectas paralelas.")
        titulo = self.encabezado("Misma pendiente, distinta altura")
        plano = ejes_iguales((-1, 6), (-1, 6), unidad=0.65).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        leyenda = sistema_con_llave(("x + y", "=", "5"), ("2x + 2y", "=", "4"), font_size=44).to_edge(RIGHT, buff=1.4).shift(UP * 2)
        lineas = rectas(plano, [(1, 1, 5), (2, 2, 4)])
        with self.narrar("Ahora el sistema: equis más ye igual a cinco, y dos equis más dos ye igual a cuatro."):
            self.play(Create(plano), FadeIn(leyenda))
        with self.narrar("Las dos rectas tienen la misma pendiente, pero distinta altura: son paralelas y nunca se cortan. "
                         "No hay ningún punto común."):
            self.play(Create(lineas[0]), Create(lineas[1]))
            self.pie("Las rectas no se cortan nunca: no hay ningún punto común.")
        algebra = VGroup(
            MathTex(r"2x + 2y = 4 \;\Leftrightarrow\; x + y = 2", font_size=40),
            MathTex(r"x + y = 5 \ \text{ y } \ x + y = 2", font_size=40),
            MathTex(r"\Rightarrow\ 5 = 2", font_size=46, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.4).next_to(leyenda, DOWN, buff=0.6)
        notas = [
            "Dividimos la 2.ª entre 2 (regla 2).",
            "El mismo número x + y no puede valer 5 y 2 a la vez.",
            "Contradicción: el sistema no tiene solución.",
        ]
        frases = (
            "Algebraicamente: dividimos la segunda ecuación entre dos, y queda equis más ye igual a dos.",
            "Entonces el mismo número, equis más ye, tendría que valer cinco y dos a la vez.",
            "Eso lleva a cinco igual a dos: una contradicción. El sistema no tiene solución.",
        )
        for a, nota, frase in zip(algebra, notas, frases):
            with self.narrar(frase):
                self.play(Write(a))
                self.pie(nota)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo reconocerlo en los coeficientes")
        bloque = VGroup(
            MathTex(r"(a_2, b_2) = (2, 2) = 2\cdot(1, 1) = 2\,(a_1, b_1)", font_size=44),
            MathTex(r"c_2 = 4 \ \neq \ 2\cdot 5 = 2\,c_1", font_size=44, color=COLOR_ERROR),
            Tex(r"Coeficientes proporcionales pero términos independientes \textbf{no}: rectas paralelas, \textbf{ninguna} solución.", font_size=36),
        ).arrange(DOWN, buff=0.6)
        frases = (
            "En los coeficientes: el par dos, dos es el doble del par uno, uno.",
            "Pero el término independiente cuatro no es el doble de cinco.",
            "Coeficientes proporcionales, pero términos independientes no: rectas paralelas, ninguna solución.",
        )
        for b, frase in zip(bloque, frases):
            with self.narrar(frase):
                self.play(FadeIn(b))
        with self.narrar("El sistema es contradictorio: las dos ecuaciones piden cosas incompatibles."):
            self.pie("El sistema es contradictorio: las dos ecuaciones piden cosas incompatibles.")
        self.wait(2)

        self.ejercicio_propuesto(
            "F03-N2-02",
            VGroup(
                Tex(r"¿Para qué valores de $c$ el sistema no tiene solución? ¿Y para cuáles tiene infinitas?", font_size=38),
                MathTex(r"\begin{cases} x - 2y = 3 \\ -2x + 4y = c \end{cases}", font_size=50),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: ¿para qué valores de ce este sistema no tiene solución? ¿Y para cuáles tiene infinitas? " + PAUSA,
            espera=4,
        )
        self.resumen(
            [
                "Rectas paralelas (distintas): ningún punto común, ninguna solución.",
                "Se detecta al llegar a una igualdad falsa, como 5 = 2.",
                "En los coeficientes: (a, b) proporcionales, c no.",
            ],
            "rectas coincidentes.",
            voz="En resumen: dos rectas paralelas distintas no tienen ningún punto común, y el sistema no tiene solución. "
                "Se detecta al llegar a una igualdad falsa, como cinco igual a dos. "
                "En los coeficientes: los de las incógnitas son proporcionales, pero los términos independientes no. "
                "En el siguiente video: rectas coincidentes.",
            espera=2,
        )


class RectasCoincidentes(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 8 · Parte 4", "Rectas coincidentes: infinitas soluciones",
                             voz="Cuarta parte: rectas coincidentes.")
        titulo = self.encabezado("Dos ecuaciones, la misma recta")
        plano = ejes_iguales((-1, 6), (-1, 6), unidad=0.65).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)
        leyenda = sistema_con_llave(("x + y", "=", "5"), ("2x + 2y", "=", "10"), font_size=44).to_edge(RIGHT, buff=1.4).shift(UP * 2)
        lineas = rectas(plano, [(1, 1, 5), (2, 2, 10)], discontinuas=(1,))
        with self.narrar("Ahora: equis más ye igual a cinco, y dos equis más dos ye igual a diez."):
            self.play(Create(plano), FadeIn(leyenda))
            self.play(Create(lineas[0]))
        with self.narrar("Al dibujar la segunda recta, cae exactamente encima de la primera."):
            self.play(Create(lineas[1]))
        textos = VGroup(
            MathTex(r"(2, 2 \mid 10) = 2\cdot(1, 1 \mid 5)", font_size=42),
            Tex(r"La segunda ecuación\\no añade nada:\\es \textbf{redundante}.", font_size=38),
            MathTex(r"(x, y) = (5 - t,\ t)", font_size=46, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.5).next_to(leyenda, DOWN, buff=0.6)
        frases = (
            "La segunda ecuación entera, coeficientes y término independiente, es la primera multiplicada por dos.",
            "No añade ninguna condición nueva: es redundante.",
        )
        for t, frase in zip(textos[:2], frases):
            with self.narrar(frase):
                self.play(FadeIn(t))
        t = ValueTracker(0)
        punto = always_redraw(lambda: Dot(plano.c2p(5 - t.get_value(), t.get_value()), color=COLOR_PIVOTE, radius=0.1))
        with self.narrar("Cualquier punto de la recta es solución. Si llamamos te al valor de ye, equis vale cinco menos te: "
                         "las soluciones son cinco menos te, coma, te, para cualquier número te."):
            self.play(Write(textos[2]), FadeIn(punto))
            for valor in (4, 1, 2.5):
                self.play(t.animate.set_value(valor), run_time=1.5)
        with self.narrar("Todos los puntos de la recta son solución: hay infinitas soluciones, descritas con un parámetro."):
            self.pie("Todos los puntos de la recta son solución: INFINITAS soluciones, con un parámetro.")
        self.wait(1)
        self.limpiar(titulo)

        # Los tres casos juntos.
        titulo = self.cambiar_encabezado(titulo, "Los tres casos posibles")
        casos = [
            ([(1, 1, 5), (1, -1, 1)], (), "se cortan", "una solución", COLOR_SOLUCION),
            ([(1, 1, 5), (1, 1, 2)], (), "paralelas", "ninguna", COLOR_ERROR),
            ([(1, 1, 5), (2, 2, 10)], (1,), "coincidentes", "infinitas", COLOR_LIBRE),
        ]
        paneles = VGroup()
        for coef, disc, nombre, resultado, color in casos:
            mini = ejes_iguales((-1, 6), (-1, 6), unidad=0.5, numeros=False)
            panel = VGroup(
                mini,
                rectas(mini, coef, discontinuas=disc),
                Text(nombre, font_size=TAM_TEXTO),
                Text(resultado, font_size=TAM_TEXTO, color=color),
            )
            panel[2].next_to(mini, DOWN, buff=0.3)
            panel[3].next_to(panel[2], DOWN, buff=0.2)
            paneles.add(panel)
        paneles.arrange(RIGHT, buff=0.9).shift(DOWN * 0.2)
        frases = ("Si las rectas se cortan: una solución.", "Si son paralelas: ninguna.", "Si coinciden: infinitas.")
        for p, frase in zip(paneles, frases):
            with self.narrar(frase):
                self.play(FadeIn(p))
        with self.narrar("Y nunca hay exactamente dos soluciones: dos rectas distintas no pueden cortarse en dos puntos."):
            self.pie("Nunca hay exactamente dos soluciones: dos rectas distintas no pueden cortarse en dos puntos.")
        self.wait(2)

        self.ejercicio_propuesto(
            "F03-N3-01",
            Tex(
                r"Escribe un sistema de dos ecuaciones con dos incógnitas que tenga:\\"
                r"a) solución única $(2, -1)$; \ b) ninguna solución;\\"
                r"c) infinitas soluciones, todas cumpliendo $x + y = 3$.",
                font_size=42,
            ),
            voz="Ejercicio propuesto: escribe tres sistemas. Uno con solución única dos, menos uno; otro sin solución; "
                "y otro con infinitas soluciones, todas sobre la recta equis más ye igual a tres. " + PAUSA,
            espera=4,
        )
        self.resumen(
            [
                "Rectas coincidentes: una ecuación es múltiplo de la otra; infinitas soluciones.",
                "Se cortan: una solución. Paralelas: ninguna. Coincidentes: infinitas.",
                "Con dos incógnitas, nunca hay exactamente dos soluciones.",
            ],
            "Lección 9 — sistemas de tres ecuaciones con tres incógnitas.",
            voz="En resumen: si una ecuación es múltiplo de la otra, las rectas coinciden y hay infinitas soluciones. "
                "Se cortan: una solución. Paralelas: ninguna. Coincidentes: infinitas. "
                "Y con dos incógnitas nunca hay exactamente dos soluciones. "
                "En la lección nueve pasamos a tres ecuaciones con tres incógnitas.",
            espera=2,
        )
