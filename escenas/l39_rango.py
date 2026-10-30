"""Lección 39 — El rango de una matriz.

Escenas (un video cada una):
    RangoComoNumeroDePivotes, RangoDeAyDeAumentada, RangoNoEsNumeroDeEcuaciones

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l39_rango.py -a
"""

import sys
from fractions import Fraction
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class RangoComoNumeroDePivotes(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 39 · Parte 1", "El rango de una matriz")
        titulo = self.encabezado("Contar pivotes")
        m = matriz_gauss([[1, 2, 3, 0], [2, 4, 6, 0], [1, 1, 1, 0]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Tomemos la matriz uno, dos, tres; dos, cuatro, seis; uno, uno, uno. La última columna, de ceros, solo está para poder operar. Vamos a escalonarla.")
        self.play(FadeIn(m), FadeIn(historial))
        self.decir("A la fila dos le restamos dos veces la fila uno: queda de ceros. Es el doble de la primera.")
        m = self.operar_filas(m, ("sumar", 1, 0, -2), historial=historial)
        self.decir("A la fila tres le restamos la fila uno.")
        m = self.operar_filas(m, ("sumar", 2, 0, -1), historial=historial)
        self.decir("Y como el pivote de la segunda columna debería estar en la fila dos, intercambiamos las filas dos y tres.")
        m = self.operar_filas(m, ("intercambio", 1, 2), historial=historial, pivotes=[(0, 0), (1, 1)])
        self.play(Create(escalera(m, [(0, 0), (1, 1)])))
        self.wait(1)
        resultado = Tex(r"2 pivotes $\;\Rightarrow\;$ rango $= 2$", font_size=48, color=COLOR_PIVOTE).next_to(m, DOWN, buff=0.7)
        self.decir("La forma escalonada tiene dos pivotes, y una fila de ceros. El número de pivotes es el rango de la matriz: aquí, dos.")
        self.play(Write(resultado))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición")
        definicion = VGroup(
            parrafo(r"El \textbf{rango} de una matriz $A$, $\operatorname{rg}(A)$, es el número de pivotes", r"de cualquier forma escalonada de $A$ (= número de filas no nulas).", font_size=40, sangria=0.5),
            parrafo(r"Está bien definido: las posiciones de los pivotes no dependen del camino (L25),", r"y la reducida es única (L31).", font_size=36, sangria=0.5, color=COLOR_SECUNDARIO),
            MathTex(r"\operatorname{rg}(A) \le \min(m, n)", font_size=52, color=COLOR_PIVOTE),
            Tex(r"Hay a lo sumo un pivote por fila y uno por columna.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(definicion, margen=0.5)
        self.decir("El rango de una matriz es el número de pivotes de cualquier forma escalonada suya, que es lo mismo que el número de filas no nulas. Está bien definido porque las posiciones de los pivotes no dependen del camino, y la forma reducida es única. Y como hay a lo sumo un pivote por fila y uno por columna, el rango nunca supera ni al número de filas ni al de columnas.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Rango completo")
        casos = VGroup(
            parrafo(r"$\operatorname{rg}(A) = m$ (todas las filas con pivote): \textbf{rango por filas completo}.", font_size=36, sangria=0.4),
            parrafo(r"$\operatorname{rg}(A) = n$ (todas las columnas con pivote): \textbf{rango por columnas completo}.", font_size=36, sangria=0.4),
            parrafo(r"Si $A$ es $n \times n$ y $\operatorname{rg}(A) = n$, su reducida es $I$", r"(se verá en la Unidad 8 que equivale a ser invertible).", font_size=36, sangria=0.4, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(casos, margen=0.5)
        self.decir("Si el rango es igual al número de filas, todas las filas tienen pivote. Si es igual al número de columnas, todas las columnas lo tienen. Y si la matriz es cuadrada, de ene por ene, y su rango es ene, su forma reducida es la identidad.")
        for c in casos:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N2-01",
            VGroup(
                Text("Calcula el rango de A escalonando, e indica la forma reducida:", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 3 & 2 \\ 2 & 6 & 5 \\ 1 & 3 & 3 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: calcula el rango de esta matriz escalonándola, e indica su forma reducida. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Rango = número de pivotes de una forma escalonada.",
                "Está bien definido: la reducida es única.",
                "rg(A) ≤ mín(m, n).",
            ],
            "el rango de A y el de la matriz aumentada.",
            voz="En resumen: el rango es el número de pivotes de una forma escalonada. Está bien definido, porque la forma reducida es única. Y es menor o igual que el mínimo entre el número de filas y el de columnas. Siguiente: el rango de a y el de la matriz aumentada.",
        )


class RangoDeAyDeAumentada(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 39 · Parte 2", "Rango de A y de [A | b]")
        titulo = self.encabezado("Una columna más, a lo sumo un pivote más")
        izq = matriz_gauss([[1, 1, 1, 2], [0, 1, 2, 3], [0, 0, 0, 0]], pivotes=[(0, 0), (1, 1)], escala=0.85)
        der = matriz_gauss([[1, 1, 1, 2], [0, 1, 2, 3], [0, 0, 0, 1]], pivotes=[(0, 0), (1, 1), (2, 3)], escala=0.85)
        paneles = VGroup(izq, der).arrange(RIGHT, buff=1.4).shift(UP * 0.4)
        r_izq = MathTex(r"\operatorname{rg}(A) = 2,\ \ \operatorname{rg}[A \mid \mathbf{b}] = 2", font_size=38, color=COLOR_SOLUCION).next_to(izq, DOWN, buff=0.5)
        r_der = MathTex(r"\operatorname{rg}(A) = 2,\ \ \operatorname{rg}[A \mid \mathbf{b}] = 3", font_size=38, color=COLOR_ERROR).next_to(der, DOWN, buff=0.5)
        self.decir("Para un sistema, tenemos dos rangos: el de la matriz de coeficientes a, y el de la matriz aumentada, a con la columna be. Estos son los sistemas de la lección veintiocho, ya escalonados.")
        self.play(FadeIn(izq), FadeIn(der))
        self.play(Create(escalera(izq, [(0, 0), (1, 1)])), Create(escalera(der, [(0, 0), (1, 1), (2, 3)])))
        self.decir("En el primero, la última fila es cero igual a cero: los dos rangos valen dos. En el segundo, la última fila es cero, cero, cero, uno: hay un pivote más, en la columna de be. El rango de a vale dos, y el de la aumentada, tres.")
        self.play(FadeIn(r_izq))
        self.play(FadeIn(r_der))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Siempre: rg(A) ≤ rg[A | b] ≤ rg(A) + 1")
        reglas = VGroup(
            MathTex(r"\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1", font_size=52, color=COLOR_PIVOTE),
            parrafo(r"Las operaciones por filas sobre $[A \mid \mathbf{b}]$ escalonan $A$ al mismo tiempo:", r"los pivotes de $A$ son pivotes de $[A \mid \mathbf{b}]$.", font_size=36, sangria=0.5),
            parrafo(r"La columna $\mathbf{b}$ aporta como mucho \textbf{un} pivote más", r"(solo si su pivote cae en una fila sin pivote de $A$).", font_size=36, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(reglas, margen=0.5)
        self.decir("Siempre ocurre que el rango de a es menor o igual que el de la aumentada, y este, menor o igual que el de a más uno. Porque al escalonar la aumentada se escalona también a, así que los pivotes de a lo son también de la aumentada; y la columna de be puede aportar, como mucho, un pivote más.")
        for r in reglas:
            self.play(FadeIn(r))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N2-02",
            VGroup(
                Text("Halla rg(A) y rg[A | b] para:", font_size=TAM_TEXTO),
                MathTex(r"\left[\begin{array}{ccc|c} 1 & 2 & 1 & 4 \\ 2 & 4 & 2 & 7 \\ 1 & 1 & 3 & 5 \end{array}\right]", font_size=48),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla el rango de la matriz de coeficientes y el de la matriz aumentada de este sistema. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Dos rangos: rg(A) y rg[A | b].",
                "rg(A) ≤ rg[A | b] ≤ rg(A) + 1.",
                "Si coinciden, b no añade pivote; si no, hay un pivote en la columna de b.",
            ],
            "el rango no es el número de ecuaciones.",
            voz="En resumen: hay dos rangos, el de a y el de la aumentada. El primero es menor o igual que el segundo, y este, menor o igual que el primero más uno. Si coinciden, be no añade pivote; si no, hay un pivote en la columna de be. Siguiente: el rango no es el número de ecuaciones.",
        )


class RangoNoEsNumeroDeEcuaciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 39 · Parte 3", "El rango no es el número de ecuaciones")
        titulo = self.encabezado("Tres ecuaciones, rango 2")
        sistema = MathTex(r"\begin{cases} x + y = 3 \\ x - y = 1 \\ 2x + 0y = 4 \end{cases}", font_size=46).to_edge(LEFT, buff=1.0).shift(UP * 0.5)
        reducida = matriz_gauss([[1, 0, 2], [0, 1, 1], [0, 0, 0]], pivotes=[(0, 0), (1, 1)], escala=0.9).next_to(sistema, RIGHT, buff=1.4)
        nota = Tex(r"$E_3 = E_1 + E_2$: la tercera ecuación sobra. $\operatorname{rg} = 2$, no $3$.", font_size=38, color=COLOR_PIVOTE).next_to(VGroup(sistema, reducida), DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(sistema, reducida, nota), margen=0.5)
        self.decir("Tres ecuaciones no significan rango tres. En este sistema, la tercera ecuación es la suma de las otras dos. Al reducir, queda una fila de ceros: el rango de la matriz aumentada es dos, no tres.")
        self.play(Write(sistema))
        self.play(FadeIn(reducida))
        self.play(FadeIn(nota))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Más ecuaciones que incógnitas, o menos")
        ejemplos = VGroup(
            parrafo(r"$4 \times 3$: como mucho rango $3$ (columnas); una fila siempre depende de las demás.", font_size=36, sangria=0.4),
            parrafo(r"$2 \times 5$: como mucho rango $2$ (filas); hay al menos $3$ columnas sin pivote.", font_size=36, sangria=0.4),
            parrafo(r"Dos filas proporcionales, o una fila que es suma de otras: bajan el rango.", font_size=36, sangria=0.4),
            parrafo(r"Una fila de ceros: no cuenta.", font_size=36, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(ejemplos, margen=0.5)
        self.decir("Con cuatro ecuaciones y tres incógnitas, el rango es como mucho tres. Con dos ecuaciones y cinco incógnitas, como mucho dos, y quedan al menos tres columnas sin pivote. Dos filas proporcionales, o una fila que es suma de otras, bajan el rango. Y una fila de ceros no cuenta.")
        for e in ejemplos:
            self.play(FadeIn(e))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué mide el rango")
        mide = VGroup(
            Tex(r"El rango es el número de ecuaciones \textbf{realmente independientes}.", font_size=40),
            Tex(r"Cada ecuación aporta información nueva solo si trae un pivote nuevo.", font_size=38),
            Tex(r"Lo que se llamó ``cada ecuación quita un grado de libertad'' (L10):", font_size=38, color=COLOR_SECUNDARIO),
            Tex(r"las que sobran no lo quitan; el rango cuenta las que sí.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(mide, margen=0.5)
        self.decir("El rango mide el número de ecuaciones realmente independientes. Cada ecuación aporta información nueva solo si trae un pivote nuevo. En la lección diez dijimos que cada ecuación quita un grado de libertad: las que sobran no lo quitan, y el rango cuenta las que sí.")
        for m in mide:
            self.play(FadeIn(m))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N3-01",
            VGroup(
                Text("Sin resolver, ¿cuál es el rango de la matriz aumentada?", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + y + z = 1 \\ 2x + 2y + 2z = 2 \\ x - y = 0 \\ 3x + y + 2z = 2 \end{cases}", font_size=44),
                Text("¿Qué ecuaciones sobran?", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: sin resolver, di cuál es el rango de la matriz aumentada de este sistema de cuatro ecuaciones, y qué ecuaciones sobran. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "El rango no es el número de ecuaciones: es el de ecuaciones independientes.",
                "Hay filas que sobran si son combinación de otras.",
                "rg ≤ mín(filas, columnas).",
            ],
            "Lección 40 — el teorema de Rouché-Frobenius.",
            voz="En resumen: el rango no es el número de ecuaciones, sino el de ecuaciones independientes. Sobran las filas que son combinación de otras. Y el rango es menor o igual que el mínimo entre filas y columnas. Siguiente: lección cuarenta, el teorema de Rouché-Frobenius.",
        )
