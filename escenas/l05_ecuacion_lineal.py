"""Lección 5 — ¿Qué es una ecuación lineal?

Escenas (un video cada una):
    DefinicionEcuacionLineal, LinealVsNoLineal, TrampasDeLinealidad

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l05_ecuacion_lineal.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, ejes_iguales, recta_general  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class DefinicionEcuacionLineal(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 5 · Parte 1", "¿Qué es una ecuación lineal?")

        # Intuición: «lineal» viene de «línea».
        titulo = self.encabezado("«Lineal» viene de «línea»")
        sistema = ejes_iguales((-1, 4), (-1, 5), unidad=0.8).to_edge(LEFT, buff=1).shift(DOWN * 0.3)
        ecuacion = MathTex("2x + y = 4", font_size=52, color=COLOR_COEFICIENTE).to_edge(RIGHT, buff=1.5).shift(UP * 1.5)
        self.decir("Busquemos puntos que cumplan dos equis más ye igual a cuatro.")
        self.play(Create(sistema), Write(ecuacion))
        puntos = VGroup(*[Dot(sistema.c2p(x, 4 - 2 * x), color=COLOR_SOLUCION) for x in (-0.5, 0, 0.5, 1, 1.5, 2, 2.5)])
        self.decir("Están todos alineados: forman una recta.")
        self.play(LaggedStart(*[FadeIn(p, scale=2) for p in puntos], lag_ratio=0.2))
        self.play(Create(recta_general(sistema, 2, 1, 4, color=COLOR_SOLUCION)))
        self.decir("Por eso estas ecuaciones se llaman lineales: lineal viene de línea.")
        self.pie("Sus soluciones (los puntos que la cumplen) forman una recta. De ahí el nombre.", espera=3)
        self.limpiar(titulo)

        # Definición formal.
        titulo = self.cambiar_encabezado(titulo, "Definición")
        general = MathTex(
            "a_1", "x_1", "+", "a_2", "x_2", "+", r"\cdots", "+", "a_n", "x_n", "=", "b", font_size=64
        ).shift(UP * 1.2)
        for i in (0, 3, 8):
            general[i].set_color(COLOR_COEFICIENTE)
        general[11].set_color(COLOR_TERMINO_INDEP)
        self.decir("En general, una ecuación lineal tiene esta forma: cada incógnita, multiplicada por un número fijo, su coeficiente; todo sumado, e igualado a otro número fijo, el término independiente.")
        self.play(Write(general))
        partes = [
            (VGroup(general[1], general[4], general[9]), "incógnitas", WHITE, UP),
            (VGroup(general[0], general[3], general[8]), "coeficientes: números fijos", COLOR_COEFICIENTE, DOWN),
            (general[11], "término\nindependiente", COLOR_TERMINO_INDEP, DOWN),
        ]
        for grupo, nombre, color, lado in partes:
            marcas = VGroup(*[SurroundingRectangle(m, color=color, buff=0.06) for m in (grupo if isinstance(grupo, VGroup) else [grupo])])
            rotulo = Text(nombre, font_size=TAM_NOTA, color=color, line_spacing=1.0).next_to(general, lado, buff=0.5)
            rotulo.match_x(grupo)
            self.play(Create(marcas), FadeIn(rotulo))
            self.wait(1.2)
        regla = Text(
            "Las incógnitas solo se multiplican por números y se suman:\n"
            "sin potencias, sin productos entre ellas, sin dividir entre ellas, sin funciones (raíces, senos...).",
            font_size=TAM_NOTA,
            line_spacing=1.2,
        ).to_edge(DOWN, buff=1.0)
        self.decir("Las incógnitas solo pueden aparecer así: multiplicadas por números y sumadas. Nada de potencias, ni productos entre incógnitas, ni dividir entre ellas, ni raíces o senos.")
        self.play(FadeIn(regla))
        self.wait(5)
        self.limpiar(titulo)

        # Ejemplos llevados a la forma estándar.
        titulo = self.cambiar_encabezado(titulo, "Ejemplos: llevar a la forma a₁x + a₂y = b")
        ejemplos = [
            (r"3x - 2y = 7", r"3x - 2y = 7", r"a_1 = 3,\ a_2 = -2,\ b = 7"),
            (r"2x + 3 = 5y - x", r"3x - 5y = -3", r"a_1 = 3,\ a_2 = -5,\ b = -3"),
            (r"\tfrac{x}{2} + \tfrac{y}{3} = 1", r"\tfrac12 x + \tfrac13 y = 1", r"a_1 = \tfrac12,\ a_2 = \tfrac13,\ b = 1"),
            (r"\sqrt{2}\,x + \pi y = 0", r"\sqrt{2}\,x + \pi y = 0", r"a_1 = \sqrt{2},\ a_2 = \pi,\ b = 0"),
        ]
        filas = VGroup()
        for original, estandar, datos in ejemplos:
            fila = VGroup(
                MathTex(original, font_size=40),
                MathTex(r"\to", font_size=40, color=COLOR_SECUNDARIO),
                MathTex(estandar, font_size=40, color=COLOR_COEFICIENTE),
                MathTex(datos, font_size=34, color=COLOR_SECUNDARIO),
            ).arrange(RIGHT, buff=0.5)
            filas.add(fila)
        filas.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        ajustar_al_encuadre(filas)
        self.decir("Para reconocer los coeficientes, pasamos todas las incógnitas a un lado. Tres equis menos dos ye igual a siete ya está en esa forma. Dos equis más tres igual a cinco ye menos equis se convierte en tres equis menos cinco ye igual a menos tres. Los coeficientes pueden ser fracciones, como un medio y un tercio, o incluso raíz de dos o pi.")
        for fila in filas:
            self.play(Write(fila[0]))
            self.play(FadeIn(fila[1]), TransformFromCopy(fila[0], fila[2]))
            self.play(FadeIn(fila[3]))
            self.wait(1.2)
        self.decir("Lo que importa es cómo aparecen las incógnitas, no qué números las acompañan.")
        self.pie(
            "En el 2.º ejemplo se pasan todas las incógnitas a un lado (reglas de la Lección 2).\n"
            "Los coeficientes pueden ser fracciones o irracionales: lo que importa es cómo aparecen las incógnitas.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F01-N1-01",
            VGroup(
                Tex(r"Escribe en la forma $a_1x + a_2y + a_3z = b$ e indica coeficientes y término independiente:", font_size=38),
                MathTex(r"\text{a) } 4x = 2y - z + 3 \qquad \text{b) } \frac{x - y}{2} = z \qquad \text{c) } 5 = x", font_size=44),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Ecuación lineal: a1·x1 + a2·x2 + ... + an·xn = b.",
                "Coeficientes y término independiente son números fijos.",
                "Las incógnitas solo aparecen multiplicadas por números y sumadas.",
                "Con dos incógnitas, sus soluciones forman una recta.",
            ],
            "cómo distinguir lo lineal de lo que no lo es.",
            voz="En resumen: una ecuación lineal tiene la forma a uno equis uno, más a dos equis dos, y así hasta a ene equis ene, igual a be. Los coeficientes y el término independiente son números fijos. Las incógnitas solo aparecen multiplicadas por números y sumadas. Y con dos incógnitas, sus soluciones forman una recta. Siguiente: cómo distinguir lo lineal de lo que no lo es.",
        )


class LinealVsNoLineal(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 5 · Parte 2", "Lineal o no lineal")
        titulo = self.encabezado("Clasifiquemos")
        col_si = Text("Lineales", font_size=34, color=COLOR_SOLUCION).move_to(LEFT * 4 + UP * 2.4)
        col_no = Text("No lineales", font_size=34, color=COLOR_ERROR).move_to(RIGHT * 2.5 + UP * 2.4)
        separador = DashedLine(UP * 2.7 + LEFT * 1.2, DOWN * 1.6 + LEFT * 1.2, color=COLOR_SECUNDARIO)
        self.decir("Clasifiquemos: ¿lineal o no lineal?")
        self.play(FadeIn(col_si), FadeIn(col_no), Create(separador))
        casos = [
            (r"x + y = 1", None),
            (r"x^2 + y = 1", "potencia de una incógnita"),
            (r"xy = 4", "producto de incógnitas"),
            (r"\tfrac{x}{3} - 2y = 0", None),
            (r"\tfrac{1}{x} + y = 2", "incógnita en un denominador"),
            (r"\sqrt{x} = 3", "raíz de una incógnita"),
            (r"\sqrt{2}\,x = 5", None),
            (r"\operatorname{sen} x + y = 0", "función de una incógnita"),
        ]
        izquierda, derecha = [], []
        self.decir("Equis más ye igual a uno: lineal. Equis al cuadrado más ye: no lineal, hay una potencia. Equis por ye: no lineal, es un producto de incógnitas. Equis tercios menos dos ye: sí, porque dividir entre tres es multiplicar por un tercio. Uno entre equis: no, la incógnita está en un denominador. Raíz de equis: no. Raíz de dos por equis: sí, raíz de dos es solo un número. Y seno de equis: no.")
        for tex, motivo in casos:
            caso = MathTex(tex, font_size=44).move_to(DOWN * 2.4 + LEFT * 1.2)
            self.play(Write(caso), run_time=0.8)
            self.wait(0.6)
            if motivo is None:
                destino = col_si.get_bottom() + DOWN * (0.6 + 0.7 * len(izquierda))
                izquierda.append(caso)
                self.play(caso.animate.move_to(destino).set_color(COLOR_SOLUCION))
            else:
                fila = VGroup(caso.copy(), Text(motivo, font_size=TAM_NOTA - 2, color=COLOR_SECUNDARIO)).arrange(RIGHT, buff=0.4)
                fila.next_to(col_no.get_bottom() + DOWN * (0.25 + 0.7 * len(derecha)), DOWN, buff=0).align_to(col_no, LEFT).shift(LEFT * 1)
                derecha.append(fila)
                self.play(caso.animate.move_to(fila[0]).set_color(COLOR_ERROR))
                self.play(FadeIn(fila[1]))
                fila[0].set_color(COLOR_ERROR)
                self.remove(caso)
                self.add(fila[0])
            self.wait(0.4)
        self.decir("Fíjate: dividir entre un número es lineal; dividir entre la incógnita no lo es.")
        self.pie("Fíjate: dividir ENTRE UN NÚMERO (x/3) es lineal; dividir ENTRE LA INCÓGNITA (1/x) no lo es.", espera=4)
        self.limpiar(titulo)

        # Las gráficas delatan la diferencia.
        titulo = self.cambiar_encabezado(titulo, "Las gráficas lo delatan")
        sistema = ejes_iguales((-4, 4), (-3, 4), unidad=0.68).to_edge(LEFT, buff=0.8).shift(UP * 0.1)
        recta = recta_general(sistema, 1, 1, 1, color=COLOR_SOLUCION)
        parabola = sistema.plot(lambda x: 1 - x * x, x_range=[-2, 2], color=COLOR_ERROR)
        rama_1 = sistema.plot(lambda x: 4 / x, x_range=[1, 4], color=COLOR_TERMINO_INDEP)
        rama_2 = sistema.plot(lambda x: 4 / x, x_range=[-4, -4 / 3], color=COLOR_TERMINO_INDEP)
        leyenda = VGroup(
            MathTex(r"x + y = 1:\ \text{recta}", color=COLOR_SOLUCION, font_size=40),
            MathTex(r"x^2 + y = 1:\ \text{parábola}", color=COLOR_ERROR, font_size=40),
            MathTex(r"xy = 4:\ \text{hipérbola}", color=COLOR_TERMINO_INDEP, font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=0.8).shift(UP * 0.8)
        self.decir("Las gráficas lo delatan.")
        self.play(Create(sistema))
        self.decir("La ecuación lineal da una recta; las otras, curvas.")
        self.play(Create(recta), Write(leyenda[0]))
        self.play(Create(parabola), Write(leyenda[1]))
        self.play(Create(rama_1), Create(rama_2), Write(leyenda[2]))
        self.decir("Esa regularidad es la que hará posible un método que resuelve cualquier sistema lineal: la eliminación de Gauss.")
        self.pie(
            "Solo la lineal da una recta. Esa regularidad es la que permitirá resolver sistemas lineales\n"
            "con un método que siempre funciona (Gauss), algo imposible en general para ecuaciones no lineales.",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F01-N1-02",
            VGroup(
                Text("¿Lineal o no lineal? Si no lo es, di por qué.", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } 3x - y = 2z \quad \text{b) } xy + z = 1 \quad \text{c) } \tfrac{x}{5} + 4 = y"
                    r"\quad \text{d) } \tfrac{5}{x} + y = 1 \quad \text{e) } x + y^2 = 3 \quad \text{f) } \pi x - \sqrt{3}\,y = 0",
                    font_size=38,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "No lineal: potencias, productos de incógnitas, incógnitas en\ndenominadores o dentro de raíces y funciones.",
                "Dividir entre un número sí es lineal: x/3 = (1/3)·x.",
                "Las gráficas de las ecuaciones lineales son rectas (o planos);\nlas de las no lineales, curvas.",
            ],
            "trampas frecuentes.",
            voz="En resumen: no es lineal si hay potencias, productos de incógnitas, o incógnitas en denominadores o dentro de raíces y funciones. Dividir entre un número sí es lineal: equis tercios es un tercio por equis. Y las gráficas de las ecuaciones lineales son rectas o planos; las de las no lineales, curvas. Siguiente: trampas frecuentes.",
        )


class TrampasDeLinealidad(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 5 · Parte 3", "Trampas: ¿lineal o no?")

        # Trampa 1: parece no lineal pero lo es.
        titulo = self.encabezado("Trampa 1: parece no lineal… pero lo es")
        pasos = VGroup(
            MathTex(r"(x + 1)^2 = x^2 + 3", font_size=48),
            MathTex(r"x^2 + 2x + 1 = x^2 + 3", font_size=48),
            MathTex(r"2x = 2", font_size=48, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.5)
        notas = ["desarrollamos el cuadrado", "restamos x² y 1 en ambos lados"]
        self.decir("Esta ecuación parece no lineal por los cuadrados.")
        self.play(Write(pasos[0]))
        self.decir("Pero al desarrollar el cuadrado y restar equis al cuadrado y uno en los dos lados, se cancelan: queda dos equis igual a dos.")
        for i, nota in enumerate(notas):
            self.play(Write(pasos[i + 1]))
            self.pie(nota, COLOR_OPERACION, espera=1.5)
        self.decir("Es lineal: se decide después de simplificar.")
        self.pie("Tras simplificar con pasos válidos queda una ecuación lineal: se decide DESPUÉS de simplificar.", espera=4)
        self.limpiar(titulo)

        # Trampa 2: parece lineal pero no lo es.
        titulo = self.cambiar_encabezado(titulo, "Trampa 2: parece lineal… pero no lo es")
        pasos = VGroup(
            MathTex(r"\frac{x}{y} = 2", font_size=56),
            MathTex(r"x = 2y \quad (\text{multiplicando por } y)", font_size=44),
            MathTex(r"(0, 0) \text{ cumple } x = 2y, \text{ pero } \tfrac{0}{0} \text{ no está definido}", font_size=40, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.6)
        self.decir("Esta parece lineal, pero ye está en un denominador. Si multiplicamos por ye, obtenemos equis igual a dos ye, que admite el punto cero, cero, donde la ecuación original ni siquiera está definida.")
        for p in pasos:
            self.play(Write(p))
            self.wait(1.5)
        self.decir("No es lineal, y multiplicar por la incógnita la ha cambiado.")
        self.pie(
            "La incógnita y está en un denominador: no es lineal. Multiplicar por y exige y distinto de 0\n"
            "(Lección 2), y sin esa condición aparece una solución falsa.",
            espera=5,
        )
        self.limpiar(titulo)

        # Trampa 3: parámetros.
        titulo = self.cambiar_encabezado(titulo, "Trampa 3: ¿quién es incógnita?")
        bloque = VGroup(
            MathTex(r"a\,x + 3y = 5", font_size=60),
            Tex(r"Si $a$ es un \textbf{número fijo} (un \emph{parámetro}) e $x, y$ son las incógnitas: \textbf{lineal}.", font_size=38, color=COLOR_SOLUCION),
            Tex(r"Si también $a$ fuera incógnita, $a\,x$ sería un producto de incógnitas: \textbf{no lineal}.", font_size=38, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.6)
        bloque[0][0][0].set_color(COLOR_LIBRE)
        self.decir("¿Es lineal a equis más tres ye igual a cinco? Depende de quién sea incógnita. Si a es un número fijo, un parámetro, sí. Si también fuera incógnita, a por equis sería un producto de incógnitas.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.decir("Lineal siempre se dice respecto de unas incógnitas concretas. Los parámetros, en verde, son números fijos.")
        self.pie("«Lineal» siempre se dice respecto de unas incógnitas concretas. Los parámetros (verde) son números fijos.", espera=4)
        self.limpiar(titulo)

        # Trampa 4: todos los coeficientes nulos.
        titulo = self.cambiar_encabezado(titulo, "Trampa 4: coeficientes todos nulos")
        casos = VGroup(
            VGroup(MathTex(r"0x + 0y = 5", font_size=52), Tex(r"$0 = 5$ para cualquier $(x, y)$: \textbf{ninguna} solución", font_size=38, color=COLOR_ERROR)),
            VGroup(MathTex(r"0x + 0y = 0", font_size=52), Tex(r"$0 = 0$ siempre: \textbf{todos} los pares son solución", font_size=38, color=COLOR_SOLUCION)),
        )
        self.decir("Cuando todos los coeficientes son cero, la ecuación dice cero igual a algo.")
        for c in casos:
            c.arrange(RIGHT, buff=0.8)
        casos.arrange(DOWN, buff=0.8)
        self.decir("Si ese algo no es cero, como cero igual a cinco, no hay ninguna solución. Si es cero, todos los pares son solución.")
        for c in casos:
            self.play(Write(c[0]))
            self.wait(1)
            self.play(FadeIn(c[1]))
            self.wait(2)
        self.decir("Volveremos a encontrar estas ecuaciones al final de la eliminación de Gauss.")
        self.pie(
            "Son ecuaciones lineales «degeneradas». Aparecerán al final de la eliminación de Gauss:\n"
            "0 = 5 delatará un sistema sin solución; 0 = 0, una ecuación que sobraba.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F01-N4-01",
            VGroup(
                Tex(r"¿Son lineales en $x, y$? Justifica.", font_size=40),
                MathTex(
                    r"\text{a) } (x - 2)(x + 2) = x^2 + y \qquad \text{b) } \frac{x}{y + 1} = 3",
                    font_size=42,
                ),
                MathTex(
                    r"\text{c) } k\,x - k^2 y = 1 \ (k \text{ fijo}) \qquad \text{d) } 2x + 3y = 2x + 3y + 1",
                    font_size=42,
                ),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Decide si es lineal después de simplificar con pasos válidos.",
                "Una incógnita en un denominador hace la ecuación no lineal.",
                "La linealidad depende de qué letras son incógnitas y cuáles parámetros.",
                "0 = 5 (ninguna solución) y 0 = 0 (todas) son casos degenerados.",
            ],
            "Lección 6 — ecuaciones lineales con una incógnita.",
            voz="En resumen: decide si es lineal después de simplificar con pasos válidos. Una incógnita en un denominador hace la ecuación no lineal. La linealidad depende de qué letras son incógnitas y cuáles parámetros. Y cero igual a cinco, sin solución, y cero igual a cero, con todas, son casos degenerados. Siguiente: lección seis, ecuaciones lineales con una incógnita.",
        )
