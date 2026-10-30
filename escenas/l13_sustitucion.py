"""Lección 13 — El método de sustitución.

Escenas (un video cada una):
    SustitucionPasoAPaso, SustitucionCuandoConviene, SustitucionCasosEspeciales

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l13_sustitucion.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import (  # noqa: E402
    EscenaCurso,
    ajustar_al_encuadre,
    ejes_iguales,
    num,
    paso_numerado,
    rectas_de_sistema,
    resolver_paso_a_paso,
    sistema_con_llave,
)
from curso.estilo import *  # noqa: E402,F403


class SustitucionPasoAPaso(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 13 · Parte 1", "El método de sustitución")
        titulo = self.encabezado("Idea: quedarnos con una sola incógnita")
        sistema = sistema_con_llave(("3x + y", "=", "11"), ("x - 2y", "=", "-1"), font_size=46)
        sistema.to_corner(UL, buff=0.8).shift(DOWN * 0.8)
        self.decir("Tres equis más ye igual a once, y equis menos dos ye igual a menos uno. Ya sabemos resolver ecuaciones con una incógnita. La idea de la sustitución es convertir el sistema en una de ellas.")
        self.play(Write(sistema))
        self.pie("Ya sabemos resolver ecuaciones con UNA incógnita (Lección 6). Sustituir sirve para eliminar una.", espera=3)

        e1, e2 = sistema[1]
        pasos = VGroup(
            paso_numerado(1, "y", "=", "11 - 3x"),
            paso_numerado(2, "x - 2", "(", "11 - 3x", ")", "=", "-1"),
            paso_numerado(3, r"x - 22 + 6x = -1 \;\Rightarrow\; 7x = 21 \;\Rightarrow\; x = 3"),
            paso_numerado(4, r"y = 11 - 3\cdot 3 = 2"),
            paso_numerado(5, r"3\cdot 3 + 2 = 11\ \checkmark \qquad 3 - 2\cdot 2 = -1\ \checkmark"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        pasos.next_to(sistema, DOWN, buff=0.5, aligned_edge=LEFT)
        pasos[1][1][2].set_color(COLOR_COEFICIENTE)
        pasos[0][1][2].set_color(COLOR_COEFICIENTE)

        self.decir("Primero, despejamos ye en la primera ecuación, donde su coeficiente es uno: así no aparecen fracciones. Ye es igual a once menos tres equis.")
        self.play(Indicate(e1))
        self.pie("1. Despejamos y en la primera ecuación: su coeficiente es 1, así no aparecen fracciones.")
        self.play(FadeIn(pasos[0][0]), TransformFromCopy(e1, pasos[0][1]))
        self.wait(2)
        self.decir("Segundo: en la segunda ecuación escribimos once menos tres equis en lugar de ye, entre paréntesis.")
        self.play(Indicate(e2))
        self.pie("2. En la segunda ecuación escribimos 11 − 3x en lugar de y, ENTRE PARÉNTESIS.")
        formula = pasos[1][1]
        self.play(FadeIn(pasos[1][0]), Write(VGroup(formula[0], formula[1], formula[3], formula[4], formula[5])))
        self.play(TransformFromCopy(pasos[0][1][2], formula[2]), run_time=1.5)
        self.wait(2)
        self.decir("Tercero: queda una ecuación con una sola incógnita, y la resolvemos como en la lección seis. Equis vale tres.")
        self.pie("3. Queda una ecuación con una sola incógnita: la resolvemos como en la Lección 6.")
        self.play(FadeIn(pasos[2][0]), Write(pasos[2][1]), run_time=2)
        self.wait(2)
        self.decir("Cuarto: volvemos al despeje para calcular ye. Once menos nueve: ye vale dos.")
        self.pie("4. Volvemos al despeje para calcular y.")
        self.play(FadeIn(pasos[3][0]), Write(pasos[3][1]))
        self.wait(1.5)
        self.decir("Y quinto: verificamos en las dos ecuaciones originales.")
        self.pie("5. Verificamos en las dos ecuaciones ORIGINALES.")
        self.play(FadeIn(pasos[4][0]), Write(pasos[4][1]))
        solucion = MathTex(r"(x, y) = (3, 2)", font_size=48, color=COLOR_SOLUCION).next_to(sistema, RIGHT, buff=1.5)
        self.decir("La solución es tres, dos.")
        self.play(Write(solucion), Create(SurroundingRectangle(solucion, color=COLOR_SOLUCION, buff=0.2)))
        self.wait(3)
        self.limpiar(titulo)

        # Justificación.
        titulo = self.cambiar_encabezado(titulo, "¿Por qué no se pierden ni se ganan soluciones?")
        equivalencia = MathTex(
            r"\begin{cases} 3x + y = 11 \\ x - 2y = -1 \end{cases}",
            r"\quad\Longleftrightarrow\quad",
            r"\begin{cases} y = 11 - 3x \\ x - 2(11 - 3x) = -1 \end{cases}",
            font_size=46,
        ).shift(UP * 1.4)
        self.decir("¿Por qué funciona? Porque el sistema nuevo tiene exactamente las mismas soluciones que el original.")
        self.play(Write(equivalencia), run_time=2)
        razones = VGroup(
            Tex(r"Primera fila: despejar $y$ solo usa las reglas 1 y 2 (pasos reversibles).", font_size=36),
            Tex(r"Segunda fila: si $y$ vale $11 - 3x$, escribir $11 - 3x$ en su lugar no cambia nada.", font_size=36),
            Tex(r"Los dos sistemas tienen las mismas soluciones, y el de la derecha tiene una ecuación \emph{solo con $x$}.", font_size=36, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(equivalencia, DOWN, buff=0.7)
        ajustar_al_encuadre(razones)
        self.decir("Despejar ye solo usa las reglas uno y dos, que se pueden deshacer. Y si ye vale once menos tres equis, escribir una cosa u otra es lo mismo. El sistema nuevo tiene una ecuación solo con equis.")
        for r in razones:
            self.play(FadeIn(r))
            self.wait(2.2)
        self.limpiar(titulo)

        # Geometría: recorrer la primera recta hasta tocar la segunda.
        titulo = self.cambiar_encabezado(titulo, "En el dibujo: recorrer una recta hasta tocar la otra")
        plano = ejes_iguales((-1, 5), (-2, 7), unidad=0.6).to_edge(LEFT, buff=0.9).shift(DOWN * 0.3)
        self.decir("En el dibujo, al usar ye igual a once menos tres equis, solo miramos puntos de la recta azul.")
        self.play(Create(plano), Create(rectas_de_sistema(plano, [(3, 1, 11), (1, -2, -1)])))
        x = ValueTracker(1.5)
        punto = always_redraw(lambda: Dot(plano.c2p(x.get_value(), 11 - 3 * x.get_value()), color=COLOR_PIVOTE, radius=0.1))

        def lectura():
            valor = 7 * x.get_value() - 22  # x - 2y con y = 11 - 3x
            color = COLOR_SOLUCION if abs(valor + 1) < 0.05 else WHITE
            return VGroup(
                MathTex(rf"(x,\ 11 - 3x) = ({num(x.get_value())},\ {num(11 - 3 * x.get_value())})", font_size=36, color=COLOR_PIVOTE),
                MathTex(rf"x - 2y = {num(valor)}", font_size=44, color=color),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=0.8).shift(UP * 0.8)

        explicacion = Text(
            "Con y = 11 − 3x solo miramos puntos de la recta azul.\nBuscamos el que además cumple x − 2y = −1.",
            font_size=TAM_NOTA,
            line_spacing=1.2,
        ).to_edge(RIGHT, buff=0.6).shift(DOWN * 1.2)
        panel = always_redraw(lectura)
        self.decir("Movemos el punto por la recta azul. La segunda ecuación nos dice cuál de ellos está también en la naranja.")
        self.play(FadeIn(punto), FadeIn(panel), FadeIn(explicacion))
        for valor in (4.2, 2.0, 3.0):
            self.play(x.animate.set_value(valor), run_time=2.5)
            self.wait(0.6)
        self.decir("En equis igual a tres, el punto cae justo sobre la recta naranja: es la solución, tres, dos.")
        self.play(Flash(punto, color=COLOR_SOLUCION))
        self.pie("En x = 3 el punto azul cae justo sobre la recta naranja: es la solución (3, 2).", espera=4)

        self.ejercicio_propuesto(
            "F04-N1-01",
            VGroup(
                Text("Resuelve por sustitución y verifica:", font_size=TAM_TEXTO),
                sistema_con_llave(("2x + y", "=", "8"), ("x - y", "=", "1"), font_size=48, colores=False),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Despejar una incógnita en una ecuación.",
                "Sustituirla (entre paréntesis) en la otra: queda una ecuación con una incógnita.",
                "Resolverla, volver al despeje y verificar en las ecuaciones originales.",
                "Funciona porque el sistema nuevo es equivalente al original.",
            ],
            "cuándo conviene sustituir.",
            voz="En resumen: en el método de sustitución, despejamos una incógnita en una ecuación y la sustituimos, entre paréntesis, en la otra. Queda una ecuación con una incógnita; la resolvemos, volvemos al despeje y verificamos en las ecuaciones originales. Siguiente: cuándo conviene sustituir.",
        )


class SustitucionCuandoConviene(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 13 · Parte 2", "¿Cuándo conviene sustituir?")
        titulo = self.encabezado("Elegir bien qué despejar")
        sistema = sistema_con_llave(("2x + 3y", "=", "7"), ("5x - 4y", "=", "6"), font_size=46).to_edge(LEFT, buff=0.9).shift(UP * 1.6)
        self.decir("Dos equis más tres ye igual a siete, y cinco equis menos cuatro ye igual a seis.")
        self.play(Write(sistema))
        opciones = VGroup(
            MathTex(r"x = \frac{7 - 3y}{2}", font_size=40),
            MathTex(r"y = \frac{7 - 2x}{3}", font_size=40),
            MathTex(r"x = \frac{6 + 4y}{5}", font_size=40),
            MathTex(r"y = \frac{5x - 6}{4}", font_size=40),
        ).arrange_in_grid(rows=2, cols=2, buff=(1.0, 0.5)).to_edge(RIGHT, buff=1.0).match_y(sistema)
        self.decir("Ningún coeficiente es uno o menos uno: cualquier despeje trae fracciones. Se puede igual, con más cuidado.")
        self.play(LaggedStart(*[FadeIn(o) for o in opciones], lag_ratio=0.3))
        self.pie("Ningún coeficiente es 1 o −1: cualquier despeje trae fracciones. Se puede, pero con más cuidado.", espera=3)
        self.play(*[FadeOut(o) for o in opciones[1:]], opciones[0].animate.set_color(COLOR_COEFICIENTE))
        self.decir("Despejamos equis en la primera: siete menos tres ye, entre dos. Lo sustituimos en la segunda, y multiplicamos por dos para quitar el denominador. Treinta y cinco menos quince ye menos ocho ye, igual a doce. Menos veintitrés ye igual a menos veintitrés: ye vale uno.")
        bloque = resolver_paso_a_paso(
            self,
            [(r"5\cdot\frac{7 - 3y}{2} - 4y", "6"), ("35 - 15y - 8y", "12"), ("-23y", "-23"), ("y", "1")],
            ["multiplicar ambos lados por 2", "agrupar los términos con y", "dividir entre −23"],
            font_size=40,
            debajo_de=sistema,
        )
        final = MathTex(r"x = \frac{7 - 3\cdot 1}{2} = 2 \qquad \text{verificación: } 4 + 3 = 7\ \checkmark \quad 10 - 4 = 6\ \checkmark", font_size=38, color=COLOR_SOLUCION)
        final.next_to(bloque, DOWN, buff=0.4, aligned_edge=LEFT)
        ajustar_al_encuadre(final)
        self.quitar_pie()
        self.decir("Entonces equis vale siete menos tres, entre dos: dos. Y la verificación confirma las dos ecuaciones.")
        self.play(Write(final))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Con tres incógnitas también funciona… pero se alarga")
        sistema = sistema_con_llave(("x + y + z", "=", "6"), ("x - y + z", "=", "2"), ("x + y - z", "=", "0"), font_size=40).to_edge(LEFT, buff=0.8).shift(UP * 1.4)
        self.decir("Con tres incógnitas también funciona.")
        self.play(Write(sistema))
        pasos = VGroup(
            paso_numerado(1, r"z = 6 - x - y", font_size=36),
            paso_numerado(2, r"x - y + (6 - x - y) = 2 \;\Rightarrow\; -2y = -4 \;\Rightarrow\; y = 2", font_size=36),
            paso_numerado(3, r"x + y - (6 - x - y) = 0 \;\Rightarrow\; 2x + 2y = 6 \;\Rightarrow\; x = 1", font_size=36),
            paso_numerado(4, r"z = 6 - 1 - 2 = 3 \qquad (x, y, z) = (1, 2, 3)", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(sistema, DOWN, buff=0.5, aligned_edge=LEFT)
        ajustar_al_encuadre(pasos)
        self.decir("Despejamos una incógnita, la sustituimos en las otras dos ecuaciones, y repetimos con el sistema más pequeño que queda. Pero cada sustitución alarga las expresiones.")
        for p in pasos:
            self.play(FadeIn(p[0]), Write(p[1]))
            self.wait(1.8)
        self.decir("Con cinco o diez incógnitas sería inmanejable: necesitaremos un método más ordenado.")
        self.pie(
            "Aquí hubo suerte (y y x se despejaron solas). Con coeficientes cualesquiera, o con 5 o 10 incógnitas,\n"
            "las expresiones sustituidas crecen sin control. Hará falta un método más ordenado.",
            espera=6,
        )

        self.ejercicio_propuesto(
            "F04-N2-01",
            VGroup(
                Text("Resuelve por sustitución (aparecerán fracciones) y verifica:", font_size=TAM_TEXTO),
                sistema_con_llave(("3x + 2y", "=", "12"), ("4x - 5y", "=", "-7"), font_size=48, colores=False),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Conviene despejar una incógnita con coeficiente 1 o −1.",
                "Si no la hay, sustituir funciona, pero con fracciones.",
                "Con muchas incógnitas, las sustituciones se vuelven largas.",
            ],
            "qué pasa cuando el sistema no tiene solución única.",
            voz="En resumen: conviene despejar la incógnita con coeficiente uno o menos uno. Si no lo hay, se puede igual, multiplicando para quitar denominadores. Y con tres incógnitas funciona, pero se alarga: hará falta un método más ordenado. Siguiente: qué pasa cuando la incógnita desaparece.",
        )


class SustitucionCasosEspeciales(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 13 · Parte 3", "Sustitución: cuando la incógnita desaparece")
        titulo = self.encabezado("Caso 1: llegamos a 0 = 0")
        sistema = sistema_con_llave(("x + 2y", "=", "4"), ("2x + 4y", "=", "8"), font_size=44).to_edge(LEFT, buff=0.9).shift(UP * 1.6)
        self.decir("A veces la incógnita desaparece. Equis más dos ye igual a cuatro, y dos equis más cuatro ye igual a ocho.")
        self.play(Write(sistema))
        self.decir("Despejamos equis igual a cuatro menos dos ye, y sustituimos en la segunda: ocho menos cuatro ye más cuatro ye, igual a ocho. La ye se cancela: cero por ye igual a cero.")
        bloque = resolver_paso_a_paso(
            self,
            [("2(4 - 2y) + 4y", "8"), ("8 - 4y + 4y", "8"), ("0\\cdot y", "0")],
            ["despejamos x = 4 − 2y en la 1.ª y sustituimos", "la y se cancela"],
            font_size=42,
            debajo_de=sistema,
        )
        conclusion = MathTex(r"\text{todo } y \text{ sirve: } y = t,\ x = 4 - 2t \ \Rightarrow\ \text{SCI}", font_size=40, color=COLOR_LIBRE)
        conclusion.next_to(bloque, DOWN, buff=0.5, aligned_edge=LEFT)
        self.decir("Cualquier valor de ye sirve: infinitas soluciones. Con ye igual a te, equis vale cuatro menos dos te. La segunda ecuación era el doble de la primera.")
        self.play(Write(conclusion))
        self.pie("0·y = 0 se cumple para cualquier y: infinitas soluciones (la 2.ª ecuación era el doble de la 1.ª).", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Caso 2: llegamos a una igualdad falsa")
        sistema = sistema_con_llave(("x + 2y", "=", "4"), ("2x + 4y", "=", "3"), font_size=44).to_edge(LEFT, buff=0.9).shift(UP * 1.6)
        self.decir("Ahora cambiamos el ocho por un tres.")
        self.play(Write(sistema))
        self.decir("Al sustituir, la ye vuelve a desaparecer, pero queda ocho igual a tres: cero por ye igual a menos cinco.")
        bloque = resolver_paso_a_paso(
            self,
            [("2(4 - 2y) + 4y", "3"), ("8", "3"), ("0\\cdot y", "-5")],
            ["la y se cancela", "restando 8"],
            font_size=42,
            debajo_de=sistema,
        )
        conclusion = MathTex(r"\text{ningún } y \text{ cumple } 0\cdot y = -5 \ \Rightarrow\ \text{SI}", font_size=40, color=COLOR_ERROR)
        conclusion.next_to(bloque, DOWN, buff=0.5, aligned_edge=LEFT)
        self.decir("Ningún valor de ye lo cumple: el sistema no tiene solución. Son rectas paralelas.")
        self.play(Write(conclusion))
        self.pie("Rectas paralelas: ninguna solución.", espera=3)
        self.limpiar(titulo)

        # La ecuación final decide.
        titulo = self.cambiar_encabezado(titulo, "La ecuación con una incógnita decide el tipo de sistema")
        filas = [
            (r"a\,y = b,\ a \neq 0", "una solución: SCD", COLOR_SOLUCION),
            (r"0\cdot y = 0", "infinitas: SCI", COLOR_LIBRE),
            (r"0\cdot y = b,\ b \neq 0", "ninguna: SI", COLOR_ERROR),
        ]
        tabla = VGroup()
        for tex, texto, color in filas:
            tabla.add(MathTex(tex, font_size=46), Text(texto, font_size=TAM_TEXTO, color=color))
        tabla.arrange_in_grid(rows=3, cols=2, buff=(1.2, 0.6), col_alignments="ll")
        self.decir("La ecuación final con una incógnita decide el tipo de sistema. Si su coeficiente no es cero, una solución. Si queda cero igual a cero, infinitas. Si queda cero igual a un número distinto de cero, ninguna. Son los tres casos de la lección seis.")
        for i in range(3):
            self.play(FadeIn(tabla[2 * i]), FadeIn(tabla[2 * i + 1]))
            self.wait(1.2)
        self.pie("Son los tres casos de ax = b (Lección 6), ahora diciendo cuántas soluciones tiene el SISTEMA.", espera=4)
        self.limpiar(titulo)

        # Error frecuente: sustituir en la misma ecuación.
        titulo = self.cambiar_encabezado(titulo, "Error frecuente: sustituir en la MISMA ecuación")
        bloque = VGroup(
            MathTex(r"\begin{cases} 3x + y = 11 \\ x - 2y = -1 \end{cases}", font_size=44),
            MathTex(r"y = 11 - 3x \ \text{ en la primera: }\ 3x + (11 - 3x) = 11 \ \Rightarrow\ 11 = 11", font_size=40, color=COLOR_ERROR),
            Tex(r"Siempre sale $0 = 0$: no dice nada. ¡El sistema de la Parte 1 tenía solución única!", font_size=36, color=COLOR_ERROR),
            Tex(r"El despeje se sustituye en la \textbf{otra} ecuación.", font_size=40, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.5)
        self.decir("Cuidado con un error frecuente: si sustituimos el despeje en la misma ecuación de la que salió, siempre obtenemos una identidad, como once igual a once, que no dice nada. Hay que sustituir en la otra ecuación.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2.2)

        self.ejercicio_propuesto(
            "F04-N3-01",
            VGroup(
                Text("Clasifica por sustitución y, si hay infinitas soluciones, parametrízalas:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \begin{cases} x - 3y = 2 \\ -2x + 6y = -4 \end{cases} \qquad \text{b) } \begin{cases} x - 3y = 2 \\ -2x + 6y = 1 \end{cases}",
                    font_size=46,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Si la incógnita desaparece: 0 = 0 da infinitas soluciones; 0 = b con b distinto de 0, ninguna.",
                "La ecuación final con una incógnita decide si el sistema es SCD, SCI o SI.",
                "El despeje se sustituye en la OTRA ecuación.",
            ],
            "Lección 14 — el método de igualación.",
            voz="En resumen: si al sustituir queda cero igual a cero, el sistema tiene infinitas soluciones; si queda una igualdad falsa, ninguna. La ecuación con una incógnita decide el tipo de sistema. Y el despeje se sustituye siempre en la otra ecuación. Siguiente: lección catorce, el método de igualación.",
        )
