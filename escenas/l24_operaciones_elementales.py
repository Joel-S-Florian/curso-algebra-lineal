"""Lección 24 — Operaciones elementales por filas.

Escenas (un video cada una):
    OperacionesElementales, CadaOperacionSeDeshace

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l24_operaciones_elementales.py -a
"""

import sys
from fractions import Fraction
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz_gauss, meter_en_encuadre, parrafo, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def sistema(*ecuaciones, font_size=40):
    return sistema_con_llave(*ecuaciones, font_size=font_size, colores=False)


class OperacionesElementales(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 24 · Parte 1", "Las tres operaciones elementales")
        titulo = self.encabezado("Cambiar el sistema sin cambiar sus soluciones")
        idea = Tex(
            r"En la reducción (L15) cambiábamos ecuaciones por otras más sencillas.\\"
            r"Ahora lo hacemos con las filas de $[A\mid\mathbf{b}]$ y solo con \textbf{tres} movimientos:",
            font_size=36,
        ).next_to(titulo, DOWN, buff=0.6)
        tipos = VGroup(
            MathTex(r"\text{1. Intercambio: } R_i \leftrightarrow R_j"),
            MathTex(r"\text{2. Escalado: } R_i \leftarrow k\,R_i,\quad k \neq 0"),
            MathTex(r"\text{3. Reemplazo: } R_i \leftarrow R_i + k\,R_j,\quad i \neq j"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(idea, DOWN, buff=0.6)
        tipos.set_color(COLOR_OPERACION)
        self.decir("En la reducción cambiábamos ecuaciones por otras más sencillas. Ahora lo hacemos con las filas de la matriz aumentada, y solo con tres movimientos.")
        self.play(FadeIn(idea))
        self.decir("Uno: intercambiar dos filas. Dos: multiplicar una fila por un número distinto de cero. Y tres: sumar a una fila un múltiplo de otra fila.")
        for t in tipos:
            self.play(Write(t))
            self.wait(0.8)
        self.decir("Erre uno, erre dos son las filas. La flecha se lee: se sustituye por.")
        self.pie("R₁, R₂, … son las filas. La flecha se lee «se sustituye por»: R₂ ← 3R₂ significa «la fila 2 pasa a ser 3 veces ella misma».\nk es un número; i y j, los números de dos filas distintas.", espera=5)
        self.limpiar(titulo)

        # 1. Intercambio
        titulo = self.cambiar_encabezado(titulo, "1. Intercambiar dos filas")
        s = sistema(("3y", "=", "6"), ("x + y", "=", "3")).move_to(LEFT * 4.6 + UP * 0.6)
        m = matriz_gauss([[0, 3, 6], [1, 1, 3]]).move_to(LEFT * 0.6 + UP * 0.6)
        self.decir("Primera operación: intercambiar dos filas. Este sistema tiene un cero arriba, en la primera columna: conviene empezar por la otra ecuación.")
        self.play(Write(s), FadeIn(m))
        self.pie("Arriba hay un 0 en la primera columna: conviene empezar por la otra ecuación.")
        self.decir("Intercambiamos la fila uno y la fila dos.")
        m = self.operar_filas(m, ("intercambio", 0, 1))
        self.play(ReplacementTransform(s, sistema(("x + y", "=", "3"), ("3y", "=", "6")).move_to(s)))
        self.decir("Cambiar el orden de las ecuaciones no cambia qué pares las cumplen todas: sigue siendo ye igual a dos, equis igual a uno.")
        self.pie("Cambiar el orden de las ecuaciones no cambia qué pares (x, y) las cumplen todas: sigue siendo y = 2, x = 1.", espera=4)
        self.limpiar(titulo)

        # 2. Escalado
        titulo = self.cambiar_encabezado(titulo, "2. Multiplicar una fila por un número distinto de 0")
        s = sistema(("2x + 4y", "=", "10"), ("3x - y", "=", "1")).move_to(LEFT * 4.6 + UP * 0.8)
        m = matriz_gauss([[2, 4, 10], [3, -1, 1]]).move_to(LEFT * 0.6 + UP * 0.8)
        self.decir("Segunda operación: multiplicar una fila por un número distinto de cero.")
        self.play(Write(s), FadeIn(m))
        self.decir("Multiplicar la primera fila por un medio la simplifica: equis más dos ye igual a cinco.")
        m = self.operar_filas(m, ("escalar", 0, Fraction(1, 2)))
        s2 = sistema(("x + 2y", "=", "5"), ("3x - y", "=", "1")).move_to(s)
        self.play(ReplacementTransform(s, s2))
        self.decir("Y se puede volver atrás multiplicando por dos. Por eso el número tiene que ser distinto de cero.")
        self.pie("Si 2x + 4y = 10, entonces x + 2y = 5; y al revés, multiplicando por 2. Por eso k tiene que ser distinto de 0.", espera=4)
        self.quitar_pie()

        # Caso alternativo: k = 0
        mala = matriz_gauss([[1, 2, 5], [0, 0, 0]]).next_to(m, DOWN, buff=0.9)
        flecha = Arrow(m.get_bottom(), mala.get_top(), buff=0.1, color=COLOR_ERROR)
        rotulo = MathTex(r"R_2 \leftarrow 0\cdot R_2", font_size=36, color=COLOR_ERROR).next_to(flecha, RIGHT)
        self.decir("¿Qué pasa si multiplicamos por cero?")
        self.play(GrowArrow(flecha), Write(rotulo))
        self.play(FadeIn(mala))
        aviso = parrafo(r"$0x + 0y = 0$ la cumple todo par:", r"$(5, 0)$ cumple el sistema nuevo,", r"pero no $3x - y = 1$ \ ($15 \neq 1$).",
                        r"Se perdió una ecuación.", font_size=32, color=COLOR_ERROR)
        meter_en_encuadre(aviso.next_to(mala, RIGHT, buff=0.5))
        self.decir("La ecuación se convierte en cero igual a cero, que la cumple cualquier par. Cinco, cero cumple el sistema nuevo, pero no tres equis menos ye igual a uno: se perdió una ecuación.")
        self.play(FadeIn(aviso))
        self.wait(5)
        self.limpiar(titulo)

        # 3. Reemplazo
        titulo = self.cambiar_encabezado(titulo, "3. Sumar a una fila un múltiplo de otra")
        s = sistema(("x + 2y", "=", "5"), ("3x - y", "=", "1")).move_to(LEFT * 4.6 + UP * 0.8)
        m = matriz_gauss([[1, 2, 5], [3, -1, 1]], pivotes=[(0, 0)]).move_to(LEFT * 0.6 + UP * 0.8)
        self.decir("Tercera operación: sumar a una fila un múltiplo de otra.")
        self.play(Write(s), FadeIn(m))
        self.decir("Queremos un cero debajo del pivote uno, en amarillo: a la fila dos le restamos tres veces la fila uno.")
        self.pie("Queremos un 0 debajo del pivote 1 (amarillo): a la fila 2 le restamos 3 veces la fila 1.")
        m = self.operar_filas(m, ("sumar", 1, 0, -3))
        self.play(ReplacementTransform(s, sistema(("x + 2y", "=", "5"), ("-7y", "=", "-14")).move_to(s)))
        self.decir("Es la reducción de la lección quince, hecha con números. Solo cambia la fila destino; la fila de origen se queda igual.")
        self.pie("Es la reducción de la L15 hecha con números. Solo cambia la fila destino (R₂); la fila de origen (R₁) se queda igual.", espera=4)
        self.decir("Multiplicamos la segunda fila por menos un séptimo.")
        m = self.operar_filas(m, ("escalar", 1, Fraction(-1, 7)), pivotes=[(0, 0), (1, 1)])
        self.decir("Ya se lee la solución: ye igual a dos, y de equis más dos ye igual a cinco, equis igual a uno.")
        self.pie("Ya se lee la solución: y = 2 y, de x + 2y = 5, x = 1.", espera=3)
        self.limpiar(titulo)

        # Visual: la cadena completa conserva la solución
        titulo = self.cambiar_encabezado(titulo, "Una cadena de sistemas equivalentes")
        cadena = MathTex(
            r"\left[\begin{array}{cc|c} 2 & 4 & 10 \\ 3 & -1 & 1 \end{array}\right] \sim"
            r"\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & -1 & 1 \end{array}\right] \sim"
            r"\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -7 & -14 \end{array}\right] \sim"
            r"\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 2 \end{array}\right]",
            font_size=40,
        ).shift(UP * 0.8)
        ajustar_al_encuadre(cadena)
        comprobacion = MathTex(
            r"(x, y) = (1, 2):\quad 2 + 8 = 10,\ \ 3 - 2 = 1;\quad 1 + 4 = 5;\quad -7\cdot 2 = -14;\quad 2 = 2\ \ \checkmark",
            font_size=36,
            color=COLOR_SOLUCION,
        ).next_to(cadena, DOWN, buff=0.7)
        ajustar_al_encuadre(comprobacion)
        self.decir("Cada operación produce un sistema equivalente: una cadena de matrices distintas, con las mismas soluciones.")
        self.play(Write(cadena), run_time=3)
        self.decir("Todas las matrices de la cadena tienen la misma solución: uno, dos.")
        self.play(FadeIn(comprobacion))
        self.decir("Por eso entre ellas se escribe el símbolo de equivalencia, no un igual.")
        self.pie("El símbolo ~ une matrices de sistemas equivalentes: las matrices cambian, las soluciones no.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Operar solo los coeficientes y olvidar la columna de $\mathbf{b}$.", font_size=36),
            Tex(r"En $R_2 \leftarrow R_2 - 3R_1$ cambiar también $R_1$: la fila de origen no se toca.", font_size=36),
            Tex(r"Multiplicar por $0$, o sumar a una fila un múltiplo de sí misma.", font_size=36),
            Tex(r"Escribir $=$ entre las matrices: son distintas; se escribe $\sim$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        ajustar_al_encuadre(errores)
        self.decir("Errores frecuentes: operar solo los coeficientes y olvidar la columna de be; cambiar también la fila de origen; multiplicar por cero, o sumar a una fila un múltiplo de sí misma; y escribir igual entre matrices que son distintas.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N1-01",
            VGroup(
                MathTex(r"M = \left[\begin{array}{cc|c} 2 & -1 & 3 \\ 1 & 4 & 6 \end{array}\right]", font_size=48),
                Tex(r"Aplica a $M$ cada operación por separado:", font_size=36),
                MathTex(r"\text{a) } R_1 \leftrightarrow R_2 \qquad \text{b) } R_2 \leftarrow 3R_2 \qquad \text{c) } R_2 \leftarrow R_2 - 2R_1", font_size=40),
                Tex(r"Comprueba que $(2, 1)$ es solución de los cuatro sistemas.", font_size=36),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Intercambiar dos filas; multiplicar una fila por k distinto de 0; sumar a una fila k veces otra.",
                "Se aplican a la fila entera, columna de b incluida; solo cambia la fila destino.",
                "Cada una da un sistema equivalente: mismas soluciones.",
            ],
            "por qué conservan las soluciones (demostración).",
            voz="En resumen: las operaciones elementales son tres: intercambiar dos filas, multiplicar una fila por un número distinto de cero, y sumar a una fila un múltiplo de otra. Se aplican a la fila entera, columna de be incluida, y solo cambia la fila destino. Cada una da un sistema equivalente, con las mismas soluciones. Siguiente: por qué conservan las soluciones.",
        )


class CadaOperacionSeDeshace(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 24 · Parte 2", "Cada operación se puede deshacer")
        titulo = self.encabezado("Si dos igualdades son ciertas, su combinación también")
        e1 = MathTex(r"x + 2y = 5", font_size=42)
        e2 = MathTex(r"3x - y = 1", font_size=42)
        combinada = MathTex(r"(3x - y) - 3(x + 2y) = 1 - 3\cdot 5", font_size=42, color=COLOR_OPERACION)
        bloque = VGroup(e1, e2, combinada).arrange(DOWN, buff=0.45).shift(LEFT * 2.5 + UP * 0.6)
        en_s = VGroup(
            MathTex(r"1 + 4 = 5\ \checkmark", font_size=38),
            MathTex(r"3 - 2 = 1\ \checkmark", font_size=38),
            MathTex(r"1 - 15 = -14\ \checkmark", font_size=38, color=COLOR_OPERACION),
        )
        for a, b in zip(en_s, bloque):
            a.next_to(b, RIGHT, buff=1.2).set_x(3.6)
        cabecera = Text("en (x, y) = (1, 2):", font_size=TAM_NOTA, color=COLOR_SOLUCION).next_to(en_s[0], UP, buff=0.4)
        self.decir("Si dos igualdades son ciertas, cualquier combinación de ellas también lo es.")
        self.play(Write(e1), Write(e2))
        self.play(FadeIn(cabecera), FadeIn(en_s[0]), FadeIn(en_s[1]))
        self.decir("Por eso, la solución del sistema viejo cumple las ecuaciones nuevas: se multiplican y se suman igualdades ciertas.")
        self.play(Write(combinada))
        self.play(FadeIn(en_s[2]))
        self.decir("Falta la otra mitad: que lo nuevo no tenga soluciones de más.")
        self.pie("Toda solución de las ecuaciones viejas cumple las nuevas: se multiplican y se suman igualdades ciertas.\nFalta la otra mitad: que las nuevas no tengan soluciones de más.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cada operación tiene una inversa del mismo tipo")
        celdas = [
            Text("operación", font_size=TAM_NOTA, color=COLOR_SECUNDARIO),
            Text("la deshace", font_size=TAM_NOTA, color=COLOR_SECUNDARIO),
            MathTex(r"R_i \leftrightarrow R_j", color=COLOR_OPERACION),
            MathTex(r"R_i \leftrightarrow R_j", color=COLOR_OPERACION),
            MathTex(r"R_i \leftarrow k\,R_i \ \ (k \neq 0)", color=COLOR_OPERACION),
            MathTex(r"R_i \leftarrow \tfrac{1}{k}\,R_i", color=COLOR_OPERACION),
            MathTex(r"R_i \leftarrow R_i + k\,R_j", color=COLOR_OPERACION),
            MathTex(r"R_i \leftarrow R_i - k\,R_j", color=COLOR_OPERACION),
        ]
        tabla = VGroup(*celdas).arrange_in_grid(rows=4, cols=2, buff=(1.6, 0.45)).shift(UP * 0.4)
        self.decir("Cada operación se deshace con otra del mismo tipo. Un intercambio se deshace repitiéndolo. Multiplicar por ka se deshace multiplicando por uno entre ka. Y sumar ka veces una fila se deshace restándolas.")
        for k in range(0, 8, 2):
            self.play(FadeIn(celdas[k]), FadeIn(celdas[k + 1]))
            self.wait(1)
        self.decir("La inversa existe gracias a las condiciones: uno entre ka necesita ka distinto de cero, y la fila que se suma tiene que ser otra.")
        self.pie("La inversa existe gracias a las condiciones: 1/k necesita k distinto de 0, y al sumar a la fila i un múltiplo de la fila j,\nla fila j no cambia (si fueran la misma fila, con k = -1 se borraría y no habría vuelta atrás).", espera=6)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Ida y vuelta")
        m = matriz_gauss([[1, 2, 5], [3, -1, 1]], pivotes=[(0, 0)]).move_to(LEFT * 2 + UP * 0.8)
        self.decir("Ida y vuelta.")
        self.play(FadeIn(m))
        self.decir("Restamos a la fila dos tres veces la fila uno.")
        m = self.operar_filas(m, ("sumar", 1, 0, -3))
        self.decir("Ahora la operación inversa: sumamos lo que restamos.")
        self.pie("Ahora la operación inversa: sumar lo que se restó.")
        m = self.operar_filas(m, ("sumar", 1, 0, 3))
        self.decir("Volvemos exactamente a la matriz de partida: no se perdió información.")
        self.pie("Volvemos exactamente a la matriz de partida: no se perdió información.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Demostración: S y S' tienen las mismas soluciones")
        pasos = VGroup(
            Tex(r"Sea $S'$ el sistema que resulta de aplicar a $S$ una operación elemental.", font_size=34),
            parrafo(r"(1) Si $\mathbf{s}$ cumple $S$, cumple $S'$: cada ecuación de $S'$ es una de $S$,",
                    r"$k$ veces una de $S$ o $E_i + kE_j$, y las igualdades ciertas se pueden",
                    r"multiplicar y sumar. Así, $\mathrm{Sol}(S) \subseteq \mathrm{Sol}(S')$.", sangria=0.5),
            parrafo(r"(2) $S$ se obtiene de $S'$ con la operación inversa, que también es elemental.",
                    r"Por (1) aplicado a $S'$: \ $\mathrm{Sol}(S') \subseteq \mathrm{Sol}(S)$.", sangria=0.5),
            parrafo(r"(3) Las dos inclusiones dan $\mathrm{Sol}(S) = \mathrm{Sol}(S')$. Con varias operaciones",
                    r"seguidas, se repite el argumento en cada paso. \ $\blacksquare$", sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(pasos)
        self.decir("La demostración tiene dos mitades. Primera: toda solución del sistema viejo cumple el nuevo. Segunda: toda solución del nuevo vuelve al viejo con la operación inversa. Las dos juntas dan que los conjuntos de soluciones son iguales.")
        for p in pasos:
            self.play(FadeIn(p))
            self.wait(3)
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Sin inversa, solo vale la mitad")
        ejemplo = MathTex(
            r"\begin{cases} x + 2y = 5 \\ 3x - y = 1 \end{cases}",
            r"\ \xrightarrow{\ R_2 \leftarrow 0\cdot R_2\ }\ ",
            r"\begin{cases} x + 2y = 5 \\ 0 = 0 \end{cases}",
            font_size=44,
        ).shift(UP * 0.8)
        ejemplo[1].set_color(COLOR_ERROR)
        explicacion = Tex(
            r"La inclusión (1) se cumple: $(1, 2)$ sigue siendo solución.\\"
            r"Pero $(5, 0)$ es solución nueva: la (2) falla porque $0\cdot R_2$ no se deshace.",
            font_size=34,
        ).next_to(ejemplo, DOWN, buff=0.7)
        self.decir("Sin operación inversa, solo vale la primera mitad.")
        self.play(Write(ejemplo))
        self.decir("Con cero por la fila dos, el sistema gana soluciones que no tenía.")
        self.play(FadeIn(explicacion))
        self.wait(5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Probar solo la inclusión (1): podrían aparecer soluciones que no lo eran.", font_size=36),
            Tex(r"Usar operaciones sin inversa ($0\cdot R_i$, \ $R_i \leftarrow R_i - R_i$).", font_size=36),
            Tex(r"Creer que ``equivalente'' significa ``igual'': las matrices cambian.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: probar solo la primera mitad, porque podrían aparecer soluciones que no lo eran; usar operaciones sin inversa, como multiplicar por cero o restarle a una fila ella misma; y creer que equivalente significa igual: las matrices cambian.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N2-01",
            VGroup(
                Tex(r"$N = \left[\begin{array}{cc|c} 1 & 3 & 2 \\ 0 & -5 & 1 \end{array}\right]$ se obtuvo de una matriz $M$ con $R_2 \leftarrow R_2 - 2R_1$.", font_size=38),
                Tex(r"a) Deshaz la operación para encontrar $M$. \quad b) Resuelve $N$ y comprueba en $M$.", font_size=38),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Toda solución del sistema viejo cumple el nuevo (combinar igualdades ciertas).",
                "Cada operación elemental se deshace con otra elemental: el recíproco también vale.",
                "Por eso conservan el conjunto solución; multiplicar por 0 no tiene inversa y no está permitido.",
            ],
            "Lección 25 — forma escalonada y pivotes.",
            voz="En resumen: toda solución del sistema viejo cumple el nuevo, porque se combinan igualdades ciertas. Cada operación elemental se deshace con otra elemental, así que el recíproco también vale. Por eso conservan el conjunto solución. Multiplicar por cero no tiene inversa y no está permitido. Siguiente: lección veinticinco, forma escalonada y pivotes.",
        )
