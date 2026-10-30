"""Lección 51 — Elegir el método.

Escenas (un video cada una):
    ArbolDeDecisionDeMetodos, PreguntaYHerramienta

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l51_elegir_el_metodo.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def caja(texto: str, color=WHITE, ancho: float = 3.9, tam: int = 24, relleno: float = 0.12) -> VGroup:
    """Rectángulo redondeado con texto (líneas separadas por «\\n»)."""
    t = Text(texto, font_size=tam, line_spacing=1.0, color=color)
    marco = RoundedRectangle(corner_radius=0.15, width=max(ancho, t.width + 0.4), height=t.height + 0.4, color=color, stroke_width=3, fill_color=color, fill_opacity=relleno)
    t.move_to(marco)
    return VGroup(marco, t)


def flecha_entre(a: Mobject, b: Mobject, color=COLOR_SECUNDARIO) -> Arrow:
    return Arrow(a.get_bottom(), b.get_top(), buff=0.08, color=color, stroke_width=3, max_tip_length_to_length_ratio=0.15)


class ArbolDeDecisionDeMetodos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 51 · Parte 1", "Elegir el método")
        titulo = self.encabezado("Empieza por la pregunta, no por la matriz")
        raiz = caja("¿Qué quieres saber?", COLOR_PIVOTE, ancho=3.6, tam=28).move_to(UP * 2.4)
        a = caja("¿Cuántas soluciones\ntiene?", COLOR_COEFICIENTE).move_to(LEFT * 4.8 + UP * 0.8)
        b = caja("Quiero la solución", COLOR_SOLUCION).move_to(UP * 0.8)
        c = caja("Quiero describir\ntodas las soluciones", COLOR_OPERACION).move_to(RIGHT * 4.8 + UP * 0.8)
        ra = caja("Rouché-Frobenius\ncompara rg(A), rg[A|b] y n", COLOR_COEFICIENTE, ancho=3.9, tam=22).move_to(LEFT * 4.8 + DOWN * 1.2)
        b1 = caja("Un solo b", COLOR_SOLUCION, ancho=2.2, tam=22).move_to(LEFT * 1.4 + DOWN * 0.7)
        b2 = caja("Varios b,\nla misma A", COLOR_SOLUCION, ancho=2.2, tam=22).move_to(RIGHT * 1.4 + DOWN * 0.7)
        rb1 = caja("Gauss y\nsustitución\nhacia atrás", COLOR_SOLUCION, ancho=2.4, tam=21).move_to(LEFT * 1.4 + DOWN * 2.3)
        rb2 = caja("LU con\npivoteo\n(PA = LU)", COLOR_SOLUCION, ancho=2.4, tam=21).move_to(RIGHT * 1.4 + DOWN * 2.3)
        rc = caja("Gauss-Jordan\ny x = xp + ker A", COLOR_OPERACION, ancho=3.9, tam=22).move_to(RIGHT * 4.8 + DOWN * 1.2)
        self.decir("Elegir el método empieza por la pregunta, no por la matriz. Antes de operar, ¿qué quieres saber?")
        self.play(FadeIn(raiz))
        self.wait(1)

        self.decir("Si solo quieres saber cuántas soluciones tiene el sistema, no hace falta resolverlo: el teorema de Rouché-Frobenius lo decide comparando el rango de la matriz, el de la aumentada y el número de incógnitas.")
        self.play(FadeIn(a), GrowArrow(flecha_entre(raiz, a)))
        self.play(FadeIn(ra), GrowArrow(flecha_entre(a, ra)))
        self.wait(2)

        self.decir("Si quieres la solución, depende de cuántos lados derechos tengas. Con uno solo, Gauss con sustitución hacia atrás. Con varios lados derechos y la misma matriz, la factorización L U, con pivoteo si hace falta: se factoriza una vez y cada lado derecho cuesta poco.")
        self.play(FadeIn(b), GrowArrow(flecha_entre(raiz, b)))
        self.play(FadeIn(b1), FadeIn(b2), GrowArrow(flecha_entre(b, b1)), GrowArrow(flecha_entre(b, b2)))
        self.play(FadeIn(rb1), FadeIn(rb2), GrowArrow(flecha_entre(b1, rb1)), GrowArrow(flecha_entre(b2, rb2)))
        self.wait(2)

        self.decir("Y si quieres describir todas las soluciones, sobre todo cuando hay infinitas, Gauss-Jordan te da la forma reducida, de donde sale la solución general: una solución particular más el núcleo.")
        self.play(FadeIn(c), GrowArrow(flecha_entre(raiz, c)))
        self.play(FadeIn(rc), GrowArrow(flecha_entre(c, rc)))
        self.wait(2.5)

        self.pie("A mano, con 2 o 3 incógnitas: sustitución, igualación o reducción. Siempre: verificar en el sistema original.", espera=4)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Qué suele ir mal al elegir")
        errores = VGroup(
            parrafo(r"Resolver cuando solo se pedía \textbf{clasificar}: Rouché-Frobenius es más barato.", font_size=36, sangria=0.4),
            parrafo(r"Repetir Gauss para cada $\mathbf{b}$: con la misma $A$, factoriza una vez ($LU$).", font_size=36, sangria=0.4),
            parrafo(r"Gauss-Jordan a ciegas en sistemas grandes: cuesta más ($\approx n^3/2$ frente a $\approx n^3/3$).", font_size=36, sangria=0.4),
            parrafo(r"No verificar: sustituir en el sistema \textbf{original}, no en el ya transformado.", font_size=36, sangria=0.4, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(errores, margen=0.5)
        self.decir("Qué suele ir mal al elegir. Resolver cuando solo se pedía clasificar. Repetir Gauss para cada lado derecho en lugar de factorizar una vez. Usar Gauss-Jordan en sistemas grandes, que cuesta más. Y no verificar: hay que sustituir en el sistema original, no en el transformado.")
        for e in errores:
            self.play(FadeIn(e))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F04-N3-15",
            VGroup(
                Text("Para cada situación, di qué método usarías y por qué:", font_size=TAM_TEXTO),
                Text("a) ¿Cuántas soluciones tiene un sistema de 4 ecuaciones y 6 incógnitas?", font_size=TAM_NOTA + 2),
                Text("b) Una misma matriz 100×100 con 50 lados derechos distintos.", font_size=TAM_NOTA + 2),
                Text("c) Describir todas las soluciones de un sistema de 3×5.", font_size=TAM_NOTA + 2),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35),
            voz="Ejercicio propuesto: para cada situación, di qué método usarías y por qué. Pausa el video e inténtalo; en el banco hay ejercicios de verdadero o falso con justificación para practicar.",
        )
        self.resumen(
            [
                "Primero la pregunta: contar soluciones, resolver o describirlas.",
                "Contar: Rouché-Frobenius. Resolver: Gauss (un b) o LU (varios b).",
                "Describir: Gauss-Jordan y x = xp + núcleo. Siempre, verificar.",
            ],
            "las preguntas y sus herramientas, en una tabla.",
            voz="En resumen: primero la pregunta. Para contar soluciones, Rouché-Frobenius. Para resolver, Gauss con un lado derecho, o L U con varios. Para describirlas todas, Gauss-Jordan y la forma solución particular más núcleo. Y siempre, verificar. Siguiente: las preguntas y sus herramientas, en una tabla.",
        )


class PreguntaYHerramienta(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 51 · Parte 2", "Pregunta y herramienta")
        titulo = self.encabezado("Una pregunta, una herramienta")
        filas = [
            ("Si el sistema tiene solución", "rg(A) = rg[A | b]", "L39-L40"),
            ("Si la solución es única", "rg(A) = n (núcleo trivial)", "L40, L46"),
            ("Cuántos parámetros libres", "n − rg(A) = nul(A)", "L46"),
            ("Solución de un sistema (un b)", "Gauss + sustitución atrás", "L26"),
            ("Solución con varios b", "A = LU (PA = LU)", "L36-L38"),
            ("Solución general", "x = xp + núcleo", "L47"),
            ("Si b es alcanzable", "b en el espacio columna", "L48"),
            ("Cuántas ecuaciones no sobran", "rg(A)", "L39"),
        ]
        encabezados = ("Pregunta", "Herramienta", "Lección")
        tabla = VGroup(*[Text(h, font_size=TAM_NOTA, weight="BOLD", color=COLOR_SECUNDARIO) for h in encabezados])
        for fila in filas:
            for j, texto in enumerate(fila):
                tabla.add(Text(texto, font_size=TAM_NOTA, weight="BOLD" if j == 0 else "NORMAL", color=COLOR_PIVOTE if j == 1 else WHITE))
        tabla.arrange_in_grid(rows=len(filas) + 1, cols=3, buff=(0.6, 0.36), col_alignments="lll").next_to(titulo, DOWN, buff=0.45)
        ajustar_al_encuadre(tabla, margen=0.5)
        self.decir("Esta tabla pone cada pregunta junto a su herramienta. Si el sistema tiene solución: el rango de a igual al de la aumentada. Si es única: el rango igual al número de incógnitas, es decir, núcleo trivial. Cuántos parámetros libres: ene menos el rango, la nulidad.")
        self.play(FadeIn(tabla[:12]))
        self.decir("La solución de un sistema con un lado derecho: Gauss y sustitución hacia atrás. Con varios lados derechos: la factorización L U. La solución general: una solución particular más el núcleo. Si be es alcanzable: si está en el espacio columna. Y cuántas ecuaciones no sobran: el rango.")
        self.play(FadeIn(tabla[12:]))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Tres hábitos antes de dar por terminado")
        habitos = VGroup(
            parrafo(r"\textbf{1.} Comprueba en el sistema original: $A\mathbf{x} = \mathbf{b}$.", font_size=40, sangria=0.4),
            parrafo(r"\textbf{2.} Comprueba la coherencia de los rangos: $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.", font_size=40, sangria=0.4),
            parrafo(r"\textbf{3.} Escribe la respuesta como te la piden: punto, recta, plano o ``no hay solución''.", font_size=40, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(habitos, margen=0.5)
        self.decir("Tres hábitos antes de dar un problema por terminado. Uno: comprobar en el sistema original. Dos: comprobar que los rangos son coherentes, que el rango más la nulidad es ene. Y tres: escribir la respuesta como la piden, un punto, una recta, un plano, o que no hay solución.")
        for h in habitos:
            self.play(FadeIn(h))
            self.wait(2.8)
        self.wait(1)

        self.ejercicio_propuesto(
            "F15-N4-24",
            VGroup(
                Text("Verdadero o falso, justificando (más en F15-N4-24 y siguientes):", font_size=TAM_TEXTO),
                Text("«Si A x = b tiene solución única, A x = 0 solo tiene la solución trivial.»", font_size=TAM_NOTA + 2),
                Text("«Un sistema con más incógnitas que ecuaciones siempre tiene solución.»", font_size=TAM_NOTA + 2),
            ).arrange(DOWN, buff=0.45),
            voz="Ejercicio propuesto: decide si estas dos afirmaciones son verdaderas o falsas, y justifica. Pausa el video e inténtalo; en el banco tienes más ejercicios como este.",
        )
        self.resumen(
            [
                "Cada pregunta tiene su herramienta: rangos, Gauss, LU, núcleo, espacio columna.",
                "Tres hábitos: verificar, comprobar rangos, responder en la forma pedida.",
            ],
            "Lección 52 — problemas integradores.",
            voz="En resumen: cada pregunta tiene su herramienta, y hay tres hábitos al terminar: verificar, comprobar los rangos y responder en la forma pedida. Siguiente: lección cincuenta y dos, problemas integradores.",
        )
