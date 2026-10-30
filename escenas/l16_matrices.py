"""Lección 16 — Matrices: dimensión, filas, columnas, elementos y tipos.

Escenas (un video cada una):
    QueEsUnaMatriz, TiposDeMatrices

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l16_matrices.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def tarjeta(m: Matrix, nombre: str, condicion: str) -> VGroup:
    return VGroup(
        Text(nombre, font_size=TAM_NOTA + 2, weight="BOLD"),
        m.scale(0.65),
        MathTex(condicion, font_size=30, color=COLOR_SECUNDARIO),
    ).arrange(DOWN, buff=0.25)


class QueEsUnaMatriz(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 16 · Parte 1", "¿Qué es una matriz?")

        # Intuición: una tabla de datos.
        titulo = self.encabezado("Una tabla de números")
        filas_txt = ["Tienda Norte", "Tienda Sur"]
        cols_txt = ["camisas", "pantalones", "zapatos"]
        datos = [[12, 5, 8], [7, 9, 3]]
        tabla = VGroup()
        tabla.add(Text("", font_size=TAM_NOTA))
        for c in cols_txt:
            tabla.add(Text(c, font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP))
        for nombre, fila in zip(filas_txt, datos):
            tabla.add(Text(nombre, font_size=TAM_NOTA, color=COLOR_COEFICIENTE))
            for valor in fila:
                tabla.add(MathTex(str(valor), font_size=44))
        tabla.arrange_in_grid(rows=3, cols=4, buff=(0.9, 0.5))
        self.decir("Una tabla de ventas de una semana: cada fila es una tienda, y cada columna, un producto.")
        self.play(FadeIn(tabla))
        self.pie("Ventas de una semana: cada fila es una tienda, cada columna un producto.", espera=4)
        numeros = VGroup(*[tabla[5 + 4 * i + j] for i in range(2) for j in range(3)])
        etiquetas = VGroup(*[m for m in tabla if m not in numeros])
        m = matriz(datos).scale(1.2)
        self.decir("Si quitamos los rótulos y nos quedamos con los números en su sitio, ordenados, tenemos una matriz.")
        self.play(FadeOut(etiquetas))
        self.play(ReplacementTransform(numeros, VGroup(*m.get_entries())), FadeIn(m.get_brackets()))
        self.consolidar(m)
        self.pie("Si quitamos los rótulos y dejamos solo los números, ordenados, tenemos una MATRIZ.", espera=3)
        self.limpiar(titulo)

        # Definición: filas, columnas, dimensión.
        titulo = self.cambiar_encabezado(titulo, "Filas, columnas y dimensión")
        a = matriz([[4, -1, 0, 7], [2, 5, 3, -2], [1, 0, 6, 8]]).shift(LEFT * 2.6 + DOWN * 0.2)
        nombre = MathTex("A =", font_size=52).next_to(a, LEFT)
        # Columna de rótulos a la derecha, colocada de una vez para que nada pise la matriz.
        definicion = Tex(r"\textbf{Matriz}: tabla rectangular de números\\ ordenados en filas y columnas.", font_size=34)
        rot_fila = Text("fila 2 (horizontal)", font_size=TAM_NOTA, color=COLOR_COEFICIENTE)
        rot_col = Text("columna 3 (vertical)", font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP)
        dimension = MathTex(r"A \text{ es de dimensión } ", "3", r"\times", "4", font_size=44)
        dimension[1].set_color(COLOR_COEFICIENTE)
        dimension[3].set_color(COLOR_TERMINO_INDEP)
        rotulos = VGroup(definicion, rot_fila, rot_col, dimension).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        rotulos.to_edge(RIGHT, buff=0.5).shift(UP * 0.3)
        self.decir("Una matriz es una tabla rectangular de números. Las llamamos con letras mayúsculas, como a.")
        self.play(Write(nombre), Write(a))
        self.play(FadeIn(definicion))
        fila = SurroundingRectangle(a.get_rows()[1], color=COLOR_COEFICIENTE)
        self.decir("Las filas son horizontales.")
        self.play(Create(fila), FadeIn(rot_fila))
        self.wait(1.5)
        columna = SurroundingRectangle(a.get_columns()[2], color=COLOR_TERMINO_INDEP)
        self.decir("Y las columnas, verticales.")
        self.play(Create(columna), FadeIn(rot_col))
        self.wait(1.5)
        self.play(FadeOut(fila), FadeOut(columna))
        llave_m = Brace(a, LEFT, buff=0.15)
        llave_n = Brace(a, DOWN)
        rot_m = MathTex("3", r"\text{ filas}", font_size=34, color=COLOR_COEFICIENTE).next_to(llave_m, LEFT, buff=0.15)
        rot_n = MathTex("4", r"\text{ columnas}", font_size=34, color=COLOR_TERMINO_INDEP).next_to(llave_n, DOWN)
        self.decir("Esta matriz tiene tres filas y cuatro columnas: es de dimensión tres por cuatro. Siempre se dice primero el número de filas, y después el de columnas.")
        self.play(FadeOut(nombre), GrowFromCenter(llave_m), FadeIn(rot_m), GrowFromCenter(llave_n), FadeIn(rot_n))
        self.play(Write(dimension))
        self.pie("Se lee «tres por cuatro»: SIEMPRE primero el número de filas y después el de columnas.", espera=4)
        self.limpiar(titulo)

        # Elemento a_ij.
        titulo = self.cambiar_encabezado(titulo, "El elemento a sub i j")
        a = matriz([[4, -1, 0, 7], [2, 5, 3, -2], [1, 0, 6, 8]]).scale(1.1).shift(LEFT * 2.8 + DOWN * 0.2)
        nombre = MathTex("A =", font_size=52).next_to(a, LEFT)
        self.decir("Cada número de la matriz es un elemento.")
        self.play(FadeIn(nombre), FadeIn(a))
        general = MathTex(
            r"A = \begin{bmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \end{bmatrix}",
            font_size=36,
        ).to_edge(RIGHT, buff=0.6).shift(UP * 1.2)
        self.decir("El elemento a sub i jota está donde se cruzan la fila i y la columna jota: primero la fila, después la columna, como en la lección cuatro.")
        self.play(Write(general))
        self.pie("a_ij es el número de la fila i y la columna j (Lección 4: primero fila, después columna).", espera=2)
        self.decir("a dos tres vale tres. a tres dos vale cero: el orden importa. Y a uno cuatro vale siete.")
        for (i, j), texto in (((1, 2), r"a_{23} = 3"), ((2, 1), r"a_{32} = 0"), ((0, 3), r"a_{14} = 7")):
            cruce = VGroup(
                SurroundingRectangle(a.get_rows()[i], color=COLOR_COEFICIENTE, buff=0.08),
                SurroundingRectangle(a.get_columns()[j], color=COLOR_TERMINO_INDEP, buff=0.08),
            )
            elemento = a.get_rows()[i][j]
            lectura = MathTex(texto, font_size=48, color=COLOR_PIVOTE).next_to(general, DOWN, buff=0.8)
            self.play(Create(cruce))
            self.play(elemento.animate.set_color(COLOR_PIVOTE).scale(1.3), Write(lectura))
            self.wait(1.5)
            self.play(FadeOut(cruce), FadeOut(lectura), elemento.animate.set_color(WHITE).scale(1 / 1.3))
        notacion = MathTex(r"A = [a_{ij}]_{3\times 4}", font_size=48).next_to(general, DOWN, buff=0.8)
        self.decir("También se escribe la matriz entera como a sub i jota, entre corchetes, indicando su dimensión.")
        self.play(Write(notacion))
        self.pie("También se escribe A = [a_ij] indicando la dimensión.", espera=3)
        self.limpiar(titulo)

        # Igualdad de matrices.
        titulo = self.cambiar_encabezado(titulo, "¿Cuándo dos matrices son iguales?")
        bloque = VGroup(
            Tex(r"$A = B$ si tienen la \textbf{misma dimensión} y los \textbf{mismos elementos en las mismas posiciones}.", font_size=36),
            MathTex(r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \neq \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix} \qquad \begin{bmatrix} 1 & 2 \end{bmatrix} \neq \begin{bmatrix} 1 \\ 2 \end{bmatrix}", font_size=44, color=COLOR_ERROR),
            MathTex(r"\begin{bmatrix} x & 2 \\ 3 & y \end{bmatrix} = \begin{bmatrix} 5 & 2 \\ 3 & -1 \end{bmatrix} \;\Longleftrightarrow\; x = 5,\ y = -1", font_size=44, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.7)
        ajustar_al_encuadre(bloque)
        self.decir("Dos matrices son iguales si tienen la misma dimensión, y el mismo número en cada posición.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.5)
        self.decir("Por eso una igualdad de matrices son muchas igualdades de números a la vez: una por posición.")
        self.pie("Una igualdad de matrices son muchas igualdades de números a la vez: una por posición.", espera=3)

        self.ejercicio_propuesto(
            "F05-N1-01",
            VGroup(
                MathTex(r"B = \begin{bmatrix} 3 & -2 & 0 \\ 1 & 7 & -5 \end{bmatrix}", font_size=52),
                Tex(r"a) Dimensión de $B$. \quad b) $b_{12}$, $b_{21}$, $b_{23}$. \quad c) ¿Existe $b_{32}$? ¿Por qué?", font_size=40),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Una matriz es una tabla rectangular de números.",
                "Dimensión m × n: m filas, n columnas (primero filas).",
                "a_ij: elemento de la fila i y la columna j.",
                "A = B: misma dimensión y mismos elementos en cada posición.",
            ],
            "tipos de matrices.",
            voz="En resumen: una matriz es una tabla rectangular de números. Su dimensión, eme por ene, indica eme filas y ene columnas, primero las filas. a i jota es el elemento de la fila i y la columna jota. Y dos matrices son iguales si tienen la misma dimensión y los mismos elementos en cada posición. Siguiente: tipos de matrices.",
        )


class TiposDeMatrices(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 16 · Parte 2", "Tipos de matrices")
        titulo = self.encabezado("Cuadradas y rectangulares")
        cuadrada = matriz([[2, 7, 1], [0, 5, -3], [4, 8, 6]]).scale(1.1).shift(LEFT * 3.5)
        rectangular = matriz([[1, 0, -2, 5], [3, 4, 1, 0]]).scale(1.1).shift(RIGHT * 3)
        rot = VGroup(
            Tex(r"cuadrada: $3\times 3$", font_size=38).next_to(cuadrada, DOWN, buff=0.4),
            Tex(r"rectangular: $2\times 4$", font_size=38).next_to(rectangular, DOWN, buff=0.4),
        )
        self.decir("Si una matriz tiene tantas filas como columnas, es cuadrada. Si no, es rectangular.")
        self.play(FadeIn(cuadrada), FadeIn(rectangular), FadeIn(rot))
        self.pie("Cuadrada: tantas filas como columnas (n × n). Si no, rectangular.", espera=2)
        diagonal = VGroup(*[cuadrada.get_rows()[i][i] for i in range(3)])
        self.decir("En una matriz cuadrada, los elementos con fila igual a columna, a uno uno, a dos dos, y así, forman la diagonal principal.")
        self.play(diagonal.animate.set_color(COLOR_PIVOTE))
        linea = DashedLine(cuadrada.get_rows()[0][0].get_center(), cuadrada.get_rows()[2][2].get_center(), color=COLOR_PIVOTE)
        self.play(Create(linea))
        rot_diag = Tex(r"diagonal principal: $a_{11}, a_{22}, a_{33}$", font_size=36, color=COLOR_PIVOTE).next_to(rot[0], DOWN, buff=0.4)
        self.play(FadeIn(rot_diag))
        self.pie("En una matriz cuadrada, los elementos a_ii (fila = columna) forman la DIAGONAL PRINCIPAL.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Matrices especiales")
        tarjetas = VGroup(
            tarjeta(matriz([[0, 0, 0], [0, 0, 0]]), "nula  O", r"a_{ij} = 0"),
            tarjeta(matriz([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), "identidad  I₃", r"1 \text{ en la diagonal, } 0 \text{ fuera}"),
            tarjeta(matriz([[3, 0, 0], [0, -2, 0], [0, 0, 5]]), "diagonal", r"a_{ij} = 0 \text{ si } i \neq j"),
            tarjeta(matriz([[2, 1, 4], [0, 3, -1], [0, 0, 6]]), "triangular superior", r"a_{ij} = 0 \text{ si } i > j"),
            tarjeta(matriz([[2, 0, 0], [5, 3, 0], [1, -4, 6]]), "triangular inferior", r"a_{ij} = 0 \text{ si } i < j"),
        ).arrange_in_grid(rows=2, cols=3, buff=(0.8, 0.6))
        ajustar_al_encuadre(tarjetas, margen=1.4)  # deja sitio abajo para el pie
        tarjetas.move_to(DOWN * 0.1)
        self.decir("Hay matrices especiales. La matriz nula tiene todo ceros. La identidad, unos en la diagonal y ceros fuera. Una matriz diagonal solo puede tener números distintos de cero en la diagonal. Una triangular superior tiene ceros debajo de la diagonal; una inferior, encima.")
        for t in tarjetas:
            self.play(FadeIn(t, shift=UP * 0.2))
            self.wait(1.8)
        # Resaltar los ceros de las triangulares: zona bajo y sobre la diagonal.
        sup, inf = tarjetas[3][1], tarjetas[4][1]
        ceros_sup = VGroup(sup.get_rows()[1][0], sup.get_rows()[2][0], sup.get_rows()[2][1])
        ceros_inf = VGroup(inf.get_rows()[0][1], inf.get_rows()[0][2], inf.get_rows()[1][2])
        self.decir("Fíjate en dónde están los ceros de cada triangular.")
        self.play(ceros_sup.animate.set_color(COLOR_ERROR), ceros_inf.animate.set_color(COLOR_ERROR))
        self.pie(
            "Triangular superior: ceros DEBAJO de la diagonal. Triangular inferior: ceros ENCIMA.\n"
            "Serán protagonistas de la eliminación de Gauss (forma escalonada) y de la factorización LU.",
            espera=6,
        )
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Una matriz puede ser de varios tipos a la vez")
        bloque = VGroup(
            Tex(r"La identidad es diagonal, triangular superior \emph{y} triangular inferior.", font_size=38),
            Tex(r"Una matriz diagonal es triangular superior e inferior a la vez.", font_size=38),
            Tex(r"La matriz nula $m\times n$ existe para cualquier dimensión; la identidad solo es cuadrada.", font_size=38),
        ).arrange(DOWN, buff=0.5)
        self.decir("Una misma matriz puede pertenecer a varios tipos a la vez: la identidad es diagonal, triangular superior y triangular inferior.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F05-N1-02",
            VGroup(
                Text("Clasifica cada matriz (puede tener varios tipos):", font_size=TAM_TEXTO),
                MathTex(
                    r"P = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad Q = \begin{bmatrix} 0 & 0 \\ 4 & 2 \end{bmatrix} \quad R = \begin{bmatrix} 5 & 1 & 0 \end{bmatrix} \quad S = \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}",
                    font_size=44,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Cuadrada (n × n) o rectangular. Diagonal principal: a₁₁, a₂₂, …",
                "Nula O, identidad I, diagonal, triangular superior e inferior.",
                "Una matriz puede pertenecer a varios tipos.",
            ],
            "Lección 17 — vectores.",
            voz="En resumen: una matriz es cuadrada si tiene tantas filas como columnas, y si no, rectangular. Su diagonal principal la forman a uno uno, a dos dos, y así. Las matrices especiales son la nula, la identidad, la diagonal y las triangulares superior e inferior. Y una matriz puede pertenecer a varios tipos. Siguiente: lección diecisiete, vectores.",
        )
