"""Lección 4 — Lenguaje matemático: conjuntos, subíndices, sumatorios, lógica y demostraciones.

Escenas (un video cada una):
    ConjuntosYPertenencia, SubindicesYSumatorio, ImplicacionYEquivalencia, ComoSeDemuestraAlgo

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l04_lenguaje_matematico.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def presentar_lineas(escena: Scene, lineas, espera=1.8):
    for linea in lineas:
        escena.play(FadeIn(linea, shift=RIGHT * 0.2))
        escena.wait(espera)


class ConjuntosYPertenencia(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 4 · Parte 1", "Conjuntos")

        # Extensión y pertenencia.
        titulo = self.encabezado("Un conjunto es una colección de objetos")
        bolsa = Ellipse(width=4.5, height=3, color=COLOR_COEFICIENTE).shift(LEFT * 3)
        nombre = MathTex("A", font_size=56, color=COLOR_COEFICIENTE).next_to(bolsa, UL, buff=-0.2)
        elementos = VGroup(*[MathTex(str(k), font_size=50) for k in (1, 2, 3)]).arrange(RIGHT, buff=0.8).move_to(bolsa)
        fuera = MathTex("5", font_size=50).next_to(bolsa, RIGHT, buff=0.8)
        self.decir("Un conjunto es una colección de objetos. Este conjunto, a, tiene tres elementos: uno, dos y tres.")
        self.play(Create(bolsa), Write(nombre), LaggedStart(*[FadeIn(e, scale=1.5) for e in elementos], lag_ratio=0.3))
        extension = MathTex(r"A = \{1,\ 2,\ 3\}", font_size=50).shift(RIGHT * 3 + UP * 1.2)
        self.decir("Si escribimos los elementos entre llaves, describimos el conjunto por extensión.")
        self.play(Write(extension))
        self.pie("Escribir los elementos entre llaves se llama describir el conjunto por EXTENSIÓN.", espera=2.5)
        pertenece = MathTex(r"2 \in A", font_size=50, color=COLOR_SOLUCION).next_to(extension, DOWN, buff=0.6)
        no_pertenece = MathTex(r"5 \notin A", font_size=50, color=COLOR_ERROR).next_to(pertenece, DOWN, buff=0.4)
        self.decir("El símbolo que parece una e redondeada significa: pertenece a. El dos pertenece a a.")
        self.play(Indicate(elementos[1], color=COLOR_SOLUCION), Write(pertenece))
        self.decir("Tachado significa: no pertenece a. El cinco no pertenece a a.")
        self.play(FadeIn(fuera), Write(no_pertenece))
        self.pie("∈ se lee «pertenece a»;  ∉, «no pertenece a».", espera=3)
        self.limpiar(titulo)

        # Comprensión.
        titulo = self.cambiar_encabezado(titulo, "Describir un conjunto por una propiedad")
        definicion = MathTex(r"S", "=", r"\{", r"x \in \mathbb{R}", r"\;:\;", r"2x + 1 = 7", r"\}", font_size=60).shift(UP * 1.2)
        self.decir("También se puede describir un conjunto con una propiedad.")
        self.play(Write(definicion))
        lecturas = [
            (3, "x es un número real", COLOR_COEFICIENTE),
            (4, "tal que", COLOR_SECUNDARIO),
            (5, "cumple esta condición", COLOR_TERMINO_INDEP),
        ]
        rotulos = VGroup()
        for indice, texto, color in lecturas:
            llave = Brace(definicion[indice], DOWN, color=color)
            rotulos.add(VGroup(llave, Text(texto, font_size=TAM_NOTA, color=color).next_to(llave, DOWN, buff=0.1)))
        rotulos[1][1].shift(DOWN * 0.5)  # cada rótulo en su propia altura para que no choquen
        rotulos[2][1].shift(DOWN * 1.0)
        self.decir("Esto se lee: los equis reales tales que dos equis más uno es igual a siete.")
        for r in rotulos:
            self.play(FadeIn(r))
            self.wait(0.8)
        resultado = MathTex(r"S = \{3\}", font_size=60, color=COLOR_SOLUCION).shift(DOWN * 1.8)
        self.decir("Es exactamente el conjunto solución de la ecuación: el conjunto que contiene solo al tres.")
        self.play(Write(resultado))
        self.pie("Así escribiremos los CONJUNTOS SOLUCIÓN: los valores que cumplen una condición.", espera=3)
        self.limpiar(titulo)

        # Vacío y subconjunto.
        titulo = self.cambiar_encabezado(titulo, "El conjunto vacío y los subconjuntos")
        lineas = VGroup(
            MathTex(r"\{x \in \mathbb{R} : x + 1 = x + 2\} = \varnothing", font_size=48),
            Tex(r"$\varnothing$: el conjunto vacío, sin elementos (la ecuación no tiene solución).", font_size=36),
            MathTex(r"\{x \in \mathbb{R} : 2(x + 1) = 2x + 2\} = \mathbb{R}", font_size=48),
            Tex(r"Todos los reales cumplen la condición (es una identidad).", font_size=36),
            MathTex(r"\{1, 2\} \subset \{1, 2, 3\} \qquad \mathbb{N} \subset \mathbb{Z}", font_size=48),
            Tex(r"$A \subset B$: todo elemento de $A$ es también elemento de $B$.", font_size=36),
        ).arrange(DOWN, buff=0.3)
        for i in (1, 3, 5):
            lineas[i].set_color(COLOR_SECUNDARIO)
            lineas[i].shift(UP * 0.1)
        self.decir("Si ningún número cumple la condición, obtenemos el conjunto vacío. Si todos la cumplen, obtenemos todos los reales. Y un conjunto es subconjunto de otro si todos sus elementos están también en el otro.")
        presentar_lineas(self, lineas, espera=1.5)
        self.wait(2)
        self.limpiar(titulo)

        # Intersección y sistemas.
        titulo = self.cambiar_encabezado(titulo, "Intersección: lo que está en los dos")
        c1 = Circle(radius=1.5, color=COLOR_COEFICIENTE, fill_opacity=0.15).shift(LEFT * 0.9)
        c2 = Circle(radius=1.5, color=COLOR_TERMINO_INDEP, fill_opacity=0.15).shift(RIGHT * 0.9)
        venn = VGroup(c1, c2, MathTex("A", color=COLOR_COEFICIENTE).next_to(c1, UL, buff=0), MathTex("B", color=COLOR_TERMINO_INDEP).next_to(c2, UR, buff=0))
        venn.shift(LEFT * 3.5 + UP * 0.2)
        comun = Intersection(c1, c2, color=COLOR_PIVOTE, fill_opacity=0.6)
        self.decir("La intersección de dos conjuntos contiene lo que está en los dos a la vez.")
        self.play(Create(venn))
        self.play(FadeIn(comun))
        definicion = MathTex(r"A \cap B = \{\, x : x \in A \text{ y } x \in B \,\}", font_size=40).next_to(venn, DOWN, buff=0.4)
        self.play(Write(definicion))

        plano = Axes(x_range=[-1, 4, 1], y_range=[-1, 4, 1], x_length=4, y_length=4).shift(RIGHT * 3.5 + UP * 0.2)
        r1 = plano.plot(lambda x: 3 - x, x_range=[-1, 4], color=COLOR_COEFICIENTE)
        r2 = plano.plot(lambda x: x - 1, x_range=[0, 4], color=COLOR_TERMINO_INDEP)
        punto = Dot(plano.c2p(2, 1), color=COLOR_PIVOTE, radius=0.1)
        rot_s1 = MathTex(r"S_1:\ x + y = 3", font_size=30, color=COLOR_COEFICIENTE).move_to(plano.c2p(2.3, 3.8))
        rot_s2 = MathTex(r"S_2:\ x - y = 1", font_size=30, color=COLOR_TERMINO_INDEP).move_to(plano.c2p(2.3, 3.2))
        self.decir("Y aquí está la conexión con los sistemas: las soluciones de un sistema son las que cumplen todas las ecuaciones a la vez.")
        self.play(Create(plano), Create(r1), Write(rot_s1))
        self.play(Create(r2), Write(rot_s2))
        self.decir("Es decir, la intersección de los conjuntos solución. Geométricamente, el punto donde se cortan las rectas.")
        self.play(FadeIn(punto, scale=3))
        conclusion = MathTex(r"S_1 \cap S_2 = \{(2, 1)\}", font_size=40, color=COLOR_PIVOTE).next_to(plano, DOWN, buff=0.4)
        self.play(Write(conclusion))
        self.pie(
            "El conjunto solución de un SISTEMA es la intersección de los conjuntos solución de sus ecuaciones.\n"
            "Ojo: {(2, 1)} es un conjunto con un elemento; (2, 1) es el elemento (el punto).",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F00-N1-08",
            VGroup(
                Text("Escribe por extensión cada conjunto:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \{x \in \mathbb{R} : 3x - 1 = 5\} \qquad \text{b) } \{x \in \mathbb{R} : x - 4 = x\} \qquad \text{c) } \{n \in \mathbb{N} : n < 4\}",
                    font_size=40,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Un conjunto se describe por extensión {1, 2, 3} o por una propiedad {x : ...}.",
                "Pertenencia: 2 ∈ A. Vacío: ∅. Subconjunto: A ⊂ B.",
                "Conjunto solución de un sistema = intersección de los de cada ecuación.",
            ],
            "subíndices y sumatorios.",
            voz="En resumen: un conjunto se describe por extensión, con sus elementos entre llaves, o por una propiedad. Hay que conocer la pertenencia, el conjunto vacío y los subconjuntos. Y el conjunto solución de un sistema es la intersección de los conjuntos solución de cada ecuación. Siguiente: subíndices y sumatorios.",
        )


class SubindicesYSumatorio(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 4 · Parte 2", "Subíndices y sumatorios")

        # Cuando se acaban las letras.
        titulo = self.encabezado("Cuando se acaban las letras")
        letras = MathTex("x,", "y,", "z,", "w,", r"\ \dots\ ?", font_size=60).shift(UP * 1.2)
        self.decir("Con muchas incógnitas se acaban las letras.")
        self.play(Write(letras))
        subindices = MathTex(r"x_1,\ x_2,\ x_3,\ \dots,\ x_n", font_size=60).next_to(letras, DOWN, buff=0.8)
        self.decir("La solución es numerarlas con subíndices: equis uno, equis dos, hasta equis ene.")
        self.play(Write(subindices))
        ejemplo = MathTex(r"2x_1 - x_2 + 4x_3 + x_4 = 7", font_size=52, color=COLOR_COEFICIENTE).next_to(subindices, DOWN, buff=0.8)
        self.play(Write(ejemplo))
        self.pie("Con subíndices podemos tener tantas incógnitas como haga falta: x₁ se lee «equis uno».", espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un subíndice es solo una etiqueta")
        comparacion = VGroup(
            VGroup(MathTex("x_2", font_size=64), Text("la incógnita número 2", font_size=TAM_NOTA, color=COLOR_SOLUCION)),
            VGroup(MathTex(r"x \cdot 2", font_size=64), Text("x multiplicado por 2", font_size=TAM_NOTA, color=COLOR_ERROR)),
            VGroup(MathTex("x^2", font_size=64), Text("x al cuadrado", font_size=TAM_NOTA, color=COLOR_ERROR)),
        )
        for c in comparacion:
            c.arrange(DOWN, buff=0.4)
        comparacion.arrange(RIGHT, buff=1.6)
        self.decir("Un subíndice no es una operación: equis sub dos es simplemente la segunda incógnita. No es equis por dos, ni equis al cuadrado.")
        presentar_lineas(self, comparacion, espera=1.2)
        self.pie("Son tres cosas distintas. El subíndice no opera: solo distingue.", espera=3)
        self.limpiar(titulo)

        # Doble subíndice.
        titulo = self.cambiar_encabezado(titulo, "Dos subíndices: fila y columna")
        tabla = VGroup(*[MathTex(f"a_{{{i}{j}}}", font_size=52) for i in range(1, 4) for j in range(1, 4)])
        tabla.arrange_in_grid(rows=3, cols=3, buff=(0.9, 0.5)).shift(LEFT * 2.5)
        self.decir("Con dos subíndices organizamos números en una tabla: el primero indica la fila, y el segundo, la columna.")
        self.play(LaggedStart(*[FadeIn(t) for t in tabla], lag_ratio=0.1))
        fila = SurroundingRectangle(VGroup(*tabla[3:6]), color=COLOR_COEFICIENTE)
        columna = SurroundingRectangle(VGroup(tabla[2], tabla[5], tabla[8]), color=COLOR_TERMINO_INDEP)
        self.decir("a dos tres está en la fila dos, columna tres.")
        self.play(Create(fila), Create(columna))
        self.play(tabla[5].animate.set_color(COLOR_PIVOTE).scale(1.2))
        explicacion = VGroup(
            MathTex(r"a_{23}", font_size=60, color=COLOR_PIVOTE),
            Tex(r"primer subíndice: \textbf{fila} 2", font_size=38, color=COLOR_COEFICIENTE),
            Tex(r"segundo subíndice: \textbf{columna} 3", font_size=38, color=COLOR_TERMINO_INDEP),
            Tex(r"$a_{23} \neq a_{32}$: el orden importa", font_size=38, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(RIGHT * 3)
        presentar_lineas(self, explicacion, espera=1.2)
        self.decir("Y no es lo mismo que a tres dos. Así nombraremos los números de una matriz, en la lección dieciséis.")
        self.play(Indicate(tabla[7], color=COLOR_ERROR))
        self.pie("Así se nombrarán los números de una matriz (Lección 16): a sub i j, fila i, columna j.", espera=4)
        self.limpiar(titulo)

        # Sumatorio.
        titulo = self.cambiar_encabezado(titulo, "El sumatorio Σ: una suma abreviada")
        suma = MathTex(r"\sum_{k=1}^{4}", "k", font_size=80).shift(LEFT * 3.5 + UP * 0.5)
        self.decir("La letra griega sigma significa: suma de. Debajo se indica dónde empieza el índice, y arriba, dónde termina.")
        self.play(Write(suma))
        partes = VGroup(
            Text("Σ: «suma de»", font_size=TAM_NOTA),
            Text("k: el índice, que va cambiando", font_size=TAM_NOTA),
            Text("abajo: dónde empieza (k = 1)", font_size=TAM_NOTA),
            Text("arriba: dónde termina (4)", font_size=TAM_NOTA),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(suma, DOWN, buff=0.6)
        presentar_lineas(self, partes, espera=0.8)
        desarrollo = MathTex("=", "1", "+", "2", "+", "3", "+", "4", "=", "10", font_size=64).next_to(suma, RIGHT, buff=0.4)
        contador = Integer(1, font_size=44, color=COLOR_PIVOTE)
        rot_contador = VGroup(MathTex("k =", font_size=44, color=COLOR_PIVOTE), contador).arrange(RIGHT).next_to(desarrollo, UP, buff=0.8)
        self.decir("Damos al índice los valores uno, dos, tres y cuatro, y sumamos: uno más dos más tres más cuatro, diez.")
        self.play(FadeIn(rot_contador), Write(desarrollo[0]))
        for k in range(1, 5):
            contador.set_value(k)
            indices = [1] if k == 1 else [2 * k - 2, 2 * k - 1]
            self.play(*[Write(desarrollo[i]) for i in indices], Indicate(contador), run_time=0.9)
        self.play(Write(desarrollo[8:]))
        self.wait(2)
        self.limpiar(titulo)
        mas = VGroup(
            MathTex(r"\sum_{k=1}^{3} k^2 = 1 + 4 + 9 = 14", font_size=44),
            MathTex(r"\sum_{j=1}^{3} a_j x_j = a_1x_1 + a_2x_2 + a_3x_3", font_size=44),
            MathTex(r"\sum_{j=1}^{3} a_j x_j = \sum_{k=1}^{3} a_k x_k", font_size=44),
        ).arrange(DOWN, buff=0.6).shift(DOWN * 0.2)
        notas = [
            "Lo que va detrás de Σ se calcula para cada valor del índice.",
            "Con subíndices: así se escribe el lado izquierdo de una ecuación lineal.",
            "El nombre del índice no importa (índice «mudo»).",
        ]
        self.decir("Lo que va detrás de sigma se calcula para cada valor del índice. Con subíndices, así se escribe el lado izquierdo de una ecuación lineal. Y el nombre del índice no importa: es un índice mudo.")
        for linea, nota in zip(mas, notas):
            self.play(Write(linea))
            self.pie(nota, espera=2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La ecuación lineal general (anticipo)")
        general = VGroup(
            MathTex(r"a_1x_1 + a_2x_2 + \dots + a_nx_n = b", font_size=56),
            MathTex(r"\Longleftrightarrow", font_size=56),
            MathTex(r"\sum_{j=1}^{n} a_j x_j = b", font_size=56),
        ).arrange(DOWN, buff=0.5)
        self.decir("Con sigma, la ecuación lineal general con ene incógnitas cabe en una línea: la suma de a jota por equis jota, con jota de uno a ene, es igual a be. La estudiaremos en la lección cinco.")
        self.play(Write(general[0]))
        self.play(Write(general[1]), Write(general[2]))
        self.pie("Esta es la forma de TODAS las ecuaciones lineales. La estudiaremos en la Lección 5.", espera=4)

        self.ejercicio_propuesto(
            "F00-N2-07",
            VGroup(
                MathTex(r"\text{a) } \sum_{k=1}^{5} (2k - 1)", font_size=44),
                MathTex(
                    r"\text{b) } \sum_{j=1}^{3} a_j x_j \ \text{ con } a_1 = 2,\ a_2 = -1,\ a_3 = 3,\ \ x_1 = 1,\ x_2 = 4,\ x_3 = -2",
                    font_size=40,
                ),
                MathTex(r"\text{c) Escribe con } \Sigma:\ \ 3 + 6 + 9 + 12", font_size=44),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4),
        )
        self.resumen(
            [
                "x1, x2, ..., xn (con subíndices): muchas incógnitas con una sola letra.",
                "a₂₃: fila 2, columna 3. El orden importa.",
                "Σ resume una suma: índice, inicio, final y lo que se suma.",
            ],
            "implicación y equivalencia.",
            voz="En resumen: con subíndices, equis uno, equis dos, hasta equis ene, tenemos muchas incógnitas con una sola letra. a dos tres está en la fila dos, columna tres, y el orden importa. Y sigma resume una suma: índice, inicio, final y lo que se suma. Siguiente: implicación y equivalencia.",
        )


class ImplicacionYEquivalencia(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 4 · Parte 3", "Implicación, equivalencia y condiciones")

        # Proposiciones.
        titulo = self.encabezado("Proposiciones: frases verdaderas o falsas")
        ejemplos = VGroup(
            Tex(r"``$2 + 1 = 3$'' \quad $\to$ \quad verdadera", font_size=42, color=COLOR_SOLUCION),
            Tex(r"``$5 < 2$'' \quad $\to$ \quad falsa", font_size=42, color=COLOR_ERROR),
            Tex(r"``$x = 3$ es solución de $2x + 1 = 7$'' \quad $\to$ \quad verdadera", font_size=42, color=COLOR_SOLUCION),
            Tex(r"``¿Qué hora es?'' \quad $\to$ \quad no es proposición", font_size=42, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        self.decir("Una proposición es una frase que es verdadera o falsa. Dos más uno es tres: verdadera. Cinco es menor que dos: falsa. Una pregunta no es una proposición.")
        presentar_lineas(self, ejemplos, espera=1.3)
        self.wait(2)
        self.limpiar(titulo)

        # Implicación y su recíproco.
        titulo = self.cambiar_encabezado(titulo, "«Si P, entonces Q»:  P ⇒ Q")
        directa = MathTex(r"x = 2", r"\;\Longrightarrow\;", r"x^2 = 4", font_size=60).shift(UP * 1.4)
        self.decir("La flecha doble significa: si, entonces. Si equis es dos, su cuadrado es cuatro: verdadero.")
        self.play(Write(directa))
        self.play(directa.animate.set_color(COLOR_SOLUCION))
        self.pie("Verdadera: siempre que x vale 2, su cuadrado vale 4.", espera=2.5)
        reciproca = MathTex(r"x^2 = 4", r"\;\Longrightarrow\;", r"x = 2", font_size=60).shift(DOWN * 0.2)
        self.decir("Al revés no: equis igual a menos dos también tiene cuadrado cuatro. Basta un contraejemplo para tumbar una implicación.")
        self.play(Write(reciproca))
        contra = MathTex(r"x = -2:\quad (-2)^2 = 4 \text{ pero } -2 \neq 2", font_size=44, color=COLOR_ERROR).next_to(reciproca, DOWN, buff=0.6)
        self.play(reciproca.animate.set_color(COLOR_ERROR), Write(contra))
        self.pie(
            "Falsa: x = -2 es un CONTRAEJEMPLO. Que P ⇒ Q sea cierta no dice nada de Q ⇒ P (el recíproco).",
            espera=5,
        )
        self.limpiar(titulo)

        # Suficiente y necesaria, con diagrama.
        titulo = self.cambiar_encabezado(titulo, "Condición suficiente y condición necesaria")
        grande = Ellipse(width=6, height=4, color=COLOR_TERMINO_INDEP, fill_opacity=0.12).shift(LEFT * 3 + DOWN * 0.3)
        chica = Ellipse(width=3, height=2, color=COLOR_COEFICIENTE, fill_opacity=0.25).move_to(grande).shift(LEFT * 0.8 + DOWN * 0.3)
        rot_grande = Text("números pares (Q)", font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP).next_to(grande, UP, buff=0.1)
        rot_chica = Text("múltiplos de 4 (P)", font_size=TAM_NOTA - 2, color=COLOR_COEFICIENTE).move_to(chica)
        seis = MathTex("6", font_size=40).move_to(grande.get_center() + RIGHT * 1.9 + UP * 0.6)
        self.decir("Ser múltiplo de cuatro implica ser par.")
        self.play(Create(grande), FadeIn(rot_grande))
        self.decir("Decimos que ser múltiplo de cuatro es suficiente para ser par, y que ser par es necesario para ser múltiplo de cuatro.")
        self.play(Create(chica), FadeIn(rot_chica))
        explicacion = VGroup(
            MathTex(r"P \Longrightarrow Q", font_size=52),
            Tex(r"$P$ es \textbf{suficiente} para $Q$:\\ basta saber que $n$ es múltiplo de 4\\ para asegurar que es par.", font_size=34),
            Tex(r"$Q$ es \textbf{necesaria} para $P$:\\ si $n$ no es par, no puede ser múltiplo de 4.", font_size=34),
            Tex(r"$Q$ no es suficiente: $6$ es par\\ y no es múltiplo de 4.", font_size=34, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(RIGHT, buff=0.6)
        presentar_lineas(self, explicacion[:3], espera=2.5)
        self.decir("Pero no es suficiente: seis es par y no es múltiplo de cuatro.")
        self.play(FadeIn(seis, scale=2), FadeIn(explicacion[3]))
        self.wait(3)
        self.decir("Fuera de las matemáticas: ser mayor de edad es necesario para votar, pero no suficiente.")
        self.pie("Fuera de las matemáticas: ser mayor de edad es NECESARIO para votar, pero no SUFICIENTE.", espera=4)
        self.limpiar(titulo)

        # Equivalencia y contrarrecíproco.
        titulo = self.cambiar_encabezado(titulo, "Equivalencia: «si y solo si»  P ⇔ Q")
        bloque = VGroup(
            MathTex(r"P \Longleftrightarrow Q \quad\text{significa}\quad (P \Rightarrow Q) \text{ y } (Q \Rightarrow P)", font_size=44),
            MathTex(r"2x + 1 = 7 \;\Longleftrightarrow\; x = 3", font_size=50, color=COLOR_SOLUCION),
            Tex(r"Cada una es condición \textbf{necesaria y suficiente} para la otra.", font_size=38),
            Tex(r"Por eso, en la Lección 2, ``ecuaciones equivalentes'' = mismas soluciones.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).shift(UP * 0.8)
        self.decir("Cuando la implicación vale en los dos sentidos, decimos: si y solo si. Cada afirmación es condición necesaria y suficiente para la otra. Eso es lo que significaba que dos ecuaciones fueran equivalentes.")
        presentar_lineas(self, bloque, espera=2)
        contrarreciproco = VGroup(
            Tex(r"Contrarrecíproco: \quad $(P \Rightarrow Q)$ \ dice lo mismo que \ $(\text{no } Q \Rightarrow \text{no } P)$", font_size=38),
            Tex(r"``si $n$ es múltiplo de 4, es par'' $=$ ``si $n$ no es par, no es múltiplo de 4''", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.3).next_to(bloque, DOWN, buff=0.6)
        self.decir("Una implicación dice lo mismo que su contrarrecíproco: si un número no es par, no es múltiplo de cuatro.")
        presentar_lineas(self, contrarreciproco, espera=2.5)
        self.decir("Más adelante, el teorema de Rouché-Frobenius será justamente un si y solo si que decide si un sistema tiene solución.")
        self.pie(
            "Anticipo (Lección 40): un sistema tiene solución ⇔ rango(A) = rango([A | b]).\n"
            "Ese «si y solo si» será la clave para clasificar sistemas.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F00-N3-04",
            VGroup(
                Tex(r"¿$P$ es condición necesaria, suficiente, ambas o ninguna para $Q$?", font_size=40),
                MathTex(
                    r"\text{a) } P: x = 3,\ \ Q: x^2 = 9 \qquad \text{b) } P: x > 0,\ \ Q: x > 5 \qquad \text{c) } P: 2x = 6,\ \ Q: x = 3",
                    font_size=38,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "P ⇒ Q: si P es cierta, Q también. El recíproco puede fallar.",
                "En P ⇒ Q, P es suficiente para Q y Q es necesaria para P.",
                "P ⇔ Q: ambas implicaciones; condición necesaria y suficiente.",
                "Un solo contraejemplo basta para refutar una implicación.",
            ],
            "cómo se demuestra algo.",
            voz="En resumen: pe implica cu significa que, si pe es cierta, cu también; el recíproco puede fallar. En esa implicación, pe es suficiente para cu, y cu es necesaria para pe. Si y solo si significa las dos implicaciones: condición necesaria y suficiente. Y un solo contraejemplo basta para refutar una implicación. Siguiente: cómo se demuestra algo.",
        )


class ComoSeDemuestraAlgo(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 4 · Parte 4", "¿Cómo se demuestra algo?")

        # Los ejemplos no demuestran.
        titulo = self.encabezado("Comprobar ejemplos no es demostrar")
        afirmacion = Tex(r"Afirmación: ``$n^2 + n + 41$ es primo para todo natural $n$''", font_size=42).shift(UP * 2)
        self.decir("Esta fórmula, ene al cuadrado más ene más cuarenta y uno, da números primos para ene igual a cero, uno, dos, y así hasta treinta y nueve. Parece una ley.")
        self.play(Write(afirmacion))
        filas = VGroup(
            *[
                MathTex(rf"n = {n}:\ \ {n * n + n + 41}\ \checkmark", font_size=38, color=COLOR_SOLUCION)
                for n in range(0, 6)
            ]
        ).arrange_in_grid(rows=2, cols=3, buff=(1.0, 0.4)).next_to(afirmacion, DOWN, buff=0.6)
        presentar_lineas(self, filas, espera=0.4)
        self.pie("Seis ejemplos, todos primos... ¿ya está demostrado?", espera=2)
        fallo = MathTex(r"n = 40:\ \ 40^2 + 40 + 41 = 1681 = 41 \cdot 41", font_size=48, color=COLOR_ERROR)
        fallo.next_to(filas, DOWN, buff=0.8)
        self.decir("Pero para ene igual a cuarenta da mil seiscientos ochenta y uno, que es cuarenta y uno al cuadrado. Los ejemplos, por muchos que sean, no demuestran un para todo.")
        self.play(Write(fallo))
        self.pie(
            "1681 no es primo: n = 40 es un CONTRAEJEMPLO y la afirmación es falsa.\n"
            "Para afirmar «para todo n» hace falta un argumento que valga para todos, no ejemplos.",
            espera=6,
        )
        self.limpiar(titulo)

        # Demostración directa.
        titulo = self.cambiar_encabezado(titulo, "Demostración directa")
        pasos = VGroup(
            Tex(r"\textbf{Afirmación}: la suma de dos números pares es par.", font_size=40),
            Tex(r"\textbf{Definición}: $n$ es par si $n = 2k$ para algún entero $k$.", font_size=38, color=COLOR_SECUNDARIO),
            Tex(r"1. Sean $a$ y $b$ pares: \ $a = 2k$, \ $b = 2m$ \ ($k, m$ enteros).", font_size=40),
            Tex(r"2. Entonces \ $a + b = 2k + 2m = 2(k + m)$ \ (distributiva).", font_size=40),
            Tex(r"3. $k + m$ es entero, así que $a + b$ es par. \quad $\blacksquare$", font_size=40, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        self.decir("Una demostración directa parte de las definiciones: un número es par si es dos por un entero. Escribimos a y be así, sumamos, sacamos factor común, y obtenemos dos por un entero. Cada paso tiene una justificación.")
        presentar_lineas(self, pasos, espera=2.2)
        self.pie("Cada paso se justifica con una definición o una propiedad ya conocida. El cuadrado del final indica que la prueba terminó.", espera=4)
        self.limpiar(titulo)

        # Reducción al absurdo: raíz de 2.
        titulo = self.cambiar_encabezado(titulo, "Reducción al absurdo: √2 no es una fracción")
        pasos = VGroup(
            Tex(r"1. Supongamos lo contrario: $\sqrt{2} = \frac{p}{q}$ \textbf{irreducible} ($p, q$ enteros, $q \neq 0$).", font_size=34),
            Tex(r"2. Elevando al cuadrado: $2 = \frac{p^2}{q^2}$, \ es decir, \ $p^2 = 2q^2$. \ Así que $p^2$ es par.", font_size=34),
            Tex(r"3. $p$ no puede ser impar (impar $\cdot$ impar $=$ impar), así que $p = 2k$.", font_size=34),
            Tex(r"4. Sustituyendo: $4k^2 = 2q^2$, \ o sea \ $q^2 = 2k^2$. \ Entonces $q^2$ es par, y $q$ también.", font_size=34),
            Tex(r"5. $p$ y $q$ son pares: tienen el factor común 2. \textbf{¡Contradicción!}", font_size=34, color=COLOR_ERROR),
            Tex(r"6. La suposición era falsa: $\sqrt{2}$ no es racional. \quad $\blacksquare$", font_size=34, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        self.decir("En la reducción al absurdo suponemos lo contrario de lo que queremos probar. Si raíz de dos fuera una fracción irreducible, pe entre cu, al elevar al cuadrado, pe al cuadrado sería el doble de cu al cuadrado, luego pe sería par. Sustituyendo, cu también sería par. Pero entonces la fracción no era irreducible: contradicción. Luego raíz de dos no es una fracción.")
        presentar_lineas(self, pasos, espera=3)
        self.pie(
            "Idea: suponer lo contrario de lo que queremos probar y llegar a algo imposible.\n"
            "(Irreducible = sin factores comunes. Toda fracción se puede simplificar hasta serlo: el paso 1 es legítimo.)",
            espera=6,
        )
        self.limpiar(titulo)

        # Intuición frente a demostración.
        titulo = self.cambiar_encabezado(titulo, "Intuición visual y demostración")
        ideas = VGroup(
            Text("En la Lección 1, un dibujo nos dijo DÓNDE está √2 en la recta.", font_size=TAM_TEXTO),
            Text("Hoy hemos DEMOSTRADO que no es una fracción.", font_size=TAM_TEXTO),
            Text("En este curso, cada animación ayuda a entender;\nlas demostraciones aparecerán por separado, con sus hipótesis.", font_size=TAM_TEXTO, color=COLOR_PIVOTE, line_spacing=1.1),
        ).arrange(DOWN, buff=0.6)
        self.decir("En la lección uno, un dibujo nos dijo dónde está raíz de dos. Hoy hemos demostrado que no es una fracción. En este curso, las animaciones ayudan a entender; las demostraciones van aparte, con sus hipótesis.")
        presentar_lineas(self, ideas, espera=2.5)
        self.wait(2)

        self.ejercicio_propuesto(
            "F00-N5-04",
            VGroup(
                Tex(r"a) Demuestra que la suma de dos números impares es par.", font_size=40),
                Tex(r"b) Refuta con un contraejemplo: ``si $x^2 > 4$, entonces $x > 2$''.", font_size=40),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4),
        )
        self.resumen(
            [
                "Los ejemplos no demuestran un «para todo»; un contraejemplo sí lo refuta.",
                "Demostración directa: de las hipótesis a la conclusión, paso a paso.",
                "Reducción al absurdo: suponer lo contrario y llegar a una contradicción.",
                "Una animación es intuición, no demostración.",
            ],
            "Unidad 1, Lección 5 — ¿qué es una ecuación lineal?",
            voz="En resumen: los ejemplos no demuestran un para todo, pero un contraejemplo sí lo refuta. La demostración directa va de las hipótesis a la conclusión, paso a paso. La reducción al absurdo supone lo contrario y llega a una contradicción. Y una animación es intuición, no demostración. Siguiente: unidad uno, lección cinco: ¿qué es una ecuación lineal?",
        )
