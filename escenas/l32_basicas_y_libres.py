"""Lección 32 — Variables básicas y libres: leer la solución de la reducida.

Escenas (un video cada una):
    LeerLaSolucion, TresFinalesPosibles

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l32_basicas_y_libres.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def cabeceras_de(m, nombres, colores):
    """Etiquetas de las incógnitas sobre las columnas de m (sin la de b), con su color."""
    c = VGroup(*[MathTex(v, font_size=38, color=col).next_to(col_m, UP, buff=0.45) for v, col, col_m in zip(nombres, colores, m.get_columns())])
    c.align_to(c[0], DOWN)
    return c


class LeerLaSolucion(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 32 · Parte 1", "Variables básicas y libres")
        titulo = self.encabezado("Qué columna es qué")
        m = matriz_gauss([[1, 2, 0, -1, 3], [0, 0, 1, 4, 2], [0, 0, 0, 0, 0]], pivotes=[(0, 0), (1, 2)]).move_to(LEFT * 3.5 + UP * 0.4)
        nombres = ("x_1", "x_2", "x_3", "x_4")
        colores = (COLOR_PIVOTE, COLOR_LIBRE, COLOR_PIVOTE, COLOR_LIBRE)
        cab = cabeceras_de(m, nombres, colores)
        lectura = VGroup(
            Tex(r"Columnas \textbf{pivote}: 1 y 3", font_size=36, color=COLOR_PIVOTE),
            Tex(r"\textbf{Variables básicas}: $x_1,\ x_3$", font_size=36, color=COLOR_PIVOTE),
            Tex(r"Columnas \textbf{sin pivote}: 2 y 4", font_size=36, color=COLOR_LIBRE),
            Tex(r"\textbf{Variables libres}: $x_2,\ x_4$", font_size=36, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(m, RIGHT, buff=0.9)
        self.decir("Esta matriz aumentada está en forma reducida. Las columnas uno y tres tienen pivote: sus variables, equis uno y equis tres, son las variables básicas. Las columnas dos y cuatro no tienen pivote: sus variables, equis dos y equis cuatro, son las variables libres.")
        self.play(FadeIn(m), FadeIn(cab))
        self.play(Create(escalera(m, [(0, 0), (1, 2)])))
        for t in lectura:
            self.play(FadeIn(t))
            self.wait(0.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Las libres reciben parámetros; las básicas se despejan")
        m = matriz_gauss([[1, 2, 0, -1, 3], [0, 0, 1, 4, 2], [0, 0, 0, 0, 0]], pivotes=[(0, 0), (1, 2)], escala=0.75).move_to(LEFT * 4.4 + UP * 0.2)
        cab = cabeceras_de(m, nombres, colores)
        parametros =MathTex(r"x_2 = s,\qquad x_4 = t", font_size=44, color=COLOR_LIBRE).next_to(titulo, DOWN, buff=0.6).set_x(2.6)
        eq1 = MathTex(r"x_1 + 2x_2 - x_4 = 3 \;\Rightarrow\; x_1 = 3 - 2s + t", font_size=38)
        eq2 = MathTex(r"x_3 + 4x_4 = 2 \;\Rightarrow\; x_3 = 2 - 4t", font_size=38)
        eq3 = MathTex(r"0 = 0 \quad (\text{no dice nada})", font_size=38, color=COLOR_SECUNDARIO)
        ecuaciones = VGroup(eq1, eq2, eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(parametros, DOWN, buff=0.6).set_x(2.6)
        ajustar_al_encuadre(VGroup(parametros, ecuaciones), margen=0.5)
        self.decir("Para leer la solución, damos un parámetro a cada variable libre: equis dos es ese, equis cuatro es te.")
        self.play(FadeIn(m), FadeIn(cab))
        self.play(Write(parametros))
        for i, ec in enumerate((eq1, eq2, eq3)):
            marco = SurroundingRectangle(m.get_rows()[i], color=COLOR_PIVOTE)
            frases = (
                "La primera fila dice equis uno más dos equis dos menos equis cuatro igual a tres. Despejamos la básica: equis uno vale tres menos dos ese más te.",
                "La segunda fila dice equis tres más cuatro equis cuatro igual a dos: equis tres vale dos menos cuatro te.",
                "Y la tercera fila es cero igual a cero: no dice nada.",
            )
            self.decir(frases[i])
            self.play(Create(marco), Write(ec))
            self.wait(1)
            self.play(FadeOut(marco))
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "En forma vectorial")
        vectorial = MathTex(
            r"\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \\ 2 \\ 0 \end{bmatrix} + s\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + t\begin{bmatrix} 1 \\ 0 \\ -4 \\ 1 \end{bmatrix}",
            font_size=46,
        ).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(vectorial)
        regla = VGroup(
            Tex(r"Un vector fijo (libres $= 0$): la columna de $\mathbf{b}$ de la reducida.", font_size=34, color=COLOR_TERMINO_INDEP),
            parrafo(r"Un vector por cada libre: un $1$ en su posición, y en las posiciones básicas,", r"la columna de esa libre \emph{cambiada de signo}.", font_size=34, color=COLOR_LIBRE, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(vectorial, DOWN, buff=0.6)
        ajustar_al_encuadre(regla)
        self.decir("Escrita como vectores, la solución es un vector fijo más un múltiplo de un vector por cada variable libre. El vector fijo es la columna de be de la reducida: son los valores cuando las libres valen cero.")
        self.play(Write(vectorial))
        self.wait(1)
        self.decir("Y cada vector de los parámetros tiene un uno en la posición de su libre, y en las posiciones de las básicas, la columna de esa libre, cambiada de signo. Se puede leer sin hacer cuentas.")
        for r in regla:
            self.play(FadeIn(r))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificación")
        verif = VGroup(
            MathTex(r"s = 1,\ t = 0:\ (1, 1, 2, 0)\quad 1 + 2 - 0 = 3\ \checkmark,\quad 2 + 0 = 2\ \checkmark", font_size=38),
            MathTex(r"s = 0,\ t = 1:\ (4, 0, -2, 1)\quad 4 + 0 - 1 = 3\ \checkmark,\quad -2 + 4 = 2\ \checkmark", font_size=38),
            MathTex(r"\text{general: } (3 - 2s + t) + 2s - t = 3 \ \checkmark,\quad (2 - 4t) + 4t = 2\ \checkmark", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        verif.set_color(COLOR_SOLUCION)
        ajustar_al_encuadre(verif)
        cuenta = Tex(r"4 incógnitas $-$ 2 pivotes $=$ 2 variables libres $=$ 2 parámetros", font_size=38, color=COLOR_PIVOTE).next_to(verif, DOWN, buff=0.7)
        ajustar_al_encuadre(VGroup(verif, cuenta))
        self.decir("Verificamos con valores concretos: ese uno, te cero, da uno, uno, dos, cero; y ese cero, te uno, da cuatro, cero, menos dos, uno. Las dos ecuaciones se cumplen. Y con los parámetros generales, los términos con ese y con te se cancelan.")
        for v in verif:
            self.play(Write(v))
            self.wait(1)
        self.decir("La cuenta final: cuatro incógnitas menos dos pivotes son dos variables libres, y dos parámetros.")
        self.play(FadeIn(cuenta))
        self.wait(2)

        self.ejercicio_propuesto(
            "F09-N2-03",
            VGroup(
                Text("Lleva a forma reducida y escribe la solución en forma paramétrica y vectorial:", font_size=TAM_TEXTO),
                MathTex(r"\begin{cases} x + 2y + z = 3 \\ 2x + 4y + 3z = 8 \end{cases}", font_size=48),
                Text("Identifica las variables básicas y las libres, y verifica.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: lleva este sistema a forma reducida, escribe la solución en forma paramétrica y vectorial, identifica las variables básicas y las libres, y verifica. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Columnas con pivote: variables básicas. Sin pivote: variables libres.",
                "Cada libre recibe un parámetro; cada básica se despeja de su fila.",
                "Solución = vector fijo + un vector por cada libre.",
                "Parámetros = incógnitas − pivotes.",
            ],
            "los tres finales posibles.",
            voz="En resumen: las columnas con pivote son variables básicas, y las que no tienen pivote, variables libres. Cada libre recibe un parámetro, y cada básica se despeja de su fila. La solución es un vector fijo más un vector por cada libre. Y el número de parámetros es el de incógnitas menos el de pivotes. Siguiente: los tres finales posibles.",
        )


class TresFinalesPosibles(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 32 · Parte 2", "Tres finales posibles")
        titulo = self.encabezado("Qué dice la reducida de un sistema")
        casos = [
            ([[1, 0, 0, 1], [0, 1, 0, -1], [0, 0, 1, 2]], [(0, 0), (1, 1), (2, 2)], "Un pivote por incógnita,\nsin pivote en b", "una solución: SCD", COLOR_SOLUCION),
            ([[1, 0, 2, 3], [0, 1, -1, 1], [0, 0, 0, 0]], [(0, 0), (1, 1)], "Alguna incógnita sin pivote,\nsin pivote en b", "infinitas: SCI", COLOR_LIBRE),
            ([[1, 0, 2, 3], [0, 1, -1, 1], [0, 0, 0, 1]], [(0, 0), (1, 1), (2, 3)], "Pivote en la columna\nde b", "ninguna: SI", COLOR_ERROR),
        ]
        paneles = VGroup()
        for datos, pivotes, condicion, resultado, color in casos:
            m = matriz_gauss(datos, pivotes=pivotes, escala=0.62)
            paneles.add(VGroup(
                m,
                Text(condicion, font_size=TAM_NOTA - 4, line_spacing=1.1).next_to(m, DOWN, buff=0.35),
                Text(resultado, font_size=TAM_NOTA, color=color, weight="BOLD"),
            ))
            paneles[-1][2].next_to(paneles[-1][1], DOWN, buff=0.25)
        paneles.arrange(RIGHT, buff=0.7, aligned_edge=UP).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(paneles)
        frases = (
            "Primer final: hay un pivote en cada columna de las incógnitas, y ninguno en la columna de be. La reducida da el valor de cada incógnita: una única solución. Es compatible determinado.",
            "Segundo final: alguna incógnita no tiene pivote, y tampoco hay pivote en la columna de be. Esa incógnita es libre: hay infinitas soluciones. Es compatible indeterminado.",
            "Tercer final: hay un pivote en la columna de be. La última fila dice cero igual a uno: el sistema es incompatible.",
        )
        for p, frase in zip(paneles, frases):
            self.decir(frase)
            self.play(FadeIn(p[0]))
            self.play(FadeIn(p[1]), FadeIn(p[2]))
            self.wait(1)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El criterio, en tres preguntas")
        criterio = VGroup(
            parrafo(r"\textbf{1.} ¿Hay un pivote en la columna de $\mathbf{b}$?", r"Sí $\Rightarrow$ \textbf{incompatible} (SI). Se acabó.", font_size=38, sangria=0.6, color=COLOR_ERROR),
            parrafo(r"\textbf{2.} Si no: ¿hay un pivote en \emph{cada} columna de las incógnitas?", r"Sí $\Rightarrow$ \textbf{una solución} (SCD).", font_size=38, sangria=0.6, color=COLOR_SOLUCION),
            parrafo(r"\textbf{3.} Si no: alguna incógnita queda libre.", r"$\Rightarrow$ \textbf{infinitas soluciones} (SCI), con $n - r$ parámetros.", font_size=38, sangria=0.6, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(criterio)
        self.decir("El criterio se resume en tres preguntas. Primera: ¿hay un pivote en la columna de be? Si es así, es incompatible, y se acabó. Segunda: si no, ¿hay un pivote en cada columna de las incógnitas? Entonces hay una única solución. Y tercera: si no, alguna incógnita queda libre: infinitas soluciones, con ene menos erre parámetros, donde erre es el número de pivotes.")
        for c in criterio:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Lo que los pivotes explican")
        notas = VGroup(
            Tex(r"Como hay a lo sumo un pivote por fila, $r \le m$ (ecuaciones) y $r \le n$ (incógnitas).", font_size=36),
            Tex(r"Si $m < n$, hay incógnitas sin pivote: nunca puede haber una única solución (L12).", font_size=36),
            Tex(r"Una fila $[\,0 \ \cdots \ 0 \mid 0\,]$ no cuenta: lo que importa son los \textbf{pivotes}, no las ecuaciones.", font_size=36),
            Tex(r"Ese número $r$ de pivotes es el \textbf{rango} (Unidad 7).", font_size=36, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(notas)
        self.decir("Los pivotes lo explican todo. Hay a lo sumo un pivote por fila, así que el número de pivotes no supera ni al de ecuaciones ni al de incógnitas. Si hay menos ecuaciones que incógnitas, siempre queda alguna libre, y nunca hay una única solución. Una fila de ceros no cuenta: importan los pivotes, no las ecuaciones. Y ese número de pivotes se llamará rango, en la unidad siete.")
        for n in notas:
            self.play(FadeIn(n))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F09-N3-04",
            VGroup(
                Text("Clasifica cada sistema (SCD, SCI o SI) mirando solo su matriz reducida:", font_size=TAM_TEXTO),
                MathTex(
                    r"\text{a) } \left[\begin{array}{ccc|c} 1 & 0 & 3 & 2 \\ 0 & 1 & -1 & 4 \end{array}\right] \quad \text{b) } \left[\begin{array}{ccc|c} 1 & 0 & 0 & 5 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & 0 \end{array}\right] \quad \text{c) } \left[\begin{array}{ccc|c} 1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array}\right]",
                    font_size=32,
                ),
                Text("Si es compatible, da la solución.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: clasifica cada uno de estos sistemas, compatible determinado, indeterminado o incompatible, mirando solo su matriz reducida. Si es compatible, da la solución. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Pivote en la columna de b: incompatible.",
                "Si no, un pivote en cada columna de incógnitas: una solución; si no, infinitas.",
                "Parámetros = n − r (incógnitas menos pivotes).",
            ],
            "Lección 33 — Gauss frente a Gauss-Jordan.",
            voz="En resumen: un pivote en la columna de be significa que el sistema es incompatible. Si no, un pivote en cada columna de incógnitas da una única solución, y si no, infinitas, con ene menos erre parámetros. Siguiente: lección treinta y tres, Gauss frente a Gauss-Jordan.",
        )
