"""Lección 41 — Clasificación con ejemplos y árbol de decisión.

Escenas (un video cada una):
    EjemplosClasificados, ArbolDeDecision

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l41_clasificacion_con_ejemplos.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def ejemplo(sistema_tex, datos, pivotes, rangos_tex, conclusion, color, solucion_tex=None):
    """Sistema, su reducida, los rangos y la conclusión, en una columna."""
    s = MathTex(sistema_tex, font_size=34)
    m = matriz_gauss(datos, pivotes=pivotes, escala=0.62)
    r = MathTex(rangos_tex, font_size=30)
    c = Text(conclusion, font_size=TAM_NOTA, color=color, weight="BOLD")
    partes = [s, m, r, c]
    if solucion_tex:
        partes.append(MathTex(solucion_tex, font_size=30, color=COLOR_SOLUCION))
    return VGroup(*partes).arrange(DOWN, buff=0.3)


def caja(texto, color=WHITE, ancho=3.2):
    t = Text(texto, font_size=TAM_NOTA - 2, color=color, line_spacing=1.05)
    r = RoundedRectangle(corner_radius=0.12, width=max(ancho, t.width + 0.4), height=t.height + 0.4, color=color)
    return VGroup(r, t)


class EjemplosClasificados(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 41 · Parte 1", "Clasificar con ejemplos")
        titulo = self.encabezado("Cuatro sistemas, dos rangos cada uno")
        ejemplos = VGroup(
            ejemplo(r"\begin{cases} x + y + z = 6 \\ x - y + z = 2 \\ x + y - z = 0 \end{cases}",
                    [[1, 0, 0, 1], [0, 1, 0, 2], [0, 0, 1, 3]], [(0, 0), (1, 1), (2, 2)],
                    r"\operatorname{rg}A = \operatorname{rg}[A|b] = 3 = n", "SCD", COLOR_SOLUCION, r"(1, 2, 3)"),
            ejemplo(r"\begin{cases} x + y + z + w = 4 \\ x + 2y + 3z + 4w = 10 \\ 2x + 3y + 4z + 5w = 14 \end{cases}",
                    [[1, 0, -1, -2, -2], [0, 1, 2, 3, 6], [0, 0, 0, 0, 0]], [(0, 0), (1, 1)],
                    r"\operatorname{rg}A = \operatorname{rg}[A|b] = 2 < 4", "SCI (2 parámetros)", COLOR_LIBRE),
            ejemplo(r"\begin{cases} x + y = 2 \\ x - y = 0 \\ 2x + y = 4 \end{cases}",
                    [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [(0, 0), (1, 1), (2, 2)],
                    r"\operatorname{rg}A = 2 \ne 3 = \operatorname{rg}[A|b]", "SI", COLOR_ERROR),
            ejemplo(r"\begin{cases} x + y + z = 1 \\ x + y + z = 3 \end{cases}",
                    [[1, 1, 1, 0], [0, 0, 0, 1]], [(0, 0), (1, 3)],
                    r"\operatorname{rg}A = 1 \ne 2 = \operatorname{rg}[A|b]", "SI", COLOR_ERROR),
        ).arrange(RIGHT, buff=0.35, aligned_edge=UP).next_to(titulo, DOWN, buff=0.35)
        ajustar_al_encuadre(ejemplos, margen=0.3)
        frases = (
            "Primer sistema: tres ecuaciones con tres incógnitas. Los dos rangos valen tres, y hay tres incógnitas: compatible determinado. La solución es uno, dos, tres.",
            "Segundo sistema: tres ecuaciones con cuatro incógnitas. Los dos rangos valen dos: es compatible, con cuatro menos dos, dos parámetros. Compatible indeterminado.",
            "Tercero: tres ecuaciones con dos incógnitas. El rango de a vale dos, pero el de la aumentada, tres: incompatible. En efecto, equis igual a uno, ye igual a uno, no cumplen la tercera.",
            "Y cuarto: dos ecuaciones con tres incógnitas que se contradicen. El rango de a vale uno, y el de la aumentada, dos: incompatible. Tener menos ecuaciones que incógnitas no garantiza que haya solución.",
        )
        for e, frase in zip(ejemplos, frases):
            self.decir(frase)
            self.play(FadeIn(e))
            self.wait(1.5)
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que cada ejemplo enseña")
        lecciones = VGroup(
            Tex(r"Ejemplo 1: $m = n$ no basta para ser SCD; lo decide el rango (aquí, $r = 3$).", font_size=34),
            Tex(r"Ejemplo 2: una ecuación puede sobrar ($E_3 = E_1 + E_2$): $r = 2 < m = 3$.", font_size=34),
            Tex(r"Ejemplo 3: $m > n$ puede ser SI aunque cada pareja de ecuaciones tenga solución.", font_size=34),
            Tex(r"Ejemplo 4: $m < n$ puede ser SI: nunca SCD, pero tampoco siempre SCI.", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(lecciones, margen=0.5)
        self.decir("Lo que enseña cada ejemplo. Primero: que haya tantas ecuaciones como incógnitas no basta para que sea determinado; lo decide el rango. Segundo: una ecuación puede sobrar, y entonces el rango es menor que el número de ecuaciones. Tercero: con más ecuaciones que incógnitas puede ser incompatible. Y cuarto: con menos ecuaciones que incógnitas, nunca hay solución única, pero puede ser incompatible.")
        for l in lecciones:
            self.play(FadeIn(l))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N2-04",
            VGroup(
                Text("Clasifica con los rangos y, si es compatible, da la solución:", font_size=TAM_TEXTO),
                MathTex(r"\text{a) } \begin{cases} x + 2y - z = 1 \\ 2x + 4y - 2z = 2 \end{cases}\quad \text{b) } \begin{cases} x + 2y = 3 \\ 2x + 4y = 7 \end{cases}\quad \text{c) } \begin{cases} x + y = 1 \\ x - y = 3 \\ 2x + y = 3 \end{cases}", font_size=32),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: clasifica estos tres sistemas calculando los dos rangos y, si son compatibles, da la solución. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Se calculan rg(A) y rg[A | b], y se compara con n.",
                "El número de ecuaciones por sí solo no clasifica (L12).",
                "m < n: nunca SCD; m > n: puede ser de cualquier tipo.",
            ],
            "un árbol de decisión.",
            voz="En resumen: se calculan los rangos de a y de la aumentada, y se comparan con ene. El número de ecuaciones por sí solo no clasifica. Con menos ecuaciones que incógnitas nunca hay solución única, y con más, puede pasar cualquier cosa. Siguiente: un árbol de decisión.",
        )


class ArbolDeDecision(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 41 · Parte 2", "Árbol de decisión")
        titulo = self.encabezado("Tres preguntas bastan")
        p1 = caja("¿rg(A) = rg[A | b]?", COLOR_PIVOTE, 3.8).shift(UP * 1.6)
        si = caja("INCOMPATIBLE (SI)\nninguna solución", COLOR_ERROR, 3.4).shift(RIGHT * 4.6 + UP * 0.2)
        p2 = caja("¿rg(A) = n?", COLOR_PIVOTE, 3.0).shift(LEFT * 2.6 + DOWN * 0.1)
        scd = caja("SCD\nuna solución", COLOR_SOLUCION, 2.6).shift(LEFT * 5.2 + DOWN * 2.1)
        sci = caja("SCI\ninfinitas, n − r parámetros", COLOR_LIBRE, 3.6).shift(LEFT * 0.2 + DOWN * 2.1)
        e1 = Arrow(p1.get_bottom(), p2.get_top(), buff=0.1)
        e2 = Arrow(p1.get_right(), si.get_top(), buff=0.1)
        e3 = Arrow(p2.get_bottom(), scd.get_top(), buff=0.1)
        e4 = Arrow(p2.get_bottom(), sci.get_top(), buff=0.1)
        etiquetas = VGroup(
            Text("sí", font_size=TAM_NOTA - 4, color=COLOR_SECUNDARIO).next_to(e1.get_center(), LEFT, buff=0.1),
            Text("no", font_size=TAM_NOTA - 4, color=COLOR_SECUNDARIO).next_to(e2.get_center(), UP, buff=0.1),
            Text("sí", font_size=TAM_NOTA - 4, color=COLOR_SECUNDARIO).next_to(e3.get_center(), LEFT, buff=0.1),
            Text("no", font_size=TAM_NOTA - 4, color=COLOR_SECUNDARIO).next_to(e4.get_center(), RIGHT, buff=0.1),
        )
        arbol = VGroup(p1, si, p2, scd, sci, e1, e2, e3, e4, etiquetas)
        ajustar_al_encuadre(arbol, margen=0.5)
        self.decir("El teorema se resume en un árbol de decisión. Primera pregunta: ¿el rango de a es igual al de la aumentada? Si no, el sistema es incompatible, y no hay nada más que decir.")
        self.play(FadeIn(p1))
        self.play(GrowArrow(e2), FadeIn(etiquetas[1]), FadeIn(si))
        self.decir("Si sí, segunda pregunta: ¿el rango es igual al número de incógnitas? Si es así, compatible determinado: una solución. Y si no, compatible indeterminado: infinitas soluciones, con ene menos erre parámetros.")
        self.play(GrowArrow(e1), FadeIn(etiquetas[0]), FadeIn(p2))
        self.play(GrowArrow(e3), FadeIn(etiquetas[2]), FadeIn(scd))
        self.play(GrowArrow(e4), FadeIn(etiquetas[3]), FadeIn(sci))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Atajos")
        atajos = VGroup(
            Tex(r"$m < n$: nunca SCD. Si es compatible, es SCI con $n - r \ge n - m \ge 1$ parámetros.", font_size=34),
            Tex(r"$\operatorname{rg}(A) = m$: siempre compatible (para todo $\mathbf{b}$).", font_size=34),
            Tex(r"Homogéneo: siempre compatible; SCD (solo la trivial) $\iff r = n$.", font_size=34),
            Tex(r"$m = n$ y $r = n$: siempre SCD, para cualquier $\mathbf{b}$.", font_size=34, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(atajos, margen=0.5)
        self.decir("Algunos atajos. Con menos ecuaciones que incógnitas, nunca es determinado; si es compatible, tiene al menos ene menos eme parámetros. Si el rango es igual al número de ecuaciones, siempre es compatible. Un sistema homogéneo siempre es compatible, y solo tiene la solución trivial si el rango es ene. Y con tantas ecuaciones como incógnitas y rango ene, siempre es determinado, para cualquier be.")
        for a in atajos:
            self.play(FadeIn(a))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N3-04",
            VGroup(
                Text("Un sistema tiene 3 ecuaciones y 5 incógnitas; otro, 5 ecuaciones y 3 incógnitas.", font_size=TAM_TEXTO),
                Text("¿Qué clasificaciones (SCD, SCI, SI) son posibles en cada caso? Da un ejemplo de cada una.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: un sistema tiene tres ecuaciones y cinco incógnitas, y otro, cinco ecuaciones y tres incógnitas. ¿Qué clasificaciones son posibles en cada caso? Da un ejemplo de cada una. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Primero: ¿rg(A) = rg[A | b]? Si no, SI.",
                "Después: ¿rg(A) = n? Si sí, SCD; si no, SCI con n − r parámetros.",
                "Atajos: m < n nunca SCD; rg(A) = m siempre compatible.",
            ],
            "Lección 42 — discusión con parámetros.",
            voz="En resumen: primero, ¿el rango de a es igual al de la aumentada? Si no, incompatible. Después, ¿el rango es ene? Si es así, determinado; si no, indeterminado, con ene menos erre parámetros. Y hay atajos: con menos ecuaciones que incógnitas nunca es determinado, y si el rango es eme, siempre es compatible. Siguiente: lección cuarenta y dos, discusión con parámetros.",
        )
