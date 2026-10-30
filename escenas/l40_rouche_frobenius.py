"""Lección 40 — El teorema de Rouché-Frobenius.

Escenas (un video cada una):
    EnunciadoRF, DemostracionRF, IncognitasRangoYLibres

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l40_rouche_frobenius.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def panel_caso(datos, pivotes, rg_a, rg_ab, n, resultado, color):
    """Matriz aumentada reducida con sus dos rangos y la conclusión."""
    m = matriz_gauss(datos, pivotes=pivotes, escala=0.62)
    rangos = MathTex(rf"\operatorname{{rg}}(A) = {rg_a},\ \operatorname{{rg}}[A \mid \mathbf{{b}}] = {rg_ab},\ n = {n}", font_size=30).next_to(m, DOWN, buff=0.35)
    final = Text(resultado, font_size=TAM_NOTA, color=color, weight="BOLD").next_to(rangos, DOWN, buff=0.25)
    return VGroup(m, rangos, final)


class EnunciadoRF(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 40 · Parte 1", "El teorema de Rouché-Frobenius")
        titulo = self.encabezado("Clasificar sin resolver")
        teorema = VGroup(
            Tex(r"\textbf{Teorema (Rouché-Frobenius).} Sea $A\mathbf{x} = \mathbf{b}$ un sistema de $m$ ecuaciones", font_size=36),
            Tex(r"con $n$ incógnitas, y $r = \operatorname{rg}(A)$. Entonces:", font_size=36),
            parrafo(r"(1) Es compatible $\iff \operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$.", font_size=36, sangria=0.6),
            parrafo(r"(2) Si es compatible y $r = n$: \textbf{una} solución (SCD).", font_size=36, sangria=0.6, color=COLOR_SOLUCION),
            parrafo(r"(3) Si es compatible y $r < n$: \textbf{infinitas}, con $n - r$ parámetros (SCI).", font_size=36, sangria=0.6, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(teorema, margen=0.5)
        self.decir("El teorema de Rouché-Frobenius clasifica un sistema sin resolverlo. Sea a equis igual a be un sistema de eme ecuaciones con ene incógnitas, y erre el rango de a. Uno: el sistema es compatible si y solo si el rango de a es igual al rango de la aumentada. Dos: si es compatible y erre es igual a ene, hay una única solución. Y tres: si es compatible y erre es menor que ene, hay infinitas soluciones, con ene menos erre parámetros.")
        for t in teorema:
            self.play(FadeIn(t))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Los tres casos en matrices")
        paneles = VGroup(
            panel_caso([[1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 2]], [(0, 0), (1, 1), (2, 2)], 3, 3, 3, "SCD", COLOR_SOLUCION),
            panel_caso([[1, 0, -1, -2], [0, 1, 2, 3], [0, 0, 0, 0]], [(0, 0), (1, 1)], 2, 2, 3, "SCI (1 parámetro)", COLOR_LIBRE),
            panel_caso([[1, 0, -1, 0], [0, 1, 2, 0], [0, 0, 0, 1]], [(0, 0), (1, 1), (2, 3)], 2, 3, 3, "SI", COLOR_ERROR),
        ).arrange(RIGHT, buff=0.5, aligned_edge=UP).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(paneles, margen=0.4)
        frases = (
            "Primer caso: los dos rangos valen tres, y hay tres incógnitas. Es compatible determinado.",
            "Segundo caso: los dos rangos valen dos, y hay tres incógnitas. Es compatible, con tres menos dos, un parámetro: indeterminado.",
            "Tercer caso: el rango de a vale dos, y el de la aumentada, tres. No coinciden: incompatible.",
        )
        for p, frase in zip(paneles, frases):
            self.decir(frase)
            self.play(FadeIn(p))
            self.wait(1.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Consecuencias inmediatas")
        consecuencias = VGroup(
            Tex(r"Si $m < n$: $r \le m < n$, así que nunca hay una única solución (L12, L32).", font_size=36),
            Tex(r"Si $\operatorname{rg}(A) = m$ (rango por filas completo): $\operatorname{rg}[A \mid \mathbf{b}] = m$ para todo $\mathbf{b}$:", font_size=36),
            Tex(r"el sistema es \emph{siempre} compatible, para cualquier lado derecho.", font_size=36, color=COLOR_PIVOTE),
            Tex(r"Un sistema homogéneo ($\mathbf{b} = \mathbf{0}$): $\operatorname{rg}[A \mid \mathbf{0}] = \operatorname{rg}(A)$, siempre compatible.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(consecuencias, margen=0.5)
        self.decir("Algunas consecuencias inmediatas. Con menos ecuaciones que incógnitas, el rango no supera a eme, que es menor que ene: nunca hay solución única. Si el rango de a es igual al número de filas, el rango de la aumentada también lo es, para cualquier be: el sistema siempre es compatible. Y un sistema homogéneo siempre es compatible, porque añadir una columna de ceros no cambia el rango.")
        for c in consecuencias:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N2-03",
            VGroup(
                Text("Clasifica con el teorema de Rouché-Frobenius, y resuelve si es compatible:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y + z = 4 \\ 2x + 4y + 3z = 9 \\ 3x + 6y + 4z = 13 \end{cases}", font_size=44),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: clasifica este sistema con el teorema de Rouché-Frobenius, calculando los dos rangos, y resuélvelo si es compatible. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Compatible ⇔ rg(A) = rg[A | b].",
                "Compatible con r = n: una solución. Con r < n: infinitas, n − r parámetros.",
                "rg(A) = m: siempre compatible. Homogéneo: siempre compatible.",
            ],
            "por qué es cierto: la demostración.",
            voz="En resumen: el sistema es compatible si y solo si el rango de a es igual al de la aumentada. Si es compatible con erre igual a ene, una solución; con erre menor que ene, infinitas, con ene menos erre parámetros. Si el rango de a es igual a eme, siempre es compatible; y los homogéneos también. Siguiente: por qué es cierto.",
        )


class DemostracionRF(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 40 · Parte 2", "Demostración")
        titulo = self.encabezado("Vía la forma escalonada")
        base = VGroup(
            parrafo(r"Las operaciones por filas conservan las soluciones (L24) y los rangos.", r"Basta probar el teorema para $[A \mid \mathbf{b}]$ ya \textbf{escalonada}.", font_size=38, sangria=0.5),
            parrafo(r"En una escalonada, $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$ son los pivotes", r"en las columnas de $A$ y en todas las columnas.", font_size=38, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(base, margen=0.5)
        self.decir("La demostración usa la forma escalonada. Las operaciones por filas conservan las soluciones, y los rangos; así que basta probar el teorema con la matriz aumentada ya escalonada. En ella, el rango de a son los pivotes de las columnas de a, y el de la aumentada, los pivotes de todas las columnas.")
        for b in base:
            self.play(FadeIn(b))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "(1) Compatible ⇔ los dos rangos coinciden")
        ida = VGroup(
            parrafo(r"\textbf{($\Rightarrow$)} Si es compatible, ninguna fila es $[\,0\ \cdots\ 0 \mid c\,]$ con $c \ne 0$,", r"así que no hay pivote en la columna de $\mathbf{b}$: los dos rangos son iguales.", font_size=36, sangria=0.6, color=COLOR_SOLUCION),
            parrafo(r"\textbf{($\Leftarrow$)} Si los rangos coinciden, no hay pivote en la columna de $\mathbf{b}$,", r"luego no hay ninguna ecuación $0 = c$ imposible. Sustituyendo hacia atrás", r"se construye una solución (L28).", font_size=36, sangria=0.6, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(ida, margen=0.5)
        self.decir("Primera parte: compatible si y solo si los rangos coinciden. Si es compatible, ninguna fila es de ceros con un número distinto de cero al final, así que no hay pivote en la columna de be, y los dos rangos son iguales. Y al revés, si los rangos coinciden, no hay pivote en la columna de be, no hay ninguna ecuación imposible, y sustituyendo hacia atrás se construye una solución.")
        for i in ida:
            self.play(FadeIn(i))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "(2) y (3) Cuántas soluciones")
        cuantas = VGroup(
            parrafo(r"Las $r$ variables pivote se despejan hacia atrás; las otras $n - r$ son libres.", font_size=36, sangria=0.4),
            parrafo(r"\textbf{Si $r = n$:} no hay libres, todas las incógnitas están determinadas: \textbf{una} solución.", font_size=36, sangria=0.4, color=COLOR_SOLUCION),
            parrafo(r"\textbf{Si $r < n$:} hay al menos una libre. Cada valor real que le demos", r"da una solución distinta: \textbf{infinitas}, con $n - r$ parámetros. $\blacksquare$", font_size=36, sangria=0.4, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(cuantas, margen=0.5)
        self.decir("Segunda parte: cuántas soluciones. Las erre variables pivote se despejan hacia atrás; las otras ene menos erre son libres. Si erre es igual a ene, no hay libres, y todas las incógnitas quedan determinadas: una solución. Si erre es menor que ene, hay al menos una libre, y cada valor real que le demos da una solución distinta: infinitas, con ene menos erre parámetros.")
        for c in cuantas:
            self.play(FadeIn(c))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Un ejemplo, con los dos rangos")
        sis = VGroup(
            MathTex(r"\begin{cases} x + y + z = 2 \\ x + 2y + 3z = 5 \\ 2x + 3y + 4z = 7 \end{cases}", font_size=40),
            MathTex(r"\left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 1 & 2 & 3 & 5 \\ 2 & 3 & 4 & 7 \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 0 & -1 & -1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{array}\right]", font_size=36),
            Tex(r"$\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 2 < 3 = n$: compatible, $3 - 2 = 1$ parámetro.", font_size=36, color=COLOR_LIBRE),
            MathTex(r"(x, y, z) = (-1 + t,\ 3 - 2t,\ t)", font_size=40, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(sis, margen=0.5)
        self.decir("Un ejemplo, con el sistema de la lección veintiocho. Al reducir, los dos rangos valen dos, y hay tres incógnitas. Es compatible, con tres menos dos, un parámetro. La solución es menos uno más te, tres menos dos te, te.")
        for s in sis:
            self.play(FadeIn(s))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N3-02",
            VGroup(
                Text("Demuestra con la forma escalonada:", font_size=TAM_TEXTO),
                Text("si rg(A) < rg[A | b], el sistema es incompatible.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: demuestra, con la forma escalonada, que si el rango de a es menor que el de la aumentada, el sistema es incompatible. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Se escalona [A | b]: las operaciones conservan soluciones y rangos.",
                "Pivote en b ⇒ ecuación 0 = c imposible ⇒ incompatible.",
                "Sin pivote en b: n − r libres ⇒ una solución si n − r = 0, infinitas si no.",
            ],
            "las incógnitas, el rango y las variables libres.",
            voz="En resumen: se escalona la matriz aumentada. Un pivote en la columna de be da una ecuación imposible, cero igual a ce: incompatible. Sin pivote en be, hay ene menos erre variables libres: una solución si ene menos erre es cero, e infinitas si no. Siguiente: las incógnitas, el rango y las variables libres.",
        )


class IncognitasRangoYLibres(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 40 · Parte 3", "Incógnitas, rango y variables libres")
        titulo = self.encabezado("n − r variables libres")
        formula = MathTex(r"\underbrace{n}_{\text{incógnitas}} \;-\; \underbrace{r}_{\text{pivotes (rango)}} \;=\; \underbrace{n - r}_{\text{variables libres}}", font_size=48).next_to(titulo, DOWN, buff=0.7)
        ejemplos = VGroup(
            MathTex(r"n = 5,\ \ r = 3:\ \ 2 \text{ parámetros (un plano de soluciones)}", font_size=38),
            MathTex(r"n = 4,\ \ r = 4:\ \ 0 \text{ parámetros (solución única)}", font_size=38),
            MathTex(r"n = 3,\ \ r = 1:\ \ 2 \text{ parámetros (un plano en } \mathbb{R}^3\text{)}", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(formula, DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(formula, ejemplos), margen=0.5)
        self.decir("El número de variables libres es el de incógnitas menos el rango. Con cinco incógnitas y rango tres, dos parámetros. Con cuatro incógnitas y rango cuatro, ninguno: solución única. Con tres incógnitas y rango uno, dos parámetros: un plano de soluciones.")
        self.play(Write(formula))
        for e in ejemplos:
            self.play(FadeIn(e))
            self.wait(1.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Geometría: el rango fija la dimensión")
        geo = VGroup(
            Tex(r"Con $\mathbf{x} \in \mathbb{R}^3$ y sistema compatible:", font_size=38),
            Tex(r"$n - r = 0$: un \textbf{punto}.", font_size=38, color=COLOR_SOLUCION),
            Tex(r"$n - r = 1$: una \textbf{recta}.", font_size=38, color=COLOR_LIBRE),
            Tex(r"$n - r = 2$: un \textbf{plano}.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"$n - r = 3$ ($A = O$, $\mathbf{b} = \mathbf{0}$): todo $\mathbb{R}^3$.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(geo, margen=0.5)
        self.decir("Geométricamente, el rango fija la dimensión del conjunto de soluciones. En tres incógnitas, con un sistema compatible: ene menos erre igual a cero, un punto. Uno: una recta. Dos: un plano. Y tres, solo si a es la matriz nula y be es cero: todo el espacio.")
        for g in geo:
            self.play(FadeIn(g))
            self.wait(1.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cada ecuación independiente quita una libertad")
        quitar = VGroup(
            Tex(r"En $\mathbb{R}^3$: \ 1 ecuación independiente $\to$ plano; \ 2 $\to$ recta; \ 3 $\to$ punto.", font_size=38),
            Tex(r"Lo que en la L10 era ``normalmente'' ahora tiene nombre: \textbf{independientes} = rango.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Las ecuaciones que no suben el rango, no quitan libertad.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(quitar, margen=0.5)
        self.decir("Cada ecuación independiente quita una libertad. En el espacio, una ecuación independiente deja un plano; dos, una recta; tres, un punto. Lo que en la lección diez era normalmente, ahora tiene nombre: independientes, es decir, rango. Las ecuaciones que no suben el rango no quitan libertad.")
        for q in quitar:
            self.play(FadeIn(q))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F11-N4-02",
            VGroup(
                Text("Un sistema compatible tiene 4 ecuaciones y 5 incógnitas, con rg(A) = 3.", font_size=TAM_TEXTO),
                Text("¿Cuántos parámetros tiene la solución? ¿Qué cambia si rg[A | b] = 4?", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: un sistema compatible tiene cuatro ecuaciones y cinco incógnitas, con rango de a igual a tres. ¿Cuántos parámetros tiene la solución? ¿Qué cambia si el rango de la aumentada es cuatro? Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Variables libres = n − r.",
                "Dimensión del conjunto de soluciones = n − r.",
                "Rango = número de ecuaciones independientes.",
            ],
            "Lección 41 — clasificación con ejemplos.",
            voz="En resumen: el número de variables libres es ene menos erre, y es también la dimensión del conjunto de soluciones. El rango es el número de ecuaciones independientes. Siguiente: lección cuarenta y uno, clasificación con ejemplos.",
        )
