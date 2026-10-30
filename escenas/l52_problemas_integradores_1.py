"""Lección 52 — Problemas integradores I (numéricos).

Escenas (un video cada una):
    ProblemaMezclas, ProblemaRotonda, ProblemaVariosLadosDerechos, ProblemaParabola

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l52_problemas_integradores_1.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, ejes_iguales, escalera, matriz, matriz_gauss, panel_derecha, parrafo, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


class ProblemaMezclas(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 52 · Problema 1", "Una mezcla de tres piensos")
        titulo = self.encabezado("Planteamiento")
        datos = VGroup(
            parrafo(r"Por kilo, cada pienso aporta (en unidades de 100 g):", font_size=36, sangria=0.0),
            parrafo(r"pienso 1: proteínas 1, grasas 2, fibra 1", font_size=34, sangria=0.4),
            parrafo(r"pienso 2: proteínas 2, grasas 1, fibra 1", font_size=34, sangria=0.4),
            parrafo(r"pienso 3: proteínas 1, grasas 3, fibra 2", font_size=34, sangria=0.4),
            parrafo(r"Se quiere una mezcla con proteínas 8, grasas 11 y fibra 7.", r"¿Cuántos kilos de cada pienso?", font_size=36, sangria=0.4, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(titulo, DOWN, buff=0.4).to_edge(LEFT, buff=0.7)
        sistema = sistema_con_llave(("x + 2y + z", "=", "8"), ("2x + y + 3z", "=", "11"), ("x + y + 2z", "=", "7"), font_size=40).next_to(datos, DOWN, buff=0.45).align_to(datos, LEFT).shift(RIGHT * 0.6)
        nota = Tex(r"$x, y, z$: kilos de cada pienso.", font_size=34, color=COLOR_SECUNDARIO).next_to(sistema, RIGHT, buff=0.9)
        ajustar_al_encuadre(VGroup(datos, sistema, nota), margen=0.5)
        self.decir("Primer problema integrador. Tres piensos aportan, por kilo, proteínas, grasas y fibra, con las cantidades de la tabla. Se quiere una mezcla con ocho unidades de proteínas, once de grasas y siete de fibra. ¿Cuántos kilos de cada pienso?")
        self.play(FadeIn(datos))
        self.decir("Se llama equis, y, zeta a los kilos de cada pienso. Cada rasgo da una ecuación: las proteínas, equis más dos y más zeta igual a ocho; las grasas, dos equis más y más tres zeta igual a once; la fibra, equis más y más dos zeta igual a siete.")
        self.play(FadeIn(sistema), FadeIn(nota))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Resolución por Gauss")
        m = matriz_gauss([[1, 2, 1, 8], [2, 1, 3, 11], [1, 1, 2, 7]], pivotes=[(0, 0)]).move_to(LEFT * 3.6 + UP * 0.7)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Escalonamos la matriz aumentada. A la fila dos le restamos dos veces la fila uno, y a la fila tres, la fila uno.")
        self.play(FadeIn(m), FadeIn(historial))
        m = self.operar_filas(m, ("sumar", 1, 0, -2), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 0, -1), historial=historial)
        self.decir("Ahora el candidato a pivote de la columna dos, menos tres, haría fracciones. Es más cómodo intercambiar las filas dos y tres, que tiene un menos uno, y después restar a la fila tres tres veces la fila dos.")
        m = self.operar_filas(m, ("intercambio", 1, 2), historial=historial, pivotes=[(0, 0), (1, 1)])
        m = self.operar_filas(m, ("sumar", 2, 1, -3), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        self.play(Create(escalera(m, [(0, 0), (1, 1), (2, 2)])))
        atras = VGroup(
            MathTex(r"-2z = -2 \Rightarrow z = 1", font_size=40),
            MathTex(r"-y + z = -1 \Rightarrow y = 2", font_size=40),
            MathTex(r"x + 2y + z = 8 \Rightarrow x = 3", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(m, DOWN, buff=0.5)
        ajustar_al_encuadre(VGroup(m, atras), margen=0.5)
        self.decir("La última fila dice menos dos zeta igual a menos dos: zeta vale uno. La segunda, menos y más zeta igual a menos uno: y vale dos. Y la primera da equis igual a tres.")
        for linea in atras:
            self.play(FadeIn(linea))
            self.wait(1.2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificar e interpretar")
        comprobacion = VGroup(
            MathTex(r"3 + 2\cdot 2 + 1 = 8", font_size=44),
            MathTex(r"2\cdot 3 + 2 + 3\cdot 1 = 11", font_size=44),
            MathTex(r"3 + 2 + 2\cdot 1 = 7", font_size=44),
            Tex(r"Hay que mezclar \textbf{3 kg} del pienso 1, \textbf{2 kg} del 2 y \textbf{1 kg} del 3.", font_size=40, color=COLOR_SOLUCION),
            Tex(r"Las tres cantidades son positivas: la mezcla es posible.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.4).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(comprobacion, margen=0.5)
        self.decir("Verificamos en el sistema original. Las tres ecuaciones se cumplen. Hay que mezclar tres kilos del primer pienso, dos del segundo y uno del tercero. Y como las tres cantidades son positivas, la mezcla es posible; si alguna saliera negativa, el problema no tendría solución real.")
        for c in comprobacion:
            self.play(FadeIn(c))
            self.wait(1.6)
        self.wait(1)

        self.ejercicio_propuesto(
            "F15-N3-11",
            Text("Resuelve el problema de mezclas F15-N3-11 del banco\n(otras cantidades, el mismo planteamiento).", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: resuelve el problema de mezclas del banco, con otras cantidades pero el mismo planteamiento. Pausa el video e inténtalo; la solución está en el solucionario.",
        )
        self.resumen(
            [
                "Una incógnita por producto, una ecuación por rasgo.",
                "Gauss, con intercambio de filas si evita fracciones.",
                "Verificar y mirar si las cantidades tienen sentido.",
            ],
            "un problema con infinitas soluciones: una rotonda.",
            voz="En resumen: una incógnita por producto y una ecuación por rasgo. Se resuelve con Gauss, intercambiando filas si así se evitan fracciones. Y se verifica, mirando también que las cantidades tengan sentido. Siguiente: un problema con infinitas soluciones, una rotonda.",
        )


class ProblemaRotonda(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 52 · Problema 2", "El flujo de una rotonda")
        titulo = self.encabezado("Planteamiento")
        colores = [COLOR_COEFICIENTE, COLOR_TERMINO_INDEP, COLOR_PIVOTE, COLOR_SOLUCION]
        centro = LEFT * 4.2 + DOWN * 0.2
        arcos = VGroup(*[Arc(radius=1.6, start_angle=k * PI / 2, angle=PI / 2, color=colores[k], stroke_width=9, arc_center=centro) for k in range(4)])
        etiquetas_arco = VGroup(*[MathTex(f"x_{k + 1}", font_size=40, color=colores[k]).move_to(centro + 2.1 * np.array([np.cos((k + 0.5) * PI / 2), np.sin((k + 0.5) * PI / 2), 0])) for k in range(4)])
        nodos = VGroup(*[Dot(centro + 1.6 * np.array([np.cos(k * PI / 2), np.sin(k * PI / 2), 0]), color=WHITE) for k in range(4)])
        totales = [6, 7, 8, 7]  # nodo en 0°, 90°, 180°, 270°
        rotulos_nodo = VGroup(*[MathTex(str(v), font_size=34, color=COLOR_SECUNDARIO).move_to(centro + 2.15 * np.array([np.cos(k * PI / 2), np.sin(k * PI / 2), 0]) + (RIGHT * 0.25 if k == 0 else (LEFT * 0.25 if k == 2 else ORIGIN))) for k, v in enumerate(totales)])
        sistema = sistema_con_llave(("x_1 + x_2", "=", "7"), ("x_2 + x_3", "=", "8"), ("x_3 + x_4", "=", "7"), ("x_4 + x_1", "=", "6"), font_size=40).to_edge(RIGHT, buff=1.2).shift(UP * 0.4)
        nota = Tex(r"$x_i$: vehículos por minuto en cada tramo.", font_size=34, color=COLOR_SECUNDARIO).next_to(sistema, DOWN, buff=0.5)
        ajustar_al_encuadre(nota, margen=0.5)
        self.decir("Segundo problema. Una rotonda tiene cuatro tramos, con equis uno, equis dos, equis tres y equis cuatro vehículos por minuto. En cada cruce se mide la suma de los dos tramos que se juntan: siete, ocho, siete y seis.")
        self.play(Create(arcos), FadeIn(etiquetas_arco), FadeIn(nodos), FadeIn(rotulos_nodo))
        self.decir("Cada cruce da una ecuación. Son cuatro ecuaciones con cuatro incógnitas.")
        self.play(FadeIn(sistema), FadeIn(nota))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Resolución")
        m = matriz_gauss([[1, 1, 0, 0, 7], [0, 1, 1, 0, 8], [0, 0, 1, 1, 7], [1, 0, 0, 1, 6]], pivotes=[(0, 0)], escala=0.85).move_to(LEFT * 3.6 + UP * 0.6)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Escalonamos. A la fila cuatro le restamos la fila uno; después le sumamos la fila dos; y por último le restamos la fila tres.")
        self.play(FadeIn(m), FadeIn(historial))
        m = self.operar_filas(m, ("sumar", 3, 0, -1), historial=historial, pivotes=[(0, 0)])
        m = self.operar_filas(m, ("sumar", 3, 1, 1), historial=historial, pivotes=[(0, 0), (1, 1)])
        m = self.operar_filas(m, ("sumar", 3, 2, -1), historial=historial, pivotes=[(0, 0), (1, 1), (2, 2)])
        self.play(Create(escalera(m, [(0, 0), (1, 1), (2, 2)])))
        nota2 = Tex(r"Rango 3 con 4 incógnitas: $x_4 = s$ es libre; la última fila es $0 = 0$.", font_size=36, color=COLOR_LIBRE).next_to(m, DOWN, buff=0.5).set_x(0)
        ajustar_al_encuadre(VGroup(m, nota2), margen=0.5)
        self.decir("La cuarta fila queda de ceros: el rango es tres, con cuatro incógnitas. Equis cuatro es libre, y la rotonda tiene infinitas soluciones.")
        self.play(FadeIn(nota2))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "La solución general y su sentido")
        general = VGroup(
            MathTex(r"x_4 = s,\quad x_3 = 7 - s,\quad x_2 = 1 + s,\quad x_1 = 6 - s", font_size=44),
            MathTex(r"\mathbf{x} = (6, 1, 7, 0) + s\,(-1, 1, -1, 1)", font_size=48, color=COLOR_PIVOTE),
            Tex(r"Ningún flujo puede ser negativo: $6 - s \ge 0$, $1 + s \ge 0$, $7 - s \ge 0$, $s \ge 0$.", font_size=38),
            MathTex(r"0 \le s \le 6", font_size=52, color=COLOR_SOLUCION),
            Tex(r"Por ejemplo $s = 4$ da $(2, 5, 3, 4)$; los extremos $s = 0$ y $s = 6$ dan $(6,1,7,0)$ y $(0,7,1,6)$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(general, margen=0.5)
        self.decir("Despejando desde abajo: equis cuatro es ese; equis tres, siete menos ese; equis dos, uno más ese; equis uno, seis menos ese. En forma vectorial, una solución particular, seis, uno, siete, cero, más ese por el vector menos uno, uno, menos uno, uno, que genera el núcleo. Ahora el sentido físico: ningún flujo puede ser negativo, así que ese está entre cero y seis. Con ese igual a cuatro sale dos, cinco, tres, cuatro; y los extremos son seis, uno, siete, cero y cero, siete, uno, seis.")
        for g in general:
            self.play(FadeIn(g))
            self.wait(2.4)
        self.wait(1)

        self.ejercicio_propuesto(
            "F15-N4-19",
            Text("Resuelve el problema de la rotonda F15-N4-19 del banco\ny halla el intervalo admisible del parámetro.", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: resuelve el problema de la rotonda del banco y halla el intervalo en que puede variar el parámetro. Pausa el video e inténtalo; la solución está en el solucionario.",
        )
        self.resumen(
            [
                "Un nodo, una ecuación: balance de lo que entra y sale.",
                "Rango menor que n: infinitas soluciones, con parámetro.",
                "Las restricciones físicas (flujos no negativos) acotan el parámetro.",
            ],
            "varios lados derechos con la misma matriz: la factorización LU.",
            voz="En resumen: cada nodo da una ecuación de balance. Si el rango es menor que el número de incógnitas hay infinitas soluciones, con un parámetro. Y las restricciones físicas, como que los flujos no sean negativos, acotan ese parámetro. Siguiente: varios lados derechos con la misma matriz, la factorización L U.",
        )


class ProblemaVariosLadosDerechos(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 52 · Problema 3", "La misma matriz, varios lados derechos")
        titulo = self.encabezado("Una factorización, muchos usos")
        datos = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 3 & 1 \\ -1 & 1 & 2 \end{bmatrix} = \underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix}}_{L}\underbrace{\begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 10 \end{bmatrix}}_{U}", font_size=40),
            Tex(r"Resolver $A\mathbf{x} = \mathbf{b}$ para $\mathbf{b}_1 = (-3, 1, 2)$ y para $\mathbf{b}_2 = (1, 5, 0)$.", font_size=38),
            Tex(r"La factorización ya está hecha; cada lado derecho solo pide dos sustituciones.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.55).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(datos, margen=0.5)
        self.decir("Tercer problema. Tenemos la matriz de las lecciones treinta y cinco y treinta y seis, ya factorizada como ele por u. Hay que resolver el sistema para dos lados derechos distintos. La factorización ya está hecha: cada lado derecho solo pide dos sustituciones.")
        for d in datos:
            self.play(FadeIn(d))
            self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Para b2 = (1, 5, 0)")
        adelante = VGroup(
            Tex(r"Hacia adelante, $L\mathbf{y} = \mathbf{b}_2$:", font_size=40, color=COLOR_SECUNDARIO),
            MathTex(r"y_1 = 1,\quad y_2 = 5 - 2\cdot 1 = 3,\quad y_3 = 0 + 1 + 3\cdot 3 = 10", font_size=42),
            Tex(r"Hacia atrás, $U\mathbf{x} = \mathbf{y}$:", font_size=40, color=COLOR_SECUNDARIO),
            MathTex(r"10z = 10 \Rightarrow z = 1;\quad -y + 3z = 3 \Rightarrow y = 0;\quad x + 2y - z = 1 \Rightarrow x = 2", font_size=36),
            MathTex(r"\mathbf{x} = (2, 0, 1)", font_size=56, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.55)
        ajustar_al_encuadre(adelante, margen=0.5)
        self.decir("Para el segundo lado derecho, uno, cinco, cero. Primero ele y igual a be: y uno vale uno; y dos es cinco menos dos por uno, tres; y tres es cero más uno, más tres por tres, diez. Ahora u equis igual a y, hacia atrás: diez zeta igual a diez, zeta vale uno; menos y más tres zeta igual a tres, y vale cero; y equis más dos y menos zeta igual a uno, equis vale dos. La solución es dos, cero, uno.")
        for a in adelante:
            self.play(FadeIn(a))
            self.wait(2.4)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Comprobar y comparar el coste")
        final = VGroup(
            MathTex(r"A\mathbf{x} = \begin{bmatrix} 2 + 0 - 1 \\ 4 + 0 + 1 \\ -2 + 0 + 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ 0 \end{bmatrix} = \mathbf{b}_2 \ \checkmark", font_size=44),
            Tex(r"Para $\mathbf{b}_1$ salió $\mathbf{x} = (1, -1, 2)$ (L36), con la misma $L$ y $U$.", font_size=36),
            Tex(r"Coste: factorizar una vez $\approx n^3/3$; cada $\mathbf{b}$, solo $n^2$ (dos sustituciones).", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Con 1000 lados derechos y $n = 100$: Gauss cada vez $\approx 3{,}3\cdot 10^8$ operaciones; $LU$, $\approx 1{,}3\cdot 10^7$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(final, margen=0.5)
        self.decir("Comprobamos: a por equis da uno, cinco, cero, que es be dos. Para el primer lado derecho salió uno, menos uno, dos, con las mismas ele y u. Y el coste: factorizar cuesta del orden de ene cubo entre tres, una sola vez; cada lado derecho, solo ene cuadrado. Con mil lados derechos y una matriz de cien por cien, repetir Gauss cuesta unos trescientos treinta millones de operaciones; con ele u, unos trece millones.")
        for f in final:
            self.play(FadeIn(f))
            self.wait(2.4)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N3-19",
            Text("Resuelve con LU el sistema A x = b del ejercicio F10-N3-19\ndel banco (parte 2 de F10).", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: resuelve con la factorización L U un sistema del banco de ejercicios. Pausa el video e inténtalo; la solución está en el solucionario.",
        )
        self.resumen(
            [
                "Con la misma A, factoriza una vez.",
                "Cada b: L y = b hacia adelante, U x = y hacia atrás.",
                "Coste por lado derecho: n² (frente a ≈ n³/3 de Gauss).",
            ],
            "interpolación: ajustar una parábola a tres puntos.",
            voz="En resumen: con la misma matriz, se factoriza una vez. Cada lado derecho se resuelve con dos sustituciones, y cuesta ene cuadrado, en lugar de unas ene cubo entre tres. Siguiente: interpolación, ajustar una parábola a tres puntos.",
        )


class ProblemaParabola(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 52 · Problema 4", "Una parábola por tres puntos")
        titulo = self.encabezado("Las incógnitas son los coeficientes")
        ejes = ejes_iguales((-3, 5), (-2, 8), unidad=0.55).to_edge(LEFT, buff=0.7).shift(DOWN * 0.3)
        puntos = [(-1, 6), (1, 0), (2, 3)]
        marcas = VGroup(*[Dot(ejes.c2p(x, y), color=COLOR_PIVOTE, radius=0.09) for x, y in puntos])
        rotulos = VGroup(*[MathTex(f"({x}, {y})", font_size=30, color=COLOR_PIVOTE).next_to(ejes.c2p(x, y), UR if x != 1 else DR, buff=0.12) for x, y in puntos])
        texto = VGroup(
            Tex(r"Hallar $y = c_0 + c_1x + c_2x^2$ por", font_size=36),
            Tex(r"$(-1, 6)$, $(1, 0)$ y $(2, 3)$.", font_size=36, color=COLOR_PIVOTE),
            Tex(r"Cada punto es una ecuación en $c_0, c_1, c_2$:", font_size=36, color=COLOR_SECUNDARIO),
            MathTex(r"\begin{cases} c_0 - c_1 + c_2 = 6 \\ c_0 + c_1 + c_2 = 0 \\ c_0 + 2c_1 + 4c_2 = 3 \end{cases}", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(RIGHT, buff=0.7).shift(DOWN * 0.1)
        ajustar_al_encuadre(texto, margen=0.5)
        self.decir("Cuarto problema. Queremos la parábola y igual a ce cero más ce uno equis más ce dos equis cuadrado que pasa por los puntos menos uno, seis; uno, cero; y dos, tres. Aquí las incógnitas no son equis ni y, sino los coeficientes de la parábola.")
        self.play(Create(ejes), FadeIn(marcas), FadeIn(rotulos))
        self.decir("Cada punto da una ecuación. Sustituimos: en menos uno, ce cero menos ce uno más ce dos igual a seis; en uno, ce cero más ce uno más ce dos igual a cero; y en dos, ce cero más dos ce uno más cuatro ce dos igual a tres.")
        self.play(FadeIn(texto))
        self.wait(3)
        self.limpiar(titulo)

        m = matriz_gauss([[1, -1, 1, 6], [1, 1, 1, 0], [1, 2, 4, 3]], pivotes=[(0, 0)], escala=0.85).move_to(LEFT * 3.4 + UP * 0.9)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.6)
        self.decir("Escalonamos con dos operaciones: a las filas dos y tres les restamos la fila uno.")
        self.play(FadeIn(m), FadeIn(historial))
        m = self.operar_filas(m, ("sumar", 1, 0, -1), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 0, -1), historial=historial, pivotes=[(0, 0), (1, 1)])
        lecturas = VGroup(
            MathTex(r"2c_1 = -6 \Rightarrow c_1 = -3", font_size=40),
            MathTex(r"3c_1 + 3c_2 = -3 \Rightarrow c_2 = 2", font_size=40),
            MathTex(r"c_0 - c_1 + c_2 = 6 \Rightarrow c_0 = 1", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(m, DOWN, buff=0.5)
        self.decir("La segunda fila dice dos ce uno igual a menos seis: ce uno vale menos tres. La tercera, tres ce uno más tres ce dos igual a menos tres: ce dos vale dos. Y la primera da ce cero igual a uno.")
        for linea in lecturas:
            self.play(FadeIn(linea))
            self.wait(1.4)
        self.wait(1)
        resultado = MathTex(r"y = 1 - 3x + 2x^2", font_size=56, color=COLOR_SOLUCION).to_edge(RIGHT, buff=0.8).shift(UP * 0.2)
        verificacion = VGroup(
            Tex(r"Comprobación: $x=-1$: $1+3+2 = 6$,", font_size=34),
            Tex(r"$x=1$: $1-3+2 = 0$, $\;x=2$: $1-6+8 = 3$.", font_size=34),
            Tex(r"$2x^2 - 3x + 1 = (2x - 1)(x - 1)$: corta el eje $x$ en $\tfrac12$ y $1$.", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(resultado, DOWN, buff=0.5).align_to(resultado, LEFT)
        panel_derecha(VGroup(resultado, verificacion), ancho=6.3, buff=0.5)
        self.decir("La parábola es y igual a uno menos tres equis más dos equis cuadrado. Comprobamos los tres puntos. Y factorizando, dos equis menos uno por equis menos uno, vemos que corta el eje equis en un medio y en uno.")
        self.play(Write(resultado))
        self.play(FadeIn(verificacion))
        self.wait(3)
        self.limpiar()

        titulo = self.encabezado("La parábola pasa por los tres puntos")
        ejes2 = ejes_iguales((-3, 5), (-2, 8), unidad=0.62).move_to(DOWN * 0.3)
        curva = ejes2.plot(lambda x: 2 * x * x - 3 * x + 1, x_range=[-1.3, 2.5], color=COLOR_SOLUCION, stroke_width=5)
        marcas2 = VGroup(*[Dot(ejes2.c2p(x, y), color=COLOR_PIVOTE, radius=0.1) for x, y in puntos])
        self.decir("Dibujada, la parábola pasa por los tres puntos. Tres puntos con abscisas distintas determinan una única parábola, porque la matriz del sistema, de Vandermonde, es invertible.")
        self.play(Create(ejes2), FadeIn(marcas2))
        self.play(Create(curva), run_time=2.5)
        self.wait(3)

        self.ejercicio_propuesto(
            "F15-N3-13",
            Text("Halla la parábola del ejercicio F15-N3-13 del banco\n(otros tres puntos, el mismo planteamiento).", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: halla la parábola del ejercicio del banco, con otros tres puntos pero el mismo planteamiento. Pausa el video e inténtalo; la solución está en el solucionario.",
        )
        self.resumen(
            [
                "En interpolación, las incógnitas son los coeficientes.",
                "Cada punto da una ecuación lineal en ellos.",
                "Tres abscisas distintas: sistema compatible determinado.",
            ],
            "Lección 53 — parámetros y estructura.",
            voz="En resumen: en interpolación, las incógnitas son los coeficientes. Cada punto da una ecuación lineal en ellos. Y con tres abscisas distintas el sistema es compatible determinado. Siguiente: lección cincuenta y tres, parámetros y estructura.",
        )
