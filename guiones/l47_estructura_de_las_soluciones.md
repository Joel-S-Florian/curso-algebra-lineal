# L47 — Estructura de las soluciones: $\mathbf{x} = \mathbf{x}_p + \mathbf{n}$

**Objetivo**: demostrar que las soluciones de $A\mathbf{x} = \mathbf{b}$ son una solución particular más el núcleo, y verlo como una recta trasladada.
**Prerrequisitos**: L45, L46.
**Código**: `escenas/l47_estructura_de_las_soluciones.py`
**Videos**: `videos/l47_estructura_de_las_soluciones/1080p60/` → `SolucionParticularMasNucleo.mp4`, `RectaTrasladada.mp4`
**Ejercicios**: F13-N3-05, F13-N4-01, F13-N4-02, F13-N5-01.

---

## Desarrollo matemático

**Ejemplo.** $A$ de $3\times 4$ de siempre, $\mathbf{b} = (1,3,2)$: reducida de $[A\mid\mathbf{b}]$ con filas $(1,2,0,1\mid 1)$, $(0,0,1,2\mid 1)$, $\mathbf{0}$. Solución general: $\mathbf{x} = (1,0,1,0) + s(-2,1,0,0) + t(-1,0,-2,1)$.

**Teorema.** Si $A\mathbf{x}_p = \mathbf{b}$, el conjunto de soluciones es $\{\mathbf{x}_p + \mathbf{n} : \mathbf{n} \in \ker A\}$.
*Demostración.* ($\supseteq$) $A(\mathbf{x}_p + \mathbf{n}) = \mathbf{b} + \mathbf{0}$. ($\subseteq$) si $A\mathbf{x} = \mathbf{b}$, $A(\mathbf{x} - \mathbf{x}_p) = \mathbf{b} - \mathbf{b} = \mathbf{0}$.

**Geometría.** $A = \begin{bmatrix} 1&2\\2&4 \end{bmatrix}$, $\mathbf{b} = (3,6)$: $\ker A$ = recta $x_1 + 2x_2 = 0$; solución $\mathbf{x}_p = (3,0)$; soluciones = la recta paralela $x_1 + 2x_2 = 3$.

**Clasificación con el núcleo.** Sin solución: $\mathbf{b} \notin \operatorname{Col}(A)$. Única: compatible y $\ker A = \{\mathbf{0}\}$. Infinitas: compatible y $\ker A \ne \{\mathbf{0}\}$ (tamaño = nulidad).

---

## Guion de narración

### Video 1 — `SolucionParticularMasNucleo`

| En pantalla | Narración |
|---|---|
| Reducida aumentada y despeje | "Equis uno y equis tres en función de las libres." |
| Vector con tres partes | "Una solución concreta, más la base del núcleo." |
| Teorema | "Solución particular más una solución del homogéneo." |
| Demostración | "A por equis menos equis pe es be menos be." |

### Video 2 — `RectaTrasladada`

| En pantalla | Narración |
|---|---|
| Núcleo, recta por el origen | "Soluciones del sistema homogéneo." |
| Recta paralela por $\mathbf{x}_p$ | "El núcleo, trasladado." |
| Tres posibilidades | "Sin solución, única o infinitas, ahora con el núcleo." |

---

## Errores frecuentes

- Dar solo el núcleo como solución de $A\mathbf{x} = \mathbf{b}$.
- Pensar que el conjunto solución pasa por el origen cuando $\mathbf{b} \ne \mathbf{0}$ (no es un subespacio).
- Olvidar que el teorema supone que ya existe una solución.

## Resumen y conexión

Solución general = particular + núcleo. La L48 caracteriza cuándo existe al menos una: $\mathbf{b} \in \operatorname{Col}(A)$.
