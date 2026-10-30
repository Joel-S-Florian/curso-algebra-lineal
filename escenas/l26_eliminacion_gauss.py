"""Lección 26 — Eliminación hacia adelante y sustitución hacia atrás.

Escenas (un video cada una):
    GaussDosPorDos, GaussTresPorTres

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l26_eliminacion_gauss.py -a
"""

import sys
from fractions import Fraction
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz_gauss, parrafo, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def sistema(*ecuaciones, font_size=40):
    return sistema_con_llave(*ecuaciones, font_size=font_size, colores=False)


def sustitucion_atras(escena, m, filas, pasos, x=2.6, font_size=40):
    """Escribe cada paso de la sustitución hacia atrás recuadrando la fila que usa."""
    lineas = VGroup(*[MathTex(p, font_size=font_size) for p in pasos]).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
    lineas.match_y(m).set_x(x)
    ajustar_al_encuadre(lineas)
    for i, linea in zip(filas, lineas):
        marco = SurroundingRectangle(m.get_rows()[i], color=COLOR_PIVOTE)
        escena.play(Create(marco), Write(linea))
        escena.wait(1.5)
        escena.play(FadeOut(marco))
    return lineas


class GaussDosPorDos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 26 · Parte 1", "Gauss en un sistema 2 × 2")
        titulo = self.encabezado("La estrategia en dos fases")
        fases = VGroup(
            parrafo(r"\textbf{1. Eliminación hacia adelante}: con operaciones elementales, ceros", r"debajo de cada pivote, columna a columna, hasta la forma escalonada.", font_size=38, sangria=0.45),
            parrafo(r"\textbf{2. Sustitución hacia atrás}: se resuelve la última ecuación", r"y se sube sustituyendo lo ya conocido.", font_size=38, sangria=0.45),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        multiplicador = MathTex(
            r"R_i \leftarrow R_i - m\,R_p, \qquad m = \frac{\text{entrada que se quiere anular}}{\text{pivote}}",
            font_size=40, color=COLOR_OPERACION,
        ).next_to(fases, DOWN, buff=0.7)
        self.decir("La eliminación de Gauss tiene dos fases. Primera, eliminación hacia adelante: con operaciones elementales, ceros debajo de cada pivote, columna a columna, hasta la forma escalonada. Segunda, sustitución hacia atrás: se resuelve la última ecuación, y se sube sustituyendo lo ya conocido.")
        for f in fases:
            self.play(FadeIn(f))
            self.wait(2)
        self.decir("Para anular una entrada, a su fila le restamos eme veces la fila del pivote. El multiplicador eme es la entrada que queremos anular dividida entre el pivote.")
        self.play(Write(multiplicador))
        self.pie("m es el multiplicador: el número de veces que se resta la fila del pivote para que debajo quede un 0.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Sistema y matriz, paso a paso")
        s = sistema(("2x + 3y", "=", "8"), ("4x - y", "=", "2")).move_to(LEFT * 4.6 + UP * 0.8)
        m = matriz_gauss([[2, 3, 8], [4, -1, 2]], pivotes=[(0, 0)]).move_to(LEFT * 0.6 + UP * 0.8)
        self.decir("Veámoslo en un sistema de dos por dos: dos equis más tres ye igual a ocho, y cuatro equis menos ye igual a dos.")
        self.play(Write(s), FadeIn(m))
        calculo = MathTex(r"m = \frac{4}{2} = 2", font_size=40, color=COLOR_OPERACION).next_to(m, DOWN, buff=0.5)
        self.decir("El multiplicador es cuatro entre dos: dos.")
        self.play(Indicate(m.get_rows()[1][0]), Indicate(m.get_rows()[0][0]), Write(calculo))
        self.wait(2)
        self.play(FadeOut(calculo))
        self.decir("A la fila dos le restamos dos veces la fila uno.")
        m = self.operar_filas(m, ("sumar", 1, 0, -2), pivotes=[(0, 0), (1, 1)])
        self.decir("En el sistema, la equis desaparece de la segunda ecuación: menos siete ye igual a menos catorce.")
        self.play(ReplacementTransform(s, sistema(("2x + 3y", "=", "8"), ("-7y", "=", "-14")).move_to(s)))
        self.play(Create(escalera(m, [(0, 0), (1, 1)])))
        self.pie("Cada fila de la matriz es una ecuación del sistema: la x desapareció de la segunda ecuación.", espera=3)
        self.quitar_pie()
        lineas = sustitucion_atras(self, m, (1, 0), (r"-7y = -14 \;\Rightarrow\; y = 2", r"2x + 3\cdot 2 = 8 \;\Rightarrow\; x = 1"), x=4.3)
        self.decir("Ahora, sustitución hacia atrás. Primero la última ecuación: ye vale dos. Arriba, dos equis más seis igual a ocho: equis vale uno.")
        self.pie("Sustitución hacia atrás: primero la última ecuación (una incógnita), luego la de arriba.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificación en el sistema ORIGINAL")
        verif = VGroup(
            MathTex(r"2x + 3y = 8:\quad 2\cdot 1 + 3\cdot 2 = 8\ \checkmark", font_size=44),
            MathTex(r"4x - y = 2:\quad 4\cdot 1 - 2 = 2\ \checkmark", font_size=44),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(UP * 0.5)
        verif.set_color(COLOR_SOLUCION)
        self.decir("Y comprobamos en el sistema original: dos más seis, ocho; cuatro menos dos, dos.")
        for v in verif:
            self.play(Write(v))
            self.wait(1)
        self.decir("Se comprueba en el original, no en el escalonado: un error de cuentas al eliminar no se detecta en el sistema ya transformado.")
        self.pie("Se comprueba en el original, no en el escalonado: un error de cuentas al eliminar no se detecta en el sistema ya transformado.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Si el multiplicador es una fracción")
        m = matriz_gauss([[2, 3, 8], [3, 1, 5]], pivotes=[(0, 0)]).move_to(LEFT * 2 + UP * 0.8)
        self.decir("Si el multiplicador es una fracción, no pasa nada.")
        self.play(FadeIn(m))
        self.decir("Aquí eme es tres medios: se opera con fracciones exactas.")
        self.pie("m = 3/2: no pasa nada, se opera con fracciones exactas.")
        m = self.operar_filas(m, ("sumar", 1, 0, Fraction(-3, 2)), pivotes=[(0, 0), (1, 1)])
        res = MathTex(r"-\tfrac{7}{2}\,y = -7 \;\Rightarrow\; y = 2,\qquad 2x + 6 = 8 \;\Rightarrow\; x = 1", font_size=38, color=COLOR_SOLUCION)
        res.next_to(m, DOWN, buff=0.6).set_x(0)
        self.decir("Menos siete medios por ye igual a menos siete: ye vale dos. Y equis vale uno.")
        self.play(Write(res))
        self.decir("Dos más seis, ocho; tres más dos, cinco. También se puede escalar primero, para evitar las fracciones.")
        self.pie("Comprobación: 2 + 6 = 8 y 3 + 2 = 5. También vale R₂ ← 2R₂ - 3R₁ (escalar por 2 y sumar), que evita fracciones.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Equivocar el signo: $R_2 \leftarrow R_2 + 2R_1$ da $4 + 4 = 8$, no un $0$.", font_size=36),
            Tex(r"Invertir el cociente: $m = \frac{\text{pivote}}{\text{entrada}}$ no anula nada.", font_size=36),
            Tex(r"Olvidar la columna de $\mathbf{b}$ al restar.", font_size=36),
            Tex(r"Verificar en el sistema escalonado en lugar del original.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: equivocar el signo, porque sumar dos veces la fila uno da ocho, no cero; invertir el cociente; olvidar la columna de be al restar; y verificar en el sistema escalonado en lugar del original.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N2-03",
            VGroup(
                Text("Resuelve por eliminación de Gauss (escribe cada operación) y verifica:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} 3x + 2y = 7 \\ 6x - y = 4 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Hacia adelante: ceros debajo de cada pivote restando m veces su fila, m = entrada / pivote.",
                "Hacia atrás: última ecuación primero y se sube sustituyendo.",
                "Se verifica siempre en el sistema original.",
            ],
            "Gauss completo en un sistema 3 × 3.",
            voz="En resumen: hacia adelante, se hacen ceros debajo de cada pivote restando eme veces su fila, con eme igual a la entrada entre el pivote. Hacia atrás, se resuelve primero la última ecuación y se sube sustituyendo. Y siempre se verifica en el sistema original. Siguiente: Gauss completo en un sistema de tres por tres.",
        )


class GaussTresPorTres(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 26 · Parte 2", "Gauss en un sistema 3 × 3")
        titulo = self.encabezado("El sistema")
        s = sistema(("x + 2y - z", "=", "-3"), ("2x + 3y + z", "=", "1"), ("-x + y + 2z", "=", "2"), font_size=44).shift(LEFT * 3 + UP * 0.4)
        m = matriz_gauss([[1, 2, -1, -3], [2, 3, 1, 1], [-1, 1, 2, 2]]).shift(RIGHT * 3 + UP * 0.4)
        self.decir("Ahora un sistema de tres ecuaciones con tres incógnitas.")
        self.play(Write(s))
        self.decir("Lo pasamos a la matriz aumentada.")
        self.play(TransformFromCopy(s, m), run_time=2)
        self.consolidar(m)
        self.decir("El objetivo: tres ceros debajo de la diagonal. Primero en la columna uno, después en la columna dos.")
        self.pie("Objetivo: tres ceros debajo de la diagonal. Primero la columna 1, después la columna 2.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Columna 1: el pivote es el 1 de arriba")
        m = matriz_gauss([[1, 2, -1, -3], [2, 3, 1, 1], [-1, 1, 2, 2]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("En la columna uno, el pivote es el uno de arriba.")
        self.play(FadeIn(m), FadeIn(historial))
        self.decir("A la fila dos le restamos dos veces la fila uno.")
        m = self.operar_filas(m, ("sumar", 1, 0, -2), historial=historial)
        self.decir("Y a la fila tres le sumamos la fila uno.")
        m = self.operar_filas(m, ("sumar", 2, 0, 1), historial=historial, pivotes=[(0, 0), (1, 1)])
        titulo = self.cambiar_encabezado(titulo, "Columna 2: el pivote es el -1 de la fila 2 nueva")
        self.decir("Ahora el pivote de la columna dos es el menos uno de la fila dos nueva. Tres entre menos uno es menos tres: a la fila tres le sumamos tres veces la fila dos. Solo usamos filas que ya tienen cero en la columna uno, así no se pierden los ceros conseguidos.")
        self.pie("m = 3 / (-1) = -3, así que R₃ ← R₃ - (-3)R₂ = R₃ + 3R₂. Solo se usan filas que ya tienen 0 en la columna 1:\nlos ceros conseguidos no se estropean.")
        m = self.operar_filas(m, ("sumar", 2, 1, 3), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        self.quitar_pie()
        self.decir("La matriz ya está escalonada.")
        self.play(Create(escalera(m, [(0, 0), (1, 1), (2, 2)])))
        self.wait(2)
        self.play(FadeOut(historial))

        titulo = self.cambiar_encabezado(titulo, "Sustitución hacia atrás")
        self.decir("Sustitución hacia atrás: diez zeta igual a veinte, zeta vale dos. Menos ye más seis igual a siete: ye vale menos uno. Y equis menos dos menos dos igual a menos tres: equis vale uno.")
        sustitucion_atras(
            self, m, (2, 1, 0),
            (r"10z = 20 \;\Rightarrow\; z = 2", r"-y + 3\cdot 2 = 7 \;\Rightarrow\; y = -1", r"x + 2(-1) - 2 = -3 \;\Rightarrow\; x = 1"),
            x=3.4,
        )
        self.decir("La solución es uno, menos uno, dos.")
        self.pie("Solución: (x, y, z) = (1, -1, 2).", color=COLOR_SOLUCION, espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificación en el sistema original")
        verif = VGroup(
            MathTex(r"x + 2y - z:\quad 1 - 2 - 2 = -3\ \checkmark", font_size=42),
            MathTex(r"2x + 3y + z:\quad 2 - 3 + 2 = 1\ \checkmark", font_size=42),
            MathTex(r"-x + y + 2z:\quad -1 - 1 + 4 = 2\ \checkmark", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(UP * 0.5)
        verif.set_color(COLOR_SOLUCION)
        self.decir("Las tres ecuaciones originales se cumplen: uno menos dos menos dos, menos tres; dos menos tres más dos, uno; y menos uno menos uno más cuatro, dos.")
        for v in verif:
            self.play(Write(v))
            self.wait(1)
        self.decir("En forma matricial: a por la solución da be.")
        self.pie("En forma matricial: A(1, -1, 2) = (-3, 1, 2) = b (L22).", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Por qué en este orden?")
        razones = VGroup(
            Tex(r"Columna a columna, de izquierda a derecha, con la fila del pivote actual.", font_size=36),
            parrafo(r"Si en la columna 2 usáramos $R_1$ (por ejemplo $R_3 \leftarrow R_3 - 3R_1$),", r"volvería a aparecer la $x$ en la fila 3: se pierde un cero ya conseguido.", font_size=36),
            Tex(r"En un sistema $n\times n$ hay que conseguir $\frac{n(n-1)}{2}$ ceros: $1$ si $n = 2$, $3$ si $n = 3$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(razones)
        self.decir("¿Por qué en este orden? Columna a columna, de izquierda a derecha, con la fila del pivote actual. Si en la columna dos usáramos la fila uno, volvería a aparecer la equis en la fila tres: se perdería un cero. En un sistema de tres por tres hay que conseguir tres ceros.")
        for r in razones:
            self.play(FadeIn(r))
            self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            parrafo(r"Usar la fila 2 \textbf{vieja} como pivote de la columna 2:", r"hay que usar la ya transformada.", font_size=34, sangria=0.4),
            Tex(r"Signos con pivote negativo: $m = 3/(-1) = -3$, y restar $-3R_2$ es sumar $3R_2$.", font_size=34),
            Tex(r"Sustituir hacia atrás con un valor mal copiado: apunta cada valor al hallarlo.", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes: usar la fila dos vieja como pivote de la columna dos, en vez de la ya transformada; equivocar los signos con un pivote negativo; y copiar mal un valor en la sustitución hacia atrás.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N2-04",
            VGroup(
                Text("Resuelve por eliminación de Gauss y verifica en el sistema original:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + y + 2z = 3 \\ 2x + 3y + z = 2 \\ -x + 2y + 3z = -1 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "3 × 3: dos ceros con el pivote de la columna 1, uno con el de la columna 2.",
                "Cada pivote se usa solo para anular lo que tiene debajo.",
                "Sustitución hacia atrás z, y, x, y verificación en el original.",
            ],
            "Lección 27 — pivotes nulos y filas nulas.",
            voz="En resumen: en un sistema de tres por tres, se hacen dos ceros con el pivote de la columna uno, y uno con el de la columna dos. Cada pivote se usa solo para anular lo que tiene debajo. Después, sustitución hacia atrás, zeta, ye y equis, y verificación en el original. Siguiente: lección veintisiete, pivotes nulos y filas nulas.",
        )
