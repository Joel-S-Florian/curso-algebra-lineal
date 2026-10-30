"""Lección 15 — El método de reducción y comparación de métodos.

Escenas (un video cada una):
    ReduccionPasoAPaso, PorQueReduccionConservaSoluciones, ComparacionDeMetodos

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l15_reduccion.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import (  # noqa: E402
    EscenaCurso,
    ajustar_al_encuadre,
    alinear_por_igual,
    ejes_iguales,
    matriz_aumentada,
    num,
    paso_numerado,
    recta_general,
    rectas_de_sistema,
    sistema_con_llave,
)
from curso.estilo import *  # noqa: E402,F403


def bloque_suma(filas, etiquetas, signo: str) -> VGroup:
    """Ecuaciones apiladas para operarlas en columna: filas[-1] es el resultado.

    Devuelve VGroup(filas, etiquetas, linea, signo) ya colocado (alineado por '=').
    """
    ecuaciones = alinear_por_igual(*filas, buff=0.35)
    ecuaciones[-1].shift(DOWN * 0.25)  # sitio para la raya de la suma
    rotulos = VGroup(*[MathTex(e, font_size=34, color=COLOR_OPERACION).next_to(f, LEFT, buff=0.5) for e, f in zip(etiquetas, ecuaciones)])
    rotulos.align_to(rotulos[-1], RIGHT)
    raya = Line(LEFT, RIGHT).set_width(ecuaciones.width + 0.3).next_to(ecuaciones[-2], DOWN, buff=0.15).align_to(ecuaciones, LEFT).shift(LEFT * 0.15)
    # El signo va a la izquierda del rótulo de la segunda ecuación para no taparlo.
    marca = MathTex(signo, font_size=44, color=COLOR_OPERACION).next_to(rotulos[1], LEFT, buff=0.25)
    return VGroup(ecuaciones, rotulos, raya, marca)


def sumar_en_columna(escena: Scene, bloque: VGroup, columnas):
    """Anima la suma término a término: columnas = [(índices en las filas de arriba, índice en el resultado)]."""
    filas = bloque[0]
    escena.play(Create(bloque[2]), FadeIn(bloque[3]), FadeIn(bloque[1][-1]))
    for origenes, destino in columnas:
        partes = VGroup(*[filas[f][i] for f in range(len(filas) - 1) for i in origenes])
        escena.play(TransformFromCopy(partes, filas[-1][destino]), run_time=1.2)
    escena.play(FadeIn(filas[-1][3]))  # el signo '=' del resultado


class ReduccionPasoAPaso(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 15 · Parte 1", "El método de reducción")
        titulo = self.encabezado("Sumar ecuaciones para eliminar una incógnita")
        filas = [
            MathTex("3x", "+", "2y", "=", "7", font_size=48),
            MathTex("5x", "-", "2y", "=", "9", font_size=48),
            MathTex("8x", "+", "0y", "=", "16", font_size=48),
        ]
        bloque = bloque_suma(filas, ["E_1", "E_2", "E_1 + E_2"], "+").to_edge(LEFT, buff=1.4).shift(UP * 0.9)
        filas[0][2].set_color(COLORES_ECUACIONES[0])
        filas[1][1:3].set_color(COLORES_ECUACIONES[1])
        filas[2][2].set_color(COLOR_ERROR)
        self.decir("Tres equis más dos ye igual a siete, y cinco equis menos dos ye igual a nueve. Los coeficientes de ye son opuestos: más dos y menos dos.")
        self.play(Write(filas[0]), Write(filas[1]), FadeIn(bloque[1][:2]))
        self.pie("Los coeficientes de y son opuestos: +2 y −2. Si sumamos las dos ecuaciones, y desaparece.", espera=2)
        self.decir("Si sumamos las dos ecuaciones, los lados izquierdos entre sí y los derechos entre sí, la ye desaparece: queda ocho equis igual a dieciséis.")
        sumar_en_columna(self, bloque, [((0,), 0), ((1, 2), 2), ((4,), 4)])
        self.play(Indicate(filas[2][2], color=COLOR_ERROR))
        self.play(FadeIn(filas[2][1]))
        self.pie("Sumar ecuaciones = sumar los lados izquierdos entre sí y los derechos entre sí.", espera=2)
        pasos = VGroup(
            paso_numerado(1, r"8x = 16 \;\Rightarrow\; x = 2"),
            paso_numerado(2, r"3\cdot 2 + 2y = 7 \;\Rightarrow\; y = \tfrac{1}{2}"),
            paso_numerado(3, r"5\cdot 2 - 2\cdot\tfrac12 = 9\ \checkmark"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=0.9).match_y(bloque)
        self.decir("Equis vale dos. Sustituimos en la primera: seis más dos ye igual a siete, así que ye vale un medio. Y verificamos en la segunda: diez menos uno, nueve.")
        for p in pasos:
            self.play(FadeIn(p[0]), Write(p[1]))
            self.wait(1.5)
        self.wait(2)
        self.limpiar(titulo)

        # Cuando no hay coeficientes opuestos: fabricarlos.
        titulo = self.cambiar_encabezado(titulo, "Si no hay coeficientes opuestos, los fabricamos")
        sistema = sistema_con_llave(("2x + 3y", "=", "8"), ("3x - 4y", "=", "-5"), font_size=44).to_corner(UL, buff=0.7).shift(DOWN * 0.8)
        self.decir("Ahora, dos equis más tres ye igual a ocho, y tres equis menos cuatro ye igual a menos cinco. No hay coeficientes opuestos, así que los fabricamos.")
        self.play(Write(sistema))
        self.pie("Para eliminar x: multiplicamos E₁ por 3 y E₂ por 2 (regla 2), y así las dos tienen 6x.", espera=2)
        filas = [
            MathTex("6x", "+", "9y", "=", "24", font_size=46),
            MathTex("6x", "-", "8y", "=", "-10", font_size=46),
            MathTex("0x", "+", "17y", "=", "34", font_size=46),
        ]
        bloque = bloque_suma(filas, [r"3E_1", r"2E_2", r"3E_1 - 2E_2"], "-").to_edge(RIGHT, buff=1.2).shift(UP * 0.9)
        filas[0][0].set_color(COLORES_ECUACIONES[0])
        filas[1][0].set_color(COLORES_ECUACIONES[1])
        filas[2][0].set_color(COLOR_ERROR)
        self.decir("Multiplicamos la primera ecuación por tres y la segunda por dos, que no son cero: las dos tienen ahora seis equis.")
        for k in range(2):
            self.play(TransformFromCopy(sistema[1][k], filas[k]), FadeIn(bloque[1][k]), run_time=1.5)
        self.wait(1)
        self.decir("Ahora restamos: seis equis menos seis equis es cero, y queda diecisiete ye igual a treinta y cuatro.")
        self.pie("Ahora restamos: 6x − 6x = 0.", espera=1)
        sumar_en_columna(self, bloque, [((0,), 0), ((1, 2), 2), ((4,), 4)])
        self.play(FadeIn(filas[2][1]))
        pasos = VGroup(
            paso_numerado(1, r"17y = 34 \;\Rightarrow\; y = 2"),
            paso_numerado(2, r"2x + 3\cdot 2 = 8 \;\Rightarrow\; x = 1"),
            paso_numerado(3, r"3\cdot 1 - 4\cdot 2 = -5\ \checkmark"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(sistema, DOWN, buff=0.7, aligned_edge=LEFT)
        self.decir("Ye vale dos. En la primera: dos equis más seis igual a ocho, equis vale uno. Y verificamos: tres menos ocho, menos cinco.")
        for p in pasos:
            self.play(FadeIn(p[0]), Write(p[1]))
            self.wait(1.5)
        self.decir("Restar es sumar después de multiplicar por menos uno.")
        self.pie("Restar es sumar después de multiplicar por −1: también podríamos usar 3E₁ + (−2)E₂.", espera=4)

        self.ejercicio_propuesto(
            "F04-N2-03",
            VGroup(
                Text("Resuelve por reducción y verifica:", font_size=TAM_TEXTO),
                sistema_con_llave(("4x + 3y", "=", "10"), ("6x - 5y", "=", "-4"), font_size=48, colores=False),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Si una incógnita tiene coeficientes opuestos, sumar las ecuaciones la elimina.",
                "Si no, se multiplican las ecuaciones por números no nulos para fabricarlos.",
                "Se resuelve la ecuación resultante y se sustituye en una original.",
            ],
            "por qué reducir no cambia las soluciones.",
            voz="En resumen: si una incógnita tiene coeficientes opuestos, sumar las ecuaciones la elimina. Si no, se multiplican las ecuaciones por números distintos de cero para fabricarlos. Después se resuelve la ecuación resultante y se sustituye en una de las originales. Siguiente: por qué reducir no cambia las soluciones.",
        )


class PorQueReduccionConservaSoluciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 15 · Parte 2", "¿Por qué reducir no cambia las soluciones?")
        titulo = self.encabezado("Cambiar E₂ por E₂ + k·E₁")
        bloque = VGroup(
            MathTex(r"\begin{cases} E_1 \\ E_2 \end{cases} \quad\longrightarrow\quad \begin{cases} E_1 \\ E_2 + k\,E_1 \end{cases}", font_size=50),
            Tex(r"$\Rightarrow$ \ Si $(x, y)$ cumple $E_1$ y $E_2$, cumple su combinación: se suman igualdades ciertas.", font_size=36),
            Tex(r"$\Leftarrow$ \ Si cumple $E_1$ y $E_2 + kE_1$, entonces $E_2 = (E_2 + kE_1) - kE_1$ también se cumple.", font_size=36),
            Tex(r"El paso se deshace restando $k\,E_1$: los dos sistemas tienen exactamente las mismas soluciones.", font_size=36, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.45)
        ajustar_al_encuadre(bloque)
        self.decir("Cambiamos la segunda ecuación por ella misma más ka veces la primera, y conservamos la primera. Toda solución del sistema cumple la combinación, porque sumamos igualdades ciertas. Y al revés: restando ka veces la primera, recuperamos la segunda. El paso se deshace, así que los dos sistemas tienen exactamente las mismas soluciones.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.4)
        self.decir("La clave es que la primera ecuación se conserva: gracias a ella podemos volver atrás.")
        self.pie("Clave: E₁ se CONSERVA. Gracias a ella podemos volver atrás.", espera=3)
        self.limpiar(titulo)

        # El haz de rectas: la combinación gira alrededor de la solución.
        titulo = self.cambiar_encabezado(titulo, "En el dibujo: la nueva recta gira alrededor de la solución")
        plano = ejes_iguales((-1, 5), (-2, 4), unidad=0.8).to_edge(LEFT, buff=0.8).shift(DOWN * 0.3)
        sistema = sistema_con_llave(("x + y", "=", "3"), ("x - y", "=", "1"), font_size=40).to_edge(RIGHT, buff=1.5).shift(UP * 2.1)
        self.decir("Veámoslo en el dibujo: equis más ye igual a tres, y equis menos ye igual a uno, que se cortan en dos, uno.")
        self.play(Create(plano), FadeIn(sistema), Create(rectas_de_sistema(plano, [(1, 1, 3), (1, -1, 1)])))
        self.play(FadeIn(Dot(plano.c2p(2, 1), color=COLOR_PIVOTE, radius=0.1), scale=2))
        k = ValueTracker(0)

        def combinada():
            kv = k.get_value()
            return recta_general(plano, 1 + kv, kv - 1, 1 + 3 * kv, color=COLOR_OPERACION, stroke_width=6)

        def lectura():
            kv = k.get_value()
            return VGroup(
                MathTex(rf"k = {num(kv)}", font_size=40, color=COLOR_OPERACION),
                MathTex(rf"E_2 + kE_1:\ ({num(1 + kv)})\,x + ({num(kv - 1)})\,y = {num(1 + 3 * kv)}", font_size=34, color=COLOR_OPERACION),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(sistema, DOWN, buff=0.6).to_edge(RIGHT, buff=0.6)

        recta, panel = always_redraw(combinada), always_redraw(lectura)
        self.decir("La recta violeta es la combinación: la segunda ecuación más ka veces la primera.")
        self.play(Create(recta), FadeIn(panel))
        self.decir("Al cambiar ka, la recta combinada gira alrededor de la solución, sin despegarse de ella. Por eso la solución no cambia.")
        for valor in (0.5, 3, -0.5, -3):
            self.play(k.animate.set_value(valor), run_time=2)
        self.pie("Para cualquier k, la recta nueva pasa por (2, 1): por eso la solución no cambia.", espera=2)
        self.decir("Con ka igual a uno, sumar, queda dos equis igual a cuatro: una recta vertical. Se lee directamente equis igual a dos.")
        self.play(k.animate.set_value(1), run_time=2)
        self.pie("Con k = 1 (sumar): 2x = 4, recta vertical. Se lee x = 2 directamente.", espera=3)
        self.decir("Con ka igual a menos uno, restar, queda menos dos ye igual a menos dos: una recta horizontal. Se lee ye igual a uno.")
        self.play(k.animate.set_value(-1), run_time=2)
        self.pie("Con k = −1 (restar): −2y = −2, recta horizontal. Se lee y = 1.", espera=3)
        self.decir("Reducir es girar una recta alrededor de la solución, hasta que la respuesta se lea directamente.")
        self.pie("Reducir = girar una recta alrededor de la solución hasta que quede vertical u horizontal.", espera=4)
        self.limpiar(titulo)

        # Error: cambiar las dos ecuaciones a la vez.
        titulo = self.cambiar_encabezado(titulo, "Error frecuente: cambiar las dos ecuaciones a la vez")
        bloque = VGroup(
            MathTex(r"\begin{cases} x + y = 3 \\ x - y = 1 \end{cases} \;\longrightarrow\; \begin{cases} E_1 + E_2:\ 2x = 4 \\ E_1 + E_2:\ 2x = 4 \end{cases}", font_size=44),
            Tex(r"Las dos ecuaciones nuevas son la misma: \textbf{se perdió información}.", font_size=38, color=COLOR_ERROR),
            Tex(r"El sistema nuevo admite $(2, 7)$, que no cumple $x + y = 3$.", font_size=38, color=COLOR_ERROR),
            Tex(r"Regla: se cambia \textbf{una} ecuación usando otra que se \textbf{conserva}. Y nunca se multiplica por 0.", font_size=38, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.5)
        ajustar_al_encuadre(bloque)
        self.decir("Un error frecuente: cambiar las dos ecuaciones a la vez. Si las dos se convierten en la primera más la segunda, nos quedamos con dos copias de la misma información, y el sistema nuevo admite soluciones falsas, como dos, siete. La regla: se cambia una ecuación usando otra que se conserva. Y nunca se multiplica por cero.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.4)

        self.ejercicio_propuesto(
            "F04-N4-01",
            VGroup(
                Text("Un estudiante resuelve el sistema así. ¿Dónde está el error? Resuélvelo bien.", font_size=TAM_TEXTO),
                MathTex(
                    r"\begin{cases} 2x + y = 5 \\ x - y = 1 \end{cases} \to \begin{cases} E_1 - E_2:\ x + 2y = 4 \\ E_2 - E_1:\ -x - 2y = -4 \end{cases} \to \text{infinitas soluciones}",
                    font_size=40,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Cambiar E₂ por E₂ + k·E₁ (conservando E₁) no cambia las soluciones: se puede deshacer.",
                "Geométricamente, la nueva recta gira alrededor de la solución.",
                "No se cambian las dos ecuaciones a la vez ni se multiplica por 0.",
            ],
            "comparar los tres métodos.",
            voz="En resumen: cambiar la segunda ecuación por ella misma más ka veces la primera, conservando la primera, no cambia las soluciones, porque se puede deshacer. Geométricamente, la nueva recta gira alrededor de la solución. Y no se cambian las dos ecuaciones a la vez, ni se multiplica por cero. Siguiente: comparar los tres métodos.",
        )


class ComparacionDeMetodos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 15 · Parte 3", "¿Qué método elegir?")
        titulo = self.encabezado("Comparación de los tres métodos")
        celdas = [
            ("Método", "Conviene cuando…", "Limitación"),
            ("Sustitución", "una incógnita tiene\ncoeficiente 1 o −1", "fracciones si no;\nse alarga con más incógnitas"),
            ("Igualación", "la misma incógnita ya está\ndespejada en las dos", "dos despejes;\nno escala a 3 incógnitas"),
            ("Reducción", "hay coeficientes opuestos\no múltiplos fáciles", "elegir multiplicadores;\nes la base de Gauss"),
        ]
        colores = [WHITE, COLOR_COEFICIENTE, COLOR_TERMINO_INDEP, COLOR_SOLUCION]
        tabla = VGroup()
        for fila, color in zip(celdas, colores):
            for j, texto in enumerate(fila):
                peso = "BOLD" if fila is celdas[0] or j == 0 else "NORMAL"
                tabla.add(Text(texto, font_size=TAM_NOTA, color=color if j == 0 or fila is celdas[0] else WHITE, weight=peso, line_spacing=1.1))
        tabla.arrange_in_grid(rows=4, cols=3, buff=(0.8, 0.45), col_alignments="lll")
        ajustar_al_encuadre(tabla)
        self.decir("Comparemos los tres métodos.")
        self.play(FadeIn(tabla[:3]))
        self.decir("La sustitución conviene cuando una incógnita tiene coeficiente uno o menos uno. La igualación, cuando la misma incógnita ya está despejada en las dos ecuaciones. Y la reducción, cuando hay coeficientes opuestos o múltiplos fáciles; es la base del método de Gauss.")
        for i in range(1, 4):
            self.play(FadeIn(tabla[3 * i: 3 * i + 3], shift=RIGHT * 0.2))
            self.wait(2.2)
        self.decir("Los tres métodos llegan a la misma solución. Elegir bien solo ahorra cuentas, y errores.")
        self.pie("Los tres llegan a la misma solución: elegir bien solo ahorra cuentas (y errores).", espera=3)
        self.limpiar(titulo)

        # Reducción con tres incógnitas: anticipo de Gauss.
        titulo = self.cambiar_encabezado(titulo, "Reducción con tres incógnitas")
        original = sistema_con_llave(("x + y + z", "=", "6"), ("x - y + z", "=", "2"), ("x + y - z", "=", "0"), font_size=42, colores=False)
        original.to_edge(LEFT, buff=0.9).shift(UP * 1.2)
        self.decir("Con tres incógnitas, la reducción es la más práctica.")
        self.play(Write(original))
        reducido = sistema_con_llave(("x + y + z", "=", "6"), ("-2y", "=", "-4"), ("-2z", "=", "-6"), font_size=42, colores=False)
        reducido.to_edge(RIGHT, buff=1.5).match_y(original)
        operaciones = VGroup(
            MathTex(r"E_2 \leftarrow E_2 - E_1", font_size=34, color=COLOR_OPERACION),
            MathTex(r"E_3 \leftarrow E_3 - E_1", font_size=34, color=COLOR_OPERACION),
        ).arrange(DOWN, buff=0.3).move_to((original.get_right() + reducido.get_left()) / 2)
        flecha = Arrow(original.get_right(), reducido.get_left(), buff=0.3).next_to(operaciones, DOWN, buff=0.15)
        self.decir("Usamos la primera ecuación para eliminar equis de las otras dos: a la segunda le restamos la primera, y a la tercera también.")
        self.play(FadeIn(operaciones), GrowArrow(flecha))
        self.play(TransformFromCopy(original, reducido), run_time=2)
        self.decir("Cada ecuación queda con una incógnita menos.")
        self.pie("Con E₁ eliminamos x de las otras dos ecuaciones. Cada ecuación queda con UNA incógnita menos.", espera=2)
        solucion = MathTex(r"y = 2,\quad z = 3,\quad x = 6 - 2 - 3 = 1", font_size=44, color=COLOR_SOLUCION)
        solucion.next_to(VGroup(original, reducido), DOWN, buff=0.8)
        self.decir("Ye vale dos, zeta vale tres, y equis, seis menos dos menos tres: uno.")
        self.play(Write(solucion))
        self.wait(2)
        self.decir("Hacer esto de forma ordenada, ecuación a ecuación, es exactamente la eliminación de Gauss, de la unidad cuatro.")
        self.pie("Hacer esto de forma ordenada, ecuación a ecuación, es exactamente la eliminación de Gauss (Unidad 4).", espera=3)
        self.limpiar(titulo)

        # Solo importan los números.
        titulo = self.cambiar_encabezado(titulo, "Las letras solo ocupan sitio")
        sistema = sistema_con_llave(("x + y + z", "=", "6"), ("x - y + z", "=", "2"), ("x + y - z", "=", "0"), font_size=44, colores=False).shift(LEFT * 3.5)
        matriz = matriz_aumentada([["1", "1", "1", "6"], ["1", "-1", "1", "2"], ["1", "1", "-1", "0"]]).shift(RIGHT * 3)
        self.decir("Y fíjate: las letras solo ocupan sitio.")
        self.play(FadeIn(sistema))
        self.decir("Las operaciones de reducción solo cambian los números. Si guardamos solo los números en una tabla, obtenemos una matriz: es lo que estudia la unidad tres.")
        self.play(GrowArrow(Arrow(sistema.get_right(), matriz.get_left(), buff=0.4)), FadeIn(matriz))
        self.pie(
            "Las operaciones de reducción solo cambian los números. Si guardamos solo los números en una tabla,\n"
            "obtenemos una MATRIZ: es lo que estudia la Unidad 3.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F04-N3-03",
            VGroup(
                Text("Elige el método más cómodo para cada sistema y resuélvelo:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \begin{cases} y = 2x + 1 \\ 3x + y = 11 \end{cases} \quad"
                    r"\text{b) } \begin{cases} 5x + 2y = 1 \\ 3x - 2y = 15 \end{cases} \quad"
                    r"\text{c) } \begin{cases} y = 4 - x \\ y = 2x - 5 \end{cases}",
                    font_size=44,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Sustitución: si hay un coeficiente 1 o −1. Igualación: si ya hay despejes.",
                "Reducción: el método más general; con 3 o más incógnitas es el único práctico.",
                "La reducción ordenada se llama eliminación de Gauss.",
                "Solo importan los números: matrices.",
            ],
            "Unidad 3, Lección 16 — ¿qué es una matriz?",
            voz="En resumen: la sustitución conviene si hay un coeficiente uno o menos uno, y la igualación, si ya hay despejes. La reducción es el método más general: con tres o más incógnitas es el único práctico. La reducción ordenada se llama eliminación de Gauss. Y solo importan los números: matrices. Siguiente: unidad tres, lección dieciséis, ¿qué es una matriz?",
        )
