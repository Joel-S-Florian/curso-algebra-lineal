"""Lección 53 — Problemas integradores II (parámetros y estructura).

Escenas (un video cada una):
    ProblemaConParametro, ProblemaNucleoEImagen, VerdaderoOFalso

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l53_problemas_integradores_2.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, escalera, matriz, matriz_gauss, parrafo, sistema_con_llave  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

A_TEX = r"\begin{bmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 1 & 2 & 1 & 3 \end{bmatrix}"


class ProblemaConParametro(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 53 · Problema 5", "Un sistema con un parámetro")
        titulo = self.encabezado("Discutir según a")
        sistema = sistema_con_llave(("x + y + az", "=", "1"), ("x + ay + z", "=", "1"), ("ax + y + z", "=", "1"), font_size=48).shift(UP * 0.8)
        pregunta = Tex(r"¿Cuántas soluciones tiene según el valor de $a$? Resuélvelo en cada caso.", font_size=38).next_to(sistema, DOWN, buff=0.8)
        ajustar_al_encuadre(VGroup(sistema, pregunta), margen=0.5)
        self.decir("Quinto problema. Este sistema de tres ecuaciones con tres incógnitas tiene un parámetro, a. Hay que decir cuántas soluciones tiene según el valor de a, y resolverlo en cada caso.")
        self.play(FadeIn(sistema))
        self.play(FadeIn(pregunta))
        self.wait(2)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Los valores críticos")
        det = VGroup(
            MathTex(r"\det\begin{bmatrix} 1 & 1 & a \\ 1 & a & 1 \\ a & 1 & 1 \end{bmatrix} = -(a - 1)^2(a + 2)", font_size=46),
            Tex(r"Se anula solo en $a = 1$ y en $a = -2$.", font_size=40, color=COLOR_PIVOTE),
            Tex(r"Si $a \ne 1, -2$: $\operatorname{rg}(A) = 3 = n$ y la solución es única.", font_size=38),
            MathTex(r"x = y = z = \dfrac{1}{a + 2}", font_size=54, color=COLOR_SOLUCION),
            Tex(r"(Comprobación: $\frac{1}{a+2}\,(1 + 1 + a) = 1$.)", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(det, margen=0.5)
        self.decir("El determinante de la matriz de coeficientes es menos a menos uno al cuadrado, por a más dos. Solo se anula si a vale uno o menos dos. Para cualquier otro valor, el rango es tres, igual al número de incógnitas, y la solución es única. Por la simetría del sistema, equis, y y zeta valen lo mismo: uno entre a más dos. Se comprueba: uno entre a más dos, por uno más uno más a, da uno.")
        for d in det:
            self.play(FadeIn(d))
            self.wait(2.2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Caso a = 1")
        caso1 = VGroup(
            Tex(r"Las tres ecuaciones son la misma: $x + y + z = 1$.", font_size=40),
            MathTex(r"\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 1 < 3", font_size=44, color=COLOR_PIVOTE),
            Tex(r"Compatible indeterminado, con $3 - 1 = 2$ parámetros libres.", font_size=38),
            MathTex(r"(x, y, z) = (1, 0, 0) + s\,(-1, 1, 0) + t\,(-1, 0, 1)", font_size=48, color=COLOR_SOLUCION),
            Tex(r"Es un plano: la solución particular más el núcleo, de dimensión 2.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(caso1, margen=0.5)
        self.decir("Si a vale uno, las tres ecuaciones son la misma: equis más y más zeta igual a uno. Los dos rangos valen uno, menos que tres: es compatible indeterminado, con dos parámetros libres. La solución general es una solución particular, uno, cero, cero, más ese por menos uno, uno, cero, más te por menos uno, cero, uno: un plano.")
        for c in caso1:
            self.play(FadeIn(c))
            self.wait(2.2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Caso a = −2")
        m = matriz_gauss([[1, 1, -2, 1], [1, -2, 1, 1], [-2, 1, 1, 1]], pivotes=[(0, 0)]).move_to(LEFT * 3.6 + UP * 0.7)
        historial = VGroup(Text("Operaciones", font_size=TAM_NOTA, color=COLOR_SECUNDARIO)).move_to(RIGHT * 4.9 + UP * 2.2)
        self.decir("Si a vale menos dos, escalonamos. A la fila dos le restamos la fila uno; a la fila tres le sumamos dos veces la fila uno; y después, a la fila tres le sumamos la fila dos.")
        self.play(FadeIn(m), FadeIn(historial))
        m = self.operar_filas(m, ("sumar", 1, 0, -1), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 0, 2), historial=historial)
        m = self.operar_filas(m, ("sumar", 2, 1, 1), historial=historial, pivotes=[(0, 0), (1, 1)])
        conclusion = VGroup(
            Tex(r"Última fila: $[\,0\ \ 0\ \ 0 \mid 3\,]$, es decir, $0 = 3$.", font_size=40, color=COLOR_ERROR),
            Tex(r"$\operatorname{rg}(A) = 2 < \operatorname{rg}[A \mid \mathbf{b}] = 3$: incompatible.", font_size=40),
        ).arrange(DOWN, buff=0.4).next_to(m, DOWN, buff=0.5).set_x(0)
        ajustar_al_encuadre(VGroup(m, conclusion), margen=0.5)
        self.decir("La última fila queda cero, cero, cero, tres: la ecuación cero igual a tres, imposible. El rango de a es dos y el de la aumentada, tres: el sistema es incompatible. Se ve también sumando las tres ecuaciones: el miembro izquierdo se anula y el derecho vale tres.")
        for c in conclusion:
            self.play(FadeIn(c))
            self.wait(1.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Resumen de la discusión")
        filas = [
            ("a distinto de 1 y de −2", "3", "3", "solución única, x = y = z = 1/(a + 2)"),
            ("a = 1", "1", "1", "infinitas (plano, 2 parámetros)"),
            ("a = −2", "2", "3", "sin solución"),
        ]
        tabla = VGroup(*[Text(h, font_size=TAM_NOTA, weight="BOLD", color=COLOR_SECUNDARIO) for h in ("Valor de a", "rg(A)", "rg[A|b]", "Resultado")])
        for fila in filas:
            for j, texto in enumerate(fila):
                tabla.add(Text(texto, font_size=TAM_NOTA, weight="BOLD" if j == 0 else "NORMAL", color=COLOR_PIVOTE if j == 3 else WHITE))
        tabla.arrange_in_grid(rows=4, cols=4, buff=(0.6, 0.5), col_alignments="llll").next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(tabla, margen=0.5)
        self.decir("Resumen de la discusión. Si a no es uno ni menos dos, los dos rangos valen tres: solución única. Si a es uno, los dos rangos valen uno: infinitas soluciones. Y si a es menos dos, el rango de a es dos y el de la aumentada, tres: sin solución.")
        self.play(FadeIn(tabla[:4]))
        self.play(FadeIn(tabla[4:8]))
        self.play(FadeIn(tabla[8:12]))
        self.play(FadeIn(tabla[12:]))
        self.wait(3)

        self.ejercicio_propuesto(
            "F15-N5-11",
            Text("Discute y resuelve el sistema con parámetro F15-N5-11 del banco,\nincluyendo la base del núcleo en el caso indeterminado.", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: discute y resuelve el sistema con parámetro del banco, incluyendo una base del núcleo en el caso indeterminado. Pausa el video e inténtalo; la solución está en el solucionario.",
        )
        self.resumen(
            [
                "Los valores críticos anulan el determinante.",
                "En cada valor crítico, comparar rg(A) y rg[A | b].",
                "Si hay infinitas soluciones: particular + núcleo.",
            ],
            "un problema completo con núcleo y espacio columna.",
            voz="En resumen: los valores críticos son los que anulan el determinante. En cada uno se comparan los rangos de a y de la aumentada. Y cuando hay infinitas soluciones, se escribe la solución particular más el núcleo. Siguiente: un problema completo con núcleo y espacio columna.",
        )


class ProblemaNucleoEImagen(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 53 · Problema 6", "Núcleo, imagen y solución")
        titulo = self.encabezado("Todo sobre una misma matriz")
        enunciado = VGroup(
            MathTex(r"A = " + A_TEX + r",\qquad \mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix}", font_size=44),
            parrafo(r"a) Reduce y halla $\operatorname{rg}(A)$.    b) Resuelve $A\mathbf{x} = \mathbf{b}$.", r"c) Base de $\ker A$.    d) Base de $\operatorname{Col}(A)$; ¿está $\mathbf{b}$ en ella?", r"e) ¿Tiene solución para $\mathbf{b}' = (1, 0, 0)$?", font_size=36, sangria=0.0),
        ).arrange(DOWN, buff=0.6).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(enunciado, margen=0.5)
        self.decir("Sexto problema: una misma matriz de tres por cuatro y un vector be. Hay que reducir y hallar el rango, resolver, dar una base del núcleo, una base del espacio columna y decir si be está en él, y decidir si hay solución para otro lado derecho, uno, cero, cero.")
        for e in enunciado:
            self.play(FadeIn(e))
            self.wait(2.5)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "a) y b): reducir")
        reducida = matriz_gauss([[1, 2, 0, 1, 1], [0, 0, 1, 2, 1], [0, 0, 0, 0, 0]], pivotes=[(0, 0), (1, 2)], escala=0.9).move_to(LEFT * 3.4 + UP * 0.7)
        despeje = VGroup(
            MathTex(r"x_1 = 1 - 2x_2 - x_4", font_size=42),
            MathTex(r"x_3 = 1 - 2x_4", font_size=42),
            MathTex(r"x_2 = s,\ x_4 = t", font_size=42, color=COLOR_LIBRE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(reducida, RIGHT, buff=1.3)
        conclusion = VGroup(
            Tex(r"$\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 2 < 4$: compatible indeterminado.", font_size=38),
            MathTex(r"\mathbf{x} = (1, 0, 1, 0) + s\,(-2, 1, 0, 0) + t\,(-1, 0, -2, 1)", font_size=44, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.4).next_to(reducida, DOWN, buff=0.6).set_x(0)
        ajustar_al_encuadre(VGroup(reducida, despeje, conclusion), margen=0.5)
        self.decir("Tras reducir, aparecen pivotes en las columnas uno y tres, y una fila de ceros: el rango de a y el de la aumentada valen dos, menos que cuatro. Es compatible indeterminado, con dos parámetros. Despejando, equis uno es uno menos dos equis dos menos equis cuatro, y equis tres, uno menos dos equis cuatro. La solución general es la particular, uno, cero, uno, cero, más ese por un vector, más te por otro.")
        self.play(FadeIn(reducida))
        self.play(Create(escalera(reducida, [(0, 0), (1, 2)])))
        self.play(FadeIn(despeje))
        self.play(FadeIn(conclusion[0]))
        self.play(Write(conclusion[1]))
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "c), d) y e)")
        respuestas = VGroup(
            parrafo(r"\textbf{c)} Base de $\ker A$: $\{(-2, 1, 0, 0),\ (-1, 0, -2, 1)\}$; $\operatorname{nul}(A) = 2$.", font_size=36, sangria=0.4),
            parrafo(r"\textbf{d)} Base de $\operatorname{Col}(A)$ (columnas pivote de la original): $\{(1, 2, 1),\ (0, 1, 1)\}$.", r"$\mathbf{b} = (1, 3, 2) = \mathbf{a}_1 + \mathbf{a}_3 \in \operatorname{Col}(A)$: coherente con b).", font_size=36, sangria=0.4),
            parrafo(r"\textbf{e)} Para $\mathbf{b}' = (1, 0, 0)$: $\operatorname{rg}(A) = 2$ pero $\operatorname{rg}[A \mid \mathbf{b}'] = 3$: incompatible.", r"$\mathbf{b}' \notin \operatorname{Col}(A)$.", font_size=36, sangria=0.4, color=COLOR_ERROR),
            MathTex(r"\operatorname{rg}(A) + \operatorname{nul}(A) = 2 + 2 = 4 = n \ \checkmark", font_size=46, color=COLOR_PIVOTE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(respuestas, margen=0.5)
        self.decir("Para el núcleo, una base son los vectores de las variables libres: menos dos, uno, cero, cero; y menos uno, cero, menos dos, uno. La nulidad es dos. Para el espacio columna, las columnas uno y tres de la matriz original; y be es la columna uno más la columna tres, así que está en él, lo que concuerda con que haya solución. Con be prima igual a uno, cero, cero, el rango de la aumentada sube a tres: no está en el espacio columna y el sistema es incompatible. Y se comprueba el teorema: dos más dos es cuatro.")
        for r_ in respuestas:
            self.play(FadeIn(r_))
            self.wait(3)
        self.wait(1)

        self.ejercicio_propuesto(
            "F15-N4-11",
            Text("Haz la ficha completa de la matriz del ejercicio F15-N4-11 del banco:\nrango, solución, núcleo, espacio columna y rango + nulidad.", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: haz la ficha completa de la matriz del ejercicio del banco: rango, solución, núcleo, espacio columna, y la comprobación de rango más nulidad. Pausa el video e inténtalo; la solución está en el solucionario.",
        )
        self.resumen(
            [
                "Una sola reducción contesta rango, solución, núcleo y columnas pivote.",
                "Todo es coherente: b en Col(A) ⇔ hay solución.",
                "rg + nul = n sirve de comprobación final.",
            ],
            "verdadero o falso, con contraejemplos.",
            voz="En resumen: una sola reducción contesta el rango, la solución, el núcleo y las columnas pivote. Todo es coherente: be está en el espacio columna exactamente cuando hay solución. Y rango más nulidad igual a ene sirve de comprobación final. Siguiente: verdadero o falso, con contraejemplos.",
        )


class VerdaderoOFalso(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 53 · Problema 7", "Verdadero o falso")
        titulo = self.encabezado("Una afirmación general se prueba; una falsa se refuta con un ejemplo")
        self.decir("Séptimo problema. Tres afirmaciones, y hay que decidir si son verdaderas o falsas. Para una afirmación general verdadera hace falta una demostración. Para una falsa basta un contraejemplo pequeño.")
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Afirmación 1")
        a1 = VGroup(
            Tex(r"«Un sistema con 2 ecuaciones y 3 incógnitas siempre tiene infinitas soluciones.»", font_size=38),
            Tex(r"\textbf{Falso.}", font_size=48, color=COLOR_ERROR),
            MathTex(r"\begin{cases} x + y + z = 1 \\ x + y + z = 2 \end{cases}", font_size=48),
            Tex(r"No tiene solución: $\operatorname{rg}(A) = 1 < \operatorname{rg}[A \mid \mathbf{b}] = 2$.", font_size=38),
            Tex(r"Menos ecuaciones que incógnitas da libertad \emph{si es compatible}.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(a1, margen=0.5)
        self.decir("Primera: un sistema con dos ecuaciones y tres incógnitas siempre tiene infinitas soluciones. Es falsa. Basta tomar equis más y más zeta igual a uno, y equis más y más zeta igual a dos: no tiene solución, porque el rango de a es uno y el de la aumentada, dos. Tener menos ecuaciones que incógnitas da libertad solo si el sistema es compatible.")
        for x in a1:
            self.play(FadeIn(x))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Afirmación 2")
        a2 = VGroup(
            Tex(r"«Si $A$ es $4\times 3$ y $\operatorname{rg}(A) = 3$, entonces $A\mathbf{x} = \mathbf{b}$ tiene solución para todo $\mathbf{b}$.»", font_size=36),
            Tex(r"\textbf{Falso.}", font_size=48, color=COLOR_ERROR),
            MathTex(r"A = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 1 & 1 \end{bmatrix},\quad \mathbf{b} = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 0 \end{bmatrix}", font_size=44),
            Tex(r"Las tres primeras filas dan $x = y = z = 1$, pero la cuarta pide $x + y + z = 0$.", font_size=36),
            Tex(r"Para tener solución $\forall\,\mathbf{b}$ hace falta $\operatorname{rg}(A) = m = 4$, y aquí $\operatorname{rg} \le 3$.", font_size=36, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.4).next_to(titulo, DOWN, buff=0.5)
        ajustar_al_encuadre(a2, margen=0.5)
        self.decir("Segunda: si a es de cuatro por tres y su rango es tres, entonces a por equis igual a be tiene solución para todo be. También es falsa. En este ejemplo, las tres primeras filas dan equis, y, zeta iguales a uno, pero la cuarta pide que sumen cero. Para tener solución con cualquier be hace falta que el rango sea igual al número de filas, cuatro, y aquí el rango no puede pasar de tres.")
        for x in a2:
            self.play(FadeIn(x))
            self.wait(2)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Afirmación 3")
        a3 = VGroup(
            Tex(r"«Si $\ker A = \{\mathbf{0}\}$, entonces $A\mathbf{x} = \mathbf{b}$ tiene a lo sumo una solución.»", font_size=38),
            Tex(r"\textbf{Verdadero.}", font_size=48, color=COLOR_SOLUCION),
            Tex(r"Si $\mathbf{x}_1$ y $\mathbf{x}_2$ son soluciones, $A(\mathbf{x}_1 - \mathbf{x}_2) = \mathbf{b} - \mathbf{b} = \mathbf{0}$.", font_size=38),
            Tex(r"Luego $\mathbf{x}_1 - \mathbf{x}_2 \in \ker A = \{\mathbf{0}\}$ y $\mathbf{x}_1 = \mathbf{x}_2$. $\qquad\blacksquare$", font_size=38, color=COLOR_PIVOTE),
            Tex(r"(Puede no tener ninguna: ``a lo sumo una'' no es ``siempre una''.)", font_size=34, color=COLOR_SECUNDARIO),
        ).arrange(DOWN, buff=0.45).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(a3, margen=0.5)
        self.decir("Tercera: si el núcleo de a es solo el vector nulo, entonces a por equis igual a be tiene a lo sumo una solución. Es verdadera y se demuestra. Si equis uno y equis dos son soluciones, a por su diferencia es be menos be, cero. Entonces la diferencia está en el núcleo, que solo contiene al cero, y las dos soluciones coinciden. Ojo: puede no tener ninguna; a lo sumo una no significa siempre una.")
        for x in a3:
            self.play(FadeIn(x))
            self.wait(2)
        self.wait(1)

        self.ejercicio_propuesto(
            "F15-N4-23",
            Text("Resuelve los ejercicios de verdadero o falso F15-N4-23 a F15-N4-26\ndel banco: justifica con una demostración o un contraejemplo.", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: resuelve los ejercicios de verdadero o falso del banco, justificando cada respuesta con una demostración o un contraejemplo. Pausa el video e inténtalo; las soluciones están en el solucionario.",
        )
        self.resumen(
            [
                "Falsa: un contraejemplo pequeño basta.",
                "Verdadera: hay que demostrarla con las definiciones.",
                "«A lo sumo una» no es «siempre una».",
            ],
            "Lección 54 — las demostraciones clave del curso.",
            voz="En resumen: para refutar basta un contraejemplo pequeño; para afirmar hay que demostrar con las definiciones; y a lo sumo una solución no es lo mismo que siempre una. Siguiente: lección cincuenta y cuatro, las demostraciones clave del curso.",
        )
