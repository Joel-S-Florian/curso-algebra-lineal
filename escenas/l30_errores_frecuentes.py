"""Lección 30 — Errores frecuentes en la eliminación de Gauss y cómo verificar.

Escenas (un video cada una):
    ErroresFrecuentesGauss, VerificarSiempre

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l30_errores_frecuentes.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, lista, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def comparacion(mal: str, bien: str) -> VGroup:
    """Dos filas «mal / bien» con su marca."""
    return VGroup(
        VGroup(MathTex(r"\times", color=COLOR_ERROR, font_size=44), MathTex(mal, font_size=40, color=COLOR_ERROR)).arrange(RIGHT, buff=0.4),
        VGroup(MathTex(r"\checkmark", color=COLOR_SOLUCION, font_size=44), MathTex(bien, font_size=40, color=COLOR_SOLUCION)).arrange(RIGHT, buff=0.4),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)


class ErroresFrecuentesGauss(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 30 · Parte 1", "Errores frecuentes en Gauss")
        titulo = self.encabezado("1. Errores de signo")
        m = matriz_gauss([[1, -2, 3], [3, -4, 5]], pivotes=[(0, 0)]).move_to(LEFT * 2.5 + UP * 1.4)
        self.decir("Primer error frecuente: los signos.")
        self.play(FadeIn(m))
        self.decir("A la fila dos le restamos tres veces la fila uno.")
        m = self.operar_filas(m, ("sumar", 1, 0, -3), pivotes=[(0, 0), (1, 1)], espera=1)
        cmp = comparacion(r"-4 - 3\cdot 2 = -10", r"-4 - 3\cdot(-2) = -4 + 6 = 2").next_to(m, DOWN, buff=0.6).set_x(0)
        self.decir("En la segunda columna, es fácil escribir menos cuatro menos tres por dos, que da menos diez. Está mal.")
        self.play(FadeIn(cmp[0]))
        self.wait(1.5)
        self.decir("Lo correcto es menos cuatro menos tres por menos dos: menos cuatro más seis, dos. Restar un negativo es sumar.")
        self.play(FadeIn(cmp[1]))
        self.decir("Escribe la cuenta de cada columna con paréntesis.")
        self.pie("Restar un negativo es sumar. Escribe la cuenta de cada columna con paréntesis: -4 - 3·(-2).", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "2. Olvidar la columna de b")
        cmp = comparacion(
            r"R_2 \leftarrow R_2 - 3R_1:\ \ \left[\begin{array}{cc|c} 0 & 2 & 5 \end{array}\right]",
            r"R_2 \leftarrow R_2 - 3R_1:\ \ \left[\begin{array}{cc|c} 0 & 2 & -4 \end{array}\right]\quad (5 - 3\cdot 3 = -4)",
        ).shift(UP * 0.5)
        self.decir("Segundo error: olvidar la columna de be, y dejar el cinco sin cambiar.")
        self.play(FadeIn(cmp[0]))
        self.wait(1.5)
        self.decir("La operación es sobre la ecuación entera: el término independiente también se resta. Cinco menos tres por tres, menos cuatro.")
        self.play(FadeIn(cmp[1]))
        self.pie("La operación es sobre la ECUACIÓN entera: el término independiente también se resta.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "3. Operaciones que no son elementales")
        ilegales = VGroup(
            Tex(r"$R_1 \leftarrow 0\cdot R_1$: \ borra una ecuación y no se puede deshacer.", font_size=36),
            Tex(r"$R_1 \leftarrow R_1\cdot R_2$ (entrada a entrada): \ $(x + y)(x - y)$ ni siquiera es lineal.", font_size=36),
            Tex(r"$R_1 \leftarrow R_1 + 3$: \ $[\,1 \ \ 1 \mid 2\,]$ pasaría a $4x + 4y = 5$, otra recta.", font_size=36),
            Tex(r"$R_2 \leftarrow R_2 - R_2$: \ es $0\cdot R_2$ disfrazado.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(ilegales)
        self.decir("Tercer error: usar operaciones que no son elementales. Multiplicar una fila por cero borra una ecuación. Multiplicar filas entre sí ni siquiera da algo lineal. Sumar un número a cada entrada cambia la recta. Y restarle a una fila ella misma es multiplicar por cero, disfrazado.")
        for i in ilegales:
            cruz = MathTex(r"\times", color=COLOR_ERROR, font_size=44).next_to(i, LEFT, buff=0.3)
            self.play(FadeIn(cruz), FadeIn(i))
            self.wait(2)
        self.decir("Solo hay tres operaciones: intercambiar, multiplicar por un número distinto de cero, y sumar a una fila un múltiplo de otra.")
        self.pie("Solo hay tres operaciones: intercambiar, multiplicar por k distinto de 0 y sumar k veces OTRA fila.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "4. Dos operaciones a la vez")
        antes = matriz_gauss([[1, 1, 2], [1, -1, 0]]).move_to(LEFT * 4 + UP * 0.6)
        despues = matriz_gauss([[0, 2, 2], [0, -2, -2]]).move_to(RIGHT * 2.6 + UP * 0.6)
        flecha = Arrow(antes.get_right(), despues.get_left(), buff=0.4, color=COLOR_ERROR)
        ops = VGroup(
            MathTex(r"R_1 \leftarrow R_1 - R_2", font_size=34, color=COLOR_ERROR),
            MathTex(r"R_2 \leftarrow R_2 - R_1", font_size=34, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.15).next_to(flecha, UP, buff=0.2)
        self.decir("Cuarto error: hacer dos operaciones a la vez.")
        self.play(FadeIn(antes))
        self.decir("Restamos la fila dos a la uno, y la fila uno a la dos, las dos a la vez.")
        self.play(GrowArrow(flecha), Write(ops))
        self.play(FadeIn(despues))
        texto = parrafo(r"Las dos usan las filas \textbf{viejas}. El resultado tiene filas",
                        r"proporcionales (parece SCI), pero el original tiene solución única",
                        r"$(1, 1)$: se perdió información.",
                        font_size=34).next_to(VGroup(antes, despues), DOWN, buff=0.8)
        ajustar_al_encuadre(texto)
        self.decir("Las dos operaciones usaron las filas viejas. El resultado tiene filas proporcionales, y parece que hay infinitas soluciones; pero el sistema original tiene una sola, uno, uno. Se perdió información.")
        self.play(FadeIn(texto))
        self.decir("Haz las operaciones de una en una, cada una sobre la matriz que dejó la anterior.")
        self.pie("Haz las operaciones de una en una, cada una sobre la matriz que dejó la anterior.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "5. Otros despistes")
        otros = VGroup(
            Tex(r"Pasar a decimales: $\tfrac{1}{3} \approx 0.33$ arrastra errores. Fracciones exactas.", font_size=36),
            Tex(r"Copiar mal una fila que no cambia al reescribir la matriz.", font_size=36),
            Tex(r"Usar como pivote una entrada que vale $0$ (o que puede valer $0$, L29).", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.decir("Otros despistes: pasar a decimales, que arrastra errores; copiar mal una fila que no cambia; y usar como pivote una entrada que vale cero, o que puede valer cero.")
        for o in otros:
            self.play(FadeIn(o))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F08-N3-04",
            VGroup(
                Tex(r"Para $\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 4 & -3 & 5 \end{array}\right]$ un estudiante escribe $R_2 \leftarrow R_2 - 2R_1$: \ $[\,0 \ \ -1 \mid -5\,]$", font_size=36),
                Tex(r"y concluye $y = 5$, $x = 0$. Encuentra el error, corrígelo y verifica.", font_size=36),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Signos: restar un negativo es sumar; cuentas por columnas con paréntesis.",
                "Toda la fila, columna de b incluida; solo las tres operaciones elementales.",
                "Una operación por paso, sobre la matriz que dejó la anterior.",
            ],
            "verificar siempre.",
            voz="En resumen: cuidado con los signos, porque restar un negativo es sumar; haz las cuentas por columnas y con paréntesis. Opera toda la fila, columna de be incluida, y solo con las tres operaciones elementales. Y una operación por paso, sobre la matriz que dejó la anterior. Siguiente: verificar siempre.",
        )


class VerificarSiempre(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 30 · Parte 2", "Verificar siempre (y bien)")
        titulo = self.encabezado("Un error que el sistema escalonado no delata")
        izq = VGroup(
            Text("con el error de signo", font_size=TAM_NOTA, color=COLOR_ERROR),
            MathTex(r"\left[\begin{array}{cc|c} 1 & -2 & 3 \\ 0 & -10 & -4 \end{array}\right]", font_size=44),
            MathTex(r"y = \tfrac{2}{5},\quad x = 3 + \tfrac{4}{5} = \tfrac{19}{5}", font_size=40),
        ).arrange(DOWN, buff=0.4).move_to(LEFT * 3.4 + UP * 0.9)
        der = VGroup(
            Text("bien hecho", font_size=TAM_NOTA, color=COLOR_SOLUCION),
            MathTex(r"\left[\begin{array}{cc|c} 1 & -2 & 3 \\ 0 & 2 & -4 \end{array}\right]", font_size=44),
            MathTex(r"y = -2,\quad x = 3 - 4 = -1", font_size=40),
        ).arrange(DOWN, buff=0.4).move_to(RIGHT * 3.4 + UP * 0.9)
        self.decir("Un error que el sistema escalonado no delata. A la izquierda, la eliminación con el error de signo; a la derecha, bien hecha.")
        self.play(FadeIn(izq), FadeIn(der))
        self.wait(2)
        comprobaciones = VGroup(
            MathTex(r"\text{en el escalonado: } \tfrac{19}{5} - \tfrac{4}{5} = 3\ \checkmark,\ \ -10\cdot\tfrac{2}{5} = -4\ \checkmark", font_size=34),
            MathTex(r"\text{en el original } 3x - 4y = 5:\ \ \tfrac{57}{5} - \tfrac{8}{5} = \tfrac{49}{5} \neq 5\ \times", font_size=34, color=COLOR_ERROR),
            MathTex(r"\text{la buena: } -1 + 4 = 3\ \checkmark,\ \ -3 + 8 = 5\ \checkmark", font_size=34, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(VGroup(izq, der), DOWN, buff=0.6)
        ajustar_al_encuadre(comprobaciones)
        self.decir("La solución equivocada, diecinueve quintos, dos quintos, cumple el sistema escalonado equivocado. Pero en el original, tres equis menos cuatro ye da cuarenta y nueve quintos, no cinco. La buena, menos uno, menos dos, cumple las dos ecuaciones.")
        for c in comprobaciones:
            self.play(FadeIn(c))
            self.wait(2)
        self.decir("Solo el sistema original delata el error.")
        self.pie("La solución equivocada cumple el sistema escalonado equivocado. Solo el ORIGINAL detecta el error.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificar con Ax = b")
        producto = MathTex(
            r"\begin{bmatrix} 1 & -2 \\ 3 & -4 \end{bmatrix}\begin{bmatrix} -1 \\ -2 \end{bmatrix} = "
            r"\begin{bmatrix} -1 + 4 \\ -3 + 8 \end{bmatrix} = \begin{bmatrix} 3 \\ 5 \end{bmatrix} = \mathbf{b}\ \checkmark",
            font_size=48,
        ).shift(UP * 0.6)
        self.decir("Es la misma comprobación escrita como a por equis igual a be: cada fila de la matriz original por la solución debe dar su término de be.")
        self.play(Write(producto), run_time=2)
        self.pie("Es la misma comprobación escrita con la matriz original A (L22): cada fila por x debe dar su término de b.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo se verifica cada tipo de resultado")
        tipos = VGroup(
            Tex(r"\textbf{SCD}: se sustituye la solución en todas las ecuaciones originales.", font_size=36),
            parrafo(r"\textbf{SCI}: se sustituye la fórmula con $t$ \textbf{general} (los términos en $t$",
                    r"deben cancelarse) y, además, un valor concreto, por ejemplo $t = 0$.", font_size=36, sangria=0.4),
            parrafo(r"\textbf{SI}: se busca la combinación de ecuaciones que da $0 = c$;",
                    r"por ejemplo, en la L28, \ $E_3 - E_1 - E_2$ da $0 = 8 - 2 - 5 = 1$.", font_size=36, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(tipos)
        self.decir("Cómo se verifica cada tipo de resultado. Con una solución, se sustituye en todas las ecuaciones originales. Con infinitas, se sustituye la fórmula con te general, y los términos en te deben cancelarse. Y si no hay solución, se muestra la combinación de ecuaciones que da cero igual a ce.")
        for t in tipos:
            self.play(FadeIn(t))
            self.wait(2.8)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lista de control")
        control = lista(
            [
                "Escribe cada operación (R₂ ← R₂ - 3R₁) antes de hacerla.",
                "Una operación por paso; solo cambia la fila destino.",
                "Toda la fila, columna de b incluida; cuentas con paréntesis.",
                "Fracciones exactas, nunca decimales redondeados.",
                "Con parámetros: separa los casos antes de dividir.",
                "Comprueba en el sistema ORIGINAL.",
            ],
            font_size=TAM_TEXTO,
        ).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(control)
        self.decir("Lista de control: escribe cada operación antes de hacerla; una operación por paso; toda la fila, con be, y cuentas con paréntesis; fracciones exactas; con parámetros, separa los casos antes de dividir; y comprueba siempre en el sistema original.")
        for c in control:
            self.play(FadeIn(c, shift=RIGHT * 0.2))
            self.wait(1.2)
        self.wait(3)

        self.ejercicio_propuesto(
            "F08-N4-07",
            VGroup(
                Tex(r"Un estudiante afirma que $(2, 1, 3)$ resuelve el sistema. Compruébalo;", font_size=36),
                Tex(r"si no es así, resuelve por Gauss y verifica tu respuesta.", font_size=36),
                MathTex(r"\begin{cases} x + y + z = 6 \\ x - y + 2z = 5 \\ 2x + y - z = 1 \end{cases}", font_size=46),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Un error de cuentas produce un sistema escalonado coherente pero falso.",
                "Por eso se verifica en el original (o con Ax = b), nunca en el escalonado.",
                "SCI: verificar con t general; SI: exhibir la combinación que da 0 = c.",
            ],
            "Unidad 5, Lección 31 — forma escalonada reducida (Gauss-Jordan).",
            voz="En resumen: un error de cuentas produce un sistema escalonado coherente, pero falso. Por eso se verifica en el original, o con a equis igual a be, nunca en el escalonado. Con infinitas soluciones, se verifica con te general; sin solución, se muestra la combinación que da cero igual a ce. Siguiente: unidad cinco, lección treinta y uno, la forma escalonada reducida.",
        )
