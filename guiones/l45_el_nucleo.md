# L45 — El núcleo de una matriz

**Objetivo**: definir el núcleo como conjunto de soluciones del sistema homogéneo, comprobar pertenencia y probar que es un subespacio.
**Prerrequisitos**: L22 (forma matricial), L44 (subespacio, base, dimensión).
**Código**: `escenas/l45_el_nucleo.py`
**Videos**: `videos/l45_el_nucleo/1080p60/` → `DefinicionNucleo.mp4`, `ComprobarSiUnVectorEstaEnElNucleo.mp4`
**Ejercicios**: F13-N1-01, F13-N1-02, F13-N2-01, F13-N2-02, F13-N4-03.

---

## Desarrollo matemático

**Definición.** $\ker A = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$, subconjunto del espacio de las incógnitas. Siempre $\mathbf{0} \in \ker A$ (no confundir el vector nulo con el espacio nulo).

**Ejemplo 2×2.** $A = \begin{bmatrix} 1&2\\2&4 \end{bmatrix}$: queda $x_1 + 2x_2 = 0$, $\ker A = \operatorname{gen}\{(-2,1)\}$, una recta por el origen.

**Subespacio.** $A(\mathbf{x}+\mathbf{y}) = \mathbf{0}$ y $A(c\mathbf{x}) = \mathbf{0}$.

**Comprobar pertenencia.** Con $A$ de $3\times 4$: $A(-3,1,-2,1)^T = \mathbf{0}$ (sí); $A(1,0,0,1)^T = (2,6,4)$ (no). Equivale a una relación entre las columnas: $x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n = \mathbf{0}$.

---

## Guion de narración

### Video 1 — `DefinicionNucleo`

| En pantalla | Narración |
|---|---|
| Sistema homogéneo 2×2 | "Dos ecuaciones proporcionales: queda una." |
| Recta en el plano | "Las soluciones forman una recta por el origen." |
| Definición | "Núcleo: soluciones del homogéneo, subconjunto del espacio de las incógnitas." |
| Vector nulo / espacio nulo | "El vector nulo siempre pertenece; puede haber muchos más." |
| Cerradura | "Suma y múltiplos de soluciones son soluciones: subespacio." |

### Video 2 — `ComprobarSiUnVectorEstaEnElNucleo`

| En pantalla | Narración |
|---|---|
| $A\mathbf{v}$ = vector nulo | "Cada fila da cero: pertenece." |
| $A\mathbf{w} = (2,6,4)$ | "Basta una componente distinta de cero para que no pertenezca." |
| $\mathbf{v} = \mathbf{n}_1 + \mathbf{n}_2$ | "Combinación de elementos del núcleo; sigue en él." |
| Equivalencias | "Es lo mismo que una relación entre las columnas." |

---

## Errores frecuentes

- Confundir $\ker A \subset \mathbb{R}^n$ con $\operatorname{Col}(A) \subset \mathbb{R}^m$.
- Creer que el núcleo puede ser vacío.
- Mirar solo una componente de $A\mathbf{x}$.

## Resumen y conexión

$\mathbf{x} \in \ker A \iff A\mathbf{x} = \mathbf{0}$. La L46 da una base del núcleo con las variables libres.
