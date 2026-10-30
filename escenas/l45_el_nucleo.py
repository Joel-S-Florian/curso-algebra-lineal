"""Lección 45 — El núcleo de una matriz.

Escenas (un video cada una):
    DefinicionNucleo, ComprobarSiUnVectorEstaEnElNucleo

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l45_el_nucleo.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import panel_derecha, EscenaCurso, ajustar_al_encuadre, ejes_iguales, flecha, parrafo, recta_general  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_U, COLOR_V, COLOR_W = COLORES_ECUACIONES


def plano_vectores(x_range=(-4, 5), y_range=(-3, 4)) -> Axes:
    return ejes_iguales(x_range, y_range, unidad=0.72).to_edge(LEFT, buff=0.5).shift(DOWN * 0.35)


class DefinicionNucleo(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 45 · Parte 1", "El núcleo de una matriz")
        titulo = self.encabezado("Las soluciones del sistema homogéneo")
        sistema = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}", font_size=50),
            MathTex(r"A\mathbf{x} = \mathbf{0} \;\Longleftrightarrow\; \begin{cases} x_1 + 2x_2 = 0 \\ 2x_1 + 4x_2 = 0 \end{cases}", font_size=44),
            Tex(r"La segunda ecuación es el doble de la primera: solo queda $x_1 + 2x_2 = 0$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(sistema, margen=0.5)
        self.decir("Empecemos con una matriz sencilla de dos por dos. Nos interesa el sistema homogéneo, a por equis igual a cero, el que tiene todos los términos independientes nulos. Sus dos ecuaciones son la misma, salvo por un factor dos: queda una sola, equis uno más dos equis dos igual a cero.")
        for s in sistema:
            self.play(FadeIn(s))
            self.wait(2)
        self.limpiar(titulo)

        p = plano_vectores()
        recta = recta_general(p, 1, 2, 0, color=COLOR_PIVOTE, stroke_width=6)
        d = flecha(p, -2, 1, COLOR_U)
        puntos = VGroup(*[Dot(p.c2p(-2 * c, c), color=COLOR_PIVOTE, radius=0.07) for c in (-1, 0.5, 1.5, 2)])
        cero = Dot(p.c2p(0, 0), color=WHITE, radius=0.09)
        texto = VGroup(
            Tex(r"Soluciones: $x_1 = -2x_2$", font_size=40),
            MathTex(r"\mathbf{x} = t\begin{bmatrix} -2 \\ 1 \end{bmatrix}", font_size=48, color=COLOR_PIVOTE),
            Tex(r"Una recta por el origen.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.7).shift(UP * 1.0)
        panel_derecha(texto)
        ajustar_al_encuadre(texto, margen=0.5)
        self.decir("Sus soluciones son los puntos con equis uno igual a menos dos equis dos: múltiplos del vector menos dos, uno. Dibujadas en el plano, forman una recta que pasa por el origen. El origen, el vector cero, siempre es una solución.")
        self.play(Create(p))
        self.play(Create(recta), FadeIn(cero, scale=2))
        self.play(GrowArrow(d), LaggedStart(*[FadeIn(q, scale=2) for q in puntos], lag_ratio=0.3), FadeIn(texto))
        self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición")
        definicion = VGroup(
            parrafo(r"El \textbf{núcleo} (o espacio nulo) de una matriz $A$ de tamaño $m \times n$ es", r"el conjunto de las soluciones del sistema homogéneo:", font_size=40, sangria=0.5),
            MathTex(r"\ker A = \{\, \mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0} \,\}", font_size=56, color=COLOR_PIVOTE),
            Tex(r"Es un subconjunto de $\mathbb{R}^n$ (el de las incógnitas), no de $\mathbb{R}^m$.", font_size=38),
            Tex(r"También se escribe $N(A)$ o $\operatorname{Nul}(A)$.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(definicion, margen=0.5)
        self.decir("El núcleo de una matriz a, de tamaño eme por ene, es el conjunto de las soluciones del sistema homogéneo. Se escribe ker de a, por la palabra alemana Kern, y es un subconjunto del espacio de ene dimensiones, el de las incógnitas, no del de las ecuaciones. También se le llama espacio nulo.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Vector nulo frente a espacio nulo")
        contraste = VGroup(
            VGroup(
                Tex(r"\textbf{Vector nulo}", font_size=42, color=COLOR_COEFICIENTE),
                MathTex(r"\mathbf{0} = (0, \dots, 0)", font_size=44),
                Tex(r"Un solo vector.", font_size=36),
            ).arrange(DOWN, buff=0.35),
            VGroup(
                Tex(r"\textbf{Espacio nulo} $\ker A$", font_size=42, color=COLOR_PIVOTE),
                MathTex(r"\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}", font_size=44),
                Tex(r"Un conjunto de vectores.", font_size=36),
            ).arrange(DOWN, buff=0.35),
        ).arrange(RIGHT, buff=1.8, aligned_edge=UP).next_to(titulo, DOWN, buff=0.8)
        nota = VGroup(
            MathTex(r"\mathbf{0} \in \ker A \ \text{ siempre}", font_size=46, color=COLOR_SOLUCION),
            Tex(r"Si $\ker A = \{\mathbf{0}\}$, el sistema homogéneo solo tiene la solución trivial;", font_size=36),
            Tex(r"si no, tiene infinitas, y $\ker A$ es una recta, un plano\dots", font_size=36),
        ).arrange(DOWN, buff=0.35).next_to(contraste, DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(contraste, nota), margen=0.5)
        self.decir("No confundamos dos cosas. El vector nulo es un solo vector, todo de ceros. El espacio nulo es un conjunto de vectores. El vector nulo siempre pertenece al núcleo, porque a por cero es cero. Si el núcleo es solo el vector nulo, el sistema homogéneo tiene únicamente la solución trivial; si no, tiene infinitas soluciones, y el núcleo es una recta, un plano, o algo mayor.")
        self.play(FadeIn(contraste[0]))
        self.wait(1.5)
        self.play(FadeIn(contraste[1]))
        self.wait(1.5)
        for n in nota:
            self.play(FadeIn(n))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El núcleo es un subespacio")
        cierre = VGroup(
            Tex(r"Si $\mathbf{x}, \mathbf{y} \in \ker A$ y $c \in \mathbb{R}$:", font_size=40),
            MathTex(r"A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}", font_size=44),
            MathTex(r"A(c\mathbf{x}) = c\,A\mathbf{x} = c\,\mathbf{0} = \mathbf{0}", font_size=44),
            Tex(r"La suma y los múltiplos de soluciones siguen siendo soluciones:", font_size=38, color=COLOR_PIVOTE),
            Tex(r"$\ker A$ es un \textbf{subespacio} de $\mathbb{R}^n$, y por eso tiene base y dimensión.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(cierre, margen=0.5)
        self.decir("Veamos por qué es un subespacio. Si equis e i griega están en el núcleo, a por su suma es a por equis más a por i griega, que es cero más cero. Y si multiplicamos equis por un número ce, a por ce equis es ce por a equis, igual a cero. La suma y los múltiplos de soluciones del sistema homogéneo siguen siendo soluciones. Por eso el núcleo tiene base y dimensión, como vimos en la lección anterior.")
        for c in cierre:
            self.play(FadeIn(c))
            self.wait(2.2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F13-N2-01",
            VGroup(
                Text("Halla el núcleo de A y descríbelo geométricamente:", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla el núcleo de esta matriz y descríbelo geométricamente. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "ker A = { x : A x = 0 } ⊂ ℝⁿ.",
                "El vector 0 siempre está; el núcleo puede tener muchos más.",
                "Es un subespacio: cerrado bajo sumas y múltiplos.",
            ],
            "cómo saber si un vector está en el núcleo.",
            voz="En resumen: el núcleo es el conjunto de soluciones del sistema homogéneo, un subconjunto del espacio de las incógnitas. El vector nulo siempre está, y puede haber muchos más. Y es un subespacio. Siguiente: cómo saber si un vector está en el núcleo.",
        )


class ComprobarSiUnVectorEstaEnElNucleo(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 45 · Parte 2", "¿Está un vector en el núcleo?")
        titulo = self.encabezado("Multiplicar y mirar si sale cero")
        a_tex = r"\begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}"
        matriz_a = MathTex(r"A = " + a_tex, font_size=46).next_to(titulo, DOWN, buff=0.5)
        self.decir("Tomemos esta matriz de tres por cuatro. Su núcleo está dentro del espacio de cuatro dimensiones. Para saber si un vector pertenece al núcleo basta multiplicar y ver si el resultado es el vector nulo.")
        self.play(Write(matriz_a))
        self.wait(1)
        v1 = MathTex(r"\mathbf{v} = \begin{bmatrix} -3 \\ 1 \\ -2 \\ 1 \end{bmatrix}", font_size=46, color=COLOR_U)
        calculo = VGroup(
            MathTex(r"A\mathbf{v} = \begin{bmatrix} -3 + 2 + 0 + 1 \\ -6 + 4 - 2 + 4 \\ -3 + 2 - 2 + 3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}", font_size=46),
            Tex(r"$A\mathbf{v} = \mathbf{0}$, luego $\mathbf{v} \in \ker A$.", font_size=42, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.4)
        fila = VGroup(v1, calculo).arrange(RIGHT, buff=0.8).next_to(matriz_a, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(matriz_a, fila), margen=0.5)
        self.decir("Con el vector menos tres, uno, menos dos, uno, cada fila da cero. A por ve es el vector nulo, así que ve pertenece al núcleo.")
        self.play(FadeIn(v1))
        self.play(Write(calculo[0]))
        self.play(FadeIn(calculo[1]))
        self.wait(2.5)
        self.play(FadeOut(fila))

        v2 = MathTex(r"\mathbf{w} = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}", font_size=46, color=COLOR_V)
        calculo2 = VGroup(
            MathTex(r"A\mathbf{w} = \begin{bmatrix} 1 + 0 + 0 + 1 \\ 2 + 0 + 0 + 4 \\ 1 + 0 + 0 + 3 \end{bmatrix} = \begin{bmatrix} 2 \\ 6 \\ 4 \end{bmatrix}", font_size=46),
            Tex(r"$A\mathbf{w} \ne \mathbf{0}$, luego $\mathbf{w} \notin \ker A$.", font_size=42, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.4)
        fila2 = VGroup(v2, calculo2).arrange(RIGHT, buff=0.8).next_to(matriz_a, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(matriz_a, fila2), margen=0.5)
        self.decir("Con el vector uno, cero, cero, uno, en cambio, sale dos, seis, cuatro. No es el vector nulo, así que uve doble no está en el núcleo. Basta que una sola componente no sea cero.")
        self.play(FadeIn(v2))
        self.play(Write(calculo2[0]))
        self.play(FadeIn(calculo2[1]))
        self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Atajo: combinar elementos del núcleo")
        atajo = VGroup(
            MathTex(r"\mathbf{n}_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix},\quad \mathbf{n}_2 = \begin{bmatrix} -1 \\ 0 \\ -2 \\ 1 \end{bmatrix} \ \in \ker A", font_size=44),
            MathTex(r"\mathbf{n}_1 + \mathbf{n}_2 = \begin{bmatrix} -3 \\ 1 \\ -2 \\ 1 \end{bmatrix} = \mathbf{v}", font_size=44, color=COLOR_PIVOTE),
            Tex(r"Como el núcleo es un subespacio, cualquier combinación $s\,\mathbf{n}_1 + t\,\mathbf{n}_2$ también está en él.", font_size=36, color=COLOR_SECUNDARIO),
            Tex(r"(En la lección siguiente veremos de dónde salen $\mathbf{n}_1$ y $\mathbf{n}_2$.)", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(atajo, margen=0.5)
        self.decir("Hay un atajo. El vector ve resulta ser la suma de estos dos vectores del núcleo, ene uno y ene dos. Como el núcleo es un subespacio, cualquier combinación de ellos también está en él. De dónde salen ene uno y ene dos lo veremos en la lección siguiente.")
        for a in atajo:
            self.play(FadeIn(a))
            self.wait(2.2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Dos formas de preguntar lo mismo")
        equivalencias = VGroup(
            MathTex(r"\mathbf{x} \in \ker A", font_size=52, color=COLOR_PIVOTE),
            MathTex(r"\iff A\mathbf{x} = \mathbf{0}", font_size=46),
            MathTex(r"\iff \mathbf{x} \text{ es solución del sistema homogéneo}", font_size=42),
            MathTex(r"\iff x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n = \mathbf{0} \ \text{ (relación entre las columnas de } A\text{)}", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(equivalencias, margen=0.5)
        self.decir("Estar en el núcleo es lo mismo que cumplir a por equis igual a cero, es decir, ser solución del sistema homogéneo. Y, leyendo por columnas, es lo mismo que una relación entre las columnas de a: una combinación de las columnas, con coeficientes equis, que da cero. Esa lectura por columnas la usaremos más adelante.")
        for e in equivalencias:
            self.play(FadeIn(e))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F13-N2-02",
            VGroup(
                Text("¿Cuáles de estos vectores están en el núcleo de A?", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}", font_size=44),
                MathTex(r"\mathbf{a} = (1, 0, 0, 1) \qquad \mathbf{b} = (-3, 1, -2, 1)", font_size=44),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: decide cuáles de estos dos vectores están en el núcleo de la matriz. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "x está en ker A ⇔ A x = 0.",
                "Se comprueba multiplicando: todas las componentes deben dar 0.",
                "Es lo mismo que una relación entre las columnas de A.",
            ],
            "Lección 46 — una base del núcleo y la nulidad.",
            voz="En resumen: equis está en el núcleo exactamente cuando a por equis es cero. Se comprueba multiplicando, y todas las componentes deben dar cero. Es lo mismo que una relación entre las columnas de a. Siguiente: lección cuarenta y seis, una base del núcleo y la nulidad.",
        )
