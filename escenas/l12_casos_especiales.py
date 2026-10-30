"""Lección 12 — Casos especiales y errores frecuentes del Bloque I.

Escenas (un video cada una):
    MasEcuacionesQueIncognitas, MenosEcuacionesQueIncognitas, ErroresFrecuentesBloqueI

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l12_casos_especiales.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, ejes_iguales, plano_3d, sistema_con_llave  # noqa: E402
from curso.componentes import rectas_de_sistema as rectas  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class MasEcuacionesQueIncognitas(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 12 · Parte 1", "Más ecuaciones que incógnitas")
        titulo = self.encabezado("Tres rectas en el plano")
        plano = ejes_iguales((-1, 4), (-1, 4), unidad=0.95).to_edge(LEFT, buff=0.9).shift(DOWN * 0.3)
        self.decir("Tres ecuaciones con dos incógnitas: tres rectas en el plano.")
        self.play(Create(plano))
        c = ValueTracker(3)
        fijas = rectas(plano, [(1, 1, 2), (1, -1, 0)])
        # Tercera recta, 2x + y = c, recortada a la ventana (y entre -1 y 4).
        tercera = always_redraw(
            lambda: plano.plot(
                lambda x: c.get_value() - 2 * x,
                x_range=[max(-1, (c.get_value() - 4) / 2), min(4, (c.get_value() + 1) / 2)],
                color=COLORES_ECUACIONES[2],
                stroke_width=4,
            )
        )
        sistema = always_redraw(
            lambda: sistema_con_llave(
                ("x + y", "=", "2"), ("x - y", "=", "0"), ("2x + y", "=", f"{c.get_value():.1f}".replace(".0", "")), font_size=40
            ).to_edge(RIGHT, buff=1.4).shift(UP * 2)
        )
        self.decir("Equis más ye igual a dos, equis menos ye igual a cero, y dos equis más ye igual a ce, que de momento vale tres.")
        self.play(FadeIn(sistema), Create(fijas))
        self.play(Create(tercera))
        punto = Dot(plano.c2p(1, 1), color=COLOR_PIVOTE, radius=0.1)
        self.decir("Aun así hay solución: las tres rectas pasan por el mismo punto, el uno, uno. Dos más uno es tres.")
        self.play(FadeIn(punto, scale=3))
        nota = Tex(r"$(1, 1)$ cumple las tres:\\ $2 + 1 = 3$ \checkmark", font_size=38, color=COLOR_SOLUCION).to_edge(RIGHT, buff=1.4).shift(DOWN * 0.3)
        self.play(FadeIn(nota))
        self.pie("Tres ecuaciones y dos incógnitas, y hay solución: las tres rectas pasan por el mismo punto.", espera=3)
        self.play(FadeOut(nota), FadeOut(punto))
        self.decir("Si cambiamos el término independiente de la tercera a cuatro, la recta se desplaza.")
        self.play(c.animate.set_value(4), run_time=2)
        vertices = [(1, 1), (2, 0), (4 / 3, 4 / 3)]
        triangulo = Polygon(*[plano.c2p(*v) for v in vertices], color=COLOR_ERROR, fill_opacity=0.25)
        self.decir("Las rectas se cortan dos a dos, pero ya no hay un punto común: dos más uno no es cuatro. Mismo número de ecuaciones, distinta respuesta.")
        self.play(FadeIn(triangulo))
        nota = Tex(r"Las tres rectas se cortan dos a dos,\\ pero no hay punto común:\\ $2 + 1 = 3 \neq 4$", font_size=38, color=COLOR_ERROR)
        nota.to_edge(RIGHT, buff=1.2).shift(DOWN * 0.5)
        self.play(FadeIn(nota))
        self.decir("Con ce igual a cuatro el sistema es incompatible. Tener más ecuaciones que incógnitas no decide nada por sí solo.")
        self.pie("Con c = 4 el sistema es incompatible. Tener más ecuaciones que incógnitas NO decide nada por sí solo.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo decidirlo")
        bloque = VGroup(
            Tex(r"1. Resolver con dos de las ecuaciones: \ $x + y = 2,\ x - y = 0 \Rightarrow (1, 1)$.", font_size=38),
            Tex(r"2. Comprobar si esa solución cumple las demás: \ $2\cdot 1 + 1 = 3$.", font_size=38),
            Tex(r"3. Compatible si $c = 3$ (SCD); incompatible si $c \neq 3$ (SI).", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Para decidir: resolvemos con dos de las ecuaciones, y obtenemos uno, uno. Luego comprobamos esa solución en la tercera: dos por uno más uno es tres. El sistema es compatible determinado si ce es tres, e incompatible si no.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F03-N4-02",
            VGroup(
                Tex(r"¿Para qué valores de $k$ es compatible el sistema? ¿Cuál es entonces la solución?", font_size=38),
                sistema_con_llave(("x + 2y", "=", "5"), ("3x - y", "=", "1"), ("2x + 3y", "=", "k"), font_size=42),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Más ecuaciones que incógnitas: puede haber solución o no.",
                "Se resuelve con unas ecuaciones y se comprueba en las demás.",
                "El número de ecuaciones, por sí solo, no clasifica un sistema.",
            ],
            "menos ecuaciones que incógnitas.",
        )


class MenosEcuacionesQueIncognitas(EscenaCurso, ThreeDScene):
    def construct(self):
        self.mostrar_portada("Lección 12 · Parte 2", "Menos ecuaciones que incógnitas")
        titulo = self.encabezado("Dos planos en el espacio")
        espacio, rotulos = self.espacio_3d(rango=(-1, 4), centro=(1, 1, 1.2), zoom=0.85)
        self.decir("Dos ecuaciones con tres incógnitas: dos planos en el espacio.")
        self.play(Create(espacio), FadeIn(rotulos))

        # Caso 1: se cortan en una recta.
        sistema = sistema_con_llave(("x + y + z", "=", "3"), ("x - y + z", "=", "1"), font_size=38).to_corner(UL, buff=0.5).shift(DOWN * 0.7)
        self._fijar(sistema)
        u, v = (-0.3, 2.3), (-0.3, 2.3)
        p1 = plano_3d(espacio, 1, 1, 1, 3, u, v, COLORES_ECUACIONES[0])
        p2 = plano_3d(espacio, 1, -1, 1, 1, u, v, COLORES_ECUACIONES[1])
        self.decir("Si se cortan, lo hacen en una recta.")
        self.play(FadeIn(sistema), Create(p1), Create(p2))
        recta = Line3D(espacio.c2p(2.3, 1, -0.3), espacio.c2p(-0.3, 1, 2.3), color=COLOR_PIVOTE, thickness=0.03)
        self.decir("Todos los puntos de esa recta son solución: dos menos te, uno, te. Infinitas soluciones.")
        self.play(Create(recta))
        texto = MathTex(r"(2 - t,\ 1,\ t):\ \text{infinitas}", font_size=38, color=COLOR_PIVOTE).to_corner(DR, buff=0.6).shift(UP * 0.6)
        self._fijar(texto)
        self.play(Write(texto))
        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(*[FadeOut(m) for m in (sistema, p1, p2, recta, texto)])

        # Caso 2: planos paralelos.
        sistema = sistema_con_llave(("x + y + z", "=", "1"), ("x + y + z", "=", "3"), font_size=38).to_corner(UL, buff=0.5).shift(DOWN * 0.7)
        self._fijar(sistema)
        q1 = plano_3d(espacio, 1, 1, 1, 1, u, v, COLORES_ECUACIONES[0])
        q2 = plano_3d(espacio, 1, 1, 1, 3, u, v, COLORES_ECUACIONES[1])
        self.decir("Si los planos son paralelos, como equis más ye más zeta igual a uno y a tres, no hay ninguna solución.")
        self.play(FadeIn(sistema), Create(q1), Create(q2))
        texto = MathTex(r"\text{paralelos: ninguna}\ (1 \neq 3)", font_size=38, color=COLOR_ERROR).to_corner(DR, buff=0.6).shift(UP * 0.6)
        self._fijar(texto)
        self.play(Write(texto))
        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.limpiar()
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1)

        titulo = self.encabezado("Lo que nunca ocurre: una única solución")
        bloque = VGroup(
            Tex(r"Dos planos no pueden cortarse en un solo punto: o en una recta, o coinciden, o no se cortan.", font_size=36),
            Tex(r"En general: con \textbf{menos ecuaciones que incógnitas}, el sistema es \textbf{SCI o SI}, nunca SCD.", font_size=36, color=COLOR_PIVOTE),
            Tex(r"Idea: si hay solución, siempre queda al menos una incógnita libre.", font_size=36),
            Tex(r"La demostración general llega con el rango (Lección 40): rango $\le m < n$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.5)
        self._fijar(bloque)
        self.decir("Lo que nunca puede pasar es que dos planos se corten en un solo punto. Con menos ecuaciones que incógnitas, el sistema es indeterminado o incompatible, nunca determinado: si hay solución, siempre queda al menos una incógnita libre. La prueba completa la daremos con el rango.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F03-N4-03",
            VGroup(
                sistema_con_llave(("x + y - z", "=", "2"), ("2x + 2y - 2z", "=", "c"), font_size=44, colores=False),
                Tex(r"¿Para qué valores de $c$ es compatible? En ese caso, describe las soluciones con parámetros.", font_size=36),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Menos ecuaciones que incógnitas: SCI o SI, nunca una única solución.",
                "Dos planos: se cortan en una recta, coinciden o son paralelos.",
                "La justificación completa llega con el rango (Lección 40).",
            ],
            "errores frecuentes del Bloque I.",
        )


class ErroresFrecuentesBloqueI(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 12 · Parte 3", "Errores frecuentes")
        errores = [
            ("«Tantas ecuaciones como incógnitas ⇒ una solución».",
             r"\begin{cases} x + y = 1 \\ 2x + 2y = 2 \end{cases}\ \text{tiene infinitas.}"),
            ("«Más ecuaciones que incógnitas ⇒ no hay solución».",
             r"\begin{cases} x + y = 2 \\ x - y = 0 \\ 2x + y = 3 \end{cases}\ \text{tiene la solución } (1, 1)."),
            ("«Menos ecuaciones que incógnitas ⇒ infinitas soluciones».",
             r"\begin{cases} x + y + z = 1 \\ x + y + z = 3 \end{cases}\ \text{no tiene ninguna.}"),
            ("«Si cumple una ecuación, es solución».",
             r"(4, 1) \text{ cumple } x + y = 5 \text{ pero no } x - y = 1."),
            ("«Llegar a 0 = 0 significa que no hay solución».",
             r"0 = 0 \text{ es siempre cierto: la ecuación sobraba. Es } 0 = 5 \text{ lo que indica SI.}"),
            ("«Un sistema homogéneo puede no tener solución».",
             r"(0, 0, \dots, 0) \text{ siempre es solución.}"),
        ]
        voces = [
            "Falso: tantas ecuaciones como incógnitas no asegura una solución. Equis más ye igual a uno, y dos equis más dos ye igual a dos, tiene infinitas.",
            "Falso: con más ecuaciones que incógnitas puede haber solución. Este sistema de tres ecuaciones tiene la solución uno, uno.",
            "Falso: con menos ecuaciones que incógnitas puede no haber ninguna. Dos planos paralelos no se cortan.",
            "Falso: un punto que cumple una sola ecuación no es solución. Cuatro, uno cumple la primera, pero no la segunda.",
            "Falso: llegar a cero igual a cero no significa que no haya solución. Es siempre cierto: la ecuación sobraba. Lo que indica un sistema incompatible es algo como cero igual a cinco.",
            "Falso: un sistema homogéneo siempre tiene solución: la trivial, con todas las incógnitas a cero.",
        ]
        titulo = self.encabezado("Seis creencias falsas")
        for (creencia, realidad), voz in zip(errores, voces):
            self.decir(voz)
            tarjeta = VGroup(
                VGroup(MathTex(r"\times", font_size=56, color=COLOR_ERROR), Text(creencia, font_size=TAM_TEXTO, color=COLOR_ERROR)).arrange(RIGHT, buff=0.3),
                MathTex(realidad, font_size=40, color=COLOR_SOLUCION),
            ).arrange(DOWN, buff=0.6)
            ajustar_al_encuadre(tarjeta)
            self.play(FadeIn(tarjeta[0], shift=DOWN * 0.2))
            self.wait(1.5)
            self.play(Write(tarjeta[1]))
            self.wait(3)
            self.play(FadeOut(tarjeta))
        self.decir("Moraleja: contar ecuaciones e incógnitas no basta para clasificar un sistema. Hace falta analizar las ecuaciones.")
        self.pie("Moraleja: la forma del sistema (cuántas ecuaciones e incógnitas) no basta para clasificarlo.", espera=4)

        self.ejercicio_propuesto(
            "F03-N4-04",
            VGroup(
                Text("¿Verdadero o falso? Da un ejemplo o un contraejemplo.", font_size=TAM_TEXTO),
                Tex(r"a) Un sistema de 3 ecuaciones con 3 incógnitas siempre tiene solución.", font_size=38),
                Tex(r"b) Si un sistema lineal tiene dos soluciones distintas, tiene infinitas.", font_size=38),
                Tex(r"c) Si un sistema tiene solución única, al quitarle una ecuación puede seguir teniéndola.", font_size=38),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35),
        )
        self.resumen(
            [
                "Contar ecuaciones e incógnitas no basta para clasificar.",
                "Una solución debe cumplir todas las ecuaciones.",
                "0 = 0 indica una ecuación que sobraba; 0 = c (c distinto de 0), un sistema incompatible.",
                "Los homogéneos siempre son compatibles.",
            ],
            "Unidad 2, Lección 13 — el método de sustitución.",
            voz="En resumen: contar ecuaciones e incógnitas no basta para clasificar. Una solución debe cumplir todas las ecuaciones. Cero igual a cero indica una ecuación que sobraba; cero igual a un número distinto de cero, un sistema incompatible. Y los sistemas homogéneos siempre son compatibles. Siguiente: unidad dos, lección trece, el método de sustitución.",
        )
