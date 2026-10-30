"""Piezas reutilizables por todas las lecciones."""

from contextlib import contextmanager
from fractions import Fraction

from manim import (
    PI,
    MoveToTarget,
    ReplacementTransform,
    DEGREES,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    WHITE,
    Arrow,
    Axes,
    Brace,
    Circle,
    Create,
    DashedVMobject,
    SurroundingRectangle,
    TransformFromCopy,
    FadeIn,
    Surface,
    FadeOut,
    Line,
    Matrix,
    MathTex,
    Mobject,
    Scene,
    Tex,
    Text,
    ThreeDAxes,
    ThreeDScene,
    VGroup,
    VMobject,
    Write,
    config,
)

from . import voz
from .estilo import (
    COLOR_OPERACION,
    COLOR_PIVOTE,
    COLOR_SECUNDARIO,
    COLOR_TERMINO_INDEP,
    COLORES_ECUACIONES,
    TAM_NOTA,
    TAM_TEXTO,
    TAM_TITULO,
)

MARGEN = 0.6  # distancia mínima a los bordes del encuadre

# Familia de ejercicios (prefijo del código) -> archivo del banco en ejercicios/.
ARCHIVOS_EJERCICIOS = {
    "F00": "F00_preliminares.md",
    "F01": "F01_ecuaciones_lineales.md",
    "F02": "F02_ecuaciones_varias_incognitas.md",
    "F03": "F03_sistemas_y_clasificacion.md",
    "F04": "F04_metodos_elementales.md",
    "F05": "F05_matrices_y_vectores.md",
    "F06": "F06_producto_y_transformaciones.md",
    "F07": "F07_sistema_y_forma_matricial.md",
    "F08": "F08_gauss.md",
    "F09": "F09_gauss_jordan.md",
    "F10": "F10_factorizacion_lu.md",
    "F11": "F11_rango_rouche_frobenius.md",
    "F12": "F12_combinaciones_independencia_base.md",
    "F13": "F13_nucleo.md",
    "F14": "F14_espacio_columna_imagen.md",
    "F15": "F15_problemas_integradores.md",
    "F16": "F16_demostraciones.md",
}


def archivo_de(codigo: str) -> str:
    """Archivo del banco donde está el ejercicio: la parte 2 (códigos desde 11) o la parte 1."""
    base = ARCHIVOS_EJERCICIOS[codigo[:3]]
    return base[:-3] + "_parte2.md" if int(codigo.rsplit("-", 1)[1]) >= 11 else base


def num(v: float, decimales: int = 1) -> str:
    """Número con decimales fijos para lecturas animadas, sin el feo «-0.0»."""
    texto = f"{v:.{decimales}f}"
    return texto[1:] if texto.startswith("-") and float(texto) == 0 else texto


def paso_numerado(numero: int, *partes: str, font_size: int = 40) -> VGroup:
    """Fila «(n) fórmula» para resoluciones paso a paso. La fórmula queda en [1]."""
    circulo = Circle(radius=0.22, color=COLOR_OPERACION)
    marca = VGroup(circulo, Text(str(numero), font_size=22, color=COLOR_OPERACION).move_to(circulo))
    return VGroup(marca, MathTex(*partes, font_size=font_size)).arrange(RIGHT, buff=0.35)


def resolver_paso_a_paso(
    escena: Scene, pasos, operaciones, font_size=46, espera=1.5, x=-1.8, debajo_de: Mobject | None = None
) -> VGroup:
    """Escribe una cadena de ecuaciones alineadas por '=' con la operación de cada paso a la derecha.

    pasos: lista de (izquierda, derecha) en LaTeX; operaciones: un texto por cada transición.
    La cadena queda centrada horizontalmente en `x`, o bajo `debajo_de` (alineada a su izquierda).
    """
    cadena = alinear_por_igual(*[MathTex(i, "=", d, font_size=font_size) for i, d in pasos], buff=0.3)
    if debajo_de is None:
        cadena.shift((x - cadena.get_x()) * RIGHT)
    else:
        cadena.next_to(debajo_de, DOWN, buff=0.45).align_to(debajo_de, LEFT)
    rotulos = VGroup()
    for k, texto in enumerate(operaciones):
        rotulo = Text(texto, font_size=TAM_NOTA - 2, color=COLOR_OPERACION)
        rotulo.next_to(cadena, RIGHT, buff=0.8).match_y(VGroup(cadena[k], cadena[k + 1]))
        rotulos.add(rotulo)
    escena.play(Write(cadena[0]))
    for k, rotulo in enumerate(rotulos):
        escena.play(FadeIn(rotulo))
        escena.play(Write(cadena[k + 1]))
        escena.wait(espera)
    return VGroup(cadena, rotulos)


def titulo_leccion(etiqueta: str, titulo: str) -> VGroup:
    """Rótulo de portada: «Lección N» pequeño encima del título."""
    return VGroup(
        Text(etiqueta, font_size=28, color=COLOR_SECUNDARIO),
        Text(titulo, font_size=TAM_TITULO, weight="BOLD"),
    ).arrange(DOWN, buff=0.3)


def ajustar_al_encuadre(mob: Mobject, margen: float = MARGEN) -> Mobject:
    """Red de seguridad: reduce `mob` si no cabe a lo ancho o a lo alto."""
    ancho, alto = config.frame_width - 2 * margen, config.frame_height - 2 * margen
    if mob.width > ancho:
        mob.scale_to_fit_width(ancho)
    if mob.height > alto:
        mob.scale_to_fit_height(alto)
    return meter_en_encuadre(mob, margen)  # escalar no recoloca: si quedaba fuera por un lado, se desplaza dentro


def lista(ideas, font_size=TAM_TEXTO, buff=0.35) -> VGroup:
    """Lista con viñetas; cada idea puede llevar saltos de línea."""
    return VGroup(*[Text("•  " + idea, font_size=font_size, line_spacing=1.1) for idea in ideas]).arrange(
        DOWN, aligned_edge=LEFT, buff=buff
    )


def parrafo(*lineas: str, font_size=34, sangria: float = 0.0, **kwargs) -> VGroup:
    """Varias líneas de Tex alineadas a la izquierda; las siguientes a la primera, con `sangria`.

    (Un Tex con «\\\\» centra sus líneas y LaTeX corta solo las de más de unos 75 caracteres).
    """
    grupo = VGroup(*[Tex(t, font_size=font_size, **kwargs) for t in lineas]).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
    for linea in grupo[1:]:
        linea.shift(RIGHT * sangria)
    return grupo


def alinear_por_igual(*ecuaciones: MathTex, buff: float = 0.45) -> VGroup:
    """Apila ecuaciones con sus signos '=' en la misma vertical.

    Cada MathTex debe tener '=' como parte separada, p. ej. MathTex("x", "+", "y", "=", "3").
    """
    grupo = VGroup(*ecuaciones).arrange(DOWN, buff=buff)
    x_ref = ecuaciones[0].get_part_by_tex("=").get_x()
    for ec in ecuaciones[1:]:
        ec.shift((x_ref - ec.get_part_by_tex("=").get_x()) * RIGHT)
    return grupo


def sistema_con_llave(*ecuaciones, font_size=48, colores=True) -> VGroup:
    """Sistema con llave; cada ecuación es una tupla de partes con '=' separado.

    Con colores=True cada ecuación toma su color (COLORES_ECUACIONES). Devuelve VGroup(llave, filas).
    """
    filas = alinear_por_igual(*[MathTex(*e, font_size=font_size) for e in ecuaciones], buff=0.3)
    if colores:
        for fila, color in zip(filas, COLORES_ECUACIONES):
            fila.set_color(color)
    return VGroup(Brace(filas, LEFT), filas)


def sustituir_alineado(original: MathTex, nueva: MathTex) -> MathTex:
    """Coloca `nueva` con su '=' exactamente donde está el '=' de `original`."""
    nueva.shift(original.get_part_by_tex("=").get_center() - nueva.get_part_by_tex("=").get_center())
    return nueva


def matriz_aumentada(filas, **kwargs) -> Matrix:
    """Matriz [A | b]: la línea vertical separa coeficientes de términos independientes.

    La línea queda en `matriz.separador` y es parte de la matriz (se mueve y escala con ella).
    """
    matriz = Matrix(filas, **kwargs)
    columnas = matriz.get_columns()
    x = (columnas[-2].get_right()[0] + columnas[-1].get_left()[0]) / 2
    alto = matriz.get_brackets()[0].height * 0.85
    matriz.separador = Line([x, matriz.get_y() + alto / 2, 0], [x, matriz.get_y() - alto / 2, 0])
    matriz.add(matriz.separador)
    return matriz



def tex_valor(v) -> str:
    """Entrada en LaTeX: enteros tal cual, fracciones con \frac y textos (parámetros) sin tocar."""
    if isinstance(v, str):
        return v
    v = Fraction(v)
    if v.denominator == 1:
        return str(v.numerator)
    return ("-" if v < 0 else "") + r"\frac{" + str(abs(v.numerator)) + "}{" + str(v.denominator) + "}"


def fila_tex(fila) -> str:
    """Una fila de [A | b] escrita como vector fila con su barra: [ 1  2 | 5 ]."""
    return r"\left[\begin{array}{" + "c" * (len(fila) - 1) + "|c}" + " & ".join(map(tex_valor, fila)) + r"\end{array}\right]"


def matriz_gauss(datos, pivotes=(), escala: float = 1.0) -> Matrix:
    """[A | b] a partir de números (int, Fraction) o textos, con b en naranja y los pivotes en amarillo.

    pivotes: posiciones (fila, columna) desde 0. Guarda `datos`, `pivotes` y `escala` para que
    EscenaCurso.operar_filas la reconstruya igual: escálala con `escala`, no con .scale().
    """
    con_fracciones = any(isinstance(v, Fraction) and v.denominator != 1 for fila in datos for v in fila)
    textos = [[tex_valor(v) for v in fila] for fila in datos]
    # Alineadas a la derecha y centradas en altura: una fracción no invade la fila de arriba.
    opciones = dict(v_buff=1.15 if con_fracciones else 0.8, element_alignment_corner=RIGHT)
    m = matriz_aumentada(textos, **opciones)
    ancho = max(e.width for e in m.get_entries())
    if ancho > 0.6:  # entradas con parámetros (a - 2, a^2 + 1): se separan más las columnas
        m = matriz_aumentada(textos, h_buff=max(1.3, ancho + 0.8), **opciones)
    m.get_columns()[-1].set_color(COLOR_TERMINO_INDEP)
    for i, j in pivotes:
        m.get_rows()[i][j].set_color(COLOR_PIVOTE)
    m.datos, m.pivotes, m.escala = [list(fila) for fila in datos], tuple(pivotes), escala
    return m.scale(escala)


def escalera(m: Matrix, pivotes, color=COLOR_PIVOTE) -> VMobject:
    """Línea en escalera que baja por la izquierda de cada pivote (fila, columna) y llega hasta la barra."""
    filas, columnas = m.get_rows(), m.get_columns()
    paso = filas[0].get_y() - filas[1].get_y() if len(filas) > 1 else 1.0

    def x_izq(c):
        if c == 0:
            return columnas[0].get_left()[0] - 0.15
        return (columnas[c - 1].get_right()[0] + columnas[c].get_left()[0]) / 2

    puntos = []
    for r, c in pivotes:
        y = filas[r].get_y()
        puntos += [[x_izq(c), y + paso / 2, 0], [x_izq(c), y - paso / 2, 0]]
    x_fin = m.separador.get_x() if hasattr(m, "separador") else columnas[-1].get_right()[0] + 0.15
    puntos.append([x_fin, puntos[-1][1], 0])
    return VMobject(color=color, stroke_width=4).set_points_as_corners(puntos)


def _coeficiente(k, delante: bool) -> str:
    """k como factor de una fila: «3», «-», «-\frac{1}{2}»; con `delante`, con su signo: «+ 3», «- 3», «+»."""
    if isinstance(k, str):
        cuerpo, negativo = (k[1:], True) if k.startswith("-") else (k, False)
    else:
        cuerpo, negativo = ("" if abs(k) == 1 else tex_valor(abs(k))), k < 0
    if delante:
        return ("- " if negativo else "+ ") + cuerpo
    return ("-" if negativo else "") + cuerpo


def meter_en_encuadre(mob: Mobject, margen: float = MARGEN) -> Mobject:
    """Desplaza `mob` lo justo para que no se salga por los lados ni por arriba o abajo."""
    ancho, alto = config.frame_width / 2 - margen, config.frame_height / 2 - margen
    mob.shift(RIGHT * (max(0, -ancho - mob.get_left()[0]) - max(0, mob.get_right()[0] - ancho)))
    mob.shift(UP * (max(0, -alto - mob.get_bottom()[1]) - max(0, mob.get_top()[1] - alto)))
    return mob

def panel_derecha(mob: Mobject, ancho: float = 5.9, buff: float = 0.4) -> Mobject:
    """Pega `mob` al borde derecho, reducido si es más ancho que `ancho` (para no pisar unos ejes a la izquierda)."""
    if mob.width > ancho:
        mob.scale_to_fit_width(ancho)
    return mob.to_edge(RIGHT, buff=buff)


def ejes_iguales(x_range, y_range, unidad=0.85, numeros=True) -> Axes:
    """Ejes con la misma escala en x y en y (si no, las pendientes se ven deformadas)."""
    return Axes(
        x_range=[*x_range, 1],
        y_range=[*y_range, 1],
        x_length=(x_range[1] - x_range[0]) * unidad,
        y_length=(y_range[1] - y_range[0]) * unidad,
        axis_config={"include_numbers": numeros, "font_size": 24},
    )


def recta_recortada(sistema: Axes, m: float, n: float, **kwargs):
    """Gráfica de y = m x + n limitada a la ventana de los ejes."""
    x0, x1 = sistema.x_range[:2]
    y0, y1 = sistema.y_range[:2]
    if abs(m) > 1e-9:
        cortes = sorted(((y0 - n) / m, (y1 - n) / m))
        x0, x1 = max(x0, cortes[0]), min(x1, cortes[1])
    return sistema.plot(lambda x: m * x + n, x_range=[x0, x1], **kwargs)


def recta_general(sistema: Axes, a: float, b: float, c: float, **kwargs):
    """Recta a x + b y = c dentro de la ventana de los ejes (incluidas las verticales, b = 0)."""
    if b != 0:
        return recta_recortada(sistema, -a / b, c / b, **kwargs)
    y0, y1 = sistema.y_range[:2]
    return Line(sistema.c2p(c / a, y0), sistema.c2p(c / a, y1), **kwargs)


def rectas_de_sistema(sistema: Axes, coeficientes, discontinuas=()) -> VGroup:
    """Una recta por ecuación (a, b, c), cada una con el color de su ecuación.

    La primera va más gruesa para que se vea si otra coincide con ella; las de
    `discontinuas` (índices) se dibujan a trazos.
    """
    grupo = VGroup()
    for k, (a, b, c) in enumerate(coeficientes):
        recta = recta_general(sistema, a, b, c, color=COLORES_ECUACIONES[k], stroke_width=8 if k == 0 else 4)
        grupo.add(DashedVMobject(recta, num_dashes=30) if k in discontinuas else recta)
    return grupo


def matriz(filas, colores_columnas=None, **kwargs) -> Matrix:
    """Matrix con entradas de texto LaTeX y, opcionalmente, un color por columna."""
    m = Matrix([[str(e) for e in fila] for fila in filas], **kwargs)
    for columna, color in zip(m.get_columns(), colores_columnas or []):
        if color is not None:
            columna.set_color(color)
    return m


def flecha(plano: Axes, x: float, y: float, color=WHITE, desde=(0, 0)) -> Arrow:
    """Vector (x, y) dibujado como flecha desde el punto `desde` del plano."""
    return Arrow(
        plano.c2p(*desde),
        plano.c2p(desde[0] + x, desde[1] + y),
        buff=0,
        color=color,
        stroke_width=6,
        max_tip_length_to_length_ratio=0.2,
    )


def animar_productos(escena: Scene, pares, destinos, cuentas, posicion, font_size=40, espera=1.5):
    """Anima «fila por columna» varias veces.

    pares: lista de (fila, columna) a recuadrar; destinos: entrada del resultado que se
    rellena con cada cuenta; cuentas: LaTeX de cada cuenta, escrito en `posicion`.
    """
    for (fila, columna), destino, cuenta in zip(pares, destinos, cuentas):
        marcos = VGroup(
            SurroundingRectangle(fila, color=COLOR_PIVOTE, buff=0.1),
            SurroundingRectangle(columna, color=COLOR_PIVOTE, buff=0.1),
        )
        texto = MathTex(cuenta, font_size=font_size).move_to(posicion)
        escena.play(Create(marcos), Write(texto))
        escena.wait(espera)
        escena.play(TransformFromCopy(texto, destino), FadeOut(marcos))
        escena.play(FadeOut(texto))


def plano_3d(espacio, a, b, c, d, rango_u=(-1, 4), rango_v=(-1, 4), color=WHITE, opacidad=0.45) -> Surface:
    """Trozo del plano a x + b y + c z = d.

    Se despeja la variable de mayor coeficiente (en valor absoluto) y las otras dos
    recorren rango_u y rango_v, en el orden x, y, z.
    """
    coef = [a, b, c]
    k = max(range(3), key=lambda i: abs(coef[i]))
    libres = [i for i in range(3) if i != k]

    def punto(u, v):
        p = [0.0, 0.0, 0.0]
        p[libres[0]], p[libres[1]] = u, v
        p[k] = (d - coef[libres[0]] * u - coef[libres[1]] * v) / coef[k]
        return espacio.c2p(*p)

    return Surface(
        punto,
        u_range=rango_u,
        v_range=rango_v,
        resolution=(6, 6),
        checkerboard_colors=False,
        fill_color=color,
        fill_opacity=opacidad,
        stroke_color=color,
        stroke_width=0.6,
    )


class EscenaCurso(Scene):
    """Base de todas las escenas: portada, encabezado, pie, ejercicio propuesto y resumen.

    También sirve para escenas 3D: `class X(EscenaCurso, ThreeDScene)`; los rótulos
    se fijan a la pantalla automáticamente.
    """

    def _fijar(self, *mobs):
        if isinstance(self, ThreeDScene):
            self.add_fixed_in_frame_mobjects(*mobs)
            # add_fixed_in_frame_mobjects también los añade a la escena; se quitan para que
            # aparezcan solo cuando se animen (siguen fijados a la pantalla).
            self.remove(*mobs)

    def espacio_3d(self, rango=(-1, 4), centro=(1.5, 1.5, 1.5), longitud=5, zoom=0.8):
        """Ejes 3D con rótulos x, y, z, centrados en `centro` (solo en escenas 3D)."""
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES, zoom=zoom)
        r = [*rango, 1]
        espacio = ThreeDAxes(x_range=r, y_range=r, z_range=r, x_length=longitud, y_length=longitud, z_length=longitud)
        espacio.shift(-espacio.c2p(*centro))
        fin = rango[1] + 0.4
        rotulos = VGroup(
            MathTex("x").move_to(espacio.c2p(fin, 0, 0)),
            MathTex("y").move_to(espacio.c2p(0, fin, 0)),
            MathTex("z").move_to(espacio.c2p(0, 0, fin)),
        )
        for rotulo in rotulos:
            self.add_fixed_orientation_mobjects(rotulo)
        return espacio, rotulos

    @contextmanager
    def narrar(self, texto: str | None):
        """La voz lee `texto` mientras se ejecuta el bloque; al salir, espera a que termine la frase.

        Con `texto=None` no hace nada (para ayudas que narran solo si se les pasa un texto).
        """
        if texto is not None:
            self.decir(texto)
        yield
        self.callar()

    def decir(self, texto: str):
        """La voz empieza a leer `texto` y las animaciones siguientes van a la vez.

        La frase siguiente, `limpiar`, `cambiar_encabezado` y el final del video esperan a que termine.
        """
        self.callar()
        ruta, duracion = voz.audio(texto)
        self.add_sound(str(ruta))
        self.add_subcaption(" ".join(texto.split()), duration=duracion)  # subtítulos .srt junto al video
        self._fin_voz = self.renderer.time + duracion

    def callar(self):
        """Espera a que termine la frase que se está leyendo (si hay alguna)."""
        resto = getattr(self, "_fin_voz", 0) - self.renderer.time
        if resto > 1 / config.frame_rate:
            self.wait(resto)

    def tear_down(self):
        self.callar()  # que el video no se corte a mitad de la última frase

    def limpiar(self, *conservar):
        """Desvanece todo lo que hay en pantalla excepto `conservar`."""
        self.callar()
        resto = [m for m in self.mobjects if m not in conservar]
        if resto:
            self.play(*[FadeOut(m) for m in resto])

    def consolidar(self, mob: Mobject):
        """Tras animar las piezas de `mob` por separado, deja `mob` como un solo objeto en escena."""
        familia = set(mob.get_family())
        self.remove(*[m for m in self.mobjects if set(m.get_family()) <= familia])
        self.add(mob)

    def desplazar(self, mobjects, vector):
        # Se anima cada objeto por separado: animar un VGroup improvisado lo añadiría
        # a la escena como objeto propio y luego no se podría limpiar por partes.
        self.play(*[m.animate.shift(vector) for m in mobjects])

    def mostrar_portada(self, etiqueta: str, titulo: str, espera: float = 2, voz: str | None = None):
        portada = ajustar_al_encuadre(titulo_leccion(etiqueta, titulo))
        voz = voz or f"{etiqueta.replace('·', ',')}: {titulo}"
        self._fijar(portada)
        self.play(FadeIn(portada, shift=UP * 0.3))
        with self.narrar(voz):
            self.wait(espera)
        self.play(FadeOut(portada))

    def _rotulo_encabezado(self, texto: str) -> Text:
        rotulo = ajustar_al_encuadre(Text(texto, font_size=38, weight="BOLD")).to_edge(UP, buff=0.4)
        self._fijar(rotulo)
        return rotulo

    def encabezado(self, texto: str) -> Text:
        """Título de sección arriba de la pantalla."""
        rotulo = self._rotulo_encabezado(texto)
        self.play(Write(rotulo))
        return rotulo

    def cambiar_encabezado(self, actual: Text, texto: str) -> Text:
        nuevo = self._rotulo_encabezado(texto)
        self.callar()
        self.play(FadeOut(actual, shift=UP * 0.3), FadeIn(nuevo, shift=UP * 0.3))
        return nuevo

    def pie(self, texto: str, color=COLOR_SECUNDARIO, espera: float = 0) -> Text:
        """Comentario breve abajo de la pantalla; sustituye al pie anterior si sigue visible."""
        rotulo = ajustar_al_encuadre(Text(texto, font_size=TAM_NOTA, color=color, line_spacing=1.1))
        rotulo.to_edge(DOWN, buff=0.45)
        self._fijar(rotulo)
        anterior = getattr(self, "_pie_actual", None)
        salida = [FadeOut(anterior)] if anterior in self.mobjects else []
        self.play(*salida, FadeIn(rotulo))
        self._pie_actual = rotulo
        if espera > 0:
            self.wait(espera)
        return rotulo

    def quitar_pie(self):
        """Retira el pie visible para dejar sitio abajo."""
        anterior = getattr(self, "_pie_actual", None)
        if anterior in self.mobjects:
            self.play(FadeOut(anterior))

    def operar_filas(self, m: Matrix, op, pivotes=None, nueva=None, cuenta=True, historial: VGroup | None = None,
                     lado_cuenta=DOWN, espera: float = 1.5) -> Matrix:
        """Anima una operación elemental sobre una matriz de `matriz_gauss` y devuelve la matriz nueva.

        op (filas numeradas desde 0):
            ("intercambio", i, j)  R_i <-> R_j
            ("escalar", i, k)      R_i <- k R_i   (k distinto de 0)
            ("sumar", i, j, k)     R_i <- R_i + k R_j   (i distinto de j)
        k puede ser un texto LaTeX ("-a"); entonces, o si hay parámetros en la matriz, `nueva` da la fila
        resultante (lista de textos). Rótulo violeta, fila destino recuadrada en violeta y origen en gris,
        cuenta de la fila (a `lado_cuenta` de la matriz) y fila nueva en su sitio. `pivotes` (los de la
        matriz nueva) por defecto se conservan. Con `historial` (VGroup ya en escena, no vacío) el rótulo
        se apunta debajo de él en lugar de desaparecer.
        """
        tipo, i = op[0], op[1]
        datos = [list(f) for f in m.datos]
        n = i + 1
        if tipo == "intercambio":
            j = op[2]
            datos[i], datos[j] = datos[j], datos[i]
            rotulo_tex, partes = f"R_{n} \\leftrightarrow R_{j + 1}", None
        elif tipo == "escalar":
            k = op[2]
            assert isinstance(k, str) or k != 0, "multiplicar una fila por 0 no es una operación elemental"
            datos[i] = nueva or [Fraction(k) * v for v in datos[i]]
            rotulo_tex = f"R_{n} \\leftarrow " + _coeficiente(k, False) + f"R_{n}"
            partes = (_coeficiente(k, False) + r"\,", fila_tex(m.datos[i]), "=", fila_tex(datos[i]))
        else:
            j, k = op[2], op[3]
            assert i != j, "R_i <- R_i + k R_i no es una operación elemental (con k = -1 borra la fila)"
            datos[i] = nueva or [a + Fraction(k) * b for a, b in zip(datos[i], datos[j])]
            rotulo_tex = f"R_{n} \\leftarrow R_{n} " + _coeficiente(k, True) + f"R_{j + 1}"
            partes = (fila_tex(m.datos[i]), _coeficiente(k, True) + r"\,", fila_tex(m.datos[j]), "=", fila_tex(datos[i]))

        filas = m.get_rows()
        nueva_m = matriz_gauss(datos, m.pivotes if pivotes is None else pivotes, m.escala).move_to(m)
        ambas = VGroup(m.copy(), nueva_m.copy())  # solo para medir: la nueva puede ser más ancha o más alta
        rotulo = MathTex(rotulo_tex, font_size=38 * m.escala, color=COLOR_OPERACION)
        rotulo.next_to(ambas, RIGHT, buff=0.5).match_y(filas[i])
        meter_en_encuadre(rotulo)
        marcos = [SurroundingRectangle(filas[i], color=COLOR_OPERACION, buff=0.12)]
        if tipo != "escalar":
            color_origen = COLOR_OPERACION if tipo == "intercambio" else COLOR_SECUNDARIO
            marcos.append(SurroundingRectangle(filas[op[2]], color=color_origen, buff=0.12))
        self.play(Write(rotulo), *[Create(r) for r in marcos])
        calculo = None
        if cuenta and partes:
            calculo = MathTex(*partes, font_size=34).next_to(ambas, lado_cuenta, buff=0.45)
            meter_en_encuadre(ajustar_al_encuadre(calculo))
            self.play(Write(calculo))
            self.wait(espera)

        animaciones = [ReplacementTransform(a, b) for a, b in zip(m.get_brackets(), nueva_m.get_brackets())]
        animaciones += [ReplacementTransform(m.separador, nueva_m.separador), *[FadeOut(r) for r in marcos]]
        temporales = []
        for r, fila_nueva in enumerate(nueva_m.get_rows()):
            if tipo != "intercambio" and r == i:
                animaciones += [FadeOut(e) for e in filas[r]]
                temporales.append(VGroup(*fila_nueva))
                animaciones.append(TransformFromCopy(calculo[-1], temporales[-1]) if calculo else FadeIn(temporales[-1]))
            else:
                origen = {i: op[2], op[2]: i}.get(r, r) if tipo == "intercambio" else r
                arco = PI / 2 if origen != r else 0
                animaciones += [ReplacementTransform(a, b, path_arc=arco) for a, b in zip(filas[origen], fila_nueva)]
        self.play(*animaciones, run_time=1.5)
        # Se limpian las piezas sueltas de la matriz vieja y los grupos auxiliares; queda la nueva entera.
        self.remove(*temporales)
        familia = set(m.get_family())
        self.remove(*[x for x in self.mobjects if set(x.get_family()) <= familia])
        self.consolidar(nueva_m)

        salida = [FadeOut(calculo)] if calculo else []
        if historial is None:
            salida.append(FadeOut(rotulo))
        else:
            rotulo.generate_target()
            rotulo.target.scale(0.8).next_to(historial, DOWN, aligned_edge=LEFT, buff=0.25)
            salida.append(MoveToTarget(rotulo))
        self.play(*salida)
        if historial is not None:
            self.remove(rotulo)  # queda solo dentro del historial: al desvanecerlo se va entero
            historial.add(rotulo)
        self.wait(espera)
        return nueva_m

    def ejercicio_propuesto(self, codigo: str, enunciado: Mobject, espera: float = 6, voz: str | None = None):
        """Paso 8 de la metodología: el ejercicio queda en pantalla para intentarlo (`voz`: lo que se narra)."""
        self.limpiar()
        voz = voz or "Ejercicio propuesto. Pausa el video e inténtalo; las pistas y la solución están en el banco de ejercicios."
        cabecera = Text(f"Ejercicio propuesto · {codigo}", font_size=34, color=COLOR_PIVOTE)
        donde = Text(
            f"Pausa el video e inténtalo. Pistas y solución: ejercicios/{archivo_de(codigo)}",
            font_size=TAM_NOTA - 2,
            color=COLOR_SECUNDARIO,
        )
        tarjeta = ajustar_al_encuadre(VGroup(cabecera, enunciado, donde).arrange(DOWN, buff=0.6))
        self._fijar(tarjeta)
        with self.narrar(voz):
            self.play(FadeIn(cabecera), FadeIn(enunciado))
            self.play(FadeIn(donde))
        self.wait(espera)
        self.limpiar()

    def resumen(self, ideas, siguiente: str, espera: float = 5, voz: str | None = None):
        """Paso 10 de la metodología: ideas esenciales y conexión con lo que sigue (`voz`: lo que se narra)."""
        self.limpiar()
        titulo = Text("Resumen", font_size=40, weight="BOLD")
        voz = voz or " ".join(["En resumen.", *ideas, "Siguiente:", siguiente])
        puntos = lista(ideas, font_size=TAM_NOTA + 2)
        proximo = Text("Siguiente: " + siguiente, font_size=TAM_NOTA, color=COLOR_SECUNDARIO)
        bloque = ajustar_al_encuadre(VGroup(titulo, puntos, proximo).arrange(DOWN, buff=0.55))
        self._fijar(bloque)
        with self.narrar(voz):
            self.play(Write(titulo))
            for punto in puntos:
                self.play(FadeIn(punto, shift=RIGHT * 0.2))
                self.wait(0.8)
            self.play(FadeIn(proximo))
        self.wait(espera)
        self.limpiar()
