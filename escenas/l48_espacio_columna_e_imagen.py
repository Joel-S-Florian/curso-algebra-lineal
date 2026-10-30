"""Lección 48 — Espacio columna e imagen.

Escenas (un video cada una):
    AxEsCombinacionDeColumnas, ExisteSolucionSiiBEnCol

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l48_espacio_columna_e_imagen.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import panel_derecha, EscenaCurso, ajustar_al_encuadre, ejes_iguales, flecha, parrafo, recta_general  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_U, COLOR_V, COLOR_W = COLORES_ECUACIONES
A_TEX = r"\begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}"


class AxEsCombinacionDeColumnas(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 48 · Parte 1", "A x es una combinación de las columnas")
        titulo = self.encabezado("Leer el producto por columnas")
        producto = MathTex(
            r"A\mathbf{x} = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \dots + x_n\mathbf{a}_n",
            font_size=48,
        ).next_to(titulo, DOWN, buff=0.8)
        nota = Tex(r"Los números de $\mathbf{x}$ son los \textbf{coeficientes} de una combinación lineal de las columnas.", font_size=38, color=COLOR_PIVOTE).next_to(producto, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(producto, nota), margen=0.5)
        self.decir("Recordemos, de la lección diecinueve, cómo se multiplica una matriz por un vector, pero leyendo por columnas. A por equis es equis uno por la primera columna, más equis dos por la segunda, y así hasta la última. Es una combinación lineal de las columnas de a, y los números de equis son los coeficientes.")
        self.play(Write(producto))
        self.wait(1.5)
        self.play(FadeIn(nota))
        self.wait(2)
        self.limpiar(titulo)

        ejemplo = VGroup(
            MathTex(r"A\mathbf{x} = 2\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} - 1\begin{bmatrix} 2 \\ 4 \\ 2 \end{bmatrix} + 3\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 1 \\ 4 \\ 3 \end{bmatrix}", font_size=44),
            MathTex(r"= \begin{bmatrix} 2 - 2 + 0 + 1 \\ 4 - 4 + 3 + 4 \\ 2 - 2 + 3 + 3 \end{bmatrix} = \begin{bmatrix} 1 \\ 7 \\ 6 \end{bmatrix}", font_size=44, color=COLOR_PIVOTE),
            Tex(r"con $A = " + A_TEX.replace("\\\\", "\\\\") + r"$ y $\mathbf{x} = (2, -1, 3, 1)$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(ejemplo, margen=0.5)
        self.decir("Con la matriz de siempre y el vector dos, menos uno, tres, uno, el producto es dos veces la columna uno, menos la columna dos, más tres veces la columna tres, más la columna cuatro. Sumando componente a componente, sale el vector uno, siete, seis. Da igual hacerlo por filas o por columnas: el resultado es el mismo.")
        self.play(Write(ejemplo[0]))
        self.wait(2)
        self.play(Write(ejemplo[1]))
        self.wait(2)
        self.play(FadeIn(ejemplo[2]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El espacio columna")
        definicion = VGroup(
            parrafo(r"El \textbf{espacio columna} de $A$ es el espacio generado por sus columnas:", font_size=40, sangria=0.4),
            MathTex(r"\operatorname{Col}(A) = \operatorname{gen}\{\mathbf{a}_1, \dots, \mathbf{a}_n\} = \{\, A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n \,\}", font_size=48, color=COLOR_PIVOTE),
            parrafo(r"Las dos descripciones coinciden porque $A\mathbf{x}$ \textbf{es} una combinación de las columnas,", r"con coeficientes $x_1, \dots, x_n$.", font_size=38, sangria=0.4),
            Tex(r"Es un subespacio de $\mathbb{R}^m$ (las ecuaciones), no de $\mathbb{R}^n$.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(definicion, margen=0.5)
        self.decir("El espacio columna de a es el espacio generado por sus columnas. Y es lo mismo que el conjunto de todos los productos a por equis, con equis cualquiera, porque cada producto es una combinación de las columnas. Es un subespacio del espacio de eme dimensiones, el de las ecuaciones, mientras que el núcleo vivía en el de las incógnitas.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un ejemplo sencillo")
        p = ejes_iguales((-3, 5), (-2, 5), unidad=0.8).to_edge(LEFT, buff=0.6).shift(DOWN * 0.35)
        a1, a2 = flecha(p, 1, 2, COLOR_U), flecha(p, 2, 4, COLOR_V)
        recta = recta_general(p, 2, -1, 0, color=COLOR_PIVOTE, stroke_width=6)
        texto = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}", font_size=46),
            MathTex(r"A\mathbf{x} = (x_1 + 2x_2)\begin{bmatrix} 1 \\ 2 \end{bmatrix}", font_size=44),
            Tex(r"$\operatorname{Col}(A)$: la recta $y = 2x$,", font_size=38, color=COLOR_PIVOTE),
            Tex(r"aunque haya dos columnas.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=0.5).shift(UP * 0.5)
        panel_derecha(texto)
        ajustar_al_encuadre(texto, margen=0.5)
        self.decir("Con la matriz uno, dos; dos, cuatro, las dos columnas apuntan en la misma dirección. Cualquier producto a por equis es un múltiplo del vector uno, dos. El espacio columna es la recta y igual a dos equis, aunque la matriz tenga dos columnas.")
        self.play(Create(p))
        self.play(GrowArrow(a1), GrowArrow(a2))
        self.play(Create(recta), FadeIn(texto))
        self.wait(3)

        self.ejercicio_propuesto(
            "F14-N1-01",
            VGroup(
                Text("Calcula A x como combinación de las columnas:", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix},\quad \mathbf{x} = \begin{bmatrix} 3 \\ -1 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: calcula el producto de esta matriz por este vector, como una combinación de las columnas. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "A x = x₁a₁ + … + xnan: combinación de las columnas.",
                "Col(A) = gen de las columnas = { A x }.",
                "Col(A) es un subespacio de ℝᵐ.",
            ],
            "cuándo A x = b tiene solución: b en Col(A).",
            voz="En resumen: a por equis es una combinación de las columnas de a. El espacio columna es el generado por las columnas, que es lo mismo que el conjunto de todos los productos a por equis, y vive en el espacio de eme dimensiones. Siguiente: cuándo a por equis igual a be tiene solución.",
        )


class ExisteSolucionSiiBEnCol(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 48 · Parte 2", "¿Cuándo tiene solución A x = b?")
        titulo = self.encabezado("Existe solución si y solo si b está en Col(A)")
        regla = VGroup(
            MathTex(r"A\mathbf{x} = \mathbf{b} \text{ tiene solución} \iff \mathbf{b} \in \operatorname{Col}(A)", font_size=52, color=COLOR_PIVOTE),
            parrafo(r"Resolver el sistema es \textbf{buscar los coeficientes} $x_1, \dots, x_n$ con los que", r"las columnas se combinan para dar $\mathbf{b}$.", font_size=38, sangria=0.5),
            MathTex(r"\iff \operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]", font_size=48),
            Tex(r"(Rouché-Frobenius, L40: añadir $\mathbf{b}$ no debe crear un pivote nuevo.)", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(regla, margen=0.5)
        self.decir("Ahora la respuesta a la pregunta central del curso. El sistema a por equis igual a be tiene solución si y solo si be pertenece al espacio columna de a. Resolver el sistema es buscar los coeficientes con los que las columnas se combinan para dar be. Y esto equivale a que el rango de a sea igual al de la matriz aumentada: añadir be no debe crear un pivote nuevo.")
        for r in regla:
            self.play(FadeIn(r))
            self.wait(2.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "En el plano")
        p = ejes_iguales((-3, 5), (-2, 7), unidad=0.62).to_edge(LEFT, buff=0.6).shift(DOWN * 0.35)
        recta = recta_general(p, 2, -1, 0, color=COLOR_PIVOTE, stroke_width=6)
        b_si, b_no = flecha(p, 1.5, 3, COLOR_SOLUCION), flecha(p, 3, 0, COLOR_ERROR)
        texto = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}", font_size=46),
            MathTex(r"\operatorname{Col}(A): y = 2x", font_size=40, color=COLOR_PIVOTE),
            Tex(r"$\mathbf{b} = (3, 6)$: sobre la recta,\\ \textbf{hay solución}.", font_size=36, color=COLOR_SOLUCION),
            Tex(r"$\mathbf{b}' = (1, 0)$: fuera de la recta,\\ \textbf{no hay solución}.", font_size=36, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=0.5).shift(UP * 0.3)
        panel_derecha(texto)
        ajustar_al_encuadre(texto, margen=0.5)
        punto_si = Dot(p.c2p(3, 6), color=COLOR_SOLUCION, radius=0.1)
        punto_no = Dot(p.c2p(1, 0), color=COLOR_ERROR, radius=0.1)
        self.decir("En el plano, con la matriz de antes, el espacio columna es la recta y igual a dos equis. El vector tres, seis está sobre la recta: a por equis igual a ese vector tiene solución. El vector uno, cero queda fuera de la recta: ninguna combinación de las columnas lo alcanza, y el sistema es incompatible.")
        self.play(Create(p))
        self.play(Create(recta), FadeIn(texto[:2]))
        self.play(FadeIn(punto_si, scale=2), FadeIn(texto[2]))
        self.wait(1.5)
        self.play(FadeIn(punto_no, scale=2), FadeIn(texto[3]))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Con la matriz de tres por cuatro")
        caso = VGroup(
            MathTex(r"\mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix} = 1\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} \in \operatorname{Col}(A)", font_size=44, color=COLOR_SOLUCION),
            MathTex(r"\mathbf{b}' = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}:\ \operatorname{rg}(A) = 2,\ \operatorname{rg}[A \mid \mathbf{b}'] = 3", font_size=44, color=COLOR_ERROR),
            Tex(r"$\mathbf{b}' \notin \operatorname{Col}(A)$: el sistema es incompatible.", font_size=38, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(caso, margen=0.5)
        self.decir("Con la matriz de tres por cuatro: el vector uno, tres, dos es la columna uno más la columna tres, así que está en el espacio columna, y el sistema es compatible. En cambio, con el vector uno, cero, cero el rango de a es dos, pero el de la aumentada es tres: no está en el espacio columna, y el sistema es incompatible.")
        for c in caso:
            self.play(FadeIn(c))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La imagen de una transformación")
        imagen = VGroup(
            MathTex(r"T(\mathbf{x}) = A\mathbf{x}, \qquad T : \mathbb{R}^n \to \mathbb{R}^m", font_size=50),
            MathTex(r"\operatorname{Im}(T) = \{\, T(\mathbf{x}) : \mathbf{x} \in \mathbb{R}^n \,\} = \operatorname{Col}(A)", font_size=48, color=COLOR_PIVOTE),
            parrafo(r"La \textbf{imagen} es el conjunto de los vectores que la transformación puede alcanzar.", r"Que $A\mathbf{x} = \mathbf{b}$ tenga solución es que $\mathbf{b}$ sea alcanzable.", font_size=38, sangria=0.4),
            Tex(r"Si $\operatorname{Col}(A) = \mathbb{R}^m$, el sistema tiene solución para \textbf{todo} $\mathbf{b}$.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(imagen, margen=0.5)
        self.decir("Lo mismo se dice con transformaciones, como en la lección veintiuno. La imagen de la transformación te de equis igual a a por equis es el conjunto de todos los vectores que puede alcanzar, y es exactamente el espacio columna. Que a por equis igual a be tenga solución es que be sea alcanzable. Y si el espacio columna es todo el espacio de eme dimensiones, el sistema tiene solución para cualquier be.")
        for i in imagen:
            self.play(FadeIn(i))
            self.wait(2.8)
        self.wait(1)

        self.ejercicio_propuesto(
            "F14-N2-02",
            VGroup(
                Text("¿Tiene solución A x = b? Responde mirando los rangos:", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix},\quad \mathbf{b}_1 = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix},\quad \mathbf{b}_2 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}", font_size=40),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: decide, mirando los rangos, si tiene solución el sistema para cada uno de estos dos vectores. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "A x = b tiene solución ⇔ b ∈ Col(A).",
                "⇔ rg(A) = rg[A | b].",
                "Imagen de T(x) = A x = Col(A): lo que se puede alcanzar.",
            ],
            "Lección 49 — una base del espacio columna.",
            voz="En resumen: a por equis igual a be tiene solución exactamente cuando be está en el espacio columna, lo que equivale a que los rangos coincidan. El espacio columna es la imagen de la transformación: lo que se puede alcanzar. Siguiente: lección cuarenta y nueve, una base del espacio columna.",
        )
