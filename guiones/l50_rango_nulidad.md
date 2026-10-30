# L50 — El teorema del rango y la nulidad

**Objetivo**: ver que el núcleo colapsa y la imagen sobrevive, y demostrar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.
**Prerrequisitos**: L46, L49.
**Código**: `escenas/l50_rango_nulidad.py`
**Videos**: `videos/l50_rango_nulidad/1080p60/` → `NucleoColapsaImagenSobrevive.mp4`, `DemostracionRangoNulidad.mp4`
**Ejercicios**: F14-N3-05, F14-N4-01, F14-N4-02, F14-N4-03, F14-N5-01.

---

## Desarrollo matemático

**Teorema.** Para $A$ de $m\times n$: $\dim\operatorname{Col}(A) + \dim\ker A = n$.

**Demostración.** Sea $r$ el número de pivotes. Hay $r$ columnas con pivote (base de $\operatorname{Col}(A)$, L49) y $n - r$ libres (una base de $\ker A$ por libre, L46). Suma: $n$.

**Visual.** $A = \begin{bmatrix} 1&2\\2&4 \end{bmatrix} = 5P$ con $P$ la proyección sobre $y = 2x$ (la recta $x_1 + 2x_2 = 0$ se aplasta al origen); la animación usa $P$ por tamaño (mismo núcleo e imagen). $x$ y $x + \mathbf{n}$ aterrizan en el mismo punto. $1 + 1 = 2$. Con $A$ de $3\times 4$: $2 + 2 = 4$.

**Consecuencias.** Inyectiva $\iff \ker A = \{\mathbf{0}\} \iff \operatorname{rg} = n$; sobreyectiva $\iff \operatorname{rg} = m$; cuadrada: rango $n$ $\iff$ núcleo trivial $\iff \operatorname{Col}(A) = \mathbb{R}^n \iff A\mathbf{x} = \mathbf{b}$ con solución única para todo $\mathbf{b}$. No hay $3\times 5$ inyectivas ni $5\times 3$ sobreyectivas.

---

## Guion de narración

### Video 1 — `NucleoColapsaImagenSobrevive`

| En pantalla | Narración |
|---|---|
| Rejilla y núcleo | "Versión a la quinta parte, mismo núcleo e imagen." |
| $\mathbf{x}$ y $\mathbf{x} + \mathbf{n}$ | "Difieren en un vector del núcleo." |
| Aplicar la matriz | "El plano se aplasta sobre una recta; los dos puntos coinciden." |
| Balance | "Una dimensión se pierde, otra sobrevive: suman las del plano." |

### Video 2 — `DemostracionRangoNulidad`

| En pantalla | Narración |
|---|---|
| Enunciado | "Rango más nulidad igual a ene." |
| Demostración | "Pivote o libre: erre más ene menos erre." |
| Consecuencias | "Inyectiva, sobreyectiva y el caso cuadrado." |

---

## Errores frecuentes

- Sumar rango y nulidad y esperar $m$ (es $n$, columnas).
- Confundir dónde vive cada espacio ($\ker A \subseteq \mathbb{R}^n$, $\operatorname{Col}(A) \subseteq \mathbb{R}^m$).
- Aplicar el resultado a las filas en lugar de a las columnas.

## Resumen y conexión

Rango + nulidad $= n$. Cierra la Unidad 8; la Unidad 9 reúne todo: elegir método, problemas integradores y prueba final.
