# F06 — Producto matriz-vector, producto de matrices y transformaciones

Banco de las lecciones L19–L21. **Parte 1: 10 ejercicios**, ligados a los videos. La **parte 2** (30 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F06_producto_y_transformaciones_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Resultados comprobados en `ejercicios/verificar/f05_f07.py`.

| Lección | Ejercicios |
|---|---|
| L19 Matriz por vector | N1-01 🎬, N2-01 🎬 |
| L20 Producto de matrices | N2-02 🎬, N3-01 🎬, N2-03, N4-01 |
| L21 Transformaciones | N1-02 🎬, N3-02 🎬, N5-01 🎬, N5-02 |

---

### F06-N1-01 · [C] Matriz por vector 🎬

**Objetivo**: multiplicar fila por columna y comprobar dimensiones.
**Dificultad**: N1

**Enunciado.** Calcula, si está definido: a) $\begin{bmatrix} 2 & -1 \\ 0 & 3 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 4 \\ 5 \end{bmatrix}$ b) $\begin{bmatrix} 1 & 0 & 2 \end{bmatrix}\begin{bmatrix} 3 \\ -1 \\ 4 \end{bmatrix}$ c) $\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$

<details><summary>Pista 1</summary>Columnas de la matriz = componentes del vector.</details>
<details><summary>Pista 2</summary>Cada fila por la columna da una componente.</details>
<details><summary>Solución</summary>

a) $(3, 15, 9)$: $8 - 5$, $0 + 15$, $4 + 5$. b) $[\,11\,]$ ($1\times 1$). c) No definido: 2 columnas y 3 componentes.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Multiplicar columna por fila; olvidar el signo de $-1$.</details>

### F06-N2-01 · [C] Dos miradas 🎬

**Objetivo**: calcular $A\mathbf{x}$ por filas y por columnas.
**Dificultad**: N2

**Enunciado.** $A = \begin{bmatrix} 2 & -1 & 3 \\ 0 & 4 & 1 \end{bmatrix}$, $\mathbf{x} = (1, 2, -1)$. Calcula $A\mathbf{x}$ por filas y por columnas.

<details><summary>Pista 1</summary>Filas: $2\cdot 1 + (-1)\cdot 2 + 3\cdot(-1)$.</details>
<details><summary>Pista 2</summary>Columnas: $1\cdot(2, 0) + 2\cdot(-1, 4) + (-1)\cdot(3, 1)$.</details>
<details><summary>Solución</summary>

Por filas: $(2 - 2 - 3,\ 0 + 8 - 1) = (-3, 7)$. Por columnas: $(2, 0) + (-2, 8) + (-3, -1) = (-3, 7)$.

**Verificación**: coinciden.
</details>
<details><summary>Errores frecuentes</summary>Usar las filas de $A$ como si fueran las columnas.</details>

### F06-N2-02 · [C] AB y BA 🎬

**Objetivo**: calcular productos de dimensiones distintas.
**Dificultad**: N2

**Enunciado.** $A = \begin{bmatrix} 1 & -1 \\ 2 & 0 \\ 3 & 1 \end{bmatrix}$, $B = \begin{bmatrix} 2 & 1 & 0 \\ -1 & 4 & 2 \end{bmatrix}$. Dimensión y valor de $AB$ y $BA$.

<details><summary>Pista 1</summary>$(3\times 2)(2\times 3) = 3\times 3$; $(2\times 3)(3\times 2) = 2\times 2$.</details>
<details><summary>Pista 2</summary>$(AB)_{11} = 1\cdot 2 + (-1)(-1) = 3$.</details>
<details><summary>Solución</summary>

$AB = \begin{bmatrix} 3 & -3 & -2 \\ 4 & 2 & 0 \\ 5 & 7 & 2 \end{bmatrix}$, $BA = \begin{bmatrix} 4 & -2 \\ 13 & 3 \end{bmatrix}$.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Pensar que $AB$ y $BA$ deben tener la misma dimensión.</details>

### F06-N2-03 · [K] ¿Qué productos existen?

**Objetivo**: decidir si un producto está definido y su dimensión.
**Dificultad**: N2

**Enunciado.** $A$ es $2\times 3$, $B$ es $3\times 3$, $C$ es $3\times 1$. ¿Cuáles están definidos y de qué dimensión son? $AB$, $BA$, $BC$, $CB$, $AC$, $ABC$.

<details><summary>Pista 1</summary>Los números "de dentro" deben coincidir.</details>
<details><summary>Pista 2</summary>$ABC = (AB)C$.</details>
<details><summary>Solución</summary>

$AB$: $2\times 3$. $BA$: no ($3\times 3$ por $2\times 3$). $BC$: $3\times 1$. $CB$: no ($3\times 1$ por $3\times 3$). $AC$: $2\times 1$. $ABC$: $2\times 1$.

**Verificación**: aplicar $(m\times n)(n\times p) = m\times p$.
</details>
<details><summary>Errores frecuentes</summary>Comparar los números "de fuera".</details>

### F06-N3-01 · [C] Conmutar no se puede 🎬

**Objetivo**: comprobar la no conmutatividad y sus consecuencias.
**Dificultad**: N3

**Enunciado.** $A = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}$, $B = \begin{bmatrix} 1 & 4 \\ 0 & -1 \end{bmatrix}$. Calcula $AB$, $BA$, $AI_2$. ¿Es $(A + B)^2 = A^2 + 2AB + B^2$?

<details><summary>Pista 1</summary>$(A + B)^2 = (A + B)(A + B) = A^2 + AB + BA + B^2$.</details>
<details><summary>Pista 2</summary>Solo sería $A^2 + 2AB + B^2$ si $AB = BA$.</details>
<details><summary>Solución</summary>

$AB = \begin{bmatrix} 2 & 8 \\ 1 & 1 \end{bmatrix}$, $BA = \begin{bmatrix} 6 & 12 \\ -1 & -3 \end{bmatrix}$, $AI_2 = A$. Como $AB \neq BA$, no: $(A + B)^2 = \begin{bmatrix} 13 & 20 \\ 5 & 8 \end{bmatrix}$ y $A^2 + 2AB + B^2 = \begin{bmatrix} 9 & 16 \\ 7 & 12 \end{bmatrix}$.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Aplicar las fórmulas de números ("binomio al cuadrado") a matrices.</details>

### F06-N4-01 · [K] No se puede simplificar

**Objetivo**: entender que $AB = AC$ no implica $B = C$.
**Dificultad**: N4

**Enunciado.** Con $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$, encuentra $B \neq C$ con $AB = AC$.

<details><summary>Pista 1</summary>$AB = AC \Leftrightarrow A(B - C) = O$.</details>
<details><summary>Pista 2</summary>Busca una $D \neq O$ con $AD = O$ (la escena de L20 tiene una) y toma $C = B - D$.</details>
<details><summary>Solución</summary>

Por ejemplo $B = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ y $C = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}$: $AB = AC = \begin{bmatrix} 1 & 0 \\ 1 & 0 \end{bmatrix}$.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>"Dividir entre $A$".</details>

### F06-N1-02 · [C] Una matriz que estira 🎬

**Objetivo**: ver qué hace una matriz con vectores concretos.
**Dificultad**: N1

**Enunciado.** $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$. Calcula $A$ por $(1, 0)$, $(0, 1)$, $(1, 1)$, $(-2, 3)$. ¿Qué hace con el plano?

<details><summary>Pista 1</summary>Multiplica fila por columna.</details>
<details><summary>Pista 2</summary>¿Qué le pasa a la primera componente? ¿Y a la segunda?</details>
<details><summary>Solución</summary>

$(3, 0)$, $(0, 1)$, $(3, 1)$, $(-6, 3)$. Estira el plano en horizontal por 3 y deja igual la dirección vertical.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Multiplicar también la segunda componente por 3.</details>

### F06-N3-02 · [C] Construir la matriz con las imágenes 🎬

**Objetivo**: usar que las columnas son $A\mathbf{e}_1$ y $A\mathbf{e}_2$.
**Dificultad**: N3

**Enunciado.** $A$ lleva $\mathbf{e}_1$ a $(0, 1)$ y $\mathbf{e}_2$ a $(-1, 0)$. a) Escribe $A$. b) $A(3, 2)$. c) ¿Qué movimiento es?

<details><summary>Pista 1</summary>Columna 1 = $A\mathbf{e}_1$, columna 2 = $A\mathbf{e}_2$.</details>
<details><summary>Pista 2</summary>Dibuja dónde van $\mathbf{e}_1$ y $\mathbf{e}_2$.</details>
<details><summary>Solución</summary>

a) $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$. b) $3(0, 1) + 2(-1, 0) = (-2, 3)$. c) Un giro de $90°$ en sentido antihorario alrededor del origen.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Colocar las imágenes como filas en vez de columnas.</details>

### F06-N5-01 · [D] ¿Lineal o no? 🎬

**Objetivo**: comprobar la linealidad con la definición o refutarla con un contraejemplo.
**Dificultad**: N5

**Enunciado.** ¿Son lineales $T(x, y) = (x + y,\ 2x)$, $S(x, y) = (x + 1,\ y)$, $R(x, y) = (xy,\ y)$?

<details><summary>Pista 1</summary>Si $T(\mathbf{0}) \neq \mathbf{0}$, no es lineal.</details>
<details><summary>Pista 2</summary>Para $R$, compara $R(2\cdot(1, 1))$ con $2R(1, 1)$.</details>
<details><summary>Solución</summary>

- $T$ sí: $T(x, y) = \begin{bmatrix} 1 & 1 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix}$, y toda transformación de la forma $\mathbf{x} \mapsto A\mathbf{x}$ es lineal (L21).
- $S$ no: $S(0, 0) = (1, 0) \neq (0, 0)$.
- $R$ no: $R(2, 2) = (4, 2)$, pero $2R(1, 1) = (2, 2)$.

**Verificación**: $T(2, 5) = (7, 4)$ y $\begin{bmatrix} 1 & 1 \\ 2 & 0 \end{bmatrix}(2, 5) = (7, 4)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Decir que $S$ es lineal "porque no tiene potencias" (sumar una constante también rompe la linealidad).</details>

### F06-N5-02 · [D] Las columnas son las imágenes de la base

**Objetivo**: demostrar el resultado clave de L21 en cualquier dimensión.
**Dificultad**: N5

**Enunciado.** Sea $A$ una matriz $m\times n$ y $\mathbf{e}_j$ el vector de $\mathbb{R}^n$ con un 1 en la posición $j$ y 0 en el resto. Demuestra que $A\mathbf{e}_j$ es la columna $j$ de $A$.

<details><summary>Pista 1</summary>Calcula la componente $i$ de $A\mathbf{e}_j$ con la fórmula del sumatorio.</details>
<details><summary>Pista 2</summary>En la suma, todos los términos tienen un factor 0 excepto uno.</details>
<details><summary>Solución</summary>

$(A\mathbf{e}_j)_i = \sum_{k=1}^{n} a_{ik}\,(\mathbf{e}_j)_k = a_{ij}\cdot 1 = a_{ij}$, porque $(\mathbf{e}_j)_k = 0$ si $k \neq j$. Las componentes de $A\mathbf{e}_j$ son $a_{1j}, \dots, a_{mj}$: la columna $j$. $\blacksquare$

**Verificación** (ejemplo): $\begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$.
</details>
<details><summary>Errores frecuentes</summary>Confundir $\mathbf{e}_j$ con la fila $j$.</details>
