"""Lección 25 — Forma escalonada y pivotes.

Escenas (un video cada una):
    FormaEscalonadaYPivotes, LaEscalonadaNoEsUnica

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l25_forma_escalonada.py -a
"""

import sys
from fractions import Fraction
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def ejemplo(filas, pivotes, valido: bool, motivo: str) -> VGroup:
    m = matriz(filas).scale(0.75)
    for i, j in pivotes:
        m.get_rows()[i][j].set_color(COLOR_PIVOTE)
    marca = MathTex(r"\checkmark" if valido else r"\times", font_size=56, color=COLOR_SOLUCION if valido else COLOR_ERROR)
    texto = Text(motivo, font_size=TAM_NOTA - 4, color=COLOR_SOLUCION if valido else COLOR_ERROR, line_spacing=1)
    return VGroup(m, marca, texto).arrange(DOWN, buff=0.3)


class FormaEscalonadaYPivotes(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 25 · Parte 1", "Forma escalonada y pivotes")
        titulo = self.encabezado("¿A qué forma queremos llegar?")
        m = matriz_gauss([[1, 1, 1, 6], [0, -2, 0, -4], [0, 0, -2, -6]]).shift(UP * 0.6)
        self.decir("¿A qué forma queremos llegar? A esta, la del final de la lección veintitrés.")
        self.play(FadeIn(m))
        pivotes = [(0, 0), (1, 1), (2, 2)]
        linea = escalera(m, pivotes)
        self.decir("Bajo la escalera solo hay ceros, y cada fila empieza más a la derecha que la anterior. Por eso se resuelve de abajo arriba.")
        self.play(Create(linea), *[m.get_rows()[i][j].animate.set_color(COLOR_PIVOTE) for i, j in pivotes], run_time=2)
        self.pie("Es la matriz del final de la L23: bajo la línea solo hay ceros y cada fila empieza más a la derecha que la anterior.\n"
                 "Por eso la última ecuación tiene una sola incógnita y el sistema se resuelve de abajo arriba.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición")
        definicion = VGroup(
            Tex(r"Una matriz está en \textbf{forma escalonada} si:", font_size=38),
            Tex(r"(1) las filas nulas (solo ceros), si las hay, están abajo;", font_size=38),
            parrafo(r"(2) la primera entrada no nula de cada fila está más a la derecha", r"que la primera entrada no nula de la fila de arriba.", font_size=38, sangria=0.55),
            Tex(r"Esa primera entrada no nula es el \textbf{pivote} de su fila.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Consecuencia de (2): debajo de cada pivote solo hay ceros.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(definicion)
        self.decir("Una matriz está en forma escalonada si las filas nulas, si las hay, están abajo, y si la primera entrada no nula de cada fila está más a la derecha que la de la fila de arriba. Esa primera entrada no nula es el pivote de su fila. Y, en consecuencia, debajo de cada pivote solo hay ceros.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(1.8)
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Escalonada o no?")
        ejemplos = VGroup(
            ejemplo([[1, 3, 2], [0, 0, 4], [0, 0, 0]], [(0, 0), (1, 2)], True, "sí: la escalera\npuede saltar columnas"),
            ejemplo([[1, 2, 3], [0, 0, 0], [0, 4, 5]], [], False, "no: hay una fila\nnula que no está abajo"),
            ejemplo([[2, 1, 0], [1, 3, 1], [0, 0, 1]], [], False, "no: debajo del 2\nhay un 1"),
            ejemplo([[0, 1, 2], [0, 0, 3], [0, 0, 0]], [(0, 1), (1, 2)], True, "sí: puede empezar\ncon una columna de ceros"),
        ).arrange(RIGHT, buff=0.6, aligned_edge=UP).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(ejemplos)
        self.decir("¿Escalonada o no? La primera sí: la escalera puede saltar columnas. La segunda no: hay una fila nula que no está abajo. La tercera no: debajo del dos hay un uno. Y la cuarta sí: puede empezar con una columna de ceros.")
        for e in ejemplos:
            self.play(FadeIn(e[0]))
            self.wait(1.2)
            self.play(FadeIn(e[1]), FadeIn(e[2]))
            self.wait(1.5)
        self.decir("Los pivotes no tienen que valer uno: basta con que sean distintos de cero.")
        self.pie("Los pivotes no tienen que valer 1: basta con que sean distintos de 0.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Columnas pivote y variables pivote")
        m = matriz_gauss([[1, 2, 0, -1, 3], [0, 0, 2, 4, 2], [0, 0, 0, 0, 0]]).shift(UP * 0.5 + LEFT * 2.5)
        nombres = ("x_1", "x_2", "x_3", "x_4")
        cabeceras = VGroup(*[MathTex(v, font_size=38, color=COLOR_SECUNDARIO).next_to(c, UP, buff=0.45) for v, c in zip(nombres, m.get_columns())])
        cabeceras.align_to(cabeceras[0], DOWN)
        self.decir("En esta matriz escalonada, cada columna corresponde a una incógnita: de equis uno a equis cuatro.")
        self.play(FadeIn(m), FadeIn(cabeceras))
        pivotes = [(0, 0), (1, 2)]
        self.decir("Los pivotes están en las columnas uno y tres.")
        self.play(Create(escalera(m, pivotes)), *[m.get_rows()[i][j].animate.set_color(COLOR_PIVOTE) for i, j in pivotes], run_time=2)
        self.play(cabeceras[0].animate.set_color(COLOR_PIVOTE), cabeceras[2].animate.set_color(COLOR_PIVOTE),
                  cabeceras[1].animate.set_color(COLOR_LIBRE), cabeceras[3].animate.set_color(COLOR_LIBRE))
        lectura = VGroup(
            Tex(r"Columnas pivote: 1 y 3", font_size=36),
            Tex(r"Variables pivote: $x_1,\ x_3$", font_size=36, color=COLOR_PIVOTE),
            Tex(r"Sin pivote: $x_2,\ x_4$\\ (serán \textbf{libres}, L28)", font_size=36, color=COLOR_LIBRE),
            Tex(r"2 pivotes, 4 incógnitas", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(m, RIGHT, buff=0.9)
        self.decir("Las columnas uno y tres son columnas pivote, y equis uno y equis tres son variables pivote. Equis dos y equis cuatro no tienen pivote: serán libres. Hay dos pivotes y cuatro incógnitas.")
        for t in lectura:
            self.play(FadeIn(t))
            self.wait(1.2)
        self.decir("La última fila es cero igual a cero: no aporta nada.")
        self.pie("Una columna pivote es la que contiene un pivote; su incógnita es una variable pivote.\nLa última fila es 0 = 0: no aporta nada (L27).", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Caso aparte: un pivote en la columna de b")
        m = matriz_gauss([[1, 2, 3], [0, 0, 5]], pivotes=[(0, 0), (1, 2)]).shift(UP * 0.6 + LEFT * 2)
        lectura = MathTex(r"0x + 0y = 5", font_size=44, color=COLOR_ERROR).next_to(m, RIGHT, buff=1).match_y(m.get_rows()[1])
        self.decir("Un caso aparte.")
        self.play(FadeIn(m))
        self.decir("Esta matriz aumentada está escalonada, pero su último pivote cae en la columna de be: la ecuación dice cero igual a cinco. El sistema no tiene solución.")
        self.play(Create(escalera(m, [(0, 0)])), Write(lectura))
        self.pie("La matriz [A | b] está escalonada, pero su último pivote cae en la columna de b: la ecuación dice 0 = 5.\n"
                 "Ese sistema no tiene solución; lo estudiaremos en la L28.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Exigir pivotes iguales a 1: basta con que sean distintos de 0 (Unidad 5).", font_size=34),
            Tex(r"Pensar que la escalera baja de columna en columna: puede saltar columnas.", font_size=34),
            Tex(r"Llamar pivote a cualquier entrada no nula: es la \textbf{primera} no nula de su fila.", font_size=34),
            Tex(r"Olvidar que las filas nulas deben ir al final.", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes: exigir pivotes iguales a uno; pensar que la escalera baja de columna en columna, cuando puede saltar columnas; llamar pivote a cualquier entrada no nula, cuando es la primera de su fila; y olvidar que las filas nulas van al final.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N1-02",
            VGroup(
                Text("¿Cuáles están en forma escalonada? En ellas, marca los pivotes y las columnas pivote.", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) }\begin{bmatrix} 3 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{bmatrix}\quad"
                    r"\text{b) }\begin{bmatrix} 1 & 2 \\ 0 & 0 \\ 0 & 5 \end{bmatrix}\quad"
                    r"\text{c) }\begin{bmatrix} 0 & 4 & 1 \\ 0 & 0 & 0 \end{bmatrix}\quad"
                    r"\text{d) }\begin{bmatrix} 1 & 0 & 2 \\ 1 & 3 & 0 \\ 0 & 0 & 4 \end{bmatrix}",
                    font_size=44,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Escalonada: filas nulas abajo y cada pivote a la derecha del de arriba (ceros debajo).",
                "Pivote: primera entrada no nula de una fila; basta con que sea distinto de 0.",
                "Columnas con pivote: variables pivote; las demás serán libres.",
            ],
            "la forma escalonada no es única.",
            voz="En resumen: una matriz es escalonada si las filas nulas están abajo y cada pivote está a la derecha del de arriba, con ceros debajo. El pivote es la primera entrada no nula de una fila; basta con que sea distinto de cero. Y las columnas con pivote dan las variables pivote; las demás serán libres. Siguiente: la forma escalonada no es única.",
        )


class LaEscalonadaNoEsUnica(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 25 · Parte 2", "La forma escalonada no es única")
        titulo = self.encabezado("Dos caminos desde la misma matriz")
        arriba, abajo = UP * 1.5, DOWN * 1.2
        ma = matriz_gauss([[2, 4, 10], [3, -1, 1]], pivotes=[(0, 0)]).move_to(LEFT * 3.2 + arriba)
        mb = matriz_gauss([[2, 4, 10], [3, -1, 1]]).move_to(LEFT * 3.2 + abajo)
        ha = VGroup(Text("Camino A", font_size=TAM_NOTA + 2, color=COLOR_SECUNDARIO)).move_to(RIGHT * 3.6 + arriba + UP * 0.6)
        hb = VGroup(Text("Camino B", font_size=TAM_NOTA + 2, color=COLOR_SECUNDARIO)).move_to(RIGHT * 3.6 + abajo + UP * 0.6)
        self.decir("Desde la misma matriz, dos caminos distintos.")
        self.play(FadeIn(ma), FadeIn(mb), FadeIn(ha), FadeIn(hb))
        self.decir("Camino a: a la fila dos le restamos tres medios de la fila uno.")
        ma = self.operar_filas(ma, ("sumar", 1, 0, Fraction(-3, 2)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=ha)
        self.decir("Camino be: primero intercambiamos las filas, y luego a la fila dos le restamos dos tercios de la fila uno.")
        mb = self.operar_filas(mb, ("intercambio", 0, 1), pivotes=[(0, 0)], cuenta=False, historial=hb)
        mb = self.operar_filas(mb, ("sumar", 1, 0, Fraction(-2, 3)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=hb)
        self.decir("Llegamos a dos matrices escalonadas distintas, las dos equivalentes a la de partida. Los pivotes están en las mismas posiciones.")
        self.play(Create(escalera(ma, [(0, 0), (1, 1)])), Create(escalera(mb, [(0, 0), (1, 1)])))
        self.pie("Dos matrices escalonadas distintas, las dos equivalentes a la de partida.\nLos pivotes están en las mismas posiciones: columnas 1 y 2.", espera=5)
        self.quitar_pie()
        self.play(FadeOut(ha), FadeOut(hb))
        sol_a = MathTex(r"-7y = -14 \Rightarrow y = 2,\quad 2x + 8 = 10 \Rightarrow x = 1", font_size=34, color=COLOR_SOLUCION)
        sol_b = MathTex(r"\tfrac{14}{3}y = \tfrac{28}{3} \Rightarrow y = 2,\quad 3x - 2 = 1 \Rightarrow x = 1", font_size=34, color=COLOR_SOLUCION)
        sol_a.next_to(ma, RIGHT, buff=0.8)
        sol_b.next_to(mb, RIGHT, buff=0.8)
        self.decir("Las dos dan ye igual a dos, y equis igual a uno.")
        self.play(FadeIn(sol_a))
        self.play(FadeIn(sol_b))
        self.wait(4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué cambia y qué no")
        puntos = VGroup(
            Tex(r"\textbf{Cambia}: el valor de las entradas (y lo cómodas que son las cuentas).", font_size=38),
            Tex(r"\textbf{No cambia}: el conjunto solución, porque todas son equivalentes (L24).", font_size=38),
            Tex(r"\textbf{Tampoco cambian} las posiciones de los pivotes ni cuántos hay.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"(Este último hecho se demuestra en la L31, con la forma escalonada reducida;\\ el número de pivotes será el \textbf{rango}, Unidad 7).", font_size=32, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(puntos)
        self.decir("Cambian los números, y lo cómodas que son las cuentas. No cambia el conjunto solución, porque todas son equivalentes. Y tampoco cambian las posiciones de los pivotes ni cuántos hay; lo demostraremos en la lección treinta y uno.")
        for p in puntos:
            self.play(FadeIn(p))
            self.wait(2.2)
        self.decir("El camino be trajo fracciones. Elegir bien el pivote ahorra trabajo, pero no cambia el resultado.")
        self.pie("El camino B trajo fracciones. Elegir bien el pivote (por ejemplo, un 1) ahorra trabajo, pero no cambia el resultado.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            parrafo(r"Creer que el otro se equivocó porque su escalonada es distinta:", r"comparad pivotes y soluciones.", font_size=34, sangria=0.4),
            Tex(r"Hablar de ``la'' forma escalonada de una matriz: hay muchas.", font_size=34),
            Tex(r"Redondear fracciones a decimales: arrastra errores. Se opera con fracciones.", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes: creer que el otro se equivocó porque su escalonada es distinta, cuando hay que comparar pivotes y soluciones; hablar de la forma escalonada, cuando hay muchas; y redondear fracciones a decimales, que arrastra errores.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N2-02",
            VGroup(
                MathTex(r"M = \left[\begin{array}{cc|c} 2 & 6 & 4 \\ 1 & 4 & 3 \end{array}\right]", font_size=48),
                parrafo(r"Lleva $M$ a forma escalonada por dos caminos:", r"a) $R_2 \leftarrow R_2 - \tfrac{1}{2}R_1$; \quad b) $R_1 \leftrightarrow R_2$ y luego $R_2 \leftarrow R_2 - 2R_1$.", font_size=36, sangria=0.4),
                Tex(r"Compara pivotes y soluciones.", font_size=34),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Una matriz tiene muchas formas escalonadas: depende de las operaciones elegidas.",
                "Todas tienen las mismas soluciones y los pivotes en las mismas posiciones.",
                "Elegir pivotes cómodos ahorra fracciones, no cambia el resultado.",
            ],
            "Lección 26 — eliminación hacia adelante y sustitución hacia atrás.",
            voz="En resumen: una matriz tiene muchas formas escalonadas, según las operaciones elegidas. Todas tienen las mismas soluciones, y los pivotes en las mismas posiciones. Elegir pivotes cómodos ahorra fracciones, pero no cambia el resultado. Siguiente: lección veintiséis, eliminación hacia adelante y sustitución hacia atrás.",
        )
