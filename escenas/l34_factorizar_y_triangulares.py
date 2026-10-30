"""Lección 34 — Factorizar, matrices triangulares y matrices elementales.

Escenas (un video cada una):
    QueEsFactorizar, TriangularesYSustitucion, MatricesElementales

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l34_factorizar_y_triangulares.py -a

Ejemplo común de la Unidad 6 (es el sistema de la L26, con solución (1, -1, 2)):
    A = [[1, 2, -1], [2, 3, 1], [-1, 1, 2]],  b = (-3, 1, 2)
    L = [[1, 0, 0], [2, 1, 0], [-1, -3, 1]],   U = [[1, 2, -1], [0, -1, 3], [0, 0, 10]]
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A = [[1, 2, -1], [2, 3, 1], [-1, 1, 2]]
L = [[1, 0, 0], [2, 1, 0], [-1, -3, 1]]
U = [[1, 2, -1], [0, -1, 3], [0, 0, 10]]


def fila_de(*partes, buff=0.3):
    return VGroup(*partes).arrange(RIGHT, buff=buff)


def mat_L(escala=0.8):
    """L con los multiplicadores (debajo de la diagonal) en violeta y el resto en gris."""
    m = matriz(L, h_buff=1.0).scale(escala)
    for k, e in enumerate(m.get_entries()):
        i, j = divmod(k, 3)
        e.set_color(COLOR_OPERACION if i > j else COLOR_SECUNDARIO)
    return m


def mat_U(escala=0.8):
    m = matriz(U, h_buff=1.0).scale(escala)
    for k, e in enumerate(m.get_entries()):
        i, j = divmod(k, 3)
        e.set_color(COLOR_PIVOTE if i == j else (WHITE if j > i else COLOR_SECUNDARIO))
    return m


class QueEsFactorizar(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 34 · Parte 1", "¿Qué es factorizar?")
        titulo = self.encabezado("Escribir algo como un producto de piezas simples")
        numeros = VGroup(
            MathTex(r"12 = 3 \cdot 4", font_size=64),
            MathTex(r"x^2 - 1 = (x - 1)(x + 1)", font_size=64),
        ).arrange(DOWN, buff=0.7).shift(UP * 0.3)
        self.decir("Factorizar es escribir algo como un producto de piezas más simples. Doce es tres por cuatro. Equis al cuadrado menos uno es equis menos uno, por equis más uno.")
        self.play(Write(numeros[0]))
        self.wait(1)
        self.play(Write(numeros[1]))
        self.wait(1)
        pregunta = Text("¿Y una matriz?", font_size=44, color=COLOR_PIVOTE).next_to(numeros, DOWN, buff=0.8)
        self.decir("¿Y se puede hacer con una matriz? Sí: y la factorización que veremos viene directamente de la eliminación de Gauss.")
        self.play(FadeIn(pregunta))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "A = L U")
        a = matriz(A, h_buff=1.0).scale(0.8)
        a.get_entries().set_color(COLOR_COEFICIENTE)
        ml, mu = mat_L(), mat_U()
        eq = fila_de(MathTex("A", font_size=56), MathTex("=", font_size=52), ml, MathTex(r"\cdot", font_size=52), mu).shift(UP * 0.2)
        eq_a = fila_de(a, MathTex("=", font_size=52), ml.copy(), MathTex(r"\cdot", font_size=52), mu.copy()).shift(UP * 0.2)
        rotulos = VGroup(
            MathTex("L", font_size=44, color=COLOR_OPERACION).next_to(eq_a[2], DOWN, buff=0.35),
            MathTex("U", font_size=44, color=COLOR_PIVOTE).next_to(eq_a[4], DOWN, buff=0.35),
            MathTex("A", font_size=44, color=COLOR_COEFICIENTE).next_to(a, DOWN, buff=0.35),
        )
        self.decir("Esta es la matriz de coeficientes del sistema de la lección veintiséis. Se puede escribir como el producto de dos matrices triangulares: ele, y u.")
        self.play(FadeIn(eq_a))
        self.play(FadeIn(rotulos))
        self.wait(1)
        definiciones = VGroup(
            parrafo(r"$L$ es \textbf{triangular inferior} con unos en la diagonal:", r"ceros por encima de la diagonal.", font_size=34, color=COLOR_OPERACION, sangria=0.4),
            parrafo(r"$U$ es \textbf{triangular superior}: ceros por debajo de la diagonal.", r"Es la forma escalonada de $A$.", font_size=34, color=COLOR_PIVOTE, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(DOWN, buff=0.45)
        ajustar_al_encuadre(definiciones, margen=0.5)
        self.decir("Ele es triangular inferior, con unos en la diagonal. U es triangular superior: es, ni más ni menos, la forma escalonada de a.")
        self.play(FadeIn(definiciones))
        self.wait(2)
        self.play(FadeOut(definiciones))
        self.limpiar(titulo, eq_a, rotulos)

        # Comprobar una entrada: (fila 3 de L) · (columna 2 de U) = a_32.
        fila3 = SurroundingRectangle(eq_a[2].get_rows()[2], color=COLOR_OPERACION)
        col2 = SurroundingRectangle(eq_a[4].get_columns()[1], color=COLOR_PIVOTE)
        entrada = SurroundingRectangle(eq_a[0].get_entries()[7], color=COLOR_SOLUCION)
        cuenta = MathTex(r"(-1)\cdot 2 + (-3)\cdot(-1) + 1\cdot 0 = -2 + 3 + 0 = 1 = a_{32}\ \checkmark", font_size=42, color=COLOR_SOLUCION).to_edge(DOWN, buff=0.7)
        ajustar_al_encuadre(cuenta, margen=0.5)
        self.decir("Comprobemos una entrada. La fila tres de ele por la columna dos de u: menos uno por dos, más menos tres por menos uno, más uno por cero. Menos dos, más tres: uno. Es la entrada tres dos de a.")
        self.play(Create(fila3), Create(col2), Create(entrada))
        self.play(Write(cuenta))
        self.wait(2)
        self.play(FadeOut(fila3), FadeOut(col2), FadeOut(entrada), FadeOut(cuenta))
        nota = parrafo(
            r"Los números violetas de $L$ no son casualidad: son los \textbf{multiplicadores}",
            r"de la eliminación de Gauss. Lo veremos en la L35.",
            font_size=36, color=COLOR_OPERACION, sangria=0.4,
        ).to_edge(DOWN, buff=0.7)
        ajustar_al_encuadre(nota, margen=0.5)
        self.decir("Los números violetas de ele no son casualidad: son los multiplicadores de la eliminación de Gauss. Lo veremos en la próxima lección.")
        self.play(FadeIn(nota))
        self.wait(2)

        self.ejercicio_propuesto(
            "F10-N1-01",
            VGroup(
                Text("Comprueba que A = L U, calculando el producto:", font_size=TAM_TEXTO),
                MathTex(r"\begin{bmatrix} 2 & 1 \\ 6 & 7 \end{bmatrix} \overset{?}{=} \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \\ 0 & 4 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: comprueba que esta matriz es el producto de ele por u, calculando el producto. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Factorizar es escribir como producto de piezas simples.",
                "A = L U: L triangular inferior con unos en la diagonal, U triangular superior.",
                "U es la forma escalonada; los números de L son los multiplicadores de Gauss.",
            ],
            "las matrices triangulares y por qué son tan cómodas.",
            voz="En resumen: factorizar es escribir como producto de piezas simples. A igual a ele u, con ele triangular inferior, de unos en la diagonal, y u triangular superior. U es la forma escalonada, y los números de ele son los multiplicadores de Gauss. Siguiente: las matrices triangulares, y por qué son tan cómodas.",
        )


class TriangularesYSustitucion(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 34 · Parte 2", "Matrices triangulares")
        titulo = self.encabezado("Por qué las triangulares son cómodas")
        sup = matriz([[1, 2, -1], [0, -1, 3], [0, 0, 10]], h_buff=1.0).scale(0.8)
        inf = matriz([[1, 0, 0], [2, 1, 0], [-1, -3, 1]], h_buff=1.0).scale(0.8)
        for m, e_rel in ((sup, lambda i, j: j >= i), (inf, lambda i, j: i >= j)):
            for k, e in enumerate(m.get_entries()):
                i, j = divmod(k, 3)
                e.set_color(WHITE if e_rel(i, j) else COLOR_SECUNDARIO)
        sup_t = Text("triangular superior", font_size=TAM_NOTA + 2, color=COLOR_PIVOTE).next_to(sup, UP, buff=0.35)
        inf_t = Text("triangular inferior", font_size=TAM_NOTA + 2, color=COLOR_OPERACION).next_to(inf, UP, buff=0.35)
        izq, der = VGroup(sup_t, sup), VGroup(inf_t, inf)
        VGroup(izq, der).arrange(RIGHT, buff=1.8).shift(DOWN * 0.1)
        self.decir("Una matriz es triangular superior si todo lo que hay debajo de la diagonal son ceros. Y triangular inferior si son ceros todo lo que hay por encima.")
        self.play(FadeIn(izq))
        self.play(FadeIn(der))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un sistema triangular se resuelve sin eliminar")
        sistema = MathTex(r"\begin{cases} x + 2y - z = -3 \\ -y + 3z = 7 \\ 10z = 20 \end{cases}", font_size=46).to_edge(LEFT, buff=1.0).shift(UP * 0.7)
        pasos = VGroup(
            MathTex(r"10z = 20 \;\Rightarrow\; z = 2", font_size=40),
            MathTex(r"-y + 3\cdot 2 = 7 \;\Rightarrow\; y = -1", font_size=40),
            MathTex(r"x + 2(-1) - 2 = -3 \;\Rightarrow\; x = 1", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(sistema, RIGHT, buff=1.0)
        ajustar_al_encuadre(VGroup(sistema, pasos), margen=0.5)
        self.decir("Un sistema con matriz triangular superior se resuelve sin eliminar nada: la última ecuación tiene una sola incógnita. Diez zeta igual a veinte: zeta vale dos.")
        self.play(Write(sistema))
        self.play(Write(pasos[0]))
        self.decir("Sustituyendo hacia atrás: menos ye más seis igual a siete, ye vale menos uno. Y equis más dos por menos uno, menos dos, igual a menos tres: equis vale uno.")
        self.play(Write(pasos[1]))
        self.play(Write(pasos[2]))
        regla = Tex(r"Hacia atrás: de la \textbf{última} ecuación a la primera.", font_size=38, color=COLOR_PIVOTE).next_to(pasos, DOWN, buff=0.7)
        self.play(FadeIn(regla))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Y uno triangular inferior, hacia adelante")
        sistema = MathTex(r"\begin{cases} y_1 = -3 \\ 2y_1 + y_2 = 1 \\ -y_1 - 3y_2 + y_3 = 2 \end{cases}", font_size=46).to_edge(LEFT, buff=1.0).shift(UP * 0.7)
        pasos = VGroup(
            MathTex(r"y_1 = -3", font_size=40),
            MathTex(r"2(-3) + y_2 = 1 \;\Rightarrow\; y_2 = 7", font_size=40),
            MathTex(r"-(-3) - 3\cdot 7 + y_3 = 2 \;\Rightarrow\; y_3 = 20", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(sistema, RIGHT, buff=1.0)
        ajustar_al_encuadre(VGroup(sistema, pasos), margen=0.5)
        self.decir("Si la matriz es triangular inferior, se hace al revés: la primera ecuación tiene una sola incógnita. Ye uno vale menos tres.")
        self.play(Write(sistema))
        self.play(Write(pasos[0]))
        self.decir("Con ella, la segunda da ye dos igual a siete. Y la tercera, ye tres igual a veinte. Es la sustitución hacia adelante.")
        self.play(Write(pasos[1]))
        self.play(Write(pasos[2]))
        regla = Tex(r"Hacia adelante: de la \textbf{primera} ecuación a la última.", font_size=38, color=COLOR_OPERACION).next_to(pasos, DOWN, buff=0.7)
        self.play(FadeIn(regla))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué cuesta y qué se conserva")
        hechos = VGroup(
            Tex(r"Resolver un sistema triangular $n\times n$ cuesta unas $\frac{n^2}{2}$ multiplicaciones: mucho menos que $\frac{n^3}{3}$.", font_size=36),
            Tex(r"El producto de dos triangulares inferiores es triangular inferior (y de unos en la diagonal, si ambas los tienen).", font_size=36),
            Tex(r"Una triangular inferior con unos en la diagonal tiene inversa, y también es triangular inferior con unos.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(hechos)
        self.decir("Tres hechos que usaremos. Resolver un sistema triangular de ene por ene cuesta unas ene cuadrado entre dos multiplicaciones: mucho menos que ene cubo entre tres. El producto de dos triangulares inferiores es triangular inferior. Y una triangular inferior con unos en la diagonal tiene inversa, que es del mismo tipo.")
        for h in hechos:
            self.play(FadeIn(h))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N2-01",
            VGroup(
                Text("Resuelve por sustitución, diciendo si es hacia adelante o hacia atrás:", font_size=TAM_TEXTO),
                MathTex(r"\text{a) } \begin{cases} 2x = 6 \\ x + 3y = 5 \end{cases} \qquad \text{b) } \begin{cases} x - y + 2z = 3 \\ 4y - z = 7 \\ 2z = 6 \end{cases}", font_size=40),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: resuelve estos dos sistemas triangulares por sustitución, diciendo en cada caso si es hacia adelante o hacia atrás. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Triangular superior: ceros debajo de la diagonal. Inferior: ceros encima.",
                "Superior: sustitución hacia atrás. Inferior: hacia adelante.",
                "Coste de un sistema triangular: unas n²/2 multiplicaciones.",
            ],
            "las matrices elementales.",
            voz="En resumen: una matriz triangular superior tiene ceros debajo de la diagonal, y una inferior, encima. Los sistemas con matriz superior se resuelven hacia atrás, y con matriz inferior, hacia adelante, con unas ene cuadrado entre dos multiplicaciones. Siguiente: las matrices elementales.",
        )


class MatricesElementales(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 34 · Parte 3", "Matrices elementales")
        titulo = self.encabezado("Una operación por filas es un producto")
        a = matriz(A, h_buff=1.0).scale(0.78)
        a.get_entries().set_color(COLOR_COEFICIENTE)
        e21 = matriz([[1, 0, 0], [-2, 1, 0], [0, 0, 1]], h_buff=1.0).scale(0.78)
        for k, e in enumerate(e21.get_entries()):
            e.set_color(COLOR_OPERACION if k == 3 else COLOR_SECUNDARIO)
        r1 = matriz([[1, 2, -1], [0, -1, 3], [-1, 1, 2]], h_buff=1.0).scale(0.78)
        eq = fila_de(e21, a, MathTex("=", font_size=52), r1, buff=0.3).shift(UP * 0.7)
        rot = MathTex(r"E_{21}\,A \quad\text{hace}\quad R_2 \leftarrow R_2 - 2R_1", font_size=40, color=COLOR_OPERACION).next_to(eq, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(eq, rot), margen=0.5)
        self.decir("Toda operación elemental por filas se puede hacer multiplicando por una matriz. Esta matriz, la identidad con un menos dos en la fila dos, columna uno, multiplica por la izquierda a nuestra matriz a. El resultado es restarle a la fila dos el doble de la fila uno.")
        self.play(FadeIn(e21), FadeIn(a), FadeIn(eq[2]))
        self.play(FadeIn(r1))
        self.play(FadeIn(rot))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Una por cada operación de la eliminación")
        e31 = MathTex(r"E_{31} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}", font_size=40)
        e32 = MathTex(r"E_{32} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix}", font_size=40)
        e21t = MathTex(r"E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}", font_size=40)
        ops = VGroup(
            MathTex(r"R_2 \leftarrow R_2 - 2R_1", font_size=34, color=COLOR_OPERACION),
            MathTex(r"R_3 \leftarrow R_3 + R_1", font_size=34, color=COLOR_OPERACION),
            MathTex(r"R_3 \leftarrow R_3 + 3R_2", font_size=34, color=COLOR_OPERACION),
        )
        columnas = VGroup(*[VGroup(m, o).arrange(DOWN, buff=0.3) for m, o in zip((e21t, e31, e32), ops)]).arrange(RIGHT, buff=0.7).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(columnas, margen=0.5)
        self.decir("La eliminación de la lección veintiséis usa tres operaciones. Cada una es una matriz elemental. Restar dos veces la fila uno a la dos: e dos uno. Sumar la fila uno a la tres: e tres uno. Y sumar tres veces la fila dos a la tres: e tres dos.")
        for c in columnas:
            self.play(FadeIn(c))
            self.wait(1.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Encadenadas, dan U")
        producto = MathTex(r"E_{32}\,E_{31}\,E_{21}\,A = U", font_size=60, color=COLOR_PIVOTE).next_to(titulo, DOWN, buff=0.6)
        pasos = VGroup(
            MathTex(r"E_{21}A = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ -1 & 1 & 2 \end{bmatrix}", font_size=38),
            MathTex(r"E_{31}E_{21}A = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 3 & 1 \end{bmatrix}", font_size=38),
            MathTex(r"E_{32}E_{31}E_{21}A = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 10 \end{bmatrix} = U", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(producto, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(producto, pasos), margen=0.5)
        self.decir("Aplicadas una tras otra, de derecha a izquierda, llevan a a su forma escalonada u. E dos uno por a da esta matriz. Después, e tres uno. Y por último, e tres dos, que deja la matriz triangular superior u.")
        self.play(Write(producto))
        for p in pasos:
            self.play(FadeIn(p))
            self.wait(2)
        self.wait(1)
        nota = Tex(r"Despejando $A$ aparecerá $L$: es el producto de las inversas (L35).", font_size=38, color=COLOR_OPERACION).to_edge(DOWN, buff=0.7)
        self.decir("Despejando a, aparecerá ele: será el producto de las inversas de estas matrices. Lo veremos en la próxima lección.")
        self.play(FadeIn(nota))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Los tres tipos")
        tipos = VGroup(
            parrafo(r"\textbf{Intercambio:} la identidad con las filas $i$ y $j$ intercambiadas.", r"$P_{ij}A$ intercambia las filas $i$ y $j$ de $A$.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{Escalado:} la identidad con $k \ne 0$ en la posición $(i, i)$.", r"$D_i(k)A$ multiplica la fila $i$ por $k$.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{Reemplazo:} la identidad con $k$ en la posición $(i, j)$.", r"$E_{ij}(k)A$ hace $R_i \leftarrow R_i + k\,R_j$.", font_size=34, sangria=0.5),
            Tex(r"La inversa de cada una es del mismo tipo: $P_{ij}^{-1} = P_{ij}$, $D_i(k)^{-1} = D_i(1/k)$, $E_{ij}(k)^{-1} = E_{ij}(-k)$.", font_size=34, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(tipos)
        self.decir("Hay tres tipos de matrices elementales, una por cada operación. Intercambio: la identidad con dos filas intercambiadas. Escalado: la identidad con un número ka distinto de cero en la diagonal. Y reemplazo: la identidad con un número en una posición fuera de la diagonal. La inversa de cada una es del mismo tipo: deshace la operación.")
        for t in tipos:
            self.play(FadeIn(t))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N2-02",
            VGroup(
                Text("Escribe la matriz elemental E de 3 × 3 tal que E A hace R₃ ← R₃ − 4R₁,", font_size=TAM_TEXTO),
                Text("y calcula su inversa. Comprueba el efecto sobre una matriz A cualquiera.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: escribe la matriz elemental de tres por tres que hace erre tres igual a erre tres menos cuatro erre uno, y calcula su inversa. Comprueba su efecto sobre una matriz cualquiera. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Cada operación por filas es multiplicar por la izquierda por una matriz elemental.",
                "La eliminación completa: E₃₂ E₃₁ E₂₁ A = U.",
                "La inversa de una elemental es del mismo tipo (deshace la operación).",
            ],
            "Lección 35 — de dónde sale A = LU.",
            voz="En resumen: cada operación por filas es multiplicar por la izquierda por una matriz elemental. La eliminación completa es e tres dos, por e tres uno, por e dos uno, por a, igual a u. Y la inversa de una elemental es del mismo tipo: deshace la operación. Siguiente: lección treinta y cinco, de dónde sale a igual a ele u.",
        )
