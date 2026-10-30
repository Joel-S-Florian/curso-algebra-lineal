"""Lección 55 — Repaso final.

Escenas (un video cada una):
    MapaConceptual, PruebaIntegradora, LoQueSigue

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l55_repaso_final.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, parrafo  # noqa: E402
from curso.estilo import *  # noqa: E402,F403


def nodo(texto: str, color=WHITE, tam: int = 22, ancho: float = 3.5) -> VGroup:
    t = Text(texto, font_size=tam, line_spacing=1.0, color=color)
    marco = RoundedRectangle(corner_radius=0.15, width=max(ancho, t.width + 0.4), height=t.height + 0.4, color=color, stroke_width=3, fill_color=color, fill_opacity=0.12)
    t.move_to(marco)
    return VGroup(marco, t)


def unir(a: Mobject, b: Mobject, color=COLOR_SECUNDARIO, doble: bool = False) -> Arrow:
    p, q = a.get_bottom(), b.get_top()
    if abs(a.get_center()[1] - b.get_center()[1]) < 0.3:  # misma altura: lado a lado
        p, q = (a.get_right(), b.get_left()) if a.get_x() < b.get_x() else (a.get_left(), b.get_right())
    clase = DoubleArrow if doble else Arrow
    return clase(p, q, buff=0.08, color=color, stroke_width=3, max_tip_length_to_length_ratio=0.15)


class MapaConceptual(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 55 · Parte 1", "El mapa del curso")
        titulo = self.encabezado("Todo gira alrededor de A x = b")
        sistema = nodo("Sistema lineal  A x = b", COLOR_PIVOTE, tam=28, ancho=4.4).move_to(UP * 2.4)
        ops = nodo("Operaciones elementales\nGauss, Gauss-Jordan, LU", COLOR_OPERACION, ancho=4.2).move_to(LEFT * 4.6 + UP * 0.6)
        rango = nodo("Rango\n(número de pivotes)", COLOR_COEFICIENTE, ancho=3.4).move_to(UP * 0.6)
        sub = nodo("Núcleo y\nespacio columna", COLOR_LIBRE, ancho=3.4).move_to(RIGHT * 4.6 + UP * 0.6)
        sol = nodo("Solución\n(o su ausencia)", COLOR_OPERACION, ancho=3.4).move_to(LEFT * 4.6 + DOWN * 1.9)
        rf = nodo("Rouché-Frobenius\nSCD, SCI o SI", COLOR_COEFICIENTE, ancho=3.4).move_to(DOWN * 1.9)
        est = nodo("x = xp + ker A\nrango + nulidad = n", COLOR_LIBRE, ancho=3.8).move_to(RIGHT * 4.6 + DOWN * 1.9)
        self.decir("Este es el mapa del curso. Todo gira alrededor de un sistema lineal, a por equis igual a be.")
        self.play(FadeIn(sistema))
        self.wait(1)

        self.decir("A la izquierda, las operaciones elementales: Gauss, Gauss-Jordan y la factorización L U transforman el sistema sin cambiar sus soluciones, y llevan a la solución, o a comprobar que no la hay.")
        self.play(FadeIn(ops), GrowArrow(unir(sistema, ops)))
        self.play(FadeIn(sol), GrowArrow(unir(ops, sol)))
        self.wait(1.5)

        self.decir("En el centro, el rango: el número de pivotes que dejan esas operaciones. Con él, el teorema de Rouché-Frobenius clasifica el sistema en compatible determinado, indeterminado o incompatible, sin resolverlo.")
        a1 = unir(ops, rango, COLOR_PIVOTE)
        self.play(FadeIn(rango), GrowArrow(unir(sistema, rango)), GrowArrow(a1))
        self.play(FadeIn(rf), GrowArrow(unir(rango, rf)))
        self.wait(1.5)

        self.decir("A la derecha, la estructura: el núcleo, las soluciones del sistema homogéneo, y el espacio columna, lo que se puede alcanzar. Las soluciones son una solución particular más el núcleo, y el rango y la nulidad suman el número de incógnitas.")
        self.play(FadeIn(sub), GrowArrow(unir(sistema, sub)), GrowArrow(unir(rango, sub, COLOR_LIBRE, doble=True)))
        self.play(FadeIn(est), GrowArrow(unir(sub, est)))
        self.wait(2)
        self.pie("Una sola idea recorre todo: los pivotes.", COLOR_PIVOTE, espera=3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Las diez ideas que hay que llevarse")
        ideas = [
            "Una ecuación lineal es una recta, un plano o un hiperplano.",
            "Un sistema tiene 0, 1 o infinitas soluciones.",
            "Las operaciones elementales no cambian las soluciones.",
            "Gauss: escalonar y sustituir hacia atrás.",
            "Gauss-Jordan: reducida y lectura directa.",
            "LU: factorizar una vez, resolver muchas veces.",
            "El rango es el número de pivotes.",
            "Rouché-Frobenius: rg(A) = rg[A | b] y rg = n.",
            "Solución general = particular + núcleo.",
            "rango + nulidad = número de columnas.",
        ]
        lista = VGroup(*[Text(f"{i + 1}. {t}", font_size=25) for i, t in enumerate(ideas)]).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(titulo, DOWN, buff=0.4).to_edge(LEFT, buff=1.2)
        ajustar_al_encuadre(lista, margen=0.5)
        columna_izq, columna_der = list(lista[:5]), list(lista[5:])
        self.decir("Las diez ideas que hay que llevarse. Una: una ecuación lineal es una recta, un plano o un hiperplano. Dos: un sistema tiene cero, una o infinitas soluciones. Tres: las operaciones elementales no cambian las soluciones. Cuatro: Gauss escalona y sustituye hacia atrás. Cinco: Gauss-Jordan da la reducida y la lectura directa.")
        for t in columna_izq:
            self.play(FadeIn(t, shift=RIGHT * 0.15))
            self.wait(0.5)
        self.decir("Seis: con la factorización L U se factoriza una vez y se resuelve muchas veces. Siete: el rango es el número de pivotes. Ocho: Rouché-Frobenius compara los rangos con el número de incógnitas. Nueve: la solución general es una particular más el núcleo. Y diez: rango más nulidad es el número de columnas.")
        for t in columna_der:
            self.play(FadeIn(t, shift=RIGHT * 0.15))
            self.wait(0.5)
        self.wait(3)

        self.ejercicio_propuesto(
            "F15-N4-11",
            Text("Dibuja tu propio mapa del curso en una hoja, con flechas,\ny comprueba cada flecha con un ejemplo de la ficha F15-N4-11.", font_size=TAM_TEXTO, line_spacing=1.2),
            voz="Ejercicio propuesto: dibuja tu propio mapa del curso en una hoja, con flechas, y comprueba cada flecha con un ejemplo. Pausa el video e inténtalo; la ficha del banco te ofrece un ejemplo completo.",
        )
        self.resumen(
            [
                "Sistema, operaciones, rango, núcleo y espacio columna: un solo mapa.",
                "Los pivotes conectan todas las ideas.",
                "Diez ideas esenciales para recordar.",
            ],
            "la prueba final integradora.",
            voz="En resumen: sistema, operaciones, rango, núcleo y espacio columna forman un solo mapa, y los pivotes conectan todas las ideas. Son diez ideas esenciales. Siguiente: la prueba final integradora.",
        )


class PruebaIntegradora(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 55 · Parte 2", "La prueba final integradora")
        titulo = self.encabezado("Diez problemas, cien puntos, dos horas")
        filas = [
            ("1", "Sistema 3×3 por Gauss", "10"),
            ("2", "Gauss-Jordan y solución general", "10"),
            ("3", "Factorización LU, dos lados derechos", "10"),
            ("4", "Sistema con parámetro", "12"),
            ("5", "Rango, núcleo y espacio columna", "12"),
            ("6", "Problema de modelado", "8"),
            ("7", "Verdadero o falso", "8"),
            ("8", "Clasificar sin resolver", "10"),
            ("9", "Una demostración", "10"),
            ("10", "Problema integrador", "10"),
        ]
        tabla = VGroup(*[Text(h, font_size=TAM_NOTA, weight="BOLD", color=COLOR_SECUNDARIO) for h in ("N.º", "Tema", "Puntos")])
        for fila in filas:
            for j, texto in enumerate(fila):
                tabla.add(Text(texto, font_size=TAM_NOTA, weight="BOLD" if j == 0 else "NORMAL", color=COLOR_PIVOTE if j == 2 else WHITE))
        tabla.arrange_in_grid(rows=len(filas) + 1, cols=3, buff=(0.7, 0.3), col_alignments="lll").next_to(titulo, DOWN, buff=0.45)
        ajustar_al_encuadre(tabla, margen=0.5)
        self.decir("La prueba final integradora tiene diez problemas, cien puntos y dos horas. Mezcla todo lo que has visto. Un sistema de tres por tres con Gauss. Gauss-Jordan y la solución general. La factorización L U con dos lados derechos. Un sistema con un parámetro. Rango, núcleo y espacio columna. Un problema de modelado. Verdadero o falso. Clasificar sin resolver. Una demostración. Y un problema integrador.")
        self.play(FadeIn(tabla[:3]))
        for k in range(10):
            self.play(FadeIn(tabla[3 + 3 * k: 6 + 3 * k]), run_time=0.5)
            self.wait(0.6)
        self.wait(3)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Cómo hacerla")
        consejos = VGroup(
            parrafo(r"Hazla en una sola sesión de dos horas, sin apuntes, y \textbf{después} corrige.", font_size=38, sangria=0.4),
            parrafo(r"Empieza por lo que mejor dominas; deja las demostraciones para el final.", font_size=38, sangria=0.4),
            parrafo(r"Verifica cada solución en el sistema original antes de pasar al siguiente problema.", font_size=38, sangria=0.4),
            parrafo(r"Corrige con el solucionario: por cada error, vuelve a la lección y al ejercicio del banco que lo trabaja.", font_size=38, sangria=0.4, color=COLOR_SOLUCION),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(consejos, margen=0.5)
        self.decir("Cómo hacerla. En una sola sesión de dos horas, sin apuntes, y después corrige. Empieza por lo que mejor dominas y deja las demostraciones para el final. Verifica cada solución en el sistema original antes de pasar al siguiente problema. Y corrige con el solucionario: por cada error, vuelve a la lección y al ejercicio del banco que lo trabaja.")
        for c in consejos:
            self.play(FadeIn(c))
            self.wait(2.8)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Dónde está todo")
        donde = VGroup(
            parrafo(r"\texttt{prueba\_final/PRUEBA\_FINAL.md}: los enunciados.", font_size=38, sangria=0.4),
            parrafo(r"\texttt{prueba\_final/SOLUCION\_PRUEBA\_FINAL.md}: soluciones y baremo.", font_size=38, sangria=0.4),
            parrafo(r"\texttt{ejercicios/BANCO.md} y \texttt{solucionario/}: 665 ejercicios con soluciones.", font_size=38, sangria=0.4),
            parrafo(r"\texttt{material/formulario.md} y \texttt{material/metodos.md}: formulario y árbol de decisión.", font_size=38, sangria=0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.7)
        ajustar_al_encuadre(donde, margen=0.5)
        self.decir("Dónde está todo. Los enunciados de la prueba, en la carpeta prueba final. Sus soluciones y el baremo, en el archivo de solución. El banco único y el solucionario, con seiscientos sesenta y cinco ejercicios. Y el formulario y el árbol de decisión, en la carpeta material.")
        for d in donde:
            self.play(FadeIn(d))
            self.wait(2.4)
        self.wait(1)
        self.resumen(
            [
                "Diez problemas, cien puntos, dos horas.",
                "Hazla sin apuntes y corrige con el solucionario.",
                "Cada error te dice qué lección y qué ejercicios repasar.",
            ],
            "lo que viene después del curso.",
            voz="En resumen: diez problemas, cien puntos y dos horas. Hazla sin apuntes y corrige con el solucionario. Y cada error te dice qué lección y qué ejercicios repasar. Siguiente: lo que viene después del curso.",
        )


class LoQueSigue(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 55 · Parte 3", "Lo que sigue")
        titulo = self.encabezado("Lo que has aprendido es el principio del álgebra lineal")
        recorrido = VGroup(
            parrafo(r"\textbf{Inversa y determinante.} Si $A$ es cuadrada con $\operatorname{rg}(A) = n$, existe $A^{-1}$ con $A^{-1}A = I$;", r"se calcula con Gauss-Jordan sobre $[A \mid I]$. El determinante mide el cambio de área o volumen.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{Ortogonalidad y mínimos cuadrados.} Cuando $A\mathbf{x} = \mathbf{b}$ no tiene solución,", r"se busca la mejor aproximación: $A^TA\,\mathbf{x} = A^T\mathbf{b}$.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{Valores y vectores propios.} Direcciones que una matriz solo estira: $A\mathbf{v} = \lambda\mathbf{v}$.", font_size=34, sangria=0.5),
            parrafo(r"\textbf{Descomposiciones.} $QR$, diagonalización, valores singulares: más factorizaciones, la idea de $LU$.", font_size=34, sangria=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.6)
        ajustar_al_encuadre(recorrido, margen=0.5)
        self.decir("Lo que has aprendido es el principio del álgebra lineal. Lo que sigue usa las mismas ideas. La inversa y el determinante: una matriz cuadrada de rango ene tiene inversa, que se calcula con Gauss-Jordan sobre a e identidad. Ortogonalidad y mínimos cuadrados: cuando no hay solución, se busca la mejor aproximación. Valores y vectores propios: las direcciones que una matriz solo estira. Y más descomposiciones, que repiten la idea de la factorización L U.")
        for r_ in recorrido:
            self.play(FadeIn(r_))
            self.wait(3)
        self.wait(1)
        self.limpiar(titulo)

        titulo = self.cambiar_encabezado(titulo, "Para terminar")
        cierre = VGroup(
            Tex(r"Un sistema lineal puede no tener solución, tener una o tener infinitas.", font_size=40),
            Tex(r"Los pivotes lo deciden; el núcleo describe lo que sobra; el espacio columna, lo que se alcanza.", font_size=38, color=COLOR_PIVOTE),
            Tex(r"Resuelve, verifica, interpreta.", font_size=52, color=COLOR_SOLUCION),
        ).arrange(DOWN, buff=0.7).next_to(titulo, DOWN, buff=0.9)
        ajustar_al_encuadre(cierre, margen=0.5)
        self.decir("Para terminar. Un sistema lineal puede no tener solución, tener una, o tener infinitas. Los pivotes lo deciden; el núcleo describe lo que sobra; el espacio columna, lo que se alcanza. Y en cada problema, tres verbos: resolver, verificar e interpretar. Gracias por seguir el curso.")
        for c in cierre:
            self.play(FadeIn(c))
            self.wait(3)
        self.wait(3)
