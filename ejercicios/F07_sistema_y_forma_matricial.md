# F07 — Del sistema a la forma matricial: Ax = b y [A | b]

Banco de las lecciones L22–L23. **Parte 1: 7 ejercicios**, ligados a los videos. La **parte 2** (23 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F07_sistema_y_forma_matricial_parte2.md`; la familia completa suma **30**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Resultados comprobados en `ejercicios/verificar/f05_f07.py`.

| Lección | Ejercicios |
|---|---|
| L22 Ax = b | N1-01 🎬, N2-01 🎬, N2-02, N4-01, N5-01 |
| L23 Matriz aumentada | N1-02 🎬, N3-01 🎬 |

---

### F07-N1-01 · [C] Construir A, x y b 🎬

**Objetivo**: ordenar el sistema y construir sus piezas.
**Dificultad**: N1

**Enunciado.** Escribe $A$, $\mathbf{x}$ y $\mathbf{b}$: $3x_1 - x_3 = 4$, $x_2 + 2x_1 = -1$, $x_3 = x_2 + 7$.

<details><summary>Pista 1</summary>Ordena cada ecuación como $\_\,x_1 + \_\,x_2 + \_\,x_3 = \_$.</details>
<details><summary>Pista 2</summary>La tercera es $-x_2 + x_3 = 7$.</details>
<details><summary>Solución</summary>

$A = \begin{bmatrix} 3 & 0 & -1 \\ 2 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix}$, $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 4 \\ -1 \\ 7 \end{bmatrix}$.

**Verificación**: la fila 2 de $A$ por $\mathbf{x}$ es $2x_1 + x_2$, el lado izquierdo de la segunda ecuación ✓.
</details>
<details><summary>Errores frecuentes</summary>Escribir la segunda fila como $[1\ 2\ 0]$ (respetando el orden en que aparecen, no el de las incógnitas).</details>

### F07-N2-01 · [C] Del producto al sistema 🎬

**Objetivo**: leer un sistema escrito en forma matricial.
**Dificultad**: N2

**Enunciado.** $\begin{bmatrix} 1 & 2 \\ 3 & -1 \\ 0 & 4 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 1 \\ 8 \end{bmatrix}$. a) Escribe el sistema. b) ¿Cuántas ecuaciones e incógnitas? c) ¿Es $(1, 2)$ solución?

<details><summary>Pista 1</summary>Cada fila por $(x, y)$ es una ecuación.</details>
<details><summary>Pista 2</summary>c) Calcula $A(1, 2)$.</details>
<details><summary>Solución</summary>

a) $x + 2y = 5$, $3x - y = 1$, $4y = 8$. b) 3 ecuaciones, 2 incógnitas. c) $A(1, 2) = (5, 1, 8) = \mathbf{b}$: **sí**.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Escribir la tercera como $4x = 8$.</details>

### F07-N2-02 · [C] Por columnas

**Objetivo**: interpretar $A\mathbf{x} = \mathbf{b}$ como combinación de columnas.
**Dificultad**: N2

**Enunciado.** Escribe como $A\mathbf{x} = \mathbf{b}$ y resuelve: "¿qué números $x, y$ cumplen $x(1, 2) + y(3, 1) = (5, 5)$?".

<details><summary>Pista 1</summary>Las columnas de $A$ son $(1, 2)$ y $(3, 1)$.</details>
<details><summary>Pista 2</summary>El sistema es $x + 3y = 5$, $2x + y = 5$.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} 1 & 3 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 5 \end{bmatrix}$. De la segunda, $y = 5 - 2x$; $x + 15 - 6x = 5 \Rightarrow x = 2$, $y = 1$.

**Verificación**: $2(1, 2) + 1(3, 1) = (5, 5)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Poner $(1, 2)$ y $(3, 1)$ como filas.</details>

### F07-N4-01 · [K] Una matriz mal construida

**Objetivo**: detectar errores al pasar a forma matricial.
**Dificultad**: N4

**Enunciado.** Para $2x + 3 = y$, $x - y = 0$, un estudiante escribe $A = \begin{bmatrix} 2 & 3 \\ 1 & -1 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} y \\ 0 \end{bmatrix}$. Corrige.

<details><summary>Pista 1</summary>$\mathbf{b}$ no puede contener incógnitas.</details>
<details><summary>Pista 2</summary>Ordena: $2x - y = -3$.</details>
<details><summary>Solución</summary>

$A = \begin{bmatrix} 2 & -1 \\ 1 & -1 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} -3 \\ 0 \end{bmatrix}$. (El 3 es un término independiente, no un coeficiente).

**Verificación**: la solución $x = y = -3$ cumple el sistema original ($-6 + 3 = -3$, $0 = 0$) y $A(-3, -3) = (-3, 0) = \mathbf{b}$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Los que muestra el ejercicio.</details>

### F07-N5-01 · [D] Diferencia de dos soluciones

**Objetivo**: usar la linealidad de $\mathbf{x} \mapsto A\mathbf{x}$.
**Dificultad**: N5

**Enunciado.** Demuestra que si $\mathbf{p}$ y $\mathbf{q}$ son soluciones de $A\mathbf{x} = \mathbf{b}$, entonces $\mathbf{p} - \mathbf{q}$ es solución del sistema homogéneo $A\mathbf{x} = \mathbf{0}$.

<details><summary>Pista 1</summary>$A(\mathbf{p} - \mathbf{q}) = A\mathbf{p} - A\mathbf{q}$ (L21).</details>
<details><summary>Pista 2</summary>¿Cuánto vale cada producto?</details>
<details><summary>Solución</summary>

$A(\mathbf{p} - \mathbf{q}) = A\mathbf{p} - A\mathbf{q} = \mathbf{b} - \mathbf{b} = \mathbf{0}$. $\blacksquare$ (Esta idea es la base de la Lección 47: toda solución es una solución particular más una solución del homogéneo).

**Verificación** (ejemplo): $x + y = 3$ con $\mathbf{p} = (1, 2)$, $\mathbf{q} = (3, 0)$: $\mathbf{p} - \mathbf{q} = (-2, 2)$ y $-2 + 2 = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Probarlo solo con un ejemplo.</details>

### F07-N1-02 · [C] Ida y vuelta con la aumentada 🎬

**Objetivo**: escribir y leer matrices aumentadas.
**Dificultad**: N1

**Enunciado.** a) Matriz aumentada de $x - y = 4 - z$, $2y + 3z = 1$, $x = 2y$. b) Sistema de $\left[\begin{array}{ccc|c} 3 & 0 & -1 & 2 \\ 0 & 0 & 5 & -4 \end{array}\right]$ (incógnitas $x, y, z$).

<details><summary>Pista 1</summary>a) Ordena: $x - y + z = 4$; $x - 2y = 0$.</details>
<details><summary>Pista 2</summary>b) Un 0 significa que la incógnita no aparece.</details>
<details><summary>Solución</summary>

a) $\left[\begin{array}{ccc|c} 1 & -1 & 1 & 4 \\ 0 & 2 & 3 & 1 \\ 1 & -2 & 0 & 0 \end{array}\right]$. b) $3x - z = 2$, $5z = -4$.

**Verificación**: releer cada fila como ecuación devuelve el sistema ordenado ✓.
</details>
<details><summary>Errores frecuentes</summary>a) Poner $4 - z$ en la última columna.</details>

### F07-N3-01 · [C] Una operación por filas 🎬

**Objetivo**: reconocer la operación que hace un cero y resolver de abajo arriba.
**Dificultad**: N3

**Enunciado.** $\left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & 1 & 0 \end{array}\right] \sim \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -5 & ? \end{array}\right]$. a) ¿Qué operación $R_2 \leftarrow R_2 - kR_1$ se aplicó? ¿Qué va en "?"? b) Resuelve.

<details><summary>Pista 1</summary>Para que $3 - k\cdot 1 = 0$, $k = 3$.</details>
<details><summary>Pista 2</summary>Aplica la misma operación a la última columna.</details>
<details><summary>Solución</summary>

a) $R_2 \leftarrow R_2 - 3R_1$; "?" $= 0 - 3\cdot 5 = -15$. b) $-5y = -15 \Rightarrow y = 3$; $x + 6 = 5 \Rightarrow x = -1$.

**Verificación**: en el original, $-1 + 6 = 5$ ✓ y $-3 + 3 = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar aplicar la operación a la columna de $\mathbf{b}$.</details>
