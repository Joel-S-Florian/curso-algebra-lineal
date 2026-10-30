# L34 — Factorizar, matrices triangulares y matrices elementales

**Objetivo**: entender qué es $A = LU$, por qué las matrices triangulares son cómodas y que cada operación por filas es el producto por una matriz elemental.
**Prerrequisitos**: L20 (producto de matrices), L24–L26 (operaciones elementales y Gauss).
**Código**: `escenas/l34_factorizar_y_triangulares.py`
**Videos**: `videos/l34_factorizar_y_triangulares/1080p60/` → `QueEsFactorizar.mp4`, `TriangularesYSustitucion.mp4`, `MatricesElementales.mp4`
**Ejercicios**: F10-N1-01, F10-N2-01, F10-N2-02.

---

## Desarrollo matemático

**Ejemplo de la Unidad 6** (el sistema de la L26, solución $(1, -1, 2)$): $A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 3 & 1 \\ -1 & 1 & 2 \end{bmatrix}$, $\mathbf{b} = (-3, 1, 2)$,
$$L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix},\qquad U = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 10 \end{bmatrix},\qquad A = LU.$$

**Triangulares.** Superior: ceros debajo de la diagonal; inferior: ceros encima. Un sistema triangular se resuelve por sustitución (hacia atrás si es superior, hacia adelante si es inferior) con unas $\frac{n^2}{2}$ multiplicaciones. El producto de triangulares inferiores es inferior, y la inversa de una inferior con unos en la diagonal también lo es.

**Matrices elementales.** Multiplicar $A$ por la izquierda por la identidad modificada hace una operación por filas: intercambio $P_{ij}$, escalado $D_i(k)$, reemplazo $E_{ij}(k)$ ($R_i \leftarrow R_i + kR_j$). Su inversa es del mismo tipo. La eliminación del ejemplo es $E_{32}E_{31}E_{21}A = U$ con $E_{21} = E_{21}(-2)$, $E_{31} = E_{31}(1)$, $E_{32} = E_{32}(3)$.

---

## Guion de narración

### Video 1 — `QueEsFactorizar`

| En pantalla | Narración |
|---|---|
| $12 = 3\cdot 4$ y $x^2 - 1$ | "Factorizar es escribir algo como un producto de piezas más simples." |
| $A = LU$ | "La matriz de la lección veintiséis es el producto de dos triangulares: ele, inferior con unos, y u, superior, que es su forma escalonada." |
| Entrada $(3,2)$ | "Fila tres de ele por columna dos de u: menos dos, más tres: uno, que es a tres dos." |

### Video 2 — `TriangularesYSustitucion`

| En pantalla | Narración |
|---|---|
| Superior e inferior | "Superior: ceros debajo de la diagonal; inferior: ceros encima." |
| Sustitución hacia atrás y hacia adelante | "Un sistema triangular se resuelve sin eliminar: de la última ecuación a la primera, o al revés." |
| Tres hechos | "Cuesta unas ene cuadrado entre dos; el producto de inferiores es inferior; la inversa de una inferior con unos es del mismo tipo." |

### Video 3 — `MatricesElementales`

| En pantalla | Narración |
|---|---|
| $E_{21}A$ | "Multiplicar por la izquierda por la identidad con un menos dos en la fila dos, columna uno, resta el doble de la fila uno a la dos." |
| $E_{32}E_{31}E_{21}A = U$ | "Encadenadas, las tres matrices elementales llevan a a su forma escalonada." |
| Los tres tipos | "Intercambio, escalado y reemplazo; la inversa de cada una es del mismo tipo." |

---

## Errores frecuentes

- Multiplicar posición a posición en lugar de fila por columna.
- Poner el multiplicador en la posición $(j, i)$ en lugar de $(i, j)$ al construir $E_{ij}$.
- Sustituir hacia adelante un sistema superior (o al revés).

## Resumen y conexión

$A = LU$ separa la eliminación en dos triangulares; las matrices elementales explican por qué: cada paso de Gauss es un producto. La L35 muestra de dónde salen exactamente los números de $L$.
