"""Lección 49 — Una base del espacio columna.

Escenas (un video cada una):
    ColumnasPivote, PorQueEnLaMatrizOriginal

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l49_base_del_espacio_columna.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A = [[1, 2, 0, 1], [2, 4, 1, 4], [1, 2, 1, 3]]
R = [[1, 2, 0, 1], [0, 0, 1, 2], [0, 0, 0, 0]]
PIVOTES = (0, 2)
COLOR_BASE = COLOR_PIVOTE  # columnas pivote
COLOR_RESTO = COLOR_SECUNDARIO


def matriz_con_columnas_marcadas(datos, pivotes=PIVOTES, escala=0.95) -> Matrix:
    """Matriz sin barra, con las columnas pivote en amarillo y las demás en gris."""
    m = matriz(datos).scale(escala)
    for j, columna in enumerate(m.get_columns()):
        columna.set_color(COLOR_BASE if j in pivotes else COLOR_RESTO)
    return m


class ColumnasPivote(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 49 · Parte 1", "Una base del espacio columna")
        titulo = self.encabezado("Las columnas pivote")
        m = matriz_con_columnas_marcadas(A, pivotes=()).to_edge(LEFT, buff=1.0).shift(UP * 0.4)
        nombres = VGroup(*[MathTex(rf"\mathbf{{a}}_{k + 1}", font_size=34, color=COLOR_SECUNDARIO).next_to(col, UP, buff=0.25) for k, col in enumerate(m.get_columns())])
        pregunta = Tex(r"¿Qué columnas bastan para generar $\operatorname{Col}(A)$?", font_size=40).next_to(titulo, DOWN, buff=0.5)
        self.decir("Queremos una base del espacio columna de esta matriz. Sus columnas lo generan, pero a lo mejor algunas sobran. ¿Qué columnas bastan?")
        self.play(FadeIn(pregunta))
        self.play(FadeIn(m), FadeIn(nombres))
        self.wait(2)

        r = matriz_con_columnas_marcadas(R).next_to(m, RIGHT, buff=1.6)
        flecha_r = MathTex(r"\xrightarrow{\ \text{reducir}\ }", font_size=40).move_to((m.get_right() + r.get_left()) / 2)
        pivotes_texto = Tex(r"Pivotes en las columnas 1 y 3.", font_size=38, color=COLOR_BASE).next_to(r, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(m, nombres, flecha_r, r, pivotes_texto), margen=0.5)
        self.decir("Reducimos la matriz. Los pivotes caen en las columnas uno y tres.")
        self.play(Write(flecha_r), FadeIn(r))
        self.play(FadeIn(pivotes_texto))
        self.wait(2)
        self.play(*[col.animate.set_color(COLOR_BASE) for col in (m.get_columns()[0], m.get_columns()[2])])
        self.wait(1)

        teorema = Tex(r"Base de $\operatorname{Col}(A)$: las columnas de $A$ (la \textbf{original}) donde hay pivote.", font_size=38, color=COLOR_BASE).to_edge(DOWN, buff=0.9)
        ajustar_al_encuadre(teorema, margen=0.5)
        self.decir("Una base del espacio columna son las columnas de la matriz original, no de la reducida, en las posiciones donde hay pivote. Aquí, la columna uno y la columna tres de a.")
        self.play(FadeIn(teorema))
        self.wait(3)
        self.limpiar(titulo)

        base = VGroup(
            MathTex(r"\operatorname{Col}(A) = \operatorname{gen}\left\{ \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix},\ \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} \right\},\qquad \dim\operatorname{Col}(A) = 2 = \operatorname{rg}(A)", font_size=44, color=COLOR_PIVOTE),
        ).next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(base, margen=0.5)
        rel = VGroup(
            Tex(r"Las otras columnas son combinación de las pivote.", font_size=38),
            MathTex(r"\mathbf{a}_2 = 2\,\mathbf{a}_1,\qquad \mathbf{a}_4 = \mathbf{a}_1 + 2\,\mathbf{a}_3", font_size=48, color=COLOR_SOLUCION),
            Tex(r"Los coeficientes se leen directamente en las columnas de la reducida:", font_size=36, color=COLOR_SECUNDARIO),
            MathTex(r"\begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix} = 2\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \qquad \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} = 1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + 2\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}", font_size=40),
        ).arrange(DOWN, buff=0.45).next_to(base, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(base, rel), margen=0.5)
        self.decir("Así, el espacio columna está generado por los vectores uno, dos, uno y cero, uno, uno, y su dimensión es dos, igual al rango. Las otras dos columnas son combinación de estas: la segunda es el doble de la primera, y la cuarta es la primera más dos veces la tercera. Esos coeficientes se leen directamente en las columnas de la forma reducida.")
        self.play(Write(base))
        self.wait(2)
        for r_ in rel:
            self.play(FadeIn(r_))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Receta")
        receta = VGroup(
            Tex(r"1.\ Reduce $A$ y localiza las columnas con pivote.", font_size=38),
            Tex(r"2.\ Toma esas mismas columnas, pero de la matriz \textbf{original} $A$.", font_size=38),
            Tex(r"3.\ Son una base de $\operatorname{Col}(A)$, y su cantidad es el rango.", font_size=38),
            Tex(r"4.\ Las demás columnas se escriben con las pivote leyendo la reducida.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(receta, margen=0.5)
        self.decir("La receta, en cuatro pasos. Uno: se reduce a y se localizan las columnas con pivote. Dos: se toman esas mismas columnas, pero de la matriz original. Tres: son una base del espacio columna, y su cantidad es el rango. Cuatro: las demás columnas se escriben en función de las pivote leyendo la forma reducida.")
        for r_ in receta:
            self.play(FadeIn(r_))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F14-N3-01",
            VGroup(
                Text("Halla una base de Col(A) y su dimensión:", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}", font_size=52),
                Text("Escribe las demás columnas como combinación de la base.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla una base del espacio columna de esta matriz y su dimensión, y escribe las demás columnas como combinación de la base. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Base de Col(A): las columnas de A donde la reducida tiene pivote.",
                "dim Col(A) = rg(A).",
                "Las otras columnas se leen de la reducida.",
            ],
            "por qué hay que tomar las columnas de la matriz original.",
            voz="En resumen: una base del espacio columna son las columnas de a donde la reducida tiene pivote. Su dimensión es el rango. Y las otras columnas se leen de la reducida. Siguiente: por qué hay que tomar las columnas de la matriz original.",
        )


class PorQueEnLaMatrizOriginal(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 49 · Parte 2", "¿Por qué las columnas de la original?")
        titulo = self.encabezado("Las operaciones por filas cambian el espacio columna")
        m = matriz_con_columnas_marcadas(A, pivotes=(0, 2)).to_edge(LEFT, buff=1.0).shift(UP * 0.3)
        r = matriz_con_columnas_marcadas(R, pivotes=(0, 2)).next_to(m, RIGHT, buff=1.6)
        flecha_r = MathTex(r"\longrightarrow", font_size=48).move_to((m.get_right() + r.get_left()) / 2)
        rot_a = MathTex(r"A", font_size=40).next_to(m, UP, buff=0.3)
        rot_r = MathTex(r"R", font_size=40).next_to(r, UP, buff=0.3)
        contraste = VGroup(
            Tex(r"$\mathbf{a}_1 = (1, 2, 1) \in \operatorname{Col}(A)$,", font_size=38),
            Tex(r"pero $(1, 2, 1) \notin \operatorname{Col}(R)$: todos los vectores de $\operatorname{Col}(R)$ tienen tercera componente $0$.", font_size=34, color=COLOR_ERROR),
            Tex(r"\textbf{$\operatorname{Col}(R) \ne \operatorname{Col}(A)$}: por eso no sirven las columnas de $R$.", font_size=38, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(VGroup(m, r), DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(m, flecha_r, r, rot_a, rot_r, contraste), margen=0.5)
        self.decir("Una advertencia importante. Las operaciones elementales por filas cambian el espacio columna. La columna uno de a, el vector uno, dos, uno, está en el espacio columna de a. Pero no está en el de la reducida, ere: todos los vectores del espacio columna de ere tienen la tercera componente igual a cero. Por eso las columnas de la reducida no sirven como base de a: hay que tomar las de la original.")
        self.play(FadeIn(m), FadeIn(rot_a))
        self.play(Write(flecha_r), FadeIn(r), FadeIn(rot_r))
        for c in contraste:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que sí se conserva: las relaciones entre columnas")
        clave = VGroup(
            MathTex(r"R = EA \quad (E \text{ invertible, producto de operaciones elementales})", font_size=42),
            MathTex(r"A\mathbf{x} = \mathbf{0} \iff EA\mathbf{x} = \mathbf{0} \iff R\mathbf{x} = \mathbf{0}", font_size=48, color=COLOR_PIVOTE),
            parrafo(r"$A$ y $R$ tienen \textbf{el mismo núcleo}: las mismas relaciones", r"$x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n = \mathbf{0}$ entre sus columnas.", font_size=38, sangria=0.5),
            Tex(r"Lo que hay que conservar son las dependencias, y las dependencias se conservan.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(clave, margen=0.5)
        self.decir("Lo que sí se conserva son las relaciones entre las columnas. Reducir es multiplicar por una matriz invertible, ere igual a e por a. Entonces a por equis es cero exactamente cuando ere por equis es cero: a y ere tienen el mismo núcleo, es decir, las mismas relaciones entre sus columnas. Y las dependencias son justo lo que importa para decidir qué columnas sobran.")
        for c in clave:
            self.play(FadeIn(c))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Demostración de la receta")
        demo = VGroup(
            parrafo(r"En $R$, las columnas pivote son $\mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_r$: son independientes,", r"y cada columna libre es combinación de ellas.", font_size=38, sangria=0.5),
            parrafo(r"Como $A$ y $R$ tienen las mismas relaciones entre columnas,", r"lo mismo vale en $A$: las columnas pivote de $A$ son independientes", r"y generan todas las demás.", font_size=38, sangria=0.5),
            Tex(r"Luego son una base de $\operatorname{Col}(A)$ y $\dim\operatorname{Col}(A) = r = \operatorname{rg}(A)$. $\qquad\blacksquare$", font_size=40, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(demo, margen=0.5)
        self.decir("Y de ahí sale la demostración de la receta. En la reducida, las columnas pivote son los vectores e uno, e dos, hasta e erre, claramente independientes, y cada columna libre es combinación de ellas. Como a y ere tienen las mismas relaciones entre columnas, lo mismo vale en a: sus columnas pivote son independientes y generan todas las demás. Por tanto son una base del espacio columna, y la dimensión es erre, el rango.")
        for d in demo:
            self.play(FadeIn(d))
            self.wait(3.2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F14-N3-04",
            VGroup(
                Text("Un estudiante toma las columnas pivote de la reducida como base de Col(A).", font_size=TAM_TEXTO - 2),
                Text("Da un ejemplo de matriz 2×2 en que eso falla, y explica por qué.", font_size=TAM_TEXTO - 2),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: un estudiante toma como base del espacio columna las columnas pivote de la matriz reducida. Da un ejemplo de matriz de dos por dos en el que eso falla, y explica por qué. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Las operaciones por filas cambian Col(A), pero no las relaciones entre columnas.",
                "Por eso se toman las columnas pivote de la original.",
                "Col(A) y Col(R) tienen la misma dimensión, pero no son iguales.",
            ],
            "Lección 50 — el teorema del rango y la nulidad.",
            voz="En resumen: las operaciones por filas cambian el espacio columna, pero no las relaciones entre las columnas; por eso se toman las columnas pivote de la matriz original. Los dos espacios columna tienen la misma dimensión, pero no son iguales. Siguiente: lección cincuenta, el teorema del rango y la nulidad.",
        )
