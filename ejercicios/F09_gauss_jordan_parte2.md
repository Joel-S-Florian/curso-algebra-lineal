# F09 — Gauss-Jordan (parte 2)

Segunda parte del banco de las lecciones L31–L33: **23 ejercicios** de práctica que completan la parte 1 (`F09_gauss_jordan.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N2: 9, N3: 14 · [C] 18, [K] 5.

---

### F09-N2-11 · [C] Gauss-Jordan hasta la reducida

**Objetivo**: llevar $[A \mid \mathbf{b}]$ a su forma escalonada reducida y leer la solución.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss-Jordan $\begin{cases} 3x - y + 3z = 0 \\ -2x - 3y - 3z = 9 \\ 2y - z = -8 \end{cases}$.

<details><summary>Pista 1</summary>Convierte cada pivote en $1$ y haz ceros también por encima.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 3 & -1 & 3 & 0 \\ -2 & -3 & -3 & 9 \\ 0 & 2 & -1 & -8 \end{array}\right] $$
$$\xrightarrow{R_1 \leftarrow (\frac{1}{3})R_1} \left[\begin{array}{ccc|c} 1 & -\frac{1}{3} & 1 & 0 \\ -2 & -3 & -3 & 9 \\ 0 & 2 & -1 & -8 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 + 2R_1} \left[\begin{array}{ccc|c} 1 & -\frac{1}{3} & 1 & 0 \\ 0 & -\frac{11}{3} & -1 & 9 \\ 0 & 2 & -1 & -8 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow (-\frac{3}{11})R_2} \left[\begin{array}{ccc|c} 1 & -\frac{1}{3} & 1 & 0 \\ 0 & 1 & \frac{3}{11} & -\frac{27}{11} \\ 0 & 2 & -1 & -8 \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 + \frac{1}{3}R_2} \left[\begin{array}{ccc|c} 1 & 0 & \frac{12}{11} & -\frac{9}{11} \\ 0 & 1 & \frac{3}{11} & -\frac{27}{11} \\ 0 & 2 & -1 & -8 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 2R_2} \left[\begin{array}{ccc|c} 1 & 0 & \frac{12}{11} & -\frac{9}{11} \\ 0 & 1 & \frac{3}{11} & -\frac{27}{11} \\ 0 & 0 & -\frac{17}{11} & -\frac{34}{11} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow (-\frac{11}{17})R_3} \left[\begin{array}{ccc|c} 1 & 0 & \frac{12}{11} & -\frac{9}{11} \\ 0 & 1 & \frac{3}{11} & -\frac{27}{11} \\ 0 & 0 & 1 & 2 \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 - \frac{12}{11}R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & -3 \\ 0 & 1 & \frac{3}{11} & -\frac{27}{11} \\ 0 & 0 & 1 & 2 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 - \frac{3}{11}R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & -3 \\ 0 & 1 & 0 & -3 \\ 0 & 0 & 1 & 2 \end{array}\right]$$

La reducida tiene la identidad a la izquierda: la solución se lee en la última columna, $(-3, -3, 2)$.

</details>
<details><summary>Errores frecuentes</summary>Dejar sin anular las entradas por encima de un pivote.</details>

### F09-N2-12 · [C] Gauss-Jordan hasta la reducida

**Objetivo**: llevar $[A \mid \mathbf{b}]$ a su forma escalonada reducida y leer la solución.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss-Jordan $\begin{cases} x - 3z = -7 \\ 3x - 2z = 0 \\ -x - 2y - 3z = -11 \end{cases}$.

<details><summary>Pista 1</summary>Convierte cada pivote en $1$ y haz ceros también por encima.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & 0 & -3 & -7 \\ 3 & 0 & -2 & 0 \\ -1 & -2 & -3 & -11 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - 3R_1} \left[\begin{array}{ccc|c} 1 & 0 & -3 & -7 \\ 0 & 0 & 7 & 21 \\ -1 & -2 & -3 & -11 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + R_1} \left[\begin{array}{ccc|c} 1 & 0 & -3 & -7 \\ 0 & 0 & 7 & 21 \\ 0 & -2 & -6 & -18 \end{array}\right]$$
$$\xrightarrow{R_2 \leftrightarrow R_3} \left[\begin{array}{ccc|c} 1 & 0 & -3 & -7 \\ 0 & -2 & -6 & -18 \\ 0 & 0 & 7 & 21 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow (-\frac{1}{2})R_2} \left[\begin{array}{ccc|c} 1 & 0 & -3 & -7 \\ 0 & 1 & 3 & 9 \\ 0 & 0 & 7 & 21 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow (\frac{1}{7})R_3} \left[\begin{array}{ccc|c} 1 & 0 & -3 & -7 \\ 0 & 1 & 3 & 9 \\ 0 & 0 & 1 & 3 \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 + 3R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 2 \\ 0 & 1 & 3 & 9 \\ 0 & 0 & 1 & 3 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 - 3R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 3 \end{array}\right]$$

La reducida tiene la identidad a la izquierda: la solución se lee en la última columna, $(2, 0, 3)$.

</details>
<details><summary>Errores frecuentes</summary>Dejar sin anular las entradas por encima de un pivote.</details>

### F09-N2-13 · [C] Gauss-Jordan hasta la reducida

**Objetivo**: llevar $[A \mid \mathbf{b}]$ a su forma escalonada reducida y leer la solución.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss-Jordan $\begin{cases} 3x - 3y - z = 20 \\ -2x + 3y + 3z = -22 \\ -x - y - z = 4 \end{cases}$.

<details><summary>Pista 1</summary>Convierte cada pivote en $1$ y haz ceros también por encima.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 3 & -3 & -1 & 20 \\ -2 & 3 & 3 & -22 \\ -1 & -1 & -1 & 4 \end{array}\right] $$
$$\xrightarrow{R_1 \leftarrow (\frac{1}{3})R_1} \left[\begin{array}{ccc|c} 1 & -1 & -\frac{1}{3} & \frac{20}{3} \\ -2 & 3 & 3 & -22 \\ -1 & -1 & -1 & 4 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 + 2R_1} \left[\begin{array}{ccc|c} 1 & -1 & -\frac{1}{3} & \frac{20}{3} \\ 0 & 1 & \frac{7}{3} & -\frac{26}{3} \\ -1 & -1 & -1 & 4 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + R_1} \left[\begin{array}{ccc|c} 1 & -1 & -\frac{1}{3} & \frac{20}{3} \\ 0 & 1 & \frac{7}{3} & -\frac{26}{3} \\ 0 & -2 & -\frac{4}{3} & \frac{32}{3} \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 + R_2} \left[\begin{array}{ccc|c} 1 & 0 & 2 & -2 \\ 0 & 1 & \frac{7}{3} & -\frac{26}{3} \\ 0 & -2 & -\frac{4}{3} & \frac{32}{3} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + 2R_2} \left[\begin{array}{ccc|c} 1 & 0 & 2 & -2 \\ 0 & 1 & \frac{7}{3} & -\frac{26}{3} \\ 0 & 0 & \frac{10}{3} & -\frac{20}{3} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow (\frac{3}{10})R_3} \left[\begin{array}{ccc|c} 1 & 0 & 2 & -2 \\ 0 & 1 & \frac{7}{3} & -\frac{26}{3} \\ 0 & 0 & 1 & -2 \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 - 2R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 2 \\ 0 & 1 & \frac{7}{3} & -\frac{26}{3} \\ 0 & 0 & 1 & -2 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 - \frac{7}{3}R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & -4 \\ 0 & 0 & 1 & -2 \end{array}\right]$$

La reducida tiene la identidad a la izquierda: la solución se lee en la última columna, $(2, -4, -2)$.

</details>
<details><summary>Errores frecuentes</summary>Dejar sin anular las entradas por encima de un pivote.</details>

### F09-N2-14 · [C] Gauss-Jordan hasta la reducida

**Objetivo**: llevar $[A \mid \mathbf{b}]$ a su forma escalonada reducida y leer la solución.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss-Jordan $\begin{cases} -x - y = 6 \\ x - 2y + 2z = 8 \\ -3x + 2y + z = -1 \end{cases}$.

<details><summary>Pista 1</summary>Convierte cada pivote en $1$ y haz ceros también por encima.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -1 & -1 & 0 & 6 \\ 1 & -2 & 2 & 8 \\ -3 & 2 & 1 & -1 \end{array}\right] $$
$$\xrightarrow{R_1 \leftarrow (-1)R_1} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -6 \\ 1 & -2 & 2 & 8 \\ -3 & 2 & 1 & -1 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 - R_1} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -6 \\ 0 & -3 & 2 & 14 \\ -3 & 2 & 1 & -1 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + 3R_1} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -6 \\ 0 & -3 & 2 & 14 \\ 0 & 5 & 1 & -19 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow (-\frac{1}{3})R_2} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -6 \\ 0 & 1 & -\frac{2}{3} & -\frac{14}{3} \\ 0 & 5 & 1 & -19 \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 - R_2} \left[\begin{array}{ccc|c} 1 & 0 & \frac{2}{3} & -\frac{4}{3} \\ 0 & 1 & -\frac{2}{3} & -\frac{14}{3} \\ 0 & 5 & 1 & -19 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 5R_2} \left[\begin{array}{ccc|c} 1 & 0 & \frac{2}{3} & -\frac{4}{3} \\ 0 & 1 & -\frac{2}{3} & -\frac{14}{3} \\ 0 & 0 & \frac{13}{3} & \frac{13}{3} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow (\frac{3}{13})R_3} \left[\begin{array}{ccc|c} 1 & 0 & \frac{2}{3} & -\frac{4}{3} \\ 0 & 1 & -\frac{2}{3} & -\frac{14}{3} \\ 0 & 0 & 1 & 1 \end{array}\right]$$
$$\xrightarrow{R_1 \leftarrow R_1 - \frac{2}{3}R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & -2 \\ 0 & 1 & -\frac{2}{3} & -\frac{14}{3} \\ 0 & 0 & 1 & 1 \end{array}\right]$$
$$\xrightarrow{R_2 \leftarrow R_2 + \frac{2}{3}R_3} \left[\begin{array}{ccc|c} 1 & 0 & 0 & -2 \\ 0 & 1 & 0 & -4 \\ 0 & 0 & 1 & 1 \end{array}\right]$$

La reducida tiene la identidad a la izquierda: la solución se lee en la última columna, $(-2, -4, 1)$.

</details>
<details><summary>Errores frecuentes</summary>Dejar sin anular las entradas por encima de un pivote.</details>

### F09-N2-15 · [K] ¿Está en forma reducida?

**Objetivo**: recordar las condiciones de la forma escalonada reducida.
**Dificultad**: N2

**Enunciado.** Indica cuáles de estas matrices están en forma escalonada reducida y, si no lo están, por qué:

a) $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

b) $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$

c) $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

d) $\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \end{bmatrix}$

<details><summary>Pista 1</summary>Condiciones: pivotes $1$, escalonada, ceros por encima y por debajo de cada pivote, filas nulas abajo.</details>
<details><summary>Solución</summary>

a) No: una fila de ceros está encima de una fila no nula.

b) No: el pivote de la fila 2 está a la izquierda del de la fila 1.

c) Sí lo está.

d) Sí lo está.

</details>
<details><summary>Errores frecuentes</summary>Olvidar los ceros por encima de los pivotes.</details>

### F09-N2-16 · [K] ¿Está en forma reducida?

**Objetivo**: recordar las condiciones de la forma escalonada reducida.
**Dificultad**: N2

**Enunciado.** Indica cuáles de estas matrices están en forma escalonada reducida y, si no lo están, por qué:

a) $\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \end{bmatrix}$

b) $\begin{bmatrix} 1 & 0 & 3 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$

c) $\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \end{bmatrix}$

d) $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

<details><summary>Pista 1</summary>Condiciones: pivotes $1$, escalonada, ceros por encima y por debajo de cada pivote, filas nulas abajo.</details>
<details><summary>Solución</summary>

a) No: hay un elemento no nulo por encima del segundo pivote.

b) Sí lo está.

c) Sí lo está.

d) Sí lo está.

</details>
<details><summary>Errores frecuentes</summary>Olvidar los ceros por encima de los pivotes.</details>

### F09-N2-17 · [K] ¿Está en forma reducida?

**Objetivo**: recordar las condiciones de la forma escalonada reducida.
**Dificultad**: N2

**Enunciado.** Indica cuáles de estas matrices están en forma escalonada reducida y, si no lo están, por qué:

a) $\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \end{bmatrix}$

b) $\begin{bmatrix} 1 & 0 & 3 & 0 \\ 0 & 1 & 2 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$

c) $\begin{bmatrix} 2 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$

d) $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

<details><summary>Pista 1</summary>Condiciones: pivotes $1$, escalonada, ceros por encima y por debajo de cada pivote, filas nulas abajo.</details>
<details><summary>Solución</summary>

a) No: hay un elemento no nulo por encima del segundo pivote.

b) Sí lo está.

c) No: el primer pivote vale $2$, no $1$.

d) Sí lo está.

</details>
<details><summary>Errores frecuentes</summary>Olvidar los ceros por encima de los pivotes.</details>

### F09-N2-18 · [K] Básicas y libres

**Objetivo**: identificar variables básicas y libres a partir de la reducida.
**Dificultad**: N2

**Enunciado.** La forma reducida de un sistema es $\left[\begin{array}{ccccc|c} 1 & 0 & 0 & -1 & 5 & -5 \\ 0 & 1 & 0 & -2 & 8 & -3 \\ 0 & 0 & 1 & -\frac{4}{3} & 4 & -\frac{1}{3} \end{array}\right]$. ¿Cuáles son las variables básicas y cuáles las libres? ¿Cuántos parámetros tiene la solución?

<details><summary>Pista 1</summary>Una variable es básica si su columna tiene pivote.</details>
<details><summary>Solución</summary>

Básicas (columnas con pivote): $x_1$, $x_2$, $x_3$. Libres: $x_4$, $x_5$. Parámetros: 2.

</details>
<details><summary>Errores frecuentes</summary>Contar la columna de $\mathbf{b}$ entre las variables.</details>

### F09-N2-19 · [K] Básicas y libres

**Objetivo**: identificar variables básicas y libres a partir de la reducida.
**Dificultad**: N2

**Enunciado.** La forma reducida de un sistema es $\left[\begin{array}{ccccc|c} 1 & 0 & 0 & 1 & 0 & 3 \\ 0 & 1 & 0 & 1 & -2 & 9 \\ 0 & 0 & 1 & \frac{1}{2} & -1 & 0 \end{array}\right]$. ¿Cuáles son las variables básicas y cuáles las libres? ¿Cuántos parámetros tiene la solución?

<details><summary>Pista 1</summary>Una variable es básica si su columna tiene pivote.</details>
<details><summary>Solución</summary>

Básicas (columnas con pivote): $x_1$, $x_2$, $x_3$. Libres: $x_4$, $x_5$. Parámetros: 2.

</details>
<details><summary>Errores frecuentes</summary>Contar la columna de $\mathbf{b}$ entre las variables.</details>

### F09-N3-11 · [C] Leer la solución en la reducida

**Objetivo**: identificar variables básicas y libres y escribir la solución general.
**Dificultad**: N3

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} -3 & -8 & 3 & -4 & -12 \\ -2 & -3 & 2 & -5 & -1 \\ 0 & -2 & 0 & 2 & -6 \end{array}\right]$ y escribe la solución general.

<details><summary>Pista 1</summary>Las columnas sin pivote son las variables libres.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (-\frac{1}{3})R_1,\ R_2 \leftarrow R_2 + 2R_1,\ R_2 \leftarrow (\frac{3}{7})R_2,\ R_1 \leftarrow R_1 - \frac{8}{3}R_2,\ R_3 \leftarrow R_3 + 2R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & -1 & 4 & -4 \\ 0 & 1 & 0 & -1 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_3$, $x_4$. Solución general: $(-4, 3, 0, 0) + s\,(1, 0, 1, 0) + t\,(-4, 1, 0, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (-12, -1, -6) = (-12, -1, -6)$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que las variables libres también forman parte del vector solución.</details>

### F09-N3-12 · [C] Leer la solución en la reducida

**Objetivo**: identificar variables básicas y libres y escribir la solución general.
**Dificultad**: N3

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} 3 & -1 & 0 & 7 & -14 \\ 6 & 0 & -2 & 6 & -6 \\ 0 & -2 & 2 & 8 & -22 \end{array}\right]$ y escribe la solución general.

<details><summary>Pista 1</summary>Las columnas sin pivote son las variables libres.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (\frac{1}{3})R_1,\ R_2 \leftarrow R_2 - 6R_1,\ R_2 \leftarrow (\frac{1}{2})R_2,\ R_1 \leftarrow R_1 + \frac{1}{3}R_2,\ R_3 \leftarrow R_3 + 2R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & -\frac{1}{3} & 1 & -1 \\ 0 & 1 & -1 & -4 & 11 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_3$, $x_4$. Solución general: $(-1, 11, 0, 0) + s\,(\frac{1}{3}, 1, 1, 0) + t\,(-1, 4, 0, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (-14, -6, -22) = (-14, -6, -22)$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que las variables libres también forman parte del vector solución.</details>

### F09-N3-13 · [C] Leer la solución en la reducida

**Objetivo**: identificar variables básicas y libres y escribir la solución general.
**Dificultad**: N3

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} -2 & 0 & 2 & -4 & 8 \\ 7 & -4 & 1 & 8 & -16 \\ -2 & 2 & -2 & -1 & 2 \end{array}\right]$ y escribe la solución general.

<details><summary>Pista 1</summary>Las columnas sin pivote son las variables libres.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (-\frac{1}{2})R_1,\ R_2 \leftarrow R_2 - 7R_1,\ R_3 \leftarrow R_3 + 2R_1,\ R_2 \leftarrow (-\frac{1}{4})R_2,\ R_3 \leftarrow R_3 - 2R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & -1 & 2 & -4 \\ 0 & 1 & -2 & \frac{3}{2} & -3 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_3$, $x_4$. Solución general: $(-4, -3, 0, 0) + s\,(1, 2, 1, 0) + t\,(-2, -\frac{3}{2}, 0, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (8, -16, 2) = (8, -16, 2)$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que las variables libres también forman parte del vector solución.</details>

### F09-N3-14 · [C] Leer la solución en la reducida

**Objetivo**: identificar variables básicas y libres y escribir la solución general.
**Dificultad**: N3

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} 7 & 6 & 0 & 2 & -7 \\ 9 & 8 & 1 & 3 & -10 \\ 6 & 6 & 3 & 3 & -9 \end{array}\right]$ y escribe la solución general.

<details><summary>Pista 1</summary>Las columnas sin pivote son las variables libres.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (\frac{1}{7})R_1,\ R_2 \leftarrow R_2 - 9R_1,\ R_3 \leftarrow R_3 - 6R_1,\ R_2 \leftarrow (\frac{7}{2})R_2,\ R_1 \leftarrow R_1 - \frac{6}{7}R_2,\ R_3 \leftarrow R_3 - \frac{6}{7}R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & -3 & -1 & 2 \\ 0 & 1 & \frac{7}{2} & \frac{3}{2} & -\frac{7}{2} \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_3$, $x_4$. Solución general: $(2, -\frac{7}{2}, 0, 0) + s\,(3, -\frac{7}{2}, 1, 0) + t\,(1, -\frac{3}{2}, 0, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (-7, -10, -9) = (-7, -10, -9)$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que las variables libres también forman parte del vector solución.</details>

### F09-N3-15 · [C] Leer la solución en la reducida

**Objetivo**: identificar variables básicas y libres y escribir la solución general.
**Dificultad**: N3

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} -3 & 1 & -6 & -7 & -40 \\ 2 & -1 & 3 & 3 & 20 \\ -2 & 0 & -6 & -8 & -40 \end{array}\right]$ y escribe la solución general.

<details><summary>Pista 1</summary>Las columnas sin pivote son las variables libres.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (-\frac{1}{3})R_1,\ R_2 \leftarrow R_2 - 2R_1,\ R_3 \leftarrow R_3 + 2R_1,\ R_2 \leftarrow (-3)R_2,\ R_1 \leftarrow R_1 + \frac{1}{3}R_2,\ R_3 \leftarrow R_3 + \frac{2}{3}R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & 3 & 4 & 20 \\ 0 & 1 & 3 & 5 & 20 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_3$, $x_4$. Solución general: $(20, 20, 0, 0) + s\,(-3, -3, 1, 0) + t\,(-4, -5, 0, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (-40, 20, -40) = (-40, 20, -40)$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que las variables libres también forman parte del vector solución.</details>

### F09-N3-16 · [C] Leer la solución en la reducida

**Objetivo**: identificar variables básicas y libres y escribir la solución general.
**Dificultad**: N3

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} -5 & 0 & -5 & -3 & -26 \\ 5 & 0 & 5 & 3 & 26 \\ -2 & 4 & -2 & 2 & 4 \end{array}\right]$ y escribe la solución general.

<details><summary>Pista 1</summary>Las columnas sin pivote son las variables libres.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (-\frac{1}{5})R_1,\ R_2 \leftarrow R_2 - 5R_1,\ R_3 \leftarrow R_3 + 2R_1,\ R_2 \leftrightarrow R_3,\ R_2 \leftarrow (\frac{1}{4})R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & 1 & \frac{3}{5} & \frac{26}{5} \\ 0 & 1 & 0 & \frac{4}{5} & \frac{18}{5} \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_3$, $x_4$. Solución general: $(\frac{26}{5}, \frac{18}{5}, 0, 0) + s\,(-1, 0, 1, 0) + t\,(-\frac{3}{5}, -\frac{4}{5}, 0, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (-26, 26, 4) = (-26, 26, 4)$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que las variables libres también forman parte del vector solución.</details>

### F09-N3-17 · [C] Una reducida con pivote en la última columna

**Objetivo**: reconocer el pivote en la columna de $\mathbf{b}$.
**Dificultad**: N3

**Enunciado.** Reduce $\left[\begin{array}{ccc|c} 7 & -3 & -3 & 28 \\ -1 & -1 & -6 & 9 \\ 0 & 2 & 9 & -18 \end{array}\right]$ y clasifica el sistema.

<details><summary>Pista 1</summary>Mira si queda una fila $[0\ \dots\ 0 \mid c]$ con $c \ne 0$.</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (\frac{1}{7})R_1,\ R_2 \leftarrow R_2 + R_1,\ R_2 \leftarrow (-\frac{7}{10})R_2,\ R_1 \leftarrow R_1 + \frac{3}{7}R_2,\ R_3 \leftarrow R_3 - 2R_2$.

Resultado: $$\left[\begin{array}{ccc|c} 1 & 0 & \frac{3}{2} & \frac{1}{10} \\ 0 & 1 & \frac{9}{2} & -\frac{91}{10} \\ 0 & 0 & 0 & \frac{1}{5} \end{array}\right]$$
Hay un pivote en la columna de términos independientes (fila $[\,0\,0\,0 \mid 1\,]$): la ecuación $0 = 1$ es imposible. Incompatible.

</details>
<details><summary>Errores frecuentes</summary>Declarar compatible un sistema con una fila contradictoria.</details>

### F09-N3-18 · [C] Una reducida con pivote en la última columna

**Objetivo**: reconocer el pivote en la columna de $\mathbf{b}$.
**Dificultad**: N3

**Enunciado.** Reduce $\left[\begin{array}{ccc|c} 1 & 1 & 2 & 9 \\ -1 & -2 & -5 & -15 \\ -1 & 0 & 1 & -1 \end{array}\right]$ y clasifica el sistema.

<details><summary>Pista 1</summary>Mira si queda una fila $[0\ \dots\ 0 \mid c]$ con $c \ne 0$.</details>
<details><summary>Solución</summary>

Operaciones: $R_2 \leftarrow R_2 + R_1,\ R_3 \leftarrow R_3 + R_1,\ R_2 \leftarrow (-1)R_2,\ R_1 \leftarrow R_1 - R_2,\ R_3 \leftarrow R_3 - R_2$.

Resultado: $$\left[\begin{array}{ccc|c} 1 & 0 & -1 & 3 \\ 0 & 1 & 3 & 6 \\ 0 & 0 & 0 & 2 \end{array}\right]$$
Hay un pivote en la columna de términos independientes (fila $[\,0\,0\,0 \mid 1\,]$): la ecuación $0 = 1$ es imposible. Incompatible.

</details>
<details><summary>Errores frecuentes</summary>Declarar compatible un sistema con una fila contradictoria.</details>

### F09-N3-19 · [C] Gauss frente a Gauss-Jordan

**Objetivo**: comparar el número de operaciones con las fórmulas.
**Dificultad**: N3

**Enunciado.** Para un sistema cuadrado $n = 8$, calcula con $\frac{n^3 + 3n^2 - n}{3}$ (Gauss con sustitución hacia atrás) y $\frac{n^3 + n^2}{2}$ (Gauss-Jordan) el número de multiplicaciones y divisiones, y la razón entre ambos.

<details><summary>Pista 1</summary>Sustituye $n$ en cada fórmula.</details>
<details><summary>Solución</summary>

Gauss: $\frac{512 + 192 - 8}{3} = 232$. Gauss-Jordan: $\frac{512 + 64}{2} = 288$. La razón es $\frac{36}{29}\approx 1.24$: Gauss-Jordan cuesta más (y la razón tiende a $3/2$ cuando $n$ crece).

</details>
<details><summary>Errores frecuentes</summary>Contar solo las operaciones hacia adelante.</details>

### F09-N3-20 · [C] Gauss frente a Gauss-Jordan

**Objetivo**: comparar el número de operaciones con las fórmulas.
**Dificultad**: N3

**Enunciado.** Para un sistema cuadrado $n = 5$, calcula con $\frac{n^3 + 3n^2 - n}{3}$ (Gauss con sustitución hacia atrás) y $\frac{n^3 + n^2}{2}$ (Gauss-Jordan) el número de multiplicaciones y divisiones, y la razón entre ambos.

<details><summary>Pista 1</summary>Sustituye $n$ en cada fórmula.</details>
<details><summary>Solución</summary>

Gauss: $\frac{125 + 75 - 5}{3} = 65$. Gauss-Jordan: $\frac{125 + 25}{2} = 75$. La razón es $\frac{15}{13}\approx 1.15$: Gauss-Jordan cuesta más (y la razón tiende a $3/2$ cuando $n$ crece).

</details>
<details><summary>Errores frecuentes</summary>Contar solo las operaciones hacia adelante.</details>

### F09-N3-21 · [C] Gauss frente a Gauss-Jordan

**Objetivo**: comparar el número de operaciones con las fórmulas.
**Dificultad**: N3

**Enunciado.** Para un sistema cuadrado $n = 4$, calcula con $\frac{n^3 + 3n^2 - n}{3}$ (Gauss con sustitución hacia atrás) y $\frac{n^3 + n^2}{2}$ (Gauss-Jordan) el número de multiplicaciones y divisiones, y la razón entre ambos.

<details><summary>Pista 1</summary>Sustituye $n$ en cada fórmula.</details>
<details><summary>Solución</summary>

Gauss: $\frac{64 + 48 - 4}{3} = 36$. Gauss-Jordan: $\frac{64 + 16}{2} = 40$. La razón es $\frac{10}{9}\approx 1.11$: Gauss-Jordan cuesta más (y la razón tiende a $3/2$ cuando $n$ crece).

</details>
<details><summary>Errores frecuentes</summary>Contar solo las operaciones hacia adelante.</details>

### F09-N3-22 · [C] Reducir una matriz 4×4 con filas dependientes

**Objetivo**: reducir y contar variables libres.
**Dificultad**: N3

**Enunciado.** Lleva $\left[\begin{array}{cccc|c} 2 & -3 & -2 & -2 & -8 \\ -1 & 2 & 8 & 1 & 17 \\ -1 & 1 & -6 & 1 & -9 \\ 1 & -3 & -4 & -1 & -7 \end{array}\right]$ a su forma reducida y di cuántas variables libres hay.

<details><summary>Pista 1</summary>Algunas filas desaparecerán (se vuelven nulas).</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (\frac{1}{2})R_1,\ R_2 \leftarrow R_2 + R_1,\ R_3 \leftarrow R_3 + R_1,\ R_4 \leftarrow R_4 - R_1,\ R_2 \leftarrow 2R_2,\ R_1 \leftarrow R_1 + \frac{3}{2}R_2,\ R_3 \leftarrow R_3 + \frac{1}{2}R_2,\ R_4 \leftarrow R_4 + \frac{3}{2}R_2,\ R_3 \leftrightarrow R_4,\ R_3 \leftarrow (\frac{1}{18})R_3,\ R_1 \leftarrow R_1 - 20R_3,\ R_2 \leftarrow R_2 - 14R_3$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & 0 & -1 & -5 \\ 0 & 1 & 0 & 0 & -2 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: 1. Solución general: $(-5, -2, 2, 0) + s\,(1, 0, 0, 1)$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas nulas como variables libres.</details>

### F09-N3-23 · [C] Reducir una matriz 4×4 con filas dependientes

**Objetivo**: reducir y contar variables libres.
**Dificultad**: N3

**Enunciado.** Lleva $\left[\begin{array}{cccc|c} 2 & -1 & 7 & -2 & 16 \\ -1 & 4 & 0 & -6 & 20 \\ 3 & -4 & 8 & 2 & 4 \\ 2 & 1 & 9 & -6 & 32 \end{array}\right]$ a su forma reducida y di cuántas variables libres hay.

<details><summary>Pista 1</summary>Algunas filas desaparecerán (se vuelven nulas).</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (\frac{1}{2})R_1,\ R_2 \leftarrow R_2 + R_1,\ R_3 \leftarrow R_3 - 3R_1,\ R_4 \leftarrow R_4 - 2R_1,\ R_2 \leftarrow (\frac{2}{7})R_2,\ R_1 \leftarrow R_1 + \frac{1}{2}R_2,\ R_3 \leftarrow R_3 + \frac{5}{2}R_2,\ R_4 \leftarrow R_4 - 2R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & 4 & -2 & 12 \\ 0 & 1 & 1 & -2 & 8 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: 2. Solución general: $(12, 8, 0, 0) + s\,(-4, -1, 1, 0) + t\,(2, 2, 0, 1)$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas nulas como variables libres.</details>

### F09-N3-24 · [C] Reducir una matriz 4×4 con filas dependientes

**Objetivo**: reducir y contar variables libres.
**Dificultad**: N3

**Enunciado.** Lleva $\left[\begin{array}{cccc|c} 4 & 6 & -6 & -4 & -2 \\ 9 & 0 & -3 & 0 & -9 \\ 3 & 0 & -1 & 0 & -3 \\ 3 & 9 & -8 & -6 & 0 \end{array}\right]$ a su forma reducida y di cuántas variables libres hay.

<details><summary>Pista 1</summary>Algunas filas desaparecerán (se vuelven nulas).</details>
<details><summary>Solución</summary>

Operaciones: $R_1 \leftarrow (\frac{1}{4})R_1,\ R_2 \leftarrow R_2 - 9R_1,\ R_3 \leftarrow R_3 - 3R_1,\ R_4 \leftarrow R_4 - 3R_1,\ R_2 \leftarrow (-\frac{2}{27})R_2,\ R_1 \leftarrow R_1 - \frac{3}{2}R_2,\ R_3 \leftarrow R_3 + \frac{9}{2}R_2,\ R_4 \leftarrow R_4 - \frac{9}{2}R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 0 & -\frac{1}{3} & 0 & -1 \\ 0 & 1 & -\frac{7}{9} & -\frac{2}{3} & \frac{1}{3} \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: 2. Solución general: $(-1, \frac{1}{3}, 0, 0) + s\,(\frac{1}{3}, \frac{7}{9}, 1, 0) + t\,(0, \frac{2}{3}, 0, 1)$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas nulas como variables libres.</details>

