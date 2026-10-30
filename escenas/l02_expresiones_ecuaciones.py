"""Lección 2 — Expresiones, igualdades y ecuaciones.

Escenas (un video cada una):
    VariableIncognitaCoeficiente, QueEsUnaEcuacion, TransformacionesQueConservanSoluciones

Renderizar (desde la carpeta raíz del proyecto):
    manim -qh escenas/l02_expresiones_ecuaciones.py -a
"""

import sys
from pathlib import Path

# Manim carga este archivo por su ruta; añadimos la raíz para poder importar `curso`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import *  # noqa: E402

from curso.componentes import EscenaCurso, ajustar_al_encuadre, alinear_por_igual  # noqa: E402
from curso.estilo import *  # noqa: E402,F403

CAIDA = 1.4  # distancia del brazo de la balanza a sus platos


def balanza(inclinacion: ValueTracker, centro, brazo=3.0, medio=1.2):
    """Balanza que se inclina según `inclinacion` (radianes; > 0 baja el plato izquierdo).

    Devuelve (dibujo, extremo) donde extremo(-1) y extremo(1) dan los puntos de los que cuelgan los platos.
    """

    def extremo(lado):
        a = inclinacion.get_value()
        return centro + lado * brazo * np.array([np.cos(a), np.sin(a), 0])

    def dibujar():
        partes = VGroup(Line(extremo(-1), extremo(1), stroke_width=6))
        for lado in (-1, 1):
            p = extremo(lado)
            base = p + DOWN * CAIDA
            partes.add(
                Line(p, base + LEFT * medio, stroke_width=2),
                Line(p, base + RIGHT * medio, stroke_width=2),
                Line(base + LEFT * medio, base + RIGHT * medio, stroke_width=5),
            )
        return partes

    soporte = Triangle(color=WHITE).scale(0.5).next_to(centro, DOWN, buff=0)
    return VGroup(always_redraw(dibujar), soporte), extremo


def poner_en_plato(etiqueta: Mobject, extremo, lado) -> Mobject:
    """La etiqueta viaja sobre el plato aunque la balanza se incline."""
    etiqueta.add_updater(lambda m: m.next_to(extremo(lado) + DOWN * CAIDA, UP, buff=0.12))
    etiqueta.update()
    return etiqueta


def angulo_para(izquierda: float, derecha: float) -> float:
    return float(np.clip((izquierda - derecha) * 0.05, -0.25, 0.25))


class VariableIncognitaCoeficiente(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 2 · Parte 1", "Variables, términos y coeficientes")

        # Una letra en lugar de un número.
        titulo = self.encabezado("Una letra en lugar de un número")
        caja = Square(side_length=1.4, color=COLOR_PIVOTE)
        interrogante = MathTex("?", font_size=80).move_to(caja)
        self.decir("Imagina una caja con un número dentro que no conoces.")
        self.play(Create(caja), Write(interrogante))
        self.pie("Imagina una caja con un número dentro que no conocemos.", espera=2)
        letra = MathTex("x", font_size=96, color=COLOR_PIVOTE).move_to(caja)
        self.decir("En matemáticas, esa caja se escribe con una letra: equis, ye, zeta.")
        self.play(ReplacementTransform(caja, letra), FadeOut(interrogante))
        self.pie("En matemáticas la caja se escribe con una letra: x, y, z...", espera=2)
        self.play(letra.animate.shift(LEFT * 3))
        valores = [MathTex(f"x = {v}", font_size=60).shift(RIGHT * 2) for v in ("1", "2", "-7", r"\tfrac{1}{2}")]
        actual = valores[0]
        self.decir("Como puede valer uno, dos, menos siete o un medio, decimos que es una variable.")
        self.play(Write(actual))
        for siguiente in valores[1:]:
            self.play(Transform(actual, siguiente), run_time=0.7)
            self.wait(0.4)
        definiciones = VGroup(
            Tex(r"\textbf{Variable}: símbolo que representa un número y puede tomar distintos valores.", font_size=36),
            Tex(r"\textbf{Incógnita}: variable cuyo valor buscamos (``desconocida'').", font_size=36),
            Tex(r"\textbf{Constante}: número fijo, como $5$ o $-\tfrac{2}{3}$.", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=1.4)
        self.decir("Una variable es un símbolo que representa un número y puede tomar distintos valores. Cuando buscamos el valor concreto que cumple una condición, la llamamos incógnita, que significa desconocida. Y una constante es un número fijo.")
        for d in definiciones:
            self.play(FadeIn(d))
            self.wait(1.5)
        self.wait(2)
        self.limpiar(titulo)

        # Anatomía de una expresión.
        titulo = self.cambiar_encabezado(titulo, "Anatomía de una expresión algebraica")
        expr = MathTex("3", "x", "+", "2", "y", "-", "5", font_size=96).shift(UP * 0.6)
        self.decir("Una expresión está formada por términos, que son los sumandos.")
        self.play(Write(expr))
        terminos = [((0, 1), "término 1"), ((2, 3, 4), "término 2"), ((5, 6), "término 3")]
        llaves = VGroup()
        for indices, nombre in terminos:
            parte = VGroup(*[expr[i] for i in indices])
            llave = Brace(parte, DOWN)
            llaves.add(VGroup(llave, Text(nombre, font_size=TAM_NOTA).next_to(llave, DOWN, buff=0.1)))
        self.play(LaggedStart(*[FadeIn(l) for l in llaves], lag_ratio=0.5))
        self.decir("El signo que va delante pertenece al término: el tercer término no es cinco, es menos cinco.")
        self.pie("Un término es cada sumando. El signo que tiene delante forma parte del término.", espera=3)
        self.play(FadeOut(llaves))
        for i in (0, 3):
            expr[i].set_color(COLOR_COEFICIENTE)
        expr[5:].set_color(COLOR_TERMINO_INDEP)
        rot_coef = Text("coeficientes: el número que multiplica a cada variable", font_size=TAM_NOTA, color=COLOR_COEFICIENTE)
        rot_coef.next_to(expr, UP, buff=1.2)
        flechas = VGroup(
            *[Arrow(rot_coef.get_bottom(), expr[i].get_top(), buff=0.1, color=COLOR_COEFICIENTE) for i in (0, 3)]
        )
        rot_ind = Text("término independiente: no lleva variable", font_size=TAM_NOTA, color=COLOR_TERMINO_INDEP)
        rot_ind.next_to(expr, DOWN, buff=0.6).align_to(expr[5], RIGHT)
        self.decir("El número que multiplica a cada variable es su coeficiente: aquí, tres y dos.")
        self.play(FadeIn(rot_coef), *[GrowArrow(f) for f in flechas])
        self.wait(2)
        self.decir("El término sin variable es el término independiente. Estos colores serán los mismos durante todo el curso.")
        self.play(FadeIn(rot_ind))
        self.wait(2)
        self.decir("El término independiente es menos cinco, con su signo.")
        self.pie("Para la expresión, el término independiente es -5 (con su signo), no 5.", espera=3)
        self.limpiar(titulo)

        # Coeficientes ocultos.
        oculto = MathTex("x", "-", "y", "+", "4", font_size=80)
        self.decir("En equis menos ye más cuatro, ¿cuáles son los coeficientes?")
        self.play(Write(oculto))
        explicito = MathTex("{1}", "x", "+", "(-1)", "y", "+", "4", font_size=80)
        explicito[0].set_color(COLOR_COEFICIENTE)
        explicito[3].set_color(COLOR_COEFICIENTE)
        explicito[6].set_color(COLOR_TERMINO_INDEP)
        self.wait(1)
        self.decir("Cuando no se ve un número delante de la letra, el coeficiente es uno, o menos uno si hay un signo menos. Esto será fundamental al escribir matrices.")
        self.play(TransformMatchingTex(oculto, explicito))
        self.pie("Si no se ve un número delante de la letra, el coeficiente es 1 (o -1 si hay un signo menos).", espera=4)
        self.limpiar(titulo)

        # Evaluar.
        titulo = self.cambiar_encabezado(titulo, "Evaluar: sustituir las letras por números")
        pasos = VGroup(
            MathTex(r"3x + 2y - 5", r"\qquad\text{con } x = 2,\ y = 1", font_size=50),
            MathTex(r"3\cdot(2) + 2\cdot(1) - 5", font_size=50),
            MathTex(r"= 6 + 2 - 5 = 3", font_size=50),
        ).arrange(DOWN, buff=0.5).shift(UP * 1)
        self.decir("Evaluar es sustituir las letras por números. Con equis igual a dos y ye igual a uno: tres por dos, más dos por uno, menos cinco. Seis más dos menos cinco: tres.")
        for p in pasos:
            self.play(Write(p))
            self.wait(1.2)
        trampa = VGroup(
            MathTex(r"x^2 \text{ con } x = -3:", r"\quad (-3)^2 = 9", font_size=46),
            MathTex(r"\text{sin paréntesis: } -3^2 = -9", font_size=46, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.35).next_to(pasos, DOWN, buff=0.8)
        self.decir("Cuidado con los signos: equis al cuadrado con equis igual a menos tres es nueve. Sin paréntesis, escribiríamos menos tres al cuadrado, que es menos nueve.")
        self.play(Write(trampa[0]))
        self.play(Write(trampa[1]))
        self.decir("Pon siempre el número entre paréntesis: así no se pierde ningún signo.")
        self.pie("Al sustituir, pon siempre el número entre paréntesis: evita errores de signo.", espera=4)
        self.limpiar(titulo)

        # Términos semejantes.
        titulo = self.cambiar_encabezado(titulo, "Términos semejantes")
        lineas = VGroup(
            MathTex(r"3x + 5x = (3 + 5)x = 8x", font_size=50),
            MathTex(r"4x + 2 - x + 6 = 3x + 8", font_size=50),
            MathTex(r"2x + 3y \neq 5xy", font_size=50, color=COLOR_ERROR),
        ).arrange(DOWN, buff=0.6)
        comentarios = [
            "Misma variable: se suman los coeficientes (propiedad distributiva).",
            "Se agrupan las x por un lado y los números por otro.",
            "Variables distintas no se pueden juntar: 2x + 3y ya no se simplifica más.",
        ]
        self.decir("Solo se pueden juntar términos con la misma variable, sumando sus coeficientes: tres equis más cinco equis es ocho equis. Cuatro equis más dos menos equis más seis es tres equis más ocho. Pero dos equis más tres ye no es cinco equis ye: no se puede simplificar.")
        for linea, comentario in zip(lineas, comentarios):
            self.play(Write(linea))
            self.pie(comentario, espera=2.5)
        self.wait(1)

        self.ejercicio_propuesto(
            "F00-N1-05",
            VGroup(
                MathTex(r"4x - y + 7 - 2z", font_size=56),
                Tex(r"a) ¿Cuántos términos tiene? \quad b) ¿Qué coeficiente tiene cada variable?", font_size=38),
                Tex(r"c) ¿Cuál es el término independiente? \quad d) Evalúala en $x = 1,\ y = -2,\ z = 3$.", font_size=38),
            ).arrange(DOWN, buff=0.35),
        )
        self.resumen(
            [
                "Una variable representa un número; una incógnita es la que buscamos.",
                "Término = sumando, con su signo. Coeficiente = número que multiplica a la variable.",
                "Término independiente = el que no lleva variable.",
                "Solo se juntan términos con la misma variable.",
            ],
            "igualdades y ecuaciones.",
            voz="En resumen: una variable representa un número, y una incógnita es la variable cuyo valor buscamos. Un término es cada sumando, con su signo. El coeficiente es el número que multiplica a la variable, y el término independiente es el que no lleva variable. Solo se juntan términos con la misma variable. Siguiente: igualdades y ecuaciones.",
        )


class QueEsUnaEcuacion(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 2 · Parte 2", "Igualdades y ecuaciones")

        # La balanza.
        titulo = self.encabezado("Una igualdad es una balanza en equilibrio")
        inclinacion = ValueTracker(0)
        dibujo, extremo = balanza(inclinacion, UP * 1.0)
        izquierda = poner_en_plato(MathTex("2x + 1", font_size=44, color=COLOR_COEFICIENTE), extremo, -1)
        derecha = poner_en_plato(MathTex("7", font_size=44, color=COLOR_TERMINO_INDEP), extremo, 1)
        self.decir("Una igualdad es como una balanza en equilibrio: afirma que lo de la izquierda pesa lo mismo que lo de la derecha. Aquí, dos equis más uno igual a siete.")
        self.play(FadeIn(dibujo), Write(izquierda), Write(derecha))
        self.pie("El signo = afirma que lo de la izquierda vale lo mismo que lo de la derecha.", espera=3)

        # Probar valores: la balanza solo se equilibra con la solución.
        prueba = None
        self.decir("Si equis vale uno, la izquierda pesa tres, y la balanza cae hacia la derecha. Con cinco, pesa once, y cae hacia la izquierda. Solo con tres se equilibra.")
        for x in (1, 5, 3):
            valor = 2 * x + 1
            correcto = valor == 7
            tex = rf"x = {x}:\quad 2\cdot({x}) + 1 = {valor}\ " + (r"\checkmark" if correcto else r"\neq 7")
            nueva = MathTex(tex, font_size=46, color=COLOR_SOLUCION if correcto else COLOR_ERROR).shift(DOWN * 2.3)
            animaciones = [Transform(prueba, nueva)] if prueba else [Write(nueva)]
            self.play(*animaciones, inclinacion.animate.set_value(angulo_para(valor, 7)), run_time=1.5)
            prueba = prueba or nueva
            self.wait(2)
        self.decir("Equis igual a tres es la solución.")
        self.pie("Solo x = 3 equilibra la balanza: x = 3 es la solución.", COLOR_SOLUCION, espera=3)
        self.limpiar(titulo)

        # Definiciones.
        titulo = self.cambiar_encabezado(titulo, "Vocabulario")
        definiciones = VGroup(
            Tex(r"\textbf{Ecuación}: igualdad entre expresiones que contienen incógnitas.", font_size=38),
            Tex(r"\textbf{Solución}: valor de las incógnitas que hace \emph{verdadera} la igualdad.", font_size=38),
            Tex(r"\textbf{Resolver}: encontrar \emph{todas} las soluciones (el \emph{conjunto solución}).", font_size=38),
            Tex(r"\textbf{Verificar}: sustituir la solución y comprobar que ambos lados coinciden.", font_size=38),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        self.decir("Una ecuación es una igualdad con incógnitas. Solución es el valor que la hace verdadera. Resolver es encontrar todas las soluciones, y verificar es sustituir y comprobar que los dos lados coinciden.")
        for d in definiciones:
            self.play(FadeIn(d, shift=RIGHT * 0.2))
            self.wait(1.8)
        self.wait(2)
        self.limpiar(titulo)

        # Una, infinitas o ninguna.
        titulo = self.cambiar_encabezado(titulo, "Una, infinitas o ninguna solución")
        casos = VGroup(
            VGroup(
                MathTex(r"2x + 1 = 7", font_size=48),
                Tex(r"Solo $x = 3$: \textbf{una} solución.", font_size=38, color=COLOR_SOLUCION),
            ),
            VGroup(
                MathTex(r"2(x + 1) = 2x + 2", font_size=48),
                Tex(r"Cierta para \emph{todo} $x$ (es la distributiva): \textbf{infinitas}.", font_size=38, color=COLOR_LIBRE),
            ),
            VGroup(
                MathTex(r"x + 1 = x + 2", font_size=48),
                Tex(r"Restando $x$: $1 = 2$, falso siempre: \textbf{ninguna}.", font_size=38, color=COLOR_ERROR),
            ),
        )
        self.decir("No todas las ecuaciones se comportan igual.")
        for caso in casos:
            caso[0].scale(0.9)
            caso[1].scale(0.9)
            caso.arrange(RIGHT, buff=0.6)
        casos.arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        self.decir("Dos equis más uno igual a siete tiene una sola solución: tres. Dos por equis más uno igual a dos equis más dos se cumple para cualquier valor: es una identidad, infinitas soluciones. Y equis más uno igual a equis más dos no se cumple nunca: restando equis queda uno igual a dos, falso. Ninguna solución.")
        for caso in casos:
            self.play(Write(caso[0]))
            self.wait(1)
            self.play(FadeIn(caso[1]))
            self.wait(2)
        self.decir("Una, infinitas o ninguna: estos tres casos son la columna vertebral de todo el curso.")
        self.pie(
            "Una igualdad cierta para todos los valores se llama identidad.\n"
            "Estos tres casos (una, infinitas, ninguna) reaparecerán en todo el curso.",
            espera=5,
        )

        self.ejercicio_propuesto(
            "F00-N2-03",
            VGroup(
                Tex(r"¿Cuáles de los valores $x = -2$, $x = 0$, $x = 4$ son solución de", font_size=40),
                MathTex(r"3x - 2 = x + 6\ ?", font_size=52),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Una ecuación es una igualdad con incógnitas.",
                "Solución: valor que la hace verdadera. Se comprueba sustituyendo.",
                "Puede haber una solución, infinitas o ninguna.",
            ],
            "cómo transformar una ecuación sin cambiar sus soluciones.",
        )


class TransformacionesQueConservanSoluciones(EscenaCurso):
    def construct(self):
        self.mostrar_portada("Lección 2 · Parte 3", "Transformar una ecuación\nsin cambiar sus soluciones")

        # Lo que se hace en un plato se hace en el otro.
        titulo = self.encabezado("Lo que se hace en un lado, se hace en el otro")
        inclinacion = ValueTracker(0)
        dibujo, extremo = balanza(inclinacion, UP * 1.4, brazo=2.6)
        izquierda = poner_en_plato(MathTex("2x + 1", font_size=44, color=COLOR_COEFICIENTE), extremo, -1)
        derecha = poner_en_plato(MathTex("7", font_size=44, color=COLOR_TERMINO_INDEP), extremo, 1)
        self.decir("Volvamos a la balanza: dos equis más uno igual a siete.")
        self.play(FadeIn(dibujo), Write(izquierda), Write(derecha))

        cadena = alinear_por_igual(
            MathTex("2x + 1", "=", "7", font_size=46),
            MathTex("2x", "=", "6", font_size=46),
            MathTex("x", "=", "3", font_size=46),
            buff=0.35,
        ).shift(DOWN * 1.9 + LEFT * 1.5)
        operaciones = VGroup(
            MathTex(r"\text{restar } 1 \text{ en ambos lados}", font_size=36, color=COLOR_OPERACION),
            MathTex(r"\text{dividir entre } 2 \text{ en ambos lados}", font_size=36, color=COLOR_OPERACION),
        )
        for i, op in enumerate(operaciones):
            op.next_to(cadena, RIGHT, buff=0.8).match_y(VGroup(cadena[i], cadena[i + 1]))
        self.play(Write(cadena[0]))
        platos = [("2x", "6"), ("x", "3")]
        self.decir("Si quitamos uno de cada plato, la balanza sigue equilibrada: dos equis igual a seis. Si dejamos la mitad en cada plato, también: equis igual a tres. Así llegamos a la solución sin romper nunca el equilibrio.")
        for i, (izq, der) in enumerate(platos):
            self.play(FadeIn(operaciones[i]))
            nueva_izq = MathTex(izq, font_size=44, color=COLOR_COEFICIENTE).move_to(izquierda)
            nueva_der = MathTex(der, font_size=44, color=COLOR_TERMINO_INDEP).move_to(derecha)
            self.play(Transform(izquierda, nueva_izq), Transform(derecha, nueva_der), Write(cadena[i + 1]))
            self.wait(1.5)
        self.pie("La balanza nunca se desequilibra: cada ecuación nueva es tan cierta como la anterior.", espera=4)
        izquierda.clear_updaters()
        derecha.clear_updaters()
        self.limpiar(titulo)

        # Las dos reglas y el atajo «pasar restando».
        titulo = self.cambiar_encabezado(titulo, "Las dos reglas seguras")
        reglas = VGroup(
            Tex(r"\textbf{Regla 1.} Sumar o restar la misma cantidad a ambos lados.", font_size=40),
            Tex(r"\textbf{Regla 2.} Multiplicar o dividir ambos lados", font_size=40),
            Tex(r"\phantom{\textbf{Regla 2.}} por el mismo número \textbf{distinto de 0}.", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(UP * 1.4)
        reglas[2].shift(UP * 0.25)  # continuación de la regla 2, más pegada
        self.decir("Las dos reglas seguras son: sumar o restar lo mismo en ambos lados, y multiplicar o dividir ambos lados por un número distinto de cero.")
        for r in reglas:
            self.play(FadeIn(r))
            self.wait(2)
        antes = MathTex("2x", "+ 1", "=", "7", font_size=56).shift(DOWN * 1)
        despues = MathTex("2x", "=", "7", "- 1", font_size=56).move_to(antes)
        despues[3].set_color(COLOR_OPERACION)
        self.decir("Lo que en el colegio se llama pasar restando es la regla uno escrita deprisa: restar uno en los dos lados.")
        self.play(Write(antes))
        self.wait(1)
        self.play(
            ReplacementTransform(antes[0], despues[0]),
            ReplacementTransform(antes[2], despues[1]),
            ReplacementTransform(antes[3], despues[2]),
            ReplacementTransform(antes[1], despues[3], path_arc=-PI / 2),
            run_time=2,
        )
        self.pie(
            "«Pasar restando» no es una regla nueva: es la regla 1 (restar 1 a ambos lados) escrita deprisa.",
            espera=5,
        )
        self.limpiar(titulo)

        # Por qué se conservan las soluciones: cada paso se puede deshacer.
        titulo = self.cambiar_encabezado(titulo, "¿Por qué no cambian las soluciones?")
        e1 = MathTex("2x + 1 = 7", font_size=50)
        e2 = MathTex("2x = 6", font_size=50)
        e3 = MathTex("x = 3", font_size=50)
        fila = VGroup(e1, e2, e3).arrange(RIGHT, buff=2.6).shift(UP * 1.3)
        idas, vueltas = VGroup(), VGroup()
        for a, b, ida, vuelta in ((e1, e2, "-1", "+1"), (e2, e3, r"\div 2", r"\cdot 2")):
            f1 = CurvedArrow(a.get_top() + UP * 0.1, b.get_top() + UP * 0.1, angle=-PI / 3, color=COLOR_OPERACION)
            f2 = CurvedArrow(b.get_bottom() + DOWN * 0.1, a.get_bottom() + DOWN * 0.1, angle=-PI / 3, color=COLOR_LIBRE)
            idas.add(VGroup(f1, MathTex(ida, font_size=36, color=COLOR_OPERACION).next_to(f1, UP, buff=0.05)))
            vueltas.add(VGroup(f2, MathTex(vuelta, font_size=36, color=COLOR_LIBRE).next_to(f2, DOWN, buff=0.05)))
        self.decir("¿Por qué no cambian las soluciones?")
        self.play(Write(fila))
        self.decir("Porque cada paso se puede deshacer: si resto uno, puedo volver sumando uno; si divido entre dos, vuelvo multiplicando por dos.")
        self.play(LaggedStart(*[Create(i) for i in idas], lag_ratio=0.5))
        self.play(LaggedStart(*[Create(v) for v in vueltas], lag_ratio=0.5))
        self.pie("Cada paso se puede deshacer con la operación contraria.", espera=2)
        prueba = VGroup(
            Tex(r"Si $a = b$, entonces $a + c = b + c$ \quad (sumar $c$ no rompe una igualdad).", font_size=36),
            Tex(r"Si $a + c = b + c$, restando $c$: $a = b$ \quad (se puede volver atrás).", font_size=36),
            Tex(
                r"Por tanto: un número es solución de una ecuación $\Leftrightarrow$ es solución de la otra.",
                font_size=36,
                color=COLOR_SOLUCION,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 1.5)
        self.decir("Si a es igual a be, sumar ce a los dos lados mantiene la igualdad. Y si a más ce es igual a be más ce, restando ce volvemos a a igual a be. Así, un número cumple la primera ecuación si y solo si cumple la última. Decimos que son equivalentes.")
        for p in prueba:
            self.play(FadeIn(p))
            self.wait(2)
        self.pie(
            "Ecuaciones con las mismas soluciones se llaman EQUIVALENTES.\n"
            "(La doble flecha se lee «si y solo si»; la estudiaremos en la Lección 4.)",
            espera=5,
        )
        self.limpiar(titulo)

        # Pasos peligrosos: no se pueden deshacer.
        titulo = self.cambiar_encabezado(titulo, "Pasos peligrosos")
        peligros = VGroup(
            VGroup(
                MathTex(r"x = 2 \;\xrightarrow{\ \cdot\, 0\ }\; 0 = 0", font_size=46),
                Text("¡Ahora la cumple cualquier x! Ganamos soluciones falsas.", font_size=TAM_NOTA, color=COLOR_ERROR),
            ),
            VGroup(
                MathTex(r"x = 2 \;\xrightarrow{\ (\ )^2\ }\; x^2 = 4", font_size=46),
                Text("x = -2 cumple x² = 4, pero no cumple x = 2: solución falsa.", font_size=TAM_NOTA, color=COLOR_ERROR),
            ),
            VGroup(
                MathTex(r"x^2 = x \;\xrightarrow{\ \div\, x\ }\; x = 1", font_size=46),
                Text("Perdimos x = 0, que sí era solución (0² = 0).", font_size=TAM_NOTA, color=COLOR_ERROR),
            ),
        )
        self.decir("Hay pasos que no se pueden deshacer.")
        for p in peligros:
            p.arrange(RIGHT, buff=0.7)
        peligros.arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        ajustar_al_encuadre(peligros)
        self.decir("Multiplicar por cero convierte cualquier ecuación en cero igual a cero: ahora la cumple cualquier número. Elevar al cuadrado puede añadir soluciones falsas: menos dos cumple equis al cuadrado igual a cuatro, pero no equis igual a dos. Y dividir entre equis puede hacer perder la solución equis igual a cero.")
        for p in peligros:
            self.play(Write(p[0]))
            self.wait(1)
            self.play(FadeIn(p[1]))
            self.wait(2.5)
        self.decir("Por eso la regla dos dice: distinto de cero.")
        self.pie(
            "Multiplicar por 0, elevar al cuadrado o dividir entre algo que puede valer 0\n"
            "no se pueden deshacer con seguridad. Por eso la regla 2 exige «distinto de 0».",
            espera=5,
        )
        self.limpiar(titulo)

        # Verificar siempre.
        titulo = self.cambiar_encabezado(titulo, "Y al final, verificar")
        verificacion = MathTex(r"x = 3:\quad 2\cdot(3) + 1 = 7\ \checkmark", font_size=56, color=COLOR_SOLUCION)
        self.decir("Y al final, siempre, verificar en la ecuación original: dos por tres más uno es siete. Correcto.")
        self.play(Write(verificacion))
        self.pie("Sustituir en la ecuación ORIGINAL detecta cualquier error de cálculo.", espera=3)

        self.ejercicio_propuesto(
            "F00-N2-04",
            VGroup(
                MathTex(r"3x - 5 = 7 - x", font_size=56),
                Text("Resuélvela indicando qué regla aplicas en cada paso, y verifica.", font_size=TAM_TEXTO),
            ).arrange(DOWN, buff=0.4),
        )
        self.resumen(
            [
                "Sumar/restar lo mismo a ambos lados no cambia las soluciones.",
                "Multiplicar/dividir ambos lados por un número distinto de 0, tampoco.",
                "Funcionan porque cada paso se puede deshacer.",
                "Multiplicar por 0, elevar al cuadrado o dividir entre una expresión\npueden ganar o perder soluciones.",
            ],
            "Lección 3 — coordenadas: la recta, el plano y el espacio.",
            voz="En resumen: sumar o restar lo mismo a los dos lados no cambia las soluciones. Multiplicar o dividir los dos lados por un número distinto de cero, tampoco. Funcionan porque cada paso se puede deshacer. En cambio, multiplicar por cero, elevar al cuadrado o dividir entre una expresión pueden ganar o perder soluciones. Siguiente: lección tres, coordenadas en la recta, el plano y el espacio.",
        )
