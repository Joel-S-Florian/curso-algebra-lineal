"""Lección 42 — Discusión con parámetros y clasificación sin resolver.

Escenas (un video cada una):
    DiscusionConParametro, ClasificarSinResolver

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l42_discusion_con_parametros.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class DiscusionConParametro(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 42 · Parte 1", "Discutir con rangos")
        titulo = self.encabezado("Un parámetro en la matriz de coeficientes")
        sistema = MathTex(r"\begin{cases} x + y = 1 \\ x + a\,y = b \end{cases}", font_size=46).next_to(titulo, DOWN, buff=0.6).to_edge(LEFT, buff=1.0)
        reducida = MathTex(r"\left[\begin{array}{cc|c} 1 & 1 & 1 \\ 1 & a & b \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - R_1} \left[\begin{array}{cc|c} 1 & 1 & 1 \\ 0 & a-1 & b-1 \end{array}\right]", font_size=40).next_to(sistema, DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(sistema, reducida), margen=0.5)
        self.decir("Discutir un sistema es clasificarlo para cada valor de los parámetros. Tomemos equis más ye igual a uno, y equis más a ye igual a be, con a y be parámetros. Escalonamos: a la fila dos le restamos la fila uno, y queda cero, a menos uno, be menos uno.")
        self.play(Write(sistema))
        self.play(Write(reducida))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Los casos, con los rangos")
        casos = VGroup(
            parrafo(r"$a \ne 1$: $a - 1$ es pivote. $\operatorname{rg}(A) = 2 = \operatorname{rg}[A \mid \mathbf{b}] = n$.", r"\textbf{SCD} para cualquier $b$.", font_size=36, sangria=0.5, color=COLOR_SOLUCION),
            parrafo(r"$a = 1$ y $b = 1$: la fila 2 es $[\,0\ 0 \mid 0\,]$. $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 1 < 2$.", r"\textbf{SCI}, con $2 - 1 = 1$ parámetro.", font_size=36, sangria=0.5, color=COLOR_LIBRE),
            parrafo(r"$a = 1$ y $b \ne 1$: la fila 2 es $[\,0\ 0 \mid b - 1\,]$ con $b - 1 \ne 0$.", r"$\operatorname{rg}(A) = 1 \ne 2 = \operatorname{rg}[A \mid \mathbf{b}]$: \textbf{SI}.", font_size=36, sangria=0.5, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(casos, margen=0.5)
        frases = (
            "Si a es distinto de uno, a menos uno es un pivote: los dos rangos valen dos, igual que el número de incógnitas. Es compatible determinado, para cualquier be.",
            "Si a vale uno, y be vale uno, la fila dos es de ceros: los dos rangos valen uno, menor que dos. Compatible indeterminado, con un parámetro.",
            "Y si a vale uno, pero be es distinto de uno, la fila dos es cero, cero, be menos uno, con be menos uno distinto de cero: el rango de la aumentada es dos, y el de a, uno. Incompatible.",
        )
        for c, frase in zip(casos, frases):
            self.decir(frase)
            self.play(FadeIn(c))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo se escribe una discusión")
        receta = VGroup(
            parrafo(r"\textbf{1.} Escalona $[A \mid \mathbf{b}]$ \emph{sin dividir} por expresiones", r"que puedan valer $0$ (solo sumas de filas y escalados por números).", font_size=34, sangria=0.5),
            parrafo(r"\textbf{2.} Halla los valores que anulan cada candidato a pivote.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{3.} Para cada caso, sustituye en toda la matriz y calcula los dos rangos.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{4.} Aplica Rouché-Frobenius y escribe la conclusión (y la solución si hace falta).", font_size=34, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(receta, margen=0.5)
        self.decir("Para escribir una discusión: uno, se escalona la aumentada sin dividir por expresiones que puedan valer cero. Dos, se buscan los valores que anulan cada candidato a pivote. Tres, para cada caso, se sustituye en toda la matriz y se calculan los dos rangos. Y cuatro, se aplica Rouché-Frobenius y se escribe la conclusión.")
        for r in receta:
            self.play(FadeIn(r))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N3-05",
            VGroup(
                Text("Discute según m, con los rangos:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} m\,x + y = 1 \\ x + m\,y = m \end{cases}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: discute este sistema según el valor del parámetro eme, con los rangos de a y de la aumentada. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Discutir = clasificar para cada valor del parámetro.",
                "Se escalona sin dividir por lo que puede valer 0 y se estudian los valores críticos.",
                "En cada caso: rg(A), rg[A | b], n, y Rouché-Frobenius.",
            ],
            "clasificar un sistema 3 × 3 sin resolverlo.",
            voz="En resumen: discutir es clasificar para cada valor del parámetro. Se escalona sin dividir por lo que puede valer cero, y se estudian los valores críticos. En cada caso, se calculan los rangos y se aplica Rouché-Frobenius. Siguiente: clasificar un sistema de tres por tres sin resolverlo.",
        )


class ClasificarSinResolver(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 42 · Parte 2", "Clasificar sin resolver")
        titulo = self.encabezado("Un parámetro en el término independiente")
        sistema = MathTex(r"\begin{cases} x + y + z = 1 \\ x + 2y + 3z = 2 \\ x + 3y + 5z = k \end{cases}", font_size=44).next_to(titulo, DOWN, buff=0.6).to_edge(LEFT, buff=1.0)
        pasos = MathTex(
            r"\left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 2 \\ 1 & 3 & 5 & k \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 0 & k - 3 \end{array}\right]",
            font_size=38,
        ).next_to(sistema, RIGHT, buff=0.7)
        ajustar_al_encuadre(VGroup(sistema, pasos), margen=0.5)
        self.decir("Veamos un sistema de tres por tres con un parámetro ka en el término independiente. Restamos la primera fila a la segunda y a la tercera, y después, a la tercera, le restamos el doble de la segunda. La última fila queda cero, cero, cero, ka menos tres.")
        self.play(Write(sistema))
        self.play(Write(pasos))
        self.wait(2)
        casos = VGroup(
            parrafo(r"$k = 3$: $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 2 < 3$: \textbf{SCI}, 1 parámetro.", font_size=36, sangria=0.5, color=COLOR_LIBRE),
            parrafo(r"$k \ne 3$: $\operatorname{rg}(A) = 2 \ne 3 = \operatorname{rg}[A \mid \mathbf{b}]$: \textbf{SI}.", font_size=36, sangria=0.5, color=COLOR_ERROR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(VGroup(sistema, pasos), DOWN, buff=0.7)
        ajustar_al_encuadre(casos, margen=0.5)
        self.decir("Hay dos casos. Si ka vale tres, la última fila es de ceros: los dos rangos valen dos, y hay tres incógnitas. Compatible indeterminado, con un parámetro. Y si ka es distinto de tres, el rango de la aumentada es tres, y el de a, dos: incompatible. Nunca es determinado, para ningún valor de ka.")
        for c in casos:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cuando la solución sí interesa")
        solucion = VGroup(
            Tex(r"Para $k = 3$: $y + 2z = 1$ y $x + y + z = 1$.", font_size=38),
            MathTex(r"z = t:\quad y = 1 - 2t,\quad x = 1 - (1 - 2t) - t = t", font_size=42),
            MathTex(r"(x, y, z) = (t,\ 1 - 2t,\ t)", font_size=46, color=COLOR_SOLUCION),
            Tex(r"Verificación en la tercera ecuación: $t + 3(1 - 2t) + 5t = 3 = k$ \checkmark", font_size=36, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(solucion, margen=0.5)
        self.decir("Y si nos interesa la solución, para ka igual a tres, resolvemos como siempre: zeta es te, ye vale uno menos dos te, y equis vale te. Verificamos en la tercera ecuación: te más tres por uno menos dos te, más cinco te, es tres, que es ka.")
        for s in solucion:
            self.play(FadeIn(s))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cuadrada no significa invertible")
        cuadrada = VGroup(
            MathTex(r"\begin{cases} x + y = 1 \\ x + y = 3 \end{cases}\quad A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix},\quad \operatorname{rg}(A) = 1 < 2", font_size=42),
            Tex(r"$A$ es cuadrada ($2 \times 2$), pero su reducida no es $I$: \textbf{no} es invertible.", font_size=38, color=COLOR_ERROR),
            Tex(r"Mismo número de ecuaciones e incógnitas \emph{no} basta para SCD: hace falta $\operatorname{rg}(A) = n$.", font_size=38),
            Tex(r"Con $\operatorname{rg}(A) = n$, el sistema es SCD para todo $\mathbf{b}$ (Unidad 8: $A$ invertible).", font_size=36, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(cuadrada, margen=0.5)
        self.decir("Una advertencia: que la matriz sea cuadrada no significa que sea invertible. Esta matriz, uno, uno; uno, uno, es de dos por dos, pero su rango es uno, menor que dos: su reducida no es la identidad. Tener tantas ecuaciones como incógnitas no basta para que el sistema sea determinado: hace falta que el rango sea ene. Con rango ene, el sistema es determinado para cualquier be: es lo que en la unidad ocho llamaremos matriz invertible.")
        for c in cuadrada:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N4-05",
            VGroup(
                Text("Discute según k y resuelve cuando sea compatible:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + y + z = 1 \\ x + 2y + 3z = 2 \\ x + 3y + 5z = k \end{cases}", font_size=44),
                Text("(Variante: cambia el segundo término independiente por m y discute según k y m.)", font_size=TAM_NOTA - 2),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: discute este sistema según ka, y resuélvelo cuando sea compatible. Como variante, cambia el segundo término independiente por eme, y discute según ka y eme. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Los parámetros pueden estar en A o en b: siempre se comparan rg(A), rg[A | b] y n.",
                "Se escalona sin dividir por expresiones con parámetro.",
                "Cuadrada no implica invertible: hace falta rg = n.",
            ],
            "Unidad 8 — núcleo e imagen.",
            voz="En resumen: los parámetros pueden estar en a o en be; siempre se comparan los rangos de a y de la aumentada, y ene. Se escalona sin dividir por expresiones con parámetro. Y que la matriz sea cuadrada no implica que sea invertible: hace falta que el rango sea ene. Siguiente: unidad ocho, núcleo e imagen.",
        )
