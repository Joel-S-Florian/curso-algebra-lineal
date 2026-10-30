"""Lección 27 — Pivotes nulos y filas nulas.

Escenas (un video cada una):
    PivoteCeroIntercambio, FilaNulaEcuacionRedundante

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l27_pivotes_nulos.py -a
"""

import sys
from fractions import Fraction
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import (  # noqa: E402
    EscenaCurso,
    ajustar_al_encuadre,
    ejes_iguales,
    escalera,
    matriz_gauss,
    parrafo,
    rectas_de_sistema,
    sistema_con_llave,
)
from curso.estilo import *  # noqa: E402,F403


def sustitucion_atras(escena, m, filas, pasos, x=2.6, font_size=40):
    lineas = VGroup(*[MathTex(p, font_size=font_size) for p in pasos]).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
    lineas.match_y(m).set_x(x)
    ajustar_al_encuadre(lineas)
    for i, linea in zip(filas, lineas):
        marco = SurroundingRectangle(m.get_rows()[i], color=COLOR_PIVOTE)
        escena.play(Create(marco), Write(linea))
        escena.wait(1.5)
        escena.play(FadeOut(marco))
    return lineas


class PivoteCeroIntercambio(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 27 · Parte 1", "Cuando el pivote vale 0")
        titulo = self.encabezado("No se puede dividir por 0")
        m = matriz_gauss([[0, 3, 6], [1, 1, 3]]).shift(LEFT * 3 + UP * 0.6)
        cociente = MathTex(r"m = \frac{1}{0}\ ???", font_size=48, color=COLOR_ERROR).next_to(m, RIGHT, buff=1.2)
        self.decir("¿Qué pasa si el pivote vale cero?")
        self.play(FadeIn(m))
        self.decir("Con un cero en el lugar del pivote no hay multiplicador: no se puede dividir entre cero.")
        self.play(Indicate(m.get_rows()[0][0], color=COLOR_ERROR), Write(cociente))
        idea = parrafo(r"Con un 0 en la posición del pivote no hay multiplicador.",
                       r"Remedio: \textbf{intercambiar} con una fila de más abajo que tenga",
                       r"una entrada no nula en esa columna (L24).", font_size=36).next_to(VGroup(m, cociente), DOWN, buff=0.8)
        self.decir("El remedio: intercambiar con una fila de más abajo que tenga una entrada no nula en esa columna.")
        self.play(FadeIn(idea))
        self.wait(5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un 0 que aparece a mitad de camino")
        m = matriz_gauss([[1, 1, 1, 3], [2, 2, 1, 5], [1, 2, 3, 6]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("A veces el cero aparece a mitad de camino.")
        self.play(FadeIn(m), FadeIn(historial))
        self.decir("Hacemos ceros en la columna uno: a la fila dos le restamos dos veces la fila uno, y a la fila tres, una vez.")
        m = self.operar_filas(m, ("sumar", 1, 0, -2), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 0, -1), historial=historial)
        marco = SurroundingRectangle(m.get_rows()[1][1], color=COLOR_ERROR)
        self.decir("El pivote de la columna dos debería estar en la fila dos, pero ahí hay un cero. Debajo, en la fila tres, hay un uno.")
        self.play(Create(marco))
        self.pie("El pivote de la columna 2 debería estar en la fila 2, pero ahí hay un 0. Debajo, en la fila 3, hay un 1.")
        self.play(FadeOut(marco))
        self.decir("Intercambiamos las filas dos y tres.")
        m = self.operar_filas(m, ("intercambio", 1, 2), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        self.play(Create(escalera(m, [(0, 0), (1, 1), (2, 2)])))
        self.decir("Tras el intercambio, la matriz ya está escalonada: no hace falta ninguna operación más.")
        self.pie("Tras el intercambio la matriz ya está escalonada: no hace falta ninguna operación más.", espera=3)
        self.quitar_pie()
        self.play(FadeOut(historial))
        sustitucion_atras(self, m, (2, 1, 0), (r"-z = -1 \;\Rightarrow\; z = 1", r"y + 2\cdot 1 = 3 \;\Rightarrow\; y = 1", r"x + 1 + 1 = 3 \;\Rightarrow\; x = 1"), x=3.2)
        self.decir("La solución es uno, uno, uno, y se verifica en el original: uno más uno más uno, tres; dos más dos más uno, cinco; uno más dos más tres, seis.")
        self.pie("Verificación en el original: 1 + 1 + 1 = 3, 2 + 2 + 1 = 5, 1 + 2 + 3 = 6.", color=COLOR_SOLUCION, espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Por qué el intercambio es seguro")
        razones = VGroup(
            Tex(r"Es una operación elemental: el sistema sigue siendo equivalente (L24).", font_size=36),
            parrafo(r"No estropea ceros: las dos filas que se intercambian tienen ya un 0", r"en todas las columnas trabajadas.", font_size=36, sangria=0.4),
            parrafo(r"Se elige una fila de \textbf{más abajo}: las de arriba ya tienen su pivote", r"y subirlas desharía la escalera.", font_size=36, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        self.decir("¿Por qué el intercambio es seguro? Es una operación elemental, así que el sistema sigue siendo equivalente. No estropea ceros, porque las dos filas tienen ya un cero en las columnas trabajadas. Y se elige una fila de más abajo: las de arriba ya tienen su pivote.")
        for r in razones:
            self.play(FadeIn(r))
            self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Y si toda la columna es 0 hacia abajo?")
        m = matriz_gauss([[1, 2, 1, 4], [0, 0, 3, 3], [0, 0, 1, 1]], pivotes=[(0, 0)]).move_to(LEFT * 2.6 + UP * 0.7)
        self.decir("¿Y si toda la columna es cero hacia abajo?")
        self.play(FadeIn(m))
        marco = SurroundingRectangle(VGroup(m.get_rows()[1][1], m.get_rows()[2][1]), color=COLOR_ERROR)
        self.decir("En la columna dos, de la fila dos hacia abajo, todo es cero: no hay con quién intercambiar. Esa columna se queda sin pivote, y se pasa a la siguiente.")
        self.play(Create(marco))
        self.pie("En la columna 2, de la fila 2 hacia abajo, todo es 0: no hay con quién intercambiar.\nEsa columna se queda sin pivote y se pasa a la siguiente: el pivote de la fila 2 es el 3.")
        self.play(FadeOut(marco), m.get_rows()[1][2].animate.set_color(COLOR_PIVOTE))
        m.pivotes = ((0, 0), (1, 2))
        self.decir("El pivote de la fila dos está en la columna tres. A la fila tres le restamos un tercio de la fila dos.")
        m = self.operar_filas(m, ("sumar", 2, 1, Fraction(-1, 3)))
        self.play(Create(escalera(m, [(0, 0), (1, 2)])))
        self.decir("La escalera salta la columna dos: la ye no tiene pivote. Eso produce variables libres, como veremos en la lección veintiocho.")
        self.pie("La escalera salta la columna 2: la y no tiene pivote. Eso produce variables libres (L28).", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Concluir ``no tiene solución'' al ver un pivote 0: primero se busca debajo.", font_size=36),
            Tex(r"Intercambiar con una fila de arriba, ya usada: se pierden ceros.", font_size=36),
            Tex(r"Intercambiar solo los coeficientes: se intercambia la fila entera, con $\mathbf{b}$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: concluir que no hay solución al ver un pivote cero, sin buscar debajo; intercambiar con una fila de arriba, ya usada; e intercambiar solo los coeficientes, cuando se intercambia la fila entera, con be.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N2-05",
            VGroup(
                Text("Resuelve por Gauss (aparecerá un pivote 0) y verifica:", font_size=TAM_TEXTO),
                MathTex(r"\left[\begin{array}{ccc|c} 1 & 2 & 1 & 4 \\ 2 & 4 & 3 & 9 \\ 1 & 3 & 2 & 6 \end{array}\right]", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Pivote 0: se intercambia con una fila de más abajo con entrada no nula.",
                "El intercambio conserva las soluciones y los ceros ya conseguidos.",
                "Si toda la columna es 0 hacia abajo, no hay pivote: se pasa a la siguiente.",
            ],
            "filas nulas y ecuaciones redundantes.",
            voz="En resumen: si el pivote vale cero, se intercambia con una fila de más abajo que tenga una entrada no nula. El intercambio conserva las soluciones y los ceros ya conseguidos. Y si toda la columna es cero hacia abajo, no hay pivote: se pasa a la siguiente. Siguiente: filas nulas y ecuaciones redundantes.",
        )


class FilaNulaEcuacionRedundante(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 27 · Parte 2", "Filas nulas y ecuaciones redundantes")
        titulo = self.encabezado("Tres ecuaciones, dos incógnitas")
        s = sistema_con_llave(("x + y", "=", "3"), ("x - y", "=", "1"), ("3x + y", "=", "7"), font_size=40, colores=False).move_to(LEFT * 5.2 + UP * 0.6)
        m = matriz_gauss([[1, 1, 3], [1, -1, 1], [3, 1, 7]], pivotes=[(0, 0)]).move_to(LEFT * 2 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Tres ecuaciones con dos incógnitas: equis más ye igual a tres, equis menos ye igual a uno, y tres equis más ye igual a siete.")
        self.play(Write(s), FadeIn(m), FadeIn(historial))
        self.decir("Eliminamos en la columna uno: restamos la fila uno a la dos, y tres veces la fila uno a la tres.")
        m = self.operar_filas(m, ("sumar", 1, 0, -1), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 0, -3), historial=historial, pivotes=[(0, 0), (1, 1)])
        self.decir("Y en la columna dos, a la fila tres le restamos la fila dos.")
        m = self.operar_filas(m, ("sumar", 2, 1, -1), historial=historial)
        lectura = MathTex(r"0x + 0y = 0", font_size=40, color=COLOR_SECUNDARIO).next_to(m, DOWN, buff=0.5)
        self.decir("Queda una fila de ceros, también en be: cero igual a cero.")
        self.play(Write(lectura))
        self.decir("Esa ecuación la cumple cualquier par: no aporta información, y se puede quitar.")
        self.pie("Una fila nula, también en b, dice 0 = 0: la cumple cualquier par (x, y). No aporta información y se puede quitar.", espera=4)
        self.quitar_pie()
        sol = MathTex(r"-2y = -2 \Rightarrow y = 1,\qquad x + 1 = 3 \Rightarrow x = 2", font_size=38, color=COLOR_SOLUCION).next_to(lectura, DOWN, buff=0.4)
        self.decir("Menos dos ye igual a menos dos: ye vale uno. Y equis más uno igual a tres: equis vale dos.")
        self.play(Write(sol))
        self.decir("Solución única: dos, uno. Hay dos pivotes para dos incógnitas. Lo que cuenta no es el número de ecuaciones, sino el de pivotes.")
        self.pie("Solución única (2, 1): hay 2 pivotes para 2 incógnitas. Lo que cuenta no es el número de ecuaciones, sino el de pivotes.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Qué ecuación sobraba?")
        rastro = VGroup(
            MathTex(r"R_3^{\text{final}} = (R_3 - 3R_1) - (R_2 - R_1) = R_3 - 2R_1 - R_2 = \mathbf{0}", font_size=40),
            MathTex(r"\Longrightarrow\quad E_3 = 2E_1 + E_2", font_size=44, color=COLOR_OPERACION),
            MathTex(r"2(x + y) + (x - y) = 3x + y, \qquad 2\cdot 3 + 1 = 7\ \checkmark", font_size=40),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        self.decir("¿Qué ecuación sobraba? La fila tres final es la tres, menos dos veces la uno, menos la dos. Así que la tercera ecuación es dos veces la primera más la segunda.")
        for r in rastro:
            self.play(Write(r))
            self.wait(2)
        self.decir("La tercera ecuación es combinación de las otras dos: es redundante. Toda solución de las dos primeras cumple automáticamente la tercera.")
        self.pie("La tercera ecuación es combinación de las otras dos: es redundante.\nToda solución de las dos primeras cumple automáticamente la tercera.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "En el plano: tres rectas por un punto")
        ejes = ejes_iguales((-1, 4), (-1, 4), unidad=0.95).shift(LEFT * 2.2 + DOWN * 0.4)
        rectas = rectas_de_sistema(ejes, [(1, 1, 3), (1, -1, 1), (3, 1, 7)])
        etiquetas = VGroup(
            MathTex(r"x + y = 3", color=COLORES_ECUACIONES[0], font_size=36),
            MathTex(r"x - y = 1", color=COLORES_ECUACIONES[1], font_size=36),
            MathTex(r"3x + y = 7", color=COLORES_ECUACIONES[2], font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(ejes, RIGHT, buff=1).shift(UP * 0.8)
        self.decir("En el plano: tres rectas.")
        self.play(Create(ejes))
        for r, e in zip(rectas, etiquetas):
            self.play(Create(r), FadeIn(e))
        punto = Dot(ejes.c2p(2, 1), color=COLOR_SOLUCION, radius=0.1)
        self.decir("La tercera recta pasa por el punto donde ya se cortaban las otras dos: el dos, uno.")
        self.play(FadeIn(punto, scale=2), FadeIn(MathTex("(2, 1)", color=COLOR_SOLUCION, font_size=36).next_to(punto, UR, buff=0.1)))
        self.pie("La tercera recta pasa por el punto donde ya se cortaban las otras dos (L12).", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Caso alternativo: la fila nula no llega hasta b")
        m = matriz_gauss([[1, 1, 3], [0, -2, -2], [0, 0, 1]], pivotes=[(0, 0), (1, 1)]).shift(LEFT * 3 + UP * 0.6)
        self.decir("¿Y si la fila nula no llega hasta be?")
        self.play(FadeIn(m))
        self.play(m.get_rows()[2].animate.set_color(COLOR_ERROR))
        texto = parrafo(r"Si la tercera ecuación fuera $3x + y = 8$,", r"la última fila sería $[\,0 \ \ 0 \mid 1\,]$:", r"$0 = 1$, imposible.", font_size=36)
        texto.next_to(m, RIGHT, buff=1)
        self.decir("Si la tercera ecuación fuera tres equis más ye igual a ocho, la última fila sería cero, cero, uno: cero igual a uno, imposible.")
        self.play(FadeIn(texto))
        self.decir("Solo es redundante si la fila es nula entera, columna de be incluida. Si no, el sistema no tiene solución.")
        self.pie("Solo es redundante si la fila es nula ENTERA, columna de b incluida. Si no, el sistema no tiene solución (L28).", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Leer una fila nula como ``no hay solución'': $0 = 0$ siempre se cumple.", font_size=36),
            Tex(r"Tachar la fila sin mirar la columna de $\mathbf{b}$.", font_size=36),
            Tex(r"Clasificar contando ecuaciones en lugar de pivotes.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: leer una fila nula como que no hay solución, cuando cero igual a cero siempre se cumple; tachar la fila sin mirar la columna de be; y clasificar contando ecuaciones en lugar de pivotes.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N3-02",
            VGroup(
                Text("Resuelve por Gauss. ¿Qué ecuación es combinación de las otras? Escribe la relación.", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y = 4 \\ 2x - y = 3 \\ 4x + 3y = 11 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Una fila [0 … 0 | 0] es la ecuación 0 = 0: redundante, se puede quitar.",
                "Indica que una ecuación era combinación de las demás.",
                "Lo que decide es el número de pivotes, no el de ecuaciones.",
            ],
            "Lección 28 — sistemas sin solución y con infinitas soluciones.",
            voz="En resumen: una fila de ceros, también en be, es la ecuación cero igual a cero: redundante, y se puede quitar. Indica que una ecuación era combinación de las demás. Y lo que decide es el número de pivotes, no el de ecuaciones. Siguiente: lección veintiocho, sistemas sin solución y con infinitas soluciones.",
        )
