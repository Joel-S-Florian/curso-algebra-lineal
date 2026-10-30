# F06 — Producto matricial y transformaciones (parte 2)

Segunda parte del banco de las lecciones L19–L21: **30 ejercicios** de práctica que completan la parte 1 (`F06_producto_y_transformaciones.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N1: 6, N2: 18, N3: 6 · [C] 23, [K] 7.

---

### F06-N1-11 · [C] Matriz por vector

**Objetivo**: calcular $A\mathbf{x}$ fila por columna.
**Dificultad**: N1

**Enunciado.** Calcula $A\mathbf{x}$ con $A = \begin{bmatrix} 4 & -2 \\ 4 & 0 \end{bmatrix}$ y $\mathbf{x} = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada fila de $A$ da una componente del resultado.</details>
<details><summary>Solución</summary>

Cada componente es una fila de $A$ por $\mathbf{x}$: $4\cdot (-1) + (-2)\cdot (-1) = -2$; $4\cdot (-1) + 0\cdot (-1) = -4$. Luego $A\mathbf{x} = \begin{bmatrix} -2 \\ -4 \end{bmatrix}$ (un vector de $\mathbb{R}^2$).

</details>
<details><summary>Errores frecuentes</summary>Multiplicar por columnas en lugar de por filas sin sumar.</details>

### F06-N1-12 · [C] Matriz por vector

**Objetivo**: calcular $A\mathbf{x}$ fila por columna.
**Dificultad**: N1

**Enunciado.** Calcula $A\mathbf{x}$ con $A = \begin{bmatrix} -3 & 0 & 4 \\ -1 & -1 & 1 \end{bmatrix}$ y $\mathbf{x} = \begin{bmatrix} 0 \\ 3 \\ 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada fila de $A$ da una componente del resultado.</details>
<details><summary>Solución</summary>

Cada componente es una fila de $A$ por $\mathbf{x}$: $(-3)\cdot 0 + 0\cdot 3 + 4\cdot 1 = 4$; $(-1)\cdot 0 + (-1)\cdot 3 + 1\cdot 1 = -2$. Luego $A\mathbf{x} = \begin{bmatrix} 4 \\ -2 \end{bmatrix}$ (un vector de $\mathbb{R}^2$).

</details>
<details><summary>Errores frecuentes</summary>Multiplicar por columnas en lugar de por filas sin sumar.</details>

### F06-N1-13 · [C] Matriz por vector

**Objetivo**: calcular $A\mathbf{x}$ fila por columna.
**Dificultad**: N1

**Enunciado.** Calcula $A\mathbf{x}$ con $A = \begin{bmatrix} -2 & -1 & 1 \\ 0 & -2 & 2 \\ 2 & 4 & -1 \end{bmatrix}$ y $\mathbf{x} = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada fila de $A$ da una componente del resultado.</details>
<details><summary>Solución</summary>

Cada componente es una fila de $A$ por $\mathbf{x}$: $(-2)\cdot 2 + (-1)\cdot 0 + 1\cdot 3 = -1$; $0\cdot 2 + (-2)\cdot 0 + 2\cdot 3 = 6$; $2\cdot 2 + 4\cdot 0 + (-1)\cdot 3 = 1$. Luego $A\mathbf{x} = \begin{bmatrix} -1 \\ 6 \\ 1 \end{bmatrix}$ (un vector de $\mathbb{R}^3$).

</details>
<details><summary>Errores frecuentes</summary>Multiplicar por columnas en lugar de por filas sin sumar.</details>

### F06-N1-14 · [C] Matriz por vector

**Objetivo**: calcular $A\mathbf{x}$ fila por columna.
**Dificultad**: N1

**Enunciado.** Calcula $A\mathbf{x}$ con $A = \begin{bmatrix} -3 & -1 & 2 \\ 1 & -3 & 3 \\ -3 & -3 & -3 \end{bmatrix}$ y $\mathbf{x} = \begin{bmatrix} -1 \\ -2 \\ -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada fila de $A$ da una componente del resultado.</details>
<details><summary>Solución</summary>

Cada componente es una fila de $A$ por $\mathbf{x}$: $(-3)\cdot (-1) + (-1)\cdot (-2) + 2\cdot (-3) = -1$; $1\cdot (-1) + (-3)\cdot (-2) + 3\cdot (-3) = -4$; $(-3)\cdot (-1) + (-3)\cdot (-2) + (-3)\cdot (-3) = 18$. Luego $A\mathbf{x} = \begin{bmatrix} -1 \\ -4 \\ 18 \end{bmatrix}$ (un vector de $\mathbb{R}^3$).

</details>
<details><summary>Errores frecuentes</summary>Multiplicar por columnas en lugar de por filas sin sumar.</details>

### F06-N1-15 · [C] Matriz por vector

**Objetivo**: calcular $A\mathbf{x}$ fila por columna.
**Dificultad**: N1

**Enunciado.** Calcula $A\mathbf{x}$ con $A = \begin{bmatrix} 0 & -1 & -3 \\ 0 & 0 & -1 \\ -1 & 2 & 4 \end{bmatrix}$ y $\mathbf{x} = \begin{bmatrix} 4 \\ -2 \\ -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada fila de $A$ da una componente del resultado.</details>
<details><summary>Solución</summary>

Cada componente es una fila de $A$ por $\mathbf{x}$: $0\cdot 4 + (-1)\cdot (-2) + (-3)\cdot (-1) = 5$; $0\cdot 4 + 0\cdot (-2) + (-1)\cdot (-1) = 1$; $(-1)\cdot 4 + 2\cdot (-2) + 4\cdot (-1) = -12$. Luego $A\mathbf{x} = \begin{bmatrix} 5 \\ 1 \\ -12 \end{bmatrix}$ (un vector de $\mathbb{R}^3$).

</details>
<details><summary>Errores frecuentes</summary>Multiplicar por columnas en lugar de por filas sin sumar.</details>

### F06-N1-16 · [C] Matriz por vector

**Objetivo**: calcular $A\mathbf{x}$ fila por columna.
**Dificultad**: N1

**Enunciado.** Calcula $A\mathbf{x}$ con $A = \begin{bmatrix} -1 & 4 & 1 \\ -3 & -1 & -3 \\ 2 & 0 & 1 \end{bmatrix}$ y $\mathbf{x} = \begin{bmatrix} -1 \\ -2 \\ 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada fila de $A$ da una componente del resultado.</details>
<details><summary>Solución</summary>

Cada componente es una fila de $A$ por $\mathbf{x}$: $(-1)\cdot (-1) + 4\cdot (-2) + 1\cdot 2 = -5$; $(-3)\cdot (-1) + (-1)\cdot (-2) + (-3)\cdot 2 = -1$; $2\cdot (-1) + 0\cdot (-2) + 1\cdot 2 = 0$. Luego $A\mathbf{x} = \begin{bmatrix} -5 \\ -1 \\ 0 \end{bmatrix}$ (un vector de $\mathbb{R}^3$).

</details>
<details><summary>Errores frecuentes</summary>Multiplicar por columnas en lugar de por filas sin sumar.</details>

### F06-N2-11 · [C] Producto de matrices 2×2

**Objetivo**: multiplicar fila por columna.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ con $A = \begin{bmatrix} 4 & 0 \\ 3 & 2 \end{bmatrix}$ y $B = \begin{bmatrix} -2 & 2 \\ 2 & 3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = \begin{bmatrix} -8 & 8 \\ -2 & 12 \end{bmatrix}$. Por ejemplo, la entrada $(1,1)$: $4\cdot (-2) + 0\cdot 2 = -8$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar entrada con entrada, como en la suma.</details>

### F06-N2-12 · [C] Producto de matrices 2×2

**Objetivo**: multiplicar fila por columna.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ con $A = \begin{bmatrix} -3 & 3 \\ 4 & 4 \end{bmatrix}$ y $B = \begin{bmatrix} 3 & 3 \\ 0 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = \begin{bmatrix} -9 & -12 \\ 12 & 8 \end{bmatrix}$. Por ejemplo, la entrada $(1,1)$: $(-3)\cdot 3 + 3\cdot 0 = -9$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar entrada con entrada, como en la suma.</details>

### F06-N2-13 · [C] Producto de matrices 2×2

**Objetivo**: multiplicar fila por columna.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ con $A = \begin{bmatrix} 1 & 4 \\ -1 & 1 \end{bmatrix}$ y $B = \begin{bmatrix} 4 & 2 \\ 2 & 0 \end{bmatrix}$.

<details><summary>Pista 1</summary>Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = \begin{bmatrix} 12 & 2 \\ -2 & -2 \end{bmatrix}$. Por ejemplo, la entrada $(1,1)$: $1\cdot 4 + 4\cdot 2 = 12$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar entrada con entrada, como en la suma.</details>

### F06-N2-14 · [C] Producto de matrices 2×2

**Objetivo**: multiplicar fila por columna.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ con $A = \begin{bmatrix} -1 & 3 \\ -2 & -1 \end{bmatrix}$ y $B = \begin{bmatrix} 0 & 1 \\ -1 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = \begin{bmatrix} -3 & 2 \\ 1 & -3 \end{bmatrix}$. Por ejemplo, la entrada $(1,1)$: $(-1)\cdot 0 + 3\cdot (-1) = -3$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar entrada con entrada, como en la suma.</details>

### F06-N2-15 · [C] Producto de matrices 2×2

**Objetivo**: multiplicar fila por columna.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ con $A = \begin{bmatrix} 3 & 0 \\ 0 & 4 \end{bmatrix}$ y $B = \begin{bmatrix} -3 & 3 \\ 1 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = \begin{bmatrix} -9 & 9 \\ 4 & 4 \end{bmatrix}$. Por ejemplo, la entrada $(1,1)$: $3\cdot (-3) + 0\cdot 1 = -9$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar entrada con entrada, como en la suma.</details>

### F06-N2-16 · [C] Producto de matrices 2×2

**Objetivo**: multiplicar fila por columna.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ con $A = \begin{bmatrix} 3 & -2 \\ 4 & -1 \end{bmatrix}$ y $B = \begin{bmatrix} 0 & 0 \\ 1 & -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Calcula primero la primera fila de $AB$ multiplicando la primera fila de $A$ por cada columna de $B$.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ es la fila $i$ de $A$ por la columna $j$ de $B$: $AB = \begin{bmatrix} -2 & 6 \\ -1 & 3 \end{bmatrix}$. Por ejemplo, la entrada $(1,1)$: $3\cdot 0 + (-2)\cdot 1 = -2$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar entrada con entrada, como en la suma.</details>

### F06-N2-17 · [C] Producto rectangular

**Objetivo**: comprobar que se puede multiplicar y calcular el tamaño del resultado.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ y $BA$ con $A = \begin{bmatrix} 0 & 3 & -1 \\ 2 & -2 & 0 \end{bmatrix}$ ($2\times 3$) y $B = \begin{bmatrix} 2 & 3 \\ -1 & -1 \\ 2 & 2 \end{bmatrix}$ ($3\times 2$). ¿Qué tamaño tienen?

<details><summary>Pista 1</summary>Mira el tamaño: $(2\times 3)(3\times 2)$ da $2\times 2$.</details>
<details><summary>Solución</summary>

$AB$ es $2\times 2$: $\begin{bmatrix} -5 & -5 \\ 6 & 8 \end{bmatrix}$. $BA$ es $3\times 3$: $\begin{bmatrix} 6 & 0 & -2 \\ -2 & -1 & 1 \\ 4 & 2 & -2 \end{bmatrix}$. Los productos son distintos hasta en tamaño.

</details>
<details><summary>Errores frecuentes</summary>Dar el mismo tamaño a $AB$ y $BA$.</details>

### F06-N2-18 · [C] Producto rectangular

**Objetivo**: comprobar que se puede multiplicar y calcular el tamaño del resultado.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ y $BA$ con $A = \begin{bmatrix} -1 & -1 & -1 \\ 2 & 1 & 3 \end{bmatrix}$ ($2\times 3$) y $B = \begin{bmatrix} 1 & 0 \\ 0 & 0 \\ 2 & 1 \end{bmatrix}$ ($3\times 2$). ¿Qué tamaño tienen?

<details><summary>Pista 1</summary>Mira el tamaño: $(2\times 3)(3\times 2)$ da $2\times 2$.</details>
<details><summary>Solución</summary>

$AB$ es $2\times 2$: $\begin{bmatrix} -3 & -1 \\ 8 & 3 \end{bmatrix}$. $BA$ es $3\times 3$: $\begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 0 & -1 & 1 \end{bmatrix}$. Los productos son distintos hasta en tamaño.

</details>
<details><summary>Errores frecuentes</summary>Dar el mismo tamaño a $AB$ y $BA$.</details>

### F06-N2-19 · [C] Producto rectangular

**Objetivo**: comprobar que se puede multiplicar y calcular el tamaño del resultado.
**Dificultad**: N2

**Enunciado.** Calcula $AB$ y $BA$ con $A = \begin{bmatrix} 1 & 1 & -2 \\ 0 & 0 & -2 \end{bmatrix}$ ($2\times 3$) y $B = \begin{bmatrix} -2 & -2 \\ 0 & -2 \\ 1 & -2 \end{bmatrix}$ ($3\times 2$). ¿Qué tamaño tienen?

<details><summary>Pista 1</summary>Mira el tamaño: $(2\times 3)(3\times 2)$ da $2\times 2$.</details>
<details><summary>Solución</summary>

$AB$ es $2\times 2$: $\begin{bmatrix} -4 & 0 \\ -2 & 4 \end{bmatrix}$. $BA$ es $3\times 3$: $\begin{bmatrix} -2 & -2 & 8 \\ 0 & 0 & 4 \\ 1 & 1 & 2 \end{bmatrix}$. Los productos son distintos hasta en tamaño.

</details>
<details><summary>Errores frecuentes</summary>Dar el mismo tamaño a $AB$ y $BA$.</details>

### F06-N2-20 · [K] ¿Está definido el producto?

**Objetivo**: decidir con los tamaños si $AB$ y $BA$ existen.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $2\times 3$ y $B$ de tamaño $3\times 4$. ¿Están definidos $AB$ y $BA$? Si lo están, ¿de qué tamaño son?

<details><summary>Pista 1</summary>Compara las columnas de la primera matriz con las filas de la segunda.</details>
<details><summary>Solución</summary>

$AB$: sí, $2\times 4$.

$BA$: no ($B$ tiene 4 columnas y $A$ tiene 2 filas).

</details>
<details><summary>Errores frecuentes</summary>Mirar filas con filas.</details>

### F06-N2-21 · [K] ¿Está definido el producto?

**Objetivo**: decidir con los tamaños si $AB$ y $BA$ existen.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $2\times 2$ y $B$ de tamaño $3\times 3$. ¿Están definidos $AB$ y $BA$? Si lo están, ¿de qué tamaño son?

<details><summary>Pista 1</summary>Compara las columnas de la primera matriz con las filas de la segunda.</details>
<details><summary>Solución</summary>

$AB$: no ($A$ tiene 2 columnas y $B$ tiene 3 filas).

$BA$: no ($B$ tiene 3 columnas y $A$ tiene 2 filas).

</details>
<details><summary>Errores frecuentes</summary>Mirar filas con filas.</details>

### F06-N2-22 · [K] ¿Está definido el producto?

**Objetivo**: decidir con los tamaños si $AB$ y $BA$ existen.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $3\times 2$ y $B$ de tamaño $3\times 2$. ¿Están definidos $AB$ y $BA$? Si lo están, ¿de qué tamaño son?

<details><summary>Pista 1</summary>Compara las columnas de la primera matriz con las filas de la segunda.</details>
<details><summary>Solución</summary>

$AB$: no ($A$ tiene 2 columnas y $B$ tiene 3 filas).

$BA$: no ($B$ tiene 2 columnas y $A$ tiene 3 filas).

</details>
<details><summary>Errores frecuentes</summary>Mirar filas con filas.</details>

### F06-N2-23 · [K] ¿Está definido el producto?

**Objetivo**: decidir con los tamaños si $AB$ y $BA$ existen.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $4\times 2$ y $B$ de tamaño $2\times 2$. ¿Están definidos $AB$ y $BA$? Si lo están, ¿de qué tamaño son?

<details><summary>Pista 1</summary>Compara las columnas de la primera matriz con las filas de la segunda.</details>
<details><summary>Solución</summary>

$AB$: sí, $4\times 2$.

$BA$: no ($B$ tiene 2 columnas y $A$ tiene 4 filas).

</details>
<details><summary>Errores frecuentes</summary>Mirar filas con filas.</details>

### F06-N2-24 · [C] Efecto de una transformación

**Objetivo**: ver una matriz $2\times 2$ como transformación del plano.
**Dificultad**: N2

**Enunciado.** La matriz $T = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ define $\mathbf{x} \mapsto T\mathbf{x}$. Halla la imagen de $(1, 0)$, $(0, 1)$, $(2, 1)$ y describe qué hace $T$.

<details><summary>Pista 1</summary>Las columnas de $T$ son las imágenes de la base canónica.</details>
<details><summary>Solución</summary>

Imágenes: $T(1, 0) = (-1, 0)$, $T(0, 1) = (0, 1)$, $T(2, 1) = (-2, 1)$.

Las columnas de $T$ son las imágenes de $(1,0)$ y $(0,1)$. Es un reflexión en el eje $y$: refleja respecto del eje $y$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar el punto por la matriz en el orden contrario.</details>

### F06-N2-25 · [C] Efecto de una transformación

**Objetivo**: ver una matriz $2\times 2$ como transformación del plano.
**Dificultad**: N2

**Enunciado.** La matriz $T = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ define $\mathbf{x} \mapsto T\mathbf{x}$. Halla la imagen de $(1, 0)$, $(0, 1)$, $(-2, 1)$ y describe qué hace $T$.

<details><summary>Pista 1</summary>Las columnas de $T$ son las imágenes de la base canónica.</details>
<details><summary>Solución</summary>

Imágenes: $T(1, 0) = (-1, 0)$, $T(0, 1) = (0, 1)$, $T(-2, 1) = (2, 1)$.

Las columnas de $T$ son las imágenes de $(1,0)$ y $(0,1)$. Es un reflexión en el eje $y$: refleja respecto del eje $y$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar el punto por la matriz en el orden contrario.</details>

### F06-N2-26 · [C] Efecto de una transformación

**Objetivo**: ver una matriz $2\times 2$ como transformación del plano.
**Dificultad**: N2

**Enunciado.** La matriz $T = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$ define $\mathbf{x} \mapsto T\mathbf{x}$. Halla la imagen de $(1, 0)$, $(0, 1)$, $(3, 2)$ y describe qué hace $T$.

<details><summary>Pista 1</summary>Las columnas de $T$ son las imágenes de la base canónica.</details>
<details><summary>Solución</summary>

Imágenes: $T(1, 0) = (-1, 0)$, $T(0, 1) = (0, 1)$, $T(3, 2) = (-3, 2)$.

Las columnas de $T$ son las imágenes de $(1,0)$ y $(0,1)$. Es un reflexión en el eje $y$: refleja respecto del eje $y$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar el punto por la matriz en el orden contrario.</details>

### F06-N2-27 · [C] Efecto de una transformación

**Objetivo**: ver una matriz $2\times 2$ como transformación del plano.
**Dificultad**: N2

**Enunciado.** La matriz $T = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ define $\mathbf{x} \mapsto T\mathbf{x}$. Halla la imagen de $(1, 0)$, $(0, 1)$, $(3, 2)$ y describe qué hace $T$.

<details><summary>Pista 1</summary>Las columnas de $T$ son las imágenes de la base canónica.</details>
<details><summary>Solución</summary>

Imágenes: $T(1, 0) = (0, 1)$, $T(0, 1) = (-1, 0)$, $T(3, 2) = (-2, 3)$.

Las columnas de $T$ son las imágenes de $(1,0)$ y $(0,1)$. Es un giro de $90^\circ$: gira $90^\circ$ en sentido antihorario.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar el punto por la matriz en el orden contrario.</details>

### F06-N2-28 · [C] Efecto de una transformación

**Objetivo**: ver una matriz $2\times 2$ como transformación del plano.
**Dificultad**: N2

**Enunciado.** La matriz $T = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ define $\mathbf{x} \mapsto T\mathbf{x}$. Halla la imagen de $(1, 0)$, $(0, 1)$, $(3, 2)$ y describe qué hace $T$.

<details><summary>Pista 1</summary>Las columnas de $T$ son las imágenes de la base canónica.</details>
<details><summary>Solución</summary>

Imágenes: $T(1, 0) = (1, 0)$, $T(0, 1) = (0, 0)$, $T(3, 2) = (3, 0)$.

Las columnas de $T$ son las imágenes de $(1,0)$ y $(0,1)$. Es un proyección en el eje $x$: proyecta sobre el eje $x$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar el punto por la matriz en el orden contrario.</details>

### F06-N3-11 · [K] El producto no conmuta

**Objetivo**: comprobar con un ejemplo que $AB \ne BA$.
**Dificultad**: N3

**Enunciado.** Con $A = \begin{bmatrix} 2 & -2 \\ 0 & 0 \end{bmatrix}$ y $B = \begin{bmatrix} 0 & 0 \\ 3 & 3 \end{bmatrix}$, calcula $AB$ y $BA$ y comprueba que son distintos.

<details><summary>Pista 1</summary>Calcula los dos productos por separado.</details>
<details><summary>Solución</summary>

$AB = \begin{bmatrix} -6 & -6 \\ 0 & 0 \end{bmatrix}$ y $BA = \begin{bmatrix} 0 & 0 \\ 6 & -6 \end{bmatrix}$. Son distintas: el producto de matrices no es conmutativo.

</details>
<details><summary>Errores frecuentes</summary>Suponer que $AB = BA$ por analogía con los números.</details>

### F06-N3-12 · [K] El producto no conmuta

**Objetivo**: comprobar con un ejemplo que $AB \ne BA$.
**Dificultad**: N3

**Enunciado.** Con $A = \begin{bmatrix} -2 & 2 \\ 2 & 0 \end{bmatrix}$ y $B = \begin{bmatrix} 1 & 2 \\ -1 & 2 \end{bmatrix}$, calcula $AB$ y $BA$ y comprueba que son distintos.

<details><summary>Pista 1</summary>Calcula los dos productos por separado.</details>
<details><summary>Solución</summary>

$AB = \begin{bmatrix} -4 & 0 \\ 2 & 4 \end{bmatrix}$ y $BA = \begin{bmatrix} 2 & 2 \\ 6 & -2 \end{bmatrix}$. Son distintas: el producto de matrices no es conmutativo.

</details>
<details><summary>Errores frecuentes</summary>Suponer que $AB = BA$ por analogía con los números.</details>

### F06-N3-13 · [K] El producto no conmuta

**Objetivo**: comprobar con un ejemplo que $AB \ne BA$.
**Dificultad**: N3

**Enunciado.** Con $A = \begin{bmatrix} 0 & 3 \\ 2 & 1 \end{bmatrix}$ y $B = \begin{bmatrix} 1 & -1 \\ 1 & -2 \end{bmatrix}$, calcula $AB$ y $BA$ y comprueba que son distintos.

<details><summary>Pista 1</summary>Calcula los dos productos por separado.</details>
<details><summary>Solución</summary>

$AB = \begin{bmatrix} 3 & -6 \\ 3 & -4 \end{bmatrix}$ y $BA = \begin{bmatrix} -2 & 2 \\ -4 & 1 \end{bmatrix}$. Son distintas: el producto de matrices no es conmutativo.

</details>
<details><summary>Errores frecuentes</summary>Suponer que $AB = BA$ por analogía con los números.</details>

### F06-N3-14 · [C] Composición de transformaciones

**Objetivo**: ver el producto de matrices como composición.
**Dificultad**: N3

**Enunciado.** $S$ tiene matriz $A = \begin{bmatrix} 1 & 3 \\ 3 & 2 \end{bmatrix}$ y $T$ tiene matriz $B = \begin{bmatrix} -2 & 1 \\ -2 & 1 \end{bmatrix}$. a) Halla la matriz de $T \circ S$ (primero $S$, luego $T$). b) Compruébalo con $\mathbf{x} = (1, -3)$.

<details><summary>Pista 1</summary>$T(S(\mathbf{x})) = B(A\mathbf{x}) = (BA)\mathbf{x}$.</details>
<details><summary>Solución</summary>

a) La matriz es $BA = \begin{bmatrix} 1 & -4 \\ 1 & -4 \end{bmatrix}$ (la primera transformación se escribe a la derecha).

b) $A\mathbf{x} = (-8, -3)$ y $B(A\mathbf{x}) = (13, 13)$; por otro lado $(BA)\mathbf{x} = (13, 13)$. Coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir $AB$ en lugar de $BA$.</details>

### F06-N3-15 · [C] Composición de transformaciones

**Objetivo**: ver el producto de matrices como composición.
**Dificultad**: N3

**Enunciado.** $S$ tiene matriz $A = \begin{bmatrix} 0 & -2 \\ 3 & -2 \end{bmatrix}$ y $T$ tiene matriz $B = \begin{bmatrix} 1 & 2 \\ -1 & -1 \end{bmatrix}$. a) Halla la matriz de $T \circ S$ (primero $S$, luego $T$). b) Compruébalo con $\mathbf{x} = (3, 2)$.

<details><summary>Pista 1</summary>$T(S(\mathbf{x})) = B(A\mathbf{x}) = (BA)\mathbf{x}$.</details>
<details><summary>Solución</summary>

a) La matriz es $BA = \begin{bmatrix} 6 & -6 \\ -3 & 4 \end{bmatrix}$ (la primera transformación se escribe a la derecha).

b) $A\mathbf{x} = (-4, 5)$ y $B(A\mathbf{x}) = (6, -1)$; por otro lado $(BA)\mathbf{x} = (6, -1)$. Coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir $AB$ en lugar de $BA$.</details>

### F06-N3-16 · [C] Composición de transformaciones

**Objetivo**: ver el producto de matrices como composición.
**Dificultad**: N3

**Enunciado.** $S$ tiene matriz $A = \begin{bmatrix} -2 & 1 \\ 0 & 3 \end{bmatrix}$ y $T$ tiene matriz $B = \begin{bmatrix} 2 & 3 \\ 0 & 2 \end{bmatrix}$. a) Halla la matriz de $T \circ S$ (primero $S$, luego $T$). b) Compruébalo con $\mathbf{x} = (-1, -1)$.

<details><summary>Pista 1</summary>$T(S(\mathbf{x})) = B(A\mathbf{x}) = (BA)\mathbf{x}$.</details>
<details><summary>Solución</summary>

a) La matriz es $BA = \begin{bmatrix} -4 & 11 \\ 0 & 6 \end{bmatrix}$ (la primera transformación se escribe a la derecha).

b) $A\mathbf{x} = (1, -3)$ y $B(A\mathbf{x}) = (-7, -6)$; por otro lado $(BA)\mathbf{x} = (-7, -6)$. Coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir $AB$ en lugar de $BA$.</details>

