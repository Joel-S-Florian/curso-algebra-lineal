# F11 — Rango y Rouché-Frobenius (parte 2)

Segunda parte del banco de las lecciones L39–L42: **34 ejercicios** de práctica que completan la parte 1 (`F11_rango_rouche_frobenius.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N2: 15, N3: 13, N4: 6 · [C] 26, [K] 8.

---

### F11-N2-11 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} 3 & -1 & 0 \\ 1 & -3 & -5 \\ 0 & -4 & -2 \\ -3 & -1 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 - \frac{1}{3}R_1, R_4 \leftarrow R_4 + R_1, R_3 \leftarrow R_3 - \frac{3}{2}R_2, R_4 \leftarrow R_4 - \frac{3}{4}R_2, R_4 \leftarrow R_4 - \frac{1}{2}R_3$.

La forma reducida es $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1, 2, 3: $\operatorname{rg}(A) = 3$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-12 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} 5 & 6 & 8 \\ 0 & -6 & -1 \\ -1 & 2 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_3 \leftarrow R_3 + \frac{1}{5}R_1, R_3 \leftarrow R_3 + \frac{8}{15}R_2$.

La forma reducida es $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, con pivotes en las columnas 1, 2, 3: $\operatorname{rg}(A) = 3$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-13 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} 1 & 2 & 1 & 2 \\ 2 & 4 & 2 & 4 \\ 2 & 4 & 2 & 4 \\ 2 & 4 & 2 & 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 - 2R_1, R_3 \leftarrow R_3 - 2R_1, R_4 \leftarrow R_4 - 2R_1$.

La forma reducida es $\begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1: $\operatorname{rg}(A) = 1$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-14 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} 9 & 9 & 9 & 9 \\ 1 & 1 & 1 & 2 \\ 3 & 3 & 3 & 3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 - \frac{1}{9}R_1, R_3 \leftarrow R_3 - \frac{1}{3}R_1$.

La forma reducida es $\begin{bmatrix} 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1, 4: $\operatorname{rg}(A) = 2$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-15 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} 1 & 2 & 1 \\ 1 & 2 & 1 \\ 2 & 4 & 2 \\ 2 & 4 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 - R_1, R_3 \leftarrow R_3 - 2R_1, R_4 \leftarrow R_4 - 2R_1$.

La forma reducida es $\begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1: $\operatorname{rg}(A) = 1$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-16 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} -4 & 4 & -4 \\ -6 & 6 & -6 \\ -2 & 2 & -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 - \frac{3}{2}R_1, R_3 \leftarrow R_3 - \frac{1}{2}R_1$.

La forma reducida es $\begin{bmatrix} 1 & -1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1: $\operatorname{rg}(A) = 1$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-17 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} -2 & -6 & 3 & 2 \\ 2 & 4 & -6 & -2 \\ 3 & 4 & -7 & 1 \\ 0 & 4 & 4 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 + R_1, R_3 \leftarrow R_3 + \frac{3}{2}R_1, R_3 \leftarrow R_3 - \frac{5}{2}R_2, R_4 \leftarrow R_4 + 2R_2, R_4 \leftarrow R_4 + \frac{2}{5}R_3$.

La forma reducida es $\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$, con pivotes en las columnas 1, 2, 3, 4: $\operatorname{rg}(A) = 4$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-18 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} -3 & 9 & 9 & -6 \\ -1 & 3 & 3 & -2 \\ -1 & 3 & 3 & -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 - \frac{1}{3}R_1, R_3 \leftarrow R_3 - \frac{1}{3}R_1$.

La forma reducida es $\begin{bmatrix} 1 & -3 & -3 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1: $\operatorname{rg}(A) = 1$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-19 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} -6 & 8 & 1 & 9 \\ 7 & 5 & 1 & 4 \\ 0 & -2 & 2 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 + \frac{7}{6}R_1, R_3 \leftarrow R_3 + \frac{6}{43}R_2$.

La forma reducida es $\begin{bmatrix} 1 & 0 & 0 & -\frac{1}{6} \\ 0 & 1 & 0 & \frac{17}{18} \\ 0 & 0 & 1 & \frac{4}{9} \end{bmatrix}$, con pivotes en las columnas 1, 2, 3: $\operatorname{rg}(A) = 3$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-20 · [C] Calcular el rango

**Objetivo**: escalonar y contar pivotes.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} -5 & -7 & 1 & 3 \\ 5 & 3 & -9 & -7 \\ 6 & 6 & -6 & -6 \\ 4 & 8 & 4 & 0 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cuenta los pivotes de una forma escalonada.</details>
<details><summary>Solución</summary>

Operaciones por filas: $R_2 \leftarrow R_2 + R_1, R_3 \leftarrow R_3 + \frac{6}{5}R_1, R_4 \leftarrow R_4 + \frac{4}{5}R_1, R_3 \leftarrow R_3 - \frac{3}{5}R_2, R_4 \leftarrow R_4 + \frac{3}{5}R_2$.

La forma reducida es $\begin{bmatrix} 1 & 0 & -3 & -2 \\ 0 & 1 & 2 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, con pivotes en las columnas 1, 2: $\operatorname{rg}(A) = 2$.

</details>
<details><summary>Errores frecuentes</summary>Contar las filas no nulas de la matriz original en lugar de la escalonada.</details>

### F11-N2-21 · [K] Contar parámetros libres

**Objetivo**: usar $n - \operatorname{rg}(A)$ en un sistema compatible.
**Dificultad**: N2

**Enunciado.** Un sistema compatible tiene 4 ecuaciones, 6 incógnitas y $\operatorname{rg}(A) = 3$. ¿Cuántos parámetros libres tiene la solución y de qué tipo es?

<details><summary>Pista 1</summary>Parámetros libres = incógnitas − rango.</details>
<details><summary>Solución</summary>

$n - \operatorname{rg}(A) = 6 - 3 = 3$ parámetros libres: compatible indeterminado.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango del número de ecuaciones.</details>

### F11-N2-22 · [K] Contar parámetros libres

**Objetivo**: usar $n - \operatorname{rg}(A)$ en un sistema compatible.
**Dificultad**: N2

**Enunciado.** Un sistema compatible tiene 5 ecuaciones, 3 incógnitas y $\operatorname{rg}(A) = 1$. ¿Cuántos parámetros libres tiene la solución y de qué tipo es?

<details><summary>Pista 1</summary>Parámetros libres = incógnitas − rango.</details>
<details><summary>Solución</summary>

$n - \operatorname{rg}(A) = 3 - 1 = 2$ parámetros libres: compatible indeterminado.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango del número de ecuaciones.</details>

### F11-N2-23 · [K] Contar parámetros libres

**Objetivo**: usar $n - \operatorname{rg}(A)$ en un sistema compatible.
**Dificultad**: N2

**Enunciado.** Un sistema compatible tiene 3 ecuaciones, 5 incógnitas y $\operatorname{rg}(A) = 2$. ¿Cuántos parámetros libres tiene la solución y de qué tipo es?

<details><summary>Pista 1</summary>Parámetros libres = incógnitas − rango.</details>
<details><summary>Solución</summary>

$n - \operatorname{rg}(A) = 5 - 2 = 3$ parámetros libres: compatible indeterminado.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango del número de ecuaciones.</details>

### F11-N2-24 · [K] Contar parámetros libres

**Objetivo**: usar $n - \operatorname{rg}(A)$ en un sistema compatible.
**Dificultad**: N2

**Enunciado.** Un sistema compatible tiene 5 ecuaciones, 3 incógnitas y $\operatorname{rg}(A) = 2$. ¿Cuántos parámetros libres tiene la solución y de qué tipo es?

<details><summary>Pista 1</summary>Parámetros libres = incógnitas − rango.</details>
<details><summary>Solución</summary>

$n - \operatorname{rg}(A) = 3 - 2 = 1$ parámetros libres: compatible indeterminado.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango del número de ecuaciones.</details>

### F11-N2-25 · [K] Contar parámetros libres

**Objetivo**: usar $n - \operatorname{rg}(A)$ en un sistema compatible.
**Dificultad**: N2

**Enunciado.** Un sistema compatible tiene 2 ecuaciones, 4 incógnitas y $\operatorname{rg}(A) = 1$. ¿Cuántos parámetros libres tiene la solución y de qué tipo es?

<details><summary>Pista 1</summary>Parámetros libres = incógnitas − rango.</details>
<details><summary>Solución</summary>

$n - \operatorname{rg}(A) = 4 - 1 = 3$ parámetros libres: compatible indeterminado.

</details>
<details><summary>Errores frecuentes</summary>Restar el rango del número de ecuaciones.</details>

### F11-N3-11 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} -3x - 6y - 3z = 6 \\ -x - y = 2 \\ 2x + 6y + 4z = -4 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 2$, $n = 3$ incógnitas. Los rangos coinciden pero son menores que $n$: compatible indeterminado (infinitas soluciones). Número de parámetros libres: $n - r = 3 - 2 = 1$.

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-12 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} 8x + 2y + 2z = 37 \\ 2x + y + 5z = 24 \\ 2x - 4z = -6 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, $n = 3$ incógnitas. Los rangos son distintos: incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-13 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} -6x - 3z = -6 \\ 4y - 4z = 4 \\ 4x - 2y + 4z = 2 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 2$, $n = 3$ incógnitas. Los rangos coinciden pero son menores que $n$: compatible indeterminado (infinitas soluciones). Número de parámetros libres: $n - r = 3 - 2 = 1$.

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-14 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} -2x + y + 2z = 1 \\ 5x - 4y - 4z = -5 \\ 4x - 2y - 4z = -2 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 2$, $n = 3$ incógnitas. Los rangos coinciden pero son menores que $n$: compatible indeterminado (infinitas soluciones). Número de parámetros libres: $n - r = 3 - 2 = 1$.

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-15 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} -2x + 6y + z + 3w = -7 \\ 2y + z + 3w = -7 \\ -x - 2y - 2z - 6w = 14 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 2$, $n = 4$ incógnitas. Los rangos coinciden pero son menores que $n$: compatible indeterminado (infinitas soluciones). Número de parámetros libres: $n - r = 4 - 2 = 2$.

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-16 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} x + 2y + 2z + 2w = 5 \\ x + 2y + 2z + 2w = 5 \\ x + 2y + 2z + 2w = 5 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 1$, $\operatorname{rg}[A \mid \mathbf{b}] = 1$, $n = 4$ incógnitas. Los rangos coinciden pero son menores que $n$: compatible indeterminado (infinitas soluciones). Número de parámetros libres: $n - r = 4 - 1 = 3$.

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-17 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} -x + y + z = 2 \\ 3x + 3y + 3z = -11 \\ -3x - 3y - 3z = 12 \\ -x - 2y - 2z = 5 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, $n = 3$ incógnitas. Los rangos son distintos: incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-18 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} 2x - 4y + 4z - 2w = 8 \\ -x - 4y - 4z + w = 18 \\ 2x - 7y + 3z - 2w = 19 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 2$, $n = 4$ incógnitas. Los rangos coinciden pero son menores que $n$: compatible indeterminado (infinitas soluciones). Número de parámetros libres: $n - r = 4 - 2 = 2$.

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-19 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} 2x + y - 4z = -1 \\ -4x + 8y + 6z = 32 \\ 2x - 4y - 4z = -16 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 3$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, $n = 3$ incógnitas. Los rangos coinciden y valen $n$: compatible determinado (solución única).

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-20 · [C] Clasificar con Rouché-Frobenius

**Objetivo**: clasificar sin resolver comparando rangos.
**Dificultad**: N3

**Enunciado.** Sin resolverlo, clasifica $\begin{cases} -2x - 3y + 4z = -1 \\ -2x - y + 4w = 6 \\ x + y - z - w = -1 \end{cases}$.

<details><summary>Pista 1</summary>Calcula los dos rangos escalonando $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, $n = 4$ incógnitas. Los rangos son distintos: incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Comparar el rango con el número de ecuaciones en vez de con el de incógnitas.</details>

### F11-N3-21 · [K] Clasificar con datos de rango

**Objetivo**: clasificar a partir de los rangos, sin calcular.
**Dificultad**: N3

**Enunciado.** Clasifica y justifica, para cada caso:

a) Un sistema con más ecuaciones que incógnitas, ¿puede ser compatible determinado?
b) $\operatorname{rg}(A) = 3$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$ y hay 4 incógnitas.
c) Un sistema homogéneo con 3 ecuaciones y 5 incógnitas.

<details><summary>Pista 1</summary>Compara $\operatorname{rg}(A)$, $\operatorname{rg}[A \mid \mathbf{b}]$ y $n$.</details>
<details><summary>Solución</summary>

a) Sí, si las ecuaciones sobrantes son combinación de las demás (rango $= n$).

b) Compatible indeterminado con $4 - 3 = 1$ parámetro libre.

c) Siempre compatible; como $\operatorname{rg} \le 3 < 5$, es indeterminado, con al menos $2$ parámetros libres.

</details>
<details><summary>Errores frecuentes</summary>No contar la columna de $\mathbf{b}$.</details>

### F11-N3-22 · [K] Clasificar con datos de rango

**Objetivo**: clasificar a partir de los rangos, sin calcular.
**Dificultad**: N3

**Enunciado.** Clasifica y justifica, para cada caso:

a) Un sistema homogéneo con 3 ecuaciones y 5 incógnitas.
b) $\operatorname{rg}(A) = 2$ y $\operatorname{rg}[A \mid \mathbf{b}] = 3$.
c) Un sistema con más ecuaciones que incógnitas, ¿puede ser compatible determinado?

<details><summary>Pista 1</summary>Compara $\operatorname{rg}(A)$, $\operatorname{rg}[A \mid \mathbf{b}]$ y $n$.</details>
<details><summary>Solución</summary>

a) Siempre compatible; como $\operatorname{rg} \le 3 < 5$, es indeterminado, con al menos $2$ parámetros libres.

b) Incompatible: el rango de la aumentada es mayor.

c) Sí, si las ecuaciones sobrantes son combinación de las demás (rango $= n$).

</details>
<details><summary>Errores frecuentes</summary>No contar la columna de $\mathbf{b}$.</details>

### F11-N3-23 · [K] Clasificar con datos de rango

**Objetivo**: clasificar a partir de los rangos, sin calcular.
**Dificultad**: N3

**Enunciado.** Clasifica y justifica, para cada caso:

a) Un sistema homogéneo con 3 ecuaciones y 5 incógnitas.
b) Un sistema con más ecuaciones que incógnitas, ¿puede ser compatible determinado?
c) ¿Puede ser $\operatorname{rg}[A \mid \mathbf{b}] < \operatorname{rg}(A)$?

<details><summary>Pista 1</summary>Compara $\operatorname{rg}(A)$, $\operatorname{rg}[A \mid \mathbf{b}]$ y $n$.</details>
<details><summary>Solución</summary>

a) Siempre compatible; como $\operatorname{rg} \le 3 < 5$, es indeterminado, con al menos $2$ parámetros libres.

b) Sí, si las ecuaciones sobrantes son combinación de las demás (rango $= n$).

c) No: la aumentada tiene una columna más, y $\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1$.

</details>
<details><summary>Errores frecuentes</summary>No contar la columna de $\mathbf{b}$.</details>

### F11-N4-11 · [C] Discusión con Rouché-Frobenius

**Objetivo**: discutir según un parámetro usando rangos.
**Dificultad**: N4

**Enunciado.** Discute según $a$, con Rouché-Frobenius: $\begin{cases} x + y + z = 1 \\ x + ay + z = 1 \\ x + y + az = 1 \end{cases}$

<details><summary>Pista 1</summary>El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.</details>
<details><summary>Pista 2</summary>Para cada valor crítico, calcula $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\det A = \left(a - 1\right)^{2}$, que se anula en $a \in \{1\}$. Si $a$ es distinto de esos valores, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3 = n$: solución única.

$a = 1$: $\operatorname{rg}(A) = 1$, $\operatorname{rg}[A \mid \mathbf{b}] = 1$, compatible indeterminado (infinitas soluciones).

</details>
<details><summary>Errores frecuentes</summary>Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\mathbf{b}$.</details>

### F11-N4-12 · [C] Discusión con Rouché-Frobenius

**Objetivo**: discutir según un parámetro usando rangos.
**Dificultad**: N4

**Enunciado.** Discute según $a$, con Rouché-Frobenius: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 1 \\ x + 4y + a^2 z = 0 \end{cases}$

<details><summary>Pista 1</summary>El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.</details>
<details><summary>Pista 2</summary>Para cada valor crítico, calcula $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\det A = \left(a - 2\right) \left(a - 1\right)$, que se anula en $a \in \{1, 2\}$. Si $a$ es distinto de esos valores, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3 = n$: solución única.

$a = 1$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

$a = 2$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\mathbf{b}$.</details>

### F11-N4-13 · [C] Discusión con Rouché-Frobenius

**Objetivo**: discutir según un parámetro usando rangos.
**Dificultad**: N4

**Enunciado.** Discute según $a$, con Rouché-Frobenius: $\begin{cases} x + y + az = 1 \\ x + ay + z = 1 \\ ax + y + z = 0 \end{cases}$

<details><summary>Pista 1</summary>El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.</details>
<details><summary>Pista 2</summary>Para cada valor crítico, calcula $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\det A = - \left(a - 1\right)^{2} \left(a + 2\right)$, que se anula en $a \in \{-2, 1\}$. Si $a$ es distinto de esos valores, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3 = n$: solución única.

$a = -2$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

$a = 1$: $\operatorname{rg}(A) = 1$, $\operatorname{rg}[A \mid \mathbf{b}] = 2$, incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\mathbf{b}$.</details>

### F11-N4-14 · [C] Discusión con Rouché-Frobenius

**Objetivo**: discutir según un parámetro usando rangos.
**Dificultad**: N4

**Enunciado.** Discute según $a$, con Rouché-Frobenius: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 2 \\ x + 4y + a^2 z = 0 \end{cases}$

<details><summary>Pista 1</summary>El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.</details>
<details><summary>Pista 2</summary>Para cada valor crítico, calcula $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\det A = \left(a - 2\right) \left(a - 1\right)$, que se anula en $a \in \{1, 2\}$. Si $a$ es distinto de esos valores, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3 = n$: solución única.

$a = 1$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

$a = 2$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\mathbf{b}$.</details>

### F11-N4-15 · [C] Discusión con Rouché-Frobenius

**Objetivo**: discutir según un parámetro usando rangos.
**Dificultad**: N4

**Enunciado.** Discute según $a$, con Rouché-Frobenius: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 0 \\ x + 4y + a^2 z = 1 \end{cases}$

<details><summary>Pista 1</summary>El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.</details>
<details><summary>Pista 2</summary>Para cada valor crítico, calcula $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\det A = \left(a - 2\right) \left(a - 1\right)$, que se anula en $a \in \{1, 2\}$. Si $a$ es distinto de esos valores, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3 = n$: solución única.

$a = 1$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

$a = 2$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\mathbf{b}$.</details>

### F11-N4-16 · [C] Discusión con Rouché-Frobenius

**Objetivo**: discutir según un parámetro usando rangos.
**Dificultad**: N4

**Enunciado.** Discute según $a$, con Rouché-Frobenius: $\begin{cases} x + y + az = 1 \\ x + ay + z = 1 \\ ax + y + z = 1 \end{cases}$

<details><summary>Pista 1</summary>El rango de $A$ baja de $3$ solo en los valores que anulan el determinante.</details>
<details><summary>Pista 2</summary>Para cada valor crítico, calcula $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

$\det A = - \left(a - 1\right)^{2} \left(a + 2\right)$, que se anula en $a \in \{-2, 1\}$. Si $a$ es distinto de esos valores, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3 = n$: solución única.

$a = -2$: $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, incompatible (sin solución).

$a = 1$: $\operatorname{rg}(A) = 1$, $\operatorname{rg}[A \mid \mathbf{b}] = 1$, compatible indeterminado (infinitas soluciones).

</details>
<details><summary>Errores frecuentes</summary>Usar el determinante cuando el sistema no es cuadrado o ignorar la columna de $\mathbf{b}$.</details>

