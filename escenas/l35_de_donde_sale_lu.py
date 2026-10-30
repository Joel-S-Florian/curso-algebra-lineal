"""Lección 35 — De dónde sale A = LU.

Escenas (un video cada una):
    LosMultiplicadoresSeGuardan, ConstruirLyU

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l35_de_donde_sale_lu.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, matriz, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def mat_l(datos, escala=0.8, resaltar=None):
    """L con los multiplicadores en violeta (el recién anotado, en amarillo) y los demás números en gris."""
    m = matriz(datos, h_buff=1.0).scale(escala)
    for k, e in enumerate(m.get_entries()):
        i, j = divmod(k, 3)
        e.set_color(COLOR_PIVOTE if (i, j) == resaltar else (COLOR_OPERACION if i > j and datos[i][j] != 0 else COLOR_SECUNDARIO))
    return m


class LosMultiplicadoresSeGuardan(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 35 · Parte 1", "Los multiplicadores se guardan")
        titulo = self.encabezado("Eliminar y, a la vez, anotar los multiplicadores")
        m = matriz_gauss([[1, 2, -1, -3], [2, 3, 1, 1], [-1, 1, 2, 2]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        l = mat_l([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).move_to(RIGHT * 4.3 + DOWN * 1.4)
        rotulo_l = MathTex("L", font_size=44, color=COLOR_OPERACION).next_to(l, LEFT, buff=0.4)
        self.decir("Repitamos la eliminación del sistema de la lección veintiséis, pero esta vez guardando cada multiplicador. A la derecha empezamos con la identidad: será nuestra matriz ele.")
        self.play(FadeIn(m), FadeIn(historial), FadeIn(l), FadeIn(rotulo_l))
        datos_l = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        pasos = [
            (("sumar", 1, 0, -2), (1, 0), 2, None,
             "Para anular el dos, a la fila dos le restamos dos veces la fila uno. El multiplicador es dos: lo anotamos en la posición dos uno de ele."),
            (("sumar", 2, 0, 1), (2, 0), -1, [(0, 0), (1, 1)],
             "Para anular el menos uno, a la fila tres le restamos menos uno veces la fila uno, o sea, le sumamos la fila uno. El multiplicador es menos uno, y va en la posición tres uno."),
            (("sumar", 2, 1, 3), (2, 1), -3, [(0, 0), (1, 1), (2, 2)],
             "Y para anular el tres de la segunda columna, le restamos menos tres veces la fila dos. El multiplicador es menos tres, en la posición tres dos."),
        ]
        for op, (i, j), mult, pivotes, frase in pasos:
            self.decir(frase)
            if pivotes:
                m = self.operar_filas(m, op, historial=historial, pivotes=pivotes)
            else:
                m = self.operar_filas(m, op, historial=historial)
            datos_l[i][j] = mult
            nueva = mat_l(datos_l, resaltar=(i, j)).move_to(l)
            self.play(ReplacementTransform(l, nueva))
            l = nueva
            self.wait(0.5)
        self.play(Create(SurroundingRectangle(l, color=COLOR_OPERACION)))
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que queda a cada lado")
        u = matriz([[1, 2, -1], [0, -1, 3], [0, 0, 10]], h_buff=1.0).scale(0.8)
        for k, e in enumerate(u.get_entries()):
            i, j = divmod(k, 3)
            e.set_color(COLOR_PIVOTE if i == j else WHITE)
        l2 = mat_l([[1, 0, 0], [2, 1, 0], [-1, -3, 1]])
        resultado = VGroup(
            VGroup(MathTex("L", font_size=44, color=COLOR_OPERACION), l2).arrange(RIGHT, buff=0.3),
            VGroup(MathTex("U", font_size=44, color=COLOR_PIVOTE), u).arrange(RIGHT, buff=0.3),
        ).arrange(RIGHT, buff=1.4).shift(UP * 0.3)
        regla = Tex(r"$L_{ij} = m_{ij}$ cuando se hace $R_i \leftarrow R_i - m_{ij}R_j$, y $A = LU$.", font_size=40, color=COLOR_OPERACION).next_to(resultado, DOWN, buff=0.8)
        ajustar_al_encuadre(VGroup(resultado, regla), margen=0.5)
        self.decir("Al terminar, a la izquierda queda u, la forma escalonada; a la derecha, ele, con los multiplicadores en su sitio. La regla es sencilla: el elemento i jota de ele es el multiplicador que se usó al restar a la fila i el múltiplo jota de la fila j. Y a es ele por u.")
        self.play(FadeIn(resultado))
        self.play(FadeIn(regla))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Para comprobar")
        cuentas = VGroup(
            MathTex(r"\text{fila 2 de } LU:\ \ 2\,[1,\ 2,\ -1] + 1\,[0,\ -1,\ 3] = [2,\ 3,\ 1]\ \checkmark", font_size=38),
            MathTex(r"\text{fila 3 de } LU:\ \ -1\,[1,\ 2,\ -1] - 3\,[0,\ -1,\ 3] + [0,\ 0,\ 10] = [-1,\ 1,\ 2]\ \checkmark", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.8)
        cuentas.set_color(COLOR_SOLUCION)
        ajustar_al_encuadre(cuentas, margen=0.5)
        self.decir("Comprobémoslo. La fila dos de ele u es dos veces la fila uno de u, más una vez la fila dos: dos, tres, uno, que es la fila dos de a. Y la fila tres: menos una vez la fila uno, menos tres veces la fila dos, más la fila tres: menos uno, uno, dos. Correcto.")
        for c in cuentas:
            self.play(Write(c))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N2-03",
            VGroup(
                Text("Halla L y U por eliminación, anotando el multiplicador, y comprueba que A = L U:", font_size=TAM_TEXTO),
                MathTex(r"A = \begin{bmatrix} 4 & 3 \\ 8 & 5 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla ele y u por eliminación, anotando el multiplicador, y comprueba que a es igual a ele por u. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Al eliminar con R_i ← R_i − m_ij R_j, se anota m_ij en la posición (i, j) de L.",
                "U es la forma escalonada y L tiene unos en la diagonal.",
                "A = L U, sin cálculos extra: la eliminación ya contiene a L.",
            ],
            "por qué los multiplicadores caen justo en su sitio.",
            voz="En resumen: al eliminar con erre i igual a erre i menos eme i jota por erre jota, se anota eme i jota en la posición i jota de ele. U es la forma escalonada, y ele tiene unos en la diagonal. Así, a es ele por u, sin cálculos extra: la eliminación ya contiene a ele. Siguiente: por qué los multiplicadores caen justo en su sitio.",
        )


class ConstruirLyU(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 35 · Parte 2", "¿Por qué funciona?")
        titulo = self.encabezado("Despejar A en E₃₂ E₃₁ E₂₁ A = U")
        cadena = VGroup(
            MathTex(r"E_{32}\,E_{31}\,E_{21}\,A = U", font_size=52),
            MathTex(r"A = E_{21}^{-1}\,E_{31}^{-1}\,E_{32}^{-1}\,U", font_size=52),
            MathTex(r"L = E_{21}^{-1}\,E_{31}^{-1}\,E_{32}^{-1}", font_size=52, color=COLOR_OPERACION),
        ).arrange(DOWN, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        self.decir("La eliminación dice que e tres dos, e tres uno, e dos uno, por a, es u. Para despejar a, multiplicamos por las inversas, en orden contrario: a es e dos uno inversa, e tres uno inversa, e tres dos inversa, por u.")
        self.play(Write(cadena[0]))
        self.play(Write(cadena[1]))
        self.wait(1)
        self.decir("Así que ele es el producto de las inversas de las matrices elementales. Falta ver por qué ese producto no es un lío.")
        self.play(Write(cadena[2]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Las inversas solo cambian el signo")
        inversas = VGroup(
            MathTex(r"E_{21}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}", font_size=38),
            MathTex(r"E_{31}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix}", font_size=38),
            MathTex(r"E_{32}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1 \end{bmatrix}", font_size=38),
        ).arrange(RIGHT, buff=0.7).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(inversas, margen=0.5)
        regla = Tex(r"$E_{ij}(k)^{-1} = E_{ij}(-k)$: deshacer ``restar $m$ veces'' es ``sumar $m$ veces''.", font_size=38, color=COLOR_OPERACION).next_to(inversas, DOWN, buff=0.7)
        self.decir("Las inversas son fáciles: deshacer restar el doble es sumar el doble. Así que cada inversa es la misma matriz con el signo del multiplicador cambiado: el dos, el menos uno, y el menos tres, que son los multiplicadores de la eliminación, ya con su signo bueno.")
        self.play(FadeIn(inversas))
        self.play(FadeIn(regla))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "En este orden, no se mezclan")
        buen = VGroup(
            MathTex(r"E_{31}^{-1}E_{32}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix}", font_size=36),
            MathTex(r"L = E_{21}^{-1}\,(E_{31}^{-1}E_{32}^{-1}) = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix}", font_size=36, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        mal = MathTex(r"\text{en el orden contrario: } E_{32}^{-1}E_{31}^{-1}E_{21}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -7 & -3 & 1 \end{bmatrix}\ \times", font_size=36, color=COLOR_ERROR).next_to(buen, DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(buen, mal), margen=0.5)
        self.decir("Y en este orden, los multiplicadores no se mezclan: al multiplicar las inversas, cada uno cae en su sitio. Ele es exactamente la matriz con el dos, el menos uno y el menos tres. Si multiplicáramos al revés, el producto saldría distinto: en la posición tres uno aparecería menos siete, que no es un multiplicador.")
        self.play(Write(buen[0]))
        self.play(Write(buen[1]))
        self.wait(1)
        self.play(Write(mal))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué hace falta")
        condiciones = VGroup(
            Tex(r"Solo se usaron operaciones de \textbf{reemplazo} hacia abajo: sin intercambios de filas.", font_size=36),
            Tex(r"Hace falta un pivote distinto de $0$ en cada paso (si no, L37: $PA = LU$).", font_size=36),
            Tex(r"Si $A$ es invertible y $A = LU$ con $L$ de unos en la diagonal, la factorización es \textbf{única}.", font_size=36, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(condiciones, margen=0.5)
        self.decir("Hay condiciones. Solo usamos operaciones de reemplazo, hacia abajo, sin intercambiar filas. Y necesitamos un pivote distinto de cero en cada paso; si no, hará falta una permutación, en la lección treinta y siete. Si a es invertible y la factorización existe, con unos en la diagonal de ele, es única.")
        for c in condiciones:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N3-02",
            VGroup(
                Text("Con las matrices elementales del ejemplo de la lección, calcula", font_size=TAM_TEXTO),
                Text("E₃₂⁻¹ E₃₁⁻¹ E₂₁⁻¹ y explica por qué no coincide con L.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: con las matrices elementales del ejemplo de la lección, calcula el producto en el orden contrario, y explica por qué no coincide con ele. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "A = E₂₁⁻¹ E₃₁⁻¹ E₃₂⁻¹ U, luego L = E₂₁⁻¹ E₃₁⁻¹ E₃₂⁻¹.",
                "La inversa de una elemental cambia el signo del multiplicador.",
                "En ese orden los multiplicadores caen en su sitio; en el contrario, se mezclan.",
            ],
            "Lección 36 — resolver con LU.",
            voz="En resumen: a es e dos uno inversa, por e tres uno inversa, por e tres dos inversa, por u, y por tanto ele es el producto de las inversas. La inversa de una elemental cambia el signo del multiplicador. En ese orden, los multiplicadores caen en su sitio; en el contrario, se mezclan. Siguiente: lección treinta y seis, resolver con ele u.",
        )
