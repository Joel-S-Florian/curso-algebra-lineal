# F05 — Matrices y vectores (parte 2)

Segunda parte del banco de las lecciones L16–L18: **40 ejercicios** de práctica que completan la parte 1 (`F05_matrices_y_vectores.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N1: 17, N2: 23 · [C] 31, [K] 9.

---

### F05-N1-11 · [C] Suma y resta de matrices

**Objetivo**: operar matrices del mismo tamaño entrada a entrada.
**Dificultad**: N1

**Enunciado.** Calcula $A + B$ con $A = \begin{bmatrix} 1 & 1 & 0 \\ 3 & 3 & 5 \end{bmatrix}$ y $B = \begin{bmatrix} -1 & -1 & 3 \\ 0 & 2 & -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las matrices tienen el mismo tamaño $2\times 3$: se pueden sumar o restar.</details>
<details><summary>Solución</summary>

Se opera entrada a entrada: $A + B = \begin{bmatrix} 0 & 0 & 3 \\ 3 & 5 & 2 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.</details>

### F05-N1-12 · [C] Suma y resta de matrices

**Objetivo**: operar matrices del mismo tamaño entrada a entrada.
**Dificultad**: N1

**Enunciado.** Calcula $A + B$ con $A = \begin{bmatrix} 2 & -4 & 0 \\ -1 & 5 & 1 \end{bmatrix}$ y $B = \begin{bmatrix} -4 & 2 & 2 \\ -1 & 2 & 0 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las matrices tienen el mismo tamaño $2\times 3$: se pueden sumar o restar.</details>
<details><summary>Solución</summary>

Se opera entrada a entrada: $A + B = \begin{bmatrix} -2 & -2 & 2 \\ -2 & 7 & 1 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.</details>

### F05-N1-13 · [C] Suma y resta de matrices

**Objetivo**: operar matrices del mismo tamaño entrada a entrada.
**Dificultad**: N1

**Enunciado.** Calcula $A + B$ con $A = \begin{bmatrix} -1 & 1 \\ -2 & 1 \\ 1 & 2 \end{bmatrix}$ y $B = \begin{bmatrix} -1 & -4 \\ -3 & -4 \\ -2 & 5 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las matrices tienen el mismo tamaño $3\times 2$: se pueden sumar o restar.</details>
<details><summary>Solución</summary>

Se opera entrada a entrada: $A + B = \begin{bmatrix} -2 & -3 \\ -5 & -3 \\ -1 & 7 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.</details>

### F05-N1-14 · [C] Suma y resta de matrices

**Objetivo**: operar matrices del mismo tamaño entrada a entrada.
**Dificultad**: N1

**Enunciado.** Calcula $A + B$ con $A = \begin{bmatrix} -4 & 4 & -1 \\ 5 & -4 & 5 \\ -4 & 0 & 0 \end{bmatrix}$ y $B = \begin{bmatrix} 5 & 5 & 0 \\ -1 & 0 & -1 \\ -1 & 3 & 3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las matrices tienen el mismo tamaño $3\times 3$: se pueden sumar o restar.</details>
<details><summary>Solución</summary>

Se opera entrada a entrada: $A + B = \begin{bmatrix} 1 & 9 & -1 \\ 4 & -4 & 4 \\ -5 & 3 & 3 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.</details>

### F05-N1-15 · [C] Suma y resta de matrices

**Objetivo**: operar matrices del mismo tamaño entrada a entrada.
**Dificultad**: N1

**Enunciado.** Calcula $A - B$ con $A = \begin{bmatrix} 5 & -4 \\ -1 & 5 \\ -2 & -1 \end{bmatrix}$ y $B = \begin{bmatrix} 2 & -1 \\ -3 & -1 \\ -3 & -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las matrices tienen el mismo tamaño $3\times 2$: se pueden sumar o restar.</details>
<details><summary>Solución</summary>

Se opera entrada a entrada: $A - B = \begin{bmatrix} 3 & -3 \\ 2 & 6 \\ 1 & 2 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.</details>

### F05-N1-16 · [C] Suma y resta de matrices

**Objetivo**: operar matrices del mismo tamaño entrada a entrada.
**Dificultad**: N1

**Enunciado.** Calcula $A + B$ con $A = \begin{bmatrix} 1 & -3 & 1 \\ -3 & 3 & -2 \\ -4 & -1 & -4 \end{bmatrix}$ y $B = \begin{bmatrix} -1 & -4 & 4 \\ -1 & 5 & 4 \\ -3 & 3 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Las matrices tienen el mismo tamaño $3\times 3$: se pueden sumar o restar.</details>
<details><summary>Solución</summary>

Se opera entrada a entrada: $A + B = \begin{bmatrix} 0 & -7 & 5 \\ -4 & 8 & 2 \\ -7 & 2 & -2 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera fila o cambiar el signo de una sola entrada de $B$.</details>

### F05-N1-17 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} -1 \\ 5 \\ 2 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} -4 \\ 2 \\ -2 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} -1 \\ 5 \\ -4 \end{bmatrix}$, calcula $-3\mathbf{u} + 3\mathbf{v} + 1\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} -10 \\ -4 \\ -16 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-18 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} -1 \\ -3 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} -4 \\ -2 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} 3 \\ -1 \end{bmatrix}$, calcula $3\mathbf{u} + (-3)\mathbf{v} + 3\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} 18 \\ -6 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-19 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} -4 \\ -3 \\ -2 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} -2 \\ -2 \\ 0 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} -3 \\ -2 \\ -3 \end{bmatrix}$, calcula $2\mathbf{u} + 3\mathbf{v} + 2\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} -20 \\ -16 \\ -10 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-20 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} -3 \\ 0 \\ -2 \\ 4 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} -3 \\ 0 \\ -2 \\ -1 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} 5 \\ 2 \\ -3 \\ 3 \end{bmatrix}$, calcula $-3\mathbf{u} + (-2)\mathbf{v} + (-1)\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} 10 \\ -2 \\ 13 \\ -13 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-21 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} -2 \\ 0 \\ 4 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} 0 \\ 5 \\ 0 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} 0 \\ -3 \\ -1 \end{bmatrix}$, calcula $-1\mathbf{u} + (-1)\mathbf{v} + 2\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} 2 \\ -11 \\ -6 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-22 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} 3 \\ 0 \\ 3 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} 3 \\ 3 \\ 0 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} 2 \\ 1 \\ -2 \end{bmatrix}$, calcula $2\mathbf{u} + (-2)\mathbf{v} + (-1)\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} -2 \\ -7 \\ 8 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-23 · [C] Combinación de vectores

**Objetivo**: operar vectores componente a componente.
**Dificultad**: N1

**Enunciado.** Con $\mathbf{u} = \begin{bmatrix} 3 \\ 0 \\ 2 \\ 0 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} 1 \\ -1 \\ 3 \\ -3 \end{bmatrix}$ y $\mathbf{w} = \begin{bmatrix} 3 \\ 1 \\ 0 \\ -3 \end{bmatrix}$, calcula $1\mathbf{u} + 2\mathbf{v} + 3\mathbf{w}$.

<details><summary>Pista 1</summary>Multiplica cada vector por su número y suma las componentes que ocupan la misma posición.</details>
<details><summary>Solución</summary>

Componente a componente: $\begin{bmatrix} 14 \\ 1 \\ 8 \\ -15 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Sumar componentes de posiciones distintas.</details>

### F05-N1-24 · [C] Matriz a partir de una regla

**Objetivo**: usar la notación $a_{ij}$ (fila $i$, columna $j$).
**Dificultad**: N1

**Enunciado.** Escribe la matriz $A$ de tamaño $2\times 3$ con $a_{ij} = i \cdot j$.

<details><summary>Pista 1</summary>El primer índice es la fila y el segundo la columna.</details>
<details><summary>Solución</summary>

Se calcula cada entrada con $i$ = fila y $j$ = columna: $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}$. Por ejemplo, $a_{23} = 6$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar fila y columna.</details>

### F05-N1-25 · [C] Matriz a partir de una regla

**Objetivo**: usar la notación $a_{ij}$ (fila $i$, columna $j$).
**Dificultad**: N1

**Enunciado.** Escribe la matriz $A$ de tamaño $3\times 3$ con $a_{ij} = \max(i, j)$.

<details><summary>Pista 1</summary>El primer índice es la fila y el segundo la columna.</details>
<details><summary>Solución</summary>

Se calcula cada entrada con $i$ = fila y $j$ = columna: $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 2 & 3 \\ 3 & 3 & 3 \end{bmatrix}$. Por ejemplo, $a_{33} = 3$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar fila y columna.</details>

### F05-N1-26 · [C] Matriz a partir de una regla

**Objetivo**: usar la notación $a_{ij}$ (fila $i$, columna $j$).
**Dificultad**: N1

**Enunciado.** Escribe la matriz $A$ de tamaño $3\times 3$ con $a_{ij} = i - j$.

<details><summary>Pista 1</summary>El primer índice es la fila y el segundo la columna.</details>
<details><summary>Solución</summary>

Se calcula cada entrada con $i$ = fila y $j$ = columna: $A = \begin{bmatrix} 0 & -1 & -2 \\ 1 & 0 & -1 \\ 2 & 1 & 0 \end{bmatrix}$. Por ejemplo, $a_{33} = 0$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar fila y columna.</details>

### F05-N1-27 · [C] Matriz a partir de una regla

**Objetivo**: usar la notación $a_{ij}$ (fila $i$, columna $j$).
**Dificultad**: N1

**Enunciado.** Escribe la matriz $A$ de tamaño $3\times 2$ con $a_{ij} = i + j$.

<details><summary>Pista 1</summary>El primer índice es la fila y el segundo la columna.</details>
<details><summary>Solución</summary>

Se calcula cada entrada con $i$ = fila y $j$ = columna: $A = \begin{bmatrix} 2 & 3 \\ 3 & 4 \\ 4 & 5 \end{bmatrix}$. Por ejemplo, $a_{32} = 5$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar fila y columna.</details>

### F05-N2-11 · [C] Combinación de matrices

**Objetivo**: multiplicar por escalares y sumar.
**Dificultad**: N2

**Enunciado.** Calcula $-A + 4B$ con $A = \begin{bmatrix} 1 & 3 & 2 \\ -2 & -3 & 3 \\ -3 & -2 & -1 \end{bmatrix}$ y $B = \begin{bmatrix} 2 & 3 & 3 \\ 2 & -1 & 2 \\ -2 & -2 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Multiplica cada matriz por su escalar antes de sumar.</details>
<details><summary>Solución</summary>

$-1A = \begin{bmatrix} -1 & -3 & -2 \\ 2 & 3 & -3 \\ 3 & 2 & 1 \end{bmatrix}$ y $4B = \begin{bmatrix} 8 & 12 & 12 \\ 8 & -4 & 8 \\ -8 & -8 & -4 \end{bmatrix}$. Sumando: $\begin{bmatrix} 7 & 9 & 10 \\ 10 & -1 & 5 \\ -5 & -6 & -3 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar solo una fila por el escalar.</details>

### F05-N2-12 · [C] Combinación de matrices

**Objetivo**: multiplicar por escalares y sumar.
**Dificultad**: N2

**Enunciado.** Calcula $-2A + B$ con $A = \begin{bmatrix} 2 & 0 & 0 \\ 3 & 1 & -3 \end{bmatrix}$ y $B = \begin{bmatrix} 4 & 2 & -2 \\ 2 & 4 & 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Multiplica cada matriz por su escalar antes de sumar.</details>
<details><summary>Solución</summary>

$-2A = \begin{bmatrix} -4 & 0 & 0 \\ -6 & -2 & 6 \end{bmatrix}$ y $1B = \begin{bmatrix} 4 & 2 & -2 \\ 2 & 4 & 4 \end{bmatrix}$. Sumando: $\begin{bmatrix} 0 & 2 & -2 \\ -4 & 2 & 10 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar solo una fila por el escalar.</details>

### F05-N2-13 · [C] Combinación de matrices

**Objetivo**: multiplicar por escalares y sumar.
**Dificultad**: N2

**Enunciado.** Calcula $-3A + 3B$ con $A = \begin{bmatrix} -1 & 4 \\ 1 & 3 \end{bmatrix}$ y $B = \begin{bmatrix} 3 & 1 \\ 3 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Multiplica cada matriz por su escalar antes de sumar.</details>
<details><summary>Solución</summary>

$-3A = \begin{bmatrix} 3 & -12 \\ -3 & -9 \end{bmatrix}$ y $3B = \begin{bmatrix} 9 & 3 \\ 9 & 6 \end{bmatrix}$. Sumando: $\begin{bmatrix} 12 & -9 \\ 6 & -3 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar solo una fila por el escalar.</details>

### F05-N2-14 · [C] Combinación de matrices

**Objetivo**: multiplicar por escalares y sumar.
**Dificultad**: N2

**Enunciado.** Calcula $-A - 3B$ con $A = \begin{bmatrix} 4 & 1 & 1 \\ 3 & 4 & 3 \\ -1 & -2 & 2 \end{bmatrix}$ y $B = \begin{bmatrix} -2 & 0 & 2 \\ -1 & -2 & 3 \\ -3 & 1 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Multiplica cada matriz por su escalar antes de sumar.</details>
<details><summary>Solución</summary>

$-1A = \begin{bmatrix} -4 & -1 & -1 \\ -3 & -4 & -3 \\ 1 & 2 & -2 \end{bmatrix}$ y $-3B = \begin{bmatrix} 6 & 0 & -6 \\ 3 & 6 & -9 \\ 9 & -3 & -6 \end{bmatrix}$. Sumando: $\begin{bmatrix} 2 & -1 & -7 \\ 0 & 2 & -12 \\ 10 & -1 & -8 \end{bmatrix}$.

</details>
<details><summary>Errores frecuentes</summary>Multiplicar solo una fila por el escalar.</details>

### F05-N2-15 · [C] Traspuesta

**Objetivo**: calcular la traspuesta y comprobar $(A + B)^T = A^T + B^T$.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 1 & -3 & 5 & 0 \\ 3 & 5 & 4 & 5 \end{bmatrix}$ y $B = \begin{bmatrix} 4 & -3 & 2 & 5 \\ -1 & 0 & 2 & 0 \end{bmatrix}$: a) halla $A^T$ y su tamaño; b) comprueba que $(A + B)^T = A^T + B^T$.

<details><summary>Pista 1</summary>Las filas de $A$ pasan a ser las columnas de $A^T$.</details>
<details><summary>Solución</summary>

a) $A^T = \begin{bmatrix} 1 & 3 \\ -3 & 5 \\ 5 & 4 \\ 0 & 5 \end{bmatrix}$, de tamaño $4\times 2$.

b) $A + B = \begin{bmatrix} 5 & -6 & 7 & 5 \\ 2 & 5 & 6 & 5 \end{bmatrix}$, luego $(A + B)^T = \begin{bmatrix} 5 & 2 \\ -6 & 5 \\ 7 & 6 \\ 5 & 5 \end{bmatrix}$. Además $A^T + B^T = \begin{bmatrix} 5 & 2 \\ -6 & 5 \\ 7 & 6 \\ 5 & 5 \end{bmatrix}$: coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir las filas como columnas en otro orden.</details>

### F05-N2-16 · [C] Traspuesta

**Objetivo**: calcular la traspuesta y comprobar $(A + B)^T = A^T + B^T$.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 4 & 4 \\ 1 & 5 \\ 3 & 3 \end{bmatrix}$ y $B = \begin{bmatrix} 4 & -3 \\ -2 & 5 \\ 5 & -2 \end{bmatrix}$: a) halla $A^T$ y su tamaño; b) comprueba que $(A + B)^T = A^T + B^T$.

<details><summary>Pista 1</summary>Las filas de $A$ pasan a ser las columnas de $A^T$.</details>
<details><summary>Solución</summary>

a) $A^T = \begin{bmatrix} 4 & 1 & 3 \\ 4 & 5 & 3 \end{bmatrix}$, de tamaño $2\times 3$.

b) $A + B = \begin{bmatrix} 8 & 1 \\ -1 & 10 \\ 8 & 1 \end{bmatrix}$, luego $(A + B)^T = \begin{bmatrix} 8 & -1 & 8 \\ 1 & 10 & 1 \end{bmatrix}$. Además $A^T + B^T = \begin{bmatrix} 8 & -1 & 8 \\ 1 & 10 & 1 \end{bmatrix}$: coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir las filas como columnas en otro orden.</details>

### F05-N2-17 · [C] Traspuesta

**Objetivo**: calcular la traspuesta y comprobar $(A + B)^T = A^T + B^T$.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 5 & 4 & -1 \\ 5 & -3 & 5 \\ 3 & 4 & 0 \end{bmatrix}$ y $B = \begin{bmatrix} 0 & -1 & -4 \\ -2 & -3 & 3 \\ 4 & 2 & 4 \end{bmatrix}$: a) halla $A^T$ y su tamaño; b) comprueba que $(A + B)^T = A^T + B^T$.

<details><summary>Pista 1</summary>Las filas de $A$ pasan a ser las columnas de $A^T$.</details>
<details><summary>Solución</summary>

a) $A^T = \begin{bmatrix} 5 & 5 & 3 \\ 4 & -3 & 4 \\ -1 & 5 & 0 \end{bmatrix}$, de tamaño $3\times 3$.

b) $A + B = \begin{bmatrix} 5 & 3 & -5 \\ 3 & -6 & 8 \\ 7 & 6 & 4 \end{bmatrix}$, luego $(A + B)^T = \begin{bmatrix} 5 & 3 & 7 \\ 3 & -6 & 6 \\ -5 & 8 & 4 \end{bmatrix}$. Además $A^T + B^T = \begin{bmatrix} 5 & 3 & 7 \\ 3 & -6 & 6 \\ -5 & 8 & 4 \end{bmatrix}$: coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir las filas como columnas en otro orden.</details>

### F05-N2-18 · [C] Traspuesta

**Objetivo**: calcular la traspuesta y comprobar $(A + B)^T = A^T + B^T$.
**Dificultad**: N2

**Enunciado.** Con $A = \begin{bmatrix} 4 & 5 & -4 \\ 1 & 0 & 4 \\ 3 & -2 & -1 \end{bmatrix}$ y $B = \begin{bmatrix} 0 & -2 & -1 \\ 0 & 1 & -3 \\ 5 & 1 & 2 \end{bmatrix}$: a) halla $A^T$ y su tamaño; b) comprueba que $(A + B)^T = A^T + B^T$.

<details><summary>Pista 1</summary>Las filas de $A$ pasan a ser las columnas de $A^T$.</details>
<details><summary>Solución</summary>

a) $A^T = \begin{bmatrix} 4 & 1 & 3 \\ 5 & 0 & -2 \\ -4 & 4 & -1 \end{bmatrix}$, de tamaño $3\times 3$.

b) $A + B = \begin{bmatrix} 4 & 3 & -5 \\ 1 & 1 & 1 \\ 8 & -1 & 1 \end{bmatrix}$, luego $(A + B)^T = \begin{bmatrix} 4 & 1 & 8 \\ 3 & 1 & -1 \\ -5 & 1 & 1 \end{bmatrix}$. Además $A^T + B^T = \begin{bmatrix} 4 & 1 & 8 \\ 3 & 1 & -1 \\ -5 & 1 & 1 \end{bmatrix}$: coinciden.

</details>
<details><summary>Errores frecuentes</summary>Escribir las filas como columnas en otro orden.</details>

### F05-N2-19 · [K] ¿Qué operaciones se pueden hacer?

**Objetivo**: razonar con tamaños antes de calcular.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $2\times 3$ y $B$ de tamaño $2\times 3$. Di cuáles de estas operaciones están definidas y qué tamaño tiene el resultado: a) $A + B$; b) $3A$; c) $A^T$; d) $AB$.

<details><summary>Pista 1</summary>Para sumar, los tamaños deben coincidir; para multiplicar, columnas de la primera = filas de la segunda.</details>
<details><summary>Solución</summary>

a) $A + B$: sí, de tamaño $2\times 3$.

b) $3A$: sí, de tamaño $2\times 3$.

c) $A^T$: sí, de tamaño $3\times 2$.

d) $AB$: no, $A$ tiene 3 columnas y $B$ tiene 2 filas.

</details>
<details><summary>Errores frecuentes</summary>Creer que se puede multiplicar cuando los tamaños no encajan.</details>

### F05-N2-20 · [K] ¿Qué operaciones se pueden hacer?

**Objetivo**: razonar con tamaños antes de calcular.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $3\times 3$ y $B$ de tamaño $3\times 3$. Di cuáles de estas operaciones están definidas y qué tamaño tiene el resultado: a) $A + B$; b) $3A$; c) $A^T$; d) $AB$.

<details><summary>Pista 1</summary>Para sumar, los tamaños deben coincidir; para multiplicar, columnas de la primera = filas de la segunda.</details>
<details><summary>Solución</summary>

a) $A + B$: sí, de tamaño $3\times 3$.

b) $3A$: sí, de tamaño $3\times 3$.

c) $A^T$: sí, de tamaño $3\times 3$.

d) $AB$: sí, de tamaño $3\times 3$ (columnas de $A$ = filas de $B$ = 3).

</details>
<details><summary>Errores frecuentes</summary>Creer que se puede multiplicar cuando los tamaños no encajan.</details>

### F05-N2-21 · [K] ¿Qué operaciones se pueden hacer?

**Objetivo**: razonar con tamaños antes de calcular.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $2\times 3$ y $B$ de tamaño $3\times 2$. Di cuáles de estas operaciones están definidas y qué tamaño tiene el resultado: a) $A + B$; b) $3A$; c) $A^T$; d) $AB$.

<details><summary>Pista 1</summary>Para sumar, los tamaños deben coincidir; para multiplicar, columnas de la primera = filas de la segunda.</details>
<details><summary>Solución</summary>

a) $A + B$: no, los tamaños son distintos.

b) $3A$: sí, de tamaño $2\times 3$.

c) $A^T$: sí, de tamaño $3\times 2$.

d) $AB$: sí, de tamaño $2\times 2$ (columnas de $A$ = filas de $B$ = 3).

</details>
<details><summary>Errores frecuentes</summary>Creer que se puede multiplicar cuando los tamaños no encajan.</details>

### F05-N2-22 · [K] ¿Qué operaciones se pueden hacer?

**Objetivo**: razonar con tamaños antes de calcular.
**Dificultad**: N2

**Enunciado.** $A$ es de tamaño $2\times 2$ y $B$ de tamaño $2\times 3$. Di cuáles de estas operaciones están definidas y qué tamaño tiene el resultado: a) $A + B$; b) $3A$; c) $A^T$; d) $AB$.

<details><summary>Pista 1</summary>Para sumar, los tamaños deben coincidir; para multiplicar, columnas de la primera = filas de la segunda.</details>
<details><summary>Solución</summary>

a) $A + B$: no, los tamaños son distintos.

b) $3A$: sí, de tamaño $2\times 2$.

c) $A^T$: sí, de tamaño $2\times 2$.

d) $AB$: sí, de tamaño $2\times 3$ (columnas de $A$ = filas de $B$ = 2).

</details>
<details><summary>Errores frecuentes</summary>Creer que se puede multiplicar cuando los tamaños no encajan.</details>

### F05-N2-23 · [K] Tipos de matrices

**Objetivo**: reconocer matrices diagonales, triangulares y simétricas.
**Dificultad**: N2

**Enunciado.** Indica de qué tipo(s) es cada matriz: diagonal, triangular superior, simétrica (puede ser más de uno).

a) $\begin{bmatrix} 4 & 5 & 5 \\ 0 & 2 & 4 \\ 0 & 0 & 5 \end{bmatrix}$

b) $\begin{bmatrix} -3 & -3 & 5 \\ -3 & 4 & -1 \\ 5 & -1 & 0 \end{bmatrix}$

c) $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix}$

<details><summary>Pista 1</summary>Una matriz es simétrica si $A = A^T$; triangular superior si todo lo que hay bajo la diagonal es cero.</details>
<details><summary>Solución</summary>

a) triangular superior.

b) simétrica.

c) diagonal, triangular superior, simétrica.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que toda matriz diagonal también es triangular y simétrica.</details>

### F05-N2-24 · [K] Tipos de matrices

**Objetivo**: reconocer matrices diagonales, triangulares y simétricas.
**Dificultad**: N2

**Enunciado.** Indica de qué tipo(s) es cada matriz: diagonal, triangular superior, simétrica (puede ser más de uno).

a) $\begin{bmatrix} -2 & 0 & 1 \\ 0 & 4 & -2 \\ 1 & -2 & 2 \end{bmatrix}$

b) $\begin{bmatrix} 3 & 1 & 3 \\ 0 & 5 & 5 \\ 0 & 0 & 3 \end{bmatrix}$

c) $\begin{bmatrix} -3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 2 \end{bmatrix}$

<details><summary>Pista 1</summary>Una matriz es simétrica si $A = A^T$; triangular superior si todo lo que hay bajo la diagonal es cero.</details>
<details><summary>Solución</summary>

a) simétrica.

b) triangular superior.

c) diagonal, triangular superior, simétrica.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que toda matriz diagonal también es triangular y simétrica.</details>

### F05-N2-25 · [K] Tipos de matrices

**Objetivo**: reconocer matrices diagonales, triangulares y simétricas.
**Dificultad**: N2

**Enunciado.** Indica de qué tipo(s) es cada matriz: diagonal, triangular superior, simétrica (puede ser más de uno).

a) $\begin{bmatrix} 1 & -1 & -3 \\ -1 & -1 & 5 \\ -3 & 5 & -3 \end{bmatrix}$

b) $\begin{bmatrix} 1 & 4 & 4 \\ 0 & 3 & 5 \\ 0 & 0 & 2 \end{bmatrix}$

c) $\begin{bmatrix} 4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$

<details><summary>Pista 1</summary>Una matriz es simétrica si $A = A^T$; triangular superior si todo lo que hay bajo la diagonal es cero.</details>
<details><summary>Solución</summary>

a) simétrica.

b) triangular superior.

c) diagonal, triangular superior, simétrica.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que toda matriz diagonal también es triangular y simétrica.</details>

### F05-N2-26 · [K] Tipos de matrices

**Objetivo**: reconocer matrices diagonales, triangulares y simétricas.
**Dificultad**: N2

**Enunciado.** Indica de qué tipo(s) es cada matriz: diagonal, triangular superior, simétrica (puede ser más de uno).

a) $\begin{bmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$

b) $\begin{bmatrix} 4 & 3 & 2 \\ 0 & 5 & 4 \\ 0 & 0 & 1 \end{bmatrix}$

c) $\begin{bmatrix} 1 & 4 & 0 \\ 4 & 4 & 4 \\ 0 & 4 & 2 \end{bmatrix}$

<details><summary>Pista 1</summary>Una matriz es simétrica si $A = A^T$; triangular superior si todo lo que hay bajo la diagonal es cero.</details>
<details><summary>Solución</summary>

a) diagonal, triangular superior, simétrica.

b) triangular superior.

c) simétrica.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que toda matriz diagonal también es triangular y simétrica.</details>

### F05-N2-27 · [K] Tipos de matrices

**Objetivo**: reconocer matrices diagonales, triangulares y simétricas.
**Dificultad**: N2

**Enunciado.** Indica de qué tipo(s) es cada matriz: diagonal, triangular superior, simétrica (puede ser más de uno).

a) $\begin{bmatrix} 4 & 3 & 2 \\ 0 & 2 & 2 \\ 0 & 0 & 5 \end{bmatrix}$

b) $\begin{bmatrix} 4 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -2 \end{bmatrix}$

c) $\begin{bmatrix} 2 & 2 & 2 \\ 2 & -2 & 5 \\ 2 & 5 & -3 \end{bmatrix}$

<details><summary>Pista 1</summary>Una matriz es simétrica si $A = A^T$; triangular superior si todo lo que hay bajo la diagonal es cero.</details>
<details><summary>Solución</summary>

a) triangular superior.

b) diagonal, triangular superior, simétrica.

c) simétrica.

</details>
<details><summary>Errores frecuentes</summary>Olvidar que toda matriz diagonal también es triangular y simétrica.</details>

### F05-N2-28 · [C] Vector entre dos puntos

**Objetivo**: usar la resta de vectores y la media.
**Dificultad**: N2

**Enunciado.** Dados $P = (-1, -5, 2)$ y $Q = (-4, 3, 0)$, halla el vector $\overrightarrow{PQ}$ y el punto medio del segmento $PQ$.

<details><summary>Pista 1</summary>El vector de $P$ a $Q$ es «llegada menos salida».</details>
<details><summary>Solución</summary>

$\overrightarrow{PQ} = Q - P = (-3, 8, -2)$. El punto medio es $\frac{P + Q}{2} = (-\frac{5}{2}, -1, 1)$.

</details>
<details><summary>Errores frecuentes</summary>Restar en el orden contrario ($P - Q$).</details>

### F05-N2-29 · [C] Vector entre dos puntos

**Objetivo**: usar la resta de vectores y la media.
**Dificultad**: N2

**Enunciado.** Dados $P = (-2, 4, 2)$ y $Q = (-2, -4, 3)$, halla el vector $\overrightarrow{PQ}$ y el punto medio del segmento $PQ$.

<details><summary>Pista 1</summary>El vector de $P$ a $Q$ es «llegada menos salida».</details>
<details><summary>Solución</summary>

$\overrightarrow{PQ} = Q - P = (0, -8, 1)$. El punto medio es $\frac{P + Q}{2} = (-2, 0, \frac{5}{2})$.

</details>
<details><summary>Errores frecuentes</summary>Restar en el orden contrario ($P - Q$).</details>

### F05-N2-30 · [C] Vector entre dos puntos

**Objetivo**: usar la resta de vectores y la media.
**Dificultad**: N2

**Enunciado.** Dados $P = (5, 1, -4)$ y $Q = (-5, -2, 1)$, halla el vector $\overrightarrow{PQ}$ y el punto medio del segmento $PQ$.

<details><summary>Pista 1</summary>El vector de $P$ a $Q$ es «llegada menos salida».</details>
<details><summary>Solución</summary>

$\overrightarrow{PQ} = Q - P = (-10, -3, 5)$. El punto medio es $\frac{P + Q}{2} = (0, -\frac{1}{2}, -\frac{3}{2})$.

</details>
<details><summary>Errores frecuentes</summary>Restar en el orden contrario ($P - Q$).</details>

### F05-N2-31 · [C] Vector entre dos puntos

**Objetivo**: usar la resta de vectores y la media.
**Dificultad**: N2

**Enunciado.** Dados $P = (1, 2, 5)$ y $Q = (3, -5, 5)$, halla el vector $\overrightarrow{PQ}$ y el punto medio del segmento $PQ$.

<details><summary>Pista 1</summary>El vector de $P$ a $Q$ es «llegada menos salida».</details>
<details><summary>Solución</summary>

$\overrightarrow{PQ} = Q - P = (2, -7, 0)$. El punto medio es $\frac{P + Q}{2} = (2, -\frac{3}{2}, 5)$.

</details>
<details><summary>Errores frecuentes</summary>Restar en el orden contrario ($P - Q$).</details>

### F05-N2-32 · [C] Vector entre dos puntos

**Objetivo**: usar la resta de vectores y la media.
**Dificultad**: N2

**Enunciado.** Dados $P = (4, 0, 5)$ y $Q = (2, -4, -2)$, halla el vector $\overrightarrow{PQ}$ y el punto medio del segmento $PQ$.

<details><summary>Pista 1</summary>El vector de $P$ a $Q$ es «llegada menos salida».</details>
<details><summary>Solución</summary>

$\overrightarrow{PQ} = Q - P = (-2, -4, -7)$. El punto medio es $\frac{P + Q}{2} = (3, -2, \frac{3}{2})$.

</details>
<details><summary>Errores frecuentes</summary>Restar en el orden contrario ($P - Q$).</details>

### F05-N2-33 · [C] Vector entre dos puntos

**Objetivo**: usar la resta de vectores y la media.
**Dificultad**: N2

**Enunciado.** Dados $P = (-1, -5, 2)$ y $Q = (4, 0, 5)$, halla el vector $\overrightarrow{PQ}$ y el punto medio del segmento $PQ$.

<details><summary>Pista 1</summary>El vector de $P$ a $Q$ es «llegada menos salida».</details>
<details><summary>Solución</summary>

$\overrightarrow{PQ} = Q - P = (5, 5, 3)$. El punto medio es $\frac{P + Q}{2} = (\frac{3}{2}, -\frac{5}{2}, \frac{7}{2})$.

</details>
<details><summary>Errores frecuentes</summary>Restar en el orden contrario ($P - Q$).</details>

