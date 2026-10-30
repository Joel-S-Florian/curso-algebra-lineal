# F10 — Factorización LU y PA = LU

Banco de las lecciones L34–L38. **Parte 1: 20 ejercicios**, ligados a los videos. La **parte 2** (20 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F10_factorizacion_lu_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $L$ triangular inferior con unos en la diagonal, $U$ triangular superior, $P$ de permutación. $R_i \leftarrow R_i - m\,R_j$ es la operación de la eliminación; $m_{ij}$ es su multiplicador.
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f10.py`.

| Lección | Ejercicios |
|---|---|
| L34 Factorizar, triangulares y elementales | N1-01 🎬, N2-01 🎬, N2-02 🎬 |
| L35 De dónde sale $A = LU$ | N2-03 🎬, N3-01, N3-02 🎬, N4-01, N5-01 |
| L36 Resolver con LU | N2-04 🎬, N3-03 🎬, N3-06, N4-02 🎬 |
| L37 Permutaciones y $PA = LU$ | N2-05, N3-04 🎬, N3-05 🎬, N4-03 🎬, N5-02 |
| L38 Comparación y aplicaciones | N2-06 🎬, N3-07 🎬, N4-04 |

---

### F10-N1-01 · [C] Comprobar una factorización 🎬

**Objetivo**: calcular el producto $LU$.
**Dificultad**: N1

**Enunciado.** Comprueba que $\begin{bmatrix} 2 & 1 \\ 6 & 7 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \\ 0 & 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Cada entrada es una fila de $L$ por una columna de $U$.</details>
<details><summary>Pista 2</summary>Entrada $(2,2)$: $3\cdot 1 + 1\cdot 4$.</details>
<details><summary>Solución</summary>

Fila 1: $[\,1\cdot 2 + 0,\ 1\cdot 1 + 0\,] = [\,2,\ 1\,]$. Fila 2: $[\,3\cdot 2 + 0,\ 3\cdot 1 + 1\cdot 4\,] = [\,6,\ 7\,]$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Multiplicar posición a posición en lugar de fila por columna.</details>

### F10-N2-01 · [C] Sistemas triangulares 🎬

**Objetivo**: sustitución hacia adelante y hacia atrás.
**Dificultad**: N2

**Enunciado.** Resuelve, diciendo si la sustitución es hacia adelante o hacia atrás: a) $\;2x = 6,\ x + 3y = 5$; b) $\;x - y + 2z = 3,\ 4y - z = 7,\ 2z = 6$.

<details><summary>Pista 1</summary>Busca la ecuación con una sola incógnita.</details>
<details><summary>Pista 2</summary>a) empieza por la primera; b) por la última.</details>
<details><summary>Solución</summary>

a) **Hacia adelante** (matriz inferior): $x = 3$, $y = \frac{5 - 3}{3} = \frac23$. b) **Hacia atrás** (superior): $z = 3$, $y = \frac{7 + 3}{4} = \frac52$, $x = 3 + \frac52 - 6 = -\frac12$.

**Verificación** de b): $-\frac12 - \frac52 + 6 = 3$ ✓, $10 - 3 = 7$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Sustituir en sentido contrario al que permite la forma de la matriz.</details>

### F10-N2-02 · [C] Una matriz elemental 🎬

**Objetivo**: construir la matriz de una operación por filas y su inversa.
**Dificultad**: N2

**Enunciado.** Escribe la matriz elemental $E$ de $3\times 3$ tal que $EA$ hace $R_3 \leftarrow R_3 - 4R_1$, y calcula $E^{-1}$. Comprueba el efecto sobre $A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 3 & 1 \\ -1 & 1 & 2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Parte de la identidad y pon $-4$ en la posición $(3, 1)$.</details>
<details><summary>Pista 2</summary>La inversa deshace la operación: $R_3 \leftarrow R_3 + 4R_1$.</details>
<details><summary>Solución</summary>

$E = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$, $E^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 4 & 0 & 1 \end{bmatrix}$. En $EA$ la fila 3 es $[-1, 1, 2] - 4[1, 2, -1] = [-5, -7, 6]$ y las otras no cambian; $EE^{-1} = I$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Poner el $-4$ en la posición $(1, 3)$ (esa matriz opera sobre columnas al multiplicar por la derecha, o sobre otra fila).</details>

### F10-N2-03 · [C] Primera factorización LU 🎬

**Objetivo**: anotar el multiplicador al eliminar.
**Dificultad**: N2

**Enunciado.** Halla $L$ y $U$ de $A = \begin{bmatrix} 4 & 3 \\ 8 & 5 \end{bmatrix}$ y comprueba que $A = LU$.

<details><summary>Pista 1</summary>La operación es $R_2 \leftarrow R_2 - m\,R_1$ con $m = 8/4$.</details>
<details><summary>Pista 2</summary>El multiplicador va en la posición $(2, 1)$ de $L$.</details>
<details><summary>Solución</summary>

$m_{21} = 2$: $R_2 \leftarrow R_2 - 2R_1$ da $U = \begin{bmatrix} 4 & 3 \\ 0 & -1 \end{bmatrix}$; $L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$.

**Verificación**: $LU = \begin{bmatrix} 4 & 3 \\ 8 & 6 - 1 \end{bmatrix} = \begin{bmatrix} 4 & 3 \\ 8 & 5 \end{bmatrix}$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Anotar $-2$ en $L$ en lugar de $2$: $L$ guarda $m$ (se resta $m\,R_1$), no $-m$.</details>

### F10-N3-01 · [C] Un LU de 3 × 3

**Objetivo**: reunir los multiplicadores de tres pasos.
**Dificultad**: N3

**Enunciado.** Halla $L$ y $U$ de $A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & -6 & 0 \\ -2 & 7 & 2 \end{bmatrix}$ y comprueba $A = LU$.

<details><summary>Pista 1</summary>$m_{21} = 2$, $m_{31} = -1$.</details>
<details><summary>Pista 2</summary>Tras los dos primeros pasos, la fila 3 es $[0, 8, 3]$ y la fila 2, $[0, -8, -2]$.</details>
<details><summary>Solución</summary>

$m_{21} = 2$, $m_{31} = -1$, $m_{32} = \frac{8}{-8} = -1$. $U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 0 & 1 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}$.

**Verificación**: fila 3 de $LU$: $-1[2, 1, 1] - 1[0, -8, -2] + [0, 0, 1] = [-2, 7, 2]$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Calcular $m_{32}$ con la fila 3 original en lugar de la ya modificada.</details>

### F10-N3-02 · [K] El orden del producto de inversas 🎬

**Objetivo**: ver por qué $L = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$ y no al revés.
**Dificultad**: N3

**Enunciado.** Con $E_{21}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, $E_{31}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -1 & 0 & 1 \end{bmatrix}$ y $E_{32}^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1 \end{bmatrix}$, calcula $E_{32}^{-1}E_{31}^{-1}E_{21}^{-1}$ y explica por qué no es $L$.

<details><summary>Pista 1</summary>Multiplica primero $E_{31}^{-1}E_{21}^{-1}$.</details>
<details><summary>Pista 2</summary>Fíjate en la entrada $(3, 1)$.</details>
<details><summary>Solución</summary>

El producto es $\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -7 & -3 & 1 \end{bmatrix}$: en la posición $(3, 1)$ aparece $-1 + (-3)(2) = -7$, mezcla de multiplicadores. En el orden correcto, $E_{31}^{-1}E_{32}^{-1}$ coloca cada multiplicador en su sitio y da $L$ con $-1$ en $(3,1)$.
</details>
<details><summary>Errores frecuentes</summary>Dar por buena cualquier orden: el producto de matrices no es conmutativo (L20).</details>

### F10-N4-01 · [C] LU con fracciones

**Objetivo**: multiplicadores fraccionarios.
**Dificultad**: N4

**Enunciado.** Halla $L$ y $U$ de $A = \begin{bmatrix} 2 & 4 & -2 \\ 1 & 3 & 0 \\ 3 & 7 & 4 \end{bmatrix}$ con fracciones exactas y comprueba el producto.

<details><summary>Pista 1</summary>$m_{21} = \frac12$, $m_{31} = \frac32$.</details>
<details><summary>Pista 2</summary>Tras los dos primeros pasos, las filas 2 y 3 son $[0, 1, 1]$ y $[0, 1, 7]$.</details>
<details><summary>Solución</summary>

$m_{32} = 1$. $U = \begin{bmatrix} 2 & 4 & -2 \\ 0 & 1 & 1 \\ 0 & 0 & 6 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ \frac12 & 1 & 0 \\ \frac32 & 1 & 1 \end{bmatrix}$.

**Verificación**: fila 3 de $LU$: $\frac32[2, 4, -2] + [0, 1, 1] + [0, 0, 6] = [3, 7, 4]$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Pasar a decimales y arrastrar redondeos.</details>

### F10-N5-01 · [D] Unicidad de LU

**Objetivo**: demostrar que, si existe, $A = LU$ con $L$ de unos y $A$ invertible es única.
**Dificultad**: N5

**Enunciado.** Sea $A$ invertible con $A = L_1U_1 = L_2U_2$, donde $L_1, L_2$ son triangulares inferiores con unos en la diagonal y $U_1, U_2$ triangulares superiores. Demuestra que $L_1 = L_2$ y $U_1 = U_2$.

<details><summary>Pista 1</summary>$U_1, U_2$ son invertibles (porque $A$ lo es). Despeja $L_2^{-1}L_1 = U_2U_1^{-1}$.</details>
<details><summary>Pista 2</summary>¿Qué forma tiene una matriz que es a la vez triangular inferior con unos y triangular superior?</details>
<details><summary>Solución</summary>

De $L_1U_1 = L_2U_2$: $L_2^{-1}L_1 = U_2U_1^{-1}$. El lado izquierdo es triangular inferior con unos en la diagonal (el producto y la inversa de tales matrices lo son); el derecho es triangular superior. Una matriz con ambas formas es diagonal, y con unos en la diagonal es $I$. Luego $L_2^{-1}L_1 = I$, es decir $L_1 = L_2$, y entonces $U_1 = U_2$. $\blacksquare$
</details>
<details><summary>Errores frecuentes</summary>Olvidar justificar que $U_1$ es invertible; no usar los unos de la diagonal.</details>

### F10-N2-04 · [C] Sustitución hacia adelante 🎬

**Objetivo**: resolver $L\mathbf{y} = \mathbf{b}$.
**Dificultad**: N2

**Enunciado.** Resuelve $\begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}\begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 3 \\ 13 \end{bmatrix}$ y, con $U = \begin{bmatrix} 2 & 1 \\ 0 & 4 \end{bmatrix}$, resuelve después $U\mathbf{x} = \mathbf{y}$.

<details><summary>Pista 1</summary>La primera ecuación da $y_1$ directamente.</details>
<details><summary>Pista 2</summary>$3y_1 + y_2 = 13$.</details>
<details><summary>Solución</summary>

$y_1 = 3$, $y_2 = 13 - 9 = 4$. Después $4x_2 = 4 \Rightarrow x_2 = 1$ y $2x_1 + 1 = 3 \Rightarrow x_1 = 1$: $\mathbf{x} = (1, 1)$.

**Verificación**: $A = LU = \begin{bmatrix} 2 & 1 \\ 6 & 7 \end{bmatrix}$ y $A(1, 1) = (3, 13)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Resolver primero $U\mathbf{x}$ con $\mathbf{b}$ en lugar de con $\mathbf{y}$.</details>

### F10-N3-03 · [C] Resolver con LU 🎬

**Objetivo**: las dos sustituciones y la verificación en $A$.
**Dificultad**: N3

**Enunciado.** Con $L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -3 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} 1 & 2 & -1 \\ 0 & -1 & 3 \\ 0 & 0 & 10 \end{bmatrix}$ (de $A = LU$), resuelve $A\mathbf{x} = \mathbf{b}$ con $\mathbf{b} = (0, 1, -3)$ y verifica en $A$.

<details><summary>Pista 1</summary>Primero $L\mathbf{y} = \mathbf{b}$, hacia adelante.</details>
<details><summary>Pista 2</summary>Obtendrás $\mathbf{y} = (0, 1, 0)$.</details>
<details><summary>Solución</summary>

$y_1 = 0$, $y_2 = 1 - 0 = 1$, $y_3 = -3 + 0 + 3 = 0$. Luego $10z = 0 \Rightarrow z = 0$; $-y + 0 = 1 \Rightarrow y = -1$; $x - 2 - 0 = 0 \Rightarrow x = 2$. $\mathbf{x} = (2, -1, 0)$.

**Verificación**: $A\mathbf{x} = (2 - 2 - 0,\ 4 - 3 + 0,\ -2 - 1 + 0) = (0, 1, -3)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Verificar en $U\mathbf{x} = \mathbf{y}$ en vez de en $A\mathbf{x} = \mathbf{b}$.</details>

### F10-N3-06 · [K] ¿Qué es $\mathbf{y}$?

**Objetivo**: interpretar $\mathbf{y} = L^{-1}\mathbf{b}$.
**Dificultad**: N3

**Enunciado.** Explica por qué el vector $\mathbf{y}$ de $L\mathbf{y} = \mathbf{b}$ coincide con la columna de términos independientes de la matriz aumentada tras la eliminación de Gauss, y compruébalo con $\mathbf{b} = (-3, 1, 2)$ y el $A$ de la lección.

<details><summary>Pista 1</summary>$E_{32}E_{31}E_{21}A = U$ y $L = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$.</details>
<details><summary>Pista 2</summary>Entonces $L^{-1} = E_{32}E_{31}E_{21}$: aplica a $\mathbf{b}$ las mismas operaciones que a $A$.</details>
<details><summary>Solución</summary>

Como $L^{-1} = E_{32}E_{31}E_{21}$, $\mathbf{y} = L^{-1}\mathbf{b} = E_{32}E_{31}E_{21}\mathbf{b}$: las mismas operaciones que llevaron $A$ a $U$ aplicadas a $\mathbf{b}$. Con $\mathbf{b} = (-3, 1, 2)$: $E_{21}\mathbf{b} = (-3, 7, 2)$, $E_{31}(\cdot) = (-3, 7, -1)$, $E_{32}(\cdot) = (-3, 7, 20)$ ✓, que es la última columna de la aumentada escalonada.
</details>
<details><summary>Errores frecuentes</summary>Aplicar las operaciones en otro orden.</details>

### F10-N4-02 · [C] Contar operaciones 🎬

**Objetivo**: coste de factorizar y de resolver.
**Dificultad**: N4

**Enunciado.** Para $n = 3$, cuenta las multiplicaciones y divisiones de: a) factorizar $A$ (sin $\mathbf{b}$); b) $L\mathbf{y} = \mathbf{b}$ y $U\mathbf{x} = \mathbf{y}$. Comprueba que suman lo mismo que Gauss con un solo $\mathbf{b}$ ($17$).

<details><summary>Pista 1</summary>Factorizar: cada multiplicador es una división; cada fila actualizada, una multiplicación por entrada a la derecha del pivote.</details>
<details><summary>Pista 2</summary>Sustitución hacia adelante con unos: $\frac{n(n-1)}{2}$; hacia atrás: $\frac{n(n+1)}{2}$.</details>
<details><summary>Solución</summary>

a) $\sum_{j=1}^{n-1} j(j+1) = \frac{n^3 - n}{3} = 8$. b) $\frac{3\cdot 2}{2} + \frac{3\cdot 4}{2} = 3 + 6 = 9 = n^2$. Total $8 + 9 = 17$ ✓ ($= \frac{27 + 27 - 3}{3}$ de Gauss). La diferencia aparece con un segundo $\mathbf{b}$: LU solo añade $9$; Gauss repite $17$.
</details>
<details><summary>Errores frecuentes</summary>Contar la columna $\mathbf{b}$ dentro de la factorización: se trata aparte.</details>

### F10-N2-05 · [K] ¿Admite LU?

**Objetivo**: reconocer cuándo falla $A = LU$.
**Dificultad**: N2

**Enunciado.** Demuestra que $A = \begin{bmatrix} 0 & 2 \\ 3 & 1 \end{bmatrix}$ no admite $A = LU$ (con $L$ de unos) y encuentra $P$ con $PA = LU$.

<details><summary>Pista 1</summary>Si $A = LU$, entonces $a_{11} = u_{11}$ y $a_{21} = l_{21}u_{11}$.</details>
<details><summary>Pista 2</summary>$P$ intercambia las dos filas.</details>
<details><summary>Solución</summary>

Si $A = LU$, $a_{11} = 1\cdot u_{11} = 0$ y entonces $a_{21} = l_{21}u_{11} = 0$, pero $a_{21} = 3$: contradicción. Con $P = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$: $PA = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix} = I\cdot\begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$, así que $L = I$ y $U = PA$.
</details>
<details><summary>Errores frecuentes</summary>Concluir que $A$ no es invertible: lo es ($\det = -6$); solo falla la factorización sin permutar.</details>

### F10-N3-04 · [C] $PA = LU$ y resolver 🎬

**Objetivo**: hallar $P$, $L$, $U$ y resolver con $P\mathbf{b}$.
**Dificultad**: N3

**Enunciado.** Para $A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 5 \\ 4 & 6 & 8 \end{bmatrix}$, halla $P$, $L$ y $U$ con $PA = LU$, y resuelve $A\mathbf{x} = \mathbf{b}$ con $\mathbf{b} = (3, 9, 18)$.

<details><summary>Pista 1</summary>Tras anular la columna 1, el candidato a pivote de la columna 2 es $0$: intercambia las filas 2 y 3.</details>
<details><summary>Pista 2</summary>Reordena $\mathbf{b}$ con la misma $P$: $P\mathbf{b} = (3, 18, 9)$.</details>
<details><summary>Solución</summary>

$P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}$, $PA = \begin{bmatrix} 1 & 1 & 1 \\ 4 & 6 & 8 \\ 2 & 2 & 5 \end{bmatrix}$, $L = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 2 & 0 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 4 \\ 0 & 0 & 3 \end{bmatrix}$. $L\mathbf{y} = P\mathbf{b}$: $\mathbf{y} = (3, 6, 3)$. $U\mathbf{x} = \mathbf{y}$: $z = 1$, $y = 1$, $x = 1$.

**Verificación**: $A(1,1,1) = (3, 9, 18)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar reordenar $\mathbf{b}$; intercambiar solo las filas de $A$ sin cambiar $L$ en los multiplicadores ya calculados.</details>

### F10-N3-05 · [K] Matrices de permutación 🎬

**Objetivo**: propiedades de las permutaciones.
**Dificultad**: N3

**Enunciado.** a) Escribe la matriz de permutación $P$ de $3\times 3$ tal que $PA$ tiene por filas $(R_3, R_1, R_2)$. b) Calcula $PP^T$. c) ¿Cuántas matrices de permutación hay de $4\times 4$?

<details><summary>Pista 1</summary>La fila $i$ de $P$ tiene un $1$ en la columna de la fila de $A$ que quieres en la posición $i$.</details>
<details><summary>Pista 2</summary>c) cuenta los órdenes posibles de 4 filas.</details>
<details><summary>Solución</summary>

a) $P = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$. b) $PP^T = I$ (cada fila por sí misma da $1$ y por las otras $0$): $P^{-1} = P^T$. c) $4! = 24$.
</details>
<details><summary>Errores frecuentes</summary>Confundir $P$ con $P^T$ (reordenan al revés).</details>

### F10-N4-03 · [C] Pivoteo parcial con 3 cifras 🎬

**Objetivo**: ver el efecto del redondeo.
**Dificultad**: N4

**Enunciado.** Resuelve $\;0{,}0002\,x + y = 1,\ x + y = 3$ con 3 cifras significativas en cada operación: a) sin intercambiar; b) intercambiando antes las filas. Compara con la solución exacta.

<details><summary>Pista 1</summary>a) $m = \frac{1}{0{,}0002} = 5000$.</details>
<details><summary>Pista 2</summary>Exacta: $x = \frac{-2}{0{,}0002 - 1} \approx 2{,}0004$.</details>
<details><summary>Solución</summary>

Exacta: $x \approx 2{,}0004$, $y \approx 0{,}9996$. a) $m = 5000$; $1 - 5000 \approx -5{,}00\cdot 10^3$ y $3 - 5000 \approx -5{,}00\cdot 10^3$, luego $y = 1{,}00$ y $x = \frac{1 - 1{,}00}{0{,}0002} = 0$ (**incorrecto**). b) $m = 0{,}0002$; $1 - 0{,}0002 \approx 1{,}00$ y $1 - 0{,}0006 \approx 0{,}999$, luego $y = 0{,}999$ y $x = 3 - 0{,}999 \approx 2{,}00$ (**correcto**).
</details>
<details><summary>Errores frecuentes</summary>Pensar que el método falla: lo que falla es el redondeo al dividir entre un pivote muy pequeño.</details>

### F10-N5-02 · [D] La inversa de una permutación

**Objetivo**: demostrar $P^{-1} = P^T$.
**Dificultad**: N5

**Enunciado.** Demuestra que, si $P$ es una matriz de permutación, $P^TP = I$.

<details><summary>Pista 1</summary>La entrada $(i, j)$ de $P^TP$ es el producto escalar de las columnas $i$ y $j$ de $P$.</details>
<details><summary>Pista 2</summary>Cada columna de $P$ tiene un único $1$, y dos columnas distintas lo tienen en filas distintas.</details>
<details><summary>Solución</summary>

La columna $i$ de $P$ es un vector $\mathbf{e}_{\sigma(i)}$ de la base canónica, con $\sigma$ inyectiva (cada fila tiene un único $1$). Entonces $(P^TP)_{ij} = \mathbf{e}_{\sigma(i)}\cdot\mathbf{e}_{\sigma(j)} = 1$ si $\sigma(i) = \sigma(j)$, es decir $i = j$, y $0$ en otro caso: $P^TP = I$. $\blacksquare$
</details>
<details><summary>Errores frecuentes</summary>Probarlo solo con un ejemplo concreto.</details>

### F10-N2-06 · [C] Dos lados derechos con la misma factorización 🎬

**Objetivo**: reutilizar $L$ y $U$.
**Dificultad**: N2

**Enunciado.** Con $L = \begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}$ y $U = \begin{bmatrix} 2 & 1 \\ 0 & 4 \end{bmatrix}$ (de $A = \begin{bmatrix} 2 & 1 \\ 6 & 7 \end{bmatrix}$), resuelve $A\mathbf{x} = \mathbf{b}$ para $\mathbf{b}_1 = (3, 13)$ y $\mathbf{b}_2 = (1, -3)$.

<details><summary>Pista 1</summary>Para $\mathbf{b}_1$ ya lo hiciste en F10-N2-04.</details>
<details><summary>Pista 2</summary>Para $\mathbf{b}_2$: $y_1 = 1$, $y_2 = -3 - 3 = -6$.</details>
<details><summary>Solución</summary>

$\mathbf{b}_1$: $\mathbf{x} = (1, 1)$. $\mathbf{b}_2$: $\mathbf{y} = (1, -6)$; $4x_2 = -6 \Rightarrow x_2 = -\frac32$; $2x_1 - \frac32 = 1 \Rightarrow x_1 = \frac54$.

**Verificación**: $A(\frac54, -\frac32) = (\frac52 - \frac32,\ \frac{15}{2} - \frac{21}{2}) = (1, -3)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Volver a eliminar para el segundo $\mathbf{b}$.</details>

### F10-N3-07 · [K] Elegir el método 🎬

**Objetivo**: usar la tabla comparativa.
**Dificultad**: N3

**Enunciado.** Elige método y justifica: a) una matriz fija y 200 lados derechos distintos; b) un sistema $2\times 2$ en un examen; c) decidir si dos sistemas son equivalentes; d) una matriz distinta en cada problema, un solo $\mathbf{b}$ por matriz.

<details><summary>Pista 1</summary>Piensa cuántas veces se reutiliza la eliminación.</details>
<details><summary>Pista 2</summary>Para c) recuerda la unicidad de la forma reducida (L31).</details>
<details><summary>Solución</summary>

a) $PA = LU$: se factoriza una vez y cada $\mathbf{b}$ cuesta $n^2$. b) Sustitución, igualación o Gauss-Jordan: pocas operaciones y lectura directa. c) Forma reducida: dos sistemas son equivalentes si y solo si tienen la misma. d) Gauss (o $PA = LU$, que cuesta lo mismo con un solo $\mathbf{b}$): no hay nada que reutilizar.
</details>
<details><summary>Errores frecuentes</summary>Pensar que LU siempre gana: con $k = 1$ cuesta lo mismo que Gauss.</details>

### F10-N4-04 · [D] Cuándo gana LU

**Objetivo**: deducir la diferencia de costes.
**Dificultad**: N4

**Enunciado.** Con coste de LU $\frac{n^3 - n}{3} + kn^2$ y de Gauss repetido $k\,\frac{n^3 + 3n^2 - n}{3}$ (multiplicaciones y divisiones, $k$ lados derechos), demuestra que la diferencia es $(k - 1)\,\frac{n^3 - n}{3}$ y deduce cuándo gana LU.

<details><summary>Pista 1</summary>Escribe $\frac{n^3 + 3n^2 - n}{3} = \frac{n^3 - n}{3} + n^2$.</details>
<details><summary>Pista 2</summary>Agrupa los términos en $k$.</details>
<details><summary>Solución</summary>

Gauss repetido $= k\left[\frac{n^3 - n}{3} + n^2\right] = k\,\frac{n^3 - n}{3} + kn^2$. Restando el coste de LU: $k\,\frac{n^3 - n}{3} - \frac{n^3 - n}{3} = (k - 1)\,\frac{n^3 - n}{3} \ge 0$, con igualdad solo si $k = 1$ (o $n = 1$). Así, LU nunca pierde y gana en cuanto $k \ge 2$ ($n \ge 2$).

**Comprobación**: $n = 100$, $k = 50$: $49\cdot 333\,300 = 16\,331\,700 = 17\,165\,000 - 833\,300$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar que el coste de la factorización se paga una sola vez.</details>
