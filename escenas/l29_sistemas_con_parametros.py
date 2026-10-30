"""Lección 29 — Sistemas con parámetros.

Escenas (un video cada una):
    GaussConParametro, DiscutirPorCasos

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l29_sistemas_con_parametros.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz_gauss, parrafo, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def caso(condicion: str, resultado: str, color) -> VGroup:
    """Fila de una discusión: condición sobre el parámetro → conclusión."""
    return VGroup(
        MathTex(condicion, font_size=40, color=COLOR_LIBRE),
        MathTex(r"\Rightarrow", font_size=40),
        MathTex(resultado, font_size=40, color=color),
    ).arrange(RIGHT, buff=0.4)


class GaussConParametro(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 29 · Parte 1", "Gauss con un parámetro")
        titulo = self.encabezado("Un coeficiente desconocido: a")
        s = sistema_con_llave(("x + y", "=", "1"), ("2x + ay", "=", "3"), font_size=42, colores=False).move_to(LEFT * 4.6 + UP * 0.8)
        m = matriz_gauss([[1, 1, 1], [2, "a", 3]], pivotes=[(0, 0)]).move_to(LEFT * 0.8 + UP * 0.8)
        m.get_rows()[1][1].set_color(COLOR_LIBRE)
        self.decir("Equis más ye igual a uno, y dos equis más a ye igual a tres. Aquí a es un parámetro: un número fijo, pero desconocido. Hay que responder para cada valor de a.")
        self.play(Write(s), FadeIn(m))
        self.pie("a es un parámetro: un número fijo pero desconocido. Hay que responder para cada valor de a.", espera=3)
        self.decir("Eliminamos como siempre: a la fila dos le restamos dos veces la fila uno. Queda a menos dos en el lugar del pivote.")
        m = self.operar_filas(m, ("sumar", 1, 0, -2), nueva=[0, "a-2", 1])
        marco = SurroundingRectangle(m.get_rows()[1][1], color=COLOR_PIVOTE)
        self.decir("¿Es a menos dos un pivote? Solo si no vale cero. Si a es dos, ese hueco vale cero. Así que no se puede despejar ye dividiendo entre a menos dos sin separar antes ese caso.")
        self.play(Create(marco))
        self.pie("¿Es a - 2 un pivote? Solo si a - 2 es distinto de 0. Si a = 2, ese hueco vale 0.\nNo se puede despejar y = 1/(a - 2) sin antes separar ese caso.", espera=5)
        self.play(FadeOut(marco))
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Discutir por casos")
        m = matriz_gauss([[1, 1, 1], [0, "a-2", 1]], pivotes=[(0, 0)]).move_to(UP * 1.9)
        self.decir("Discutimos por casos.")
        self.play(FadeIn(m))
        c1 = VGroup(
            caso(r"a \neq 2", r"a - 2 \text{ es pivote: SCD}", COLOR_SOLUCION),
            MathTex(r"y = \frac{1}{a - 2},\qquad x = 1 - y = \frac{a - 3}{a - 2}", font_size=40, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.3)
        c2 = VGroup(
            caso(r"a = 2", r"\left[\begin{array}{cc|c} 1 & 1 & 1 \\ 0 & 0 & 1 \end{array}\right]:\ 0 = 1,\ \text{SI}", COLOR_ERROR),
        )
        casos = VGroup(c1, c2).arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(m, DOWN, buff=0.6)
        ajustar_al_encuadre(casos)
        self.decir("Si a es distinto de dos, a menos dos es un pivote: solución única. Ye vale uno entre a menos dos, y equis, a menos tres entre a menos dos.")
        self.play(FadeIn(c1))
        self.wait(3)
        self.decir("Si a vale dos, sustituimos en toda la matriz: la última fila dice cero igual a uno. Sin solución.")
        self.play(FadeIn(c2))
        self.wait(2)
        self.decir("En el caso especial se sustituye el valor en toda la matriz, también en be, y se mira qué fila queda.")
        self.pie("En el caso a = 2 se sustituye el valor en TODA la matriz (también en b) y se mira qué fila queda.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificación")
        verif = VGroup(
            MathTex(r"x + y = \frac{a - 3}{a - 2} + \frac{1}{a - 2} = \frac{a - 2}{a - 2} = 1\ \checkmark", font_size=40),
            MathTex(r"2x + ay = \frac{2a - 6 + a}{a - 2} = \frac{3(a - 2)}{a - 2} = 3\ \checkmark", font_size=40),
            MathTex(r"a = 3:\ (x, y) = (0, 1):\quad 0 + 1 = 1,\ \ 0 + 3 = 3\ \checkmark", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        verif.set_color(COLOR_SOLUCION)
        self.decir("Verificamos: al sumar, a menos dos entre a menos dos es uno; y la segunda ecuación da tres. Por ejemplo, con a igual a tres, la solución es cero, uno, y cumple las dos ecuaciones.")
        for v in verif:
            self.play(Write(v))
            self.wait(1.5)
        self.decir("Simplificar a menos dos entre a menos dos es legítimo aquí, porque estamos en el caso a distinto de dos.")
        self.pie("Simplificar (a - 2)/(a - 2) = 1 es legítimo aquí porque estamos en el caso a distinto de 2.\n"
                 "Con a = 2: x + y = 1 y 2x + 2y = 3 son rectas paralelas (L08).", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué operaciones son seguras con parámetros")
        reglas = VGroup(
            parrafo(r"\textbf{Sumar} a una fila $k$ veces otra: siempre legal, aunque $k$ dependa",
                    r"de $a$ (si $k = 0$, la fila no cambia: también se deshace).", font_size=36, sangria=0.4),
            parrafo(r"\textbf{Multiplicar} una fila por $a - 2$, o \textbf{dividir} por $a - 2$:",
                    r"solo si $a \neq 2$. Si no, hay que separar el caso $a = 2$.", font_size=36, sangria=0.4, color=COLOR_ERROR),
            Tex(r"\textbf{Intercambiar} filas: siempre legal.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        self.decir("¿Qué operaciones son seguras con parámetros? Sumar a una fila un múltiplo de otra, siempre, aunque el múltiplo dependa de a. Intercambiar filas, también. Pero multiplicar o dividir una fila por a menos dos, solo si a es distinto de dos.")
        for r in reglas:
            self.play(FadeIn(r))
            self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Escribir $y = \frac{1}{a - 2}$ sin decir ``si $a \neq 2$''.", font_size=36),
            Tex(r"Hacer $R_2 \leftarrow (a - 2)R_2$ o dividir por $a$ sin discutir.", font_size=36),
            Tex(r"Estudiar el caso especial sustituyendo solo en $A$ y no en $\mathbf{b}$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: escribir ye igual a uno entre a menos dos sin decir que a es distinto de dos; multiplicar o dividir por una expresión sin discutir; y estudiar el caso especial sustituyendo solo en a y no en be.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N4-03",
            VGroup(
                Text("Discute según el valor de a y resuelve en cada caso:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y = 3 \\ 2x + ay = 6 \end{cases}", font_size=48),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Con parámetros se elimina igual, pero cada candidato a pivote puede valer 0.",
                "Antes de dividir por una expresión, se separa el caso en que vale 0.",
                "En cada caso especial se sustituye el valor en toda la matriz y se clasifica.",
            ],
            "discutir por casos un sistema 3 × 3.",
            voz="En resumen: con parámetros se elimina igual, pero cada candidato a pivote puede valer cero. Antes de dividir entre una expresión, se separa el caso en que vale cero. Y en cada caso especial se sustituye el valor en toda la matriz, y se clasifica. Siguiente: discutir por casos un sistema de tres por tres.",
        )


class DiscutirPorCasos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 29 · Parte 2", "Discutir por casos")
        titulo = self.encabezado("Un sistema 3 × 3 con parámetro a")
        m = matriz_gauss([[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, "a^2+1", "a+1"]], pivotes=[(0, 0)]).move_to(LEFT * 2.6 + UP * 0.9)
        self.decir("Un sistema de tres por tres con un parámetro a.")
        self.play(FadeIn(m))
        self.decir("Eliminamos hasta que el parámetro quede en el último candidato a pivote.")
        m = self.operar_filas(m, ("sumar", 1, 0, -1), pivotes=[(0, 0), (1, 1)])
        m = self.operar_filas(m, ("sumar", 2, 0, -1), nueva=[0, 1, "a^2", "a"])
        m = self.operar_filas(m, ("sumar", 2, 1, -1), nueva=[0, 0, "a^2-1", "a-1"])
        marco = SurroundingRectangle(m.get_rows()[2][2], color=COLOR_PIVOTE)
        factor = MathTex(r"a^2 - 1 = (a - 1)(a + 1)", font_size=42, color=COLOR_LIBRE).next_to(m, RIGHT, buff=0.8)
        self.decir("Ese candidato es a al cuadrado menos uno, que es a menos uno por a más uno.")
        self.play(Create(marco), Write(factor))
        self.decir("Se anula en a igual a uno y en a igual a menos uno: son los valores que hay que estudiar aparte.")
        self.pie("El candidato a pivote se anula en a = 1 y en a = -1: son los valores que hay que separar.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Los tres casos")
        m = matriz_gauss([[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, "a^2-1", "a-1"]], pivotes=[(0, 0), (1, 1)], escala=0.8).move_to(UP * 1.8)
        self.play(FadeIn(m))
        casos = VGroup(
            VGroup(
                caso(r"a \neq \pm 1", r"\text{tres pivotes: SCD}", COLOR_SOLUCION),
                MathTex(r"z = \frac{a - 1}{a^2 - 1} = \frac{1}{a + 1},\quad y = 1 - z = \frac{a}{a + 1},\quad x = 1 - y - z = 0", font_size=36, color=COLOR_SOLUCION),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            caso(r"a = 1", r"[\,0 \ \ 0 \ \ 0 \mid 0\,]:\ \text{SCI},\ \ (x, y, z) = (0,\ 1 - t,\ t)", COLOR_LIBRE),
            caso(r"a = -1", r"[\,0 \ \ 0 \ \ 0 \mid -2\,]:\ 0 = -2,\ \text{SI}", COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(m, DOWN, buff=0.5)
        ajustar_al_encuadre(casos)
        self.decir("Si a es distinto de uno y de menos uno, hay tres pivotes: una solución, con zeta igual a uno entre a más uno, ye igual a a entre a más uno, y equis igual a cero. Si a vale uno, la última fila se anula entera: infinitas soluciones. Y si a vale menos uno, queda cero igual a menos dos: ninguna.")
        for c in casos:
            self.play(FadeIn(c))
            self.wait(3)
        self.decir("Simplificar entre a menos uno es correcto en el primer caso, porque ahí a es distinto de uno.")
        self.pie("Simplificar entre a - 1 es correcto en el primer caso, porque ahí a es distinto de 1.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La trampa: simplificar antes de discutir")
        trampa = VGroup(
            MathTex(r"(a^2 - 1)\,z = a - 1 \quad\Longrightarrow\quad z = \frac{1}{a + 1}\ \ ???", font_size=44, color=COLOR_ERROR),
            parrafo(r"Así parece que solo $a = -1$ da problemas, y se pierde el caso $a = 1$,",
                    r"que tiene \textbf{infinitas} soluciones. Dividir entre $a - 1$ exige $a \neq 1$.", font_size=36),
        ).arrange(DOWN, buff=0.7).next_to(titulo, DOWN, buff=0.9)
        self.decir("La trampa: simplificar antes de discutir.")
        self.play(Write(trampa[0]))
        self.decir("Así parece que solo a igual a menos uno da problemas, y se pierde el caso a igual a uno, que tiene infinitas soluciones.")
        self.play(FadeIn(trampa[1]))
        self.wait(5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificación")
        s = sistema_con_llave(("x + y + z", "=", "1"), ("x + 2y + 2z", "=", "2"), ("x + 2y + (a^2 + 1)z", "=", "a + 1"), font_size=36, colores=False)
        s.next_to(titulo, DOWN, buff=0.5)
        verif = VGroup(
            MathTex(r"a \neq \pm 1:\ \ E_3 = 2\cdot\tfrac{a}{a + 1} + (a^2 + 1)\tfrac{1}{a + 1} = \tfrac{(a + 1)^2}{a + 1} = a + 1\ \checkmark", font_size=36),
            MathTex(r"a = 0:\ (0, 0, 1):\quad 1 = 1,\ \ 2 = 2,\ \ 1 = 1\ \checkmark", font_size=36),
            MathTex(r"a = 1:\ (0, 1 - t, t):\quad E_3 = 2(1 - t) + 2t = 2 = a + 1\ \checkmark", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(s, DOWN, buff=0.5)
        verif.set_color(COLOR_SOLUCION)
        ajustar_al_encuadre(VGroup(s, verif))
        self.decir("Comprobamos cada caso en el sistema original.")
        self.play(FadeIn(s))
        self.decir("Con a distinto de más y menos uno, la tercera ecuación da a más uno. Con a igual a cero, la solución es cero, cero, uno. Y con a igual a uno, cero, uno menos te, te, cumple la tercera para todo te.")
        for v in verif:
            self.play(Write(v))
            self.wait(1.5)
        self.pie("(E₁ y E₂ se cumplen siempre: x = 0 e y + z = 1). Se comprueba cada caso por separado, en el sistema original.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            Tex(r"Simplificar una fracción con parámetro antes de separar los casos.", font_size=36),
            Tex(r"Olvidar un valor crítico: hay que hallar \textbf{todas} las raíces del pivote.", font_size=36),
            Tex(r"Clasificar el caso especial sin sustituir el valor en la columna de $\mathbf{b}$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Errores frecuentes: simplificar una fracción con parámetro antes de separar los casos; olvidar un valor crítico, cuando hay que hallar todas las raíces del pivote; y clasificar el caso especial sin sustituir el valor en la columna de be.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N4-04",
            VGroup(
                Text("Discute según el valor de a (SCD, SCI o SI) y resuelve cuando haya solución:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + y + z = 1 \\ x + 2y + 2z = 3 \\ x + 2y + (a^2 - 2)z = a + 1 \end{cases}", font_size=46),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Se elimina hasta que el parámetro quede en los candidatos a pivote.",
                "Se hallan todos los valores que anulan cada candidato y se estudian por separado.",
                "Nunca se divide ni se simplifica por una expresión que puede valer 0.",
            ],
            "Lección 30 — errores frecuentes y cómo verificar.",
            voz="En resumen: se elimina hasta que el parámetro quede en los candidatos a pivote. Se hallan todos los valores que anulan cada candidato, y se estudian por separado. Y nunca se divide ni se simplifica por una expresión que puede valer cero. Siguiente: lección treinta, errores frecuentes y cómo verificar.",
        )
