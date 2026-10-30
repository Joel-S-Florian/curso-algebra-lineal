# F13 — Núcleo (parte 2)

Segunda parte del banco de las lecciones L45–L47: **27 ejercicios** de práctica que completan la parte 1 (`F13_nucleo.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N2: 9, N3: 18 · [C] 21, [K] 6.

---

### F13-N2-11 · [C] ¿Está en el núcleo?

**Objetivo**: comprobar pertenencia multiplicando.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 8 & 2 & 0 & 2 \\ -2 & -2 & 2 & 2 \\ 2 & 5 & -6 & -7 \end{bmatrix}$, ¿cuáles de $\mathbf{x}_1 = (1, -2, 1, -2)$ y $\mathbf{x}_2 = (2, -2, 1, -2)$ están en $\ker A$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ y mira si es el vector nulo.</details>
<details><summary>Solución</summary>

$A\mathbf{x}_1 = (0, 0, 0)$: sí está en el núcleo.

$A\mathbf{x}_2 = (8, -2, 2)$: no está en el núcleo.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una fila.</details>

### F13-N2-12 · [C] ¿Está en el núcleo?

**Objetivo**: comprobar pertenencia multiplicando.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} -1 & -5 & 2 & -5 \\ -6 & 2 & 4 & -6 \\ 4 & 0 & -3 & 5 \end{bmatrix}$, ¿cuáles de $\mathbf{x}_1 = (1, 1, -2, -2)$ y $\mathbf{x}_2 = (2, 1, -2, -2)$ están en $\ker A$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ y mira si es el vector nulo.</details>
<details><summary>Solución</summary>

$A\mathbf{x}_1 = (0, 0, 0)$: sí está en el núcleo.

$A\mathbf{x}_2 = (-1, -6, 4)$: no está en el núcleo.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una fila.</details>

### F13-N2-13 · [C] ¿Está en el núcleo?

**Objetivo**: comprobar pertenencia multiplicando.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} -4 & -4 & -4 & 4 \\ -6 & 2 & -2 & 0 \\ 2 & 6 & 4 & -5 \end{bmatrix}$, ¿cuáles de $\mathbf{x}_1 = (2, 2, -1, 2)$ y $\mathbf{x}_2 = (1, 2, -1, 2)$ están en $\ker A$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ y mira si es el vector nulo.</details>
<details><summary>Solución</summary>

$A\mathbf{x}_1 = (-4, -6, 2)$: no está en el núcleo.

$A\mathbf{x}_2 = (0, 0, 0)$: sí está en el núcleo.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una fila.</details>

### F13-N2-14 · [C] ¿Está en el núcleo?

**Objetivo**: comprobar pertenencia multiplicando.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 3 & 3 & 4 & 3 \\ 6 & -2 & 4 & -2 \\ 0 & -4 & -2 & -4 \end{bmatrix}$, ¿cuáles de $\mathbf{x}_1 = (-\frac{5}{6}, \frac{1}{2}, 1, -1)$ y $\mathbf{x}_2 = (\frac{1}{6}, \frac{1}{2}, 1, -1)$ están en $\ker A$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ y mira si es el vector nulo.</details>
<details><summary>Solución</summary>

$A\mathbf{x}_1 = (0, 0, 0)$: sí está en el núcleo.

$A\mathbf{x}_2 = (3, 6, 0)$: no está en el núcleo.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una fila.</details>

### F13-N2-15 · [K] Nulidad con el rango

**Objetivo**: usar $\operatorname{nul} = n - \operatorname{rg}$.
**Dificultad**: N2

**Enunciado.** Una matriz $A$ de tamaño $2\times 6$ tiene rango 2. ¿Cuál es la dimensión de $\ker A$? ¿Es $\ker A = \{\mathbf{0}\}$?

<details><summary>Pista 1</summary>Las columnas de $A$ son $n$.</details>
<details><summary>Solución</summary>

$\operatorname{nul}(A) = n - \operatorname{rg}(A) = 6 - 2 = 4$. Como la nulidad es positiva, $\ker A \ne \{\mathbf{0}\}$.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango de $m$ (filas) en vez de $n$.</details>

### F13-N2-16 · [K] Nulidad con el rango

**Objetivo**: usar $\operatorname{nul} = n - \operatorname{rg}$.
**Dificultad**: N2

**Enunciado.** Una matriz $A$ de tamaño $4\times 7$ tiene rango 3. ¿Cuál es la dimensión de $\ker A$? ¿Es $\ker A = \{\mathbf{0}\}$?

<details><summary>Pista 1</summary>Las columnas de $A$ son $n$.</details>
<details><summary>Solución</summary>

$\operatorname{nul}(A) = n - \operatorname{rg}(A) = 7 - 3 = 4$. Como la nulidad es positiva, $\ker A \ne \{\mathbf{0}\}$.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango de $m$ (filas) en vez de $n$.</details>

### F13-N2-17 · [K] Nulidad con el rango

**Objetivo**: usar $\operatorname{nul} = n - \operatorname{rg}$.
**Dificultad**: N2

**Enunciado.** Una matriz $A$ de tamaño $5\times 3$ tiene rango 1. ¿Cuál es la dimensión de $\ker A$? ¿Es $\ker A = \{\mathbf{0}\}$?

<details><summary>Pista 1</summary>Las columnas de $A$ son $n$.</details>
<details><summary>Solución</summary>

$\operatorname{nul}(A) = n - \operatorname{rg}(A) = 3 - 1 = 2$. Como la nulidad es positiva, $\ker A \ne \{\mathbf{0}\}$.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango de $m$ (filas) en vez de $n$.</details>

### F13-N2-18 · [K] Nulidad con el rango

**Objetivo**: usar $\operatorname{nul} = n - \operatorname{rg}$.
**Dificultad**: N2

**Enunciado.** Una matriz $A$ de tamaño $3\times 5$ tiene rango 3. ¿Cuál es la dimensión de $\ker A$? ¿Es $\ker A = \{\mathbf{0}\}$?

<details><summary>Pista 1</summary>Las columnas de $A$ son $n$.</details>
<details><summary>Solución</summary>

$\operatorname{nul}(A) = n - \operatorname{rg}(A) = 5 - 3 = 2$. Como la nulidad es positiva, $\ker A \ne \{\mathbf{0}\}$.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango de $m$ (filas) en vez de $n$.</details>

### F13-N2-19 · [K] Nulidad con el rango

**Objetivo**: usar $\operatorname{nul} = n - \operatorname{rg}$.
**Dificultad**: N2

**Enunciado.** Una matriz $A$ de tamaño $2\times 6$ tiene rango 1. ¿Cuál es la dimensión de $\ker A$? ¿Es $\ker A = \{\mathbf{0}\}$?

<details><summary>Pista 1</summary>Las columnas de $A$ son $n$.</details>
<details><summary>Solución</summary>

$\operatorname{nul}(A) = n - \operatorname{rg}(A) = 6 - 1 = 5$. Como la nulidad es positiva, $\ker A \ne \{\mathbf{0}\}$.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango de $m$ (filas) en vez de $n$.</details>

### F13-N3-11 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -1 & -6 & 3 & -3 \\ 1 & 9 & -5 & 5 \\ -1 & 9 & -7 & 7 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 0 & 1 & -1 \\ 0 & 1 & -\frac{2}{3} & \frac{2}{3} \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1, 2. Variables libres: $x_3$, $x_4$. Base: $(-1, \frac{2}{3}, 1, 0)$, $(1, -\frac{2}{3}, 0, 1)$. $\operatorname{nul}(A) = 2 = 4 - 2$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-12 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -2 & 1 & -3 \\ 4 & -2 & 6 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & -\frac{1}{2} & \frac{3}{2} \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$. Base: $(\frac{1}{2}, 1, 0)$, $(-\frac{3}{2}, 0, 1)$. $\operatorname{nul}(A) = 2 = 3 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-13 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} 4 & 4 & 2 \\ -4 & -4 & -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 1 & \frac{1}{2} \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$. Base: $(-1, 1, 0)$, $(-\frac{1}{2}, 0, 1)$. $\operatorname{nul}(A) = 2 = 3 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-14 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -3 & -3 & -6 & 9 \\ 1 & 1 & 2 & -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 1 & 2 & -3 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$, $x_4$. Base: $(-1, 1, 0, 0)$, $(-2, 0, 1, 0)$, $(3, 0, 0, 1)$. $\operatorname{nul}(A) = 3 = 4 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-15 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -6 & 3 & -6 & -3 & -6 \\ 4 & -2 & 4 & 2 & 4 \\ -2 & 1 & -2 & -1 & -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & -\frac{1}{2} & 1 & \frac{1}{2} & 1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$, $x_4$, $x_5$. Base: $(\frac{1}{2}, 1, 0, 0, 0)$, $(-1, 0, 1, 0, 0)$, $(-\frac{1}{2}, 0, 0, 1, 0)$, $(-1, 0, 0, 0, 1)$. $\operatorname{nul}(A) = 4 = 5 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-16 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -2 & 2 & 1 \\ 6 & -6 & -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & -1 & -\frac{1}{2} \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$. Base: $(1, 1, 0)$, $(\frac{1}{2}, 0, 1)$. $\operatorname{nul}(A) = 2 = 3 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-17 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -4 & 4 & -6 & 0 \\ 2 & -4 & 6 & -4 \\ 1 & -4 & 6 & -6 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 0 & 0 & 2 \\ 0 & 1 & -\frac{3}{2} & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1, 2. Variables libres: $x_3$, $x_4$. Base: $(0, \frac{3}{2}, 1, 0)$, $(-2, -2, 0, 1)$. $\operatorname{nul}(A) = 2 = 4 - 2$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-18 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -2 & -2 & 1 & 2 & -4 \\ -4 & -4 & 2 & 4 & -8 \\ -3 & -4 & 1 & 2 & -6 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 0 & -1 & -2 & 2 \\ 0 & 1 & \frac{1}{2} & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1, 2. Variables libres: $x_3$, $x_4$, $x_5$. Base: $(1, -\frac{1}{2}, 1, 0, 0)$, $(2, -1, 0, 1, 0)$, $(-2, 0, 0, 0, 1)$. $\operatorname{nul}(A) = 3 = 5 - 2$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-19 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} -2 & -2 & 2 \\ 6 & 6 & -6 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 1 & -1 \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$. Base: $(-1, 1, 0)$, $(1, 0, 1)$. $\operatorname{nul}(A) = 2 = 3 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-20 · [C] Base del núcleo

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y dar una base con las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión para $A = \begin{bmatrix} 2 & 1 & -3 & -1 \\ -6 & -3 & 9 & 3 \\ 2 & 1 & -3 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y despeja las variables básicas en función de las libres.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & \frac{1}{2} & -\frac{3}{2} & -\frac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1. Variables libres: $x_2$, $x_3$, $x_4$. Base: $(-\frac{1}{2}, 1, 0, 0)$, $(\frac{3}{2}, 0, 1, 0)$, $(\frac{1}{2}, 0, 0, 1)$. $\operatorname{nul}(A) = 3 = 4 - 1$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar un vector de la base por cada variable libre.</details>

### F13-N3-21 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} 6x + 6y + 6w = 30 \\ 2x + 4y + z + 3w = 19 \\ 2x - 2y - 2z = -8 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (\frac{1}{2}, \frac{9}{2}, 0, 0)$. Base del núcleo: $(\frac{1}{2}, -\frac{1}{2}, 1, 0)$, $(-\frac{1}{2}, -\frac{1}{2}, 0, 1)$. Solución general: $(\frac{1}{2}, \frac{9}{2}, 0, 0) + s\,(\frac{1}{2}, -\frac{1}{2}, 1, 0) + t\,(-\frac{1}{2}, -\frac{1}{2}, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (30, 19, -8)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-22 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} 4x + 3y + 2z - 2w = -13 \\ -8x - 6y - 4z + 4w = 26 \\ 4x + 6y - 2w = -20 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (-\frac{3}{2}, -\frac{7}{3}, 0, 0)$. Base del núcleo: $(-1, \frac{2}{3}, 1, 0)$, $(\frac{1}{2}, 0, 0, 1)$. Solución general: $(-\frac{3}{2}, -\frac{7}{3}, 0, 0) + s\,(-1, \frac{2}{3}, 1, 0) + t\,(\frac{1}{2}, 0, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (-13, 26, -20)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-23 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -2x - 3y - 4z + 4w = 7 \\ 2x + z - w = -1 \\ 8x + y + 5z - 5w = -6 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (-\frac{1}{2}, -2, 0, 0)$. Base del núcleo: $(-\frac{1}{2}, -1, 1, 0)$, $(\frac{1}{2}, 1, 0, 1)$. Solución general: $(-\frac{1}{2}, -2, 0, 0) + s\,(-\frac{1}{2}, -1, 1, 0) + t\,(\frac{1}{2}, 1, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (7, -1, -6)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-24 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} 6x - 3z - 3w = -18 \\ -2x - 3y + 4z - 2w = 15 \\ 2x + y - 2z = -9 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (-3, -3, 0, 0)$. Base del núcleo: $(\frac{1}{2}, 1, 1, 0)$, $(\frac{1}{2}, -1, 0, 1)$. Solución general: $(-3, -3, 0, 0) + s\,(\frac{1}{2}, 1, 1, 0) + t\,(\frac{1}{2}, -1, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (-18, 15, -9)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-25 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -6x + 4y + 2z + 8w = -10 \\ 6x + 8y - 2z = -30 \\ -6x - 5y + 2z + 2w = 20 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (-\frac{5}{9}, -\frac{10}{3}, 0, 0)$. Base del núcleo: $(\frac{1}{3}, 0, 1, 0)$, $(\frac{8}{9}, -\frac{2}{3}, 0, 1)$. Solución general: $(-\frac{5}{9}, -\frac{10}{3}, 0, 0) + s\,(\frac{1}{3}, 0, 1, 0) + t\,(\frac{8}{9}, -\frac{2}{3}, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (-10, -30, 20)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-26 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} 2x - 8z - 3w = 11 \\ 4x + 4y - 4z + 2w = 18 \\ 2x + 2y - 2z + w = 9 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (\frac{11}{2}, -1, 0, 0)$. Base del núcleo: $(4, -3, 1, 0)$, $(\frac{3}{2}, -2, 0, 1)$. Solución general: $(\frac{11}{2}, -1, 0, 0) + s\,(4, -3, 1, 0) + t\,(\frac{3}{2}, -2, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (11, 18, 9)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-27 · [C] Solución general: particular más núcleo

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + \ker A$.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -2x + 8y - 4z = 0 \\ 3x - 6y + 8z + 4w = 2 \\ x + 2y + 4z + 4w = 2 \end{cases}$ y escribe la solución como $\mathbf{x}_p + $ combinación de una base de $\ker A$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y pon las libres a cero para $\mathbf{x}_p$.</details>
<details><summary>Solución</summary>

Solución particular (libres $= 0$): $\mathbf{x}_p = (\frac{4}{3}, \frac{1}{3}, 0, 0)$. Base del núcleo: $(-\frac{10}{3}, -\frac{1}{3}, 1, 0)$, $(-\frac{8}{3}, -\frac{2}{3}, 0, 1)$. Solución general: $(\frac{4}{3}, \frac{1}{3}, 0, 0) + s\,(-\frac{10}{3}, -\frac{1}{3}, 1, 0) + t\,(-\frac{8}{3}, -\frac{2}{3}, 0, 1)$.

Comprobación: $A\mathbf{x}_p = (0, 2, 2)$ y cada vector de la base cumple $A\mathbf{n} = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar sumar $\mathbf{x}_p$ y dar solo el núcleo.</details>

### F13-N3-28 · [K] Preguntas sobre el núcleo

**Objetivo**: razonar sobre el núcleo sin calcular.
**Dificultad**: N3

**Enunciado.** a) ¿Puede el núcleo de una matriz $3 \times 5$ ser $\{\mathbf{0}\}$?

b) Si $A\mathbf{x} = \mathbf{b}$ tiene dos soluciones distintas, ¿qué sabes de $\ker A$?

c) ¿Es el conjunto de soluciones de $A\mathbf{x} = \mathbf{b}$, con $\mathbf{b} \ne \mathbf{0}$, un subespacio?

<details><summary>Pista 1</summary>Usa $\operatorname{nul} = n - \operatorname{rg}$ y la estructura $\mathbf{x}_p + \ker A$.</details>
<details><summary>Solución</summary>

a) No: $\operatorname{nul} = 5 - \operatorname{rg} \ge 5 - 3 = 2$.

b) Su diferencia está en el núcleo y es no nula: $\ker A \ne \{\mathbf{0}\}$ (y hay infinitas soluciones).

c) No: no contiene a $\mathbf{0}$ (es el núcleo trasladado, un «subespacio afín»).

</details>
<details><summary>Errores frecuentes</summary>Pensar que el conjunto solución siempre contiene a $\mathbf{0}$.</details>

