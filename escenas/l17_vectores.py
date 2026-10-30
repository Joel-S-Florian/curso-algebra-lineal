"""Lección 17 — Vectores: flecha, punto, fila y columna; suma, escalar y combinación lineal.

Escenas (un video cada una):
    VectorComoFlechaYComoPunto, SumaYEscalarGeometricos, PrimeraCombinacionLineal

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l17_vectores.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, flecha, matriz, num, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_U, COLOR_V, COLOR_W = COLORES_ECUACIONES


def plano(x_range=(-2, 6), y_range=(-2, 5), unidad=0.75) -> NumberPlane:
    return NumberPlane(
        x_range=[*x_range, 1],
        y_range=[*y_range, 1],
        x_length=(x_range[1] - x_range[0]) * unidad,
        y_length=(y_range[1] - y_range[0]) * unidad,
        background_line_style={"stroke_opacity": 0.3},
    )


def columna(*componentes, color=WHITE, font_size=40) -> MathTex:
    filas = r" \\ ".join(str(c) for c in componentes)
    return MathTex(r"\begin{bmatrix} " + filas + r" \end{bmatrix}", font_size=font_size, color=color)


class VectorComoFlechaYComoPunto(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 17 · Parte 1", "¿Qué es un vector?")
        titulo = self.encabezado("Una lista ordenada de números")
        p = plano().to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)
        self.play(Create(p))
        v = flecha(p, 3, 2, COLOR_U)
        punto = Dot(p.c2p(3, 2), color=COLOR_U)
        notacion = VGroup(MathTex(r"\mathbf{v} =", font_size=48), columna(3, 2, color=COLOR_U, font_size=48)).arrange(RIGHT)
        notacion.to_edge(RIGHT, buff=1.5).shift(UP * 1.8)
        self.decir("Un vector es una lista ordenada de números, sus componentes. Este vector del plano tiene dos: tres y dos.")
        self.play(Write(notacion))
        self.pie("Un vector del plano es una lista ordenada de 2 números: sus COMPONENTES.", espera=2)
        self.decir("Se puede dibujar como un punto.")
        self.play(FadeIn(punto, scale=2))
        self.pie("Se puede dibujar como un punto…", espera=1.5)
        self.decir("O como una flecha desde el origen: avanza tres a la derecha y sube dos. Es un desplazamiento.")
        self.play(GrowArrow(v))
        self.pie("…o como una flecha desde el origen: «avanza 3 a la derecha y sube 2». Es un desplazamiento.", espera=3)
        guias = VGroup(
            DashedLine(p.c2p(0, 0), p.c2p(3, 0), color=COLOR_COEFICIENTE),
            DashedLine(p.c2p(3, 0), p.c2p(3, 2), color=COLOR_TERMINO_INDEP),
        )
        self.decir("Una flecha con la misma longitud, dirección y sentido representa el mismo desplazamiento, esté donde esté. Pero en este curso, salvo aviso, dibujaremos los vectores desde el origen.")
        self.play(Create(guias))
        self.wait(1)
        copias = VGroup(flecha(p, 3, 2, COLOR_U, desde=(-1, -1)).set_opacity(0.5), flecha(p, 3, 2, COLOR_U, desde=(1, 2)).set_opacity(0.5))
        self.play(FadeOut(guias), LaggedStart(*[TransformFromCopy(v, c) for c in copias], lag_ratio=0.4))
        self.pie("Flechas con la misma longitud, dirección y sentido representan el mismo desplazamiento.\nPero en este curso, salvo aviso, los vectores salen del origen.", espera=4)
        self.play(FadeOut(copias))
        mas = VGroup(
            MathTex(r"\mathbf{w} = \begin{bmatrix} 2 \\ -1 \\ 4 \end{bmatrix} \in \mathbb{R}^3", font_size=40),
            MathTex(r"\mathbf{x} = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} \in \mathbb{R}^n", font_size=40),
        ).arrange(DOWN, buff=0.5).next_to(notacion, DOWN, buff=0.7)
        self.decir("Con tres componentes, el vector vive en el espacio. Con ene componentes ya no se puede dibujar, pero sigue siendo una lista de ene números.")
        self.play(FadeIn(mas[0]))
        self.wait(1.5)
        self.play(FadeIn(mas[1]))
        self.pie("Con n componentes ya no se puede dibujar, pero sigue siendo una lista de n números.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Vector columna y vector fila")
        col = VGroup(columna(3, 2, -1, font_size=56), Tex(r"vector columna: matriz $3\times 1$", font_size=36))
        fila = VGroup(MathTex(r"\begin{bmatrix} 3 & 2 & -1 \end{bmatrix}", font_size=56), Tex(r"vector fila: matriz $1\times 3$", font_size=36))
        for g in (col, fila):
            g.arrange(DOWN, buff=0.4)
        VGroup(col, fila).arrange(RIGHT, buff=2.5).shift(UP * 1.1)
        self.decir("Los mismos números se pueden escribir en columna, o en fila.")
        self.play(FadeIn(col))
        self.play(TransformFromCopy(col[0], fila[0]), FadeIn(fila[1]))
        self.wait(1)
        traspuesta = MathTex(
            r"\begin{bmatrix} 3 & 2 & -1 \end{bmatrix}^{T} = \begin{bmatrix} 3 \\ 2 \\ -1 \end{bmatrix}", font_size=44
        ).next_to(VGroup(col, fila), DOWN, buff=0.5)
        self.decir("La traspuesta cambia uno por otro. En este curso, los vectores son columnas.")
        self.play(Write(traspuesta))
        self.pie(
            "Mismos números, distinta forma. La T (TRASPUESTA) convierte filas en columnas y viceversa.\n"
            "Convenio del curso: los vectores son COLUMNAS. Para ahorrar espacio, a veces escribiremos (3, 2, −1).",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F05-N1-03",
            VGroup(
                Text("Dibuja como flechas desde el origen:", font_size=TAM_TEXTO),
                MathTex(r"\mathbf{a} = \begin{bmatrix} -2 \\ 3 \end{bmatrix} \quad \mathbf{b} = \begin{bmatrix} 4 \\ 0 \end{bmatrix} \quad \mathbf{c} = \begin{bmatrix} 0 \\ -3 \end{bmatrix}", font_size=46),
                Tex(r"¿Qué dimensión tiene cada uno como matriz? ¿Y $\mathbf{a}^T$?", font_size=38),
            ).arrange(DOWN, buff=0.45),
        )
        self.resumen(
            [
                "Un vector con n componentes es una lista ordenada de n números.",
                "Con 2 o 3 componentes se dibuja como punto o como flecha desde el origen.",
                "Vector columna: n × 1. Vector fila: 1 × n. La traspuesta cambia uno por otro.",
            ],
            "sumar vectores y multiplicarlos por números.",
            voz="En resumen: un vector con ene componentes es una lista ordenada de ene números. Con dos o tres componentes se dibuja como un punto, o como una flecha desde el origen. Un vector columna es de ene por uno, y un vector fila, de uno por ene; la traspuesta cambia uno por otro. Siguiente: sumar vectores y multiplicarlos por números.",
        )


class SumaYEscalarGeometricos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 17 · Parte 2", "Sumar vectores y multiplicarlos por un número")
        titulo = self.encabezado("Suma: componente a componente")
        p = plano(x_range=(-2, 6), y_range=(-2, 4)).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)
        self.play(Create(p))
        u, v = flecha(p, 1, 2, COLOR_U), flecha(p, 3, -1, COLOR_V)
        rot_u = MathTex(r"\mathbf{u}", color=COLOR_U).next_to(u.get_end(), LEFT, buff=0.1)
        rot_v = MathTex(r"\mathbf{v}", color=COLOR_V).next_to(v.get_end(), DOWN, buff=0.1)
        self.decir("Tomemos dos vectores, u y uve.")
        self.play(GrowArrow(u), GrowArrow(v), Write(rot_u), Write(rot_v))
        algebra = MathTex(
            r"\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 + 3 \\ 2 + (-1) \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}",
            font_size=40,
        ).to_edge(RIGHT, buff=0.5).shift(UP * 1.8)
        self.decir("Para sumarlos, se suman las componentes que ocupan la misma posición.")
        self.play(Write(algebra))
        self.pie("Algebraicamente, se suman las componentes que ocupan la misma posición.", espera=2)
        v_trasladado = flecha(p, 3, -1, COLOR_V, desde=(1, 2))
        self.decir("En el dibujo, es un desplazamiento tras otro: ponemos la cola de uve en la punta de u.")
        self.play(TransformFromCopy(v, v_trasladado), run_time=1.5)
        suma = flecha(p, 4, 1, COLOR_W)
        rot_s = MathTex(r"\mathbf{u} + \mathbf{v}", color=COLOR_W).next_to(suma.get_end(), RIGHT, buff=0.1)
        self.play(GrowArrow(suma), Write(rot_s))
        self.pie("Geométricamente: un desplazamiento tras otro (la cola de v en la punta de u).", espera=2)
        u_trasladado = flecha(p, 1, 2, COLOR_U, desde=(3, -1))
        self.decir("En el otro orden se llega al mismo punto: se forma un paralelogramo, y u más uve es igual a uve más u.")
        self.play(TransformFromCopy(u, u_trasladado), run_time=1.5)
        self.pie("En el otro orden se llega al mismo punto: se forma un paralelogramo y u + v = v + u.", espera=4)
        self.limpiar(titulo, p)

        # Producto por un escalar.
        titulo = self.cambiar_encabezado(titulo, "Multiplicar por un número (escalar)")
        c = ValueTracker(1)
        base = flecha(p, 1, 2, COLOR_U).set_opacity(0.35)
        def escalado_actual():
            cv = c.get_value()
            if abs(cv) < 0.05:  # una flecha de longitud 0 no se puede dibujar: se muestra un punto
                return Dot(p.c2p(0, 0), color=COLOR_U, radius=0.1)
            return flecha(p, cv, 2 * cv, COLOR_U)

        escalado = always_redraw(escalado_actual)
        lectura = always_redraw(
            lambda: MathTex(
                rf"{num(c.get_value())}\cdot\begin{{bmatrix}} 1 \\ 2 \end{{bmatrix}} = \begin{{bmatrix}} {num(c.get_value())} \\ {num(2 * c.get_value())} \end{{bmatrix}}",
                font_size=44,
            ).to_edge(RIGHT, buff=0.8).shift(UP * 1.5)
        )
        self.add(base)
        self.decir("Multiplicar un vector por un número, un escalar, es multiplicar cada componente por ese número.")
        self.play(FadeIn(escalado), FadeIn(lectura))
        notas = {2: "Por 2: el doble de largo, misma dirección.", 0.5: "Por 1/2: la mitad.", -1: "Por −1: misma longitud, sentido contrario (el OPUESTO −u).", 0: "Por 0: el vector nulo (0, 0)."}
        self.decir("Multiplicar por un número mayor que uno estira la flecha; por un número entre cero y uno, la encoge; con un número negativo, la da la vuelta. Y con cero, se reduce al vector nulo.")
        for valor, nota in notas.items():
            self.play(c.animate.set_value(valor), run_time=1.5)
            self.pie(nota, espera=1.5)
        self.play(c.animate.set_value(1))
        self.decir("Todos los múltiplos de u quedan sobre la misma recta que pasa por el origen.")
        self.pie("Todos los múltiplos c·u quedan sobre la misma recta que pasa por el origen.", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Resta y vector nulo")
        bloque = VGroup(
            MathTex(r"\mathbf{u} - \mathbf{v} = \mathbf{u} + (-1)\mathbf{v} = \begin{bmatrix} 1 - 3 \\ 2 - (-1) \end{bmatrix} = \begin{bmatrix} -2 \\ 3 \end{bmatrix}", font_size=44),
            MathTex(r"\mathbf{0} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}: \quad \mathbf{u} + \mathbf{0} = \mathbf{u}, \qquad \mathbf{u} + (-\mathbf{u}) = \mathbf{0}", font_size=44),
            Tex(r"Solo se suman vectores con el \textbf{mismo número de componentes}.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.6)
        self.decir("Restar es sumar el opuesto: u menos uve es u más menos uno por uve. El vector nulo, con todas sus componentes cero, es el neutro de la suma. Y solo se suman vectores con el mismo número de componentes.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F05-N2-01",
            VGroup(
                MathTex(r"\mathbf{u} = \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} -1 \\ 4 \\ 0 \end{bmatrix}", font_size=46),
                MathTex(r"\text{Calcula: a) } \mathbf{u} + \mathbf{v} \quad \text{b) } 3\mathbf{u} \quad \text{c) } 2\mathbf{u} - 3\mathbf{v} \quad \text{d) } \mathbf{u} - \mathbf{u}", font_size=42),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "u + v: se suman las componentes; en el dibujo, punta con cola (paralelogramo).",
                "c·u: se multiplica cada componente; estira, encoge o invierte el vector.",
                "u − v = u + (−1)v. El vector nulo 0 es neutro de la suma.",
            ],
            "combinar vectores.",
            voz="En resumen: para sumar vectores se suman sus componentes; en el dibujo, se pone la punta de uno en la cola del otro, y se forma un paralelogramo. Multiplicar por un número multiplica cada componente: estira, encoge o invierte el vector. Restar es sumar el opuesto, y el vector nulo es el neutro de la suma. Siguiente: combinar vectores.",
        )


class PrimeraCombinacionLineal(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 17 · Parte 3", "Combinaciones lineales")
        titulo = self.encabezado("Mezclar dos vectores con dos pesos")
        p = plano(x_range=(-2, 7), y_range=(-2, 5), unidad=0.7).to_edge(LEFT, buff=0.5).shift(DOWN * 0.3)
        self.play(Create(p))
        u, v = flecha(p, 1, 2, COLOR_U), flecha(p, 3, -1, COLOR_V)
        self.decir("Tenemos dos vectores: u, el uno, dos, y uve, el tres, menos uno.")
        self.play(GrowArrow(u), GrowArrow(v))
        definicion = MathTex(r"a\,\mathbf{u} + b\,\mathbf{v}", font_size=52).to_edge(RIGHT, buff=1.5).shift(UP * 2.2)
        self.decir("Mezclándolos con dos pesos, a y be, obtenemos una combinación lineal: a por u, más be por uve.")
        self.play(Write(definicion))
        self.pie("Una COMBINACIÓN LINEAL de u y v es a·u + b·v, con a y b números cualesquiera (los pesos).", espera=3)

        a, b = ValueTracker(0.5), ValueTracker(1.5)

        def combinacion():
            av, bv = a.get_value(), b.get_value()
            parte_u = flecha(p, av * 1, av * 2, COLOR_U)
            parte_v = flecha(p, bv * 3, -bv, COLOR_V, desde=(av, 2 * av))
            total = flecha(p, av + 3 * bv, 2 * av - bv, COLOR_W)
            return VGroup(parte_u, parte_v, total)

        def lectura():
            av, bv = a.get_value(), b.get_value()
            return MathTex(
                rf"{num(av)}\,\mathbf{{u}} + {num(bv)}\,\mathbf{{v}} = ({num(av + 3 * bv)},\ {num(2 * av - bv)})",
                font_size=40,
            ).next_to(definicion, DOWN, buff=0.5).to_edge(RIGHT, buff=0.5)

        objetivo = Dot(p.c2p(5, 3), color=COLOR_PIVOTE, radius=0.12)
        rot_obj = MathTex(r"\mathbf{w} = (5, 3)", font_size=36, color=COLOR_PIVOTE).next_to(objetivo, UR, buff=0.1)
        dibujo, panel = always_redraw(combinacion), always_redraw(lectura)
        self.decir("Al cambiar los pesos, llegamos a puntos distintos.")
        self.play(FadeIn(dibujo), FadeIn(panel))
        for av, bv in ((1, 1), (-0.5, 1), (2, 0.5)):
            self.play(a.animate.set_value(av), b.animate.set_value(bv), run_time=2)
        self.decir("¿Qué pesos nos llevan exactamente al punto cinco, tres?")
        self.play(FadeIn(objetivo, scale=2), Write(rot_obj))
        self.pie("¿Qué pesos a y b hacen que a·u + b·v llegue exactamente a w = (5, 3)?", espera=2)
        self.decir("Con a igual a dos y be igual a uno: dos por uno, dos, más uno por tres, menos uno, da cinco, tres. ¿Cómo encontrar los pesos sin tantear?")
        self.play(a.animate.set_value(2), b.animate.set_value(1), run_time=3)
        self.play(Flash(objetivo, color=COLOR_PIVOTE))
        self.pie("Con a = 2 y b = 1: 2·(1, 2) + 1·(3, −1) = (5, 3). ¿Cómo encontrar a y b sin tantear?", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¡Encontrar los pesos es resolver un sistema!")
        ecuacion = MathTex(
            r"a \begin{bmatrix} 1 \\ 2 \end{bmatrix} + b \begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}", font_size=52
        ).shift(UP * 2.0)
        self.decir("Escribimos la igualdad de vectores.")
        self.play(Write(ecuacion))
        componentes = MathTex(r"\begin{bmatrix} a + 3b \\ 2a - b \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \end{bmatrix}", font_size=52).next_to(ecuacion, DOWN, buff=0.4)
        self.decir("Dos vectores son iguales si coinciden componente a componente: dos ecuaciones.")
        self.play(TransformFromCopy(ecuacion, componentes))
        self.pie("Dos vectores son iguales si coinciden componente a componente: dos ecuaciones.", espera=2)
        sistema = sistema_con_llave(("a + 3b", "=", "5"), ("2a - b", "=", "3"), font_size=48).next_to(componentes, DOWN, buff=0.4)
        self.decir("Aparece un sistema de ecuaciones: a más tres be igual a cinco, y dos a menos be igual a tres.")
        self.play(TransformFromCopy(componentes, sistema))
        solucion = MathTex(r"\Rightarrow\ a = 2,\ b = 1", font_size=48, color=COLOR_SOLUCION).next_to(sistema, RIGHT, buff=0.6)
        self.decir("Su solución es a igual a dos, be igual a uno. Resolver un sistema lineal es lo mismo que buscar los pesos de una combinación lineal.")
        self.play(Write(solucion))
        self.pie(
            "Resolver un sistema lineal = buscar los pesos de una combinación lineal. Esta idea\n"
            "volverá con fuerza en Ax = b (Lección 22) y en el espacio columna (Lección 48).",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F05-N3-01",
            VGroup(
                MathTex(r"\text{Escribe } \mathbf{w} = \begin{bmatrix} 1 \\ 8 \end{bmatrix} \text{ como combinación lineal de } \mathbf{u} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \text{ y } \mathbf{v} = \begin{bmatrix} 3 \\ -1 \end{bmatrix}.", font_size=42),
                Text("Plantea el sistema, resuélvelo y comprueba.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Combinación lineal de u y v: a·u + b·v (a y b, los pesos).",
                "Al variar los pesos se alcanzan distintos puntos.",
                "Encontrar los pesos que dan un vector w es resolver un sistema lineal.",
            ],
            "Lección 18 — suma de matrices y producto por escalar.",
            voz="En resumen: una combinación lineal de u y uve es a por u más be por uve, donde a y be son los pesos. Al variar los pesos se alcanzan distintos puntos. Y encontrar los pesos que dan un vector concreto es resolver un sistema lineal. Siguiente: lección dieciocho, suma de matrices y producto por un escalar.",
        )
