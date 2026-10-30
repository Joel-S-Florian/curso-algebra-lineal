# F08 — Eliminación de Gauss (parte 2)

Segunda parte del banco de las lecciones L24–L30: **28 ejercicios** de práctica que completan la parte 1 (`F08_gauss.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N3: 21, N4: 7 · [C] 25, [K] 3.

---

### F08-N3-11 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} -3x - y - z = 5 \\ x + 3y + z = -13 \\ -3x + y - 3z = -1 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -3 & -1 & -1 & 5 \\ 1 & 3 & 1 & -13 \\ -3 & 1 & -3 & -1 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + \frac{1}{3}R_1} \left[\begin{array}{ccc|c} -3 & -1 & -1 & 5 \\ 0 & \frac{8}{3} & \frac{2}{3} & -\frac{34}{3} \\ -3 & 1 & -3 & -1 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_1} \left[\begin{array}{ccc|c} -3 & -1 & -1 & 5 \\ 0 & \frac{8}{3} & \frac{2}{3} & -\frac{34}{3} \\ 0 & 2 & -2 & -6 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{3}{4}R_2} \left[\begin{array}{ccc|c} -3 & -1 & -1 & 5 \\ 0 & \frac{8}{3} & \frac{2}{3} & -\frac{34}{3} \\ 0 & 0 & -\frac{5}{2} & \frac{5}{2} \end{array}\right]$$

Sustitución hacia atrás: $(0, -4, -1)$. Comprobación en la primera ecuación: $(-3)\cdot 0 + (-1)\cdot (-4) + (-1)\cdot (-1) = 5$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-12 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} -x + 3y - 2z = -3 \\ -3x - 2y = 2 \\ 2x + 3y + 3z = -3 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -1 & 3 & -2 & -3 \\ -3 & -2 & 0 & 2 \\ 2 & 3 & 3 & -3 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - 3R_1} \left[\begin{array}{ccc|c} -1 & 3 & -2 & -3 \\ 0 & -11 & 6 & 11 \\ 2 & 3 & 3 & -3 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + 2R_1} \left[\begin{array}{ccc|c} -1 & 3 & -2 & -3 \\ 0 & -11 & 6 & 11 \\ 0 & 9 & -1 & -9 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{9}{11}R_2} \left[\begin{array}{ccc|c} -1 & 3 & -2 & -3 \\ 0 & -11 & 6 & 11 \\ 0 & 0 & \frac{43}{11} & 0 \end{array}\right]$$

Sustitución hacia atrás: $(0, -1, 0)$. Comprobación en la primera ecuación: $(-1)\cdot 0 + 3\cdot (-1) + (-2)\cdot 0 = -3$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-13 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} -x - 2y = 6 \\ -x - 2y + 3z = -3 \\ -2x - 3y - 3z = 18 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -1 & -2 & 0 & 6 \\ -1 & -2 & 3 & -3 \\ -2 & -3 & -3 & 18 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - R_1} \left[\begin{array}{ccc|c} -1 & -2 & 0 & 6 \\ 0 & 0 & 3 & -9 \\ -2 & -3 & -3 & 18 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 2R_1} \left[\begin{array}{ccc|c} -1 & -2 & 0 & 6 \\ 0 & 0 & 3 & -9 \\ 0 & 1 & -3 & 6 \end{array}\right]$$
$$\xrightarrow{R_2 \leftrightarrow R_3} \left[\begin{array}{ccc|c} -1 & -2 & 0 & 6 \\ 0 & 1 & -3 & 6 \\ 0 & 0 & 3 & -9 \end{array}\right]$$

Sustitución hacia atrás: $(0, -3, -3)$. Comprobación en la primera ecuación: $(-1)\cdot 0 + (-2)\cdot (-3) + 0\cdot (-3) = 6$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-14 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} x - y + 2z = 8 \\ 3x + 2y + 2z = 10 \\ -2x - y - 2z = -8 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & -1 & 2 & 8 \\ 3 & 2 & 2 & 10 \\ -2 & -1 & -2 & -8 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - 3R_1} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 8 \\ 0 & 5 & -4 & -14 \\ -2 & -1 & -2 & -8 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + 2R_1} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 8 \\ 0 & 5 & -4 & -14 \\ 0 & -3 & 2 & 8 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{3}{5}R_2} \left[\begin{array}{ccc|c} 1 & -1 & 2 & 8 \\ 0 & 5 & -4 & -14 \\ 0 & 0 & -\frac{2}{5} & -\frac{2}{5} \end{array}\right]$$

Sustitución hacia atrás: $(4, -2, 1)$. Comprobación en la primera ecuación: $1\cdot 4 + (-1)\cdot (-2) + 2\cdot 1 = 8$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-15 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} x - 3y - z = 0 \\ -3x - y - 3z = 24 \\ -2x + 2y - z = 12 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & -3 & -1 & 0 \\ -3 & -1 & -3 & 24 \\ -2 & 2 & -1 & 12 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + 3R_1} \left[\begin{array}{ccc|c} 1 & -3 & -1 & 0 \\ 0 & -10 & -6 & 24 \\ -2 & 2 & -1 & 12 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + 2R_1} \left[\begin{array}{ccc|c} 1 & -3 & -1 & 0 \\ 0 & -10 & -6 & 24 \\ 0 & -4 & -3 & 12 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{2}{5}R_2} \left[\begin{array}{ccc|c} 1 & -3 & -1 & 0 \\ 0 & -10 & -6 & 24 \\ 0 & 0 & -\frac{3}{5} & \frac{12}{5} \end{array}\right]$$

Sustitución hacia atrás: $(-4, 0, -4)$. Comprobación en la primera ecuación: $1\cdot (-4) + (-3)\cdot 0 + (-1)\cdot (-4) = 0$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-16 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} x + y = -8 \\ -3x + 2y - z = 7 \\ x - y + 2z = -6 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & 1 & 0 & -8 \\ -3 & 2 & -1 & 7 \\ 1 & -1 & 2 & -6 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + 3R_1} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -8 \\ 0 & 5 & -1 & -17 \\ 1 & -1 & 2 & -6 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_1} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -8 \\ 0 & 5 & -1 & -17 \\ 0 & -2 & 2 & 2 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{2}{5}R_2} \left[\begin{array}{ccc|c} 1 & 1 & 0 & -8 \\ 0 & 5 & -1 & -17 \\ 0 & 0 & \frac{8}{5} & -\frac{24}{5} \end{array}\right]$$

Sustitución hacia atrás: $(-4, -4, -3)$. Comprobación en la primera ecuación: $1\cdot (-4) + 1\cdot (-4) + 0\cdot (-3) = -8$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-17 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} 2x - 2y - z = -1 \\ -3x - 2y + 3z = -8 \\ -y - 3z = 8 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 2 & -2 & -1 & -1 \\ -3 & -2 & 3 & -8 \\ 0 & -1 & -3 & 8 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + \frac{3}{2}R_1} \left[\begin{array}{ccc|c} 2 & -2 & -1 & -1 \\ 0 & -5 & \frac{3}{2} & -\frac{19}{2} \\ 0 & -1 & -3 & 8 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{1}{5}R_2} \left[\begin{array}{ccc|c} 2 & -2 & -1 & -1 \\ 0 & -5 & \frac{3}{2} & -\frac{19}{2} \\ 0 & 0 & -\frac{33}{10} & \frac{99}{10} \end{array}\right]$$

Sustitución hacia atrás: $(-1, 1, -3)$. Comprobación en la primera ecuación: $2\cdot (-1) + (-2)\cdot 1 + (-1)\cdot (-3) = -1$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-18 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} y - 3z = 0 \\ 2x + y + 3z = 12 \\ -2x - y = -9 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 0 & 1 & -3 & 0 \\ 2 & 1 & 3 & 12 \\ -2 & -1 & 0 & -9 \end{array}\right] $$
$$\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{ccc|c} 2 & 1 & 3 & 12 \\ 0 & 1 & -3 & 0 \\ -2 & -1 & 0 & -9 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + R_1} \left[\begin{array}{ccc|c} 2 & 1 & 3 & 12 \\ 0 & 1 & -3 & 0 \\ 0 & 0 & 3 & 3 \end{array}\right]$$

Sustitución hacia atrás: $(3, 3, 1)$. Comprobación en la primera ecuación: $0\cdot 3 + 1\cdot 3 + (-3)\cdot 1 = 0$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-19 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} x + y + z = -2 \\ 3x - 3y = 18 \\ 3y = -6 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & 1 & 1 & -2 \\ 3 & -3 & 0 & 18 \\ 0 & 3 & 0 & -6 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - 3R_1} \left[\begin{array}{ccc|c} 1 & 1 & 1 & -2 \\ 0 & -6 & -3 & 24 \\ 0 & 3 & 0 & -6 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{1}{2}R_2} \left[\begin{array}{ccc|c} 1 & 1 & 1 & -2 \\ 0 & -6 & -3 & 24 \\ 0 & 0 & -\frac{3}{2} & 6 \end{array}\right]$$

Sustitución hacia atrás: $(4, -2, -4)$. Comprobación en la primera ecuación: $1\cdot 4 + 1\cdot (-2) + 1\cdot (-4) = -2$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-20 · [C] Gauss en un sistema 3×3

**Objetivo**: escalonar $[A \mid \mathbf{b}]$ y resolver hacia atrás.
**Dificultad**: N3

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} -x + 2y + 3z = 3 \\ 3x + 3y + 2z = -14 \\ -3x - 3y - z = 16 \end{cases}$ y comprueba el resultado.

<details><summary>Pista 1</summary>Haz ceros bajo el primer pivote y luego bajo el segundo.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -1 & 2 & 3 & 3 \\ 3 & 3 & 2 & -14 \\ -3 & -3 & -1 & 16 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + 3R_1} \left[\begin{array}{ccc|c} -1 & 2 & 3 & 3 \\ 0 & 9 & 11 & -5 \\ -3 & -3 & -1 & 16 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 3R_1} \left[\begin{array}{ccc|c} -1 & 2 & 3 & 3 \\ 0 & 9 & 11 & -5 \\ 0 & -9 & -10 & 7 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + R_2} \left[\begin{array}{ccc|c} -1 & 2 & 3 & 3 \\ 0 & 9 & 11 & -5 \\ 0 & 0 & 1 & 2 \end{array}\right]$$

Sustitución hacia atrás: $(-3, -3, 2)$. Comprobación en la primera ecuación: $(-1)\cdot (-3) + 2\cdot (-3) + 3\cdot 2 = 3$.

</details>
<details><summary>Errores frecuentes</summary>Aplicar la operación a la matriz pero no a la columna de $\mathbf{b}$.</details>

### F08-N3-21 · [C] Pivote nulo: hay que intercambiar

**Objetivo**: intercambiar filas cuando el primer pivote es cero.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -3y + z = -8 \\ -x + 3y - 2z = 7 \\ -2x + y + z = 4 \end{cases}$ por eliminación gaussiana. ¿Por qué hay que intercambiar filas?

<details><summary>Pista 1</summary>Si el pivote es cero, busca debajo una fila con un elemento no nulo en esa columna.</details>
<details><summary>Solución</summary>

El coeficiente de $x$ en la primera ecuación es $0$, así que no puede ser pivote: se intercambia con una fila que tenga $x$.

$$ \left[\begin{array}{ccc|c} 0 & -3 & 1 & -8 \\ -1 & 3 & -2 & 7 \\ -2 & 1 & 1 & 4 \end{array}\right] $$
$$\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{ccc|c} -1 & 3 & -2 & 7 \\ 0 & -3 & 1 & -8 \\ -2 & 1 & 1 & 4 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 2R_1} \left[\begin{array}{ccc|c} -1 & 3 & -2 & 7 \\ 0 & -3 & 1 & -8 \\ 0 & -5 & 5 & -10 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{5}{3}R_2} \left[\begin{array}{ccc|c} -1 & 3 & -2 & 7 \\ 0 & -3 & 1 & -8 \\ 0 & 0 & \frac{10}{3} & \frac{10}{3} \end{array}\right]$$

Solución: $(0, 3, 1)$.

</details>
<details><summary>Errores frecuentes</summary>Dividir entre el pivote cero.</details>

### F08-N3-22 · [C] Pivote nulo: hay que intercambiar

**Objetivo**: intercambiar filas cuando el primer pivote es cero.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} y - 3z = 0 \\ -3x + y + 3z = 12 \\ 2x + 2y - z = -8 \end{cases}$ por eliminación gaussiana. ¿Por qué hay que intercambiar filas?

<details><summary>Pista 1</summary>Si el pivote es cero, busca debajo una fila con un elemento no nulo en esa columna.</details>
<details><summary>Solución</summary>

El coeficiente de $x$ en la primera ecuación es $0$, así que no puede ser pivote: se intercambia con una fila que tenga $x$.

$$ \left[\begin{array}{ccc|c} 0 & 1 & -3 & 0 \\ -3 & 1 & 3 & 12 \\ 2 & 2 & -1 & -8 \end{array}\right] $$
$$\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{ccc|c} -3 & 1 & 3 & 12 \\ 0 & 1 & -3 & 0 \\ 2 & 2 & -1 & -8 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{2}{3}R_1} \left[\begin{array}{ccc|c} -3 & 1 & 3 & 12 \\ 0 & 1 & -3 & 0 \\ 0 & \frac{8}{3} & 1 & 0 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{8}{3}R_2} \left[\begin{array}{ccc|c} -3 & 1 & 3 & 12 \\ 0 & 1 & -3 & 0 \\ 0 & 0 & 9 & 0 \end{array}\right]$$

Solución: $(-4, 0, 0)$.

</details>
<details><summary>Errores frecuentes</summary>Dividir entre el pivote cero.</details>

### F08-N3-23 · [C] Pivote nulo: hay que intercambiar

**Objetivo**: intercambiar filas cuando el primer pivote es cero.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} 2y + 3z = 5 \\ -3x - y = 2 \\ x + y - 3z = -11 \end{cases}$ por eliminación gaussiana. ¿Por qué hay que intercambiar filas?

<details><summary>Pista 1</summary>Si el pivote es cero, busca debajo una fila con un elemento no nulo en esa columna.</details>
<details><summary>Solución</summary>

El coeficiente de $x$ en la primera ecuación es $0$, así que no puede ser pivote: se intercambia con una fila que tenga $x$.

$$ \left[\begin{array}{ccc|c} 0 & 2 & 3 & 5 \\ -3 & -1 & 0 & 2 \\ 1 & 1 & -3 & -11 \end{array}\right] $$
$$\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{ccc|c} -3 & -1 & 0 & 2 \\ 0 & 2 & 3 & 5 \\ 1 & 1 & -3 & -11 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{1}{3}R_1} \left[\begin{array}{ccc|c} -3 & -1 & 0 & 2 \\ 0 & 2 & 3 & 5 \\ 0 & \frac{2}{3} & -3 & -\frac{31}{3} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{1}{3}R_2} \left[\begin{array}{ccc|c} -3 & -1 & 0 & 2 \\ 0 & 2 & 3 & 5 \\ 0 & 0 & -4 & -12 \end{array}\right]$$

Solución: $(0, -2, 3)$.

</details>
<details><summary>Errores frecuentes</summary>Dividir entre el pivote cero.</details>

### F08-N3-24 · [C] Pivote nulo: hay que intercambiar

**Objetivo**: intercambiar filas cuando el primer pivote es cero.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -2y + 2z = 6 \\ -2x - 2y + z = 13 \\ x - 3y + 2z = 7 \end{cases}$ por eliminación gaussiana. ¿Por qué hay que intercambiar filas?

<details><summary>Pista 1</summary>Si el pivote es cero, busca debajo una fila con un elemento no nulo en esa columna.</details>
<details><summary>Solución</summary>

El coeficiente de $x$ en la primera ecuación es $0$, así que no puede ser pivote: se intercambia con una fila que tenga $x$.

$$ \left[\begin{array}{ccc|c} 0 & -2 & 2 & 6 \\ -2 & -2 & 1 & 13 \\ 1 & -3 & 2 & 7 \end{array}\right] $$
$$\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{ccc|c} -2 & -2 & 1 & 13 \\ 0 & -2 & 2 & 6 \\ 1 & -3 & 2 & 7 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{1}{2}R_1} \left[\begin{array}{ccc|c} -2 & -2 & 1 & 13 \\ 0 & -2 & 2 & 6 \\ 0 & -4 & \frac{5}{2} & \frac{27}{2} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 2R_2} \left[\begin{array}{ccc|c} -2 & -2 & 1 & 13 \\ 0 & -2 & 2 & 6 \\ 0 & 0 & -\frac{3}{2} & \frac{3}{2} \end{array}\right]$$

Solución: $(-3, -4, -1)$.

</details>
<details><summary>Errores frecuentes</summary>Dividir entre el pivote cero.</details>

### F08-N3-25 · [C] Sistema sin solución

**Objetivo**: reconocer una fila contradictoria.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} x + 3z = 8 \\ 2x + 2y = -14 \\ 3x + 2y + 3z = -4 \end{cases}$.

<details><summary>Pista 1</summary>Mira si la tercera ecuación es combinación de las otras dos en los coeficientes.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & 0 & 3 & 8 \\ 2 & 2 & 0 & -14 \\ 3 & 2 & 3 & -4 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{ccc|c} 1 & 0 & 3 & 8 \\ 0 & 2 & -6 & -30 \\ 3 & 2 & 3 & -4 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 3R_1} \left[\begin{array}{ccc|c} 1 & 0 & 3 & 8 \\ 0 & 2 & -6 & -30 \\ 0 & 2 & -6 & -28 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} 1 & 0 & 3 & 8 \\ 0 & 2 & -6 & -30 \\ 0 & 0 & 0 & 2 \end{array}\right]$$

La última fila queda $[\,0\ 0\ 0 \mid c\,]$ con $c \ne 0$: es la ecuación $0 = c$, imposible. El sistema es incompatible (no tiene solución).

</details>
<details><summary>Errores frecuentes</summary>Seguir operando después de encontrar $0 = c$.</details>

### F08-N3-26 · [C] Sistema sin solución

**Objetivo**: reconocer una fila contradictoria.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} x - 3y + 2z = 10 \\ -y - z = -3 \\ x - 4y + z = 11 \end{cases}$.

<details><summary>Pista 1</summary>Mira si la tercera ecuación es combinación de las otras dos en los coeficientes.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & -3 & 2 & 10 \\ 0 & -1 & -1 & -3 \\ 1 & -4 & 1 & 11 \end{array}\right] $$
$$\xrightarrow{R_3 \leftarrow R_3 - R_1} \left[\begin{array}{ccc|c} 1 & -3 & 2 & 10 \\ 0 & -1 & -1 & -3 \\ 0 & -1 & -1 & 1 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} 1 & -3 & 2 & 10 \\ 0 & -1 & -1 & -3 \\ 0 & 0 & 0 & 4 \end{array}\right]$$

La última fila queda $[\,0\ 0\ 0 \mid c\,]$ con $c \ne 0$: es la ecuación $0 = c$, imposible. El sistema es incompatible (no tiene solución).

</details>
<details><summary>Errores frecuentes</summary>Seguir operando después de encontrar $0 = c$.</details>

### F08-N3-27 · [C] Sistema sin solución

**Objetivo**: reconocer una fila contradictoria.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -2x + 3z = -4 \\ 3x - y + z = 8 \\ x - y + 4z = 6 \end{cases}$.

<details><summary>Pista 1</summary>Mira si la tercera ecuación es combinación de las otras dos en los coeficientes.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -2 & 0 & 3 & -4 \\ 3 & -1 & 1 & 8 \\ 1 & -1 & 4 & 6 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + \frac{3}{2}R_1} \left[\begin{array}{ccc|c} -2 & 0 & 3 & -4 \\ 0 & -1 & \frac{11}{2} & 2 \\ 1 & -1 & 4 & 6 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{1}{2}R_1} \left[\begin{array}{ccc|c} -2 & 0 & 3 & -4 \\ 0 & -1 & \frac{11}{2} & 2 \\ 0 & -1 & \frac{11}{2} & 4 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} -2 & 0 & 3 & -4 \\ 0 & -1 & \frac{11}{2} & 2 \\ 0 & 0 & 0 & 2 \end{array}\right]$$

La última fila queda $[\,0\ 0\ 0 \mid c\,]$ con $c \ne 0$: es la ecuación $0 = c$, imposible. El sistema es incompatible (no tiene solución).

</details>
<details><summary>Errores frecuentes</summary>Seguir operando después de encontrar $0 = c$.</details>

### F08-N3-28 · [C] Infinitas soluciones

**Objetivo**: reconocer una fila nula y escribir la solución con un parámetro.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -2z = -8 \\ x - z = -1 \\ x - 3z = -9 \end{cases}$.

<details><summary>Pista 1</summary>Una ecuación es suma de las otras dos.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 0 & 0 & -2 & -8 \\ 1 & 0 & -1 & -1 \\ 1 & 0 & -3 & -9 \end{array}\right] $$
$$\xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{ccc|c} 1 & 0 & -1 & -1 \\ 0 & 0 & -2 & -8 \\ 1 & 0 & -3 & -9 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_1} \left[\begin{array}{ccc|c} 1 & 0 & -1 & -1 \\ 0 & 0 & -2 & -8 \\ 0 & 0 & -2 & -8 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} 1 & 0 & -1 & -1 \\ 0 & 0 & -2 & -8 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

Queda una fila de ceros y una variable libre. Solución general: $(3, 0, 4) + s\,(0, 1, 0)$ con $s \in \mathbb{R}$ (compatible indeterminado).

</details>
<details><summary>Errores frecuentes</summary>Decir que no hay solución porque aparece una fila de ceros.</details>

### F08-N3-29 · [C] Infinitas soluciones

**Objetivo**: reconocer una fila nula y escribir la solución con un parámetro.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -x + 3y - z = 11 \\ 3x + 2y - z = -4 \\ 2x + 5y - 2z = 7 \end{cases}$.

<details><summary>Pista 1</summary>Una ecuación es suma de las otras dos.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -1 & 3 & -1 & 11 \\ 3 & 2 & -1 & -4 \\ 2 & 5 & -2 & 7 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + 3R_1} \left[\begin{array}{ccc|c} -1 & 3 & -1 & 11 \\ 0 & 11 & -4 & 29 \\ 2 & 5 & -2 & 7 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + 2R_1} \left[\begin{array}{ccc|c} -1 & 3 & -1 & 11 \\ 0 & 11 & -4 & 29 \\ 0 & 11 & -4 & 29 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} -1 & 3 & -1 & 11 \\ 0 & 11 & -4 & 29 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

Queda una fila de ceros y una variable libre. Solución general: $(-\frac{34}{11}, \frac{29}{11}, 0) + s\,(\frac{1}{11}, \frac{4}{11}, 1)$ con $s \in \mathbb{R}$ (compatible indeterminado).

</details>
<details><summary>Errores frecuentes</summary>Decir que no hay solución porque aparece una fila de ceros.</details>

### F08-N3-30 · [C] Infinitas soluciones

**Objetivo**: reconocer una fila nula y escribir la solución con un parámetro.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} -2x - z = -4 \\ 3y - z = 3 \\ -2x + 3y - 2z = -1 \end{cases}$.

<details><summary>Pista 1</summary>Una ecuación es suma de las otras dos.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} -2 & 0 & -1 & -4 \\ 0 & 3 & -1 & 3 \\ -2 & 3 & -2 & -1 \end{array}\right] $$
$$\xrightarrow{R_3 \leftarrow R_3 - R_1} \left[\begin{array}{ccc|c} -2 & 0 & -1 & -4 \\ 0 & 3 & -1 & 3 \\ 0 & 3 & -1 & 3 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} -2 & 0 & -1 & -4 \\ 0 & 3 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

Queda una fila de ceros y una variable libre. Solución general: $(2, 1, 0) + s\,(-\frac{1}{2}, \frac{1}{3}, 1)$ con $s \in \mathbb{R}$ (compatible indeterminado).

</details>
<details><summary>Errores frecuentes</summary>Decir que no hay solución porque aparece una fila de ceros.</details>

### F08-N3-31 · [C] Infinitas soluciones

**Objetivo**: reconocer una fila nula y escribir la solución con un parámetro.
**Dificultad**: N3

**Enunciado.** Resuelve $\begin{cases} x + y - 2z = -7 \\ -x + 2z = 4 \\ y = -3 \end{cases}$.

<details><summary>Pista 1</summary>Una ecuación es suma de las otras dos.</details>
<details><summary>Solución</summary>

$$ \left[\begin{array}{ccc|c} 1 & 1 & -2 & -7 \\ -1 & 0 & 2 & 4 \\ 0 & 1 & 0 & -3 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 + R_1} \left[\begin{array}{ccc|c} 1 & 1 & -2 & -7 \\ 0 & 1 & 0 & -3 \\ 0 & 1 & 0 & -3 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - R_2} \left[\begin{array}{ccc|c} 1 & 1 & -2 & -7 \\ 0 & 1 & 0 & -3 \\ 0 & 0 & 0 & 0 \end{array}\right]$$

Queda una fila de ceros y una variable libre. Solución general: $(-4, -3, 0) + s\,(2, 0, 1)$ con $s \in \mathbb{R}$ (compatible indeterminado).

</details>
<details><summary>Errores frecuentes</summary>Decir que no hay solución porque aparece una fila de ceros.</details>

### F08-N4-11 · [K] Encuentra el error en la eliminación

**Objetivo**: detectar una operación aplicada solo a los coeficientes.
**Dificultad**: N4

**Enunciado.** Para $\begin{cases} -x + 2y + z = -5 \\ 2x + 3y + z = -18 \\ -2x - y + 3z = 10 \end{cases}$ un estudiante aplica $R_2 \leftarrow R_2 + 2R_1$ y obtiene la segunda fila $\left[\begin{array}{ccc|c} 0 & 7 & 3 & -18 \end{array}\right]$. ¿Es correcto? Corrígelo.

<details><summary>Pista 1</summary>Una operación elemental actúa sobre todas las entradas de la fila de $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

No: la operación hay que aplicarla a la fila entera, columna de $\mathbf{b}$ incluida. El estudiante dejó $b_2 = -18$ sin cambiar. Lo correcto es $b_2 + (2)\,b_1 = -28$, es decir, la fila $\left[\begin{array}{ccc|c} 0 & 7 & 3 & -28 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Operar solo sobre la parte de coeficientes.</details>

### F08-N4-12 · [K] Encuentra el error en la eliminación

**Objetivo**: detectar una operación aplicada solo a los coeficientes.
**Dificultad**: N4

**Enunciado.** Para $\begin{cases} -x - y - 3z = -2 \\ x - 2y - 2z = 2 \\ -3x - y - 3z = -6 \end{cases}$ un estudiante aplica $R_2 \leftarrow R_2 + R_1$ y obtiene la segunda fila $\left[\begin{array}{ccc|c} 0 & -3 & -5 & 2 \end{array}\right]$. ¿Es correcto? Corrígelo.

<details><summary>Pista 1</summary>Una operación elemental actúa sobre todas las entradas de la fila de $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

No: la operación hay que aplicarla a la fila entera, columna de $\mathbf{b}$ incluida. El estudiante dejó $b_2 = 2$ sin cambiar. Lo correcto es $b_2 + (1)\,b_1 = 0$, es decir, la fila $\left[\begin{array}{ccc|c} 0 & -3 & -5 & 0 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Operar solo sobre la parte de coeficientes.</details>

### F08-N4-13 · [K] Encuentra el error en la eliminación

**Objetivo**: detectar una operación aplicada solo a los coeficientes.
**Dificultad**: N4

**Enunciado.** Para $\begin{cases} 2x - y - 2z = -19 \\ -3x + y + 2z = 23 \\ 3x + 2y + 3z = 6 \end{cases}$ un estudiante aplica $R_2 \leftarrow R_2 + \frac{3}{2}R_1$ y obtiene la segunda fila $\left[\begin{array}{ccc|c} 0 & -\frac{1}{2} & -1 & 23 \end{array}\right]$. ¿Es correcto? Corrígelo.

<details><summary>Pista 1</summary>Una operación elemental actúa sobre todas las entradas de la fila de $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

No: la operación hay que aplicarla a la fila entera, columna de $\mathbf{b}$ incluida. El estudiante dejó $b_2 = 23$ sin cambiar. Lo correcto es $b_2 + (\frac{3}{2})\,b_1 = -\frac{11}{2}$, es decir, la fila $\left[\begin{array}{ccc|c} 0 & -\frac{1}{2} & -1 & -\frac{11}{2} \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Operar solo sobre la parte de coeficientes.</details>

### F08-N4-14 · [C] Sistema 3×3 con parámetro

**Objetivo**: discutir un sistema con un parámetro: determinante y valores críticos.
**Dificultad**: N4

**Enunciado.** Discute el sistema según los valores de $a$: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 2 \\ x + 4y + a^2 z = 1 \end{cases}$

<details><summary>Pista 1</summary>Calcula el determinante o escalona dejando $a$ como letra.</details>
<details><summary>Pista 2</summary>Los valores críticos son los que anulan un pivote.</details>
<details><summary>Solución</summary>

El determinante de la matriz de coeficientes es $\det A = \left(a - 2\right) \left(a - 1\right)$. Se anula para $a \in \{1, 2\}$. Para los demás valores de $a$ hay solución única.

Si $a = 1$: incompatible (sin solución).

Si $a = 2$: incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>No estudiar por separado cada valor crítico.</details>

### F08-N4-15 · [C] Sistema 3×3 con parámetro

**Objetivo**: discutir un sistema con un parámetro: determinante y valores críticos.
**Dificultad**: N4

**Enunciado.** Discute el sistema según los valores de $a$: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 0 \\ x + 4y + a^2 z = 0 \end{cases}$

<details><summary>Pista 1</summary>Calcula el determinante o escalona dejando $a$ como letra.</details>
<details><summary>Pista 2</summary>Los valores críticos son los que anulan un pivote.</details>
<details><summary>Solución</summary>

El determinante de la matriz de coeficientes es $\det A = \left(a - 2\right) \left(a - 1\right)$. Se anula para $a \in \{1, 2\}$. Para los demás valores de $a$ hay solución única.

Si $a = 1$: incompatible (sin solución).

Si $a = 2$: incompatible (sin solución).

</details>
<details><summary>Errores frecuentes</summary>No estudiar por separado cada valor crítico.</details>

### F08-N4-16 · [C] Sistema 3×3 con parámetro

**Objetivo**: discutir un sistema con un parámetro: determinante y valores críticos.
**Dificultad**: N4

**Enunciado.** Discute el sistema según los valores de $a$: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 2 \\ x + 4y + a^2 z = 4 \end{cases}$

<details><summary>Pista 1</summary>Calcula el determinante o escalona dejando $a$ como letra.</details>
<details><summary>Pista 2</summary>Los valores críticos son los que anulan un pivote.</details>
<details><summary>Solución</summary>

El determinante de la matriz de coeficientes es $\det A = \left(a - 2\right) \left(a - 1\right)$. Se anula para $a \in \{1, 2\}$. Para los demás valores de $a$ hay solución única.

Si $a = 1$: infinitas soluciones (1 parámetro libre).

Si $a = 2$: infinitas soluciones (1 parámetro libre).

</details>
<details><summary>Errores frecuentes</summary>No estudiar por separado cada valor crítico.</details>

### F08-N4-17 · [C] Sistema 3×3 con parámetro

**Objetivo**: discutir un sistema con un parámetro: determinante y valores críticos.
**Dificultad**: N4

**Enunciado.** Discute el sistema según los valores de $a$: $\begin{cases} x + y + z = 1 \\ x + 2y + az = 1 \\ x + 4y + a^2 z = 1 \end{cases}$

<details><summary>Pista 1</summary>Calcula el determinante o escalona dejando $a$ como letra.</details>
<details><summary>Pista 2</summary>Los valores críticos son los que anulan un pivote.</details>
<details><summary>Solución</summary>

El determinante de la matriz de coeficientes es $\det A = \left(a - 2\right) \left(a - 1\right)$. Se anula para $a \in \{1, 2\}$. Para los demás valores de $a$ hay solución única.

Si $a = 1$: infinitas soluciones (1 parámetro libre).

Si $a = 2$: infinitas soluciones (1 parámetro libre).

</details>
<details><summary>Errores frecuentes</summary>No estudiar por separado cada valor crítico.</details>

