# F10 — Factorización LU (parte 2)

Segunda parte del banco de las lecciones L34–L38: **20 ejercicios** de práctica que completan la parte 1 (`F10_factorizacion_lu.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N3: 16, N4: 4 · [C] 17, [K] 3.

---

### F10-N3-11 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} -2 & 3 & 0 \\ 6 & -8 & -2 \\ -2 & 4 & -4 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = -3$, $\ell_{31} = 1$, $\ell_{32} = 1$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -2 & 3 & 0 \\ 0 & 1 & -2 \\ 0 & 0 & -2 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} -2 & 3 & 0 \\ 6 & -8 & -2 \\ -2 & 4 & -4 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-12 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} 1 & 1 & -3 \\ -3 & -4 & 12 \\ 0 & 0 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = -3$, $\ell_{31} = 0$, $\ell_{32} = 0$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 1 & 1 & -3 \\ 0 & -1 & 3 \\ 0 & 0 & 1 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} 1 & 1 & -3 \\ -3 & -4 & 12 \\ 0 & 0 & 1 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-13 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} -1 & -2 & 3 \\ 0 & 2 & 3 \\ -3 & -12 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = 0$, $\ell_{31} = 3$, $\ell_{32} = -3$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 3 & -3 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -1 & -2 & 3 \\ 0 & 2 & 3 \\ 0 & 0 & 2 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} -1 & -2 & 3 \\ 0 & 2 & 3 \\ -3 & -12 & 2 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-14 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} -2 & -2 & -2 \\ 4 & 3 & 4 \\ -6 & -9 & -5 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = -2$, $\ell_{31} = 3$, $\ell_{32} = 3$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 3 & 3 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -2 & -2 & -2 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} -2 & -2 & -2 \\ 4 & 3 & 4 \\ -6 & -9 & -5 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-15 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} -1 & 1 & -2 \\ 2 & 1 & 1 \\ -3 & 6 & -7 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = -2$, $\ell_{31} = 3$, $\ell_{32} = 1$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 3 & 1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -1 & 1 & -2 \\ 0 & 3 & -3 \\ 0 & 0 & 2 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} -1 & 1 & -2 \\ 2 & 1 & 1 \\ -3 & 6 & -7 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-16 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} 3 & 1 & 0 \\ 0 & -1 & -1 \\ -9 & 0 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = 0$, $\ell_{31} = -3$, $\ell_{32} = -3$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -3 & -3 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 3 & 1 & 0 \\ 0 & -1 & -1 \\ 0 & 0 & -2 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} 3 & 1 & 0 \\ 0 & -1 & -1 \\ -9 & 0 & 1 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-17 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} -2 & 3 & -1 \\ -6 & 8 & -3 \\ 6 & -8 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = 3$, $\ell_{31} = -3$, $\ell_{32} = -1$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ -3 & -1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -2 & 3 & -1 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} -2 & 3 & -1 \\ -6 & 8 & -3 \\ 6 & -8 & 2 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-18 · [C] Factorización $A = LU$

**Objetivo**: obtener $L$ y $U$ guardando los multiplicadores.
**Dificultad**: N3

**Enunciado.** Factoriza $A = LU$ (sin intercambios): $A = \begin{bmatrix} -1 & 1 & 3 \\ 1 & 2 & -4 \\ 3 & 0 & -8 \end{bmatrix}$.

<details><summary>Pista 1</summary>El multiplicador $\ell_{ik}$ es (entrada a eliminar) / (pivote).</details>
<details><summary>Pista 2</summary>$U$ es la matriz escalonada que resulta de eliminar.</details>
<details><summary>Solución</summary>

Multiplicadores: $\ell_{21} = -1$, $\ell_{31} = -3$, $\ell_{32} = 1$.

$L = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ -3 & 1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -1 & 1 & 3 \\ 0 & 3 & -1 \\ 0 & 0 & 2 \end{bmatrix}$.

Comprobación: $LU = \begin{bmatrix} -1 & 1 & 3 \\ 1 & 2 & -4 \\ 3 & 0 & -8 \end{bmatrix} = A$.

</details>
<details><summary>Errores frecuentes</summary>Guardar el multiplicador con el signo contrario en $L$.</details>

### F10-N3-19 · [C] Resolver con $LU$

**Objetivo**: resolver $A\mathbf{x} = \mathbf{b}$ con dos sustituciones.
**Dificultad**: N3

**Enunciado.** Dado $A = LU$ con $L = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 1 & 3 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} -1 & 1 & -3 \\ 0 & -2 & 2 \\ 0 & 0 & 1 \end{bmatrix}$, resuelve $A\mathbf{x} = \begin{bmatrix} -9 \\ 21 \\ 30 \end{bmatrix}$.

<details><summary>Pista 1</summary>Llama $\mathbf{y} = U\mathbf{x}$.</details>
<details><summary>Pista 2</summary>Resuelve primero con $L$, empezando por la primera fila.</details>
<details><summary>Solución</summary>

Primero $L\mathbf{y} = \mathbf{b}$ (hacia adelante): $\mathbf{y} = (-9, 12, 3)$. Después $U\mathbf{x} = \mathbf{y}$ (hacia atrás): $\mathbf{x} = (-3, -3, 3)$.

Comprobación: $A\mathbf{x} = (-9, 21, 30)$.

</details>
<details><summary>Errores frecuentes</summary>Resolver con $U$ antes que con $L$.</details>

### F10-N3-20 · [C] Resolver con $LU$

**Objetivo**: resolver $A\mathbf{x} = \mathbf{b}$ con dos sustituciones.
**Dificultad**: N3

**Enunciado.** Dado $A = LU$ con $L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -2 & -2 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} 1 & -1 & 1 \\ 0 & -2 & 2 \\ 0 & 0 & 3 \end{bmatrix}$, resuelve $A\mathbf{x} = \begin{bmatrix} -4 \\ -2 \\ 6 \end{bmatrix}$.

<details><summary>Pista 1</summary>Llama $\mathbf{y} = U\mathbf{x}$.</details>
<details><summary>Pista 2</summary>Resuelve primero con $L$, empezando por la primera fila.</details>
<details><summary>Solución</summary>

Primero $L\mathbf{y} = \mathbf{b}$ (hacia adelante): $\mathbf{y} = (-4, -2, -6)$. Después $U\mathbf{x} = \mathbf{y}$ (hacia atrás): $\mathbf{x} = (-3, -1, -2)$.

Comprobación: $A\mathbf{x} = (-4, -2, 6)$.

</details>
<details><summary>Errores frecuentes</summary>Resolver con $U$ antes que con $L$.</details>

### F10-N3-21 · [C] Resolver con $LU$

**Objetivo**: resolver $A\mathbf{x} = \mathbf{b}$ con dos sustituciones.
**Dificultad**: N3

**Enunciado.** Dado $A = LU$ con $L = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ -1 & -2 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} 1 & 3 & 3 \\ 0 & 3 & 0 \\ 0 & 0 & -2 \end{bmatrix}$, resuelve $A\mathbf{x} = \begin{bmatrix} 3 \\ -9 \\ 5 \end{bmatrix}$.

<details><summary>Pista 1</summary>Llama $\mathbf{y} = U\mathbf{x}$.</details>
<details><summary>Pista 2</summary>Resuelve primero con $L$, empezando por la primera fila.</details>
<details><summary>Solución</summary>

Primero $L\mathbf{y} = \mathbf{b}$ (hacia adelante): $\mathbf{y} = (3, -6, -4)$. Después $U\mathbf{x} = \mathbf{y}$ (hacia atrás): $\mathbf{x} = (3, -2, 2)$.

Comprobación: $A\mathbf{x} = (3, -9, 5)$.

</details>
<details><summary>Errores frecuentes</summary>Resolver con $U$ antes que con $L$.</details>

### F10-N3-22 · [C] Resolver con $LU$

**Objetivo**: resolver $A\mathbf{x} = \mathbf{b}$ con dos sustituciones.
**Dificultad**: N3

**Enunciado.** Dado $A = LU$ con $L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -2 & 3 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} 1 & -1 & 3 \\ 0 & -1 & -1 \\ 0 & 0 & 1 \end{bmatrix}$, resuelve $A\mathbf{x} = \begin{bmatrix} -4 \\ -9 \\ 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Llama $\mathbf{y} = U\mathbf{x}$.</details>
<details><summary>Pista 2</summary>Resuelve primero con $L$, empezando por la primera fila.</details>
<details><summary>Solución</summary>

Primero $L\mathbf{y} = \mathbf{b}$ (hacia adelante): $\mathbf{y} = (-4, -1, -1)$. Después $U\mathbf{x} = \mathbf{y}$ (hacia atrás): $\mathbf{x} = (1, 2, -1)$.

Comprobación: $A\mathbf{x} = (-4, -9, 4)$.

</details>
<details><summary>Errores frecuentes</summary>Resolver con $U$ antes que con $L$.</details>

### F10-N3-23 · [C] Resolver con $LU$

**Objetivo**: resolver $A\mathbf{x} = \mathbf{b}$ con dos sustituciones.
**Dificultad**: N3

**Enunciado.** Dado $A = LU$ con $L = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & -3 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} -2 & 1 & 2 \\ 0 & -2 & 1 \\ 0 & 0 & -1 \end{bmatrix}$, resuelve $A\mathbf{x} = \begin{bmatrix} -5 \\ 16 \\ -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Llama $\mathbf{y} = U\mathbf{x}$.</details>
<details><summary>Pista 2</summary>Resuelve primero con $L$, empezando por la primera fila.</details>
<details><summary>Solución</summary>

Primero $L\mathbf{y} = \mathbf{b}$ (hacia adelante): $\mathbf{y} = (-5, 1, 1)$. Después $U\mathbf{x} = \mathbf{y}$ (hacia atrás): $\mathbf{x} = (1, -1, -1)$.

Comprobación: $A\mathbf{x} = (-5, 16, -2)$.

</details>
<details><summary>Errores frecuentes</summary>Resolver con $U$ antes que con $L$.</details>

### F10-N3-24 · [K] ¿Existe $A = LU$?

**Objetivo**: reconocer cuándo falla la factorización sin intercambios.
**Dificultad**: N3

**Enunciado.** ¿Admite la matriz $A = \begin{bmatrix} 0 & 3 & 2 \\ 1 & 1 & 2 \\ 1 & 2 & 3 \end{bmatrix}$ una factorización $A = LU$ sin permutaciones? ¿Y $PA = LU$?

<details><summary>Pista 1</summary>Mira la entrada $(1,1)$.</details>
<details><summary>Solución</summary>

No admite $A = LU$: el primer pivote es $0$ y, sin intercambiar filas, no se puede eliminar la primera columna. Sí admite $PA = LU$ (si $A$ es invertible siempre se puede con una permutación adecuada): su determinante es $-1\ne 0$.

</details>
<details><summary>Errores frecuentes</summary>Pensar que una matriz invertible siempre tiene $LU$ directa.</details>

### F10-N3-25 · [K] ¿Existe $A = LU$?

**Objetivo**: reconocer cuándo falla la factorización sin intercambios.
**Dificultad**: N3

**Enunciado.** ¿Admite la matriz $A = \begin{bmatrix} 0 & 2 & 2 \\ 4 & 1 & 2 \\ 1 & 2 & 3 \end{bmatrix}$ una factorización $A = LU$ sin permutaciones? ¿Y $PA = LU$?

<details><summary>Pista 1</summary>Mira la entrada $(1,1)$.</details>
<details><summary>Solución</summary>

No admite $A = LU$: el primer pivote es $0$ y, sin intercambiar filas, no se puede eliminar la primera columna. Sí admite $PA = LU$ (si $A$ es invertible siempre se puede con una permutación adecuada): su determinante es $-6\ne 0$.

</details>
<details><summary>Errores frecuentes</summary>Pensar que una matriz invertible siempre tiene $LU$ directa.</details>

### F10-N3-26 · [K] ¿Existe $A = LU$?

**Objetivo**: reconocer cuándo falla la factorización sin intercambios.
**Dificultad**: N3

**Enunciado.** ¿Admite la matriz $A = \begin{bmatrix} 0 & 2 & 3 \\ 2 & 1 & 2 \\ 1 & 2 & 3 \end{bmatrix}$ una factorización $A = LU$ sin permutaciones? ¿Y $PA = LU$?

<details><summary>Pista 1</summary>Mira la entrada $(1,1)$.</details>
<details><summary>Solución</summary>

No admite $A = LU$: el primer pivote es $0$ y, sin intercambiar filas, no se puede eliminar la primera columna. Sí admite $PA = LU$ (si $A$ es invertible siempre se puede con una permutación adecuada): su determinante es $1\ne 0$.

</details>
<details><summary>Errores frecuentes</summary>Pensar que una matriz invertible siempre tiene $LU$ directa.</details>

### F10-N4-11 · [C] $PA = LU$ con pivoteo

**Objetivo**: factorizar con una matriz de permutación cuando aparece un pivote nulo.
**Dificultad**: N4

**Enunciado.** Esta matriz no admite $A = LU$ sin intercambios. Halla $P$, $L$, $U$ con $PA = LU$ (pivoteo parcial): $A = \begin{bmatrix} 0 & 1 & 4 \\ 1 & 1 & 4 \\ 3 & 2 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Si el pivote es cero, intercambia con una fila inferior; los multiplicadores viajan con su fila.</details>
<details><summary>Solución</summary>

Eligiendo en cada columna el pivote de mayor valor absoluto: $P = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ \frac{1}{3} & \frac{1}{3} & 1 \end{bmatrix}$, $U = \begin{bmatrix} 3 & 2 & 1 \\ 0 & 1 & 4 \\ 0 & 0 & \frac{7}{3} \end{bmatrix}$.

Comprobación: $PA = \begin{bmatrix} 3 & 2 & 1 \\ 0 & 1 & 4 \\ 1 & 1 & 4 \end{bmatrix}$ y $LU = \begin{bmatrix} 3 & 2 & 1 \\ 0 & 1 & 4 \\ 1 & 1 & 4 \end{bmatrix}$ coinciden.

</details>
<details><summary>Errores frecuentes</summary>Olvidar intercambiar también los multiplicadores ya guardados en $L$.</details>

### F10-N4-12 · [C] $PA = LU$ con pivoteo

**Objetivo**: factorizar con una matriz de permutación cuando aparece un pivote nulo.
**Dificultad**: N4

**Enunciado.** Esta matriz no admite $A = LU$ sin intercambios. Halla $P$, $L$, $U$ con $PA = LU$ (pivoteo parcial): $A = \begin{bmatrix} 3 & 4 & 4 \\ 3 & 4 & -3 \\ -3 & 0 & 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Si el pivote es cero, intercambia con una fila inferior; los multiplicadores viajan con su fila.</details>
<details><summary>Solución</summary>

Eligiendo en cada columna el pivote de mayor valor absoluto: $P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 3 & 4 & 4 \\ 0 & 4 & 8 \\ 0 & 0 & -7 \end{bmatrix}$.

Comprobación: $PA = \begin{bmatrix} 3 & 4 & 4 \\ -3 & 0 & 4 \\ 3 & 4 & -3 \end{bmatrix}$ y $LU = \begin{bmatrix} 3 & 4 & 4 \\ -3 & 0 & 4 \\ 3 & 4 & -3 \end{bmatrix}$ coinciden.

</details>
<details><summary>Errores frecuentes</summary>Olvidar intercambiar también los multiplicadores ya guardados en $L$.</details>

### F10-N4-13 · [C] $PA = LU$ con pivoteo

**Objetivo**: factorizar con una matriz de permutación cuando aparece un pivote nulo.
**Dificultad**: N4

**Enunciado.** Esta matriz no admite $A = LU$ sin intercambios. Halla $P$, $L$, $U$ con $PA = LU$ (pivoteo parcial): $A = \begin{bmatrix} -3 & 1 & 0 \\ 3 & -1 & 4 \\ -4 & 2 & -1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Si el pivote es cero, intercambia con una fila inferior; los multiplicadores viajan con su fila.</details>
<details><summary>Solución</summary>

Eligiendo en cada columna el pivote de mayor valor absoluto: $P = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ -\frac{3}{4} & 1 & 0 \\ \frac{3}{4} & -1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -4 & 2 & -1 \\ 0 & \frac{1}{2} & \frac{13}{4} \\ 0 & 0 & 4 \end{bmatrix}$.

Comprobación: $PA = \begin{bmatrix} -4 & 2 & -1 \\ 3 & -1 & 4 \\ -3 & 1 & 0 \end{bmatrix}$ y $LU = \begin{bmatrix} -4 & 2 & -1 \\ 3 & -1 & 4 \\ -3 & 1 & 0 \end{bmatrix}$ coinciden.

</details>
<details><summary>Errores frecuentes</summary>Olvidar intercambiar también los multiplicadores ya guardados en $L$.</details>

### F10-N4-14 · [C] $PA = LU$ con pivoteo

**Objetivo**: factorizar con una matriz de permutación cuando aparece un pivote nulo.
**Dificultad**: N4

**Enunciado.** Esta matriz no admite $A = LU$ sin intercambios. Halla $P$, $L$, $U$ con $PA = LU$ (pivoteo parcial): $A = \begin{bmatrix} 0 & 4 & -1 \\ 1 & 3 & -1 \\ 1 & 3 & 3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Si el pivote es cero, intercambia con una fila inferior; los multiplicadores viajan con su fila.</details>
<details><summary>Solución</summary>

Eligiendo en cada columna el pivote de mayor valor absoluto: $P = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 1 & 3 & -1 \\ 0 & 4 & -1 \\ 0 & 0 & 4 \end{bmatrix}$.

Comprobación: $PA = \begin{bmatrix} 1 & 3 & -1 \\ 0 & 4 & -1 \\ 1 & 3 & 3 \end{bmatrix}$ y $LU = \begin{bmatrix} 1 & 3 & -1 \\ 0 & 4 & -1 \\ 1 & 3 & 3 \end{bmatrix}$ coinciden.

</details>
<details><summary>Errores frecuentes</summary>Olvidar intercambiar también los multiplicadores ya guardados en $L$.</details>

