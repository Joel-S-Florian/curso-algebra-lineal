"""Lección 21 — La matriz como transformación lineal del plano.

Escenas (un video cada una):
    LaRejillaSeDeforma, ColumnasSonImagenesDeLaBase, QueSignificaLineal

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l21_transformaciones.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, matriz  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_E1, COLOR_E2 = COLOR_COEFICIENTE, COLOR_TERMINO_INDEP


def con_fondo(mob: Mobject) -> Mobject:
    """Rótulo legible encima de la rejilla."""
    return mob.add_background_rectangle(color=BLACK, opacity=0.85, buff=0.15)


class EscenaRejilla(EscenaCurso):
    """Rejilla de fondo fija + rejilla de color que se transforma (unidad 1: coordenadas = pantalla)."""

    def preparar(self, rango=10):
        self.fondo = NumberPlane(
            x_range=[-rango, rango, 1], y_range=[-rango, rango, 1],
            x_length=2 * rango, y_length=2 * rango,
            background_line_style={"stroke_color": GREY_D, "stroke_opacity": 0.5, "stroke_width": 1},
            axis_config={"stroke_opacity": 0.4},
        )
        self.rejilla = NumberPlane(
            x_range=[-rango, rango, 1], y_range=[-rango, rango, 1],
            x_length=2 * rango, y_length=2 * rango,
            background_line_style={"stroke_color": BLUE_D, "stroke_opacity": 0.8, "stroke_width": 2},
        )
        self.add(self.fondo)
        self.play(Create(self.rejilla), run_time=1.5)

    def vector(self, x, y, color) -> Arrow:
        return Arrow(ORIGIN, [x, y, 0], buff=0, color=color, stroke_width=7, max_tip_length_to_length_ratio=0.18)

    def base(self):
        e1, e2 = self.vector(1, 0, COLOR_E1), self.vector(0, 1, COLOR_E2)
        self.play(GrowArrow(e1), GrowArrow(e2))
        return e1, e2

    def transformar(self, m, flechas=(), otros=(), run_time=3):
        """Aplica la matriz m a la rejilla (y a `otros`) y redibuja cada flecha en su nueva posición.

        Las flechas no se deforman con ApplyMatrix porque la punta se estiraría con la rejilla.
        """
        matriz_np = np.array(m, dtype=float)

        def imagen(p):
            x, y = matriz_np @ p[:2]
            return np.array([x, y, 0.0])

        nuevas = [
            Arrow(imagen(f.get_start()), imagen(f.get_end()), buff=0, color=f.get_color(), stroke_width=7, max_tip_length_to_length_ratio=0.18)
            for f in flechas
        ]
        self.play(
            ApplyMatrix(m, VGroup(self.rejilla, *otros)),
            *[Transform(f, n) for f, n in zip(flechas, nuevas)],
            run_time=run_time,
        )

    def rotulo_matriz(self, tex: str) -> Mobject:
        rot = con_fondo(MathTex(tex, font_size=46)).to_corner(UL, buff=0.5)
        self._fijar(rot)
        return rot


class LaRejillaSeDeforma(EscenaRejilla):
    def construct(self):
        self.mostrar_portada("Lección 21 · Parte 1", "La matriz como transformación del plano")
        self.preparar()
        idea = con_fondo(Text("Cada punto x del plano se mueve al punto Ax", font_size=TAM_TEXTO)).to_edge(UP, buff=0.4)
        self.decir("Una matriz de dos por dos mueve cada punto equis del plano al punto a por equis. Veamos qué le pasa a todo el plano a la vez.")
        self.play(FadeIn(idea))
        e1, e2 = self.base()
        v = self.vector(1, 2, COLOR_PIVOTE)
        rot_v = con_fondo(MathTex(r"\mathbf{x} = (1, 2)", font_size=36, color=COLOR_PIVOTE)).next_to([1, 2, 0], RIGHT, buff=0.15)
        self.decir("Fijémonos en un vector y en los dos vectores de la base, e uno y e dos.")
        self.play(GrowArrow(v), FadeIn(rot_v))
        m = self.rotulo_matriz(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}")
        self.decir("Con esta matriz, uno, uno; cero, uno…")
        self.play(FadeIn(m))
        self.wait(1)
        self.play(FadeOut(rot_v))
        self.decir("…cada punto se desplaza en horizontal tanto como vale su altura: la rejilla se inclina, se cizalla.")
        self.transformar([[1, 1], [0, 1]], flechas=[e1, e2, v])
        rot_ax = con_fondo(MathTex(r"A\mathbf{x} = (3, 2)", font_size=36, color=COLOR_PIVOTE)).next_to([3, 2, 0], RIGHT, buff=0.15)
        self.play(FadeIn(rot_ax))
        cuenta = con_fondo(MathTex(r"\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}", font_size=40)).to_corner(DL, buff=0.5)
        self.decir("La cuenta lo confirma: a por equis suma a la primera coordenada el valor de la segunda.")
        self.play(FadeIn(cuenta))
        self.pie("La rejilla se «cizalla»: cada punto se desplaza en horizontal tanto como vale su altura.", espera=4)
        self.play(FadeOut(rot_ax), FadeOut(cuenta), FadeOut(m))
        self.decir("Deshacemos el cambio.")
        self.transformar([[1, -1], [0, 1]], flechas=[e1, e2, v], run_time=2)

        m = self.rotulo_matriz(r"B = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}")
        self.play(FadeIn(m))
        self.decir("Con otra matriz, dos, menos uno; uno, uno, la rejilla gira y se estira.")
        self.transformar([[2, -1], [1, 1]], flechas=[e1, e2, v])
        propiedades = con_fondo(VGroup(
            Text("Las rectas siguen siendo rectas.", font_size=TAM_NOTA + 2),
            Text("Las paralelas siguen paralelas e igualmente espaciadas.", font_size=TAM_NOTA + 2),
            Text("El origen no se mueve: A·0 = 0.", font_size=TAM_NOTA + 2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)).to_corner(DR, buff=0.5)
        self._fijar(propiedades)
        self.decir("Pero las rectas siguen siendo rectas, las paralelas siguen paralelas e igual de separadas, y el origen no se mueve.")
        self.play(FadeIn(propiedades))
        self.wait(5)
        self.pie(
            "Una matriz 2 × 2 transforma TODO el plano. Este tipo de deformación se llama TRANSFORMACIÓN LINEAL.\n"
            "El dibujo es una intuición; la definición precisa llega en el video 3.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F06-N1-02",
            VGroup(
                MathTex(r"A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}", font_size=52),
                Tex(r"Calcula $A$ por $(1, 0)$, $(0, 1)$, $(1, 1)$ y $(-2, 3)$. ¿Qué hace $A$ con el plano?", font_size=40),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Una matriz A de 2 × 2 mueve cada punto x del plano al punto Ax.",
                "Las rectas siguen rectas, las paralelas siguen paralelas y equiespaciadas.",
                "El origen queda fijo.",
            ],
            "qué papel juegan las columnas de la matriz.",
            voz="En resumen: una matriz a de dos por dos mueve cada punto equis del plano al punto a por equis. Las rectas siguen rectas, y las paralelas siguen paralelas y equiespaciadas. Y el origen queda fijo. Siguiente: qué papel juegan las columnas de la matriz.",
        )


class ColumnasSonImagenesDeLaBase(EscenaRejilla):
    def construct(self):
        self.mostrar_portada("Lección 21 · Parte 2", "Las columnas dicen adónde van e₁ y e₂")
        self.preparar()
        e1, e2 = self.base()
        rotulos = VGroup(
            con_fondo(MathTex(r"\mathbf{e}_1 = (1, 0)", font_size=34, color=COLOR_E1)).next_to([1, 0, 0], DR, buff=0.1),
            con_fondo(MathTex(r"\mathbf{e}_2 = (0, 1)", font_size=34, color=COLOR_E2)).next_to([0, 1, 0], UL, buff=0.1),
        )
        self.decir("Los vectores e uno y e dos forman la base del plano.")
        self.play(FadeIn(rotulos))
        # x = (1, 2) = 1 e1 + 2 e2, como camino.
        tramo1 = self.vector(1, 0, COLOR_E1)
        tramo2 = Arrow([1, 0, 0], [1, 2, 0], buff=0, color=COLOR_E2, stroke_width=7, max_tip_length_to_length_ratio=0.18)
        x = self.vector(1, 2, COLOR_PIVOTE)
        lectura = con_fondo(MathTex(r"\mathbf{x} = 1\,\mathbf{e}_1 + 2\,\mathbf{e}_2", font_size=40, color=COLOR_PIVOTE)).to_corner(UR, buff=0.5)
        self._fijar(lectura)
        self.decir("Todo vector se escribe con e uno y e dos: uno, dos es un paso por e uno y dos pasos por e dos.")
        self.play(GrowArrow(tramo1), GrowArrow(tramo2))
        self.play(GrowArrow(x), FadeIn(lectura))
        self.pie("Todo vector es una combinación de e₁ y e₂: (1, 2) = 1·e₁ + 2·e₂.", espera=3)

        m = self.rotulo_matriz(r"A = \begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}")
        self.decir("Ahora transformamos con la matriz dos, menos uno; uno, uno.")
        self.play(FadeIn(m), FadeOut(rotulos))
        self.transformar([[2, -1], [1, 1]], flechas=[e1, e2, tramo1, tramo2, x])
        imagenes = VGroup(
            con_fondo(MathTex(r"A\mathbf{e}_1 = (2, 1)", font_size=34, color=COLOR_E1)).next_to([2, 1, 0], DR, buff=0.1),
            con_fondo(MathTex(r"A\mathbf{e}_2 = (-1, 1)", font_size=34, color=COLOR_E2)).next_to([-1, 1, 0], UL, buff=0.1),
        )
        self.decir("Después de transformar, e uno ha ido a dos, uno, y e dos, a menos uno, uno.")
        self.play(FadeIn(imagenes))
        columnas = con_fondo(matriz([[2, -1], [1, 1]], colores_columnas=[COLOR_E1, COLOR_E2])).next_to(m, DOWN, buff=0.3).align_to(m, LEFT)
        self._fijar(columnas)
        self.decir("¡Son la primera y la segunda columna de a! Las columnas son las imágenes de la base.")
        self.play(FadeIn(columnas))
        self.pie("¡e₁ va a la primera columna de A y e₂ a la segunda! Las columnas son las imágenes de la base.", espera=4)
        nueva_lectura = con_fondo(MathTex(r"A\mathbf{x} = 1\,(2, 1) + 2\,(-1, 1) = (0, 3)", font_size=40, color=COLOR_PIVOTE)).to_corner(UR, buff=0.5)
        self._fijar(nueva_lectura)
        self.decir("Y el camino se transforma igual: un paso por a e uno, y dos pasos por a e dos. Es a por equis como combinación de columnas.")
        self.play(FadeOut(lectura), FadeIn(nueva_lectura))
        self.decir("Para conocer una matriz, basta saber adónde van e uno y e dos.")
        self.pie(
            "El camino «1 paso por e₁, 2 por e₂» se convierte en «1 paso por Ae₁, 2 por Ae₂».\n"
            "Es Ax como combinación de columnas (Lección 19): conocer las columnas basta para conocer A.",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F06-N3-02",
            VGroup(
                Tex(r"Una matriz $A$ de $2\times 2$ lleva $\mathbf{e}_1$ a $(0, 1)$ y $\mathbf{e}_2$ a $(-1, 0)$.", font_size=40),
                Tex(r"a) Escribe $A$. \quad b) Calcula $A(3, 2)$. \quad c) ¿Qué movimiento del plano es?", font_size=40),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Columna 1 de A = A·e₁; columna 2 de A = A·e₂.",
                "A(x₁e₁ + x₂e₂) = x₁·Ae₁ + x₂·Ae₂.",
                "Para describir A basta saber adónde van e₁ y e₂.",
            ],
            "qué significa exactamente «lineal».",
            voz="En resumen: la columna uno de a es a por e uno, y la columna dos es a por e dos. Como equis es equis uno por e uno más equis dos por e dos, a por equis es equis uno por a e uno más equis dos por a e dos. Para describir a basta saber adónde van e uno y e dos. Siguiente: qué significa exactamente lineal.",
        )


class QueSignificaLineal(EscenaRejilla):
    def construct(self):
        self.mostrar_portada("Lección 21 · Parte 3", "¿Qué significa «lineal»?")
        self.preparar()
        definicion = con_fondo(VGroup(
            MathTex(r"T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})", font_size=40),
            MathTex(r"T(c\,\mathbf{u}) = c\,T(\mathbf{u})", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)).to_corner(UL, buff=0.4)
        self._fijar(definicion)
        self.decir("Lineal significa dos cosas: la imagen de una suma es la suma de las imágenes, y la imagen de un múltiplo es el múltiplo de la imagen.")
        self.play(FadeIn(definicion))
        u, v = self.vector(1.5, 0.3, COLOR_E1), self.vector(0.5, 1.5, COLOR_E2)
        suma = self.vector(2, 1.8, COLOR_PIVOTE)
        lados = VGroup(
            DashedLine([1.5, 0.3, 0], [2, 1.8, 0], color=COLOR_E2),
            DashedLine([0.5, 1.5, 0], [2, 1.8, 0], color=COLOR_E1),
        )
        self.decir("Tomemos dos vectores, u y uve.")
        self.play(GrowArrow(u), GrowArrow(v))
        self.decir("Su suma es la diagonal del paralelogramo que forman.")
        self.play(Create(lados), GrowArrow(suma))
        self.pie("u + v es la diagonal del paralelogramo formado por u y v.", espera=2)
        self.decir("Después de transformar, sigue siendo un paralelogramo: la imagen de u más uve es la imagen de u más la imagen de uve.")
        self.transformar([[1, -1], [1, 1]], flechas=[u, v, suma], otros=[lados])
        self.pie("Después de transformar, sigue siendo un paralelogramo: la imagen de u + v es T(u) + T(v).", espera=4)
        doble = self.vector(2.4, 3.6, COLOR_E1)  # 2·T(u), con T(u) = (1.2, 1.8)
        self.decir("Y el doble de u se transforma en el doble de su imagen. Una transformación con estas dos propiedades es lineal.")
        self.play(TransformFromCopy(u, doble), run_time=1.5)
        self.pie("Y el doble de u se transforma en el doble de T(u). Una transformación con estas dos propiedades es LINEAL.", espera=4)
        self.limpiar()

        # Contraejemplos.
        curva = NumberPlane(x_range=[-7, 7, 1], y_range=[-4, 4, 1], x_length=14, y_length=8,
                            background_line_style={"stroke_color": BLUE_D, "stroke_opacity": 0.8, "stroke_width": 2})
        curva.prepare_for_nonlinear_transform()
        self.add(self.fondo)
        self.decir("Esto, en cambio, no es lineal.")
        self.play(Create(curva))
        titulo = con_fondo(Text("Transformaciones que NO son lineales", font_size=38, weight="BOLD")).to_edge(UP, buff=0.4)
        self.play(FadeIn(titulo))
        self.decir("Las rectas se curvan.")
        self.play(ApplyPointwiseFunction(lambda p: p + np.array([0.15 * p[1] ** 2, 0.1 * p[0] ** 2 - 0.5, 0]), curva), run_time=3)
        nota = con_fondo(Text("Las rectas se curvan: no es lineal\n(no la puede producir ninguna matriz).", font_size=TAM_NOTA + 2, line_spacing=1.1)).to_corner(DR, buff=0.5)
        self._fijar(nota)
        self.play(FadeIn(nota))
        self.wait(3)
        self.play(FadeOut(nota), FadeOut(curva))
        traslacion = NumberPlane(x_range=[-9, 9, 1], y_range=[-6, 6, 1], x_length=18, y_length=12,
                                 background_line_style={"stroke_color": BLUE_D, "stroke_opacity": 0.8, "stroke_width": 2})
        origen = Dot(ORIGIN, color=COLOR_ERROR, radius=0.12)
        self.decir("Y trasladar tampoco es lineal…")
        self.play(Create(traslacion), FadeIn(origen))
        self.bring_to_front(titulo)
        self.decir("…porque el origen se mueve, y una transformación lineal siempre deja fijo el origen.")
        self.play(VGroup(traslacion, origen).animate.shift(RIGHT * 1 + UP * 1), run_time=2)
        nota = con_fondo(Text("Trasladar mueve el origen: T(0) no es 0.\nNo es lineal (A·0 = 0 para toda matriz).", font_size=TAM_NOTA + 2, line_spacing=1.1)).to_corner(DR, buff=0.5)
        self._fijar(nota)
        self.play(FadeIn(nota))
        self.wait(4)
        self.limpiar()

        titulo = self.encabezado("Demostración: multiplicar por A es lineal")
        prueba = VGroup(
            MathTex(r"\big(A(\mathbf{u} + \mathbf{v})\big)_i = \sum_j a_{ij}(u_j + v_j) = \sum_j a_{ij}u_j + \sum_j a_{ij}v_j = (A\mathbf{u})_i + (A\mathbf{v})_i", font_size=38),
            MathTex(r"\big(A(c\,\mathbf{u})\big)_i = \sum_j a_{ij}(c\,u_j) = c\sum_j a_{ij}u_j = c\,(A\mathbf{u})_i", font_size=38),
            Tex(r"Solo se ha usado la propiedad distributiva de los números reales. \quad $\blacksquare$", font_size=36, color=COLOR_SOLUCION),
            Tex(r"La animación lo sugiere; esta cuenta lo demuestra, para cualquier tamaño $m\times n$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.55)
        self._fijar(prueba)
        self.decir("Que multiplicar por una matriz es lineal se demuestra con la propiedad distributiva de los números: a por u más uve es a por u más a por uve, y a por ce u es ce por a u.")
        for linea in prueba:
            self.play(FadeIn(linea))
            self.wait(2.5)

        self.ejercicio_propuesto(
            "F06-N5-01",
            VGroup(
                Tex(r"¿Es lineal $T(x, y) = (x + y,\ 2x)$? ¿Y $S(x, y) = (x + 1,\ y)$? ¿Y $R(x, y) = (xy,\ y)$?", font_size=40),
                Tex(r"Si lo es, escribe su matriz; si no, da un contraejemplo.", font_size=40),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Lineal: T(u + v) = T(u) + T(v) y T(cu) = cT(u).",
                "Toda matriz A define una transformación lineal: x se transforma en Ax.",
                "Curvar rectas o mover el origen no es lineal.",
            ],
            "Lección 22 — escribir un sistema como Ax = b.",
            voz="En resumen: una transformación es lineal si la imagen de una suma es la suma de las imágenes, y la imagen de ce por u es ce por la imagen de u. Toda matriz a define una transformación lineal: equis se transforma en a por equis. Y curvar rectas o mover el origen no es lineal. Siguiente: lección veintidós, escribir un sistema como a equis igual a be.",
        )
