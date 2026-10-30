# F16 — Demostraciones (parte 2)

Segunda parte del banco de las lecciones L54: **25 ejercicios** de práctica que completan la parte 1 (`F16_demostraciones.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N3: 5, N4: 8, N5: 12 · [D] 25.

---

### F16-N3-11 · [D] Un sistema lineal no tiene exactamente dos soluciones

**Objetivo**: un sistema lineal no tiene exactamente dos soluciones.
**Dificultad**: N3

**Enunciado.** Prueba que un sistema lineal tiene $0$, $1$ o infinitas soluciones; en particular no puede tener exactamente dos.

<details><summary>Pista 1</summary>Si hay dos soluciones, prueba que toda la recta que las une es solución.</details>
<details><summary>Solución</summary>

Si $\mathbf{x}$ e $\mathbf{y}$ son soluciones distintas, para cada $t \in \mathbb{R}$ el vector $\mathbf{z}_t = \mathbf{x} + t(\mathbf{y} - \mathbf{x})$ cumple $A\mathbf{z}_t = A\mathbf{x} + t(A\mathbf{y} - A\mathbf{x}) = \mathbf{b} + t(\mathbf{b} - \mathbf{b}) = \mathbf{b}$. Como los $\mathbf{z}_t$ son todos distintos (porque $\mathbf{y} \ne \mathbf{x}$), hay infinitas soluciones. $\blacksquare$

</details>

### F16-N3-12 · [D] El homogéneo es cerrado bajo suma y múltiplos

**Objetivo**: el homogéneo es cerrado bajo suma y múltiplos.
**Dificultad**: N3

**Enunciado.** Si $A\mathbf{x} = \mathbf{0}$ y $A\mathbf{y} = \mathbf{0}$, prueba que $A(\mathbf{x} + \mathbf{y}) = \mathbf{0}$ y $A(c\mathbf{x}) = \mathbf{0}$.

<details><summary>Pista 1</summary>Usa que el producto matriz-vector es lineal.</details>
<details><summary>Solución</summary>

Por linealidad, $A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}$ y $A(c\mathbf{x}) = c\,A\mathbf{x} = c\,\mathbf{0} = \mathbf{0}$. $\blacksquare$

</details>

### F16-N3-13 · [D] Traspuesta de un producto

**Objetivo**: traspuesta de un producto.
**Dificultad**: N3

**Enunciado.** Prueba que $(AB)^T = B^TA^T$.

<details><summary>Pista 1</summary>Compara las entradas $(i, j)$ de los dos miembros.</details>
<details><summary>Solución</summary>

La entrada $(i, j)$ de $(AB)^T$ es la entrada $(j, i)$ de $AB$: $\sum_k a_{jk}b_{ki}$. La entrada $(i, j)$ de $B^TA^T$ es $\sum_k (B^T)_{ik}(A^T)_{kj} = \sum_k b_{ki}a_{jk}$. Coinciden para todo $(i, j)$. $\blacksquare$

</details>

### F16-N3-14 · [D] Las operaciones elementales son reversibles

**Objetivo**: las operaciones elementales son reversibles.
**Dificultad**: N3

**Enunciado.** Prueba que cada operación elemental por filas se deshace con otra operación elemental.

<details><summary>Pista 1</summary>Para cada tipo, busca la operación inversa.</details>
<details><summary>Solución</summary>

$R_i \leftrightarrow R_j$ se deshace repitiéndola. $R_i \leftarrow cR_i$ ($c \ne 0$) se deshace con $R_i \leftarrow \frac1c R_i$. $R_i \leftarrow R_i + cR_j$ ($i \ne j$) se deshace con $R_i \leftarrow R_i - cR_j$, porque la fila $j$ no cambió. $\blacksquare$

</details>

### F16-N3-15 · [D] Homogéneo con más incógnitas que ecuaciones

**Objetivo**: homogéneo con más incógnitas que ecuaciones.
**Dificultad**: N3

**Enunciado.** Prueba que un sistema homogéneo con $m < n$ tiene soluciones no triviales.

<details><summary>Pista 1</summary>Cuenta pivotes y variables libres.</details>
<details><summary>Solución</summary>

El rango cumple $\operatorname{rg}(A) \le m < n$, así que al menos una columna no tiene pivote y hay una variable libre. Dando a esa variable el valor $1$ y a las otras libres el valor $0$, se obtiene una solución distinta de $\mathbf{0}$. $\blacksquare$

</details>

### F16-N4-11 · [D] Las operaciones elementales conservan las soluciones

**Objetivo**: las operaciones elementales conservan las soluciones.
**Dificultad**: N4

**Enunciado.** Prueba que si $[A' \mid \mathbf{b}']$ se obtiene de $[A \mid \mathbf{b}]$ por operaciones elementales, ambos sistemas tienen las mismas soluciones.

<details><summary>Pista 1</summary>Prueba las dos inclusiones; usa la reversibilidad para la segunda.</details>
<details><summary>Solución</summary>

Basta una operación. Si $\mathbf{x}$ resuelve el sistema original, cumple las ecuaciones $E_i$; la nueva ecuación es una combinación de ellas ($E_i + cE_j$, $cE_i$ o un intercambio) y $\mathbf{x}$ la cumple. Recíprocamente, la operación es reversible (ejercicio anterior), así que las ecuaciones originales son combinación de las nuevas y toda solución del nuevo sistema resuelve el original. $\blacksquare$

</details>

### F16-N4-12 · [D] $\operatorname{rg}(A) \le \min(m, n)$

**Objetivo**: $\operatorname{rg}(A) \le \min(m, n)$.
**Dificultad**: N4

**Enunciado.** Prueba que el rango de una matriz $m \times n$ no supera $m$ ni $n$.

<details><summary>Pista 1</summary>Un pivote ocupa su fila y su columna.</details>
<details><summary>Solución</summary>

El rango es el número de pivotes. Hay a lo sumo un pivote por fila, luego $\le m$, y a lo sumo un pivote por columna, luego $\le n$. $\blacksquare$

</details>

### F16-N4-13 · [D] Rango de la matriz aumentada

**Objetivo**: rango de la matriz aumentada.
**Dificultad**: N4

**Enunciado.** Prueba que $\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1$.

<details><summary>Pista 1</summary>Piensa en los pivotes de las primeras $n$ columnas.</details>
<details><summary>Solución</summary>

Al escalonar $[A \mid \mathbf{b}]$ se escalona $A$ con las mismas operaciones: los pivotes de $A$ son pivotes de $[A \mid \mathbf{b}]$, luego el primer rango es $\le$ el segundo. La columna $\mathbf{b}$ es una sola y añade a lo sumo un pivote (hay a lo sumo uno por columna). $\blacksquare$

</details>

### F16-N4-14 · [D] Producto de triangulares inferiores unitarias

**Objetivo**: producto de triangulares inferiores unitarias.
**Dificultad**: N4

**Enunciado.** Prueba que el producto de dos matrices triangulares inferiores con unos en la diagonal es triangular inferior con unos en la diagonal.

<details><summary>Pista 1</summary>Mira qué índices $k$ hacen no nulos los dos factores.</details>
<details><summary>Solución</summary>

Si $L_1, L_2$ son triangulares inferiores, $(L_1L_2)_{ij} = \sum_k (L_1)_{ik}(L_2)_{kj}$. Para $i < j$ cada sumando tiene $(L_1)_{ik} \ne 0$ solo si $k \le i$ y $(L_2)_{kj} \ne 0$ solo si $k \ge j$; como $i < j$ no hay $k$ posible: la entrada es $0$. Para $i = j$ solo sobrevive $k = i$: $(L_1)_{ii}(L_2)_{ii} = 1\cdot 1 = 1$. $\blacksquare$

</details>

### F16-N4-15 · [D] Núcleo trivial y columnas independientes

**Objetivo**: núcleo trivial y columnas independientes.
**Dificultad**: N4

**Enunciado.** Prueba que $\ker A = \{\mathbf{0}\}$ si y solo si las columnas de $A$ son linealmente independientes.

<details><summary>Pista 1</summary>Lee $A\mathbf{x}$ por columnas.</details>
<details><summary>Solución</summary>

$A\mathbf{x} = x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n$. Entonces $\ker A = \{\mathbf{0}\}$ significa que la única combinación de columnas igual a $\mathbf{0}$ es la trivial, que es la definición de independencia. $\blacksquare$

</details>

### F16-N4-16 · [D] El espacio columna y la existencia de solución

**Objetivo**: el espacio columna y la existencia de solución.
**Dificultad**: N4

**Enunciado.** Prueba que $\operatorname{Col}(A)$ es un subespacio de $\mathbb{R}^m$ y que $A\mathbf{x} = \mathbf{b}$ tiene solución si y solo si $\mathbf{b} \in \operatorname{Col}(A)$.

<details><summary>Pista 1</summary>Usa $\operatorname{Col}(A) = \{A\mathbf{x}\}$.</details>
<details><summary>Solución</summary>

$\operatorname{Col}(A) = \{A\mathbf{x}\}$. Contiene a $\mathbf{0} = A\mathbf{0}$; si $\mathbf{u} = A\mathbf{x}$ y $\mathbf{v} = A\mathbf{y}$, entonces $\mathbf{u} + \mathbf{v} = A(\mathbf{x} + \mathbf{y})$ y $c\mathbf{u} = A(c\mathbf{x})$: es un subespacio de $\mathbb{R}^m$. Que $A\mathbf{x} = \mathbf{b}$ tenga solución es, por definición, que $\mathbf{b} = A\mathbf{x}$ para algún $\mathbf{x}$, es decir, $\mathbf{b} \in \operatorname{Col}(A)$. $\blacksquare$

</details>

### F16-N4-17 · [D] Solución única para todo $\mathbf{b}$

**Objetivo**: solución única para todo $\mathbf{b}$.
**Dificultad**: N4

**Enunciado.** Sea $A$ cuadrada $n \times n$ con $\operatorname{rg}(A) = n$. Prueba que $A\mathbf{x} = \mathbf{b}$ tiene solución única para todo $\mathbf{b}$.

<details><summary>Pista 1</summary>Escribe la reducida de $[A \mid \mathbf{b}]$.</details>
<details><summary>Solución</summary>

Con $\operatorname{rg}(A) = n$ todas las filas y columnas tienen pivote: la reducida de $A$ es $I$. Entonces la reducida de $[A \mid \mathbf{b}]$ es $[I \mid \mathbf{c}]$, sin filas contradictorias y sin variables libres: hay una única solución $\mathbf{x} = \mathbf{c}$. $\blacksquare$

</details>

### F16-N4-18 · [D] Diferencia de soluciones

**Objetivo**: diferencia de soluciones.
**Dificultad**: N4

**Enunciado.** Prueba que si $\mathbf{x}_1, \mathbf{x}_2$ son soluciones de $A\mathbf{x} = \mathbf{b}$, entonces $\mathbf{x}_1 - \mathbf{x}_2 \in \ker A$; y que la solución es única si y solo si $\ker A = \{\mathbf{0}\}$ (cuando hay alguna).

<details><summary>Pista 1</summary>Resta las dos ecuaciones.</details>
<details><summary>Solución</summary>

$A(\mathbf{x}_1 - \mathbf{x}_2) = \mathbf{b} - \mathbf{b} = \mathbf{0}$. Si $\ker A = \{\mathbf{0}\}$, la diferencia es $\mathbf{0}$ y hay una sola solución. Si hay $\mathbf{n} \ne \mathbf{0}$ en $\ker A$ y $\mathbf{x}_p$ es solución, $\mathbf{x}_p + \mathbf{n}$ es otra solución distinta. $\blacksquare$

</details>

### F16-N5-11 · [D] Teorema de Rouché-Frobenius

**Objetivo**: teorema de Rouché-Frobenius.
**Dificultad**: N5

**Enunciado.** Prueba: $A\mathbf{x} = \mathbf{b}$ es compatible si y solo si $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$; y en ese caso la solución es única si y solo si el rango es $n$.

<details><summary>Pista 1</summary>Fíjate en si hay un pivote en la columna de $\mathbf{b}$.</details>
<details><summary>Solución</summary>

Se escalona $[A \mid \mathbf{b}]$. Los rangos son distintos exactamente cuando hay un pivote en la última columna, es decir, una fila $[0 \dots 0 \mid c]$ con $c \ne 0$, que es la ecuación imposible $0 = c$: incompatible. Si los rangos coinciden, no hay tal fila y se resuelve hacia atrás: el sistema es compatible. Las variables libres son las $n - \operatorname{rg}(A)$ columnas sin pivote; hay solución única si y solo si no hay libres, es decir, $\operatorname{rg}(A) = n$. $\blacksquare$

</details>

### F16-N5-12 · [D] Teorema del rango y la nulidad

**Objetivo**: teorema del rango y la nulidad.
**Dificultad**: N5

**Enunciado.** Prueba que $\operatorname{rg}(A) + \operatorname{nul}(A) = n$ para una matriz $m \times n$.

<details><summary>Pista 1</summary>Cuenta columnas con y sin pivote.</details>
<details><summary>Solución</summary>

Sea $r$ el número de pivotes. Las $r$ columnas con pivote de la reducida son $\mathbf{e}_1, \dots, \mathbf{e}_r$ y las demás son combinación de ellas; como $A$ y la reducida tienen las mismas relaciones entre columnas, las $r$ columnas pivote de $A$ son una base de $\operatorname{Col}(A)$: $\dim\operatorname{Col}(A) = r$. Cada una de las $n - r$ variables libres aporta un vector a una base de $\ker A$ (generan, y son independientes por los unos y ceros en las posiciones libres): $\dim\ker A = n - r$. Suman $n$. $\blacksquare$

</details>

### F16-N5-13 · [D] Las columnas pivote son una base de $\operatorname{Col}(A)$

**Objetivo**: las columnas pivote son una base de $\operatorname{Col}(A)$.
**Dificultad**: N5

**Enunciado.** Prueba que las columnas de $A$ en las posiciones de los pivotes de su reducida $R$ son una base de $\operatorname{Col}(A)$.

<details><summary>Pista 1</summary>Compara $\ker A$ y $\ker R$.</details>
<details><summary>Solución</summary>

Escribe $R = EA$ con $E$ invertible. Para cualquier $\mathbf{x}$: $A\mathbf{x} = \mathbf{0} \iff R\mathbf{x} = \mathbf{0}$, es decir, $A$ y $R$ tienen las mismas relaciones lineales entre sus columnas. En $R$, las columnas pivote ($\mathbf{e}_1, \dots, \mathbf{e}_r$) son independientes y cada columna libre es combinación de ellas. Esas dos propiedades pasan a $A$: sus columnas pivote son independientes y generan las demás, luego generan $\operatorname{Col}(A)$. $\blacksquare$

</details>

### F16-N5-14 · [D] Un generador es mayor que un independiente

**Objetivo**: un generador es mayor que un independiente.
**Dificultad**: N5

**Enunciado.** Si $\mathbf{v}_1, \dots, \mathbf{v}_k$ generan un subespacio $S$ y $\mathbf{w}_1, \dots, \mathbf{w}_m \in S$ son independientes, prueba que $m \le k$.

<details><summary>Pista 1</summary>Escribe cada $\mathbf{w}_j$ con los $\mathbf{v}_i$ y mira el sistema que resulta.</details>
<details><summary>Solución</summary>

Cada $\mathbf{w}_j$ es combinación de los $\mathbf{v}_i$: $\mathbf{w}_j = \sum_i a_{ij}\mathbf{v}_i$. Sea $B = (a_{ij})$, de tamaño $k \times m$. Si $m > k$, el sistema homogéneo $B\mathbf{c} = \mathbf{0}$ tiene una solución $\mathbf{c} \ne \mathbf{0}$ (más incógnitas que ecuaciones). Entonces $\sum_j c_j\mathbf{w}_j = \sum_i \big(\sum_j a_{ij}c_j\big)\mathbf{v}_i = \mathbf{0}$ con $\mathbf{c} \ne \mathbf{0}$, contradiciendo la independencia. Luego $m \le k$. $\blacksquare$

</details>

### F16-N5-15 · [D] Todas las bases tienen el mismo número de vectores

**Objetivo**: todas las bases tienen el mismo número de vectores.
**Dificultad**: N5

**Enunciado.** Prueba que dos bases de un mismo subespacio tienen el mismo número de vectores.

<details><summary>Pista 1</summary>Aplica el resultado anterior dos veces.</details>
<details><summary>Solución</summary>

Sean $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ y $\{\mathbf{w}_1, \dots, \mathbf{w}_m\}$ bases de $S$. Los $\mathbf{v}$ generan y los $\mathbf{w}$ son independientes: $m \le k$ (ejercicio anterior). Intercambiando los papeles, $k \le m$. Luego $k = m$. $\blacksquare$

</details>

### F16-N5-16 · [D] El rango por filas y por columnas coincide

**Objetivo**: el rango por filas y por columnas coincide.
**Dificultad**: N5

**Enunciado.** Prueba que $\operatorname{rg}(A) = \operatorname{rg}(A^T)$.

<details><summary>Pista 1</summary>Las operaciones por filas conservan el espacio fila.</details>
<details><summary>Solución</summary>

Las operaciones por filas no cambian el espacio generado por las filas (cada fila nueva es combinación de las antiguas y, por reversibilidad, al revés). En la reducida, las $r$ filas no nulas son independientes (cada una tiene un $1$ en una columna pivote donde las demás tienen $0$): son una base del espacio fila, que tiene dimensión $r$. Pero $r$ es también $\operatorname{rg}(A)$ (número de pivotes). Como el espacio fila de $A$ es el espacio columna de $A^T$, resulta $\operatorname{rg}(A^T) = r = \operatorname{rg}(A)$. $\blacksquare$

</details>

### F16-N5-17 · [D] Existencia para todo $\mathbf{b}$

**Objetivo**: existencia para todo $\mathbf{b}$.
**Dificultad**: N5

**Enunciado.** Prueba que $A\mathbf{x} = \mathbf{b}$ tiene solución para todo $\mathbf{b} \in \mathbb{R}^m$ si y solo si $\operatorname{rg}(A) = m$.

<details><summary>Pista 1</summary>Recuerda que existencia equivale a $\operatorname{Col}(A) = \mathbb{R}^m$, es decir, $\dim\operatorname{Col}(A) = m$.</details>
<details><summary>Solución</summary>

($\Leftarrow$) Si $\operatorname{rg}(A) = m$, la reducida de $A$ no tiene filas nulas, así que $[A \mid \mathbf{b}]$ nunca produce una fila $[0 \dots 0 \mid c]$ con $c \ne 0$: es compatible. ($\Rightarrow$) Si $\operatorname{rg}(A) < m$, la reducida tiene una fila nula; deshaciendo las operaciones, existe $\mathbf{b}$ cuyo sistema reducido tiene esa fila $[0 \dots 0 \mid 1]$ (basta tomar $\mathbf{b} = E^{-1}\mathbf{e}_m$), que es incompatible. $\blacksquare$

</details>

### F16-N5-18 · [D] Unicidad de $A = LU$

**Objetivo**: unicidad de $A = LU$.
**Dificultad**: N5

**Enunciado.** Si $A$ es invertible y $A = L_1U_1 = L_2U_2$ con $L_i$ triangulares inferiores con unos en la diagonal y $U_i$ triangulares superiores, prueba que $L_1 = L_2$ y $U_1 = U_2$.

<details><summary>Pista 1</summary>Despeja para que a un lado queden las $L$ y al otro las $U$.</details>
<details><summary>Solución</summary>

Como $A$ es invertible, $L_i$ y $U_i$ también lo son (determinantes no nulos). De $L_1U_1 = L_2U_2$ se tiene $L_2^{-1}L_1 = U_2U_1^{-1}$. El miembro izquierdo es triangular inferior con unos en la diagonal (producto e inversa de matrices así); el derecho es triangular superior. Una matriz a la vez triangular inferior y superior es diagonal, y con unos en la diagonal es $I$. Luego $L_2^{-1}L_1 = I$, es decir, $L_1 = L_2$, y entonces $U_1 = U_2$. $\blacksquare$

</details>

### F16-N5-19 · [D] Coste de la factorización $LU$

**Objetivo**: coste de la factorización $LU$.
**Dificultad**: N5

**Enunciado.** Prueba que factorizar una matriz $n \times n$ sin intercambios cuesta $\frac{n^3 - n}{3}$ multiplicaciones y divisiones.

<details><summary>Pista 1</summary>Cuenta las operaciones de cada paso y suma con $\sum j$ y $\sum j^2$.</details>
<details><summary>Solución</summary>

En el paso $k$ ($k = 1, \dots, n-1$) hay $n - k$ filas por debajo del pivote. Para cada una se calcula un multiplicador (1 división) y se actualizan $n - k$ entradas (1 multiplicación cada una): $(n - k)(n - k + 1)$ operaciones. Con $j = n - k$ recorriendo $1, \dots, n - 1$: $\sum_{j=1}^{n-1} j(j+1) = \sum j^2 + \sum j = \frac{(n-1)n(2n-1)}{6} + \frac{(n-1)n}{2} = \frac{(n-1)n(n+1)}{3} = \frac{n^3 - n}{3}$. $\blacksquare$

</details>

### F16-N5-20 · [D] La reducida conserva las relaciones

**Objetivo**: la reducida conserva las relaciones.
**Dificultad**: N5

**Enunciado.** Si $R = EA$ con $E$ invertible, prueba que $\ker R = \ker A$ y que $\operatorname{Col}(R)$ no tiene por qué ser igual a $\operatorname{Col}(A)$.

<details><summary>Pista 1</summary>Multiplica por $E^{-1}$ para la implicación inversa.</details>
<details><summary>Solución</summary>

$R\mathbf{x} = \mathbf{0} \iff EA\mathbf{x} = \mathbf{0} \iff A\mathbf{x} = \mathbf{0}$ (multiplicando por $E^{-1}$ para la implicación inversa): los núcleos coinciden. Contraejemplo para el espacio columna: $A = \begin{bmatrix} 1&1\\1&1 \end{bmatrix}$ tiene $\operatorname{Col}(A) = \operatorname{gen}\{(1,1)\}$, pero su reducida $R = \begin{bmatrix} 1&1\\0&0 \end{bmatrix}$ tiene $\operatorname{Col}(R) = \operatorname{gen}\{(1,0)\}$. $\blacksquare$

</details>

### F16-N5-21 · [D] Un sistema compatible determinado para un $\mathbf{b}$ lo es para todos

**Objetivo**: un sistema compatible determinado para un $\mathbf{b}$ lo es para todos.
**Dificultad**: N5

**Enunciado.** Sea $A$ cuadrada. Si $A\mathbf{x} = \mathbf{b}_0$ tiene solución única para algún $\mathbf{b}_0$, prueba que $A\mathbf{x} = \mathbf{b}$ tiene solución única para todo $\mathbf{b}$.

<details><summary>Pista 1</summary>Convierte la hipótesis en una afirmación sobre $\ker A$ y usa rango-nulidad.</details>
<details><summary>Solución</summary>

Si $A\mathbf{x} = \mathbf{b}_0$ tiene solución única, por el ejercicio sobre la diferencia de soluciones $\ker A = \{\mathbf{0}\}$, es decir, $\operatorname{nul}(A) = 0$ y por rango-nulidad $\operatorname{rg}(A) = n$. Como $A$ es cuadrada, $\operatorname{rg}(A) = n = m$ y por el ejercicio de existencia hay solución para todo $\mathbf{b}$; es única porque el núcleo es trivial. $\blacksquare$

</details>

### F16-N5-22 · [D] Coeficientes racionales, solución racional

**Objetivo**: coeficientes racionales, solución racional.
**Dificultad**: N5

**Enunciado.** Prueba que un sistema con coeficientes racionales que tiene alguna solución real tiene también una solución racional.

<details><summary>Pista 1</summary>¿Qué números aparecen al hacer eliminación?</details>
<details><summary>Solución</summary>

Al escalonar $[A \mid \mathbf{b}]$ solo se usan sumas, productos y cocientes de racionales, así que la forma reducida tiene entradas racionales y los mismos rangos. Si el sistema es compatible, poniendo las variables libres iguales a $0$ y leyendo las básicas en la última columna de la reducida se obtiene una solución cuyas componentes son racionales. $\blacksquare$

</details>

