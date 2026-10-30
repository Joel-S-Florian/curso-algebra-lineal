"""Lección 50 — El teorema del rango y la nulidad.

Escenas (un video cada una):
    NucleoColapsaImagenSobrevive, DemostracionRangoNulidad

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l50_rango_nulidad.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

# A = 5 P: P proyecta el plano sobre la recta y = 2x (la imagen) y aplasta la recta x + 2y = 0 (el núcleo).
# Se anima P, que tiene el mismo núcleo y la misma imagen que A = [[1, 2], [2, 4]] pero cabe en pantalla.
P = [[0.2, 0.4], [0.4, 0.8]]


def aplicar(punto):
    x, y = punto
    return np.array([P[0][0] * x + P[0][1] * y, P[1][0] * x + P[1][1] * y, 0.0])


class NucleoColapsaImagenSobrevive(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 50 · Parte 1", "Lo que se pierde y lo que sobrevive")
        titulo = self.encabezado("Una transformación que aplasta una dirección")
        plano = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-2, 2, 1], x_length=8, y_length=4,
            background_line_style={"stroke_color": BLUE_D, "stroke_opacity": 0.7, "stroke_width": 2},
            axis_config={"stroke_opacity": 0.5},
        ).shift(DOWN * 0.35)
        centro = plano.c2p(0, 0)
        nucleo = Line(plano.c2p(4, -2), plano.c2p(-4, 2), color=COLOR_PIVOTE, stroke_width=6)
        imagen = Line(plano.c2p(-1.4, -2.8), plano.c2p(1.4, 2.8), color=COLOR_SOLUCION, stroke_width=6)
        rot_nucleo = MathTex(r"\ker A", font_size=40, color=COLOR_PIVOTE).next_to(plano.c2p(-3.0, 1.5), UP, buff=0.15)
        self.decir("Veamos qué hace la matriz uno, dos; dos, cuatro, como transformación del plano. Para que quepa en pantalla dibujamos una versión reducida a la quinta parte, que tiene exactamente el mismo núcleo y la misma imagen. Su núcleo es la recta equis más dos ye igual a cero.")
        self.play(Create(plano))
        self.play(Create(nucleo), FadeIn(rot_nucleo))
        self.wait(1.5)

        x_a, x_b = np.array([1.0, 0.5]), np.array([-1.0, 1.5])  # x_b = x_a + (-2, 1): difieren en un vector del núcleo
        punto_a = Dot(plano.c2p(*x_a), color=COLORES_ECUACIONES[0], radius=0.11)
        punto_b = Dot(plano.c2p(*x_b), color=COLORES_ECUACIONES[1], radius=0.11)
        enlace = DashedLine(punto_a.get_center(), punto_b.get_center(), color=COLOR_SECUNDARIO)
        rot_a = MathTex(r"\mathbf{x}", font_size=36, color=COLORES_ECUACIONES[0]).next_to(punto_a, RIGHT, buff=0.15)
        rot_b = MathTex(r"\mathbf{x} + \mathbf{n}", font_size=36, color=COLORES_ECUACIONES[1]).next_to(punto_b, LEFT, buff=0.15)
        self.decir("Tomemos un punto equis y otro que se diferencia de él en un vector del núcleo, equis más ene. Están en una recta paralela al núcleo.")
        self.play(FadeIn(punto_a, scale=2), FadeIn(punto_b, scale=2))
        self.play(Create(enlace), FadeIn(rot_a), FadeIn(rot_b))
        self.wait(2)

        self.decir("Ahora aplicamos la transformación. Todo el plano se aplasta sobre una recta: la recta y igual a dos equis. El núcleo se colapsa al origen, y los dos puntos que diferían en un vector del núcleo aterrizan en el mismo punto.")
        destino_a, destino_b = plano.c2p(*aplicar(x_a)[:2]), plano.c2p(*aplicar(x_b)[:2])
        self.play(
            ApplyMatrix(np.array(P), plano, about_point=centro),
            ApplyMatrix(np.array(P), nucleo, about_point=centro),
            ApplyMatrix(np.array(P), enlace, about_point=centro),
            punto_a.animate.move_to(destino_a),
            punto_b.animate.move_to(destino_b),
            FadeOut(rot_a), FadeOut(rot_b), FadeOut(rot_nucleo),
            run_time=4,
        )
        rot_imagen = MathTex(r"\operatorname{Im} = \operatorname{Col}(A)", font_size=40, color=COLOR_SOLUCION).next_to(plano.c2p(0.9, 1.8), RIGHT, buff=0.3)
        self.play(Create(imagen), FadeIn(rot_imagen))
        self.wait(2)
        self.limpiar(titulo)

        balance = VGroup(
            Tex(r"Se pierde una dimensión (el núcleo: $\operatorname{nul} = 1$).", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Sobrevive una dimensión (la imagen: $\operatorname{rg} = 1$).", font_size=38, color=COLOR_SOLUCION),
            MathTex(r"1 + 1 = 2 = n", font_size=50),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.9)
        ajustar_al_encuadre(balance, margen=0.5)
        self.decir("Una dimensión se pierde, la del núcleo; una sobrevive, la de la imagen. Entre las dos suman las dos dimensiones del plano de partida.")
        self.play(FadeIn(balance[0]))
        self.wait(1.5)
        self.play(FadeIn(balance[1]))
        self.wait(1.5)
        self.play(Write(balance[2]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Con la matriz de tres por cuatro")
        tabla = VGroup(
            MathTex(r"A\ (3 \times 4):\quad \mathbb{R}^4 \longrightarrow \mathbb{R}^3", font_size=46),
            MathTex(r"\dim\ker A = 2 \quad \text{(se pierden)}", font_size=44, color=COLOR_PIVOTE),
            MathTex(r"\dim\operatorname{Col}(A) = 2 \quad \text{(sobreviven)}", font_size=44, color=COLOR_SOLUCION),
            MathTex(r"2 + 2 = 4 = n", font_size=54),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(tabla, margen=0.5)
        self.decir("Con la matriz de tres por cuatro, que lleva el espacio de cuatro dimensiones al de tres, el núcleo tiene dimensión dos y el espacio columna tiene dimensión dos. Dos más dos son cuatro, el número de columnas: de las cuatro dimensiones de partida, se pierden dos y sobreviven dos.")
        for t in tabla:
            self.play(FadeIn(t))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F14-N4-01",
            VGroup(
                Text("Calcula rango y nulidad, y comprueba que suman n:", font_size=TAM_TEXTO),
                MathTex(r"B = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix} \qquad C = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}", font_size=48),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: calcula el rango y la nulidad de estas dos matrices, y comprueba que suman el número de columnas. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "El núcleo se aplasta al origen: se pierde esa dimensión.",
                "La imagen sobrevive: su dimensión es el rango.",
                "Rango + nulidad = número de columnas.",
            ],
            "la demostración del teorema.",
            voz="En resumen: el núcleo se aplasta al origen y esa dimensión se pierde; la imagen sobrevive, y su dimensión es el rango. Entre las dos suman el número de columnas. Siguiente: la demostración del teorema.",
        )


class DemostracionRangoNulidad(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 50 · Parte 2", "El teorema del rango y la nulidad")
        titulo = self.encabezado("Enunciado")
        teorema = VGroup(
            Tex(r"Para toda matriz $A$ de tamaño $m \times n$:", font_size=42),
            MathTex(r"\operatorname{rg}(A) + \operatorname{nul}(A) = n", font_size=72, color=COLOR_PIVOTE),
            MathTex(r"\dim\operatorname{Col}(A) + \dim\ker A = n", font_size=52),
            Tex(r"(el número de columnas, es decir, de incógnitas).", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(teorema, margen=0.5)
        self.decir("El teorema del rango y la nulidad dice: para toda matriz a de tamaño eme por ene, el rango más la nulidad es igual a ene. Dicho con dimensiones, la dimensión del espacio columna más la dimensión del núcleo es el número de columnas.")
        for t in teorema:
            self.play(FadeIn(t))
            self.wait(2.2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Demostración")
        demo = VGroup(
            Tex(r"Reduce $A$. Sea $r$ el número de pivotes.", font_size=40),
            parrafo(r"Cada una de las $n$ columnas tiene pivote o no lo tiene: hay $r$ con pivote", r"y $n - r$ sin él (las variables libres).", font_size=38, sangria=0.5),
            parrafo(r"L49: las $r$ columnas pivote son una base de $\operatorname{Col}(A)$:", r"$\dim\operatorname{Col}(A) = r$.", font_size=38, sangria=0.5, color=COLOR_SOLUCION),
            parrafo(r"L46: cada variable libre aporta un vector a la base de $\ker A$:", r"$\dim\ker A = n - r$.", font_size=38, sangria=0.5, color=COLOR_PIVOTE),
            MathTex(r"\dim\operatorname{Col}(A) + \dim\ker A = r + (n - r) = n. \qquad \blacksquare", font_size=46),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(demo, margen=0.5)
        self.decir("La demostración junta lo que ya sabemos. Reducimos a, y sea erre el número de pivotes. Cada una de las ene columnas tiene pivote o no lo tiene: erre columnas lo tienen, y ene menos erre no, son las variables libres. Por la lección cuarenta y nueve, las erre columnas pivote son una base del espacio columna: su dimensión es erre. Por la lección cuarenta y seis, cada variable libre aporta un vector a la base del núcleo: su dimensión es ene menos erre. Sumando, erre más ene menos erre es ene.")
        for d in demo:
            self.play(FadeIn(d))
            self.wait(3.2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Consecuencias")
        consecuencias = VGroup(
            parrafo(r"\textbf{Inyectiva} (cada $\mathbf{b}$ se alcanza a lo sumo una vez):", r"$\ker A = \{\mathbf{0}\} \iff \operatorname{rg}(A) = n$.", font_size=36, sangria=0.5),
            parrafo(r"\textbf{Sobreyectiva} (se alcanza todo $\mathbf{b} \in \mathbb{R}^m$):", r"$\operatorname{Col}(A) = \mathbb{R}^m \iff \operatorname{rg}(A) = m$.", font_size=36, sangria=0.5),
            parrafo(r"Si $A$ es cuadrada ($m = n$): $\operatorname{rg}(A) = n \iff \ker A = \{\mathbf{0}\}$", r"$\iff \operatorname{Col}(A) = \mathbb{R}^n \iff A\mathbf{x} = \mathbf{b}$ tiene solución \textbf{única} para todo $\mathbf{b}$.", font_size=36, sangria=0.5, color=COLOR_PIVOTE),
            Tex(r"No existe $A$ de $3 \times 5$ inyectiva ($\operatorname{nul} \ge 2$) ni de $5 \times 3$ sobreyectiva ($\operatorname{rg} \le 3 < 5$).", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(consecuencias, margen=0.5)
        self.decir("Consecuencias. La transformación es inyectiva, es decir, cada vector se alcanza a lo sumo una vez, exactamente cuando el núcleo es trivial, o sea, cuando el rango es ene. Es sobreyectiva, se alcanza todo el espacio de eme dimensiones, cuando el rango es eme. Si la matriz es cuadrada, ambas condiciones coinciden: el rango es ene, el núcleo es trivial, el espacio columna es todo, y el sistema tiene solución única para cualquier lado derecho. Y no hay matrices de tres por cinco inyectivas, ni de cinco por tres sobreyectivas.")
        for c in consecuencias:
            self.play(FadeIn(c))
            self.wait(3.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F14-N4-02",
            VGroup(
                Text("Una matriz de 5×7 tiene rango 3.", font_size=TAM_TEXTO),
                Text("¿Cuál es la nulidad? ¿En qué espacio vive Col(A) y cuál es su dimensión?", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: una matriz de cinco por siete tiene rango tres. ¿Cuál es su nulidad? ¿En qué espacio vive su espacio columna, y qué dimensión tiene? Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "rg(A) + nul(A) = n, el número de columnas.",
                "Demostración: columnas con pivote (r) más columnas libres (n − r).",
                "Cuadrada: rango n ⇔ núcleo trivial ⇔ solución única para todo b.",
            ],
            "la síntesis: elegir el método y resolver problemas integradores (Unidad 9).",
            voz="En resumen: el rango más la nulidad es el número de columnas. La demostración cuenta las columnas con pivote, erre, y las libres, ene menos erre. Y en una matriz cuadrada, rango ene equivale a núcleo trivial y a solución única para todo lado derecho. Con esto termina la Unidad 8. Siguiente: la síntesis, elegir el método y resolver problemas integradores.",
        )
