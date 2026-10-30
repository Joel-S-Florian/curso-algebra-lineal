"""Lección 0 — Prueba del entorno.

Una mini-clase que ejercita todo lo que usará el curso: texto con tildes (Pango),
fórmulas (LaTeX), matrices, transformaciones de ecuaciones, operaciones por filas
y ejes con rectas. Si este video se genera bien, el entorno está listo.

Renderizar (desde la carpeta raíz del proyecto):
    manim -pql escenas/l00_prueba_entorno.py PruebaEntorno   # borrador rápido
    manim -qh  escenas/l00_prueba_entorno.py PruebaEntorno   # calidad final 1080p60
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import (  # noqa: E402
    EscenaCurso,
    alinear_por_igual,
    matriz_aumentada,
    sustituir_alineado,
    titulo_leccion,
)
from curso.estilo import *  # noqa: E402,F403


def colorear_ecuacion(ec: MathTex, coeficientes=(0, 3), termino=6) -> MathTex:
    """Colorea coeficientes y término independiente de una ecuación «a x + b y = c»."""
    for i in coeficientes:
        ec[i].set_color(COLOR_COEFICIENTE)
    ec[termino].set_color(COLOR_TERMINO_INDEP)
    return ec


class PruebaEntorno(EscenaCurso):
    def construct(self):
        self.portada()
        ec1, ec2, llave, matriz = self.sistema_a_matriz()
        ec1, ec2, llave = self.operacion_por_filas(ec1, ec2, llave, matriz)
        self.sustitucion_hacia_atras(ec1, ec2, llave)
        self.interpretacion_geometrica()
        self.cierre()

    # ------------------------------------------------------------------ 1
    def portada(self):
        titulo = titulo_leccion("Lección 0", "Prueba del entorno")
        subtitulo = Text(
            "Un sistema de ecuaciones, de principio a fin",
            font_size=TAM_TEXTO,
            color=COLOR_SECUNDARIO,
        ).next_to(titulo, DOWN, buff=0.6)
        self.decir("Bienvenido. Antes de empezar el curso, vamos a recorrer en pocos minutos el camino completo que haremos durante muchas lecciones: de un sistema de ecuaciones a su solución.")
        self.play(FadeIn(titulo, shift=UP * 0.3))
        self.play(Write(subtitulo))
        self.wait(2)
        self.limpiar()

    # ------------------------------------------------------------------ 2
    def sistema_a_matriz(self):
        pregunta = Text(
            "¿Qué par de números (x, y) cumple las dos ecuaciones a la vez?",
            font_size=TAM_TEXTO,
        ).to_edge(UP)
        ec1 = MathTex("x", "+", "y", "=", "3")
        ec2 = MathTex("x", "-", "y", "=", "1")
        sistema = alinear_por_igual(ec1, ec2).scale(1.3)
        llave = Brace(sistema, LEFT)
        self.decir("Buscamos dos números, equis y ye, que cumplan las dos igualdades a la vez: equis más ye igual a tres, y equis menos ye igual a uno. Eso es un sistema de ecuaciones.")
        self.play(Write(pregunta))
        self.play(Write(sistema), GrowFromCenter(llave))
        self.wait(2)

        # Los coeficientes «invisibles»: x = 1·x y −y = (−1)·y.
        # "{1}" se ve igual que "1", pero así TransformMatchingTex no confunde
        # el coeficiente con el término independiente 1.
        ec1e = colorear_ecuacion(MathTex("{1}", "x", "+", "{1}", "y", "=", "3"))
        ec2e = colorear_ecuacion(MathTex("{1}", "x", "+", "(-1)", "y", "=", "1"))
        explicito = alinear_por_igual(ec1e, ec2e).scale(1.3).move_to(sistema)
        nota = Tex(
            r"Coeficientes que no se escriben: $x = 1\cdot x$, \quad $-y = (-1)\cdot y$",
            font_size=34,
            color=COLOR_SECUNDARIO,
        ).to_edge(DOWN, buff=0.8)
        self.decir("Delante de equis hay un uno que no se escribe, y delante de menos ye hay un menos uno. Esos números que multiplican a las incógnitas se llaman coeficientes. El signo menos pertenece al coeficiente.")
        self.play(
            TransformMatchingTex(ec1, ec1e),
            TransformMatchingTex(ec2, ec2e),
            Transform(llave, Brace(explicito, LEFT)),
            FadeIn(nota),
        )
        self.wait(3)

        # La matriz aumentada guarda solo los números, columna por columna.
        self.play(FadeOut(nota))
        bloque = VGroup(explicito, llave)
        self.desplazar([ec1e, ec2e, llave], LEFT * (bloque.get_left()[0] + config.frame_width / 2 - 1.2))
        matriz = matriz_aumentada([["1", "1", "3"], ["1", "-1", "1"]]).scale(1.15)
        matriz.to_edge(RIGHT, buff=2)
        columnas = matriz.get_columns()
        columnas[0].set_color(COLOR_COEFICIENTE)
        columnas[1].set_color(COLOR_COEFICIENTE)
        columnas[2].set_color(COLOR_TERMINO_INDEP)
        flecha = Arrow(bloque.get_right(), matriz.get_left(), buff=0.4)

        entradas = matriz.get_entries()  # en orden de lectura: fila 1, luego fila 2
        origenes = [ec1e[0], ec1e[3], ec1e[6], ec2e[0], ec2e[3], ec2e[6]]
        self.decir("Si solo guardamos los números, en el mismo orden, obtenemos una tabla: la matriz aumentada.")
        self.play(GrowArrow(flecha))
        self.play(Write(matriz.get_brackets()), Create(matriz.separador))
        self.play(*[TransformFromCopy(o, e) for o, e in zip(origenes, entradas)], run_time=2)
        # Las piezas entraron por separado; desde aquí la matriz es un solo objeto en escena.
        self.remove(*[m for m in self.mobjects if m in matriz.get_family()])
        self.add(matriz)

        rotulo_a = VGroup(
            b := Brace(VGroup(columnas[0], columnas[1]), DOWN, color=COLOR_COEFICIENTE),
            Text("coeficientes (A)", font_size=TAM_NOTA, color=COLOR_COEFICIENTE).next_to(b, DOWN),
        )
        rotulo_b = VGroup(
            c := Brace(columnas[2], UP, color=COLOR_TERMINO_INDEP),
            Text("términos independientes (b)", font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP).next_to(c, UP),
        )
        nombre = Tex(r"Matriz aumentada $[A \mid b]$", font_size=38).next_to(rotulo_a, DOWN, buff=0.4)
        self.decir("En azul, los coeficientes. Detrás de la barra, en naranja, los términos independientes.")
        self.play(FadeIn(rotulo_a), FadeIn(rotulo_b), Write(nombre))
        self.wait(2)

        # Cada fila de la matriz ES una ecuación.
        self.decir("Cada fila de la matriz es exactamente una ecuación del sistema. No hemos perdido información: solo hemos dejado de escribir las letras.")
        for i, ec in enumerate((ec1e, ec2e)):
            marcos = VGroup(
                SurroundingRectangle(ec, color=COLOR_PIVOTE),
                SurroundingRectangle(matriz.get_rows()[i], color=COLOR_PIVOTE),
            )
            self.play(Create(marcos))
            self.wait(1)
            self.play(FadeOut(marcos))

        self.limpiar(ec1e, ec2e, llave, matriz)
        return ec1e, ec2e, llave, matriz

    # ------------------------------------------------------------------ 3
    def operacion_por_filas(self, ec1, ec2, llave, matriz):
        operacion = MathTex(r"R_2 \;\leftarrow\; R_2 - R_1", color=COLOR_OPERACION, font_size=52)
        lectura = Text("«a la fila 2 le restamos la fila 1»", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)
        VGroup(operacion, lectura).arrange(DOWN, buff=0.25).to_edge(UP, buff=0.6)
        self.decir("Ahora, a la segunda fila le restamos la primera, número a número.")
        self.play(Write(operacion), FadeIn(lectura))
        self.wait(1.5)

        # La cuenta, columna por columna.
        cuenta = MathTex(r"1-1=0", r",\qquad", r"-1-1=-2", r",\qquad", r"1-3=-2", font_size=38)
        cuenta.next_to(matriz, DOWN, buff=0.7)
        sobra = cuenta.get_right()[0] - (config.frame_width / 2 - 0.6)
        cuenta.shift(LEFT * max(0, sobra))  # que no toque el borde derecho
        self.decir("Uno menos uno, cero. Menos uno menos uno, menos dos. Y uno menos tres, menos dos.")
        self.play(Write(cuenta))
        self.wait(2)

        nueva_matriz = matriz_aumentada([["1", "1", "3"], ["0", "-2", "-2"]]).scale(1.15).move_to(matriz)
        nueva_fila = nueva_matriz.get_rows()[1]
        nueva_fila[0].set_color(COLOR_PIVOTE)  # el 0 que buscábamos
        nueva_fila[1].set_color(COLOR_COEFICIENTE)
        nueva_fila[2].set_color(COLOR_TERMINO_INDEP)

        # El mismo cambio en el sistema: comparación simultánea.
        ec2n = MathTex("0", "x", "+", "(-2)", "y", "=", "-2").scale(1.3)
        colorear_ecuacion(ec2n)[0].set_color(COLOR_PIVOTE)
        sustituir_alineado(ec2, ec2n)

        self.decir("A la izquierda vemos el mismo cambio hecho en las ecuaciones.")
        self.play(
            ReplacementTransform(matriz.get_rows()[1], nueva_fila),
            TransformMatchingTex(ec2, ec2n),
            run_time=2,
        )
        self.wait(1)
        nota = Text(
            "La x desapareció de la segunda ecuación: ahora solo queda y.",
            font_size=TAM_NOTA,
        ).to_edge(DOWN, buff=0.5)
        self.decir("El objetivo era ese cero: la equis desaparece de la segunda ecuación. Por qué esta operación no cambia las soluciones lo demostraremos en la lección veinticuatro.")
        self.play(FadeIn(nota))
        self.wait(3)

        self.limpiar(ec1, ec2n, llave)
        return ec1, ec2n, llave

    # ------------------------------------------------------------------ 4
    def sustitucion_hacia_atras(self, ec1, ec2, llave):
        sistema = VGroup(ec1, ec2, llave)
        self.desplazar(sistema, UP * 1.8 - sistema.get_center())

        paso1 = MathTex(r"-2y = -2", r"\;\Longrightarrow\;", r"y = 1", font_size=44)
        paso2 = MathTex(r"x + 1 = 3", r"\;\Longrightarrow\;", r"x = 2", font_size=44)
        VGroup(paso1, paso2).arrange(DOWN, buff=0.5).next_to(sistema, DOWN, buff=0.8)
        self.decir("La segunda ecuación ya solo tiene ye: dividimos entre menos dos, y obtenemos ye igual a uno.")
        self.play(Indicate(ec2))
        self.play(Write(paso1))
        self.wait(1.5)
        self.decir("Lo sustituimos en la primera: equis más uno igual a tres, luego equis igual a dos.")
        self.play(Indicate(ec1))
        self.play(Write(paso2))
        self.wait(1.5)

        solucion = MathTex(r"(x,\, y) = (2,\, 1)", font_size=52, color=COLOR_SOLUCION)
        solucion.next_to(paso2, DOWN, buff=0.7)
        self.decir("La solución del sistema es el par dos, uno.")
        self.play(Write(solucion), Create(SurroundingRectangle(solucion, color=COLOR_SOLUCION, buff=0.2)))
        self.wait(3)
        self.limpiar()

    # ------------------------------------------------------------------ 5
    def interpretacion_geometrica(self):
        titulo = Text("Interpretación geométrica", font_size=40).to_edge(UP, buff=0.4)
        ejes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-2, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 24},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.4)
        recta1 = ejes.plot(lambda x: 3 - x, x_range=[-1, 5], color=COLOR_COEFICIENTE)
        recta2 = ejes.plot(lambda x: x - 1, x_range=[-1, 5], color=COLOR_TERMINO_INDEP)

        leyenda = VGroup(
            MathTex(r"x + y = 3", color=COLOR_COEFICIENTE),
            MathTex(r"x - y = 1", color=COLOR_TERMINO_INDEP),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explicacion = Text(
            "Cada ecuación lineal en x, y\nes una recta del plano.",
            font_size=TAM_NOTA,
            line_spacing=1.2,
        )
        idea = Text(
            "La solución del sistema es\nel punto que está en las\ndos rectas a la vez.",
            font_size=TAM_NOTA,
            line_spacing=1.2,
        )
        # Comprobación: sustituir en el sistema ORIGINAL.
        comprobacion = VGroup(
            MathTex(r"2 + 1 = 3", r"\;\checkmark"),
            MathTex(r"2 - 1 = 1", r"\;\checkmark"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        for linea in comprobacion:
            linea[1].set_color(COLOR_SOLUCION)
        # Todo el panel se coloca de una vez para que ninguna línea salga del encuadre.
        panel = VGroup(leyenda, explicacion, idea, comprobacion).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        panel.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.3)

        self.decir("Cada ecuación con dos incógnitas es una recta del plano.")
        self.play(Write(titulo), Create(ejes))
        self.play(Create(recta1), Write(leyenda[0]))
        self.play(Create(recta2), Write(leyenda[1]))
        self.play(FadeIn(explicacion))
        self.wait(2)

        self.decir("Resolver el sistema es encontrar el punto que está en las dos rectas a la vez: el dos, uno.")
        punto = Dot(ejes.c2p(2, 1), color=COLOR_SOLUCION, radius=0.1)
        etiqueta = MathTex(r"(2,\, 1)", color=COLOR_SOLUCION).next_to(punto, RIGHT, buff=0.2)
        self.play(FadeIn(punto, scale=3), Write(etiqueta))
        self.play(Flash(punto, color=COLOR_SOLUCION), FadeIn(idea))
        self.wait(2)
        self.decir("Y nunca terminamos sin comprobar: sustituimos en el sistema original. Dos más uno es tres, y dos menos uno es uno. Las dos igualdades se cumplen.")
        self.play(Write(comprobacion), run_time=2)
        self.wait(3)
        self.limpiar()

    # ------------------------------------------------------------------ 6
    def cierre(self):
        listo = Text("El entorno funciona.", font_size=44, color=COLOR_SOLUCION)
        siguiente = Text(
            "Siguiente: Lección 1 — Números reales y sus operaciones",
            font_size=TAM_TEXTO,
            color=COLOR_SECUNDARIO,
        )
        VGroup(listo, siguiente).arrange(DOWN, buff=0.6)
        self.decir("Si ves este video, tu entorno está listo. Empezamos de verdad en la lección uno, con los números reales.")
        self.play(FadeIn(listo, shift=UP * 0.3))
        self.play(FadeIn(siguiente))
        self.wait(3)
        self.play(FadeOut(listo), FadeOut(siguiente))
