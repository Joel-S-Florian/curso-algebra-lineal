"""Lección 28 — Sistemas sin solución y con infinitas soluciones.

Escenas (un video cada una):
    FilaContradictoria, VariablesLibresYSolucionParametrica

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l28_sin_solucion_e_infinitas.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz_gauss, parrafo, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def con_parametro(*partes, font_size=42) -> MathTex:
    """MathTex con los parámetros (las partes "t" y "s") en verde."""
    tex = MathTex(*partes, font_size=font_size)
    for parte, trozo in zip(partes, tex):
        if parte in ("t", "s"):
            trozo.set_color(COLOR_LIBRE)
    return tex


def eliminar(escena, b3):
    """Sistema común de las dos escenas; solo cambia el último término independiente."""
    s = sistema_con_llave(("x + y + z", "=", "2"), ("x + 2y + 3z", "=", "5"), ("2x + 3y + 4z", "=", str(b3)), font_size=32, colores=False)
    s.move_to(LEFT * 5.4 + UP * 0.6)
    m = matriz_gauss([[1, 1, 1, 2], [1, 2, 3, 5], [2, 3, 4, b3]], pivotes=[(0, 0)], escala=0.85).move_to(LEFT * 1.3 + UP * 0.6)
    historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 5.1 + UP * 2.2)
    escena.play(Write(s), FadeIn(m), FadeIn(historial))
    m = escena.operar_filas(m, ("sumar", 1, 0, -1), historial=historial)
    m = escena.operar_filas(m, ("sumar", 2, 0, -2), historial=historial, pivotes=[(0, 0), (1, 1)])
    m = escena.operar_filas(m, ("sumar", 2, 1, -1), historial=historial)
    return s, m, historial


class FilaContradictoria(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 28 · Parte 1", "Cuando aparece 0 = c")
        titulo = self.encabezado("Eliminamos como siempre…")
        self.decir("Tres ecuaciones con tres incógnitas. Eliminamos como siempre: a la fila dos le restamos la uno, a la tres, dos veces la uno, y después, a la tres le restamos la dos.")
        s, m, historial = eliminar(self, 8)
        self.decir("La última fila es cero, cero, cero, uno.")
        self.play(m.get_rows()[2].animate.set_color(COLOR_ERROR))
        lectura = MathTex(r"0x + 0y + 0z = 1", font_size=42, color=COLOR_ERROR).next_to(m, DOWN, buff=0.5)
        self.decir("Dice cero igual a uno. Ninguna terna la cumple: el sistema no tiene solución. Es incompatible.")
        self.play(Write(lectura))
        self.pie("Ninguna terna (x, y, z) cumple 0 = 1. El sistema no tiene solución: es incompatible (SI).", color=COLOR_ERROR, espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Por qué podemos concluir")
        pasos = VGroup(
            Tex(r"(1) Las operaciones elementales conservan el conjunto solución (L24).", font_size=36),
            Tex(r"(2) El sistema final contiene $0 = 1$: su conjunto solución es vacío.", font_size=36),
            Tex(r"(3) Luego el original tampoco tiene solución.", font_size=36),
            parrafo(r"Comprobación directa: $E_3 - E_1 - E_2$ da $0x + 0y + 0z = 8 - 2 - 5 = 1$.",
                    r"Si una terna cumpliera las tres ecuaciones, cumpliría también $0 = 1$.", font_size=36, color=COLOR_OPERACION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(pasos)
        self.decir("¿Por qué podemos concluir eso? Las operaciones elementales conservan el conjunto solución, y el sistema final no tiene ninguna solución. Luego el original tampoco. Además, la tercera ecuación menos las otras dos da directamente cero igual a uno.")
        for p in pasos:
            self.play(FadeIn(p))
            self.wait(2.5)
        self.decir("Geométricamente: tres planos sin ningún punto común a los tres.")
        self.pie("Geométricamente: tres planos sin ningún punto común a los tres (L09).", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La regla")
        regla = MathTex(r"\left[\begin{array}{ccc|c} 0 & \cdots & 0 & c \end{array}\right],\quad c \neq 0", font_size=56, color=COLOR_ERROR).shift(UP * 1.2)
        explicacion = parrafo(
            r"Si una forma escalonada de $[A \mid \mathbf{b}]$ tiene una fila así",
            r"(un pivote en la columna de $\mathbf{b}$), el sistema es \textbf{incompatible}.",
            r"Basta con un $c$ no nulo cualquiera: $0 = -3$ también es imposible.",
            font_size=36,
        ).next_to(regla, DOWN, buff=0.7)
        self.decir("La regla: si una forma escalonada tiene una fila de ceros con un número distinto de cero en la columna de be, es decir, un pivote en la columna de be…")
        self.play(Write(regla))
        self.decir("…el sistema es incompatible. Vale cualquier número distinto de cero.")
        self.play(FadeIn(explicacion))
        self.decir("Si ese número es cero, la fila es cero igual a cero: redundante. Y si no aparece ninguna fila así, hay solución, como veremos en el siguiente video.")
        self.pie("Si c = 0 la fila es 0 = 0, redundante (L27). Y si no aparece ninguna fila así, hay solución: siguiente video.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Seguir sustituyendo hacia atrás tras ver $0 = 1$: no hay nada que despejar.", font_size=36),
            Tex(r"Leer $[\,0 \ \ 0 \ \ 0 \mid 1\,]$ como $x = y = z = 0$.", font_size=36),
            Tex(r"Confundir $[\,0 \ \ 0 \ \ 0 \mid 0\,]$ (redundante) con $[\,0 \ \ 0 \ \ 0 \mid c\,]$, $c \neq 0$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: seguir sustituyendo hacia atrás después de ver cero igual a uno; leer esa fila como equis, ye y zeta iguales a cero; y confundir una fila nula entera, que es redundante, con una que termina en un número distinto de cero.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N2-06",
            VGroup(
                Text("Aplica Gauss y clasifica. Encuentra la combinación de ecuaciones que da 0 = c.", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y - z = 1 \\ 2x + 3y + z = 4 \\ 3x + 5y = 6 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Una fila [0 … 0 | c] con c distinto de 0 es la ecuación imposible 0 = c.",
                "Como las operaciones conservan las soluciones, el sistema original es incompatible.",
                "Un pivote en la columna de b significa: sin solución.",
            ],
            "variables libres y solución paramétrica.",
            voz="En resumen: una fila de ceros que termina en un número ce distinto de cero es la ecuación imposible cero igual a ce. Como las operaciones conservan las soluciones, el sistema original es incompatible. Un pivote en la columna de be significa: sin solución. Siguiente: variables libres y solución paramétrica.",
        )


class VariablesLibresYSolucionParametrica(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 28 · Parte 2", "Variables libres y solución paramétrica")
        titulo = self.encabezado("El mismo sistema, con un 7 en lugar del 8")
        self.decir("El mismo sistema, pero con un siete en lugar del ocho.")
        s, m, historial = eliminar(self, 7)
        self.decir("Ahora la última fila es entera de ceros: redundante. No hay contradicción, pero quedan dos pivotes para tres incógnitas.")
        self.pie("Ahora la última fila es [0 0 0 | 0]: redundante. No hay contradicción, pero quedan 2 pivotes para 3 incógnitas.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Variables pivote y variables libres")
        m = matriz_gauss([[1, 1, 1, 2], [0, 1, 2, 3], [0, 0, 0, 0]], pivotes=[(0, 0), (1, 1)]).move_to(LEFT * 3.5 + UP * 0.6)
        cabeceras = VGroup(*[MathTex(v, font_size=40).next_to(c, UP, buff=0.45) for v, c in zip("xyz", m.get_columns())])
        cabeceras.align_to(cabeceras[0], DOWN)
        cabeceras[0].set_color(COLOR_PIVOTE)
        cabeceras[1].set_color(COLOR_PIVOTE)
        cabeceras[2].set_color(COLOR_LIBRE)
        self.decir("Las columnas de equis y de ye tienen pivote.")
        self.play(FadeIn(m), FadeIn(cabeceras))
        self.play(Create(escalera(m, [(0, 0), (1, 1)])))
        definicion = parrafo(
            r"La columna de $z$ no tiene pivote:",
            r"$z$ es una \textbf{variable libre}.",
            r"Puede valer cualquier número; la",
            r"llamamos $t$ (un \textbf{parámetro}).",
            font_size=36,
        ).next_to(m, RIGHT, buff=1)
        definicion[1].set_color(COLOR_LIBRE)
        self.decir("La columna de zeta no tiene pivote: zeta es una variable libre. Puede valer cualquier número; la llamamos te, un parámetro.")
        self.play(FadeIn(definicion))
        self.wait(4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Sustitución hacia atrás con parámetro")
        m = matriz_gauss([[1, 1, 1, 2], [0, 1, 2, 3], [0, 0, 0, 0]], pivotes=[(0, 0), (1, 1)]).move_to(LEFT * 3.8 + UP * 0.6)
        self.decir("Sustitución hacia atrás, con el parámetro.")
        self.play(FadeIn(m))
        pasos = VGroup(
            con_parametro(r"z = ", "t"),
            con_parametro(r"y + 2", "t", r" = 3 \;\Rightarrow\; y = 3 - 2", "t"),
            con_parametro(r"x + (3 - 2", "t", r") + ", "t", r" = 2 \;\Rightarrow\; x = -1 + ", "t"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(m, RIGHT, buff=0.8)
        ajustar_al_encuadre(pasos)
        self.decir("Zeta es te. De la segunda fila, ye más dos te igual a tres: ye vale tres menos dos te. Y de la primera, equis vale menos uno más te.")
        for i, p in zip((None, 1, 0), pasos):
            marco = SurroundingRectangle(m.get_rows()[i], color=COLOR_PIVOTE) if i is not None else None
            self.play(*([Create(marco)] if marco else []), Write(p))
            self.wait(1.5)
            if marco:
                self.play(FadeOut(marco))
        solucion = MathTex(r"(x, y, z) = (-1 + t,\ 3 - 2t,\ t) = (-1, 3, 0) + t\,(1, -2, 1),\quad t \in \mathbb{R}", font_size=38, color=COLOR_SOLUCION)
        solucion.next_to(VGroup(m, pasos), DOWN, buff=0.7)
        ajustar_al_encuadre(solucion)
        self.decir("Hay una solución para cada valor de te: infinitas soluciones. Es la recta en que se cortan los tres planos.")
        self.play(Write(solucion))
        self.pie("Infinitas soluciones (SCI), una por cada valor de t: es la recta en que se cortan los tres planos (L09).", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificación para TODO t")
        verif = VGroup(
            MathTex(r"E_1:\ (-1 + t) + (3 - 2t) + t = 2\ \checkmark", font_size=40),
            MathTex(r"E_2:\ (-1 + t) + 2(3 - 2t) + 3t = 5\ \checkmark", font_size=40),
            MathTex(r"E_3:\ 2(-1 + t) + 3(3 - 2t) + 4t = 7\ \checkmark", font_size=40),
            MathTex(r"t = 0:\ (-1, 3, 0) \qquad t = 1:\ (0, 1, 1)", font_size=40, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.7)
        verif[:3].set_color(COLOR_SOLUCION)
        self.decir("Para verificar, sustituimos con te general: los términos con te se cancelan en cada ecuación. Por ejemplo, con te igual a cero sale menos uno, tres, cero; y con te igual a uno, cero, uno, uno.")
        for v in verif:
            self.play(Write(v))
            self.wait(1.2)
        self.decir("Por eso valen todos los te. Y la cuenta: tres incógnitas menos dos pivotes, una variable libre.")
        self.pie("Los términos con t se cancelan en cada ecuación: por eso valen todos los t.\nCuenta: 3 incógnitas - 2 pivotes = 1 variable libre.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Caso alternativo: dos variables libres")
        caso = VGroup(
            MathTex(r"\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \end{array}\right]", font_size=48),
            con_parametro(r"y = ", "s", r",\quad z = ", "t", r",\quad x = 3 - 2", "s", " + ", "t", r",\qquad ", "s", ", ", "t", r" \in \mathbb{R}"),
        ).arrange(DOWN, buff=0.6).shift(UP * 0.6)
        self.decir("Un caso con dos variables libres: una sola ecuación, equis más dos ye menos zeta igual a tres.")
        self.play(FadeIn(caso[0]))
        self.decir("Ye y zeta son libres: ese y te. Equis vale tres menos dos ese más te. Tres incógnitas menos un pivote, dos libres: es un plano, con dos parámetros.")
        self.play(Write(caso[1]))
        self.pie("Una sola ecuación x + 2y - z = 3: 3 incógnitas - 1 pivote = 2 libres. Es un plano, con dos parámetros.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Dar a la libre un valor ($z = 0$) y decir que la solución es única.", font_size=36),
            Tex(r"Tomar como libre una variable pivote: libres son las columnas \textbf{sin} pivote.", font_size=36),
            Tex(r"Olvidar que $x$ e $y$ dependen de $t$, o no escribir $t \in \mathbb{R}$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: darle a la libre un valor, como zeta igual a cero, y decir que la solución es única; tomar como libre una variable pivote, cuando libres son las columnas sin pivote; y olvidar que equis e ye dependen de te.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N3-03",
            VGroup(
                Text("Resuelve por Gauss, da la solución en forma paramétrica y verifícala para todo t:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y - z = 1 \\ 2x + 3y + z = 4 \\ 3x + 5y = 5 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Columnas sin pivote: variables libres; reciben parámetros (t, s, …).",
                "Las variables pivote se despejan hacia atrás en función de los parámetros.",
                "Sin fila [0 … 0 | c]: con libres, infinitas soluciones (SCI); sin libres, una (SCD).",
            ],
            "Lección 29 — sistemas con parámetros.",
            voz="En resumen: las columnas sin pivote dan las variables libres, que reciben parámetros como te y ese. Las variables pivote se despejan hacia atrás en función de los parámetros. Y si no hay una fila imposible: con variables libres, infinitas soluciones; sin libres, una sola. Siguiente: lección veintinueve, sistemas con parámetros.",
        )
