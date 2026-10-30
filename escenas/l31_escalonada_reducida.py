"""Lección 31 — Forma escalonada reducida (Gauss-Jordan).

Escenas (un video cada una):
    DeEscalonadaAReducida, EliminarArribaYAbajo, LaReducidaEsUnica

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l31_escalonada_reducida.py -a
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


class DeEscalonadaAReducida(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 31 · Parte 1", "Forma escalonada reducida")
        titulo = self.encabezado("Seguir hasta que la solución se lea sola")
        esc = matriz_gauss([[1, 2, -1, -3], [0, -1, 3, 7], [0, 0, 10, 20]], pivotes=[(0, 0), (1, 1), (2, 2)]).shift(LEFT * 3.4 + UP * 0.6)
        red = matriz_gauss([[1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 2]], pivotes=[(0, 0), (1, 1), (2, 2)]).shift(RIGHT * 3.4 + UP * 0.6)
        flecha = Arrow(esc.get_right(), red.get_left(), buff=0.3)
        rotulo = Text("Gauss-Jordan", font_size=TAM_NOTA, color=COLOR_OPERACION).next_to(flecha, UP, buff=0.1)
        nota_esc = Text("hay que sustituir\nhacia atrás", font_size=TAM_NOTA, color=COLOR_SECUNDARIO, line_spacing=1.1).next_to(esc, DOWN, buff=0.5)
        nota_red = Tex(r"se lee directamente:\\ $x = 1,\ y = -1,\ z = 2$", font_size=34, color=COLOR_SOLUCION).next_to(red, DOWN, buff=0.5)
        self.decir("Esta es la forma escalonada del sistema de la lección veintiséis. Para leer la solución, hay que sustituir hacia atrás.")
        self.play(FadeIn(esc))
        self.play(Create(escalera(esc, [(0, 0), (1, 1), (2, 2)])), FadeIn(nota_esc))
        self.decir("Si seguimos operando con las filas, llegamos a esta otra matriz, equivalente a la anterior: tiene la misma solución, pero se lee directamente. Equis uno, ye menos uno, zeta dos. Se llama forma escalonada reducida.")
        self.play(GrowArrow(flecha), FadeIn(rotulo))
        self.play(FadeIn(red))
        self.play(FadeIn(nota_red))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición")
        definicion = VGroup(
            Tex(r"Una matriz está en \textbf{forma escalonada reducida} si:", font_size=38),
            Tex(r"(1) está en forma escalonada;", font_size=38),
            Tex(r"(2) cada pivote vale $1$;", font_size=38, color=COLOR_PIVOTE),
            parrafo(r"(3) cada pivote es la \textbf{única} entrada no nula de su columna", r"(ceros arriba \emph{y} abajo).", font_size=38, sangria=0.6, color=COLOR_PIVOTE),
            Tex(r"Gauss deja ceros solo \emph{debajo} de los pivotes; Gauss-Jordan, también \emph{encima}.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(definicion)
        self.decir("Una matriz está en forma escalonada reducida si cumple tres cosas. Uno: está en forma escalonada. Dos: cada pivote vale uno. Y tres: cada pivote es la única entrada no nula de su columna; hay ceros arriba, y también abajo. Gauss deja ceros solo debajo de los pivotes; Gauss-Jordan, también encima.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(1.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Reducida o no?")
        ejemplos = VGroup(
            ejemplo([[1, 0, 2], [0, 1, 3]], [(0, 0), (1, 1)], True, "sí: pivotes 1 y\nceros arriba y abajo"),
            ejemplo([[1, 0, 2], [0, 2, 3]], [(0, 0), (1, 1)], False, "no: un pivote\nvale 2"),
            ejemplo([[1, 2, 0], [0, 1, 3]], [(0, 0), (1, 1)], False, "no: encima del\npivote 1 hay un 2"),
            ejemplo([[1, 0, 3, 0], [0, 0, 0, 1], [0, 0, 0, 0]], [(0, 0), (1, 3)], True, "sí: la columna sin\npivote puede tener números"),
        ).arrange(RIGHT, buff=0.6, aligned_edge=UP).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(ejemplos)
        self.decir("¿Reducida o no? La primera sí: pivotes uno, con ceros arriba y abajo. La segunda no: un pivote vale dos. La tercera no: encima del pivote de la segunda fila hay un dos. Y la cuarta sí: la columna sin pivote puede tener cualquier número.")
        for e in ejemplos:
            self.play(FadeIn(e[0]))
            self.wait(1.2)
            self.play(FadeIn(e[1]), FadeIn(e[2]))
            self.wait(1.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Olvidar los ceros \emph{encima} de un pivote: eso es solo escalonada.", font_size=36),
            Tex(r"Dejar un pivote distinto de $1$: hay que dividir la fila entera, con $\mathbf{b}$.", font_size=36),
            Tex(r"Pensar que las columnas sin pivote deben ser ceros: pueden valer cualquier cosa.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes: olvidar los ceros encima de un pivote, porque entonces la matriz es solo escalonada; dejar un pivote distinto de uno, cuando hay que dividir la fila entera, con be; y pensar que las columnas sin pivote deben ser ceros, cuando pueden valer cualquier número.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2)

        self.ejercicio_propuesto(
            "F09-N1-01",
            VGroup(
                Text("¿Cuáles de estas matrices están en forma escalonada reducida?", font_size=TAM_TEXTO),
                MathTex(
                    r"A = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 2 \end{bmatrix} \quad B = \begin{bmatrix} 1 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad C = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}",
                    font_size=40,
                ),
                Text("Justifica cada respuesta con la definición.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: decide cuáles de estas tres matrices están en forma escalonada reducida, y justifica cada respuesta con la definición. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Reducida = escalonada + pivotes iguales a 1 + ceros también encima de cada pivote.",
                "Gauss deja ceros debajo de los pivotes; Gauss-Jordan, también encima.",
                "De la reducida la solución se lee directamente.",
            ],
            "cómo se llega a ella, paso a paso.",
            voz="En resumen: una matriz es escalonada reducida si es escalonada, sus pivotes valen uno, y hay ceros también encima de cada pivote. Gauss deja ceros debajo de los pivotes; Gauss-Jordan, también encima. Y de la reducida, la solución se lee directamente. Siguiente: cómo se llega a ella, paso a paso.",
        )


class EliminarArribaYAbajo(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 31 · Parte 2", "Gauss-Jordan paso a paso")
        titulo = self.encabezado("Primero, Gauss: ceros debajo")
        m = matriz_gauss([[1, 1, 1, 6], [1, -1, 1, 2], [1, 1, -1, 0]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Tomemos el sistema de la lección quince: equis más ye más zeta igual a seis; equis menos ye más zeta igual a dos; y equis más ye menos zeta igual a cero. Primero hacemos Gauss: ceros debajo del pivote.")
        self.play(FadeIn(m), FadeIn(historial))
        self.decir("A la fila dos le restamos la fila uno.")
        m = self.operar_filas(m, ("sumar", 1, 0, -1), historial=historial)
        self.decir("Y a la fila tres, también.")
        m = self.operar_filas(m, ("sumar", 2, 0, -1), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        self.decir("La matriz ya está escalonada: hasta aquí llega Gauss. En la lección veintiséis ahora sustituíamos hacia atrás; en Gauss-Jordan, seguimos operando con las filas.")
        self.play(Create(escalera(m, [(0, 0), (1, 1), (2, 2)])))
        self.wait(1)
        titulo = self.cambiar_encabezado(titulo, "Segundo: pivotes a 1")
        self.decir("Segundo paso: hacer que cada pivote valga uno. Multiplicamos la fila dos por menos un medio.")
        m = self.operar_filas(m, ("escalar", 1, Fraction(-1, 2)), historial=historial)
        self.decir("Y la fila tres, también.")
        m = self.operar_filas(m, ("escalar", 2, Fraction(-1, 2)), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        titulo = self.cambiar_encabezado(titulo, "Tercero: ceros encima, de derecha a izquierda")
        self.decir("Tercer paso: ceros encima de los pivotes, empezando por el último, el de la derecha. A la fila uno le restamos la fila tres.")
        m = self.operar_filas(m, ("sumar", 0, 2, -1), historial=historial)
        self.decir("Y le restamos la fila dos.")
        m = self.operar_filas(m, ("sumar", 0, 1, -1), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        lectura = Tex(r"$x = 1,\quad y = 2,\quad z = 3$", font_size=44, color=COLOR_SOLUCION).next_to(m, DOWN, buff=0.6)
        self.decir("Ya está en forma reducida. La solución se lee directamente: equis uno, ye dos, zeta tres.")
        self.play(Write(lectura))
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El algoritmo de Gauss-Jordan")
        pasos = VGroup(
            parrafo(r"\textbf{1.} Eliminación hacia adelante (Gauss): forma escalonada.", font_size=38),
            parrafo(r"\textbf{2.} Dividir cada fila no nula por su pivote: pivotes iguales a $1$.", font_size=38),
            parrafo(r"\textbf{3.} Ceros encima de cada pivote, de derecha a izquierda.", font_size=38),
            parrafo(r"\textbf{4.} Leer la solución en la matriz reducida.", font_size=38, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        nota = parrafo(
            r"Cada cero de arriba es un paso de la sustitución hacia atrás,",
            r"hecho directamente sobre la matriz.",
            font_size=34, color=COLOR_SECUNDARIO,
        ).next_to(pasos, DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(pasos, nota))
        self.decir("El algoritmo de Gauss-Jordan, entonces. Uno: eliminación hacia adelante, hasta la forma escalonada. Dos: dividir cada fila no nula por su pivote. Tres: ceros encima de cada pivote, de derecha a izquierda. Y cuatro: leer la solución en la matriz reducida.")
        for p in pasos:
            self.play(FadeIn(p))
            self.wait(1.5)
        self.decir("Cada cero de arriba es un paso de la sustitución hacia atrás, hecho directamente sobre la matriz.")
        self.play(FadeIn(nota))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Por qué de derecha a izquierda?")
        razon = VGroup(
            Tex(r"Con el pivote de la columna 3 se anulan sus entradas de arriba; las columnas 1 y 2 no cambian.", font_size=34),
            Tex(r"Si empezáramos por la columna 2, al usar la fila 3 después se volvería a ensuciar lo ya hecho.", font_size=34),
            Tex(r"Además, al empezar por la derecha, la fila de pivote tiene ceros a su izquierda: solo cambia su columna y las de la derecha.", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(razon)
        self.decir("¿Por qué de derecha a izquierda? Porque la fila de un pivote tiene ceros a su izquierda: al usarla, solo cambian su propia columna y las de su derecha, y los ceros ya conseguidos no se estropean.")
        for r in razon:
            self.play(FadeIn(r))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F09-N2-02",
            VGroup(
                Text("Resuelve por Gauss-Jordan (escribe cada operación) y verifica en el original:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + y + z = 2 \\ 2x + 3y + z = 7 \\ x - y + 2z = -3 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: resuelve este sistema por Gauss-Jordan, escribiendo cada operación, y verifica la solución en el sistema original. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Gauss-Jordan: escalonar, pivotes a 1, ceros encima de derecha a izquierda.",
                "La solución se lee en la última columna de la reducida.",
                "Siempre se verifica en el sistema original.",
            ],
            "la reducida es única.",
            voz="En resumen: en Gauss-Jordan se escalona, se llevan los pivotes a uno, y se hacen ceros encima de ellos, de derecha a izquierda. La solución se lee en la última columna de la matriz reducida. Y siempre se verifica en el sistema original. Siguiente: la forma reducida es única.",
        )


class LaReducidaEsUnica(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 31 · Parte 3", "La forma reducida es única")
        titulo = self.encabezado("Dos caminos, una sola reducida")
        arriba, abajo = UP * 1.5, DOWN * 1.2
        ma = matriz_gauss([[2, 4, 10], [3, -1, 1]], pivotes=[(0, 0)]).move_to(LEFT * 4.4 + arriba)
        mb = matriz_gauss([[2, 4, 10], [3, -1, 1]]).move_to(LEFT * 4.4 + abajo)
        ha = VGroup(Text("Camino A", font_size=TAM_NOTA + 2, color=COLOR_SECUNDARIO)).move_to(RIGHT * 0.5 + UP * 2.3)
        hb = VGroup(Text("Camino B", font_size=TAM_NOTA + 2, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.6 + UP * 2.3)
        self.decir("En la lección veinticinco vimos que una matriz tiene muchas formas escalonadas. Partamos otra vez de la misma matriz, por dos caminos distintos, hasta la forma reducida.")
        self.play(FadeIn(ma), FadeIn(mb), FadeIn(ha), FadeIn(hb))
        self.decir("Camino a: a la fila dos le restamos tres medios de la fila uno; dividimos la fila dos entre menos siete; a la fila uno le restamos cuatro veces la fila dos; y la dividimos entre dos.")
        ma = self.operar_filas(ma, ("sumar", 1, 0, Fraction(-3, 2)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=ha, espera=0.8)
        ma = self.operar_filas(ma, ("escalar", 1, Fraction(-1, 7)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=ha, espera=0.8)
        ma = self.operar_filas(ma, ("sumar", 0, 1, -4), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=ha, espera=0.8)
        ma = self.operar_filas(ma, ("escalar", 0, Fraction(1, 2)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=ha, espera=0.8)
        self.decir("Camino be: intercambiamos las filas; a la fila dos le restamos dos tercios de la fila uno; la dividimos por catorce tercios; sumamos la fila dos a la uno; y la dividimos entre tres.")
        mb = self.operar_filas(mb, ("intercambio", 0, 1), pivotes=[(0, 0)], cuenta=False, historial=hb, espera=0.8)
        mb = self.operar_filas(mb, ("sumar", 1, 0, Fraction(-2, 3)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=hb, espera=0.8)
        mb = self.operar_filas(mb, ("escalar", 1, Fraction(3, 14)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=hb, espera=0.8)
        mb = self.operar_filas(mb, ("sumar", 0, 1, 1), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=hb, espera=0.8)
        mb = self.operar_filas(mb, ("escalar", 0, Fraction(1, 3)), pivotes=[(0, 0), (1, 1)], cuenta=False, historial=hb, espera=0.8)
        igual = Text("¡La misma matriz!", font_size=TAM_TEXTO, color=COLOR_SOLUCION).to_edge(DOWN, buff=0.5)
        self.decir("Los dos caminos terminan en la misma matriz: uno, cero, uno; cero, uno, dos. Con la forma escalonada, cada camino daba una distinta; con la reducida, no.")
        self.play(FadeIn(igual))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Teorema")
        teorema = VGroup(
            Tex(r"\textbf{Teorema.} Toda matriz es equivalente por filas a \emph{una única}", font_size=40),
            Tex(r"matriz en forma escalonada reducida.", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(titulo, DOWN, buff=0.6)
        consecuencia = parrafo(
            r"Consecuencia: dos sistemas son equivalentes si y solo si sus matrices aumentadas",
            r"tienen la \emph{misma} reducida. La reducida es la ``huella'' del sistema.",
            font_size=36, color=COLOR_PIVOTE, sangria=0.4,
        ).next_to(teorema, DOWN, buff=0.7)
        self.decir("Esto no es casualidad: es un teorema. Toda matriz es equivalente por filas a una única matriz en forma escalonada reducida.")
        self.play(FadeIn(teorema))
        self.wait(2)
        self.decir("Una consecuencia: dos sistemas son equivalentes si y solo si sus matrices aumentadas tienen la misma reducida. La reducida es como la huella del sistema.")
        self.play(FadeIn(consecuencia))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Idea de la demostración")
        idea = VGroup(
            parrafo(r"\textbf{1.} Las operaciones por filas conservan las relaciones entre columnas:", r"$Mx = 0 \iff Rx = 0$ si $M$ y $R$ son equivalentes.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{2.} En una reducida, cada columna sin pivote es una suma de las columnas", r"pivote anteriores, multiplicadas por sus propias entradas.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{3.} Dos reducidas equivalentes tendrían las mismas relaciones:", r"mismas columnas pivote y mismas entradas. Luego son iguales.", font_size=34, sangria=0.5),
            Tex(r"(Los detalles necesitan combinaciones lineales: Unidad 8.)", font_size=30, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(idea)
        self.decir("La idea de la demostración tiene tres pasos. Uno: las operaciones por filas conservan las relaciones entre las columnas. Dos: en una reducida, cada columna sin pivote es una suma de las columnas pivote anteriores, multiplicadas por sus propias entradas. Y tres: dos reducidas equivalentes tendrían las mismas relaciones, es decir, las mismas columnas pivote y las mismas entradas; por tanto, serían iguales. Los detalles llegarán con las combinaciones lineales, en la unidad ocho.")
        for p in idea:
            self.play(FadeIn(p))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F09-N3-01",
            VGroup(
                Text("Reduce esta matriz por dos caminos distintos y comprueba que llegas a la misma reducida:", font_size=TAM_TEXTO),
                MathTex(r"\left[\begin{array}{cc|c} 0 & 2 & 4 \\ 1 & 1 & 3 \end{array}\right]", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: reduce esta matriz por dos caminos distintos, y comprueba que llegas a la misma forma reducida. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "La forma escalonada no es única; la reducida sí.",
                "Dos sistemas son equivalentes si y solo si tienen la misma reducida.",
                "Idea: las operaciones por filas conservan las relaciones entre columnas.",
            ],
            "Lección 32 — variables básicas y libres: leer la solución.",
            voz="En resumen: la forma escalonada no es única, pero la reducida sí. Dos sistemas son equivalentes si y solo si tienen la misma reducida. Y la idea de la demostración es que las operaciones por filas conservan las relaciones entre columnas. Siguiente: lección treinta y dos, variables básicas y libres: leer la solución.",
        )
