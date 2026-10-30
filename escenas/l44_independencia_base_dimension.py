"""Lección 44 — Independencia lineal, base y dimensión.

Escenas (un video cada una):
    DependenciaLineal, ComoComprobarIndependencia, BaseYDimension

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l44_independencia_base_dimension.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import panel_derecha, EscenaCurso, ajustar_al_encuadre, ejes_iguales, escalera, flecha, matriz, matriz_gauss, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

COLOR_U, COLOR_V, COLOR_W = COLORES_ECUACIONES


def columna(*componentes, color=WHITE, font_size=40) -> MathTex:
    filas = r" \\ ".join(str(c) for c in componentes)
    return MathTex(r"\begin{bmatrix} " + filas + r" \end{bmatrix}", font_size=font_size, color=color)


def plano_vectores(x_range=(-4, 6), y_range=(-3, 5)) -> Axes:
    return ejes_iguales(x_range, y_range, unidad=0.72).to_edge(LEFT, buff=0.5).shift(DOWN * 0.35)


class DependenciaLineal(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 44 · Parte 1", "Dependencia e independencia lineal")
        titulo = self.encabezado("¿Sobra algún vector?")
        p = plano_vectores()
        u, v = flecha(p, 1, 2, COLOR_U), flecha(p, 2, 4, COLOR_V)
        relacion = MathTex(r"2\,\mathbf{u} - 1\,\mathbf{v} = \mathbf{0}", font_size=50, color=COLOR_PIVOTE)
        nota = Tex(r"$\mathbf{v}$ es múltiplo de $\mathbf{u}$:", font_size=38)
        panel = VGroup(nota, relacion, Tex(r"\textbf{dependientes}", font_size=44, color=COLOR_ERROR)).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.7).shift(UP * 1.0)
        panel_derecha(panel)
        ajustar_al_encuadre(panel, margen=0.5)
        self.decir("Vamos a medir si en una lista de vectores alguno sobra. Estos dos, u igual a uno, dos y ve igual a dos, cuatro, apuntan en la misma dirección. Ve es el doble de u, así que no aporta nada nuevo: dos veces u menos una vez ve da el vector nulo.")
        self.play(Create(p))
        self.play(GrowArrow(u), GrowArrow(v))
        self.play(FadeIn(panel[0]), Write(panel[1]))
        self.play(FadeIn(panel[2]))
        self.wait(2)
        self.limpiar(titulo)

        p2 = plano_vectores()
        a, b = flecha(p2, 1, 2, COLOR_U), flecha(p2, 2, 1, COLOR_V)
        independiente = VGroup(
            Tex(r"Direcciones distintas:", font_size=38),
            MathTex(r"c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{0} \;\Rightarrow\; c_1 = c_2 = 0", font_size=42, color=COLOR_PIVOTE),
            Tex(r"\textbf{independientes}", font_size=44, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.45).to_edge(RIGHT, buff=0.6).shift(UP * 1.0)
        panel_derecha(independiente)
        ajustar_al_encuadre(independiente, margen=0.5)
        self.decir("Estos otros dos vectores, uno, dos y dos, uno, apuntan en direcciones distintas. La única forma de combinarlos para obtener el vector nulo es con los dos coeficientes iguales a cero: son independientes.")
        self.play(Create(p2))
        self.play(GrowArrow(a), GrowArrow(b))
        self.play(FadeIn(independiente[0]), Write(independiente[1]))
        self.play(FadeIn(independiente[2]))
        self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definición")
        definicion = VGroup(
            parrafo(r"Los vectores $\mathbf{v}_1, \dots, \mathbf{v}_k$ son \textbf{linealmente independientes} si", r"la única solución de la ecuación siguiente es la trivial:", font_size=38, sangria=0.5),
            MathTex(r"c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots + c_k\mathbf{v}_k = \mathbf{0} \;\Longrightarrow\; c_1 = c_2 = \dots = c_k = 0", font_size=40, color=COLOR_PIVOTE),
            parrafo(r"Si existe una solución con algún $c_i \ne 0$, son \textbf{dependientes}:", r"alguno es combinación lineal de los demás.", font_size=38, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(definicion, margen=0.5)
        self.decir("Los vectores ve uno, hasta ve ka, son linealmente independientes si la única solución de esta ecuación es la trivial, todos los coeficientes cero. Si existe alguna solución con algún coeficiente distinto de cero, son dependientes, y entonces alguno de ellos es combinación lineal de los demás.")
        for d in definicion:
            self.play(FadeIn(d))
            self.wait(2.5)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Tres consecuencias que conviene recordar")
        hechos = VGroup(
            parrafo(r"Un conjunto que contiene al vector nulo es siempre \textbf{dependiente}.", r"($1\cdot\mathbf{0} = \mathbf{0}$ es una combinación no trivial.)", font_size=36, sangria=0.5),
            parrafo(r"Dos vectores son dependientes si y solo si uno es múltiplo del otro.", font_size=36, sangria=0.5),
            parrafo(r"Más de $n$ vectores en $\mathbb{R}^n$ son siempre \textbf{dependientes}.", r"(Se verá en la siguiente escena, por rangos.)", font_size=36, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(hechos, margen=0.5)
        self.decir("Tres consecuencias que conviene recordar. Un conjunto que contiene al vector nulo siempre es dependiente. Dos vectores son dependientes exactamente cuando uno es múltiplo del otro. Y más de ene vectores en el espacio de ene dimensiones siempre son dependientes; lo veremos enseguida, con rangos.")
        for h in hechos:
            self.play(FadeIn(h))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F12-N2-03",
            VGroup(
                Text("¿Son linealmente independientes? Si no, da una relación entre ellos.", font_size=TAM_TEXTO),
                MathTex(r"\mathbf{u} = \begin{bmatrix} 1 \\ 2 \end{bmatrix},\quad \mathbf{v} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: decide si estos dos vectores son linealmente independientes, y si no lo son, da una relación entre ellos. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Independientes: c₁v₁ + … + ckvk = 0 solo con todos los ci = 0.",
                "Dependientes: alguno sobra (es combinación de los demás).",
                "Con el vector nulo, o con más de n vectores en ℝⁿ, siempre dependientes.",
            ],
            "cómo comprobarlo con un sistema homogéneo.",
            voz="En resumen: son independientes si la única combinación que da el vector nulo es la trivial; son dependientes si alguno sobra. Con el vector nulo, o con más de ene vectores en el espacio de ene dimensiones, son siempre dependientes. Siguiente: cómo comprobarlo con un sistema homogéneo.",
        )


class ComoComprobarIndependencia(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 44 · Parte 2", "Cómo comprobar la independencia")
        titulo = self.encabezado("Reducir a un sistema homogéneo")
        vectores = VGroup(
            columna(1, 2, 1, color=COLOR_U, font_size=44),
            columna(0, 1, 1, color=COLOR_V, font_size=44),
            columna(1, 4, 3, color=COLOR_W, font_size=44),
        ).arrange(RIGHT, buff=0.9)
        etiquetas = VGroup(*[MathTex(t, font_size=40, color=c) for t, c in zip((r"\mathbf{u}", r"\mathbf{v}", r"\mathbf{w}"), COLORES_ECUACIONES)])
        for e, vec in zip(etiquetas, vectores):
            e.next_to(vec, UP, buff=0.25)
        bloque = VGroup(vectores, etiquetas).next_to(titulo, DOWN, buff=0.8)
        ecuacion = MathTex(r"c_1\mathbf{u} + c_2\mathbf{v} + c_3\mathbf{w} = \mathbf{0}", font_size=50, color=COLOR_PIVOTE).next_to(bloque, DOWN, buff=0.7)
        self.decir("Para decidir si unos vectores son independientes, escribimos la ecuación que define la independencia. Tomemos tres vectores de tres componentes: u, ve y uve doble. La ecuación es ce uno u, más ce dos ve, más ce tres uve doble, igual al vector nulo.")
        self.play(FadeIn(bloque))
        self.play(Write(ecuacion))
        self.wait(2)
        self.limpiar(titulo)

        m = matriz_gauss([[1, 0, 1, 0], [2, 1, 4, 0], [1, 1, 3, 0]], pivotes=[(0, 0)]).move_to(LEFT * 3.4 + UP * 0.4)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Es un sistema homogéneo cuya matriz tiene a los vectores por columnas. Lo escalonamos. A la fila dos le restamos dos veces la fila uno, y a la fila tres, la fila uno.")
        self.play(FadeIn(m), FadeIn(historial))
        m = self.operar_filas(m, ("sumar", 1, 0, -2), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 0, -1), historial=historial)
        self.decir("Ahora, a la fila tres le restamos la fila dos. La última fila queda de ceros.")
        m = self.operar_filas(m, ("sumar", 2, 1, -1), historial=historial, pivotes=[(0, 0), (1, 1)])
        self.play(Create(escalera(m, [(0, 0), (1, 1)])))
        self.wait(1)
        nota = VGroup(
            Tex(r"Hay una columna sin pivote $\Rightarrow$ $c_3$ es libre", font_size=40, color=COLOR_LIBRE),
            MathTex(r"c_3 = t:\quad c_1 = -t,\ c_2 = -2t", font_size=44),
            MathTex(r"-\mathbf{u} - 2\mathbf{v} + \mathbf{w} = \mathbf{0}\ \Rightarrow\ \mathbf{w} = \mathbf{u} + 2\mathbf{v}", font_size=44, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.4).next_to(m, DOWN, buff=0.5).set_x(0)
        ajustar_al_encuadre(nota, margen=0.5)
        self.decir("La tercera columna no tiene pivote, así que el coeficiente ce tres es libre. Tomando ce tres igual a te, salen ce uno igual a menos te, y ce dos igual a menos dos te. Hay soluciones distintas de cero: son dependientes. Con te igual a uno, uve doble es u más dos ve.")
        for n in nota:
            self.play(FadeIn(n))
            self.wait(1.5)
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "El criterio")
        criterio = VGroup(
            Tex(r"Sea $V = [\,\mathbf{v}_1 \ \cdots \ \mathbf{v}_k\,]$ la matriz con los vectores por columnas.", font_size=38),
            MathTex(r"\mathbf{v}_1, \dots, \mathbf{v}_k \text{ independientes} \iff V\mathbf{c} = \mathbf{0} \text{ solo tiene } \mathbf{c} = \mathbf{0}", font_size=40, color=COLOR_PIVOTE),
            MathTex(r"\iff \operatorname{rg}(V) = k \quad (\text{todas las columnas con pivote})", font_size=44),
            Tex(r"En $\mathbb{R}^n$: con $k > n$ vectores, $\operatorname{rg}(V) \le n < k$, luego son dependientes.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(criterio, margen=0.5)
        self.decir("Resumiendo el método. Sea ve la matriz con los vectores por columnas. Los vectores son independientes si y solo si el sistema ve por ce igual a cero solo tiene la solución trivial; esto equivale a que el rango de ve sea igual al número de vectores, es decir, que todas las columnas tengan pivote. Y si hay más vectores que componentes, el rango no puede llegar al número de vectores, así que son dependientes.")
        for c in criterio:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F12-N3-01",
            VGroup(
                Text("Decide si son independientes; si no, da una relación:", font_size=TAM_TEXTO),
                MathTex(r"\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix},\ \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix},\ \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: decide si estos tres vectores son independientes, y si no, da una relación entre ellos. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Matriz V con los vectores por columnas.",
                "Independientes ⇔ rg(V) = número de vectores.",
                "Si hay columna sin pivote, su variable libre da una relación.",
            ],
            "base y dimensión.",
            voz="En resumen: se forma la matriz con los vectores por columnas. Son independientes exactamente cuando el rango es igual al número de vectores. Y si hay una columna sin pivote, su variable libre da una relación de dependencia. Siguiente: base y dimensión.",
        )


class BaseYDimension(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 44 · Parte 3", "Base y dimensión")
        titulo = self.encabezado("Una base: lo justo para generar")
        p = plano_vectores()
        e1, e2 = flecha(p, 1, 0, COLOR_U), flecha(p, 0, 1, COLOR_V)
        d1, d2 = flecha(p, 1, 1, COLOR_W), flecha(p, 1, -1, COLOR_PIVOTE)
        p_punto = Dot(p.c2p(3, 1), color=COLOR_SOLUCION)
        coord_a = MathTex(r"(3,1) = 3\,\mathbf{e}_1 + 1\,\mathbf{e}_2", font_size=40).to_edge(RIGHT, buff=0.7).shift(UP * 1.8)
        panel_derecha(coord_a)
        coord_b = MathTex(r"(3,1) = 2\,(1,1) + 1\,(1,-1)", font_size=40, color=COLOR_PIVOTE).next_to(coord_a, DOWN, buff=0.5)
        panel_derecha(VGroup(coord_a, coord_b))
        self.decir("Una base es un conjunto de vectores que genera todo el espacio sin tener ninguno de sobra. En el plano, los vectores e uno y e dos, uno cero y cero uno, son una base. Con ellos, el punto tres, uno se escribe de una única manera: tres e uno más uno e dos.")
        self.play(Create(p))
        self.play(GrowArrow(e1), GrowArrow(e2), FadeIn(p_punto, scale=2))
        self.play(Write(coord_a))
        self.wait(1.5)
        self.decir("Pero también los vectores uno, uno y uno, menos uno forman una base. Con ellos, el mismo punto es dos veces el primero más una vez el segundo. Hay muchas bases, pero en cada una las coordenadas de un vector son únicas.")
        self.play(GrowArrow(d1), GrowArrow(d2))
        self.play(Write(coord_b))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Definiciones")
        definiciones = VGroup(
            parrafo(r"$\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ es una \textbf{base} de un subespacio $S$ si:", r"1) es linealmente independiente;  2) genera $S$.", font_size=38, sangria=0.5),
            parrafo(r"Todo vector de $S$ se escribe de \textbf{una única manera} como combinación", r"lineal de la base (sus \textbf{coordenadas}).", font_size=38, sangria=0.5),
            parrafo(r"Todas las bases de $S$ tienen el mismo número de vectores:", r"es la \textbf{dimensión} de $S$, $\dim S$.", font_size=38, sangria=0.5),
            MathTex(r"\dim \mathbb{R}^n = n \qquad \dim\{\mathbf{0}\} = 0", font_size=48, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(definiciones, margen=0.5)
        self.decir("Una base de un subespacio es un conjunto de vectores que cumple dos cosas: es linealmente independiente, y genera el subespacio. Entonces todo vector del subespacio se escribe de una única manera como combinación de la base; esos coeficientes son sus coordenadas. Todas las bases de un mismo subespacio tienen el mismo número de vectores: ese número es la dimensión. El espacio de ene dimensiones tiene dimensión ene, y el subespacio que solo contiene el vector nulo, dimensión cero.")
        for d in definiciones:
            self.play(FadeIn(d))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Una base se puede extraer de un generador")
        m = matriz([[1, 2, 0, 1], [2, 4, 1, 4], [1, 2, 1, 3]]).scale(0.9).to_edge(LEFT, buff=0.9).shift(UP * 0.2)
        reducida = matriz([[1, 2, 0, 1], [0, 0, 1, 2], [0, 0, 0, 0]]).scale(0.9).next_to(m, RIGHT, buff=1.4)
        for i, j in [(0, 0), (1, 2)]:
            reducida.get_rows()[i][j].set_color(COLOR_PIVOTE)
        for fila in m.get_rows():
            fila[0].set_color(COLOR_PIVOTE)
            fila[2].set_color(COLOR_PIVOTE)
        flecha_r = MathTex(r"\longrightarrow", font_size=48).move_to((m.get_right() + reducida.get_left()) / 2)
        texto = VGroup(
            Tex(r"Pivotes en las columnas 1 y 3:", font_size=38, color=COLOR_PIVOTE),
            Tex(r"base de $\operatorname{gen}\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3, \mathbf{a}_4\}$ $=$ $\{\mathbf{a}_1, \mathbf{a}_3\}$, dimensión $2$.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(VGroup(m, reducida), DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(m, reducida, texto), margen=0.5)
        self.decir("Para quedarnos con una base a partir de unos vectores que generan, ponemos los vectores por columnas y escalonamos. Los vectores de las columnas con pivote, en la matriz original, son una base de lo que generan. Aquí, las columnas uno y tres: la dimensión es dos. Por qué hay que tomar las columnas de la matriz original lo veremos en la lección cuarenta y nueve.")
        self.play(FadeIn(m))
        self.play(Write(flecha_r), FadeIn(reducida))
        self.play(FadeIn(texto))
        self.wait(3)

        self.ejercicio_propuesto(
            "F12-N4-01",
            VGroup(
                Text("Halla una base y la dimensión del espacio generado por las columnas de:", font_size=TAM_TEXTO),
                MathTex(r"\begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: halla una base y la dimensión del espacio generado por las columnas de esta matriz. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Base: independiente y generadora.",
                "Las coordenadas respecto de una base son únicas.",
                "Todas las bases tienen el mismo número de vectores: la dimensión.",
            ],
            "Lección 45 — el núcleo de una matriz.",
            voz="En resumen: una base es un conjunto independiente que genera. Las coordenadas respecto de una base son únicas. Y todas las bases tienen el mismo número de vectores: la dimensión. Siguiente: lección cuarenta y cinco, el núcleo de una matriz.",
        )
