"""Lección 38 — Comparación y aplicaciones de LU.

Escenas (un video cada una):
    MuchosLadosDerechos, TablaComparativa

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l38_comparacion_y_aplicaciones.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def coste_lu(n: int, k: int) -> int:
    """Factorizar una vez ((n³ - n)/3) y resolver k lados derechos (n² cada uno)."""
    return (n**3 - n) // 3 + k * n**2


def coste_gauss_repetido(n: int, k: int) -> int:
    """Gauss con sustitución hacia atrás repetido para cada lado derecho."""
    return k * (n**3 + 3 * n**2 - n) // 3


class MuchosLadosDerechos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 38 · Parte 1", "Factorizar una vez, resolver muchas")
        titulo = self.encabezado("La misma matriz, lados derechos distintos")
        sistemas = VGroup(
            MathTex(r"A\mathbf{x}_1 = \mathbf{b}_1,\quad A\mathbf{x}_2 = \mathbf{b}_2,\quad \dots,\quad A\mathbf{x}_k = \mathbf{b}_k", font_size=48),
            Tex(r"Por ejemplo, una estructura con la misma rigidez $A$ y $k$ cargas distintas $\mathbf{b}_i$.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(sistemas, margen=0.5)
        self.decir("Hay problemas en los que la matriz a es siempre la misma, pero el lado derecho cambia: por ejemplo, una estructura con la misma rigidez, y muchas cargas distintas. Hay que resolver a equis uno igual a be uno, a equis dos igual a be dos, y así, hasta ka sistemas.")
        self.play(Write(sistemas[0]))
        self.play(FadeIn(sistemas[1]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Con Gauss, se repite todo; con LU, no")
        comparacion = VGroup(
            parrafo(r"\textbf{Gauss repetido:} la eliminación se rehace para cada $\mathbf{b}_i$.", r"Cada sistema cuesta $\approx \frac{n^3}{3}$.", font_size=38, sangria=0.5, color=COLOR_ERROR),
            parrafo(r"\textbf{LU:} se factoriza una sola vez, $A = LU$, y cada $\mathbf{b}_i$ solo exige", r"las dos sustituciones: $n^2$ operaciones.", font_size=38, sangria=0.5, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(comparacion, margen=0.5)
        self.decir("Con Gauss, habría que rehacer toda la eliminación para cada lado derecho: unas ene cubo entre tres operaciones cada vez. Con ele u, factorizamos una sola vez, y para cada be solo hacen falta las dos sustituciones: ene cuadrado operaciones.")
        for c in comparacion:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Tres lados derechos con la misma L y U")
        sol = VGroup(
            MathTex(r"\mathbf{b}_1 = (-3,\ 1,\ 2) \;\Rightarrow\; \mathbf{y} = (-3,\ 7,\ 20) \;\Rightarrow\; \mathbf{x} = (1,\ -1,\ 2)", font_size=38),
            MathTex(r"\mathbf{b}_2 = (0,\ 1,\ -3) \;\Rightarrow\; \mathbf{y} = (0,\ 1,\ 0) \;\Rightarrow\; \mathbf{x} = (2,\ -1,\ 0)", font_size=38),
            MathTex(r"\mathbf{b}_3 = (2,\ 5,\ 1) \;\Rightarrow\; \mathbf{y} = (2,\ 1,\ 6) \;\Rightarrow\; \mathbf{x} = \left(1,\ \tfrac45,\ \tfrac35\right)", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(sol, margen=0.5)
        nota = Tex(r"$L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix},\ U = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 10 \end{bmatrix}$ \ no cambian.", font_size=36, color=COLOR_SECUNDARIO).next_to(sol, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(sol, nota), margen=0.5)
        self.decir("Con la factorización de nuestro ejemplo, resolvemos tres lados derechos. Menos tres, uno, dos: ye es menos tres, siete, veinte, y la solución, uno, menos uno, dos. Cero, uno, menos tres: la solución es dos, menos uno, cero. Y dos, cinco, uno: ye es dos, uno, seis, y la solución, uno, cuatro quintos, tres quintos. Ele y u no han cambiado.")
        for s in sol:
            self.play(Write(s))
            self.wait(1.5)
        self.play(FadeIn(nota))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cuánto se ahorra")
        n, k = 100, 50
        ahorro = VGroup(
            MathTex(r"\text{LU: } \frac{n^3 - n}{3} + k\,n^2", font_size=40, color=COLOR_SOLUCION),
            MathTex(r"\text{Gauss repetido: } k\,\frac{n^3 + 3n^2 - n}{3}", font_size=40, color=COLOR_ERROR),
            MathTex(r"\text{Diferencia: } (k - 1)\,\frac{n^3 - n}{3} \ \ge 0", font_size=40, color=COLOR_PIVOTE),
            Tex(rf"Con $n = {n}$ y $k = {k}$: LU {coste_lu(n, k):,} frente a {coste_gauss_repetido(n, k):,}.".replace(",", r"\,"), font_size=38),
            Tex(rf"LU hace unas {coste_gauss_repetido(n, k) / coste_lu(n, k):.0f} veces menos operaciones.", font_size=38, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(ahorro, margen=0.5)
        self.decir("¿Cuánto se ahorra? Con ele u, factorizar cuesta ene cubo menos ene, entre tres, una vez, más ene cuadrado por cada uno de los ka lados derechos. Gauss repetido cuesta ka veces ene cubo más tres ene cuadrado menos ene, entre tres. La diferencia es ka menos uno, por ene cubo menos ene, entre tres: nunca es negativa, y con un solo lado derecho, es cero.")
        for a in ahorro[:3]:
            self.play(Write(a))
            self.wait(1.5)
        self.decir("Con un sistema de cien por cien y cincuenta lados derechos, ele u hace ochocientas treinta y tres mil trescientas operaciones, frente a diecisiete millones ciento sesenta y cinco mil de Gauss repetido: unas veintiuna veces menos.")
        self.play(FadeIn(ahorro[3]))
        self.play(FadeIn(ahorro[4]))
        self.wait(2)

        self.ejercicio_propuesto(
            "F10-N2-06",
            VGroup(
                Text("Con L = [[1, 0], [3, 1]] y U = [[2, 1], [0, 4]] (de A = [[2, 1], [6, 7]]),", font_size=TAM_TEXTO),
                Text("resuelve A x = b para b₁ = (3, 13) y para b₂ = (1, −3), sin volver a eliminar.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: con estos ele y u, de la matriz a igual a dos, uno, seis, siete, resuelve a equis igual a be para be uno igual a tres, trece, y para be dos igual a uno, menos tres, sin volver a eliminar. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Con la misma A y k lados derechos: factorizar una vez, resolver k veces.",
                "LU: (n³ − n)/3 + k n²; Gauss repetido: k (n³ + 3n² − n)/3.",
                "Con k = 1 cuestan igual; con k mayor, LU gana por (k − 1)(n³ − n)/3.",
            ],
            "una tabla para elegir método.",
            voz="En resumen: con la misma matriz y ka lados derechos, se factoriza una vez y se resuelve ka veces. Ele u cuesta ene cubo menos ene, entre tres, más ka ene cuadrado; Gauss repetido, ka veces ene cubo más tres ene cuadrado menos ene, entre tres. Con ka igual a uno cuestan igual, y con ka mayor, ele u gana. Siguiente: una tabla para elegir método.",
        )


class TablaComparativa(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 38 · Parte 2", "¿Qué método elegir?")
        titulo = self.encabezado("Todos los métodos de la Unidad 2 a la 6")
        filas = [
            ("Método", "Cuándo conviene", "Coste (n × n)"),
            ("Sustitución, igualación", "2 o 3 incógnitas, a mano", "—"),
            ("Reducción / Gauss", "un sistema, a mano o en máquina", "≈ n³/3"),
            ("Gauss-Jordan", "a mano, lectura directa; comparar sistemas", "≈ n³/2"),
            ("LU (PA = LU)", "misma A, muchos lados derechos", "≈ n³/3 una vez + n² por b"),
        ]
        tabla = VGroup()
        for i, fila in enumerate(filas):
            for j, texto in enumerate(fila):
                tabla.add(Text(texto, font_size=TAM_NOTA, weight="BOLD" if i == 0 or j == 0 else "NORMAL", color=COLOR_SECUNDARIO if i == 0 else WHITE))
        tabla.arrange_in_grid(rows=len(filas), cols=3, buff=(0.6, 0.42), col_alignments="lll").next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(tabla, margen=0.5)
        self.decir("Esta es la tabla de todos los métodos que hemos visto. Sustitución e igualación: para dos o tres incógnitas, a mano. Reducción, que es Gauss: un solo sistema, a mano o en máquina, con unas ene cubo entre tres operaciones.")
        self.play(FadeIn(tabla[:3]))
        self.play(FadeIn(tabla[3:9]))
        self.decir("Gauss-Jordan: a mano, con lectura directa de la solución, y para comparar sistemas, con unas ene cubo entre dos. Y ele u, con pivoteo: la misma matriz con muchos lados derechos, con ene cubo entre tres una sola vez, más ene cuadrado por cada be.")
        self.play(FadeIn(tabla[9:]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué comparten")
        comun = VGroup(
            Tex(r"Todos usan solo las tres operaciones elementales (L24) o equivalen a ellas.", font_size=38),
            Tex(r"Todos dan el mismo conjunto solución.", font_size=38),
            Tex(r"Todos exigen \textbf{verificar en el sistema original} (L30).", font_size=38, color=COLOR_SOLUCION),
            Tex(r"Ninguno resuelve lo que el sistema no tiene: SI y SCI se detectan por los pivotes (L32).", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(comun, margen=0.5)
        self.decir("Qué comparten. Todos se basan en las tres operaciones elementales, o equivalen a ellas. Todos dan el mismo conjunto solución. Todos exigen verificar en el sistema original. Y ninguno resuelve lo que el sistema no tiene: que no haya solución, o que haya infinitas, se detecta por los pivotes.")
        for c in comun:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que viene")
        siguiente = VGroup(
            Tex(r"Hasta ahora hemos \emph{resuelto} sistemas. ¿Podemos \emph{clasificarlos sin resolver}?", font_size=40),
            Tex(r"El número de pivotes tiene nombre: el \textbf{rango}.", font_size=40, color=COLOR_PIVOTE),
            Tex(r"Unidad 7: Rouché-Frobenius, un teorema que decide SI, SCD o SCI con el rango.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(siguiente, margen=0.5)
        self.decir("Hasta ahora hemos resuelto sistemas. ¿Podemos clasificarlos sin resolver? El número de pivotes tiene nombre: el rango. En la unidad siete veremos el teorema de Rouché-Frobenius, que decide si un sistema es incompatible, determinado o indeterminado, usando el rango.")
        for s in siguiente:
            self.play(FadeIn(s))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N3-07",
            VGroup(
                Text("Elige el método más adecuado y justifica:", font_size=TAM_TEXTO),
                Text("a) Una matriz fija y 200 lados derechos distintos.", font_size=TAM_NOTA + 2),
                Text("b) Un sistema 2 × 2 en un examen.", font_size=TAM_NOTA + 2),
                Text("c) Saber si dos sistemas con las mismas incógnitas son equivalentes.", font_size=TAM_NOTA + 2),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4),
            voz="Ejercicio propuesto: elige el método más adecuado y justifica la elección. Uno: una matriz fija y doscientos lados derechos distintos. Dos: un sistema de dos por dos en un examen. Tres: saber si dos sistemas son equivalentes. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Pocas incógnitas, a mano: sustitución, igualación o Gauss-Jordan.",
                "Un sistema grande: Gauss. Misma A con muchos b: P A = L U.",
                "Todos: verificar en el original.",
            ],
            "Unidad 7 — rango y teorema de Rouché-Frobenius.",
            voz="En resumen: con pocas incógnitas, a mano, sustitución, igualación o Gauss-Jordan. Para un sistema grande, Gauss; y con la misma matriz y muchos lados derechos, pe a igual a ele u. En todos, verificar en el sistema original. Siguiente: unidad siete, rango y teorema de Rouché-Frobenius.",
        )
