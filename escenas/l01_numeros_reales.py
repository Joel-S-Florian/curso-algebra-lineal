"""Lección 1 — Números reales y sus operaciones.

Escenas (un video cada una):
    ConjuntosNumericos, ReglasDeSignos, Fracciones, PropiedadesDeLasOperaciones

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l01_numeros_reales.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, alinear_por_igual  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def recta_numerica(desde=-6, hasta=6) -> NumberLine:
    return NumberLine(x_range=[desde, hasta, 1], length=hasta - desde, include_numbers=True, font_size=28)


def barra(partes: int, sombreadas: int, ancho=4.0, alto=0.5, color=COLOR_COEFICIENTE) -> VGroup:
    """Unidad dividida en `partes` trozos iguales, con los primeros `sombreadas` rellenos."""
    return VGroup(
        *[
            Rectangle(
                width=ancho / partes,
                height=alto,
                stroke_width=2,
                fill_color=color,
                fill_opacity=0.85 if i < sombreadas else 0,
            )
            for i in range(partes)
        ]
    ).arrange(RIGHT, buff=0)


class ConjuntosNumericos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 1 · Parte 1", "Los conjuntos numéricos")
        recta = recta_numerica().shift(DOWN * 0.8)

        # Naturales: contar.
        titulo = self.encabezado("Contar: los números naturales")
        self.decir("Los primeros números que aprendemos sirven para contar: uno, dos, tres. Se llaman números naturales, y los representamos como puntos de una recta, separados siempre la misma distancia.")
        self.play(Create(recta))
        naturales = VGroup(*[Dot(recta.n2p(k), color=COLOR_PIVOTE) for k in range(1, 7)])
        self.play(LaggedStart(*[FadeIn(d, scale=2) for d in naturales], lag_ratio=0.3))
        conjunto = MathTex(r"\mathbb{N} = \{1,\ 2,\ 3,\ \dots\}", font_size=48).shift(UP * 1.6)
        self.play(Write(conjunto))
        self.decir("Algunos libros también incluyen el cero entre los naturales.")
        nota = self.pie("Sirven para contar. Algunos libros también incluyen el 0 entre los naturales.", espera=3)

        # Enteros: restar.
        self.play(FadeOut(nota), FadeOut(conjunto), naturales.animate.set_color(COLOR_SECUNDARIO))
        titulo = self.cambiar_encabezado(titulo, "Restar: los números enteros")
        pregunta = MathTex(r"3 - 5 = \ ?", font_size=52).shift(UP * 1.6)
        self.decir("Pero con ellos no siempre se puede restar. Si a tres le quito cinco, me salgo por la izquierda del uno.")
        self.play(Write(pregunta))
        paso = Arrow(recta.n2p(3) + UP * 0.6, recta.n2p(-2) + UP * 0.6, buff=0, color=COLOR_TERMINO_INDEP)
        rotulo_paso = Text("5 pasos a la izquierda", font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP)
        rotulo_paso.next_to(paso, UP, buff=0.1)
        self.play(GrowArrow(paso), FadeIn(rotulo_paso))
        nota = self.pie("Con los naturales no hay respuesta: nos salimos por la izquierda del 1.", espera=2)

        # Los negativos son el reflejo de los naturales respecto del 0.
        negativos = VGroup(*[Dot(recta.n2p(-k), color=COLOR_PIVOTE) for k in range(1, 7)])
        cero = Dot(recta.n2p(0), color=COLOR_PIVOTE)
        self.decir("Para que la resta siempre tenga respuesta, reflejamos los naturales al otro lado del cero: aparecen los negativos. Tres menos cinco es menos dos.")
        self.play(TransformFromCopy(naturales, negativos, path_arc=PI), FadeIn(cero, scale=2), run_time=2)
        self.play(Transform(pregunta, MathTex(r"3 - 5 = -2", font_size=52).move_to(pregunta)))
        enteros = MathTex(r"\mathbb{Z} = \{\dots,\ -2,\ -1,\ 0,\ 1,\ 2,\ \dots\}", font_size=44)
        enteros.next_to(pregunta, DOWN, buff=0.35)
        self.decir("Naturales, cero y negativos forman los números enteros.")
        self.play(FadeOut(nota), Write(enteros))
        self.wait(3)

        # Racionales: dividir.
        self.play(
            *[FadeOut(m) for m in (pregunta, enteros, paso, rotulo_paso)],
            VGroup(naturales, negativos, cero).animate.set_color(COLOR_SECUNDARIO),
        )
        titulo = self.cambiar_encabezado(titulo, "Dividir: los números racionales")
        pregunta = MathTex(r"1 \div 2 = \ ?", font_size=52).shift(UP * 1.6)
        self.decir("Con los enteros tampoco se puede dividir siempre: uno entre dos no es un entero.")
        self.play(Write(pregunta))
        fracciones = [(1 / 2, r"\tfrac{1}{2}"), (-3 / 4, r"-\tfrac{3}{4}"), (5 / 3, r"\tfrac{5}{3}"), (-7 / 2, r"-\tfrac{7}{2}")]
        marcas = VGroup()
        for valor, tex in fracciones:
            punto = Dot(recta.n2p(valor), color=COLOR_PIVOTE)
            marcas.add(VGroup(punto, MathTex(tex, font_size=38, color=COLOR_PIVOTE).next_to(punto, UP, buff=0.2)))
        self.play(LaggedStart(*[FadeIn(m, scale=1.5) for m in marcas], lag_ratio=0.5))
        racionales = MathTex(
            r"\mathbb{Q} = \left\{ \frac{p}{q} \;:\; p \text{ y } q \text{ enteros},\ q \neq 0 \right\}",
            font_size=44,
        ).next_to(pregunta, DOWN, buff=0.35)
        self.play(Transform(pregunta, MathTex(r"1 \div 2 = \tfrac{1}{2}", font_size=52).move_to(pregunta)))
        self.decir("Las fracciones de enteros, con denominador distinto de cero, son los números racionales. Llenan muchísimos huecos de la recta.")
        self.play(Write(racionales))
        self.decir("Su expresión decimal termina, como un medio, que es cero coma cinco; o se repite sin fin, como un tercio, que es cero coma tres tres tres.")
        nota = self.pie("Su expresión decimal termina (1/2 = 0.5) o se repite sin fin (1/3 = 0.333...).", espera=3)

        # Irracionales: la diagonal del cuadrado de lado 1.
        self.play(*[FadeOut(m) for m in (pregunta, racionales, nota, marcas)])
        titulo = self.cambiar_encabezado(titulo, "Huecos en la recta: los irracionales")
        unidad = recta.get_unit_size()
        cuadrado = Square(side_length=unidad, color=WHITE).move_to(recta.n2p(0), aligned_edge=DL)
        lados = VGroup(
            MathTex("1", font_size=34).next_to(cuadrado, LEFT, buff=0.15),
            MathTex("1", font_size=34).next_to(cuadrado, UP, buff=0.15),
        )
        diagonal = Line(recta.n2p(0), cuadrado.get_corner(UR), color=COLOR_PIVOTE, stroke_width=6)
        self.decir("Pero no todos los huecos. La diagonal de un cuadrado de lado uno mide raíz de dos, por el teorema de Pitágoras.")
        self.play(Create(cuadrado), FadeIn(lados))
        self.play(Create(diagonal))
        pitagoras = MathTex(r"d^2 = 1^2 + 1^2 = 2", r"\quad\Longrightarrow\quad", r"d = \sqrt{2}", font_size=44)
        pitagoras.shift(UP * 2.2)
        self.play(Write(pitagoras))
        self.wait(1.5)
        arco = Arc(radius=np.sqrt(2) * unidad, start_angle=PI / 4, angle=-PI / 4, arc_center=recta.n2p(0))
        arco.set_stroke(COLOR_PIVOTE, opacity=0.6)
        self.decir("Si la giramos hasta la recta, marca un punto. Ese punto no corresponde a ninguna fracción.")
        self.play(Rotate(diagonal, -PI / 4, about_point=recta.n2p(0)), Create(arco), run_time=2)
        raiz = Dot(recta.n2p(np.sqrt(2)), color=COLOR_PIVOTE)
        rotulo_raiz = MathTex(r"\sqrt{2} = 1.41421\ldots", font_size=34, color=COLOR_PIVOTE)
        rotulo_raiz.next_to(raiz, UP, buff=1.4)  # por encima del cuadrado
        flecha_raiz = Arrow(rotulo_raiz.get_bottom(), raiz.get_top(), buff=0.1, color=COLOR_PIVOTE, stroke_width=3)
        self.play(FadeIn(raiz, scale=2), Write(rotulo_raiz), GrowArrow(flecha_raiz))
        pi = Dot(recta.n2p(PI), color=COLOR_PIVOTE)
        rotulo_pi = MathTex(r"\pi = 3.14159\ldots", font_size=34, color=COLOR_PIVOTE).next_to(pi, UR, buff=0.15)
        self.decir("Lo mismo pasa con pi. El dibujo nos dice dónde está raíz de dos; que no es una fracción lo demostraremos en la lección cuatro, porque un dibujo no es una demostración.")
        self.play(FadeIn(pi, scale=2), Write(rotulo_pi))
        nota = self.pie(
            "Ni raíz de 2 ni pi se pueden escribir como fracción: su parte decimal no termina ni se repite.\n"
            "El dibujo dice DÓNDE está raíz de 2; que no es fracción lo demostraremos en la Lección 4.",
            espera=5,
        )

        # Los reales y la cadena de inclusiones.
        self.limpiar(titulo)
        titulo = self.cambiar_encabezado(titulo, "Los números reales: todos los puntos de la recta")
        inclusion = MathTex(r"\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}", font_size=50)
        lectura = Tex(r"($\subset$ se lee: ``está contenido en'')", font_size=34, color=COLOR_SECUNDARIO)
        VGroup(inclusion, lectura).arrange(RIGHT, buff=0.6).next_to(titulo, DOWN, buff=0.35)
        diagrama = self.diagrama_conjuntos().next_to(VGroup(inclusion, lectura), DOWN, buff=0.35)
        self.decir("Juntando racionales e irracionales obtenemos los números reales: todos los puntos de la recta. Cada conjunto está contenido en el siguiente.")
        self.play(LaggedStart(*[FadeIn(parte) for parte in diagrama], lag_ratio=0.4), run_time=4)
        self.play(Write(inclusion))
        self.play(FadeIn(lectura))
        self.wait(2)
        self.decir("En este curso, los coeficientes y las soluciones de los sistemas serán números reales.")
        self.pie("En este curso, los coeficientes y las soluciones de los sistemas serán números reales.", espera=4)

        self.ejercicio_propuesto(
            "F00-N1-01",
            VGroup(
                Text("Indica el conjunto más pequeño (N, Z, Q o R) al que pertenece cada número:", font_size=TAM_TEXTO),
                MathTex(r"-7,\qquad 0,\qquad \tfrac{3}{4},\qquad \sqrt{9},\qquad \sqrt{5},\qquad 0.25,\qquad -\pi"),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Naturales para contar, enteros para poder restar,\nracionales para poder dividir (nunca entre 0).",
                "Hay números que no son fracciones: los irracionales\n(raíz de 2, pi).",
                "Los reales son todos los puntos de la recta.",
                "Cada conjunto está contenido en el siguiente.",
            ],
            "cómo se opera con signos.",
        )

    def diagrama_conjuntos(self) -> VGroup:
        """Rectángulos anidados con ejemplos de cada conjunto en la franja que le es propia."""
        datos = [  # (nombre, ancho, alto, ejemplos)
            (r"\mathbb{R}", 12.0, 5.0, r"\sqrt{2},\ \pi"),
            (r"\mathbb{Q}", 9.4, 3.9, r"\tfrac{1}{2},\ -\tfrac{3}{4}"),
            (r"\mathbb{Z}", 6.8, 2.8, r"-2,\ 0"),
            (r"\mathbb{N}", 4.2, 1.7, r"1,\ 2,\ 3"),
        ]
        grupo, rects = VGroup(), []
        for i, (nombre, ancho, alto, _) in enumerate(datos):
            rect = RoundedRectangle(corner_radius=0.25, width=ancho, height=alto, stroke_color=COLOR_COEFICIENTE)
            # Esquina inferior izquierda 0.4 más adentro que la del rectángulo anterior.
            rect.move_to((RIGHT + UP) * 0.4 * i + (RIGHT * (ancho - 12) + UP * (alto - 5)) / 2)
            rect.set_fill(COLOR_COEFICIENTE, opacity=0.06)
            etiqueta = MathTex(nombre, font_size=40).move_to(rect.get_corner(UL) + RIGHT * 0.4 + DOWN * 0.35)
            rects.append(rect)
            grupo.add(VGroup(rect, etiqueta))
        for i, (_, _, _, ejemplos) in enumerate(datos):
            borde_interior = rects[i + 1].get_right()[0] if i + 1 < len(rects) else rects[i].get_left()[0]
            x = (borde_interior + rects[i].get_right()[0]) / 2
            grupo[i].add(MathTex(ejemplos, font_size=40, color=COLOR_PIVOTE).move_to([x, rects[i].get_y(), 0]))
        return grupo.scale(0.85)


class ReglasDeSignos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 1 · Parte 2", "Signos: opuestos, sumas y productos")
        recta = recta_numerica().shift(DOWN * 1.2)

        # El opuesto: simetría respecto del 0.
        titulo = self.encabezado("El opuesto de un número")
        self.play(Create(recta))
        tres = Dot(recta.n2p(3), color=COLOR_PIVOTE)
        self.decir("El signo menos delante de un número significa: el opuesto. Es su reflejo respecto del cero.")
        self.play(FadeIn(tres, scale=2))
        menos_tres = Dot(recta.n2p(-3), color=COLOR_TERMINO_INDEP)
        self.play(TransformFromCopy(tres, menos_tres, path_arc=PI), run_time=1.5)
        formula = MathTex(r"-(3) = -3", font_size=48).shift(UP * 1.3)
        self.play(Write(formula))
        self.wait(1)
        self.decir("Reflejar dos veces nos devuelve al punto de partida; por eso, menos menos tres es tres.")
        self.play(TransformFromCopy(menos_tres, tres.copy(), path_arc=-PI), run_time=1.5)
        formula2 = MathTex(r"-(-3) = 3", font_size=48).next_to(formula, DOWN, buff=0.3)
        self.play(Write(formula2))
        nota = self.pie(
            "El signo menos delante de un número significa «el opuesto»: su reflejo respecto del 0.\n"
            "Reflejar dos veces devuelve el número original.",
            espera=4,
        )
        self.limpiar(titulo, recta)

        # Sumar es desplazarse.
        titulo = self.cambiar_encabezado(titulo, "Sumar es desplazarse por la recta")
        ida = Arrow(recta.n2p(0) + UP * 0.5, recta.n2p(3) + UP * 0.5, buff=0, color=COLOR_COEFICIENTE)
        vuelta = Arrow(recta.n2p(3) + UP * 1.1, recta.n2p(-2) + UP * 1.1, buff=0, color=COLOR_TERMINO_INDEP)
        suma = MathTex("3", "+", "(-5)", "=", "-2", font_size=52).shift(UP * 2.3)
        suma[0].set_color(COLOR_COEFICIENTE)
        suma[2].set_color(COLOR_TERMINO_INDEP)
        self.decir("Sumar es desplazarse por la recta. Tres más menos cinco: avanzo tres, retrocedo cinco, y llego a menos dos.")
        self.play(Write(suma[0]), GrowArrow(ida))
        self.play(Write(suma[1:3]), GrowArrow(vuelta))
        llegada = Dot(recta.n2p(-2), color=COLOR_PIVOTE)
        self.play(FadeIn(llegada, scale=2), Write(suma[3:]))
        self.wait(1.5)
        resta = MathTex(r"2 - 5", "=", r"2 + (-5)", "=", "-3", font_size=48).next_to(suma, DOWN, buff=0.4)
        self.decir("Y restar cinco es exactamente lo mismo que sumar menos cinco: toda resta es una suma.")
        self.play(Write(resta))
        self.pie("Restar un número es sumar su opuesto. Así, toda resta es una suma.", espera=4)
        self.limpiar(titulo)

        # Producto: el patrón que obliga a que (−)·(−) = (+).
        titulo = self.cambiar_encabezado(titulo, "Multiplicar con signos")
        filas = [
            (r"(-3)\cdot 2", "-6"),
            (r"(-3)\cdot 1", "-3"),
            (r"(-3)\cdot 0", "0"),
            (r"(-3)\cdot(-1)", "?"),
            (r"(-3)\cdot(-2)", "?"),
        ]
        patron = alinear_por_igual(*[MathTex(a, "=", b, font_size=44) for a, b in filas], buff=0.3)
        patron.to_edge(LEFT, buff=1.0).shift(DOWN * 0.2)
        self.decir("¿Por qué menos por menos es más? Mira la tabla del menos tres.")
        self.play(LaggedStart(*[FadeIn(f) for f in patron[:3]], lag_ratio=0.5))
        saltos = VGroup()
        for i in range(4):
            arriba, abajo = patron[i][2], patron[i + 1][2]
            salto = MathTex("+3", font_size=32, color=COLOR_LIBRE)
            salto.move_to([patron.get_right()[0] + 1.0, (arriba.get_y() + abajo.get_y()) / 2, 0])
            saltos.add(salto)
        self.decir("Cada vez que el segundo factor baja una unidad, el resultado sube tres.")
        self.play(FadeIn(saltos[:2]))
        self.pie("Cada vez que el segundo factor baja 1, el resultado SUBE 3.", espera=2)
        self.decir("Si el patrón sigue, menos tres por cero es cero, y menos tres por menos uno tiene que ser tres. Cualquier otra regla rompería la propiedad distributiva.")
        self.play(FadeIn(patron[3:]), FadeIn(saltos[2:]))
        self.wait(1)
        for fila, valor in ((patron[3], "3"), (patron[4], "6")):
            nuevo = MathTex(valor, font_size=44, color=COLOR_SOLUCION).move_to(fila[2], aligned_edge=LEFT)
            self.play(Transform(fila[2], nuevo))
        tabla = VGroup(
            *[
                MathTex(t, font_size=44)
                for t in (r"(+)\cdot(+) = +", r"(+)\cdot(-) = -", r"(-)\cdot(+) = -", r"(-)\cdot(-) = +")
            ]
        ).arrange_in_grid(rows=2, cols=2, buff=(0.8, 0.4))
        tabla.to_edge(RIGHT, buff=0.9).match_y(patron)
        caja = SurroundingRectangle(tabla, color=COLOR_PIVOTE, buff=0.3)
        self.decir("En resumen: signos iguales dan positivo, y signos distintos dan negativo.")
        self.play(Write(tabla), Create(caja))
        division = MathTex(r"\frac{-12}{3} = -4 \qquad \frac{-12}{-3} = 4", font_size=40).next_to(caja, DOWN, buff=0.5)
        self.decir("Para dividir valen las mismas reglas de signos.")
        self.play(Write(division))
        self.pie("Para dividir valen las mismas reglas de signos.", espera=4)
        self.limpiar(titulo)

        # Errores frecuentes.
        titulo = self.cambiar_encabezado(titulo, "Errores frecuentes")
        errores = VGroup(
            MathTex(r"-3^2 = -(3\cdot 3) = -9", font_size=44),
            MathTex(r"(-3)^2 = (-3)\cdot(-3) = 9", font_size=44),
            MathTex(r"-(2 + 5) = -2 - 5 = -7", r"\qquad\text{y no}\qquad", r"-2 + 5", font_size=44),
        ).arrange(DOWN, buff=0.6)
        errores[2][2].set_color(COLOR_ERROR)
        self.decir("Dos errores muy frecuentes. Primero: la potencia actúa antes que el signo, así que menos tres al cuadrado es menos nueve. Si queremos elevar el menos tres, hay que escribir paréntesis. Segundo: un signo menos delante de un paréntesis cambia el signo de todos los términos de dentro, no solo del primero.")
        for linea in errores:
            self.play(Write(linea))
            self.wait(1.5)
        self.pie(
            "La potencia actúa antes que el signo menos.\n"
            "El signo menos delante de un paréntesis cambia el signo de TODOS los términos de dentro.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F00-N1-02",
            MathTex(
                r"\text{a) } (-4)(-5) - 3\cdot(-2) \qquad \text{b) } -2^2 + (-2)^2 \qquad \text{c) } 7 - (-3) - (+5)",
                font_size=42,
            ),
        )
        self.resumen(
            [
                "El opuesto de a es -a: su reflejo respecto del 0.",
                "Restar es sumar el opuesto.",
                "Signos iguales dan +, signos distintos dan -\n(en productos y en divisiones).",
                "-3² = -9, pero (-3)² = 9.",
            ],
            "fracciones.",
            voz="En resumen: el opuesto de un número es su reflejo respecto del cero. Restar es sumar el opuesto. Signos iguales dan positivo y signos distintos dan negativo, en productos y en divisiones. Y menos tres al cuadrado es menos nueve, pero el cuadrado de menos tres, entre paréntesis, es nueve. Siguiente: fracciones.",
        )


class Fracciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 1 · Parte 3", "Fracciones")

        # Significado de a/b.
        titulo = self.encabezado("Qué significa a/b")
        tres_cuartos = barra(4, 3, ancho=6, alto=0.8)
        fraccion = MathTex(r"\frac{3}{4}", font_size=72).next_to(tres_cuartos, LEFT, buff=0.8)
        self.decir("Tres cuartos significa: parto la unidad en cuatro trozos iguales y tomo tres. Además, tres cuartos es tres dividido entre cuatro.")
        self.play(Create(tres_cuartos), Write(fraccion))
        explicacion = VGroup(
            Tex(r"Denominador $4$: la unidad se parte en $4$ trozos iguales.", font_size=38),
            Tex(r"Numerador $3$: se toman $3$ de esos trozos.", font_size=38),
            Tex(r"Además, $\frac{3}{4} = 3 \div 4$.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(VGroup(fraccion, tres_cuartos), DOWN, buff=0.8)
        for linea in explicacion:
            self.play(FadeIn(linea))
            self.wait(1.2)
        self.wait(1)
        self.limpiar(titulo)

        # Por qué no se divide entre 0.
        titulo = self.cambiar_encabezado(titulo, "¿Por qué no se puede dividir entre 0?")
        lineas = VGroup(
            MathTex(r"\frac{6}{2} = 3", r"\quad\text{porque}\quad", r"2\cdot 3 = 6", font_size=48),
            MathTex(r"\frac{6}{0} = \ ?", r"\quad\text{exigiría}\quad", r"0\cdot ? = 6", font_size=48),
            MathTex(r"\frac{0}{0} = \ ?", r"\quad\text{exigiría}\quad", r"0\cdot ? = 0", font_size=48),
        ).arrange(DOWN, buff=0.7)
        self.decir("Dividir es la operación inversa de multiplicar: seis entre dos es tres, porque dos por tres es seis.")
        self.play(Write(lineas[0]))
        self.wait(2)
        self.decir("Entonces, seis entre cero debería ser un número que multiplicado por cero dé seis: no existe.")
        self.play(Write(lineas[1]))
        self.play(lineas[1][2].animate.set_color(COLOR_ERROR))
        nota = self.pie("Ningún número multiplicado por 0 da 6: no hay respuesta.", COLOR_ERROR, espera=3)
        self.decir("Y cero entre cero, un número que multiplicado por cero dé cero: sirve cualquiera.")
        self.play(FadeOut(nota), Write(lineas[2]))
        self.play(lineas[2][2].animate.set_color(COLOR_ERROR))
        nota = self.pie("Aquí sirve CUALQUIER número: tampoco hay una respuesta única.", COLOR_ERROR, espera=3)
        self.decir("En ningún caso hay una respuesta única, así que dividir entre cero no está definido. Antes de dividir, comprueba siempre que no divides entre cero.")
        self.play(FadeOut(nota))
        self.pie(
            "Por eso dividir entre 0 no está definido. Lo usaremos mil veces:\n"
            "en Gauss, antes de dividir entre un número, hay que asegurarse de que no es 0.",
            espera=5,
        )
        self.limpiar(titulo)

        # Fracciones equivalentes.
        titulo = self.cambiar_encabezado(titulo, "Fracciones equivalentes y simplificación")
        seis_octavos = barra(8, 6, ancho=6, alto=0.6)
        tres_cuartos = barra(4, 3, ancho=6, alto=0.6)
        VGroup(seis_octavos, tres_cuartos).arrange(DOWN, buff=0.9).shift(UP * 0.6 + RIGHT * 1.5)
        rot_68 = MathTex(r"\frac{6}{8}", font_size=48).next_to(seis_octavos, LEFT, buff=0.6)
        rot_34 = MathTex(r"\frac{3}{4}", font_size=48).next_to(tres_cuartos, LEFT, buff=0.6)
        self.decir("Seis octavos y tres cuartos ocupan exactamente lo mismo: son la misma cantidad.")
        self.play(Create(seis_octavos), Write(rot_68))
        self.play(Create(tres_cuartos), Write(rot_34))
        guia = DashedLine(
            seis_octavos.get_corner(UL) + RIGHT * 4.5 + UP * 0.3,
            tres_cuartos.get_corner(DL) + RIGHT * 4.5 + DOWN * 0.3,
            color=COLOR_PIVOTE,
        )
        self.play(Create(guia))
        simplificar = MathTex(
            r"\frac{6}{8} = \frac{6 \div 2}{8 \div 2} = \frac{3}{4}", font_size=48
        ).next_to(VGroup(seis_octavos, tres_cuartos), DOWN, buff=0.7).shift(LEFT * 1.5)
        self.decir("Dividir el numerador y el denominador por el mismo número distinto de cero no cambia la fracción. Eso es simplificar.")
        self.play(Write(simplificar))
        self.pie(
            "Multiplicar o dividir numerador y denominador por el mismo número (distinto de 0)\n"
            "no cambia la fracción: es la misma cantidad.",
            espera=5,
        )
        self.limpiar(titulo)

        # Suma con denominador común.
        titulo = self.cambiar_encabezado(titulo, "Sumar fracciones: denominador común")
        medio, tercio = barra(2, 1, ancho=6, alto=0.6), barra(3, 1, ancho=6, alto=0.6, color=COLOR_TERMINO_INDEP)
        VGroup(medio, tercio).arrange(DOWN, buff=0.9).shift(UP * 1.2 + RIGHT * 1.5)
        rot_medio = MathTex(r"\frac{1}{2}", font_size=48).next_to(medio, LEFT, buff=0.6)
        rot_tercio = MathTex(r"\frac{1}{3}", font_size=48).next_to(tercio, LEFT, buff=0.6)
        self.decir("Para sumar un medio y un tercio, primero partimos los dos en trozos del mismo tamaño: sextos.")
        self.play(Create(medio), Write(rot_medio), Create(tercio), Write(rot_tercio))
        self.pie("Trozos de tamaños distintos no se pueden contar juntos. Los partimos en sextos.", espera=2)
        sextos_a = barra(6, 3, ancho=6, alto=0.6).move_to(medio)
        sextos_b = barra(6, 2, ancho=6, alto=0.6, color=COLOR_TERMINO_INDEP).move_to(tercio)
        self.play(
            ReplacementTransform(medio, sextos_a),
            ReplacementTransform(tercio, sextos_b),
            Transform(rot_medio, MathTex(r"\frac{3}{6}", font_size=48).move_to(rot_medio)),
            Transform(rot_tercio, MathTex(r"\frac{2}{6}", font_size=48).move_to(rot_tercio)),
        )
        total = VGroup(*[Rectangle(width=1, height=0.6, stroke_width=2) for _ in range(6)]).arrange(RIGHT, buff=0)
        for i in range(5):
            total[i].set_fill(COLOR_COEFICIENTE if i < 3 else COLOR_TERMINO_INDEP, opacity=0.85)
        total.next_to(sextos_b, DOWN, buff=0.9)
        rot_total = MathTex(r"\frac{5}{6}", font_size=48).next_to(total, LEFT, buff=0.6)
        self.decir("Tres sextos más dos sextos son cinco sextos.")
        self.play(FadeIn(total), Write(rot_total))
        cuenta = MathTex(
            r"\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}", font_size=46
        ).next_to(total, DOWN, buff=0.5)
        self.play(Write(cuenta))
        self.wait(2)
        error = MathTex(r"\frac{1}{2} + \frac{1}{3} \neq \frac{1+1}{2+3} = \frac{2}{5}", font_size=40, color=COLOR_ERROR)
        error.to_corner(DR, buff=0.5)
        self.limpiar(titulo, cuenta)
        self.play(cuenta.animate.shift(UP * 3))
        error.next_to(cuenta, DOWN, buff=0.8)
        self.decir("Sumar numeradores y denominadores por separado daría dos quintos, que es menos que un medio: absurdo.")
        self.play(Write(error))
        self.pie(
            "Error frecuente: sumar numeradores y denominadores. ¡2/5 es menor que 1/2!\n"
            "Sumar 1/3 a 1/2 no puede dar algo más pequeño que 1/2.",
            COLOR_ERROR,
            espera=5,
        )
        self.limpiar(titulo)

        # Producto, cociente y signos.
        titulo = self.cambiar_encabezado(titulo, "Multiplicar, dividir y signos")
        reglas = VGroup(
            MathTex(r"\frac{2}{3}\cdot\frac{3}{4} = \frac{2\cdot 3}{3\cdot 4} = \frac{6}{12} = \frac{1}{2}", font_size=46),
            MathTex(
                r"\frac{2}{3}\div\frac{4}{5} = \frac{2}{3}\cdot\frac{5}{4} = \frac{10}{12} = \frac{5}{6}", font_size=46
            ),
            MathTex(r"-\frac{3}{4} = \frac{-3}{4} = \frac{3}{-4}", font_size=46),
        ).arrange(DOWN, buff=0.6)
        comentarios = [
            "Numerador por numerador, denominador por denominador.",
            "Dividir entre una fracción es multiplicar por su inversa (darle la vuelta).",
            "El signo menos puede ir delante, arriba o abajo: es la misma fracción.",
        ]
        nota = None
        self.decir("Para multiplicar, numerador por numerador y denominador por denominador. Para dividir, multiplicamos por la fracción inversa. Y el signo menos puede ir delante, arriba o abajo: es la misma fracción.")
        for linea, comentario in zip(reglas, comentarios):
            if nota:
                self.play(FadeOut(nota))
            self.play(Write(linea))
            nota = self.pie(comentario, espera=3)

        self.ejercicio_propuesto(
            "F00-N2-01",
            MathTex(
                r"\text{a) } \frac{2}{3} - \frac{5}{6} + \frac{1}{4} \qquad\qquad \text{b) } \frac{3}{5} \div \left(-\frac{9}{10}\right)",
                font_size=48,
            ),
        )
        self.resumen(
            [
                "a/b: partir la unidad en b trozos y tomar a. Además, a/b = a ÷ b.",
                "Nunca se divide entre 0.",
                "Para sumar, primero denominador común.",
                "Para dividir, multiplicar por la inversa.",
            ],
            "las propiedades que usaremos para despejar.",
            voz="En resumen: a partido por be significa partir la unidad en be trozos y tomar a; además, es a dividido entre be. Nunca se divide entre cero. Para sumar, primero hay que buscar un denominador común. Para dividir, se multiplica por la inversa. Siguiente: las propiedades que usaremos para despejar.",
        )


class PropiedadesDeLasOperaciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 1 · Parte 4", "Propiedades de las operaciones")

        # Conmutativa y asociativa.
        titulo = self.encabezado("Conmutativa y asociativa")
        bloque = VGroup(
            Tex(r"Conmutativa: \quad $a + b = b + a$ \qquad $a\cdot b = b\cdot a$", font_size=42),
            MathTex(r"2 + 5 = 5 + 2 = 7 \qquad 3\cdot 4 = 4\cdot 3 = 12", font_size=40, color=COLOR_SECUNDARIO),
            Tex(r"Asociativa: \quad $(a + b) + c = a + (b + c)$ \qquad $(ab)c = a(bc)$", font_size=42),
            MathTex(r"(2 + 3) + 4 = 2 + (3 + 4) = 9", font_size=40, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.8)
        self.decir("En la suma y en el producto, el orden no importa, y tampoco cómo agrupemos.")
        for linea in bloque:
            self.play(FadeIn(linea))
            self.wait(1.2)
        cuidado = VGroup(
            MathTex(r"5 - 2 = 3 \neq -3 = 2 - 5", font_size=40),
            MathTex(r"(12 \div 6)\div 2 = 1 \neq 4 = 12 \div (6 \div 2)", font_size=40),
        ).arrange(DOWN, buff=0.3).next_to(bloque, DOWN, buff=0.6)
        cuidado.set_color(COLOR_ERROR)
        self.decir("En la resta y en la división sí importa: cinco menos dos no es dos menos cinco. Más adelante veremos que el producto de matrices tampoco es conmutativo.")
        self.play(Write(cuidado))
        self.pie(
            "La resta y la división NO son conmutativas ni asociativas.\n"
            "Más adelante veremos que el producto de matrices tampoco es conmutativo.",
            espera=5,
        )
        self.limpiar(titulo)

        # Distributiva como área.
        titulo = self.cambiar_encabezado(titulo, "Distributiva: a(b + c) = ab + ac")
        a, b, c = 2, 3, 2
        izquierda = Rectangle(width=b, height=a, fill_color=COLOR_COEFICIENTE, fill_opacity=0.5)
        derecha = Rectangle(width=c, height=a, fill_color=COLOR_TERMINO_INDEP, fill_opacity=0.5)
        rect = VGroup(izquierda, derecha).arrange(RIGHT, buff=0).shift(LEFT * 2.5 + UP * 0.3)
        lado_a = MathTex("a = 2", font_size=36).next_to(rect, LEFT, buff=0.2)
        lado_b = MathTex("b = 3", font_size=36).next_to(izquierda, UP, buff=0.2)
        lado_c = MathTex("c = 2", font_size=36).next_to(derecha, UP, buff=0.2)
        self.decir("La propiedad distributiva tiene una imagen sencilla: un rectángulo de altura dos, y base tres más dos.")
        self.play(Create(rect), FadeIn(lado_a), FadeIn(lado_b), FadeIn(lado_c))
        area_total = MathTex(r"a(b + c) = 2\cdot 5 = 10", font_size=42)
        area_partes = MathTex(r"ab + ac = 6 + 4 = 10", font_size=42)
        VGroup(area_total, area_partes).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(rect, RIGHT, buff=1)
        self.decir("El área del rectángulo entero es dos por cinco, diez. Y es la suma de las áreas de sus dos partes: seis más cuatro, diez.")
        self.play(Indicate(rect), Write(area_total))
        self.play(Indicate(izquierda), Indicate(derecha), Write(area_partes))
        self.pie("El área del rectángulo entero es la suma de las áreas de sus dos partes.", espera=3)
        usos = VGroup(
            Tex(r"Sacar factor común: \quad $3x + 5x = (3 + 5)x = 8x$", font_size=40),
            Tex(r"Con $a = -1$: \quad $-(b + c) = -b - c$", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(rect, DOWN, buff=0.9).align_to(rect, LEFT)
        self.decir("Leída al revés, es sacar factor común: tres equis más cinco equis es ocho equis.")
        self.play(FadeIn(usos[0]))
        self.wait(2)
        self.play(FadeIn(usos[1]))
        self.wait(4)
        self.limpiar(titulo)

        # Neutros, opuestos, inversos.
        titulo = self.cambiar_encabezado(titulo, "Neutros, opuestos e inversos")
        tabla = VGroup(
            Tex(r"Neutro de la suma: \quad $a + 0 = a$", font_size=42),
            Tex(r"Neutro del producto: \quad $a \cdot 1 = a$", font_size=42),
            Tex(r"Opuesto: \quad $a + (-a) = 0$", font_size=42),
            Tex(r"Inverso: \quad $a \cdot \frac{1}{a} = 1$ \quad (solo si $a \neq 0$)", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(UP * 0.6)
        self.decir("El cero no cambia una suma; el uno no cambia un producto. Todo número tiene opuesto, y todo número distinto de cero tiene inverso.")
        for linea in tabla:
            self.play(FadeIn(linea))
            self.wait(1)
        cero = MathTex(r"0 \cdot x = 0 \neq 1 \quad \text{para todo } x", font_size=42, color=COLOR_ERROR)
        cero.next_to(tabla, DOWN, buff=0.6)
        self.decir("El cero no: cero por cualquier cosa da cero, nunca uno. Por eso dividir entre a, que es multiplicar por su inverso, exige que a sea distinto de cero.")
        self.play(Write(cero))
        self.pie(
            "El 0 no tiene inverso. Dividir entre a es multiplicar por su inverso 1/a:\n"
            "por eso, otra vez, no se divide entre 0.",
            espera=5,
        )
        self.limpiar(titulo)

        # Jerarquía de operaciones.
        titulo = self.cambiar_encabezado(titulo, "El orden de las operaciones")
        expresion = MathTex(r"2 + 3\cdot 4", font_size=56).shift(UP * 1.8)
        self.decir("Por último, el orden de las operaciones. ¿Cuánto es dos más tres por cuatro?")
        self.play(Write(expresion))
        mal = MathTex(r"(2 + 3)\cdot 4 = 20", font_size=44, color=COLOR_ERROR)
        bien = MathTex(r"2 + 12 = 14", font_size=44, color=COLOR_SOLUCION)
        VGroup(mal, bien).arrange(RIGHT, buff=2).next_to(expresion, DOWN, buff=0.6)
        self.decir("Si sumamos primero, sale veinte: está mal.")
        self.play(FadeIn(mal))
        self.play(Create(Cross(mal, stroke_color=COLOR_ERROR)))
        self.decir("Primero se multiplica: tres por cuatro es doce, y dos más doce, catorce.")
        self.play(FadeIn(bien))
        orden = VGroup(
            Text("1.  Paréntesis", font_size=TAM_TEXTO),
            Text("2.  Potencias", font_size=TAM_TEXTO),
            Text("3.  Multiplicaciones y divisiones, de izquierda a derecha", font_size=TAM_TEXTO),
            Text("4.  Sumas y restas, de izquierda a derecha", font_size=TAM_TEXTO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(VGroup(mal, bien), DOWN, buff=0.7)
        self.decir("El orden es: paréntesis; potencias; multiplicaciones y divisiones; y al final, sumas y restas. Cuando hay empate, de izquierda a derecha.")
        self.play(LaggedStart(*[FadeIn(o) for o in orden], lag_ratio=0.4))
        self.wait(3)
        ejemplo = MathTex(r"18 - 6 \div 2 \cdot 3 = 18 - 3\cdot 3 = 18 - 9 = 9", font_size=44)
        ejemplo.next_to(orden, DOWN, buff=0.6)
        self.decir("Por ejemplo: dieciocho menos seis entre dos por tres. De izquierda a derecha: seis entre dos es tres, por tres es nueve, y dieciocho menos nueve es nueve.")
        self.play(Write(ejemplo))
        self.wait(4)

        self.ejercicio_propuesto(
            "F00-N2-02",
            VGroup(
                MathTex(r"\text{a) Calcula } 2 + 4\cdot(5 - 3)^2 \div 8", font_size=44),
                Tex(r"b) Calcula $7\cdot(10 + 3)$ de dos formas distintas.", font_size=40),
                Tex(r"¿Qué propiedad usa la segunda forma?", font_size=40),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Suma y producto son conmutativos y asociativos;\nresta y división, no.",
                "Distributiva: a(b + c) = ab + ac (sacar factor común es leerla al revés).",
                "0 es neutro de la suma, 1 del producto; el 0 no tiene inverso.",
                "Orden: paréntesis, potencias, × y ÷, + y −.",
            ],
            "Lección 2 — expresiones, igualdades y ecuaciones.",
            voz="En resumen: la suma y el producto son conmutativos y asociativos; la resta y la división, no. Propiedad distributiva: a por be más ce es a be más a ce; sacar factor común es leerla al revés. El cero es el neutro de la suma, y el uno, del producto; el cero no tiene inverso. Y el orden: paréntesis, potencias, multiplicaciones y divisiones, y al final sumas y restas. Siguiente: lección dos, expresiones, igualdades y ecuaciones.",
        )
