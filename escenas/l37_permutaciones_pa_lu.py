"""Lección 37 — Cuando LU falla: permutaciones y PA = LU.

Escenas (un video cada una):
    CuandoLUFalla, MatricesDePermutacion, PivoteoParcial

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l37_permutaciones_pa_lu.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class CuandoLUFalla(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 37 · Parte 1", "Cuando LU falla")
        titulo = self.encabezado("Un pivote 0 en la diagonal")
        m = matriz_gauss([[1, 1, 1, 3], [2, 2, 5, 9], [4, 6, 8, 18]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Intentemos factorizar esta matriz, la del sistema de coeficientes uno, uno, uno; dos, dos, cinco; cuatro, seis, ocho. Hacemos ceros debajo del primer pivote.")
        self.play(FadeIn(m), FadeIn(historial))
        self.decir("A la fila dos le restamos dos veces la fila uno.")
        m = self.operar_filas(m, ("sumar", 1, 0, -2), historial=historial)
        self.decir("Y a la fila tres, cuatro veces la fila uno.")
        m = self.operar_filas(m, ("sumar", 2, 0, -4), historial=historial)
        marco = SurroundingRectangle(m.get_rows()[1][1], color=COLOR_ERROR)
        aviso = Tex(r"El pivote de la fila 2 es $0$: no hay multiplicador $m_{32} = 2/0$.", font_size=38, color=COLOR_ERROR).to_edge(DOWN, buff=0.7)
        self.decir("Ahora el pivote de la segunda columna debería estar en la fila dos, pero vale cero. El multiplicador de la fila tres sería dos entre cero: no existe. Con solo operaciones de reemplazo, la factorización ele u falla.")
        self.play(Create(marco), FadeIn(aviso))
        self.wait(2)
        self.play(FadeOut(marco), FadeOut(aviso))
        self.decir("La solución es la de la lección veintisiete: intercambiar la fila dos con la fila tres, que tiene un dos.")
        m = self.operar_filas(m, ("intercambio", 1, 2), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        self.play(Create(escalera(m, [(0, 0), (1, 1), (2, 2)])))
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El intercambio, hecho antes")
        idea = VGroup(
            parrafo(r"Si se intercambian las filas 2 y 3 \textbf{desde el principio},", r"la eliminación ya no se atasca:", font_size=38, sangria=0.5),
            MathTex(r"PA = \begin{bmatrix} 1 & 1 & 1 \\ 4 & 6 & 8 \\ 2 & 2 & 5 \end{bmatrix}", font_size=46),
            MathTex(r"PA = LU,\quad L = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 2 & 0 & 1 \end{bmatrix},\quad U = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 4 \\ 0 & 0 & 3 \end{bmatrix}", font_size=42, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(idea, margen=0.5)
        self.decir("Si hacemos ese intercambio desde el principio, la eliminación ya no se atasca. La matriz con las filas dos y tres cambiadas sí se factoriza: pe a es ele u, con ele con un cuatro y un dos, y u la matriz uno, uno, uno; cero, dos, cuatro; cero, cero, tres. Es el mismo trabajo, con las filas en otro orden.")
        for i in idea:
            self.play(FadeIn(i))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Resolver con PA = LU")
        pasos = VGroup(
            MathTex(r"A\mathbf{x} = \mathbf{b} \;\Longleftrightarrow\; PA\,\mathbf{x} = P\mathbf{b}", font_size=48),
            MathTex(r"L\,U\,\mathbf{x} = P\mathbf{b}", font_size=48),
            parrafo(r"1. Calcular $P\mathbf{b}$ (reordenar $\mathbf{b}$).", r"2. $L\mathbf{y} = P\mathbf{b}$ hacia adelante.", r"3. $U\mathbf{x} = \mathbf{y}$ hacia atrás.", font_size=38, sangria=0.5, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(pasos, margen=0.5)
        self.decir("Para resolver a equis igual a be, aplicamos el mismo intercambio a los dos lados: pe a equis igual a pe be. Entonces ele u equis es pe be. Reordenamos be, resolvemos ele ye igual a pe be hacia adelante, y u equis igual a ye hacia atrás.")
        for p in pasos:
            self.play(FadeIn(p))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N3-04",
            VGroup(
                Text("Halla P, L y U con P A = L U, y resuelve A x = b con b = (3, 9, 18):", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 5 \\ 4 & 6 & 8 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla pe, ele y u con pe a igual a ele u, y resuelve a equis igual a be, para be igual a tres, nueve, dieciocho. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Si aparece un pivote 0, A = LU puede no existir.",
                "Se intercambian filas y se obtiene PA = LU.",
                "A x = b se resuelve con P b, L y = P b y U x = y.",
            ],
            "las matrices de permutación.",
            voz="En resumen: si aparece un pivote cero, a igual a ele u puede no existir. Intercambiando filas se obtiene pe a igual a ele u. Y a equis igual a be se resuelve con pe be, ele ye igual a pe be, y u equis igual a ye. Siguiente: las matrices de permutación.",
        )


class MatricesDePermutacion(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 37 · Parte 2", "Matrices de permutación")
        titulo = self.encabezado("La identidad con las filas reordenadas")
        p = matriz([[1, 0, 0], [0, 0, 1], [0, 1, 0]], h_buff=1.0).scale(0.8)
        a = matriz([[1, 1, 1], [2, 2, 5], [4, 6, 8]], h_buff=1.0).scale(0.8)
        a.get_entries().set_color(COLOR_COEFICIENTE)
        pa = matriz([[1, 1, 1], [4, 6, 8], [2, 2, 5]], h_buff=1.0).scale(0.8)
        eq = VGroup(p, a, MathTex("=", font_size=52), pa).arrange(RIGHT, buff=0.35).shift(UP * 0.4)
        rot = MathTex(r"PA\ \text{reordena las filas de } A:\ \ R_2 \leftrightarrow R_3", font_size=40, color=COLOR_OPERACION).next_to(eq, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(eq, rot), margen=0.5)
        self.decir("Una matriz de permutación es la identidad con sus filas reordenadas. Esta tiene las filas dos y tres intercambiadas. Al multiplicar pe por a, se reordenan las filas de a de la misma manera: es el intercambio de la fila dos con la tres.")
        self.play(FadeIn(p), FadeIn(a), FadeIn(eq[2]))
        self.play(FadeIn(pa))
        self.play(FadeIn(rot))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Propiedades")
        propiedades = VGroup(
            Tex(r"Cada fila y cada columna tiene un único $1$; el resto son ceros.", font_size=38),
            Tex(r"Hay $n!$ matrices de permutación $n \times n$ (para $n = 3$, seis).", font_size=38),
            Tex(r"El producto de dos permutaciones es una permutación.", font_size=38),
            Tex(r"$P^{-1} = P^{T}$: la inversa es la traspuesta. $P^T P = I$.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Multiplicar por $P$ a la izquierda reordena \emph{filas}; a la derecha, \emph{columnas}.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(propiedades, margen=0.5)
        self.decir("Propiedades. Cada fila y cada columna tiene un único uno. Hay ene factorial matrices de permutación de ene por ene: seis, para ene igual a tres. El producto de dos permutaciones es otra permutación. La inversa de una permutación es su traspuesta. Y multiplicar por pe a la izquierda reordena filas; a la derecha, columnas.")
        for q in propiedades:
            self.play(FadeIn(q))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "PA = LU, en general")
        teorema = VGroup(
            Tex(r"\textbf{Teorema.} Toda matriz cuadrada invertible $A$ admite una factorización", font_size=38),
            MathTex(r"PA = LU", font_size=64, color=COLOR_PIVOTE),
            Tex(r"con $P$ de permutación, $L$ triangular inferior con unos en la diagonal y $U$ triangular superior.", font_size=38),
            Tex(r"La $P$ recoge los intercambios de filas de la eliminación de Gauss.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(teorema, margen=0.5)
        self.decir("Y en general: toda matriz cuadrada invertible a admite una factorización pe a igual a ele u, con pe de permutación, ele triangular inferior con unos en la diagonal, y u triangular superior. La permutación recoge los intercambios de filas que hizo la eliminación de Gauss.")
        for t in teorema:
            self.play(FadeIn(t))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N3-05",
            VGroup(
                Text("a) Escribe la matriz de permutación P de 3 × 3 que lleva las filas (1, 2, 3) a (3, 1, 2).", font_size=TAM_NOTA + 2),
                Text("b) Calcula P Pᵀ. c) ¿Cuántas matrices de permutación hay de 4 × 4?", font_size=TAM_NOTA + 2),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: escribe la matriz de permutación de tres por tres que lleva las filas uno, dos, tres a tres, uno, dos. Calcula pe por pe traspuesta. Y di cuántas matrices de permutación hay de cuatro por cuatro. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Permutación: identidad con las filas reordenadas; hay n!.",
                "P A reordena las filas de A; P⁻¹ = Pᵀ.",
                "Toda matriz invertible cumple P A = L U.",
            ],
            "el pivoteo parcial.",
            voz="En resumen: una matriz de permutación es la identidad con las filas reordenadas, y hay ene factorial. Pe a reordena las filas de a, y la inversa de pe es su traspuesta. Toda matriz invertible cumple pe a igual a ele u. Siguiente: el pivoteo parcial.",
        )


class PivoteoParcial(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 37 · Parte 3", "Pivoteo parcial")
        titulo = self.encabezado("Elegir el pivote más grande")
        regla = VGroup(
            parrafo(r"\textbf{Pivoteo parcial:} en cada columna, antes de eliminar, se intercambia", r"la fila del pivote con la fila de debajo cuya entrada tenga el mayor", r"\emph{valor absoluto}.", font_size=38, sangria=0.5),
            Tex(r"Así los multiplicadores cumplen $|m_{ij}| \le 1$.", font_size=40, color=COLOR_PIVOTE),
            Tex(r"No solo se evitan los pivotes $0$: también los pivotes \emph{muy pequeños}.", font_size=38),
        ).arrange(DOWN, buff=0.55).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(regla, margen=0.5)
        self.decir("Hay otra razón para intercambiar filas, aunque el pivote no sea cero. Con pivoteo parcial, en cada columna elegimos como pivote la entrada de mayor valor absoluto, intercambiando filas. Así, todos los multiplicadores valen, en valor absoluto, uno como máximo. Se evitan los pivotes cero, y también los pivotes muy pequeños.")
        for r in regla:
            self.play(FadeIn(r))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un pivote pequeño estropea el resultado")
        sistema = MathTex(r"\begin{cases} 0{,}0001\,x + y = 1 \\ x + y = 2 \end{cases}", font_size=46).next_to(titulo, DOWN, buff=0.5).to_edge(LEFT, buff=0.9)
        exacta = Tex(r"Solución exacta: $x \approx 1{,}0001$, $y \approx 0{,}9999$.", font_size=36, color=COLOR_SOLUCION).next_to(sistema, RIGHT, buff=0.9)
        convenio = Tex(r"Calculadora de juguete: 3 cifras significativas.", font_size=34, color=COLOR_SECUNDARIO).next_to(VGroup(sistema, exacta), DOWN, buff=0.5)
        ajustar_al_encuadre(VGroup(sistema, exacta, convenio), margen=0.5)
        self.decir("Veamos qué pasa con un pivote pequeño. Este sistema, cero coma cero cero cero uno equis más ye igual a uno, y equis más ye igual a dos, tiene por solución equis aproximadamente uno coma cero cero cero uno, y ye, cero coma nueve nueve nueve nueve. Resolvámoslo con una calculadora que solo guarda tres cifras significativas.")
        self.play(Write(sistema))
        self.play(FadeIn(exacta))
        self.play(FadeIn(convenio))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Sin intercambiar: el pivote es 0,0001")
        sin = VGroup(
            MathTex(r"m = \dfrac{1}{0{,}0001} = 10\,000", font_size=38),
            MathTex(r"y\text{: }\ 1 - 10\,000\cdot 1 = -9999 \approx -1{,}00\cdot 10^4", font_size=38),
            MathTex(r"\text{térm. indep.: }\ 2 - 10\,000\cdot 1 = -9998 \approx -1{,}00\cdot 10^4", font_size=38),
            MathTex(r"y \approx 1{,}00,\qquad x = \dfrac{1 - 1{,}00}{0{,}0001} = 0", font_size=38, color=COLOR_ERROR),
            Tex(r"¡$x = 0$, y la solución exacta es $x \approx 1$!", font_size=40, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(sin, margen=0.5)
        self.decir("Sin intercambiar, el pivote es cero coma cero cero cero uno, y el multiplicador, diez mil. Al restar, la ye de la segunda fila queda uno menos diez mil, que son menos nueve mil novecientos noventa y nueve: con tres cifras, menos uno por diez a la cuatro. El término independiente, igual. Sale ye igual a uno, y entonces equis es uno menos uno, entre cero coma cero cero cero uno: cero. Pero la solución exacta es equis casi uno: el error es total.")
        for s in sin:
            self.play(FadeIn(s))
            self.wait(1.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Con pivoteo parcial: se intercambia primero")
        con = VGroup(
            MathTex(r"\begin{cases} x + y = 2 \\ 0{,}0001\,x + y = 1 \end{cases}\qquad m = 0{,}0001", font_size=40),
            MathTex(r"y\text{: }\ 1 - 0{,}0001\cdot 1 = 0{,}9999 \approx 1{,}00", font_size=38),
            MathTex(r"\text{térm. indep.: }\ 1 - 0{,}0001\cdot 2 = 0{,}9998 \approx 1{,}00", font_size=38),
            MathTex(r"y \approx 1{,}00,\qquad x = 2 - 1{,}00 = 1{,}00", font_size=38, color=COLOR_SOLUCION),
            Tex(r"Correcto con 3 cifras: $x \approx 1{,}00$, $y \approx 1{,}00$.", font_size=40, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(con, margen=0.5)
        self.decir("Con pivoteo parcial, intercambiamos las dos filas: el pivote es uno, y el multiplicador, cero coma cero cero cero uno. La ye queda uno menos cero coma cero cero cero uno, que con tres cifras es uno; el término independiente, también uno. Entonces ye es uno, y equis es dos menos uno: uno. El resultado es correcto con tres cifras.")
        for s in con:
            self.play(FadeIn(s))
            self.wait(1.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La moraleja")
        moraleja = VGroup(
            Tex(r"Dividir entre un pivote muy pequeño amplifica los errores de redondeo.", font_size=38),
            Tex(r"Con pivoteo parcial ($|m_{ij}| \le 1$), los errores no se disparan.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Los programas de álgebra numérica resuelven con $PA = LU$ (con pivoteo parcial).", font_size=38),
            Tex(r"A mano, con fracciones exactas, el redondeo no existe: allí basta evitar el $0$.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(moraleja, margen=0.5)
        self.decir("La moraleja: dividir entre un pivote muy pequeño amplifica los errores de redondeo. Con pivoteo parcial, los multiplicadores no superan a uno, y los errores no se disparan. Por eso los programas de álgebra numérica resuelven con pe a igual a ele u, con pivoteo parcial. A mano, con fracciones exactas, no hay redondeo: basta con evitar el cero.")
        for m in moraleja:
            self.play(FadeIn(m))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N4-03",
            VGroup(
                Text("Resuelve con 3 cifras significativas, sin y con intercambio de filas:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} 0{,}0002\,x + y = 1 \\ x + y = 3 \end{cases}", font_size=48),
                Text("Compara con la solución exacta.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: resuelve este sistema con tres cifras significativas, sin y con intercambio de filas, y compara con la solución exacta. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Pivoteo parcial: pivote de mayor valor absoluto; |m_ij| ≤ 1.",
                "Evita el 0 y los pivotes muy pequeños, que amplifican el redondeo.",
                "El resultado numérico estándar: P A = L U.",
            ],
            "Lección 38 — comparación y aplicaciones.",
            voz="En resumen: el pivoteo parcial elige el pivote de mayor valor absoluto, y los multiplicadores no superan a uno. Evita el cero y los pivotes muy pequeños, que amplifican el redondeo. Y el resultado numérico estándar es pe a igual a ele u. Siguiente: lección treinta y ocho, comparación y aplicaciones.",
        )
