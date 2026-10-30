"""Lección 33 — Gauss frente a Gauss-Jordan.

Escenas (un video cada una):
    ContarOperaciones, CuandoConvieneCadaUno

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l33_gauss_frente_a_jordan.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def gauss(n: int) -> int:
    """Multiplicaciones y divisiones de Gauss + sustitución hacia atrás (n×n, una columna b, sin pivoteo)."""
    return (n**3 + 3 * n**2 - n) // 3


def jordan(n: int) -> int:
    """Lo mismo para Gauss-Jordan (comprobado con un contador en ejercicios/verificar/f09.py)."""
    return (n**3 + n**2) // 2


def cuadricula(n: int, arriba: bool) -> VGroup:
    """Parte de coeficientes de una matriz n×n: pivotes, ceros fabricados debajo (y encima si `arriba`)."""
    celdas = VGroup()
    for i in range(n):
        for j in range(n):
            if i == j:
                color, opacidad = COLOR_PIVOTE, 0.9
            elif i > j:
                color, opacidad = COLOR_SOLUCION, 0.8
            elif arriba:
                color, opacidad = COLOR_TERMINO_INDEP, 0.8
            else:
                color, opacidad = COLOR_SECUNDARIO, 0.25
            celdas.add(Square(0.46, stroke_width=1, stroke_color=WHITE, fill_color=color, fill_opacity=opacidad))
    return celdas.arrange_in_grid(rows=n, cols=n, buff=0)


class ContarOperaciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 33 · Parte 1", "¿Cuánto cuesta cada método?")
        titulo = self.encabezado("Gauss frente a Gauss-Jordan: los ceros")
        g, j = cuadricula(5, False), cuadricula(5, True)
        etiqueta_g = Text("Gauss: ceros debajo", font_size=TAM_NOTA + 2, color=COLOR_SOLUCION).next_to(g, UP, buff=0.35)
        etiqueta_j = Text("Gauss-Jordan: debajo y encima", font_size=TAM_NOTA + 2, color=COLOR_TERMINO_INDEP).next_to(j, UP, buff=0.35)
        izquierda, derecha = VGroup(etiqueta_g, g), VGroup(etiqueta_j, j)
        VGroup(izquierda, derecha).arrange(RIGHT, buff=1.6, aligned_edge=UP).shift(DOWN * 0.3)
        cuentas = VGroup(
            MathTex(r"\tfrac{n(n-1)}{2}\ \text{ceros}", font_size=36, color=COLOR_SOLUCION).next_to(g, DOWN, buff=0.35),
            MathTex(r"n(n-1)\ \text{ceros}", font_size=36, color=COLOR_TERMINO_INDEP).next_to(j, DOWN, buff=0.35),
        )
        self.decir("Gauss y Gauss-Jordan resuelven los mismos sistemas, pero no cuestan lo mismo. Fijémonos en una matriz de cinco por cinco. Gauss solo fabrica ceros debajo de la diagonal, que son los verdes.")
        self.play(FadeIn(izquierda))
        self.play(FadeIn(cuentas[0]))
        self.decir("Gauss-Jordan también los fabrica encima, los naranjas. Para una matriz de ene por ene, Gauss hace ene por ene menos uno, entre dos ceros; Gauss-Jordan, el doble.")
        self.play(FadeIn(derecha))
        self.play(FadeIn(cuentas[1]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Contar multiplicaciones y divisiones")
        convenio = Tex(r"Se cuentan las multiplicaciones y divisiones (sin pivoteo, una columna $\mathbf{b}$, $n \times n$).", font_size=34, color=COLOR_SECUNDARIO).next_to(titulo, DOWN, buff=0.5)
        formulas = VGroup(
            MathTex(r"\text{Gauss + sustitución:}\quad \frac{n(n-1)(2n+5)}{6} + \frac{n(n+1)}{2} = \frac{n^3 + 3n^2 - n}{3} \approx \frac{n^3}{3}", font_size=36, color=COLOR_SOLUCION),
            MathTex(r"\text{Gauss-Jordan:}\quad \sum_{k=1}^{n} n\,(n - k + 1) = \frac{n^2(n+1)}{2} = \frac{n^3 + n^2}{2} \approx \frac{n^3}{2}", font_size=36, color=COLOR_TERMINO_INDEP),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(convenio, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(convenio, formulas))
        self.decir("Contemos las multiplicaciones y divisiones, que son las operaciones caras. Para un sistema de ene por ene con una columna de términos independientes, y sin intercambios de filas.")
        self.play(FadeIn(convenio))
        self.wait(1)
        self.decir("Gauss con sustitución hacia atrás hace ene por ene menos uno por dos ene más cinco, entre seis, en la eliminación, más ene por ene más uno entre dos en la sustitución: en total, ene cubo más tres ene cuadrado menos ene, entre tres. Aproximadamente, ene cubo entre tres.")
        self.play(Write(formulas[0]))
        self.wait(1)
        self.decir("Gauss-Jordan hace, en cada pivote, ene por ene menos ka más uno operaciones: en total, ene cuadrado por ene más uno, entre dos. Aproximadamente, ene cubo entre dos.")
        self.play(Write(formulas[1]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Con números")
        filas = [("n", "Gauss", "Gauss-Jordan", "cociente")]
        for n in (3, 10, 100, 1000):
            filas.append((str(n), f"{gauss(n):,}".replace(",", " "), f"{jordan(n):,}".replace(",", " "), f"{jordan(n) / gauss(n):.2f}"))
        tabla = VGroup(*[Text(t, font_size=TAM_TEXTO, weight="BOLD" if i == 0 else "NORMAL", color=COLOR_SECUNDARIO if i == 0 else WHITE) for i, f in enumerate(filas) for t in f])
        tabla.arrange_in_grid(rows=len(filas), cols=4, buff=(1.0, 0.4), col_alignments="rrrr").next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(tabla)
        self.decir("Con números. Para tres incógnitas, diecisiete operaciones frente a dieciocho: casi igual. Para diez, cuatrocientas treinta frente a quinientas cincuenta. Para cien, trescientas cuarenta y tres mil trescientas frente a quinientas cinco mil. Y para mil, más de trescientos treinta y cuatro millones frente a más de quinientos millones. El cociente se acerca a uno y medio.")
        self.play(FadeIn(tabla[:4]))
        for i in range(1, 5):
            self.play(FadeIn(tabla[4 * i: 4 * i + 4]))
            self.wait(1)
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El cociente tiende a 3/2")
        ejes = Axes(
            x_range=[0, 60, 10], y_range=[1, 1.6, 0.1], x_length=8, y_length=4.2,
            axis_config={"include_numbers": True, "font_size": 22},
        ).next_to(titulo, DOWN, buff=0.6).shift(LEFT * 1.2)
        curva = ejes.plot(lambda n: 3 * (n * n + n) / (2 * (n * n + 3 * n - 1)), x_range=[2, 60], color=COLOR_PIVOTE)
        limite = DashedLine(ejes.c2p(0, 1.5), ejes.c2p(60, 1.5), color=COLOR_TERMINO_INDEP)
        rot_limite = MathTex(r"\tfrac32", font_size=36, color=COLOR_TERMINO_INDEP).next_to(limite, RIGHT, buff=0.15)
        rot_ejes = VGroup(
            MathTex("n", font_size=32).next_to(ejes.x_axis.get_end(), DOWN, buff=0.25),
            Text("Jordan / Gauss", font_size=TAM_NOTA - 2, color=COLOR_SECUNDARIO).next_to(ejes.y_axis.get_end(), UP, buff=0.15),
        )
        formula = MathTex(r"\frac{n^3 + n^2}{2}\Big/\frac{n^3 + 3n^2 - n}{3} \;\longrightarrow\; \tfrac32", font_size=34, color=COLOR_PIVOTE).to_edge(RIGHT, buff=0.6).shift(UP * 0.3)
        ajustar_al_encuadre(VGroup(ejes, rot_limite, formula), margen=0.5)
        self.decir("Dibujemos el cociente entre las operaciones de Gauss-Jordan y las de Gauss, según el tamaño del sistema. Para sistemas pequeños casi no hay diferencia, pero al crecer ene el cociente sube hacia tres medios: Gauss-Jordan necesita un cincuenta por ciento más de operaciones.")
        self.play(Create(ejes), FadeIn(rot_ejes))
        self.play(Create(limite), FadeIn(rot_limite))
        self.play(Create(curva), Write(formula), run_time=3)
        self.pie("Para un solo sistema grande, Gauss con sustitución hacia atrás gasta aproximadamente dos tercios de las operaciones de Gauss-Jordan.", espera=3)
        self.wait(1)

        self.ejercicio_propuesto(
            "F09-N2-05",
            VGroup(
                Text("Con las fórmulas de la lección, calcula cuántas multiplicaciones y divisiones", font_size=TAM_TEXTO),
                Text("hacen Gauss y Gauss-Jordan en un sistema de n = 4 y de n = 5 incógnitas.", font_size=TAM_TEXTO),
                Text("¿Qué método gana y por cuánto?", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: con las fórmulas de la lección, calcula cuántas multiplicaciones y divisiones hacen Gauss y Gauss-Jordan en un sistema de cuatro y de cinco incógnitas. ¿Qué método gana, y por cuánto? Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Gauss + sustitución: unas n³/3 multiplicaciones y divisiones.",
                "Gauss-Jordan: unas n³/2, es decir, un 50 % más para n grande.",
                "Para n pequeño la diferencia es mínima (n = 3: 17 frente a 18).",
            ],
            "cuándo conviene cada uno.",
            voz="En resumen: Gauss con sustitución hacia atrás hace unas ene cubo entre tres multiplicaciones y divisiones. Gauss-Jordan, unas ene cubo entre dos: un cincuenta por ciento más cuando ene es grande. Y para ene pequeño la diferencia es mínima: con tres incógnitas, diecisiete frente a dieciocho. Siguiente: cuándo conviene cada uno.",
        )


class CuandoConvieneCadaUno(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 33 · Parte 2", "¿Cuándo conviene cada uno?")
        titulo = self.encabezado("Comparación")
        celdas = [
            ("", "Gauss + sustitución", "Gauss-Jordan"),
            ("Operaciones", "≈ n³/3", "≈ n³/2"),
            ("Resultado", "forma escalonada", "forma reducida (única)"),
            ("Leer la solución", "sustituyendo hacia atrás", "directamente"),
            ("Variables libres", "se despejan hacia atrás", "la paramétrica se lee en las filas"),
        ]
        colores = [WHITE, COLOR_SECUNDARIO, COLOR_SECUNDARIO, COLOR_SECUNDARIO, COLOR_SECUNDARIO]
        tabla = VGroup()
        for fila in celdas:
            for j, texto in enumerate(fila):
                tabla.add(Text(texto, font_size=TAM_NOTA, weight="BOLD" if fila is celdas[0] or j == 0 else "NORMAL",
                               color=(COLOR_SOLUCION if j == 1 else COLOR_TERMINO_INDEP) if fila is celdas[0] and j else WHITE))
        tabla.arrange_in_grid(rows=len(celdas), cols=3, buff=(0.7, 0.45), col_alignments="lll").next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(tabla)
        self.decir("Comparemos los dos métodos. Gauss con sustitución hace menos operaciones, unas ene cubo entre tres, frente a ene cubo entre dos.")
        self.play(FadeIn(tabla[:3]))
        self.play(FadeIn(tabla[3:6]))
        self.decir("Gauss deja una forma escalonada, de la que se lee la solución sustituyendo hacia atrás. Gauss-Jordan deja la forma reducida, que además es única, y de la que la solución se lee directamente.")
        self.play(FadeIn(tabla[6:12]))
        self.decir("Con variables libres, la reducida da la solución paramétrica leyendo las filas, sin sustituir.")
        self.play(FadeIn(tabla[12:]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué elegir")
        recomendacion = VGroup(
            parrafo(r"\textbf{A mano, sistemas pequeños:} Gauss-Jordan. Hay pocas operaciones de más", r"y la solución se lee sin sustituir; hay menos ocasiones de equivocarse al final.", font_size=34, sangria=0.5, color=COLOR_TERMINO_INDEP),
            parrafo(r"\textbf{Un sistema grande en ordenador:} Gauss con sustitución hacia atrás.", r"Hace aproximadamente un tercio menos de operaciones.", font_size=34, sangria=0.5, color=COLOR_SOLUCION),
            parrafo(r"\textbf{Comparar dos sistemas, o saber si dos son equivalentes:} la reducida,", r"porque es única (L31).", font_size=34, sangria=0.5, color=COLOR_PIVOTE),
            parrafo(r"\textbf{Muchos lados derechos con la misma $A$:} ni uno ni otro: la factorización", r"$LU$ (Unidad 6) reutiliza la eliminación.", font_size=34, sangria=0.5, color=COLOR_OPERACION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(recomendacion)
        frases = (
            "A mano, con sistemas pequeños, conviene Gauss-Jordan: hay pocas operaciones de más, y la solución se lee sin sustituir.",
            "Para un sistema grande en un ordenador, conviene Gauss con sustitución hacia atrás: hace un tercio menos de operaciones.",
            "Para comparar sistemas, o saber si dos son equivalentes, conviene la reducida, porque es única.",
            "Y si hay muchos lados derechos con la misma matriz, ni uno ni otro: la factorización ele u, de la unidad seis, reutiliza la eliminación.",
        )
        for r, frase in zip(recomendacion, frases):
            self.decir(frase)
            self.play(FadeIn(r))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que no cambia")
        igual = VGroup(
            Tex(r"Los dos usan las mismas tres operaciones elementales (L24).", font_size=38),
            Tex(r"Los dos dan el mismo conjunto solución y las mismas posiciones de pivote.", font_size=38),
            Tex(r"Los dos terminan igual: \textbf{verificar en el sistema original} (L30).", font_size=38, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(igual)
        self.decir("Lo que no cambia: los dos usan las mismas tres operaciones elementales, dan el mismo conjunto solución y las mismas posiciones de pivote. Y los dos terminan igual: verificando en el sistema original.")
        for i in igual:
            self.play(FadeIn(i))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F09-N3-06",
            VGroup(
                Text("Elige y justifica el método más adecuado en cada caso:", font_size=TAM_TEXTO),
                Text("a) Un sistema 2 × 2 resuelto a mano en un examen.", font_size=TAM_NOTA + 2),
                Text("b) Un sistema 2000 × 2000 en un ordenador.", font_size=TAM_NOTA + 2),
                Text("c) Decidir si dos sistemas con la misma matriz de coeficientes son equivalentes.", font_size=TAM_NOTA + 2),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4),
            voz="Ejercicio propuesto: elige y justifica el método más adecuado en cada caso. Uno: un sistema de dos por dos resuelto a mano en un examen. Dos: un sistema de dos mil por dos mil en un ordenador. Y tres: decidir si dos sistemas son equivalentes. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "A mano y sistemas pequeños: Gauss-Jordan (lectura directa).",
                "Sistemas grandes: Gauss con sustitución (menos operaciones).",
                "Comparar sistemas: la reducida, por ser única.",
                "Muchos lados derechos: factorización LU (Unidad 6).",
            ],
            "Unidad 6 — factorización LU.",
            voz="En resumen: a mano, con sistemas pequeños, conviene Gauss-Jordan, por su lectura directa. Para sistemas grandes, Gauss con sustitución hacia atrás, que hace menos operaciones. Para comparar sistemas, la reducida, porque es única. Y con muchos lados derechos, la factorización ele u. Siguiente: unidad seis, factorización ele u.",
        )
