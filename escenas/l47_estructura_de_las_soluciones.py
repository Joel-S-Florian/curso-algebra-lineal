"""Lección 47 — Estructura de las soluciones: x = xp + n con n en el núcleo.

Escenas (un video cada una):
    SolucionParticularMasNucleo, RectaTrasladada

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l47_estructura_de_las_soluciones.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import panel_derecha, EscenaCurso, ajustar_al_encuadre, ejes_iguales, escalera, flecha, matriz_gauss, parrafo, recta_general  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_U, COLOR_V, COLOR_W = COLORES_ECUACIONES


class SolucionParticularMasNucleo(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 47 · Parte 1", "Una solución más el núcleo")
        titulo = self.encabezado("Resolver A x = b hasta el final")
        reducida = matriz_gauss([[1, 2, 0, 1, 1], [0, 0, 1, 2, 1], [0, 0, 0, 0, 0]], pivotes=[(0, 0), (1, 2)], escala=0.9).move_to(LEFT * 3.8 + DOWN * 0.3)
        enunciado = MathTex(r"A\mathbf{x} = \mathbf{b},\quad A = \begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix},\ \mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix}", font_size=36).next_to(titulo, DOWN, buff=0.3)
        self.decir("Resolvamos un sistema a por equis igual a be, con la matriz de las lecciones anteriores y el vector be igual a uno, tres, dos. Tras escalonar la matriz aumentada, queda esta forma reducida: es compatible, y las columnas dos y cuatro no tienen pivote.")
        self.play(FadeIn(enunciado))
        self.play(FadeIn(reducida))
        self.play(Create(escalera(reducida, [(0, 0), (1, 2)])))
        despeje = VGroup(
            MathTex(r"x_1 = 1 - 2x_2 - x_4", font_size=44),
            MathTex(r"x_3 = 1 - 2x_4", font_size=44),
            MathTex(r"x_2 = s,\ x_4 = t", font_size=44, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(reducida, RIGHT, buff=1.2)
        ajustar_al_encuadre(VGroup(enunciado, reducida, despeje), margen=0.5)
        self.decir("Despejando, equis uno es uno menos dos equis dos menos equis cuatro, y equis tres es uno menos dos equis cuatro. Las libres son ese y te.")
        for d in despeje:
            self.play(FadeIn(d))
            self.wait(1.2)
        self.wait(1)
        self.limpiar(titulo, enunciado)
        general = MathTex(
            r"\mathbf{x} = \underbrace{\begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \end{bmatrix}}_{\mathbf{x}_p} + s\underbrace{\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}}_{\mathbf{n}_1} + t\underbrace{\begin{bmatrix} -1 \\ 0 \\ -2 \\ 1 \end{bmatrix}}_{\mathbf{n}_2}",
            font_size=46,
        ).next_to(enunciado, DOWN, buff=1.0)
        nota = Tex(r"$\mathbf{x}_p$: una solución (libres $=0$).\quad $\mathbf{n}_1, \mathbf{n}_2$: base de $\ker A$.", font_size=34, color=COLOR_SECUNDARIO).next_to(general, DOWN, buff=0.35)
        ajustar_al_encuadre(VGroup(general, nota), margen=0.5)
        self.decir("Escribimos la solución general como vector, separando tres partes. Lo que no depende de ese ni de te es una solución concreta, equis pe: la que se obtiene con las libres iguales a cero. Lo que acompaña a ese y a te es la base del núcleo que ya conocemos.")
        self.play(Write(general))
        self.play(FadeIn(nota))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Teorema: estructura de las soluciones")
        teorema = VGroup(
            parrafo(r"Si $\mathbf{x}_p$ es una solución de $A\mathbf{x} = \mathbf{b}$, entonces", r"el conjunto de todas las soluciones es:", font_size=40, sangria=0.5),
            MathTex(r"\{\, \mathbf{x}_p + \mathbf{n} \;:\; \mathbf{n} \in \ker A \,\}", font_size=60, color=COLOR_PIVOTE),
            Tex(r"Toda solución es una solución particular más una solución del sistema homogéneo.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(teorema, margen=0.5)
        self.decir("Esto no es casualidad. El teorema dice: si equis pe es una solución de a por equis igual a be, el conjunto de todas las soluciones es el de los vectores equis pe más ene, con ene en el núcleo de a. Toda solución es una solución particular más una solución del sistema homogéneo.")
        for t in teorema:
            self.play(FadeIn(t))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Demostración")
        demo = VGroup(
            Tex(r"($\supseteq$) Si $\mathbf{n} \in \ker A$: $\;A(\mathbf{x}_p + \mathbf{n}) = A\mathbf{x}_p + A\mathbf{n} = \mathbf{b} + \mathbf{0} = \mathbf{b}$.", font_size=38),
            Tex(r"($\subseteq$) Si $A\mathbf{x} = \mathbf{b}$, sea $\mathbf{n} = \mathbf{x} - \mathbf{x}_p$. Entonces", font_size=38),
            MathTex(r"A\mathbf{n} = A\mathbf{x} - A\mathbf{x}_p = \mathbf{b} - \mathbf{b} = \mathbf{0},", font_size=44, color=COLOR_PIVOTE),
            Tex(r"luego $\mathbf{n} \in \ker A$ y $\mathbf{x} = \mathbf{x}_p + \mathbf{n}$. $\qquad\blacksquare$", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(demo, margen=0.5)
        self.decir("La demostración tiene dos mitades. Primera: si ene está en el núcleo, a por equis pe más ene es a por equis pe más a por ene, que es be más cero, es decir, be. Así que equis pe más ene es solución. Segunda: si equis es una solución cualquiera, llamemos ene a equis menos equis pe. Entonces a por ene es a por equis menos a por equis pe, es decir, be menos be, cero. Luego ene está en el núcleo, y equis es equis pe más ene.")
        for d in demo:
            self.play(FadeIn(d))
            self.wait(3)
        self.wait(1)

        self.ejercicio_propuesto(
            "F13-N3-05",
            VGroup(
                Text("Resuelve y escribe la solución general como x = xp + s·n1 + t·n2:", font_size=TAM_TEXTO),
                MathTex(r"\begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}\mathbf{x} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix}", font_size=48),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: resuelve este sistema y escribe la solución general como una solución particular más combinaciones de una base del núcleo. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Solución general = solución particular + núcleo.",
                "Se obtiene con las libres en 0 (xp) y una base del núcleo.",
                "Demostración: A(x − xp) = b − b = 0.",
            ],
            "cómo se ve esto geométricamente: una recta trasladada.",
            voz="En resumen: la solución general es una solución particular más el núcleo. Se obtiene poniendo las libres a cero, y añadiendo una base del núcleo. Y la demostración es que a por equis menos equis pe es be menos be, cero. Siguiente: cómo se ve esto geométricamente, como una recta trasladada.",
        )


class RectaTrasladada(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 47 · Parte 2", "La recta trasladada")
        titulo = self.encabezado("El homogéneo y el no homogéneo")
        p = ejes_iguales((-4, 6), (-3, 4), unidad=0.72).to_edge(LEFT, buff=0.5).shift(DOWN * 0.35)
        ker = recta_general(p, 1, 2, 0, color=COLOR_PIVOTE, stroke_width=6)
        n = flecha(p, -2, 1, COLOR_U)
        rot_ker = MathTex(r"\ker A:\ x_1 + 2x_2 = 0", font_size=34, color=COLOR_PIVOTE).move_to(p.c2p(2.3, -2.55))
        texto = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}", font_size=46),
            Tex(r"$A\mathbf{x} = \mathbf{0}$: la recta\\ $x_1 + 2x_2 = 0$ por el origen.", font_size=34),
        ).arrange(DOWN, buff=0.4).to_edge(RIGHT, buff=0.5).shift(UP * 1.9)
        panel_derecha(texto)
        ajustar_al_encuadre(texto, margen=0.5)
        self.decir("Veamos la estructura en el plano. Con la matriz uno, dos; dos, cuatro, el sistema homogéneo tiene como soluciones esta recta, que pasa por el origen: es el núcleo.")
        self.play(Create(p))
        self.play(Create(ker), GrowArrow(n), FadeIn(rot_ker), FadeIn(texto))
        self.wait(2)

        xp = flecha(p, 3, 0, COLOR_V)
        punto_p = Dot(p.c2p(3, 0), color=COLOR_V, radius=0.09)
        sol = recta_general(p, 1, 2, 3, color=COLOR_SOLUCION, stroke_width=6)
        texto2 = VGroup(
            MathTex(r"A\mathbf{x} = \begin{bmatrix} 3 \\ 6 \end{bmatrix}", font_size=46),
            Tex(r"Una solución: $\mathbf{x}_p = (3, 0)$.", font_size=36, color=COLOR_V),
            Tex(r"Todas: $\mathbf{x}_p + t\,(-2, 1)$,", font_size=36, color=COLOR_SOLUCION),
            Tex(r"la recta $x_1 + 2x_2 = 3$.", font_size=36, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.5).shift(DOWN * 1.0)
        panel_derecha(texto2)
        ajustar_al_encuadre(texto2, margen=0.5)
        self.decir("Ahora el sistema con lado derecho tres, seis. Una solución es equis pe igual a tres, cero. Todas las demás se obtienen sumándole múltiplos del vector del núcleo: forman otra recta, paralela a la primera, que pasa por equis pe. Es el núcleo, trasladado.")
        self.play(GrowArrow(xp), FadeIn(punto_p, scale=2))
        self.play(FadeIn(texto2[:2]))
        self.play(Create(sol), FadeIn(texto2[2:]))
        self.wait(2)

        copias = VGroup(
            flecha(p, -2, 1, COLOR_U, desde=(3, 0)),
            flecha(p, -2, 1, COLOR_U, desde=(1, 1)),
        )
        puntos = VGroup(*[Dot(p.c2p(3 - 2 * c, c), color=COLOR_SOLUCION, radius=0.08) for c in (1, 2, -1)])
        self.decir("Sumar un vector del núcleo desplaza la solución a lo largo de la recta, sin salir de ella. Aquí tenemos las soluciones tres, cero; uno, uno; y cinco, menos uno.")
        self.play(LaggedStart(*[GrowArrow(c) for c in copias], lag_ratio=0.5))
        self.play(LaggedStart(*[FadeIn(q, scale=2) for q in puntos], lag_ratio=0.3))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Tres posibilidades, ahora con el núcleo")
        casos = VGroup(
            parrafo(r"\textbf{Sin solución}: $\mathbf{b} \notin \operatorname{Col}(A)$ (el sistema es incompatible).", font_size=36, sangria=0.4, color=COLOR_ERROR),
            parrafo(r"\textbf{Solución única}: compatible y $\ker A = \{\mathbf{0}\}$ (el trasladado de un punto es un punto).", font_size=36, sangria=0.4, color=COLOR_SOLUCION),
            parrafo(r"\textbf{Infinitas soluciones}: compatible y $\ker A \ne \{\mathbf{0}\}$ (el núcleo, trasladado).", r"Su ``tamaño'' es la nulidad: una recta si $\operatorname{nul} = 1$, un plano si $2$, \dots", font_size=36, sangria=0.4, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(casos, margen=0.5)
        self.decir("Así reaparece la clasificación de la lección cuarenta y uno, ahora con el núcleo. Sin solución, cuando be no es alcanzable; lo precisaremos en la próxima lección. Solución única, cuando es compatible y el núcleo es solo el vector nulo: el trasladado de un punto es un punto. E infinitas soluciones, cuando es compatible y el núcleo es más grande: las soluciones forman el núcleo trasladado, una recta si la nulidad es uno, un plano si es dos, y así sucesivamente.")
        for c in casos:
            self.play(FadeIn(c))
            self.wait(3.2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F13-N4-01",
            VGroup(
                Text("Resuelve y dibuja el conjunto solución:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y = 3 \\ 2x + 4y = 6 \end{cases}", font_size=52),
                Text("Indica una solución particular y el núcleo.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: resuelve este sistema, indica una solución particular y el núcleo, y dibuja el conjunto solución. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Soluciones de A x = b: el núcleo trasladado por una solución particular.",
                "Solución única ⇔ compatible y núcleo trivial.",
                "El tamaño del conjunto solución es la nulidad.",
            ],
            "Lección 48 — el espacio columna y la imagen.",
            voz="En resumen: las soluciones de a por equis igual a be forman el núcleo, trasladado por una solución particular. La solución es única exactamente cuando el sistema es compatible y el núcleo es trivial. Y el tamaño del conjunto solución es la nulidad. Siguiente: lección cuarenta y ocho, el espacio columna y la imagen.",
        )
