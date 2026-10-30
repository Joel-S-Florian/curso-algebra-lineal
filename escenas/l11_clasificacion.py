"""Lección 11 — Clasificación de sistemas: ¿por qué 0, 1 o infinitas soluciones?

Escenas (un video cada una):
    ClasificacionDeSistemas, NuncaExactamenteDos

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l11_clasificacion.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ejes_iguales, sistema_con_llave  # noqa: E402
from curso.componentes import rectas_de_sistema as rectas  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def caja(texto: str, color=WHITE, ancho=None) -> VGroup:
    rotulo = Text(texto, font_size=TAM_NOTA + 2, color=color, line_spacing=1.1)
    marco = RoundedRectangle(
        corner_radius=0.15, width=ancho or rotulo.width + 0.5, height=rotulo.height + 0.4, stroke_color=color
    )
    return VGroup(marco, rotulo)


class ClasificacionDeSistemas(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 11 · Parte 1", "Clasificación de los sistemas")
        titulo = self.encabezado("Tres nombres para tres casos")

        raiz = caja("Sistema lineal").shift(UP * 2.5)
        compatible = caja("COMPATIBLE\n(tiene solución)", COLOR_SOLUCION).shift(LEFT * 2.8 + UP * 0.9)
        incompatible = caja("INCOMPATIBLE (SI)\nninguna solución", COLOR_ERROR).shift(RIGHT * 3.8 + UP * 0.9)
        determinado = caja("DETERMINADO (SCD)\nuna solución", COLOR_SOLUCION).shift(LEFT * 4.7 + DOWN * 1.0)
        indeterminado = caja("INDETERMINADO (SCI)\ninfinitas soluciones", COLOR_LIBRE).shift(RIGHT * 0.1 + DOWN * 1.0)

        def flecha(a, b, texto):
            f = Arrow(a.get_bottom(), b.get_top(), buff=0.1, stroke_width=3)
            return VGroup(f, Text(texto, font_size=TAM_NOTA - 4, color=COLOR_SECUNDARIO).next_to(f.get_center(), RIGHT, buff=0.15))

        self.decir("Clasifiquemos los sistemas lineales.")
        self.play(FadeIn(raiz))
        self.decir("Primera pregunta: ¿tiene al menos una solución? Si no la tiene, el sistema es incompatible.")
        self.play(GrowFromEdge(VGroup(flecha(raiz, compatible, "sí"), compatible), UP), GrowFromEdge(VGroup(flecha(raiz, incompatible, "no"), incompatible), UP))
        self.pie("Primera pregunta: ¿tiene al menos una solución?", espera=2)
        self.decir("Si la tiene, es compatible, y hay una segunda pregunta: ¿cuántas? Si tiene una sola, es compatible determinado. Si tiene infinitas, compatible indeterminado. Nunca hay un número finito de soluciones mayor que uno.")
        self.play(FadeIn(VGroup(flecha(compatible, determinado, "una"), determinado)), FadeIn(VGroup(flecha(compatible, indeterminado, "más de una"), indeterminado)))
        self.pie("Si la tiene, segunda pregunta: ¿cuántas? Una sola, o infinitas (nunca un número finito mayor que 1).", espera=4)

        ejemplos = VGroup(
            sistema_con_llave(("x + y", "=", "5"), ("x - y", "=", "1"), font_size=30, colores=False).next_to(determinado, DOWN, buff=0.3),
            sistema_con_llave(("x + y", "=", "5"), ("2x + 2y", "=", "10"), font_size=30, colores=False).next_to(indeterminado, DOWN, buff=0.3),
            sistema_con_llave(("x + y", "=", "5"), ("x + y", "=", "2"), font_size=30, colores=False).next_to(incompatible, DOWN, buff=1.0),
        )
        self.decir("Son los tres casos de rectas de la lección ocho: se cortan, coinciden, o son paralelas.")
        self.play(LaggedStart(*[FadeIn(e) for e in ejemplos], lag_ratio=0.5))
        self.pie("Los ejemplos de la Lección 8: rectas que se cortan, coincidentes y paralelas.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo se reconoce cada caso (por ahora)")
        bloque = VGroup(
            Tex(r"\textbf{SCD}: rectas o planos con un único punto común.", font_size=38, color=COLOR_SOLUCION),
            Tex(r"\textbf{SCI}: alguna ecuación es redundante; las soluciones llevan parámetros.", font_size=38, color=COLOR_LIBRE),
            Tex(r"\textbf{SI}: combinando ecuaciones se llega a una igualdad falsa ($5 = 2$).", font_size=38, color=COLOR_ERROR),
            Tex(r"Un sistema homogéneo nunca es SI (siempre tiene la solución trivial).", font_size=36),
            Tex(r"En la Unidad 7 clasificaremos sin resolver, con el \textbf{rango} (Teorema de Rouché-Frobenius).", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        self.decir("Por ahora los reconocemos combinando ecuaciones. Determinado: un único punto común. Indeterminado: alguna ecuación es redundante, y las soluciones llevan parámetros. Incompatible: combinando ecuaciones se llega a una igualdad falsa. Un sistema homogéneo nunca es incompatible. Y en la unidad siete aprenderemos a clasificar sin resolver, con el rango.")
        for b in bloque:
            self.play(FadeIn(b, shift=RIGHT * 0.2))
            self.wait(1.8)

        self.ejercicio_propuesto(
            "F03-N3-03",
            VGroup(
                Text("Clasifica cada sistema (SCD, SCI o SI) y justifícalo:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \begin{cases} x - y = 1 \\ 2x - 2y = 2 \end{cases} \quad"
                    r"\text{b) } \begin{cases} x + y = 1 \\ x + y = 0 \end{cases} \quad"
                    r"\text{c) } \begin{cases} x = 2 \\ y = -1 \end{cases} \quad"
                    r"\text{d) } \begin{cases} x + y + z = 0 \\ x - y = 0 \end{cases}",
                    font_size=40,
                ),
            ).arrange(DOWN, buff=0.5),
        )
        self.resumen(
            [
                "Compatible: tiene solución. Incompatible (SI): no tiene.",
                "Compatible determinado (SCD): una. Indeterminado (SCI): infinitas.",
                "Un homogéneo siempre es compatible.",
            ],
            "por qué no hay sistemas con exactamente dos soluciones.",
            voz="En resumen: un sistema es compatible si tiene solución, e incompatible si no tiene. Compatible determinado: una solución. Compatible indeterminado: infinitas. Y un sistema homogéneo siempre es compatible. Siguiente: por qué no hay sistemas con exactamente dos soluciones.",
        )


class NuncaExactamenteDos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 11 · Parte 2", "¿Por qué nunca exactamente dos soluciones?")
        titulo = self.encabezado("Si hay dos soluciones, hay infinitas")
        plano = ejes_iguales((-1, 6), (-1, 4), unidad=0.75).to_edge(LEFT, buff=0.7).shift(DOWN * 0.3)
        sistema = sistema_con_llave(("x + 2y", "=", "5"), ("2x + 4y", "=", "10"), font_size=40).to_edge(RIGHT, buff=1.2).shift(UP * 2)
        self.decir("Supongamos que un sistema lineal tiene dos soluciones distintas.")
        self.play(Create(plano), FadeIn(sistema))
        self.play(Create(rectas(plano, [(1, 2, 5), (2, 4, 10)], discontinuas=(1,))))
        p, q = np.array([1.0, 2.0]), np.array([3.0, 1.0])
        dp = Dot(plano.c2p(*p), color=COLOR_COEFICIENTE, radius=0.11)
        dq = Dot(plano.c2p(*q), color=COLOR_TERMINO_INDEP, radius=0.11)
        rp = MathTex("p = (1, 2)", font_size=34, color=COLOR_COEFICIENTE).next_to(dp, UP, buff=0.2)
        rq = MathTex("q = (3, 1)", font_size=34, color=COLOR_TERMINO_INDEP).next_to(dq, UP, buff=0.2)
        self.decir("Llamémoslas pe, el uno, dos, y cu, el tres, uno.")
        self.play(FadeIn(dp), FadeIn(dq), Write(rp), Write(rq))
        formula = MathTex(r"r(t) = (1 - t)\,p + t\,q", font_size=44, color=COLOR_PIVOTE).next_to(sistema, DOWN, buff=0.7)
        self.decir("Construimos erre de te: uno menos te, por pe, más te por cu.")
        self.play(Write(formula))
        t = ValueTracker(0.5)
        punto = always_redraw(lambda: Dot(plano.c2p(*((1 - t.get_value()) * p + t.get_value() * q)), color=COLOR_PIVOTE, radius=0.09))
        lectura = always_redraw(
            lambda: MathTex(
                rf"t = {t.get_value():.1f}:\ r = ({(1 - t.get_value()) * p[0] + t.get_value() * q[0]:.1f},\ "
                rf"{(1 - t.get_value()) * p[1] + t.get_value() * q[1]:.1f})".replace("-0.0", "0.0"),
                font_size=38,
                color=COLOR_PIVOTE,
            ).next_to(formula, DOWN, buff=0.5)
        )
        self.decir("Con te igual a cero es pe; con te igual a uno, es cu; y con cualquier otro te, otro punto de la recta que los une. Todos son soluciones.")
        self.play(FadeIn(punto), FadeIn(lectura))
        for valor in (0, 1, 2, -0.5, 1.5):
            self.play(t.animate.set_value(valor), run_time=1.5)
        self.pie("t = 0 da p, t = 1 da q, y cualquier otro t da otro punto de la misma recta: todos son soluciones.", espera=4)
        self.limpiar(titulo)

        # Demostración general.
        titulo = self.cambiar_encabezado(titulo, "Teorema y demostración")
        teorema = Tex(
            r"\textbf{Teorema.} Un sistema lineal tiene ninguna, una o infinitas soluciones.", font_size=40, color=COLOR_PIVOTE
        ).shift(UP * 2.4)
        self.decir("Teorema: si un sistema lineal tiene dos soluciones distintas, tiene infinitas.")
        self.play(FadeIn(teorema))
        prueba = VGroup(
            Tex(r"Sean $p \neq q$ dos soluciones. Para cada real $t$, sea $r = (1 - t)p + tq$ (componente a componente).", font_size=32),
            MathTex(r"\sum_{j} a_{ij} r_j = \sum_j a_{ij}\big((1 - t)p_j + t q_j\big) = (1 - t)\sum_j a_{ij} p_j + t \sum_j a_{ij} q_j", font_size=38),
            MathTex(r"= (1 - t)\,b_i + t\,b_i = b_i \qquad \text{para cada ecuación } i", font_size=38),
            Tex(r"Así que $r$ es solución para todo $t$. Si $t \neq s$, $r(t) - r(s) = (t - s)(q - p) \neq 0$: son distintas.", font_size=32),
            Tex(r"Hay tantas soluciones como números reales $t$: infinitas. \quad $\blacksquare$", font_size=34, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.35).next_to(teorema, DOWN, buff=0.5)
        self.decir("¿Por qué? Sustituimos erre en la ecuación i. Como las incógnitas aparecen de forma lineal, podemos sacar uno menos te y te fuera de las sumas. Queda uno menos te por be i, más te por be i: be i. Así que erre es solución para todo te. Además, valores distintos de te dan puntos distintos. Hay infinitas soluciones.")
        for linea in prueba:
            self.play(FadeIn(linea))
            self.wait(2.5)
        self.decir("El paso clave, sacar uno menos te y te fuera de la suma, solo funciona porque las incógnitas aparecen de forma lineal.")
        self.pie("El paso clave (sacar (1 − t) y t fuera de la suma) solo funciona porque las incógnitas aparecen de forma LINEAL.", espera=5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Sin linealidad, el argumento falla")
        contraste = VGroup(
            MathTex(r"x^2 = 1:\quad \text{soluciones } -1 \text{ y } 1 \text{ (exactamente dos)}", font_size=44),
            MathTex(r"\text{punto medio } 0:\quad 0^2 = 0 \neq 1", font_size=44, color=COLOR_ERROR),
            Tex(r"Para ecuaciones no lineales, dos soluciones no implican infinitas.", font_size=40),
        ).arrange(DOWN, buff=0.6)
        self.decir("Si la ecuación no es lineal, el argumento falla: equis al cuadrado igual a uno tiene exactamente dos soluciones, menos uno y uno, y su punto medio, cero, no es solución.")
        for c in contraste:
            self.play(FadeIn(c))
            self.wait(2)

        self.ejercicio_propuesto(
            "F03-N5-01",
            VGroup(
                Tex(r"a) Un sistema lineal tiene las soluciones $(1, 2)$ y $(3, -2)$. Da otras tres.", font_size=38),
                Tex(r"b) Demuestra que si $p$ y $q$ son soluciones de un sistema homogéneo, $p - q$ también lo es.", font_size=38),
                Tex(r"c) Muestra que el argumento falla para $x^2 + y^2 = 1$ con $(1, 0)$ y $(0, 1)$.", font_size=38),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35),
        )
        self.resumen(
            [
                "Un sistema lineal tiene 0, 1 o infinitas soluciones; nunca 2, 3, …",
                "Si p y q son soluciones, (1 − t)p + tq también, para todo t.",
                "La demostración usa la linealidad; con x² = 1 falla.",
            ],
            "Lección 12 — casos especiales y errores frecuentes.",
            voz="En resumen: un sistema lineal tiene cero, una o infinitas soluciones; nunca dos, ni tres. Si pe y cu son soluciones, uno menos te por pe, más te por cu, también lo es, para todo te. La demostración usa la linealidad; con equis al cuadrado igual a uno, falla. Siguiente: lección doce, casos especiales y errores frecuentes.",
        )
