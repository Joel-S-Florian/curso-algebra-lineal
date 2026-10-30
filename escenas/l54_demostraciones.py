"""Lección 54 — Las demostraciones clave del curso.

Escenas (un video cada una):
    NoHayExactamenteDosSoluciones, OperacionesConservanSoluciones, DemostracionesClave

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l54_demostraciones.py -a
"""

import sys
import textwrap
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, ejes_iguales, flecha, panel_derecha, parrafo, recta_general  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class NoHayExactamenteDosSoluciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 54 · Parte 1", "Dos soluciones, infinitas soluciones")
        titulo = self.encabezado("Un sistema lineal tiene 0, 1 o infinitas soluciones")
        p = ejes_iguales((-2, 6), (-2, 4), unidad=0.72).to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)
        recta = recta_general(p, 1, 2, 3, color=COLOR_SECUNDARIO, stroke_width=3)
        x = Dot(p.c2p(3, 0), color=COLOR_COEFICIENTE, radius=0.1)
        y = Dot(p.c2p(1, 1), color=COLOR_TERMINO_INDEP, radius=0.1)
        rx = MathTex(r"\mathbf{x}", font_size=38, color=COLOR_COEFICIENTE).next_to(x, DOWN, buff=0.15)
        ry = MathTex(r"\mathbf{y}", font_size=38, color=COLOR_TERMINO_INDEP).next_to(y, UP, buff=0.15)
        texto = VGroup(
            Tex(r"Supón dos soluciones distintas:", font_size=36),
            MathTex(r"A\mathbf{x} = \mathbf{b},\qquad A\mathbf{y} = \mathbf{b},\qquad \mathbf{x} \ne \mathbf{y}", font_size=40),
            Tex(r"Para cada $t \in \mathbb{R}$ sea", font_size=36),
            MathTex(r"\mathbf{z}_t = \mathbf{x} + t(\mathbf{y} - \mathbf{x})", font_size=44, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(RIGHT, buff=0.5).shift(UP * 0.4)
        panel_derecha(texto, ancho=6.2)
        self.decir("Vamos a demostrar que un sistema lineal solo puede tener cero, una o infinitas soluciones; en particular, nunca exactamente dos. Supongamos dos soluciones distintas, equis e i griega, de a por equis igual a be.")
        self.play(Create(p), Create(recta), FadeIn(x), FadeIn(y), FadeIn(rx), FadeIn(ry))
        self.play(FadeIn(texto[:2]))
        self.decir("Para cada número te, consideramos el vector zeta te, igual a equis más te por la diferencia i griega menos equis. Cuando te recorre los números reales, zeta te recorre toda la recta que pasa por los dos puntos.")
        self.play(FadeIn(texto[2:]))
        puntos = VGroup(*[Dot(p.c2p(3 - 2 * t, t), color=COLOR_PIVOTE, radius=0.07) for t in (-1, -0.5, 0.5, 1.5, 2)])
        self.play(LaggedStart(*[FadeIn(q, scale=2) for q in puntos], lag_ratio=0.25))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cada zeta te es solución")
        cuenta = VGroup(
            MathTex(r"A\mathbf{z}_t = A\mathbf{x} + t\,(A\mathbf{y} - A\mathbf{x})", font_size=48),
            MathTex(r"= \mathbf{b} + t\,(\mathbf{b} - \mathbf{b}) = \mathbf{b}", font_size=48, color=COLOR_SOLUCION),
            Tex(r"Como $\mathbf{y} - \mathbf{x} \ne \mathbf{0}$, los vectores $\mathbf{z}_t$ son todos distintos entre sí.", font_size=38),
            Tex(r"Hay infinitas soluciones. $\qquad\blacksquare$", font_size=42, color=COLOR_PIVOTE),
            Tex(r"En consecuencia: $0$, $1$ o infinitas; nunca exactamente $2$ (ni $3$, ni $17$).", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(cuenta, margen=0.5)
        self.decir("Y cada zeta te es solución. Por linealidad, a por zeta te es a por equis, más te por a por i griega menos a por equis. Como las dos son soluciones, queda be más te por be menos be, que es be. Como la diferencia no es nula, los zeta te son todos distintos: hay infinitas soluciones. Por tanto, un sistema lineal tiene cero, una o infinitas soluciones, nunca exactamente dos.")
        for c in cuenta:
            self.play(FadeIn(c))
            self.wait(2.4)
        self.wait(1)

        self.ejercicio_propuesto(
            "F16-N3-11",
            Text("Demuestra que un sistema lineal con dos soluciones distintas\ntiene infinitas (ejercicio F16-N3-11 del banco).", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: escribe tú la demostración de que un sistema con dos soluciones distintas tiene infinitas. Pausa el video e inténtalo; la demostración está en el solucionario.",
        )
        self.resumen(
            [
                "Dos soluciones distintas generan toda una recta de soluciones.",
                "Por tanto: 0, 1 o infinitas. Nunca exactamente 2.",
                "Se usa solo la linealidad: A(x + t(y − x)) = b.",
            ],
            "por qué las operaciones elementales no cambian las soluciones.",
            voz="En resumen: dos soluciones distintas generan toda una recta de soluciones; por tanto hay cero, una o infinitas, nunca exactamente dos. Y la demostración solo usa la linealidad. Siguiente: por qué las operaciones elementales no cambian las soluciones.",
        )


class OperacionesConservanSoluciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 54 · Parte 2", "Las operaciones no cambian las soluciones")
        titulo = self.encabezado("Un ejemplo antes de la demostración")
        s0 = MathTex(r"\begin{cases} x + y = 3 \\ x - y = 1 \end{cases}", font_size=46)
        s1 = MathTex(r"\begin{cases} x + y = 3 \\ -2y = -2 \end{cases}", font_size=46)
        s2 = MathTex(r"\begin{cases} x + y = 3 \\ y = 1 \end{cases}", font_size=46)
        etiquetas = [MathTex(r"R_2 \leftarrow R_2 - R_1", font_size=34, color=COLOR_OPERACION), MathTex(r"R_2 \leftarrow -\tfrac12 R_2", font_size=34, color=COLOR_OPERACION)]
        fila = VGroup(s0, etiquetas[0], s1, etiquetas[1], s2).arrange(RIGHT, buff=0.45).next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(fila, margen=0.5)
        comp = VGroup(*[MathTex(r"(2, 1)\ \checkmark", font_size=40, color=COLOR_SOLUCION).next_to(s, DOWN, buff=0.5) for s in (s0, s1, s2)])
        self.decir("Primero un ejemplo. Este sistema tiene la solución equis igual a dos, y igual a uno. Restamos a la segunda ecuación la primera, y queda menos dos y igual a menos dos. Multiplicamos por menos un medio, y queda y igual a uno. En los tres sistemas, el punto dos, uno es solución.")
        self.play(FadeIn(s0), FadeIn(comp[0]))
        self.play(FadeIn(etiquetas[0]), FadeIn(s1), FadeIn(comp[1]))
        self.play(FadeIn(etiquetas[1]), FadeIn(s2), FadeIn(comp[2]))
        self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Las tres operaciones")
        ops = VGroup(
            parrafo(r"\textbf{Intercambiar} $E_i \leftrightarrow E_j$: es la misma lista de ecuaciones, en otro orden.", font_size=36, sangria=0.4),
            parrafo(r"\textbf{Multiplicar} $E_i$ por $c \ne 0$: se cumple $E_i$ $\iff$ se cumple $cE_i$ (se divide por $c$ para volver).", font_size=36, sangria=0.4),
            parrafo(r"\textbf{Sumar} $cE_j$ a $E_i$: si se cumplen $E_i$ y $E_j$, se cumple $E_i + cE_j$; y al revés, restando $cE_j$.", font_size=36, sangria=0.4),
            Tex(r"Cada operación se deshace con otra operación elemental.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(ops, margen=0.5)
        self.decir("Veamos cada operación. Intercambiar dos ecuaciones deja la misma lista, en otro orden. Multiplicar una ecuación por un número ce distinto de cero: se cumple la original exactamente cuando se cumple la multiplicada, porque se puede dividir por ce. Y sumar ce veces una ecuación a otra: si se cumplen las dos, se cumple la suma; y al revés, restando. Así, cada operación se deshace con otra operación elemental.")
        for o in ops:
            self.play(FadeIn(o))
            self.wait(2.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Demostración")
        demo = VGroup(
            Tex(r"Sea $S$ el conjunto de soluciones del sistema y $S'$ el del sistema tras una operación.", font_size=36),
            Tex(r"($S \subseteq S'$) Una solución de las ecuaciones originales cumple la ecuación nueva, que es combinación de ellas.", font_size=36),
            Tex(r"($S' \subseteq S$) La operación se deshace con otra: las ecuaciones originales son combinación de las nuevas.", font_size=36),
            Tex(r"Luego $S = S'$. Tras varias operaciones, también. $\qquad\blacksquare$", font_size=40, color=COLOR_PIVOTE),
            Tex(r"Por eso Gauss, Gauss-Jordan y la reducción dan siempre \textbf{las mismas soluciones} que el sistema de partida.", font_size=36, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(demo, margen=0.5)
        self.decir("La demostración tiene dos inclusiones. Toda solución del sistema original cumple la ecuación nueva, porque esta es combinación de las originales. Y como la operación se deshace con otra, las ecuaciones originales son combinación de las nuevas, así que toda solución del sistema nuevo lo es del original. Los dos conjuntos coinciden, y tras varias operaciones también. Por eso Gauss y Gauss-Jordan dan siempre las mismas soluciones que el sistema de partida.")
        for d in demo:
            self.play(FadeIn(d))
            self.wait(2.8)
        self.wait(1)

        self.ejercicio_propuesto(
            "F16-N4-11",
            Text("Demuestra que las operaciones elementales conservan\nel conjunto solución (ejercicio F16-N4-11 del banco).", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: escribe tú la demostración de que las operaciones elementales conservan el conjunto solución. Pausa el video e inténtalo; la demostración está en el solucionario.",
        )
        self.resumen(
            [
                "Las tres operaciones son reversibles.",
                "Se prueban dos inclusiones: S dentro de S' y S' dentro de S.",
                "Por eso los métodos de eliminación son válidos.",
            ],
            "las demostraciones clave del curso, de un vistazo.",
            voz="En resumen: las tres operaciones son reversibles. Se prueban las dos inclusiones. Y por eso los métodos de eliminación son válidos. Siguiente: las demostraciones clave del curso, de un vistazo.",
        )


class DemostracionesClave(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 54 · Parte 3", "Las demostraciones clave, de un vistazo")
        titulo = self.encabezado("Cinco teoremas, cinco ideas")
        tarjetas = [
            ("Rouché-Frobenius", "Compatible si y solo si rg(A) = rg[A | b]; único si rg = n.", "Escalonar [A | b]: el rango sube solo si hay un pivote en la columna de b (fila 0 = c)."),
            ("Estructura de las soluciones", "Si A xp = b, las soluciones son xp + ker A.", "A(x − xp) = b − b = 0, y al revés: A(xp + n) = b + 0."),
            ("Rango y nulidad", "rg(A) + nul(A) = n.", "n columnas: r con pivote (base de Col A) y n − r libres (base de ker A)."),
            ("Columnas pivote", "Las columnas pivote de A son una base de Col(A).", "A y su reducida tienen las mismas relaciones entre columnas (mismo núcleo)."),
            ("Existencia de solución", "A x = b tiene solución si y solo si b está en Col(A).", "A x es una combinación de las columnas de A, con coeficientes x."),
        ]
        self.decir("Cinco teoremas del curso, cada uno con su idea central. Los tienes con la demostración completa en el banco de ejercicios, en la familia de demostraciones.")
        for k, (nombre, enunciado, idea) in enumerate(tarjetas):
            cabecera = Text(f"{k + 1}. {nombre}", font_size=34, weight="BOLD", color=COLOR_PIVOTE)
            enun = Text(enunciado, font_size=28)
            ide = Text(textwrap.fill("Idea: " + idea, 70), font_size=26, color=COLOR_SECUNDARIO, line_spacing=1.1)
            bloque = VGroup(cabecera, enun, ide).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(titulo, DOWN, buff=0.8)
            ajustar_al_encuadre(bloque, margen=0.5)
            bloque.to_edge(LEFT, buff=0.8)
            self.decir({
                0: "Uno, Rouché-Frobenius. El sistema es compatible si y solo si el rango de a es el de la aumentada, y es único si ese rango es ene. La idea: al escalonar la aumentada, el rango sube solo si aparece una fila cero igual a ce distinto de cero, la ecuación imposible.",
                1: "Dos, la estructura de las soluciones. Si equis pe es solución, las soluciones son equis pe más el núcleo. La idea: a por equis menos equis pe es be menos be, cero; y al revés, a por equis pe más ene es be.",
                2: "Tres, rango más nulidad igual a ene. La idea: de las ene columnas, erre tienen pivote, y son una base del espacio columna; las otras ene menos erre son las variables libres, que dan una base del núcleo.",
                3: "Cuatro, las columnas pivote de a son una base del espacio columna. La idea: a y su reducida tienen las mismas relaciones entre columnas, porque tienen el mismo núcleo.",
                4: "Y cinco, a por equis igual a be tiene solución si y solo si be está en el espacio columna. La idea: a por equis es una combinación de las columnas de a, con coeficientes equis.",
            }[k])
            self.play(FadeIn(bloque, shift=UP * 0.2))
            self.callar()
            self.wait(1)
            self.play(FadeOut(bloque))
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo se estudia una demostración")
        consejos = VGroup(
            parrafo(r"\textbf{1.} Escribe el enunciado con tus palabras y con un ejemplo $2 \times 2$.", font_size=38, sangria=0.4),
            parrafo(r"\textbf{2.} Identifica la \emph{idea} en una frase; los cálculos son su desarrollo.", font_size=38, sangria=0.4),
            parrafo(r"\textbf{3.} Comprueba cada paso con la definición exacta (rango, núcleo, independencia\dots).", font_size=38, sangria=0.4),
            parrafo(r"\textbf{4.} Prueba tú el caso contrario: ¿dónde falla si quitas una hipótesis?", font_size=38, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(consejos, margen=0.5)
        self.decir("Cómo se estudia una demostración. Uno: escribe el enunciado con tus palabras y con un ejemplo de dos por dos. Dos: identifica la idea en una frase; los cálculos son su desarrollo. Tres: comprueba cada paso con la definición exacta. Y cuatro: prueba el caso contrario, ¿dónde falla si quitas una hipótesis?")
        for c in consejos:
            self.play(FadeIn(c))
            self.wait(2.6)
        self.wait(1)

        self.ejercicio_propuesto(
            "F16-N5-11",
            Text("Escribe la demostración del teorema de Rouché-Frobenius\n(ejercicio F16-N5-11) y la del teorema del rango y la nulidad (F16-N5-12).", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: escribe la demostración del teorema de Rouché-Frobenius y la del teorema del rango y la nulidad. Pausa el video e inténtalo; las demostraciones están en el solucionario.",
        )
        self.resumen(
            [
                "Cinco teoremas: Rouché-Frobenius, estructura, rango-nulidad, columnas pivote, existencia.",
                "Cada uno se resume en una idea: pivotes, diferencia de soluciones, relaciones entre columnas.",
            ],
            "Lección 55 — repaso final y mapa del curso.",
            voz="En resumen: cinco teoremas, cada uno con una idea central: los pivotes, la diferencia de soluciones, las relaciones entre columnas. Siguiente: lección cincuenta y cinco, repaso final y mapa del curso.",
        )
