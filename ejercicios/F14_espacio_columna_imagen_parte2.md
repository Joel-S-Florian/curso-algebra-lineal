# F14 — Espacio columna e imagen (parte 2)

Segunda parte del banco de las lecciones L48–L50: **26 ejercicios** de práctica que completan la parte 1 (`F14_espacio_columna_imagen.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N2: 6, N3: 20 · [C] 21, [K] 5.

---

### F14-N2-11 · [C] ¿Está $\mathbf{b}$ en $\operatorname{Col}(A)$?

**Objetivo**: decidir la existencia de solución con rangos.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} -1 & 1 & -2 & 2 \\ 0 & 9 & 3 & 6 \\ 0 & 3 & 1 & 2 \end{bmatrix}$, ¿tiene solución $A\mathbf{x} = \begin{bmatrix} -5 \\ 13 \\ 4 \end{bmatrix}$?

<details><summary>Pista 1</summary>$\mathbf{b} \in \operatorname{Col}(A)$ si y solo si añadir $\mathbf{b}$ no crea un pivote nuevo.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 3$. No coinciden: $\mathbf{b} \notin \operatorname{Col}(A)$ y el sistema es incompatible.

</details>
<details><summary>Errores frecuentes</summary>Comparar $\operatorname{rg}(A)$ con el número de filas.</details>

### F14-N2-12 · [C] ¿Está $\mathbf{b}$ en $\operatorname{Col}(A)$?

**Objetivo**: decidir la existencia de solución con rangos.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 7 & -5 & -3 & 9 \\ -3 & 0 & 7 & -6 \\ -5 & 4 & 1 & -6 \end{bmatrix}$, ¿tiene solución $A\mathbf{x} = \begin{bmatrix} 5 \\ 14 \\ -6 \end{bmatrix}$?

<details><summary>Pista 1</summary>$\mathbf{b} \in \operatorname{Col}(A)$ si y solo si añadir $\mathbf{b}$ no crea un pivote nuevo.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 3$. No coinciden: $\mathbf{b} \notin \operatorname{Col}(A)$ y el sistema es incompatible.

</details>
<details><summary>Errores frecuentes</summary>Comparar $\operatorname{rg}(A)$ con el número de filas.</details>

### F14-N2-13 · [C] ¿Está $\mathbf{b}$ en $\operatorname{Col}(A)$?

**Objetivo**: decidir la existencia de solución con rangos.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 2 & 0 & -4 & 0 \\ -4 & 3 & 2 & 3 \\ 1 & 0 & -2 & 0 \end{bmatrix}$, ¿tiene solución $A\mathbf{x} = \begin{bmatrix} -9 \\ 20 \\ -5 \end{bmatrix}$?

<details><summary>Pista 1</summary>$\mathbf{b} \in \operatorname{Col}(A)$ si y solo si añadir $\mathbf{b}$ no crea un pivote nuevo.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 3$. No coinciden: $\mathbf{b} \notin \operatorname{Col}(A)$ y el sistema es incompatible.

</details>
<details><summary>Errores frecuentes</summary>Comparar $\operatorname{rg}(A)$ con el número de filas.</details>

### F14-N2-14 · [C] ¿Está $\mathbf{b}$ en $\operatorname{Col}(A)$?

**Objetivo**: decidir la existencia de solución con rangos.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 6 & 4 & 0 & 6 \\ -8 & -4 & 3 & -6 \\ -6 & 0 & 9 & 0 \end{bmatrix}$, ¿tiene solución $A\mathbf{x} = \begin{bmatrix} 21 \\ -30 \\ -30 \end{bmatrix}$?

<details><summary>Pista 1</summary>$\mathbf{b} \in \operatorname{Col}(A)$ si y solo si añadir $\mathbf{b}$ no crea un pivote nuevo.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 3$. No coinciden: $\mathbf{b} \notin \operatorname{Col}(A)$ y el sistema es incompatible.

</details>
<details><summary>Errores frecuentes</summary>Comparar $\operatorname{rg}(A)$ con el número de filas.</details>

### F14-N2-15 · [C] ¿Está $\mathbf{b}$ en $\operatorname{Col}(A)$?

**Objetivo**: decidir la existencia de solución con rangos.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} -6 & 9 & -6 & 6 \\ -2 & 3 & -2 & 2 \\ -2 & 6 & 4 & 2 \end{bmatrix}$, ¿tiene solución $A\mathbf{x} = \begin{bmatrix} 7 \\ 2 \\ 14 \end{bmatrix}$?

<details><summary>Pista 1</summary>$\mathbf{b} \in \operatorname{Col}(A)$ si y solo si añadir $\mathbf{b}$ no crea un pivote nuevo.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 3$. No coinciden: $\mathbf{b} \notin \operatorname{Col}(A)$ y el sistema es incompatible.

</details>
<details><summary>Errores frecuentes</summary>Comparar $\operatorname{rg}(A)$ con el número de filas.</details>

### F14-N2-16 · [C] ¿Está $\mathbf{b}$ en $\operatorname{Col}(A)$?

**Objetivo**: decidir la existencia de solución con rangos.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} -1 & 2 & -2 & 0 \\ 2 & 2 & -2 & -3 \\ 4 & -2 & 2 & -3 \end{bmatrix}$, ¿tiene solución $A\mathbf{x} = \begin{bmatrix} 9 \\ 0 \\ -18 \end{bmatrix}$?

<details><summary>Pista 1</summary>$\mathbf{b} \in \operatorname{Col}(A)$ si y solo si añadir $\mathbf{b}$ no crea un pivote nuevo.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 2$. Coinciden: $\mathbf{b} \in \operatorname{Col}(A)$ y el sistema tiene solución.

</details>
<details><summary>Errores frecuentes</summary>Comparar $\operatorname{rg}(A)$ con el número de filas.</details>

### F14-N3-11 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} -5 & 1 & 1 & 1 & 1 \\ 1 & -3 & 6 & -2 & 6 \\ -4 & -4 & 9 & 5 & 9 \\ 0 & 0 & 1 & -3 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 2, 3. Base: $(-5, 1, -4, 0)$, $(1, -3, -4, 0)$, $(1, 6, 9, 1)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 3$. Relaciones (leídas en la reducida): $\mathbf{a}_4 = (-2)\mathbf{a}_1 + (-6)\mathbf{a}_2 + (-3)\mathbf{a}_3$; $\mathbf{a}_5 = 1\mathbf{a}_3$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-12 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} 4 & 4 & -1 & 6 \\ -5 & 8 & 0 & -9 \\ -5 & 0 & 5 & -3 \\ 8 & -4 & -7 & 6 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 2, 3. Base: $(4, -5, -5, 8)$, $(4, 8, 0, -4)$, $(-1, 0, 5, -7)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 3$. Relaciones (leídas en la reducida): $\mathbf{a}_4 = (\frac{9}{5})\mathbf{a}_1 + (\frac{6}{5})\mathbf{a}_3$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-13 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} -2 & -3 & -3 & 0 \\ -8 & 3 & -4 & -1 \\ -3 & 2 & -8 & 4 \\ -4 & -1 & 4 & -5 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 2, 3. Base: $(-2, -8, -3, -4)$, $(-3, 3, 2, -1)$, $(-3, -4, -8, 4)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 3$. Relaciones (leídas en la reducida): $\mathbf{a}_4 = (\frac{6}{11})\mathbf{a}_1 + (\frac{3}{11})\mathbf{a}_2 + (-\frac{7}{11})\mathbf{a}_3$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-14 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} 9 & 5 & -4 & 3 & 5 \\ -1 & 3 & -4 & -3 & 3 \\ 7 & -5 & 8 & 9 & -5 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 2. Base: $(9, -1, 7)$, $(5, 3, -5)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 2$. Relaciones (leídas en la reducida): $\mathbf{a}_3 = (\frac{1}{4})\mathbf{a}_1 + (-\frac{5}{4})\mathbf{a}_2$; $\mathbf{a}_4 = (\frac{3}{4})\mathbf{a}_1 + (-\frac{3}{4})\mathbf{a}_2$; $\mathbf{a}_5 = 1\mathbf{a}_2$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-15 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} 0 & -4 & -4 & 2 \\ -2 & -4 & -4 & -1 \\ 3 & -9 & -9 & 9 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 2. Base: $(0, -2, 3)$, $(-4, -4, -9)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 2$. Relaciones (leídas en la reducida): $\mathbf{a}_3 = 1\mathbf{a}_2$; $\mathbf{a}_4 = (\frac{3}{2})\mathbf{a}_1 + (-\frac{1}{2})\mathbf{a}_2$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-16 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} -3 & -2 & 1 & -1 \\ 3 & 2 & -1 & 1 \\ -3 & -2 & 3 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 3. Base: $(-3, 3, -3)$, $(1, -1, 3)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 2$. Relaciones (leídas en la reducida): $\mathbf{a}_2 = (\frac{2}{3})\mathbf{a}_1$; $\mathbf{a}_4 = (\frac{2}{3})\mathbf{a}_1 + 1\mathbf{a}_3$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-17 · [C] Base del espacio columna

**Objetivo**: tomar las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y escribe las demás columnas con ella: $A = \begin{bmatrix} -2 & 0 & -1 & 3 \\ -4 & -1 & -3 & 7 \\ 0 & -1 & -1 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las columnas con pivote de la reducida indican qué columnas de $A$ tomar.</details>
<details><summary>Solución</summary>

Pivotes en las columnas 1, 2. Base: $(-2, -4, 0)$, $(0, -1, -1)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A) = 2$. Relaciones (leídas en la reducida): $\mathbf{a}_3 = (\frac{1}{2})\mathbf{a}_1 + 1\mathbf{a}_2$; $\mathbf{a}_4 = (-\frac{3}{2})\mathbf{a}_1 + (-1)\mathbf{a}_2$.

</details>
<details><summary>Errores frecuentes</summary>Usar las columnas de la reducida.</details>

### F14-N3-18 · [C] Comprobar rango + nulidad

**Objetivo**: verificar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$ en un ejemplo.
**Dificultad**: N3

**Enunciado.** Para $A = \begin{bmatrix} 9 & 6 & 6 \\ -6 & -4 & -4 \\ 6 & 4 & 4 \end{bmatrix}$ halla $\operatorname{rg}(A)$, una base de $\ker A$ y comprueba que $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.

<details><summary>Pista 1</summary>El rango es el número de pivotes; la nulidad, el de variables libres.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 1$. Base de $\ker A$: $(-\frac{2}{3}, 1, 0)$, $(-\frac{2}{3}, 0, 1)$. $\operatorname{nul}(A) = 2$. Suma: $1 + 2 = 3 = n$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que $n$ es el número de columnas, no de filas.</details>

### F14-N3-19 · [C] Comprobar rango + nulidad

**Objetivo**: verificar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$ en un ejemplo.
**Dificultad**: N3

**Enunciado.** Para $A = \begin{bmatrix} 6 & -2 & 8 & 6 & 6 \\ -3 & -4 & -1 & 4 & 7 \\ 0 & 3 & -2 & -4 & -6 \\ 6 & 2 & 7 & -1 & -2 \end{bmatrix}$ halla $\operatorname{rg}(A)$, una base de $\ker A$ y comprueba que $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.

<details><summary>Pista 1</summary>El rango es el número de pivotes; la nulidad, el de variables libres.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 3$. Base de $\ker A$: $(-\frac{5}{3}, 2, 1, 1, 0)$, $(-\frac{1}{3}, 2, 0, 0, 1)$. $\operatorname{nul}(A) = 2$. Suma: $3 + 2 = 5 = n$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que $n$ es el número de columnas, no de filas.</details>

### F14-N3-20 · [C] Comprobar rango + nulidad

**Objetivo**: verificar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$ en un ejemplo.
**Dificultad**: N3

**Enunciado.** Para $A = \begin{bmatrix} 8 & -4 & -2 \\ -4 & 4 & -4 \\ -2 & 6 & 3 \\ -8 & -2 & 2 \end{bmatrix}$ halla $\operatorname{rg}(A)$, una base de $\ker A$ y comprueba que $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.

<details><summary>Pista 1</summary>El rango es el número de pivotes; la nulidad, el de variables libres.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 3$. Base de $\ker A$: vacía (núcleo trivial). $\operatorname{nul}(A) = 0$. Suma: $3 + 0 = 3 = n$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que $n$ es el número de columnas, no de filas.</details>

### F14-N3-21 · [C] Comprobar rango + nulidad

**Objetivo**: verificar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$ en un ejemplo.
**Dificultad**: N3

**Enunciado.** Para $A = \begin{bmatrix} 3 & -3 & -2 & 9 & 5 \\ -1 & 9 & 3 & -9 & 1 \\ 2 & 4 & -3 & -9 & -3 \\ 2 & 0 & 3 & 9 & 7 \end{bmatrix}$ halla $\operatorname{rg}(A)$, una base de $\ker A$ y comprueba que $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.

<details><summary>Pista 1</summary>El rango es el número de pivotes; la nulidad, el de variables libres.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 4$. Base de $\ker A$: $(\frac{1}{16}, -\frac{17}{16}, \frac{1}{4}, -\frac{7}{8}, 1)$. $\operatorname{nul}(A) = 1$. Suma: $4 + 1 = 5 = n$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que $n$ es el número de columnas, no de filas.</details>

### F14-N3-22 · [C] Comprobar rango + nulidad

**Objetivo**: verificar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$ en un ejemplo.
**Dificultad**: N3

**Enunciado.** Para $A = \begin{bmatrix} -3 & 5 & 1 \\ 4 & -8 & -2 \\ 4 & -6 & -1 \\ -1 & 3 & 1 \end{bmatrix}$ halla $\operatorname{rg}(A)$, una base de $\ker A$ y comprueba que $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.

<details><summary>Pista 1</summary>El rango es el número de pivotes; la nulidad, el de variables libres.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$. Base de $\ker A$: $(-\frac{1}{2}, -\frac{1}{2}, 1)$. $\operatorname{nul}(A) = 1$. Suma: $2 + 1 = 3 = n$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que $n$ es el número de columnas, no de filas.</details>

### F14-N3-23 · [C] Imagen y núcleo de una transformación

**Objetivo**: describir la imagen y el núcleo de $T(\mathbf{x}) = A\mathbf{x}$.
**Dificultad**: N3

**Enunciado.** Para $T : \mathbb{R}^2 \to \mathbb{R}^3$, $T(\mathbf{x}) = A\mathbf{x}$ con $A = \begin{bmatrix} 3 & -5 \\ 6 & -6 \\ 8 & -4 \end{bmatrix}$, describe $\operatorname{Im}(T)$ y $\ker T$ (dimensión y una base).

<details><summary>Pista 1</summary>La imagen es el espacio columna.</details>
<details><summary>Solución</summary>

$\operatorname{Im}(T) = \operatorname{Col}(A)$ tiene base $(3, 6, 8)$, $(-5, -6, -4)$ y dimensión 2. $\ker T = \{\mathbf{0}\}$: $T$ es inyectiva. Comprobación: $2 + 0 = 2$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el espacio de llegada con la imagen.</details>

### F14-N3-24 · [C] Imagen y núcleo de una transformación

**Objetivo**: describir la imagen y el núcleo de $T(\mathbf{x}) = A\mathbf{x}$.
**Dificultad**: N3

**Enunciado.** Para $T : \mathbb{R}^2 \to \mathbb{R}^2$, $T(\mathbf{x}) = A\mathbf{x}$ con $A = \begin{bmatrix} -1 & 2 \\ -2 & 4 \end{bmatrix}$, describe $\operatorname{Im}(T)$ y $\ker T$ (dimensión y una base).

<details><summary>Pista 1</summary>La imagen es el espacio columna.</details>
<details><summary>Solución</summary>

$\operatorname{Im}(T) = \operatorname{Col}(A)$ tiene base $(-1, -2)$ y dimensión 1. $\ker T$ tiene dimensión $1$ y base $(2, 1)$. Comprobación: $1 + 1 = 2$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el espacio de llegada con la imagen.</details>

### F14-N3-25 · [C] Imagen y núcleo de una transformación

**Objetivo**: describir la imagen y el núcleo de $T(\mathbf{x}) = A\mathbf{x}$.
**Dificultad**: N3

**Enunciado.** Para $T : \mathbb{R}^2 \to \mathbb{R}^2$, $T(\mathbf{x}) = A\mathbf{x}$ con $A = \begin{bmatrix} 2 & -1 \\ 4 & -2 \end{bmatrix}$, describe $\operatorname{Im}(T)$ y $\ker T$ (dimensión y una base).

<details><summary>Pista 1</summary>La imagen es el espacio columna.</details>
<details><summary>Solución</summary>

$\operatorname{Im}(T) = \operatorname{Col}(A)$ tiene base $(2, 4)$ y dimensión 1. $\ker T$ tiene dimensión $1$ y base $(\frac{1}{2}, 1)$. Comprobación: $1 + 1 = 2$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el espacio de llegada con la imagen.</details>

### F14-N3-26 · [K] Preguntas de rango y nulidad

**Objetivo**: razonar con rango-nulidad sin calcular.
**Dificultad**: N3

**Enunciado.** a) Si $A$ es cuadrada $n\times n$ con $\operatorname{rg}(A) = n$, ¿qué pasa con $\ker A$ y con $\operatorname{Col}(A)$?

b) Una matriz $5\times 7$ tiene rango 3. ¿Cuál es la nulidad y en qué espacio vive $\operatorname{Col}(A)$?

c) ¿Puede $A\mathbf{x} = \mathbf{b}$ tener solución para todo $\mathbf{b}$ si $A$ es $5\times 3$?

<details><summary>Pista 1</summary>Usa $\operatorname{rg} + \operatorname{nul} = n$ y $\operatorname{rg} \le \min(m, n)$.</details>
<details><summary>Solución</summary>

a) $\ker A = \{\mathbf{0}\}$ y $\operatorname{Col}(A) = \mathbb{R}^n$: hay solución única para todo $\mathbf{b}$.

b) $\operatorname{nul} = 7 - 3 = 4$; $\operatorname{Col}(A) \subseteq \mathbb{R}^5$ con dimensión $3$.

c) No: $\operatorname{rg} \le 3 < 5$, luego $\operatorname{Col}(A) \ne \mathbb{R}^5$.

</details>
<details><summary>Errores frecuentes</summary>Mezclar $m$ y $n$.</details>

### F14-N3-27 · [K] Preguntas de rango y nulidad

**Objetivo**: razonar con rango-nulidad sin calcular.
**Dificultad**: N3

**Enunciado.** a) ¿Puede $A\mathbf{x} = \mathbf{b}$ tener solución para todo $\mathbf{b}$ si $A$ es $5\times 3$?

b) ¿Es posible que $\dim\operatorname{Col}(A) > m$ para una matriz $m \times n$?

c) Si $A$ es cuadrada $n\times n$ con $\operatorname{rg}(A) = n$, ¿qué pasa con $\ker A$ y con $\operatorname{Col}(A)$?

<details><summary>Pista 1</summary>Usa $\operatorname{rg} + \operatorname{nul} = n$ y $\operatorname{rg} \le \min(m, n)$.</details>
<details><summary>Solución</summary>

a) No: $\operatorname{rg} \le 3 < 5$, luego $\operatorname{Col}(A) \ne \mathbb{R}^5$.

b) No: $\operatorname{Col}(A) \subseteq \mathbb{R}^m$, así que su dimensión es a lo sumo $m$.

c) $\ker A = \{\mathbf{0}\}$ y $\operatorname{Col}(A) = \mathbb{R}^n$: hay solución única para todo $\mathbf{b}$.

</details>
<details><summary>Errores frecuentes</summary>Mezclar $m$ y $n$.</details>

### F14-N3-28 · [K] Preguntas de rango y nulidad

**Objetivo**: razonar con rango-nulidad sin calcular.
**Dificultad**: N3

**Enunciado.** a) Las operaciones por filas, ¿conservan $\ker A$? ¿Y $\operatorname{Col}(A)$?

b) ¿Puede $A\mathbf{x} = \mathbf{b}$ tener solución para todo $\mathbf{b}$ si $A$ es $5\times 3$?

c) ¿Puede una matriz $3\times 5$ tener $\ker A = \{\mathbf{0}\}$?

<details><summary>Pista 1</summary>Usa $\operatorname{rg} + \operatorname{nul} = n$ y $\operatorname{rg} \le \min(m, n)$.</details>
<details><summary>Solución</summary>

a) Conservan el núcleo ($A\mathbf{x} = \mathbf{0} \iff R\mathbf{x} = \mathbf{0}$) pero no el espacio columna; por eso la base de $\operatorname{Col}(A)$ se toma de la matriz original.

b) No: $\operatorname{rg} \le 3 < 5$, luego $\operatorname{Col}(A) \ne \mathbb{R}^5$.

c) No: $\operatorname{nul} \ge 5 - 3 = 2$.

</details>
<details><summary>Errores frecuentes</summary>Mezclar $m$ y $n$.</details>

### F14-N3-29 · [K] Preguntas de rango y nulidad

**Objetivo**: razonar con rango-nulidad sin calcular.
**Dificultad**: N3

**Enunciado.** a) Una matriz $5\times 7$ tiene rango 3. ¿Cuál es la nulidad y en qué espacio vive $\operatorname{Col}(A)$?

b) Las operaciones por filas, ¿conservan $\ker A$? ¿Y $\operatorname{Col}(A)$?

c) ¿Puede $A\mathbf{x} = \mathbf{b}$ tener solución para todo $\mathbf{b}$ si $A$ es $5\times 3$?

<details><summary>Pista 1</summary>Usa $\operatorname{rg} + \operatorname{nul} = n$ y $\operatorname{rg} \le \min(m, n)$.</details>
<details><summary>Solución</summary>

a) $\operatorname{nul} = 7 - 3 = 4$; $\operatorname{Col}(A) \subseteq \mathbb{R}^5$ con dimensión $3$.

b) Conservan el núcleo ($A\mathbf{x} = \mathbf{0} \iff R\mathbf{x} = \mathbf{0}$) pero no el espacio columna; por eso la base de $\operatorname{Col}(A)$ se toma de la matriz original.

c) No: $\operatorname{rg} \le 3 < 5$, luego $\operatorname{Col}(A) \ne \mathbb{R}^5$.

</details>
<details><summary>Errores frecuentes</summary>Mezclar $m$ y $n$.</details>

### F14-N3-30 · [K] Preguntas de rango y nulidad

**Objetivo**: razonar con rango-nulidad sin calcular.
**Dificultad**: N3

**Enunciado.** a) ¿Es posible que $\dim\operatorname{Col}(A) > m$ para una matriz $m \times n$?

b) ¿Puede una matriz $3\times 5$ tener $\ker A = \{\mathbf{0}\}$?

c) Si $A$ es cuadrada $n\times n$ con $\operatorname{rg}(A) = n$, ¿qué pasa con $\ker A$ y con $\operatorname{Col}(A)$?

<details><summary>Pista 1</summary>Usa $\operatorname{rg} + \operatorname{nul} = n$ y $\operatorname{rg} \le \min(m, n)$.</details>
<details><summary>Solución</summary>

a) No: $\operatorname{Col}(A) \subseteq \mathbb{R}^m$, así que su dimensión es a lo sumo $m$.

b) No: $\operatorname{nul} \ge 5 - 3 = 2$.

c) $\ker A = \{\mathbf{0}\}$ y $\operatorname{Col}(A) = \mathbb{R}^n$: hay solución única para todo $\mathbf{b}$.

</details>
<details><summary>Errores frecuentes</summary>Mezclar $m$ y $n$.</details>

