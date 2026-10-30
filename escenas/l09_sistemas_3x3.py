"""Lección 9 — Sistemas de tres ecuaciones con tres incógnitas: tres planos.

Escenas (un video cada una):
    TresPlanosUnPunto, TresPlanosUnaRecta, TresPlanosSinPuntoComun

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l09_sistemas_3x3.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, plano_3d, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class EscenaPlanos(EscenaCurso, ThreeDScene):
    """Utilidades comunes a las escenas de tres planos."""

    def mostrar_sistema(self, *ecuaciones) -> VGroup:
        sistema = sistema_con_llave(*ecuaciones, font_size=38).to_corner(UL, buff=0.5).shift(DOWN * 0.7)
        self._fijar(sistema)
        self.play(FadeIn(sistema))
        return sistema

    def mostrar_planos(self, espacio, planos, ecuaciones_en_pantalla):
        """Dibuja los planos uno a uno, resaltando la ecuación correspondiente."""
        for plano, fila in zip(planos, ecuaciones_en_pantalla[1]):
            self.play(Create(plano), Indicate(fila, color=WHITE), run_time=1.5)
            self.wait(0.5)

    def girar(self, segundos=6):
        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(segundos)
        self.stop_ambient_camera_rotation()

    def volver_a_2d(self):
        self.limpiar()
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES, zoom=1)

    def recta_3d(self, espacio, p, q, color=COLOR_PIVOTE):
        return Line3D(espacio.c2p(*p), espacio.c2p(*q), color=color, thickness=0.03)


class TresPlanosUnPunto(EscenaPlanos):
    def construct(self):
        self.mostrar_portada("Lección 9 · Parte 1", "Tres planos que se cortan en un punto")
        titulo = self.encabezado("Cada ecuación con tres incógnitas es un plano")
        espacio, rotulos = self.espacio_3d(rango=(-1, 4), centro=(1.2, 2, 2.2), zoom=0.85)
        self.decir("Con tres incógnitas, cada ecuación es un plano. Este sistema tiene tres ecuaciones: tres planos en el espacio.")
        self.play(Create(espacio), FadeIn(rotulos))
        ecuaciones = self.mostrar_sistema(("x + y + z", "=", "6"), ("x - y + z", "=", "2"), ("x + y - z", "=", "0"))
        u, v = (0.8, 3.2), (1.8, 4.2)  # rangos de y, z alrededor de la solución
        planos = [
            plano_3d(espacio, 1, 1, 1, 6, u, v, COLORES_ECUACIONES[0]),
            plano_3d(espacio, 1, -1, 1, 2, u, v, COLORES_ECUACIONES[1]),
            plano_3d(espacio, 1, 1, -1, 0, u, v, COLORES_ECUACIONES[2]),
        ]
        self.decir("Dibujemos los dos primeros.")
        self.mostrar_planos(espacio, planos[:2], (ecuaciones[0], ecuaciones[1][:2]))
        # Restando la 2.ª de la 1.ª: 2y = 4, y = 2; y queda x + z = 4: la recta (4 - t, 2, t).
        recta = self.recta_3d(espacio, (2.8, 2, 1.2), (0.2, 2, 3.8), color=WHITE)
        self.decir("Dos planos que no son paralelos se cortan en una recta: la blanca.")
        self.play(Create(recta))
        self.pie("Dos planos no paralelos se cortan en una recta (blanca).", espera=2)
        self.decir("Ahora el tercer plano.")
        self.play(Create(planos[2]), Indicate(ecuaciones[1][2], color=WHITE), run_time=1.5)
        punto = Dot3D(espacio.c2p(1, 2, 3), color=COLOR_PIVOTE, radius=0.12)
        rotulo = MathTex("(1, 2, 3)", font_size=38, color=COLOR_PIVOTE).move_to(espacio.c2p(1, 2, 3) + OUT * 0.6 + RIGHT * 0.6)
        self.add_fixed_orientation_mobjects(rotulo)
        self.decir("El tercer plano atraviesa esa recta en un único punto: uno, dos, tres. Es la única solución del sistema.")
        self.play(FadeIn(punto, scale=3), FadeIn(rotulo))
        self.pie("El tercer plano corta esa recta en un único punto: la única solución del sistema.", espera=2)
        verificacion = MathTex(
            r"1 + 2 + 3 = 6\ \checkmark \\ 1 - 2 + 3 = 2\ \checkmark \\ 1 + 2 - 3 = 0\ \checkmark",
            font_size=36,
            color=COLOR_SOLUCION,
        ).to_corner(DR, buff=0.6).shift(UP * 0.6)
        self._fijar(verificacion)
        self.decir("Y la verificamos en las tres ecuaciones: uno más dos más tres, seis; uno menos dos más tres, dos; uno más dos menos tres, cero.")
        self.play(Write(verificacion))
        self.girar()
        self.volver_a_2d()

        titulo = self.encabezado("Límites del dibujo")
        ideas = VGroup(
            Text("En un dibujo 3D es difícil ver dónde se cortan exactamente los planos.", font_size=TAM_TEXTO),
            Text("El dibujo sugiere cuántas soluciones hay; las cuentas (Lecciones 13 a 15)", font_size=TAM_TEXTO),
            Text("dan la solución exacta, y la verificación la confirma.", font_size=TAM_TEXTO),
        ).arrange(DOWN, buff=0.4)
        self._fijar(ideas)
        self.decir("Girando la cámara se entiende mejor, pero leer coordenadas exactas en un dibujo tridimensional es casi imposible. El dibujo sugiere cuántas soluciones hay; para la solución exacta están los métodos algebraicos, de las lecciones trece a quince.")
        for i in ideas:
            self.play(FadeIn(i))
            self.wait(1.5)

        self.ejercicio_propuesto(
            "F03-N1-02",
            VGroup(
                Tex(r"Comprueba que $(2, -1, 3)$ es solución del sistema y que $(1, 0, 3)$ no lo es.", font_size=40),
                sistema_con_llave(("x + y + z", "=", "4"), ("2x - y + z", "=", "8"), ("x + 3y - z", "=", "-4"), font_size=42),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Un sistema 3×3: tres planos en el espacio.",
                "Dos planos no paralelos se cortan en una recta; el tercero puede cortarla en un punto.",
                "Ese punto es la única solución: hay que verificarla en las tres ecuaciones.",
            ],
            "tres planos que comparten una recta.",
            voz="En resumen: un sistema de tres ecuaciones con tres incógnitas son tres planos en el espacio. Dos planos no paralelos se cortan en una recta, y el tercero puede cortarla en un punto. Ese punto es la única solución, y hay que verificarla en las tres ecuaciones. Siguiente: tres planos que comparten una recta.",
        )


class TresPlanosUnaRecta(EscenaPlanos):
    def construct(self):
        self.mostrar_portada("Lección 9 · Parte 2", "Tres planos que comparten una recta")
        titulo = self.encabezado("Como las páginas de un libro abierto")
        espacio, rotulos = self.espacio_3d(rango=(-1, 4), centro=(1, 1, 1.2), zoom=0.85)
        self.decir("Ahora, un sistema distinto.")
        self.play(Create(espacio), FadeIn(rotulos))
        ecuaciones = self.mostrar_sistema(("x + y + z", "=", "3"), ("x - y + z", "=", "1"), ("x + z", "=", "2"))
        u, v = (-0.3, 2.3), (-0.3, 2.3)
        planos = [
            plano_3d(espacio, 1, 1, 1, 3, u, v, COLORES_ECUACIONES[0]),
            plano_3d(espacio, 1, -1, 1, 1, u, v, COLORES_ECUACIONES[1]),
            plano_3d(espacio, 1, 0, 1, 2, u, v, COLORES_ECUACIONES[2]),
        ]
        self.decir("Dibujamos los tres planos.")
        self.mostrar_planos(espacio, planos, ecuaciones)
        recta = self.recta_3d(espacio, (2.3, 1, -0.3), (-0.3, 1, 2.3))
        self.decir("Los tres comparten la misma recta, como las páginas de un libro abierto.")
        self.play(Create(recta))
        parametrizacion = MathTex(r"(x, y, z) = (2 - t,\ 1,\ t)", font_size=40, color=COLOR_PIVOTE).to_corner(DR, buff=0.6).shift(UP * 0.8)
        self._fijar(parametrizacion)
        self.decir("Todos los puntos de la recta son solución: dos menos te, uno, te. Infinitas soluciones, con un parámetro.")
        self.play(Write(parametrizacion))
        self.pie("Los tres planos pasan por la misma recta: infinitas soluciones, con un parámetro.", espera=2)
        self.girar()
        self.volver_a_2d()

        titulo = self.encabezado("¿Por qué? La 3.ª ecuación no aporta nada nuevo")
        bloque = VGroup(
            MathTex(r"(x + y + z) + (x - y + z) = 3 + 1", font_size=44),
            MathTex(r"2x + 2z = 4 \;\Leftrightarrow\; x + z = 2", font_size=44),
            Tex(r"La tercera ecuación se deduce de las otras dos: es \textbf{redundante}.", font_size=40, color=COLOR_PIVOTE),
            Tex(r"Quedan en realidad dos ecuaciones \emph{independientes} con tres incógnitas: una recta.", font_size=38),
        ).arrange(DOWN, buff=0.5)
        self._fijar(bloque)
        self.decir("¿Por qué? Sumando las dos primeras ecuaciones, obtenemos dos equis más dos zeta igual a cuatro; dividiendo entre dos, equis más zeta igual a dos: la tercera. La tercera no aporta información nueva: es redundante. Quedan en realidad dos ecuaciones independientes con tres incógnitas: una recta.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.limpiar(titulo)
        titulo = self.cambiar_encabezado(titulo, "Otras formas de tener infinitas soluciones")
        casos = VGroup(
            Text("•  Dos planos iguales y un tercero que los corta: una recta.", font_size=TAM_TEXTO),
            Text("•  Los tres planos iguales: todo un plano de soluciones (dos parámetros).", font_size=TAM_TEXTO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self._fijar(casos)
        self.decir("Hay otras formas de tener infinitas soluciones: dos planos iguales y un tercero que los corta dan una recta; y si los tres planos son iguales, las soluciones forman todo un plano, con dos parámetros.")
        for c in casos:
            self.play(FadeIn(c))
            self.wait(2)

        self.ejercicio_propuesto(
            "F03-N2-03",
            VGroup(
                Tex(r"Comprueba que todos los puntos $(1 + t,\ 2 - t,\ t)$ son solución del sistema.", font_size=40),
                sistema_con_llave(("x + y", "=", "3"), ("y + z", "=", "2"), ("x - z", "=", "1"), font_size=42),
                Tex(r"¿Qué ecuación es combinación de las otras dos?", font_size=40),
            ).arrange(DOWN, buff=0.45),
        )
        self.resumen(
            [
                "Tres planos pueden compartir una recta: infinitas soluciones (un parámetro).",
                "Ocurre cuando una ecuación se obtiene combinando las otras.",
                "Si los tres planos son el mismo, las soluciones forman un plano.",
            ],
            "tres planos sin ningún punto común.",
        )


class TresPlanosSinPuntoComun(EscenaPlanos):
    def construct(self):
        self.mostrar_portada("Lección 9 · Parte 3", "Tres planos sin ningún punto común")
        titulo = self.encabezado("Sin solución… sin planos paralelos")
        espacio, rotulos = self.espacio_3d(rango=(-1, 4), centro=(1.5, 1, 1.5), zoom=0.8)
        self.decir("Un último sistema: en la tercera ecuación, equis más zeta vale ahora tres.")
        self.play(Create(espacio), FadeIn(rotulos))
        ecuaciones = self.mostrar_sistema(("x + y + z", "=", "3"), ("x - y + z", "=", "1"), ("x + z", "=", "3"))
        u, v = (-0.6, 2.6), (-0.2, 3.2)
        planos = [
            plano_3d(espacio, 1, 1, 1, 3, u, v, COLORES_ECUACIONES[0]),
            plano_3d(espacio, 1, -1, 1, 1, u, v, COLORES_ECUACIONES[1]),
            plano_3d(espacio, 1, 0, 1, 3, u, v, COLORES_ECUACIONES[2]),
        ]
        self.decir("Dibujamos los tres planos. Ninguno es paralelo a otro.")
        self.mostrar_planos(espacio, planos, ecuaciones)
        # Cortes dos a dos: y = 1, x + z = 2;  y = 0, x + z = 3;  y = 2, x + z = 3.
        rectas = VGroup(
            self.recta_3d(espacio, (2.2, 1, -0.2), (-0.2, 1, 2.2), color=WHITE),
            self.recta_3d(espacio, (3.2, 0, -0.2), (-0.2, 0, 3.2), color=WHITE),
            self.recta_3d(espacio, (3.2, 2, -0.2), (-0.2, 2, 3.2), color=WHITE),
        )
        self.decir("Se cortan de dos en dos, pero las tres rectas de corte son paralelas: forman un prisma, y no hay ningún punto común a los tres.")
        self.play(LaggedStart(*[Create(r) for r in rectas], lag_ratio=0.5))
        self.pie("Cada pareja de planos se corta en una recta, pero las tres rectas son paralelas: forman un «prisma».", espera=2)
        self.girar(7)
        self.volver_a_2d()

        titulo = self.encabezado("La contradicción, en las cuentas")
        bloque = VGroup(
            MathTex(r"(x + y + z) + (x - y + z) = 3 + 1 \;\Rightarrow\; x + z = 2", font_size=42),
            MathTex(r"\text{pero la tercera dice } x + z = 3", font_size=42),
            MathTex(r"\Rightarrow\ 2 = 3", font_size=50, color=COLOR_ERROR),
            Tex(r"Ningún punto cumple las tres: el sistema no tiene solución.", font_size=40, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.5)
        self._fijar(bloque)
        self.decir("Las cuentas lo confirman: sumando las dos primeras, se deduce que equis más zeta es dos. Pero la tercera exige que sea tres. Dos igual a tres: contradicción. Ningún punto cumple las tres ecuaciones.")
        for b in bloque:
            self.play(FadeIn(b))
            self.wait(2)
        self.limpiar(titulo)
        titulo = self.cambiar_encabezado(titulo, "Formas de no tener solución con tres planos")
        casos = VGroup(
            Text("•  «Prisma»: se cortan dos a dos en rectas paralelas (este ejemplo).", font_size=TAM_TEXTO),
            Text("•  Dos planos paralelos y un tercero que los corta.", font_size=TAM_TEXTO),
            Text("•  Tres planos paralelos (o dos iguales y uno paralelo).", font_size=TAM_TEXTO),
            Text("Moraleja: en 3D, no tener solución NO exige planos paralelos.", font_size=TAM_TEXTO, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        self._fijar(casos)
        self.decir("Con tres planos hay varias formas de no tener solución: el prisma de este ejemplo; dos planos paralelos y un tercero que los corta; o tres planos paralelos. Moraleja: en el espacio, no tener solución no exige que haya planos paralelos.")
        for c in casos:
            self.play(FadeIn(c))
            self.wait(1.8)

        self.ejercicio_propuesto(
            "F03-N4-01",
            VGroup(
                Tex(r"Demuestra, sumando ecuaciones, que este sistema no tiene solución.", font_size=40),
                sistema_con_llave(("x + 2y - z", "=", "1"), ("2x - y + z", "=", "3"), ("3x + y", "=", "5"), font_size=42),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Tres planos pueden no tener ningún punto común aunque ninguno sea paralelo a otro.",
                "Las cuentas lo delatan: combinando ecuaciones se llega a algo falso (2 = 3).",
                "En 3D: una solución, infinitas (recta o plano) o ninguna.",
            ],
            "Lección 10 — sistemas de m ecuaciones con n incógnitas.",
            voz="En resumen: tres planos pueden no tener ningún punto común aunque ninguno sea paralelo a otro. Las cuentas lo delatan: combinando ecuaciones se llega a algo falso, como dos igual a tres. En el espacio puede haber una solución, infinitas, en una recta o un plano, o ninguna. Siguiente: lección diez, sistemas de eme ecuaciones con ene incógnitas.",
        )
