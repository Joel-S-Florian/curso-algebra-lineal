"""Lección 23 — Matriz aumentada y sistemas equivalentes.

Escenas (un video cada una):
    SistemaAMatrizAumentada, SistemasEquivalentes

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l23_matriz_aumentada.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz_aumentada, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def colorear_aumentada(m: Matrix) -> Matrix:
    columnas = m.get_columns()
    for c in columnas[:-1]:
        c.set_color(COLOR_COEFICIENTE)
    columnas[-1].set_color(COLOR_TERMINO_INDEP)
    return m


class SistemaAMatrizAumentada(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 23 · Parte 1", "La matriz aumentada [A | b]")
        titulo = self.encabezado("Todo el sistema en una sola tabla")
        sistema = sistema_con_llave(("2x + y - z", "=", "2"), ("x - 3y + 2z", "=", "0"), ("4x + z", "=", "5"), font_size=42, colores=False)
        sistema.to_edge(LEFT, buff=0.9).shift(UP * 0.6)
        aumentada = colorear_aumentada(matriz_aumentada([["2", "1", "-1", "2"], ["1", "-3", "2", "0"], ["4", "0", "1", "5"]]))
        aumentada.to_edge(RIGHT, buff=1.4).shift(UP * 0.6)
        self.decir("Todo el sistema cabe en una sola tabla.")
        self.play(Write(sistema))
        self.play(GrowArrow(Arrow(sistema.get_right(), aumentada.get_left(), buff=0.4)))
        self.play(FadeIn(aumentada.get_brackets()), Create(aumentada.separador))
        self.decir("Cada ecuación se convierte en una fila: los coeficientes, y tras la barra, el término independiente.")
        for i in range(3):
            self.play(Indicate(sistema[1][i]), TransformFromCopy(sistema[1][i], aumentada.get_rows()[i]), run_time=1.3)
        self.consolidar(aumentada)
        llave_a = Brace(VGroup(*aumentada.get_columns()[:3]), DOWN, color=COLOR_COEFICIENTE)
        llave_b = Brace(aumentada.get_columns()[3], DOWN, color=COLOR_TERMINO_INDEP)
        rot = VGroup(
            MathTex("A", color=COLOR_COEFICIENTE).next_to(llave_a, DOWN),
            MathTex(r"\mathbf{b}", color=COLOR_TERMINO_INDEP).next_to(llave_b, DOWN),
        )
        self.decir("A la izquierda de la barra está a; a la derecha, be. Es la matriz aumentada.")
        self.play(GrowFromCenter(llave_a), GrowFromCenter(llave_b), FadeIn(rot))
        dimension = MathTex(r"[A \mid \mathbf{b}] \text{ es } 3\times 4", font_size=44).next_to(rot, DOWN, buff=0.5).set_x(aumentada.get_x())
        self.decir("Con tres ecuaciones y tres incógnitas, es de tres por cuatro: tiene una columna más que a.")
        self.play(Write(dimension))
        self.pie(
            "MATRIZ AUMENTADA: A con b añadida como última columna; la barra recuerda dónde estaba el «=».\n"
            "Con m ecuaciones y n incógnitas es m × (n + 1).",
            espera=5,
        )
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Leer al revés: de la matriz al sistema")
        m = colorear_aumentada(matriz_aumentada([["1", "0", "2", "3"], ["0", "1", "-1", "4"]]))
        m.shift(LEFT * 3.5)
        self.decir("También se puede leer al revés: de la matriz al sistema.")
        self.play(FadeIn(m))
        cabeceras = VGroup(*[MathTex(v, font_size=38, color=COLOR_SECUNDARIO).next_to(c, UP, buff=0.4) for v, c in zip(("x", "y", "z"), m.get_columns()[:3])])
        self.decir("Cada columna es una incógnita: equis, ye, zeta.")
        self.play(FadeIn(cabeceras))
        sistema = sistema_con_llave(("x + 2z", "=", "3"), ("y - z", "=", "4"), font_size=46, colores=False).shift(RIGHT * 3)
        self.decir("La primera fila dice equis más dos zeta igual a tres; la segunda, ye menos zeta igual a cuatro. Un cero significa que esa incógnita no aparece en esa ecuación.")
        self.play(TransformFromCopy(m, sistema), run_time=2)
        self.pie("Cada columna es una incógnita. Un 0 significa que esa incógnita no aparece en esa ecuación.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "A frente a [A | b]")
        izq = VGroup(
            sistema_con_llave(("2x + y - z", "=", "2"), ("x - 3y + 2z", "=", "0"), ("4x + z", "=", "5"), font_size=34, colores=False),
            colorear_aumentada(matriz_aumentada([["2", "1", "-1", "2"], ["1", "-3", "2", "0"], ["4", "0", "1", "5"]])).scale(0.8),
            Text("solución (1, 1, 1)", font_size=TAM_NOTA, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.4)
        der = VGroup(
            sistema_con_llave(("2x + y - z", "=", "0"), ("x - 3y + 2z", "=", "0"), ("4x + z", "=", "0"), font_size=34, colores=False),
            colorear_aumentada(matriz_aumentada([["2", "1", "-1", "0"], ["1", "-3", "2", "0"], ["4", "0", "1", "0"]])).scale(0.8),
            Text("homogéneo: (0, 0, 0) es solución", font_size=TAM_NOTA, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.4)
        VGroup(izq, der).arrange(RIGHT, buff=1.5).shift(DOWN * 0.1)
        self.decir("Este sistema tiene la solución uno, uno, uno.")
        self.play(FadeIn(izq))
        self.decir("Este otro tiene la misma matriz a, pero be es cero: es homogéneo, y cero, cero, cero es solución.")
        self.play(FadeIn(der))
        marcas = VGroup(*[SurroundingRectangle(VGroup(*g[1].get_columns()[:3]), color=COLOR_COEFICIENTE) for g in (izq, der)])
        self.decir("Misma matriz a, distintas soluciones: a sola no basta, hace falta be.")
        self.play(Create(marcas))
        self.pie(
            "Los dos sistemas tienen la MISMA matriz A pero distinto b, y distintas soluciones:\n"
            "A sola no basta para resolver; [A | b] contiene toda la información.",
            espera=5,
        )
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Olvidar los ceros: \ $x + 2z = 3$ da la fila $[\,1 \ \ 0 \ \ 2 \mid 3\,]$, no $[\,1 \ \ 2 \mid 3\,]$.", font_size=36),
            Tex(r"Escribir $\mathbf{b}$ antes de pasar los términos: \ $x + y = 3 - z$ \ no da $[\,1 \ \ 1 \ \ 0 \mid 3\,]$.", font_size=36),
            Tex(r"Confundir dimensiones: \ $[A\mid\mathbf{b}]$ tiene una columna más que $A$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes: olvidar los ceros de las incógnitas que faltan; escribir be antes de pasar todos los términos con incógnitas a la izquierda; y confundir dimensiones: la aumentada tiene una columna más que a.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F07-N1-02",
            VGroup(
                Text("Escribe la matriz aumentada del sistema y, al revés, el sistema de la matriz:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \begin{cases} x - y = 4 - z \\ 2y + 3z = 1 \\ x = 2y \end{cases} \qquad"
                    r"\text{b) } \left[\begin{array}{ccc|c} 3 & 0 & -1 & 2 \\ 0 & 0 & 5 & -4 \end{array}\right]",
                    font_size=44,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "[A | b]: matriz de coeficientes con b como última columna (m × (n + 1)).",
                "Cada fila es una ecuación; cada columna, una incógnita (la última, b).",
                "A sola no determina las soluciones: hace falta b.",
            ],
            "sistemas equivalentes.",
            voz="En resumen: la matriz aumentada es la matriz de coeficientes con be como última columna, y tiene una columna más que a. Cada fila es una ecuación, y cada columna, una incógnita, salvo la última, que es be. Y a sola no determina las soluciones: hace falta be. Siguiente: sistemas equivalentes.",
        )


class SistemasEquivalentes(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 23 · Parte 2", "Sistemas equivalentes y filas")
        titulo = self.encabezado("Mismas soluciones, distinto aspecto")
        definicion = Tex(r"Dos sistemas con las mismas incógnitas son \textbf{equivalentes} si tienen \textbf{el mismo conjunto de soluciones}.", font_size=36)
        definicion.next_to(titulo, DOWN, buff=0.5)
        self.decir("Dos sistemas con las mismas incógnitas son equivalentes si tienen el mismo conjunto de soluciones.")
        self.play(FadeIn(definicion))
        original = colorear_aumentada(matriz_aumentada([["1", "1", "1", "6"], ["1", "-1", "1", "2"], ["1", "1", "-1", "0"]]))
        reducida = colorear_aumentada(matriz_aumentada([["1", "1", "1", "6"], ["0", "-2", "0", "-4"], ["0", "0", "-2", "-6"]]))
        simbolo = MathTex(r"\sim", font_size=72)
        fila = VGroup(original, simbolo, reducida).arrange(RIGHT, buff=1.2).shift(DOWN * 0.3)
        self.decir("Partamos de esta matriz aumentada.")
        self.play(FadeIn(original))
        ops = VGroup(
            MathTex(r"R_2 \leftarrow R_2 - R_1", font_size=34, color=COLOR_OPERACION),
            MathTex(r"R_3 \leftarrow R_3 - R_1", font_size=34, color=COLOR_OPERACION),
        ).arrange(DOWN, buff=0.2).next_to(simbolo, UP, buff=0.4)
        self.decir("Restar la primera ecuación a la segunda es restar la primera fila a la segunda. Y lo mismo con la tercera.")
        self.play(FadeIn(ops), Write(simbolo))
        self.play(FadeIn(reducida.get_brackets()), Create(reducida.separador), TransformFromCopy(original.get_rows()[0], reducida.get_rows()[0]))
        for i in (1, 2):
            self.play(TransformFromCopy(VGroup(original.get_rows()[i], original.get_rows()[0]), reducida.get_rows()[i]), run_time=1.5)
        self.consolidar(reducida)
        self.decir("Es la reducción de la lección quince, hecha solo con números. El símbolo de equivalencia indica que las matrices son distintas, pero los sistemas tienen las mismas soluciones.")
        self.pie(
            "Es la reducción de la Lección 15, hecha solo con números: «restar la ecuación 1» es «restar la fila 1» (R = fila).\n"
            "El símbolo ~ indica sistemas equivalentes: las matrices son distintas, las soluciones no.",
            espera=5,
        )
        comprobacion = VGroup(
            MathTex(r"\text{original con } (1, 2, 3):\ \ 1 + 2 + 3 = 6,\ \ 1 - 2 + 3 = 2,\ \ 1 + 2 - 3 = 0\ \checkmark", font_size=34, color=COLOR_SOLUCION),
            MathTex(r"\text{nuevo con } (1, 2, 3):\ \ 6\ \checkmark,\ \ -2\cdot 2 = -4\ \checkmark,\ \ -2\cdot 3 = -6\ \checkmark", font_size=34, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.3).next_to(fila, DOWN, buff=0.5)
        ajustar_al_encuadre(comprobacion)
        self.quitar_pie()
        self.decir("Uno, dos, tres cumple los dos sistemas.")
        self.play(FadeIn(comprobacion))
        self.wait(4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El sistema de la derecha se resuelve de abajo arriba")
        reducida = colorear_aumentada(matriz_aumentada([["1", "1", "1", "6"], ["0", "-2", "0", "-4"], ["0", "0", "-2", "-6"]])).shift(LEFT * 3.5)
        self.decir("El sistema de la derecha se resuelve de abajo arriba.")
        self.play(FadeIn(reducida))
        pasos = VGroup(
            MathTex(r"-2z = -6 \;\Rightarrow\; z = 3", font_size=42),
            MathTex(r"-2y = -4 \;\Rightarrow\; y = 2", font_size=42),
            MathTex(r"x + 2 + 3 = 6 \;\Rightarrow\; x = 1", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(RIGHT * 2.8)
        self.decir("La última fila dice menos dos zeta igual a menos seis: zeta vale tres. La segunda, menos dos ye igual a menos cuatro: ye vale dos. Y la primera, equis más dos más tres igual a seis: equis vale uno.")
        for i, p in zip((2, 1, 0), pasos):
            marco = SurroundingRectangle(reducida.get_rows()[i], color=COLOR_PIVOTE)
            self.play(Create(marco), Write(p))
            self.wait(1)
            self.play(FadeOut(marco))
        self.decir("Se resuelve así gracias a los ceros bajo la diagonal. Llegar ahí con operaciones permitidas es la eliminación de Gauss.")
        self.pie(
            "Los ceros bajo la diagonal hacen que la última fila tenga una sola incógnita.\n"
            "Llegar a esa forma con operaciones permitidas sobre las filas es la eliminación de Gauss (Unidad 4).",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F07-N3-01",
            VGroup(
                MathTex(r"\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & 1 & 0 \end{array}\right] \sim \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -5 & ? \end{array}\right]", font_size=48),
                Tex(r"a) ¿Qué operación $R_2 \leftarrow R_2 - k R_1$ se aplicó? ¿Qué número va en ``?''?", font_size=38),
                Tex(r"b) Resuelve el sistema.", font_size=38),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Sistemas equivalentes: mismo conjunto de soluciones.",
                "Operar con ecuaciones = operar con las filas de [A | b].",
                "Con ceros bajo la diagonal, el sistema se resuelve de abajo arriba.",
            ],
            "Unidad 4, Lección 24 — operaciones elementales por filas.",
            voz="En resumen: dos sistemas son equivalentes si tienen el mismo conjunto de soluciones. Operar con ecuaciones es operar con las filas de la matriz aumentada. Y con ceros bajo la diagonal, el sistema se resuelve de abajo arriba. Siguiente: unidad cuatro, lección veinticuatro, operaciones elementales por filas.",
        )
