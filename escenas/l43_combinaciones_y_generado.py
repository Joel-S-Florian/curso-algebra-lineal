"""Lección 43 — Combinaciones lineales y espacio generado.

Escenas (un video cada una):
    CombinacionLinealGeometrica, EspacioGenerado

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l43_combinaciones_y_generado.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import panel_derecha, EscenaCurso, ajustar_al_encuadre, ejes_iguales, flecha, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_U, COLOR_V, COLOR_W = COLORES_ECUACIONES


def plano_vectores(x_range=(-4, 6), y_range=(-3, 4)) -> Axes:
    return ejes_iguales(x_range, y_range, unidad=0.72).to_edge(LEFT, buff=0.5).shift(DOWN * 0.35)


class CombinacionLinealGeometrica(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 43 · Parte 1", "Combinaciones lineales")
        titulo = self.encabezado("Estirar y sumar vectores")
        p = plano_vectores()
        u, v = flecha(p, 2, 1, COLOR_U), flecha(p, -1, 1, COLOR_V)
        rot_u = MathTex(r"\mathbf{u} = (2, 1)", font_size=36, color=COLOR_U).next_to(p.c2p(2, 1), DOWN, buff=0.25).shift(RIGHT * 0.5)
        rot_v = MathTex(r"\mathbf{v} = (-1, 1)", font_size=36, color=COLOR_V).next_to(p.c2p(-1, 1), UP, buff=0.2).shift(LEFT * 0.4)
        self.decir("Tenemos dos vectores del plano: u, dos y uno; y ve, menos uno y uno. Con ellos podemos hacer solo dos cosas: estirarlos, o multiplicarlos por un número; y sumarlos.")
        self.play(Create(p))
        self.play(GrowArrow(u), GrowArrow(v), FadeIn(rot_u), FadeIn(rot_v))
        self.wait(1)

        dos_u = flecha(p, 4, 2, COLOR_U)
        v_al_final = flecha(p, -1, 1, COLOR_V, desde=(4, 2))
        suma = flecha(p, 3, 3, COLOR_W)
        formula = MathTex(r"2\,\mathbf{u} + 1\,\mathbf{v} = (3, 3)", font_size=46, color=COLOR_W).to_edge(RIGHT, buff=0.7).shift(UP * 1.8)
        panel_derecha(formula)
        self.decir("Estiremos u al doble, y pongamos ve a continuación. El vector que va del origen al final es dos veces u, más una vez ve: el vector tres, tres.")
        self.play(TransformFromCopy(u, dos_u))
        self.play(TransformFromCopy(v, v_al_final))
        self.play(GrowArrow(suma), Write(formula))
        self.wait(2)

        otra = flecha(p, 4, -1, COLOR_W)
        resto = [dos_u, v_al_final, suma, formula]
        formula2 = MathTex(r"1\,\mathbf{u} - 2\,\mathbf{v} = (4, -1)", font_size=46, color=COLOR_W).move_to(formula)
        u_a_v = flecha(p, 2, 1, COLOR_U)
        menos_2v = flecha(p, 2, -2, COLOR_V, desde=(2, 1))
        self.decir("Otra combinación: una vez u, menos dos veces ve. Multiplicar por un número negativo invierte el sentido. Sale el vector cuatro, menos uno.")
        self.play(*[FadeOut(m) for m in resto])
        self.play(TransformFromCopy(u, u_a_v))
        self.play(TransformFromCopy(v, menos_2v))
        self.play(GrowArrow(otra), Write(formula2))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición")
        definicion = VGroup(
            parrafo(r"Una \textbf{combinación lineal} de los vectores $\mathbf{v}_1, \dots, \mathbf{v}_k$", r"es cualquier suma de múltiplos suyos:", font_size=40, sangria=0.5),
            MathTex(r"c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k", font_size=56, color=COLOR_PIVOTE),
            Tex(r"Los números $c_1, \dots, c_k$ son los \textbf{coeficientes}; pueden ser cualquiera.", font_size=38),
            Tex(r"Con $\mathbf{u}$ y $\mathbf{v}$ de antes: $2\mathbf{u}+\mathbf{v}$ y $\mathbf{u}-2\mathbf{v}$ lo son.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(definicion, margen=0.5)
        self.decir("Una combinación lineal de los vectores ve uno, hasta ve ka, es cualquier suma de múltiplos suyos: ce uno por ve uno, más ce dos por ve dos, y así hasta ce ka por ve ka. Los números ce son los coeficientes, y pueden ser cualesquiera: positivos, negativos o cero. Las dos combinaciones de antes lo son.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La pregunta de los sistemas")
        sistema = VGroup(
            MathTex(r"c_1 \begin{bmatrix} 2 \\ 1 \end{bmatrix} + c_2 \begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}", font_size=52),
            MathTex(r"\begin{cases} 2c_1 - c_2 = 3 \\ c_1 + c_2 = 3 \end{cases}", font_size=52, color=COLOR_PIVOTE),
            Tex(r"Preguntar si un vector es combinación lineal de otros es preguntar si un sistema tiene solución.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(sistema, margen=0.5)
        self.decir("Y aquí aparecen los sistemas. Preguntar si el vector tres, tres es combinación de u y ve, es buscar coeficientes ce uno y ce dos que cumplan esta igualdad. Componente a componente, es un sistema de dos ecuaciones con dos incógnitas. Tiene solución, ce uno igual a dos y ce dos igual a uno, y por eso el vector sí es combinación lineal. Preguntar si un vector es combinación lineal de otros es preguntar si un sistema tiene solución.")
        for s in sistema:
            self.play(FadeIn(s))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F12-N2-01",
            VGroup(
                Text("¿Es b combinación lineal de u y v? Si lo es, halla los coeficientes.", font_size=TAM_TEXTO),
                MathTex(r"\mathbf{u} = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix},\ \mathbf{v} = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix},\ \mathbf{b} = \begin{bmatrix} 3 \\ 5 \\ 2 \end{bmatrix}", font_size=48),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: decide si el vector be es combinación lineal de u y ve, y si lo es, halla los coeficientes. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Combinación lineal: c₁v₁ + … + ckvk.",
                "Los coeficientes pueden ser cualquier número.",
                "«¿Es b combinación de los v?» es un sistema de ecuaciones.",
            ],
            "el espacio generado: todas las combinaciones a la vez.",
            voz="En resumen: una combinación lineal es una suma de múltiplos de vectores, con coeficientes cualesquiera. Y preguntar si un vector es combinación de otros es preguntar si un sistema tiene solución. Siguiente: el espacio generado, todas las combinaciones a la vez.",
        )


class EspacioGenerado(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 43 · Parte 2", "El espacio generado")
        titulo = self.encabezado("Todas las combinaciones de un vector")
        p = plano_vectores()
        u = flecha(p, 1, 2, COLOR_U)
        recta = Line(p.c2p(-1.5, -3), p.c2p(2, 4), color=COLOR_PIVOTE, stroke_width=6)
        puntos = VGroup(*[Dot(p.c2p(c, 2 * c), color=COLOR_PIVOTE, radius=0.07) for c in (-1, -0.5, 0.5, 1.5)])
        texto = VGroup(
            MathTex(r"\operatorname{gen}\{\mathbf{u}\} = \{\,c\,\mathbf{u} : c \in \mathbb{R}\,\}", font_size=44, color=COLOR_PIVOTE),
            Tex(r"Un solo vector: una \textbf{recta} por el origen.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(RIGHT, buff=0.6).shift(UP * 1.2)
        panel_derecha(texto)
        ajustar_al_encuadre(texto, margen=0.5)
        self.decir("Si tomamos un solo vector, u, todos sus múltiplos, c por u, forman una recta que pasa por el origen. Al conjunto de todas las combinaciones lineales de unos vectores se le llama el espacio generado por ellos.")
        self.play(Create(p))
        self.play(GrowArrow(u))
        self.play(Create(recta), LaggedStart(*[FadeIn(q, scale=2) for q in puntos], lag_ratio=0.3), FadeIn(texto))
        self.wait(2)

        w = flecha(p, 2, 4, COLOR_V)
        nota = parrafo(r"$\mathbf{w} = 2\mathbf{u}$ no añade nada:", r"$\operatorname{gen}\{\mathbf{u}, \mathbf{w}\}$ sigue siendo la misma recta.", font_size=38, sangria=0.4).to_edge(RIGHT, buff=0.6).shift(DOWN * 1.4)
        panel_derecha(nota)
        ajustar_al_encuadre(nota, margen=0.5)
        self.decir("Si añadimos otro vector que ya es un múltiplo del primero, como uve doble igual a dos u, no ganamos nada: el espacio generado sigue siendo la misma recta.")
        self.play(GrowArrow(w), FadeIn(nota))
        self.wait(2.5)
        self.play(FadeOut(w), FadeOut(nota), FadeOut(recta), *[FadeOut(q) for q in puntos])

        v = flecha(p, 2, 1, COLOR_V)
        plano_total = Rectangle(width=p.x_length, height=p.y_length, color=COLOR_PIVOTE, fill_color=COLOR_PIVOTE, fill_opacity=0.18, stroke_width=3).move_to(p.get_center())
        texto2 = VGroup(
            MathTex(r"\operatorname{gen}\{\mathbf{u}, \mathbf{v}\} = \mathbb{R}^2", font_size=48, color=COLOR_PIVOTE),
            parrafo(r"Dos vectores que no son múltiplos:", r"\textbf{todo el plano}.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).to_edge(RIGHT, buff=0.6).shift(UP * 1.2)
        panel_derecha(texto2)
        ajustar_al_encuadre(texto2, margen=0.5)
        self.decir("En cambio, con un segundo vector que apunta en otra dirección, ve, dos y uno, ya podemos llegar a cualquier punto del plano: el espacio generado es todo el plano.")
        self.play(FadeOut(texto), GrowArrow(v))
        self.play(FadeIn(plano_total), FadeIn(texto2))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición y lo que se espera en el espacio")
        definicion = VGroup(
            MathTex(r"\operatorname{gen}\{\mathbf{v}_1, \dots, \mathbf{v}_k\} = \{\, c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k : c_i \in \mathbb{R} \,\}", font_size=40, color=COLOR_PIVOTE),
            Tex(r"En $\mathbb{R}^3$: un vector da una recta; dos que no son múltiplos, un plano;", font_size=36),
            Tex(r"tres que no están en un mismo plano, todo $\mathbb{R}^3$.", font_size=36),
            Tex(r"Siempre pasa por el origen: todos los coeficientes cero dan $\mathbf{0}$.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(definicion, margen=0.5)
        self.decir("El espacio generado por ve uno, hasta ve ka, es el conjunto de todas sus combinaciones lineales. En el espacio de tres dimensiones, un vector genera una recta; dos que no son múltiplos, un plano; y tres que no están en un mismo plano, todo el espacio. Siempre pasa por el origen, porque con todos los coeficientes cero se obtiene el vector nulo.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Pertenecer al espacio generado")
        regla = VGroup(
            MathTex(r"\mathbf{b} \in \operatorname{gen}\{\mathbf{v}_1, \dots, \mathbf{v}_k\}", font_size=50, color=COLOR_PIVOTE),
            MathTex(r"\iff \; [\,\mathbf{v}_1 \ \cdots \ \mathbf{v}_k \mid \mathbf{b}\,] \text{ tiene solución}", font_size=46),
            MathTex(r"\iff \; \operatorname{rg}[\,\mathbf{v}_1 \cdots \mathbf{v}_k\,] = \operatorname{rg}[\,\mathbf{v}_1 \cdots \mathbf{v}_k \mid \mathbf{b}\,]", font_size=44),
            Tex(r"La última equivalencia es el teorema de Rouché-Frobenius (L40).", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(regla, margen=0.5)
        self.decir("Para saber si be pertenece al espacio generado por unos vectores, se forma la matriz que tiene esos vectores por columnas, se le añade la columna be, y se pregunta si el sistema tiene solución. Por Rouché-Frobenius, esto ocurre justo cuando el rango de la matriz de vectores coincide con el de la matriz aumentada.")
        for r in regla:
            self.play(FadeIn(r))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F12-N2-02",
            VGroup(
                Text("Describe geométricamente el espacio generado en cada caso:", font_size=TAM_TEXTO),
                MathTex(r"\text{a) } \left\{\begin{bmatrix}1\\2\end{bmatrix}, \begin{bmatrix}2\\4\end{bmatrix}\right\} \qquad \text{b) } \left\{\begin{bmatrix}1\\2\end{bmatrix}, \begin{bmatrix}2\\1\end{bmatrix}\right\}", font_size=44),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: describe geométricamente el espacio generado por cada una de estas dos parejas de vectores. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "gen{v₁,…,vk} = todas las combinaciones lineales.",
                "Un vector: recta; dos independientes: plano.",
                "b está en el generado ⇔ el sistema [V | b] tiene solución.",
            ],
            "Lección 44 — independencia lineal, base y dimensión.",
            voz="En resumen: el espacio generado es el conjunto de todas las combinaciones lineales. Un vector genera una recta, y dos que no son múltiplos, un plano. Y be está en el generado exactamente cuando el sistema correspondiente tiene solución. Siguiente: lección cuarenta y cuatro, independencia lineal, base y dimensión.",
        )
