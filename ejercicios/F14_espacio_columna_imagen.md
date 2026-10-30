# F14 — Espacio columna, imagen y teorema del rango y la nulidad

Banco de las lecciones L48–L50. **Parte 1: 14 ejercicios**, ligados a los videos. La **parte 2** (26 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F14_espacio_columna_imagen_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $\operatorname{Col}(A) = \operatorname{gen}\{\text{columnas de } A\} = \{A\mathbf{x}\}$; $\operatorname{Im}(T_A) = \operatorname{Col}(A)$; $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.
- Matrices compartidas: $A = \begin{bmatrix} 1&2&0&1\\2&4&1&4\\1&2&1&3 \end{bmatrix}$, $B_2 = \begin{bmatrix} 1&2\\2&4 \end{bmatrix}$, $B = \begin{bmatrix} 1&1&1\\1&2&3 \end{bmatrix}$, $C = \begin{bmatrix} 1&0\\0&1\\1&1 \end{bmatrix}$.
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f12_f14.py`.

| Lección | Ejercicios |
|---|---|
| L48 Espacio columna e imagen | N1-01 🎬, N1-02, N2-01 🎬, N2-02 🎬 |
| L49 Base del espacio columna | N3-01 🎬, N3-02, N3-03, N3-04 🎬, N4-04 |
| L50 Rango y nulidad | N3-05, N4-01 🎬, N4-02 🎬, N4-03, N5-01 |

---

### F14-N1-01 · [C] $A\mathbf{x}$ como combinación de columnas 🎬

**Objetivo**: leer el producto por columnas.
**Dificultad**: N1

**Enunciado.** Calcula $B_2\mathbf{x}$ con $\mathbf{x} = (3, -1)$ escribiéndolo como combinación lineal de las columnas.

<details><summary>Pista 1</summary>$B_2\mathbf{x} = 3\,\mathbf{a}_1 - 1\,\mathbf{a}_2$.</details>
<details><summary>Solución</summary>$3\begin{bmatrix}1\\2\end{bmatrix} - \begin{bmatrix}2\\4\end{bmatrix} = \begin{bmatrix}1\\2\end{bmatrix}$. Por filas: $(3 - 2,\ 6 - 4) = (1, 2)$: el mismo resultado.</details>

### F14-N1-02 · [K] ¿En qué espacio vive?

**Objetivo**: distinguir $\operatorname{Col}(A) \subset \mathbb{R}^m$ de $\ker A \subset \mathbb{R}^n$.
**Dificultad**: N1

**Enunciado.** Para una matriz $3 \times 4$: ¿en qué $\mathbb{R}^k$ vive $\operatorname{Col}(A)$? ¿Y $\ker A$?

<details><summary>Solución</summary>Las columnas tienen 3 componentes: $\operatorname{Col}(A) \subseteq \mathbb{R}^3$. Las incógnitas son 4: $\ker A \subseteq \mathbb{R}^4$.</details>

### F14-N2-01 · [C] ¿Es alcanzable? (2×2) 🎬

**Objetivo**: decidir $\mathbf{b} \in \operatorname{Col}(A)$.
**Dificultad**: N2

**Enunciado.** Con $B_2$: ¿tiene solución $B_2\mathbf{x} = (3, 6)$? ¿Y $B_2\mathbf{x} = (1, 0)$?

<details><summary>Pista 1</summary>$\operatorname{Col}(B_2)$ es el espacio generado por $(1,2)$.</details>
<details><summary>Solución</summary>$\operatorname{Col}(B_2)$ es la recta $y = 2x$. $(3, 6)$ está en ella: sí (por ejemplo $\mathbf{x} = (3, 0)$). $(1, 0)$ no: el sistema es incompatible (los rangos son 1 y 2).</details>

### F14-N2-02 · [C] ¿Tiene solución $A\mathbf{x} = \mathbf{b}$? 🎬

**Objetivo**: aplicar $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$.
**Dificultad**: N2

**Enunciado.** Con $A$ la matriz $3 \times 4$ compartida, decide si tiene solución para $\mathbf{b}_1 = (1, 3, 2)$ y para $\mathbf{b}_2 = (1, 0, 0)$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$ y mira si hay una fila $[0\ 0\ 0\ 0 \mid c]$ con $c \ne 0$.</details>
<details><summary>Solución</summary>Para $\mathbf{b}_1$: $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}_1] = 2$: compatible; de hecho $\mathbf{b}_1 = \mathbf{a}_1 + \mathbf{a}_3$. Para $\mathbf{b}_2$: $\operatorname{rg}(A) = 2$ pero $\operatorname{rg}[A \mid \mathbf{b}_2] = 3$ (queda la fila $[0\,0\,0\,0 \mid 1]$): incompatible.</details>

### F14-N3-01 · [C] Base de $\operatorname{Col}(A)$ 🎬

**Objetivo**: columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(A)$ y su dimensión, con $A$ la matriz $3\times 4$ compartida.

<details><summary>Pista 1</summary>Pivotes de la reducida en las columnas 1 y 3.</details>
<details><summary>Solución</summary>Base: $\{\mathbf{a}_1, \mathbf{a}_3\} = \{(1,2,1),\ (0,1,1)\}$. $\dim\operatorname{Col}(A) = 2 = \operatorname{rg}(A)$.</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la reducida: $(1,0,0)$ y $(0,1,0)$ no están en $\operatorname{Col}(A)$.</details>

### F14-N3-02 · [C] Expresar las otras columnas

**Objetivo**: leer las relaciones en la reducida.
**Dificultad**: N3

**Enunciado.** Escribe $\mathbf{a}_2$ y $\mathbf{a}_4$ como combinación de la base $\{\mathbf{a}_1, \mathbf{a}_3\}$.

<details><summary>Pista 1</summary>Las columnas 2 y 4 de la reducida son $(2,0,0)$ y $(1,2,0)$.</details>
<details><summary>Solución</summary>$\mathbf{a}_2 = 2\mathbf{a}_1$ y $\mathbf{a}_4 = 1\mathbf{a}_1 + 2\mathbf{a}_3$. Comprobación: $2(1,2,1) = (2,4,2)$ y $(1,2,1) + 2(0,1,1) = (1,4,3)$.</details>

### F14-N3-03 · [C] Espacio columna de una matriz 2×3

**Objetivo**: base y dimensión; reconocer $\operatorname{Col}(B) = \mathbb{R}^2$.
**Dificultad**: N3

**Enunciado.** Halla una base de $\operatorname{Col}(B)$ con $B = \begin{bmatrix} 1&1&1\\1&2&3 \end{bmatrix}$. ¿Qué espacio es?

<details><summary>Pista 1</summary>La reducida es $\begin{bmatrix} 1&0&-1\\0&1&2 \end{bmatrix}$.</details>
<details><summary>Solución</summary>Pivotes en las columnas 1 y 2: base $\{(1,1),\ (1,2)\}$. Dimensión 2 en $\mathbb{R}^2$: $\operatorname{Col}(B) = \mathbb{R}^2$ (el sistema $B\mathbf{x} = \mathbf{b}$ tiene solución para todo $\mathbf{b}$).</details>

### F14-N3-04 · [K] El error del estudiante 🎬

**Objetivo**: entender por qué hay que usar la matriz original.
**Dificultad**: N3

**Enunciado.** Un estudiante toma como base de $\operatorname{Col}(A)$ las columnas pivote de la reducida. Da un ejemplo $2\times 2$ en que eso falla y explica por qué.

<details><summary>Pista 1</summary>Prueba con una matriz de columnas iguales.</details>
<details><summary>Solución</summary>Sea $A = \begin{bmatrix} 1&1\\1&1 \end{bmatrix}$. Su reducida es $\begin{bmatrix} 1&1\\0&0 \end{bmatrix}$ y la primera columna pivote es $(1, 0)$. Pero $\operatorname{Col}(A) = \operatorname{gen}\{(1,1)\}$ y $(1, 0) \notin \operatorname{Col}(A)$. Las operaciones por filas cambian el espacio columna; lo que se conserva son las relaciones entre columnas, por eso hay que tomar las columnas pivote de $A$: $\{(1,1)\}$.</details>

### F14-N3-05 · [C] Imagen y núcleo de una transformación

**Objetivo**: ver imagen y núcleo en el plano.
**Dificultad**: N3

**Enunciado.** Para $T(\mathbf{x}) = B_2\mathbf{x}$ ($T:\mathbb{R}^2\to\mathbb{R}^2$), describe la imagen y el núcleo y comprueba que $\operatorname{rg} + \operatorname{nul} = 2$.

<details><summary>Solución</summary>Imagen: $\operatorname{Col}(B_2) = \operatorname{gen}\{(1,2)\}$, la recta $y = 2x$ (dimensión 1). Núcleo: $\operatorname{gen}\{(-2,1)\}$, la recta $x_1 + 2x_2 = 0$ (dimensión 1). $1 + 1 = 2$. La transformación aplasta la segunda recta al origen y todo el plano sobre la primera.</details>

### F14-N4-01 · [C] Verificar rango + nulidad 🎬

**Objetivo**: comprobar el teorema en ejemplos.
**Dificultad**: N4

**Enunciado.** Calcula rango y nulidad de $B$ y de $C$, y comprueba que suman $n$. Haz lo mismo con $A$.

<details><summary>Pista 1</summary>Nulidad = número de variables libres; rango = número de pivotes.</details>
<details><summary>Solución</summary>$B$ ($n=3$): rango 2, nulidad 1; $2+1 = 3$. $C$ ($n=2$): rango 2, nulidad 0; $2+0 = 2$. $A$ ($n=4$): rango 2, nulidad 2; $2+2 = 4$.</details>

### F14-N4-02 · [C] Datos mínimos 🎬

**Objetivo**: usar el teorema sin calcular.
**Dificultad**: N4

**Enunciado.** Una matriz $5 \times 7$ tiene rango 3. ¿Cuál es su nulidad? ¿En qué $\mathbb{R}^k$ vive $\operatorname{Col}(A)$ y qué dimensión tiene?

<details><summary>Solución</summary>$\operatorname{nul} = 7 - 3 = 4$. $\operatorname{Col}(A) \subseteq \mathbb{R}^5$ con dimensión $3$ (un subespacio de dimensión 3 dentro de $\mathbb{R}^5$); $\ker A \subseteq \mathbb{R}^7$ con dimensión 4.</details>

### F14-N4-03 · [K] Matrices imposibles

**Objetivo**: usar rango-nulidad para descartar existencia.
**Dificultad**: N4

**Enunciado.** a) ¿Puede una matriz $3\times 5$ tener $\ker A = \{\mathbf{0}\}$? b) ¿Puede una matriz $5\times 3$ cumplir que $A\mathbf{x} = \mathbf{b}$ tenga solución para todo $\mathbf{b} \in \mathbb{R}^5$?

<details><summary>Solución</summary>a) No: $\operatorname{rg} \le 3$, luego $\operatorname{nul} = 5 - \operatorname{rg} \ge 2 > 0$. b) No: haría falta $\operatorname{Col}(A) = \mathbb{R}^5$, es decir $\operatorname{rg} = 5$, pero $\operatorname{rg} \le 3$.</details>

### F14-N4-04 · [D] Las columnas pivote son una base

**Objetivo**: demostrar la receta de la L49.
**Dificultad**: N4

**Enunciado.** Sea $R$ la reducida de $A$. Prueba que las columnas de $A$ correspondientes a los pivotes de $R$ son una base de $\operatorname{Col}(A)$.

<details><summary>Pista 1</summary>$A\mathbf{x} = \mathbf{0} \iff R\mathbf{x} = \mathbf{0}$: $A$ y $R$ tienen las mismas relaciones entre columnas.</details>
<details><summary>Pista 2</summary>En $R$ las columnas pivote son $\mathbf{e}_1, \dots, \mathbf{e}_r$.</details>
<details><summary>Solución</summary>En $R$, las columnas pivote son $\mathbf{e}_1,\dots,\mathbf{e}_r$ (independientes), y cada columna libre es combinación de ellas. Como una combinación $\sum x_j\mathbf{a}_j = \mathbf{0}$ de columnas de $A$ vale exactamente cuando $\sum x_j\mathbf{r}_j = \mathbf{0}$, las mismas relaciones valen en $A$: sus columnas pivote son independientes y cada columna libre es combinación de ellas. Luego generan $\operatorname{Col}(A)$ y son una base. $\blacksquare$</details>

### F14-N5-01 · [D] Teorema del rango y la nulidad

**Objetivo**: demostrar $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.
**Dificultad**: N5

**Enunciado.** Demuestra que para toda matriz $A$ de tamaño $m\times n$: $\dim\operatorname{Col}(A) + \dim\ker A = n$.

<details><summary>Pista 1</summary>Cuenta las columnas con pivote y las columnas libres.</details>
<details><summary>Solución</summary>Sea $r$ el número de pivotes. Hay $r$ columnas con pivote y $n - r$ sin él (variables libres). Por el ejercicio N4-04, $\dim\operatorname{Col}(A) = r$. Cada variable libre aporta un vector a una base de $\ker A$ (L46), así que $\dim\ker A = n - r$. Sumando: $r + (n - r) = n$. $\blacksquare$</details>
