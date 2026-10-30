"""Lección 14 — El método de igualación.

Escenas (un video cada una):
    IgualacionPasoAPaso, IgualacionInterpretacion

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l14_igualacion.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import (  # noqa: E402
    EscenaCurso,
    ejes_iguales,
    num,
    paso_numerado,
    recta_recortada,
    sistema_con_llave,
)
from curso.estilo import *  # noqa: E402,F403


class IgualacionPasoAPaso(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 14 · Parte 1", "El método de igualación")
        titulo = self.encabezado("Despejar la MISMA incógnita en las dos ecuaciones")
        sistema = sistema_con_llave(("2x - y", "=", "1"), ("x + 3y", "=", "11"), font_size=46)
        sistema.to_corner(UL, buff=0.8).shift(DOWN * 0.8)
        self.decir("Dos equis menos ye igual a uno, y equis más tres ye igual a once. En el método de igualación, despejamos la misma incógnita en las dos ecuaciones.")
        self.play(Write(sistema))
        despejes = VGroup(
            paso_numerado(1, "y", "=", "2x - 1"),
            paso_numerado(1, "y", "=", r"\frac{11 - x}{3}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(sistema, RIGHT, buff=1.5)
        despejes[0][1][2].set_color(COLORES_ECUACIONES[0])
        despejes[1][1][2].set_color(COLORES_ECUACIONES[1])
        self.decir("Primero, despejamos ye en cada ecuación: ye es dos equis menos uno, y ye es once menos equis, entre tres.")
        self.pie("1. Despejamos y en cada ecuación.")
        for fila, ecuacion in zip(despejes, sistema[1]):
            self.play(Indicate(ecuacion), FadeIn(fila[0]), TransformFromCopy(ecuacion, fila[1]))
            self.wait(1)
        self.wait(1)

        self.decir("Segundo: si ye es igual a las dos expresiones, las dos expresiones son iguales entre sí.")
        self.pie("2. Si y es igual a las dos expresiones, las dos expresiones son iguales entre sí.")
        igualdad = paso_numerado(2, "2x - 1", "=", r"\frac{11 - x}{3}")
        igualdad.next_to(sistema, DOWN, buff=0.6, aligned_edge=LEFT)
        igualdad[1][0].set_color(COLORES_ECUACIONES[0])
        igualdad[1][2].set_color(COLORES_ECUACIONES[1])
        self.play(
            FadeIn(igualdad[0]),
            TransformFromCopy(despejes[0][1][2], igualdad[1][0]),
            TransformFromCopy(despejes[1][1][2], igualdad[1][2]),
            FadeIn(igualdad[1][1]),
            run_time=1.5,
        )
        self.wait(1.5)
        self.decir("Tercero: ya tenemos una ecuación con una sola incógnita. La resolvemos: equis vale dos. Con cualquiera de los despejes, ye vale tres; los dos deben coincidir, y eso sirve de control. Y verificamos.")
        self.pie("3. Una ecuación con una sola incógnita.")
        resto = VGroup(
            paso_numerado(3, r"6x - 3 = 11 - x \;\Rightarrow\; 7x = 14 \;\Rightarrow\; x = 2"),
            paso_numerado(4, r"y = 2\cdot 2 - 1 = 3 \qquad \left(\text{y también } \tfrac{11 - 2}{3} = 3\right)"),
            paso_numerado(5, r"2\cdot 2 - 3 = 1\ \checkmark \qquad 2 + 3\cdot 3 = 11\ \checkmark"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(igualdad, DOWN, buff=0.35, aligned_edge=LEFT)
        notas = [None, "4. Volvemos a cualquiera de los despejes (los dos deben dar lo mismo).", "5. Verificamos en las ecuaciones originales."]
        for fila, nota in zip(resto, notas):
            if nota:
                self.pie(nota)
            self.play(FadeIn(fila[0]), Write(fila[1]))
            self.wait(2)
        solucion = MathTex(r"(x, y) = (2, 3)", font_size=46, color=COLOR_SOLUCION).next_to(despejes, DOWN, buff=0.8)
        self.decir("La solución es dos, tres.")
        self.play(Write(solucion), Create(SurroundingRectangle(solucion, color=COLOR_SOLUCION, buff=0.2)))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Por qué es válido?")
        bloque = VGroup(
            MathTex(r"y = A \ \text{ y } \ y = B \quad\Longrightarrow\quad A = B", font_size=50),
            Tex(r"Dos cantidades iguales a una tercera son iguales entre sí.", font_size=38),
            MathTex(r"A = B \ \text{ y } \ y = A \quad\Longrightarrow\quad y = B", font_size=50),
            Tex(r"Y al revés: con $A = B$ y uno de los despejes se recupera el otro.", font_size=38),
            Tex(r"Por eso $\{y = A,\ y = B\} \Longleftrightarrow \{y = A,\ A = B\}$: mismas soluciones.", font_size=40, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.45)
        self.decir("¿Por qué es válido? Dos cantidades iguales a una tercera son iguales entre sí. Y al revés: con la igualdad y uno de los despejes, recuperamos el otro. Así que el sistema no cambia de soluciones.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.decir("La igualación es una sustitución disfrazada: sustituimos ye igual a a en la ecuación ye igual a be.")
        self.pie("Igualación es una sustitución disfrazada: sustituimos y = A en la ecuación y = B.", espera=4)

        self.ejercicio_propuesto(
            "F04-N2-02",
            VGroup(
                Text("Resuelve por igualación (despeja x en ambas) y verifica:", font_size=TAM_TEXTO),
                sistema_con_llave(("x + 2y", "=", "7"), ("3x - y", "=", "7"), font_size=48, colores=False),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Despejar la misma incógnita en ambas ecuaciones.",
                "Igualar las dos expresiones: queda una ecuación con una incógnita.",
                "Resolver, volver a un despeje y verificar.",
                "Es válido porque dos cantidades iguales a una tercera son iguales entre sí.",
            ],
            "qué significa igualar en el dibujo.",
            voz="En resumen: en el método de igualación, despejamos la misma incógnita en las dos ecuaciones e igualamos las expresiones. Queda una ecuación con una incógnita. Los dos despejes deben dar el mismo valor, y eso sirve de control. Siguiente: igualar es buscar la misma altura.",
        )


class IgualacionInterpretacion(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 14 · Parte 2", "Igualar es buscar la misma altura")
        titulo = self.encabezado("Dos alturas que se igualan")
        plano = ejes_iguales((-1, 5), (-2, 5), unidad=0.72).to_edge(LEFT, buff=0.8).shift(DOWN * 0.3)
        r1 = recta_recortada(plano, 2, -1, color=COLORES_ECUACIONES[0], stroke_width=5)
        r2 = recta_recortada(plano, -1 / 3, 11 / 3, color=COLORES_ECUACIONES[1], stroke_width=5)
        leyenda = VGroup(
            MathTex(r"y = 2x - 1", font_size=40, color=COLORES_ECUACIONES[0]),
            MathTex(r"y = \tfrac{11 - x}{3}", font_size=40, color=COLORES_ECUACIONES[1]),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT, buff=1.4).shift(UP * 2)
        self.decir("Cada despeje es una recta: ye igual a dos equis menos uno, y ye igual a once menos equis, entre tres.")
        self.play(Create(plano), Create(r1), Create(r2), FadeIn(leyenda))

        x = ValueTracker(0)

        def alturas():
            xv = x.get_value()
            h1, h2 = 2 * xv - 1, (11 - xv) / 3
            return VGroup(
                DashedLine(plano.c2p(xv, -2), plano.c2p(xv, 5), color=COLOR_SECUNDARIO),
                Dot(plano.c2p(xv, h1), color=COLORES_ECUACIONES[0], radius=0.09),
                Dot(plano.c2p(xv, h2), color=COLORES_ECUACIONES[1], radius=0.09),
                Line(plano.c2p(xv, h1), plano.c2p(xv, h2), color=COLOR_ERROR, stroke_width=6),
            )

        def lectura():
            xv = x.get_value()
            diferencia = (2 * xv - 1) - (11 - xv) / 3
            color = COLOR_SOLUCION if abs(diferencia) < 0.02 else COLOR_ERROR
            return VGroup(
                MathTex(rf"x = {num(xv, 2)}", font_size=40),
                MathTex(r"\text{diferencia} = " + num(diferencia, 2), font_size=38, color=color),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(leyenda, DOWN, buff=0.8).to_edge(RIGHT, buff=0.8)

        marcas, panel = always_redraw(alturas), always_redraw(lectura)
        self.decir("Para cada equis, cada recta tiene una altura. Igualar es buscar el equis donde la diferencia de alturas es cero.")
        self.play(FadeIn(marcas), FadeIn(panel))
        self.pie("Para cada x, cada despeje da una altura. Igualar = buscar el x donde las dos alturas coinciden.", espera=2)
        for valor in (4, 0.8, 2):
            self.play(x.animate.set_value(valor), run_time=2.5)
            self.wait(0.5)
        self.decir("En equis igual a dos, la diferencia es cero: las rectas se cortan en dos, tres.")
        self.play(Flash(Dot(plano.c2p(2, 3)), color=COLOR_SOLUCION))
        self.pie("En x = 2 la diferencia es 0: las rectas se cortan en (2, 3).", espera=3)
        self.limpiar(titulo)

        # Cuándo conviene: ya despejado. Ejemplo de dos tarifas.
        titulo = self.cambiar_encabezado(titulo, "Cuándo conviene: las incógnitas ya vienen despejadas")
        enunciado = Text(
            "Taxi A: 3 € de bajada + 2 € por km.   Taxi B: 7 € de bajada + 1 € por km.",
            font_size=TAM_NOTA + 2,
        ).next_to(titulo, DOWN, buff=0.4)
        self.decir("La igualación es natural cuando las incógnitas ya vienen despejadas.")
        self.play(FadeIn(enunciado))
        # Escalas distintas en cada eje (km y €): aquí no importa deformar las pendientes.
        plano = Axes(
            x_range=[0, 8, 1], y_range=[0, 18, 3], x_length=5, y_length=4.4,
            axis_config={"include_numbers": True, "font_size": 24},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.8)
        etiquetas = VGroup(
            Text("km", font_size=TAM_NOTA - 4).next_to(plano.x_axis, RIGHT, buff=0.15),
            Text("€", font_size=TAM_NOTA - 4).next_to(plano.y_axis, UP, buff=0.1),
        )
        a = plano.plot(lambda k: 3 + 2 * k, x_range=[0, 7.5], color=COLORES_ECUACIONES[0])
        b = plano.plot(lambda k: 7 + k, x_range=[0, 8], color=COLORES_ECUACIONES[1])
        self.decir("Taxi a: tres euros de bajada más dos por kilómetro. Taxi be: siete euros de bajada más uno por kilómetro.")
        self.play(Create(plano), FadeIn(etiquetas), Create(a), Create(b))
        cuentas = VGroup(
            MathTex(r"y = 3 + 2x,\quad y = 7 + x", font_size=36),
            MathTex(r"3 + 2x = 7 + x \;\Rightarrow\; x = 4,\ y = 11", font_size=36, color=COLOR_SOLUCION),
            Tex(r"Hasta 4 km es más barato A;\\ desde 4 km, B.", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        self.decir("Igualamos: tres más dos equis igual a siete más equis. Equis vale cuatro, y ye, once.")
        for c in cuentas[:2]:
            self.play(Write(c))
            self.wait(1.5)
        self.decir("Los dos taxis cuestan lo mismo, once euros, a los cuatro kilómetros. Hasta cuatro kilómetros es más barato el a; desde ahí, el be.")
        self.play(FadeIn(Dot(plano.c2p(4, 11), color=COLOR_PIVOTE, radius=0.1), scale=2), FadeIn(cuentas[2]))
        self.wait(4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Casos especiales y limitaciones")
        bloque = VGroup(
            MathTex(r"y = 2x - 1,\ \ y = 2x + 3:\quad 2x - 1 = 2x + 3 \;\Rightarrow\; -1 = 3", font_size=40, color=COLOR_ERROR),
            Tex(r"Misma pendiente, distinta altura: paralelas, \textbf{SI}.", font_size=36, color=COLOR_ERROR),
            MathTex(r"y = 2x - 1,\ \ y = \tfrac{4x - 2}{2}:\quad 2x - 1 = 2x - 1 \;\Rightarrow\; 0 = 0", font_size=40, color=COLOR_LIBRE),
            Tex(r"La misma recta: \textbf{SCI}.", font_size=36, color=COLOR_LIBRE),
            Tex(r"Limitación: con tres o más incógnitas habría que despejar e igualar muchas veces.", font_size=36),
        ).arrange(DOWN, buff=0.35)
        self.decir("Si al igualar sale algo falso, como menos uno igual a tres, las rectas son paralelas: no hay solución. Si sale cero igual a cero, son la misma recta: infinitas soluciones. Y una limitación: con tres o más incógnitas habría que despejar e igualar muchas veces.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(1.8)

        self.ejercicio_propuesto(
            "F04-N3-02",
            VGroup(
                Text("Plan A: 10 € al mes + 2 € por GB.   Plan B: 4 € al mes + 3 € por GB.", font_size=TAM_TEXTO),
                Text("¿Con cuántos GB cuestan lo mismo? ¿Cuál conviene si usas 8 GB?", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Igualar = buscar el x donde las dos rectas tienen la misma altura.",
                "Conviene cuando la misma incógnita ya está despejada en ambas ecuaciones.",
                "−1 = 3 indica SI; 0 = 0, SCI.",
                "No escala bien a más incógnitas.",
            ],
            "Lección 15 — el método de reducción.",
            voz="En resumen: igualar es buscar el punto donde las dos rectas tienen la misma altura. Es natural cuando las incógnitas ya vienen despejadas. Si sale una igualdad falsa, el sistema no tiene solución; si sale cero igual a cero, tiene infinitas. Siguiente: lección quince, el método de reducción.",
        )
