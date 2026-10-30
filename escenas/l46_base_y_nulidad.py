"""Lección 46 — Base del núcleo y nulidad.

Escenas (un video cada una):
    VariablesLibresDanLaBase, Nulidad

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l46_base_y_nulidad.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A_TEX = r"\begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}"


class VariablesLibresDanLaBase(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 46 · Parte 1", "Una base del núcleo")
        titulo = self.encabezado("Resolver A x = 0 hasta el final")
        a = MathTex(r"A = " + A_TEX, font_size=42).next_to(titulo, DOWN, buff=0.45).to_edge(LEFT, buff=0.8)
        self.decir("Vamos a encontrar el núcleo de esta matriz de tres por cuatro, la misma de antes. Resolvemos el sistema homogéneo, y para eso la llevamos a su forma reducida.")
        self.play(Write(a))
        self.wait(1)
        reducida = matriz_gauss([[1, 2, 0, 1, 0], [0, 0, 1, 2, 0], [0, 0, 0, 0, 0]], pivotes=[(0, 0), (1, 2)], escala=0.85).next_to(a, RIGHT, buff=0.9)
        ajustar_al_encuadre(VGroup(a, reducida), margen=0.5)
        self.play(FadeIn(reducida))
        self.play(Create(escalera(reducida, [(0, 0), (1, 2)])))
        nota = Tex(r"Columnas con pivote: 1 y 3. Sin pivote: 2 y 4 $\Rightarrow$ $x_2$ y $x_4$ son libres.", font_size=38, color=COLOR_LIBRE).next_to(VGroup(a, reducida), DOWN, buff=0.7).set_x(0)
        ajustar_al_encuadre(nota, margen=0.5)
        self.decir("La reducida tiene pivotes en las columnas uno y tres. Las columnas dos y cuatro no tienen pivote: sus variables, equis dos y equis cuatro, son libres.")
        self.play(FadeIn(nota))
        self.wait(2)

        despeje = VGroup(
            MathTex(r"x_1 = -2x_2 - x_4", font_size=48),
            MathTex(r"x_3 = -2x_4", font_size=48),
            MathTex(r"x_2 = s,\quad x_4 = t \ \text{ (libres)}", font_size=44, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(nota, DOWN, buff=0.6).set_x(0)
        ajustar_al_encuadre(VGroup(a, reducida, nota, despeje), margen=0.5)
        self.decir("Despejamos las variables básicas en función de las libres: equis uno es menos dos equis dos menos equis cuatro; equis tres es menos dos equis cuatro. Llamamos ese y te a las dos libres.")
        for d in despeje:
            self.play(FadeIn(d))
            self.wait(1.5)
        self.wait(1)
        self.limpiar(titulo)

        general = VGroup(
            MathTex(r"\mathbf{x} = \begin{bmatrix} -2s - t \\ s \\ -2t \\ t \end{bmatrix} = s\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + t\begin{bmatrix} -1 \\ 0 \\ -2 \\ 1 \end{bmatrix}", font_size=50),
            MathTex(r"\ker A = \operatorname{gen}\{\mathbf{n}_1, \mathbf{n}_2\}", font_size=50, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.6).next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(general, margen=0.5)
        self.decir("Escribimos la solución general como vector, y separamos lo que acompaña a ese de lo que acompaña a te. Queda ese por el vector menos dos, uno, cero, cero, más te por el vector menos uno, cero, menos dos, uno. El núcleo es el espacio generado por esos dos vectores, ene uno y ene dos.")
        self.play(Write(general[0]))
        self.wait(2)
        self.play(FadeIn(general[1]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Por qué son una base?")
        razones = VGroup(
            parrafo(r"\textbf{Generan} $\ker A$: toda solución es de la forma $s\,\mathbf{n}_1 + t\,\mathbf{n}_2$", r"(es justo lo que salió al resolver).", font_size=38, sangria=0.5),
            parrafo(r"Son \textbf{independientes}: en las posiciones de las variables libres", r"(2 y 4) valen $(1, 0)$ y $(0, 1)$. Si $s\,\mathbf{n}_1 + t\,\mathbf{n}_2 = \mathbf{0}$,", r"mirando las componentes 2 y 4 queda $s = 0$ y $t = 0$.", font_size=38, sangria=0.5),
            MathTex(r"\{\mathbf{n}_1, \mathbf{n}_2\} \text{ es una base de } \ker A,\quad \dim\ker A = 2", font_size=48, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(razones, margen=0.5)
        self.decir("¿Por qué son una base? Primero, generan el núcleo: toda solución tiene esa forma, porque así la obtuvimos. Segundo, son independientes: en las posiciones de las variables libres, la dos y la cuatro, valen uno, cero para el primero y cero, uno para el segundo. Si ese por ene uno más te por ene dos es el vector nulo, mirando esas dos componentes queda ese igual a cero y te igual a cero. Así, ene uno y ene dos forman una base, y el núcleo tiene dimensión dos.")
        for r in razones:
            self.play(FadeIn(r))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Receta")
        receta = VGroup(
            Tex(r"1.\ Reduce $[A \mid \mathbf{0}]$ (la columna de ceros no cambia: basta reducir $A$).", font_size=38),
            Tex(r"2.\ Localiza las variables libres (columnas sin pivote).", font_size=38),
            Tex(r"3.\ Por cada variable libre: ponla igual a $1$, las otras libres a $0$,", font_size=38),
            Tex(r"\hspace{1.3em} y calcula las básicas. Cada vector así obtenido es un elemento de la base.", font_size=38),
            Tex(r"4.\ Esos vectores son una base de $\ker A$.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(receta, margen=0.5)
        self.decir("Resumimos la receta. Uno: se reduce la matriz; la columna de ceros no cambia, basta reducir a. Dos: se localizan las variables libres. Tres: por cada variable libre, se pone ella igual a uno y las otras libres a cero, y se calculan las básicas; cada vector así obtenido es un elemento de la base. Cuatro: esos vectores son una base del núcleo.")
        for r in receta:
            self.play(FadeIn(r))
            self.wait(2.2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F13-N3-02",
            VGroup(
                Text("Halla una base del núcleo y su dimensión:", font_size=TAM_TEXTO),
                MathTex(r"B = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla una base del núcleo de esta matriz y su dimensión. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Cada variable libre aporta un vector a la base del núcleo.",
                "Generan (así se obtuvo la solución) y son independientes (unos y ceros en las libres).",
                "dim ker A = número de variables libres.",
            ],
            "la nulidad y su relación con el rango.",
            voz="En resumen: cada variable libre aporta un vector a la base del núcleo. Generan, porque así se obtuvo la solución, y son independientes, por los unos y ceros en las posiciones libres. Y la dimensión del núcleo es el número de variables libres. Siguiente: la nulidad y su relación con el rango.",
        )


class Nulidad(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 46 · Parte 2", "La nulidad")
        titulo = self.encabezado("Contar las variables libres")
        defin = VGroup(
            parrafo(r"La \textbf{nulidad} de $A$ es la dimensión de su núcleo:", font_size=40, sangria=0.4),
            MathTex(r"\operatorname{nul}(A) = \dim \ker A = \text{número de variables libres}", font_size=46, color=COLOR_LIBRE),
            Tex(r"Cada columna de $A$ tiene pivote o es libre, y los pivotes son el rango:", font_size=38),
            MathTex(r"\operatorname{nul}(A) = n - \operatorname{rg}(A)", font_size=64, color=COLOR_PIVOTE),
            Tex(r"con $n$ el número de columnas (de incógnitas).", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(defin, margen=0.5)
        self.decir("La nulidad de a es la dimensión de su núcleo, y como cada variable libre aporta un vector a la base, es el número de variables libres. Ahora bien: cada columna de a, o tiene pivote, o es libre; y el número de pivotes es el rango. Por eso, la nulidad es ene menos el rango, donde ene es el número de columnas, es decir, de incógnitas.")
        for d in defin:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Tres ejemplos")
        filas = VGroup(
            VGroup(MathTex(r"A \ (3\times 4)", font_size=40), MathTex(r"\operatorname{rg} = 2", font_size=40), MathTex(r"\operatorname{nul} = 4 - 2 = 2", font_size=40, color=COLOR_LIBRE), Tex(r"$\ker A$: un plano", font_size=36)),
            VGroup(MathTex(r"B \ (2\times 3)", font_size=40), MathTex(r"\operatorname{rg} = 2", font_size=40), MathTex(r"\operatorname{nul} = 3 - 2 = 1", font_size=40, color=COLOR_LIBRE), Tex(r"$\ker B$: una recta", font_size=36)),
            VGroup(MathTex(r"C \ (3\times 2)", font_size=40), MathTex(r"\operatorname{rg} = 2", font_size=40), MathTex(r"\operatorname{nul} = 2 - 2 = 0", font_size=40, color=COLOR_LIBRE), Tex(r"$\ker C = \{\mathbf{0}\}$", font_size=36)),
        )
        for f in filas:
            f.arrange(RIGHT, buff=0.9)
        tabla = VGroup(*filas).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        # columnas alineadas: cada celda empieza donde empieza la misma celda de la primera fila
        for f in filas[1:]:
            for celda, ref in zip(f, filas[0]):
                celda.align_to(ref, LEFT)
        tabla.next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(tabla, margen=0.5)
        self.decir("Tres ejemplos. La matriz a, de tres por cuatro, tiene rango dos, así que su nulidad es cuatro menos dos, dos: el núcleo es un plano dentro del espacio de cuatro dimensiones. La matriz be, de dos por tres, también tiene rango dos: nulidad uno, una recta. Y la matriz ce, de tres por dos, con rango dos, tiene nulidad cero: su núcleo es solo el vector nulo.")
        for f in filas:
            self.play(FadeIn(f))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Consecuencias")
        consecuencias = VGroup(
            parrafo(r"$\ker A = \{\mathbf{0}\} \iff \operatorname{nul}(A) = 0 \iff \operatorname{rg}(A) = n$", r"(todas las columnas con pivote: el sistema homogéneo solo tiene la solución trivial).", font_size=36, sangria=0.5),
            parrafo(r"Si $m < n$ (menos ecuaciones que incógnitas): $\operatorname{nul}(A) \ge n - m > 0$.", r"Un sistema homogéneo con más incógnitas que ecuaciones \textbf{siempre} tiene soluciones no triviales.", font_size=36, sangria=0.5),
            parrafo(r"Sistema $A\mathbf{x} = \mathbf{b}$ compatible: es determinado $\iff \operatorname{nul}(A) = 0$.", r"(Es el criterio de Rouché-Frobenius de L40, escrito con la nulidad.)", font_size=36, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(consecuencias, margen=0.5)
        self.decir("De aquí salen varias consecuencias. El núcleo es solo el vector nulo exactamente cuando el rango es ene, es decir, cuando todas las columnas tienen pivote. Si hay menos ecuaciones que incógnitas, la nulidad es al menos ene menos eme, positiva: un sistema homogéneo con más incógnitas que ecuaciones siempre tiene soluciones distintas de la trivial. Y un sistema compatible es determinado justo cuando la nulidad es cero, que es el criterio de Rouché-Frobenius escrito con la nulidad.")
        for c in consecuencias:
            self.play(FadeIn(c))
            self.wait(3.2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F13-N3-04",
            VGroup(
                Text("Una matriz tiene 2 filas y 5 columnas.", font_size=TAM_TEXTO),
                Text("¿Qué puedes decir de la nulidad? ¿Y de su rango?", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: una matriz tiene dos filas y cinco columnas. ¿Qué puedes decir de su nulidad, y de su rango? Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "nul(A) = dim ker A = número de variables libres.",
                "nul(A) = n − rg(A).",
                "Más incógnitas que ecuaciones: siempre hay soluciones no triviales.",
            ],
            "Lección 47 — la estructura de las soluciones: x = xp + n.",
            voz="En resumen: la nulidad es la dimensión del núcleo, el número de variables libres, y es ene menos el rango. Con más incógnitas que ecuaciones siempre hay soluciones no triviales. Siguiente: lección cuarenta y siete, la estructura de las soluciones de un sistema cualquiera.",
        )
