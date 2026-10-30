"""Lección 36 — Resolver con LU.

Escenas (un video cada una):
    SustitucionHaciaAdelanteLy, SustitucionHaciaAtrasUx, EjemploCompletoLU

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l36_resolver_con_lu.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

LA = r"\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix}"
UA = r"\begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 10 \end{bmatrix}"


class SustitucionHaciaAdelanteLy(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 36 · Parte 1", "Resolver con LU: primero L y = b")
        titulo = self.encabezado("Dos sistemas triangulares en lugar de uno")
        cadena = VGroup(
            MathTex(r"A\mathbf{x} = \mathbf{b}", font_size=56),
            MathTex(r"L\,U\,\mathbf{x} = \mathbf{b}", font_size=56),
            MathTex(r"L\,\mathbf{y} = \mathbf{b}\quad\text{y}\quad U\,\mathbf{x} = \mathbf{y}", font_size=56, color=COLOR_PIVOTE),
        ).arrange(DOWN, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        nota = Tex(r"Llamamos $\mathbf{y} = U\mathbf{x}$: así $L(U\mathbf{x}) = L\mathbf{y} = \mathbf{b}$.", font_size=38, color=COLOR_SECUNDARIO).next_to(cadena, DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(cadena, nota), margen=0.5)
        self.decir("Para resolver a equis igual a be, si a es ele por u, sustituimos: ele, u, equis, igual a be. Llamamos ye al producto u por equis. Entonces el problema se parte en dos sistemas triangulares: primero, ele ye igual a be; después, u equis igual a ye.")
        self.play(Write(cadena[0]))
        self.play(Write(cadena[1]))
        self.play(Write(cadena[2]))
        self.play(FadeIn(nota))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Primero: L y = b, hacia adelante")
        sistema = MathTex(r"\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix}\begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = \begin{bmatrix} -3 \\ 1 \\ 2 \end{bmatrix}", font_size=46).to_edge(LEFT, buff=0.8).shift(UP * 0.6)
        pasos = VGroup(
            MathTex(r"y_1 = -3", font_size=40),
            MathTex(r"2y_1 + y_2 = 1 \;\Rightarrow\; y_2 = 1 - 2(-3) = 7", font_size=40),
            MathTex(r"-y_1 - 3y_2 + y_3 = 2 \;\Rightarrow\; y_3 = 2 + (-3) + 21 = 20", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(sistema, RIGHT, buff=0.7)
        ajustar_al_encuadre(VGroup(sistema, pasos), margen=0.5)
        self.decir("Tomemos el ele del ejemplo de la lección treinta y cinco, y be igual a menos tres, uno, dos. Como ele es triangular inferior con unos en la diagonal, sustituimos hacia adelante. La primera fila dice: ye uno es menos tres.")
        self.play(Write(sistema))
        self.play(Write(pasos[0]))
        self.decir("La segunda: dos ye uno más ye dos igual a uno. Ye dos vale uno menos dos por menos tres: siete. Y la tercera: menos ye uno, menos tres ye dos, más ye tres, igual a dos. Ye tres vale veinte.")
        self.play(Write(pasos[1]))
        self.play(Write(pasos[2]))
        y = MathTex(r"\mathbf{y} = (-3,\ 7,\ 20)", font_size=46, color=COLOR_SOLUCION).next_to(pasos, DOWN, buff=0.7)
        self.play(Write(y))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "¿Qué es y?")
        conexion = VGroup(
            Tex(r"En la eliminación de la L26, la columna $\mathbf{b}$ de la matriz aumentada acabó siendo", font_size=36),
            MathTex(r"\left[\begin{array}{ccc|c} 1 & 2 & -1 & -3 \\ 0 & -1 & 3 & 7 \\ 0 & 0 & 10 & 20 \end{array}\right]", font_size=44),
            Tex(r"es decir, $(-3,\ 7,\ 20) = \mathbf{y}$: \textbf{$\mathbf{y}$ es $\mathbf{b}$ después de la eliminación}.", font_size=36, color=COLOR_PIVOTE),
            Tex(r"$L\mathbf{y} = \mathbf{b}$ rehace la eliminación sobre $\mathbf{b}$ sin tocar $A$.", font_size=36, color=COLOR_OPERACION),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(conexion, margen=0.5)
        self.decir("¿Y qué es ye? Es la columna de be después de la eliminación. En la lección veintiséis, la matriz aumentada terminó con menos tres, siete, veinte en la última columna: es el mismo ye. Resolver ele ye igual a be es rehacer la eliminación sobre be, sin volver a tocar a.")
        for c in conexion:
            self.play(FadeIn(c))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N2-04",
            VGroup(
                Text("Resuelve L y = b por sustitución hacia adelante:", font_size=TAM_TEXTO),
                MathTex(r"\begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 3 \\ 13 \end{bmatrix}", font_size=52),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: resuelve este sistema, ele ye igual a be, por sustitución hacia adelante. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "A x = b con A = L U se parte en L y = b y U x = y.",
                "L y = b se resuelve hacia adelante.",
                "y es b después de la eliminación.",
            ],
            "U x = y, hacia atrás.",
            voz="En resumen: a equis igual a be, con a igual a ele u, se parte en ele ye igual a be, y u equis igual a ye. El primero se resuelve hacia adelante, y ye es la columna be después de la eliminación. Siguiente: u equis igual a ye, hacia atrás.",
        )


class SustitucionHaciaAtrasUx(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 36 · Parte 2", "Después: U x = y")
        titulo = self.encabezado("Segundo: U x = y, hacia atrás")
        sistema = MathTex(UA + r"\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} -3 \\ 7 \\ 20 \end{bmatrix}", font_size=46).to_edge(LEFT, buff=0.8).shift(UP * 0.6)
        pasos = VGroup(
            MathTex(r"10z = 20 \;\Rightarrow\; z = 2", font_size=40),
            MathTex(r"-y + 3z = 7 \;\Rightarrow\; y = 3\cdot 2 - 7 = -1", font_size=40),
            MathTex(r"x + 2y - z = -3 \;\Rightarrow\; x = -3 + 2 + 2 = 1", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(sistema, RIGHT, buff=0.7)
        ajustar_al_encuadre(VGroup(sistema, pasos), margen=0.5)
        self.decir("Ahora resolvemos u equis igual a ye, con el ye que acabamos de calcular: menos tres, siete, veinte. Como u es triangular superior, sustituimos hacia atrás. La última fila dice diez zeta igual a veinte: zeta vale dos.")
        self.play(Write(sistema))
        self.play(Write(pasos[0]))
        self.decir("La segunda: menos ye más tres zeta igual a siete. Ye vale seis menos siete: menos uno. Y la primera: equis más dos ye menos zeta igual a menos tres. Equis vale menos tres, más dos, más dos: uno.")
        self.play(Write(pasos[1]))
        self.play(Write(pasos[2]))
        solucion = MathTex(r"\mathbf{x} = (1,\ -1,\ 2)", font_size=48, color=COLOR_SOLUCION).next_to(pasos, DOWN, buff=0.7)
        self.play(Write(solucion))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Verificar en el sistema original")
        verif = VGroup(
            MathTex(r"A\mathbf{x} = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 3 & 1 \\ -1 & 1 & 2 \end{bmatrix}\begin{bmatrix} 1 \\ -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 - 2 - 2 \\ 2 - 3 + 2 \\ -1 - 1 + 4 \end{bmatrix} = \begin{bmatrix} -3 \\ 1 \\ 2 \end{bmatrix} = \mathbf{b}\ \checkmark", font_size=42, color=COLOR_SOLUCION),
            Tex(r"Es la misma solución que dio Gauss en la L26.", font_size=38, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.7).next_to(titulo, DOWN, buff=0.8)
        ajustar_al_encuadre(verif, margen=0.5)
        self.decir("Y siempre verificamos en el sistema original: a por la solución da menos tres, uno, dos, que es be. Es la misma solución que obtuvimos con Gauss en la lección veintiséis.")
        self.play(Write(verif[0]))
        self.play(FadeIn(verif[1]))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cuánto cuesta cada parte")
        costes = VGroup(
            Tex(r"$L\mathbf{y} = \mathbf{b}$ (unos en la diagonal): $\frac{n(n-1)}{2}$ multiplicaciones.", font_size=38),
            Tex(r"$U\mathbf{x} = \mathbf{y}$: $\frac{n(n+1)}{2}$ multiplicaciones y divisiones.", font_size=38),
            Tex(r"Total por cada $\mathbf{b}$: $n^2$. Factorizar $A$ cuesta $\frac{n^3 - n}{3}$, \textbf{una sola vez}.", font_size=38, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(costes, margen=0.5)
        self.decir("Los costes. El sistema con ele, que tiene unos en la diagonal, cuesta ene por ene menos uno, entre dos multiplicaciones. El de u, ene por ene más uno, entre dos. En total, ene cuadrado por cada be. Factorizar a cuesta ene cubo menos ene, entre tres, pero solo una vez.")
        for c in costes:
            self.play(FadeIn(c))
            self.wait(2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F10-N3-03",
            VGroup(
                Text("Con L y U de la lección, resuelve A x = b para b = (0, 1, −3):", font_size=TAM_TEXTO),
                MathTex(r"L = " + LA + r",\quad U = " + UA, font_size=36),
                Text("Resuelve L y = b, después U x = y, y verifica en el original.", font_size=TAM_NOTA),
            ).arrange(DOWN, buff=0.5),
            voz="Ejercicio propuesto: con ele y u de la lección, resuelve a equis igual a be, para be igual a cero, uno, menos tres. Resuelve primero ele ye igual a be, después u equis igual a ye, y verifica en el sistema original. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "U x = y se resuelve hacia atrás, con el y de L y = b.",
                "Siempre se verifica en el A original.",
                "Cada b nueva cuesta n² operaciones; factorizar A, una sola vez.",
            ],
            "un ejemplo completo de principio a fin.",
            voz="En resumen: u equis igual a ye se resuelve hacia atrás, con el ye de ele ye igual a be. Siempre se verifica en la matriz a original. Y cada be nueva cuesta ene cuadrado operaciones, mientras que factorizar a se hace una sola vez. Siguiente: un ejemplo completo de principio a fin.",
        )


class EjemploCompletoLU(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 36 · Parte 3", "Un ejemplo completo")
        titulo = self.encabezado("Paso 1: factorizar A")
        sistema = MathTex(r"\begin{cases} 2x + y + z = 5 \\ 4x - 6y = -2 \\ -2x + 7y + 2z = 9 \end{cases}", font_size=44).to_edge(LEFT, buff=0.9).shift(UP * 0.6)
        multiplicadores = VGroup(
            MathTex(r"R_2 \leftarrow R_2 - 2R_1:\quad m_{21} = 2", font_size=36, color=COLOR_OPERACION),
            MathTex(r"R_3 \leftarrow R_3 + R_1:\quad m_{31} = -1", font_size=36, color=COLOR_OPERACION),
            MathTex(r"R_3 \leftarrow R_3 + R_2:\quad m_{32} = -1", font_size=36, color=COLOR_OPERACION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(sistema, RIGHT, buff=0.9)
        lu = MathTex(
            r"L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix},\qquad U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 0 & 1 \end{bmatrix}",
            font_size=40,
        )
        VGroup(sistema, multiplicadores).arrange(RIGHT, buff=0.9).next_to(titulo, DOWN, buff=0.5)
        lu.next_to(VGroup(sistema, multiplicadores), DOWN, buff=0.6)
        ajustar_al_encuadre(VGroup(sistema, multiplicadores, lu), margen=0.5)
        self.decir("Un ejemplo completo. Este sistema tiene la matriz de coeficientes dos, uno, uno; cuatro, menos seis, cero; menos dos, siete, dos. Primero factorizamos. A la fila dos le restamos dos veces la fila uno: el multiplicador es dos. A la fila tres le sumamos la fila uno: menos uno. Y a la fila tres le sumamos la fila dos: menos uno.")
        self.play(Write(sistema))
        for mult in multiplicadores:
            self.play(FadeIn(mult))
            self.wait(1)
        self.decir("Con ellos, ele tiene un dos, un menos uno y un menos uno bajo la diagonal. Y u es la matriz escalonada que queda: dos, uno, uno; cero, menos ocho, menos dos; cero, cero, uno.")
        self.play(Write(lu))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Paso 2: L y = b")
        ly = VGroup(
            MathTex(r"\mathbf{b} = (5,\ -2,\ 9)", font_size=40),
            MathTex(r"y_1 = 5", font_size=40),
            MathTex(r"2\cdot 5 + y_2 = -2 \;\Rightarrow\; y_2 = -12", font_size=40),
            MathTex(r"-5 - (-12) + y_3 = 9 \;\Rightarrow\; y_3 = 2", font_size=40),
            MathTex(r"\mathbf{y} = (5,\ -12,\ 2)", font_size=44, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(ly, margen=0.5)
        self.decir("Segundo paso: ele ye igual a be, con be igual a cinco, menos dos, nueve. Ye uno vale cinco. Dos por cinco más ye dos igual a menos dos: ye dos vale menos doce. Y menos cinco, más doce, más ye tres, igual a nueve: ye tres vale dos.")
        for linea in ly:
            self.play(Write(linea))
            self.wait(1)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Paso 3: U x = y")
        ux = VGroup(
            MathTex(r"z = 2", font_size=40),
            MathTex(r"-8y - 2\cdot 2 = -12 \;\Rightarrow\; y = 1", font_size=40),
            MathTex(r"2x + 1 + 2 = 5 \;\Rightarrow\; x = 1", font_size=40),
            MathTex(r"\mathbf{x} = (1,\ 1,\ 2)", font_size=44, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(ux, margen=0.5)
        self.decir("Tercer paso: u equis igual a ye, hacia atrás. Zeta vale dos. Menos ocho ye menos cuatro igual a menos doce: ye vale uno. Y dos equis más uno más dos igual a cinco: equis vale uno.")
        for linea in ux:
            self.play(Write(linea))
            self.wait(1)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Paso 4: verificar en el original")
        verif = VGroup(
            MathTex(r"2(1) + 1 + 2 = 5\ \checkmark", font_size=44),
            MathTex(r"4(1) - 6(1) + 0 = -2\ \checkmark", font_size=44),
            MathTex(r"-2(1) + 7(1) + 2(2) = 9\ \checkmark", font_size=44),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.8)
        verif.set_color(COLOR_SOLUCION)
        resumen_pasos = Tex(r"Factorizar $\to$ $L\mathbf{y} = \mathbf{b}$ $\to$ $U\mathbf{x} = \mathbf{y}$ $\to$ verificar.", font_size=40, color=COLOR_PIVOTE).next_to(verif, DOWN, buff=0.8)
        ajustar_al_encuadre(VGroup(verif, resumen_pasos), margen=0.5)
        self.decir("Cuarto paso, verificar en el sistema original: dos más uno más dos, cinco; cuatro menos seis, menos dos; menos dos, más siete, más cuatro, nueve. Todo correcto.")
        for v in verif:
            self.play(Write(v))
            self.wait(1)
        self.decir("El proceso completo: factorizar, resolver ele ye igual a be, resolver u equis igual a ye, y verificar.")
        self.play(FadeIn(resumen_pasos))
        self.wait(2)

        self.ejercicio_propuesto(
            "F10-N4-02",
            VGroup(
                Text("Para n = 3, cuenta las multiplicaciones y divisiones de:", font_size=TAM_TEXTO),
                Text("a) factorizar A (sin contar b); b) resolver L y = b y U x = y.", font_size=TAM_NOTA + 2),
                Text("Comprueba que, sumadas, dan lo mismo que Gauss en un solo sistema (17).", font_size=TAM_NOTA + 2),
            ).arrange(DOWN, buff=0.4),
            voz="Ejercicio propuesto: para tres incógnitas, cuenta las multiplicaciones y divisiones de factorizar a, sin contar be, y de resolver los dos sistemas triangulares. Comprueba que, sumadas, dan lo mismo que Gauss en un solo sistema: diecisiete. Pausa el video e inténtalo; la solución está en el banco de ejercicios.",
        )
        self.resumen(
            [
                "Factorizar A = L U una vez, anotando los multiplicadores.",
                "Resolver L y = b (adelante) y U x = y (atrás).",
                "Verificar siempre en el sistema original.",
            ],
            "Lección 37 — cuando LU falla: permutaciones.",
            voz="En resumen: se factoriza a igual a ele u una sola vez, anotando los multiplicadores. Después se resuelve ele ye igual a be, hacia adelante, y u equis igual a ye, hacia atrás. Y siempre se verifica en el sistema original. Siguiente: lección treinta y siete, cuando ele u falla: permutaciones.",
        )
