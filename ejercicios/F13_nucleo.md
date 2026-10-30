# F13 — El núcleo de una matriz

Banco de las lecciones L45–L47. **Parte 1: 13 ejercicios**, ligados a los videos. La **parte 2** (27 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F13_nucleo_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $\ker A = \{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$; $\operatorname{nul}(A) = \dim\ker A$; $n$ es el número de columnas.
- Matrices compartidas: $A = \begin{bmatrix} 1&2&0&1\\2&4&1&4\\1&2&1&3 \end{bmatrix}$ (reducida $\begin{bmatrix} 1&2&0&1\\0&0&1&2\\0&0&0&0 \end{bmatrix}$), $B_2 = \begin{bmatrix} 1&2\\2&4 \end{bmatrix}$.
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f12_f14.py`.

| Lección | Ejercicios |
|---|---|
| L45 El núcleo | N1-01, N1-02, N2-01 🎬, N2-02 🎬, N4-03 |
| L46 Base y nulidad | N3-01 🎬, N3-02 🎬, N3-03, N3-04 🎬 |
| L47 Estructura de las soluciones | N3-05 🎬, N4-01 🎬, N4-02, N5-01 |

---

### F13-N1-01 · [C] ¿Está en el núcleo?

**Objetivo**: comprobar pertenencia multiplicando.
**Dificultad**: N1

**Enunciado.** Con $B_2 = \begin{bmatrix} 1&2\\2&4 \end{bmatrix}$, ¿están $(-2, 1)$ y $(1, 1)$ en $\ker B_2$?

<details><summary>Pista 1</summary>Calcula $B_2\mathbf{x}$ y mira si sale $\mathbf{0}$.</details>
<details><summary>Solución</summary>$B_2(-2,1) = (-2+2,\ -4+4) = (0, 0)$: sí. $B_2(1,1) = (3, 6) \ne \mathbf{0}$: no.</details>
<details><summary>Errores frecuentes</summary>Mirar solo la primera componente.</details>

### F13-N1-02 · [K] Vector nulo y espacio nulo

**Objetivo**: distinguir los dos conceptos.
**Dificultad**: N1

**Enunciado.** ¿Puede el núcleo de una matriz ser el conjunto vacío? Si $A$ es $m \times n$, ¿de qué espacio $\mathbb{R}^k$ es subconjunto $\ker A$?

<details><summary>Solución</summary>No: $A\mathbf{0} = \mathbf{0}$, así que $\mathbf{0} \in \ker A$ siempre. Es subconjunto de $\mathbb{R}^n$ (el espacio de las incógnitas), no de $\mathbb{R}^m$.</details>
<details><summary>Errores frecuentes</summary>Confundir $\ker A$ con $\operatorname{Col}(A)$, que vive en $\mathbb{R}^m$.</details>

### F13-N2-01 · [C] Núcleo de una matriz 2×2 🎬

**Objetivo**: resolver $A\mathbf{x} = \mathbf{0}$ y describir el conjunto.
**Dificultad**: N2

**Enunciado.** Halla $\ker B_2$ y descríbelo geométricamente. ¿Cuál es su dimensión?

<details><summary>Pista 1</summary>Las dos ecuaciones son proporcionales.</details>
<details><summary>Solución</summary>Queda $x_1 + 2x_2 = 0$: $x_1 = -2t$, $x_2 = t$. $\ker B_2 = \operatorname{gen}\{(-2, 1)\}$: la recta $x_1 + 2x_2 = 0$ por el origen. Dimensión 1.</details>

### F13-N2-02 · [C] Pertenencia en $\mathbb{R}^4$ 🎬

**Objetivo**: comprobar pertenencia con una matriz $3 \times 4$.
**Dificultad**: N2

**Enunciado.** Con $A$ la matriz compartida, ¿cuáles están en $\ker A$: $\mathbf{a} = (1,0,0,1)$, $\mathbf{b} = (-3, 1, -2, 1)$?

<details><summary>Pista 1</summary>Multiplica $A$ por cada vector y mira las tres componentes.</details>
<details><summary>Solución</summary>$A\mathbf{a} = (1+1,\ 2+4,\ 1+3) = (2, 6, 4) \ne \mathbf{0}$: no. $A\mathbf{b} = (-3+2+1,\ -6+4-2+4,\ -3+2-2+3) = (0, 0, 0)$: sí.</details>

### F13-N3-01 · [C] Base del núcleo 🎬

**Objetivo**: aplicar la receta de las variables libres.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker A$ y su dimensión, con $A$ la matriz compartida.

<details><summary>Pista 1</summary>Pivotes en las columnas 1 y 3; libres $x_2$ y $x_4$.</details>
<details><summary>Pista 2</summary>$x_1 = -2x_2 - x_4$, $\;x_3 = -2x_4$.</details>
<details><summary>Solución</summary>Con $x_2 = s$, $x_4 = t$: $\mathbf{x} = s(-2, 1, 0, 0) + t(-1, 0, -2, 1)$. Base: $\{(-2,1,0,0),\ (-1,0,-2,1)\}$; $\operatorname{nul}(A) = 2$.</details>
<details><summary>Errores frecuentes</summary>Dar como base un vector con las libres distintas de $(1,0)$ y $(0,1)$ sin comprobar independencia; o escribir mal los signos al despejar.</details>

### F13-N3-02 · [C] Núcleo de una matriz 2×3 🎬

**Objetivo**: base del núcleo con una sola variable libre.
**Dificultad**: N3

**Enunciado.** Halla una base de $\ker B$ y su dimensión, con $B = \begin{bmatrix} 1&1&1\\1&2&3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Resta la fila 1 de la fila 2 y luego reduce hacia arriba.</details>
<details><summary>Solución</summary>La reducida es $\begin{bmatrix} 1&0&-1\\0&1&2 \end{bmatrix}$: $x_3 = t$ libre, $x_1 = t$, $x_2 = -2t$. Base: $\{(1, -2, 1)\}$; $\operatorname{nul}(B) = 1$. Comprobación: $B(1,-2,1) = (1-2+1,\ 1-4+3) = (0,0)$.</details>

### F13-N3-03 · [C] Núcleo trivial

**Objetivo**: reconocer cuándo no hay variables libres.
**Dificultad**: N3

**Enunciado.** Halla $\ker C$ con $C = \begin{bmatrix} 1&0\\0&1\\1&1 \end{bmatrix}$.

<details><summary>Pista 1</summary>¿Tiene cada columna un pivote?</details>
<details><summary>Solución</summary>Rango 2 = número de columnas: no hay variables libres. $\ker C = \{\mathbf{0}\}$ y $\operatorname{nul}(C) = 0$ (base vacía).</details>

### F13-N3-04 · [K] Nulidad y forma de la matriz 🎬

**Objetivo**: acotar la nulidad sin calcular.
**Dificultad**: N3

**Enunciado.** Una matriz tiene 2 filas y 5 columnas. ¿Qué puedes decir de su rango y de su nulidad?

<details><summary>Pista 1</summary>El rango no supera el número de filas; la nulidad es $n - \operatorname{rg}$.</details>
<details><summary>Solución</summary>$\operatorname{rg} \le 2$, luego $\operatorname{nul} = 5 - \operatorname{rg} \ge 3$. En particular, $A\mathbf{x} = \mathbf{0}$ siempre tiene soluciones no triviales (infinitas).</details>

### F13-N3-05 · [C] Solución general de un sistema 🎬

**Objetivo**: escribir $\mathbf{x} = \mathbf{x}_p + s\mathbf{n}_1 + t\mathbf{n}_2$.
**Dificultad**: N3

**Enunciado.** Resuelve $A\mathbf{x} = \mathbf{b}$ con $A$ la matriz compartida y $\mathbf{b} = (1, 3, 2)$.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$; la última fila queda de ceros.</details>
<details><summary>Pista 2</summary>Una solución particular: pon las libres a $0$.</details>
<details><summary>Solución</summary>La reducida de $[A \mid \mathbf{b}]$ es $\begin{bmatrix} 1&2&0&1&1\\0&0&1&2&1\\0&0&0&0&0 \end{bmatrix}$: $x_1 = 1 - 2s - t$, $x_3 = 1 - 2t$. Entonces $\mathbf{x} = (1,0,1,0) + s(-2,1,0,0) + t(-1,0,-2,1)$, con $s, t$ cualesquiera. Es un sistema compatible indeterminado (rango $2 < 4$).</details>
<details><summary>Errores frecuentes</summary>Olvidar el término $\mathbf{x}_p$ y dar solo el núcleo (eso resuelve $A\mathbf{x} = \mathbf{0}$, no $A\mathbf{x} = \mathbf{b}$).</details>

### F13-N4-01 · [C] La recta trasladada 🎬

**Objetivo**: ver el conjunto solución como núcleo trasladado.
**Dificultad**: N4

**Enunciado.** Resuelve $\begin{cases} x + 2y = 3 \\ 2x + 4y = 6 \end{cases}$. Indica una solución particular, el núcleo y tres soluciones.

<details><summary>Pista 1</summary>La segunda ecuación es el doble de la primera.</details>
<details><summary>Solución</summary>Solución particular $\mathbf{x}_p = (3, 0)$; $\ker = \operatorname{gen}\{(-2, 1)\}$. Soluciones: $(3,0) + t(-2,1)$: por ejemplo $(3,0)$, $(1,1)$ ($t=1$) y $(5,-1)$ ($t=-1$). El conjunto solución es la recta $x + 2y = 3$, paralela a $\ker$ y desplazada hasta $(3, 0)$.</details>

### F13-N4-02 · [C] Diferencia de soluciones

**Objetivo**: comprobar que la diferencia de dos soluciones está en el núcleo.
**Dificultad**: N4

**Enunciado.** Comprueba que $\mathbf{x}_1 = (1, 0, 1, 0)$ y $\mathbf{x}_2 = (-1, 1, 1, 0)$ son soluciones de $A\mathbf{x} = (1, 3, 2)$, y que $\mathbf{x}_1 - \mathbf{x}_2 \in \ker A$.

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}_1$, $A\mathbf{x}_2$ y $A(\mathbf{x}_1 - \mathbf{x}_2)$.</details>
<details><summary>Solución</summary>$A\mathbf{x}_1 = (1,\ 2+1,\ 1+1) = (1,3,2)$ y $A\mathbf{x}_2 = (-1+2,\ -2+4+1,\ -1+2+1) = (1,3,2)$. La diferencia es $(2, -1, 0, 0) = -\mathbf{n}_1$, y está en el núcleo.</details>

### F13-N4-03 · [D] El núcleo es un subespacio

**Objetivo**: demostrar la cerradura.
**Dificultad**: N4

**Enunciado.** Prueba que si $\mathbf{x}, \mathbf{y} \in \ker A$ y $c \in \mathbb{R}$, entonces $\mathbf{x} + \mathbf{y} \in \ker A$ y $c\mathbf{x} \in \ker A$.

<details><summary>Solución</summary>$A(\mathbf{x} + \mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}$ y $A(c\mathbf{x}) = c\,A\mathbf{x} = c\,\mathbf{0} = \mathbf{0}$. Además $\mathbf{0} \in \ker A$. $\blacksquare$</details>

### F13-N5-01 · [D] Estructura de las soluciones

**Objetivo**: demostrar el teorema de la L47.
**Dificultad**: N5

**Enunciado.** Sea $A\mathbf{x}_p = \mathbf{b}$. Prueba que $A\mathbf{x} = \mathbf{b}$ si y solo si $\mathbf{x} - \mathbf{x}_p \in \ker A$.

<details><summary>Pista 1</summary>Usa la linealidad: $A(\mathbf{x} - \mathbf{x}_p) = A\mathbf{x} - A\mathbf{x}_p$.</details>
<details><summary>Solución</summary>($\Rightarrow$) Si $A\mathbf{x} = \mathbf{b}$: $A(\mathbf{x} - \mathbf{x}_p) = \mathbf{b} - \mathbf{b} = \mathbf{0}$. ($\Leftarrow$) Si $A(\mathbf{x} - \mathbf{x}_p) = \mathbf{0}$: $A\mathbf{x} = A\mathbf{x}_p = \mathbf{b}$. Luego las soluciones son exactamente los $\mathbf{x}_p + \mathbf{n}$ con $\mathbf{n} \in \ker A$. $\blacksquare$</details>
