# F05 — Matrices y vectores: dimensión, tipos, suma y producto por escalar

Banco de las lecciones L16–L18. **Parte 1: 10 ejercicios**, ligados a los videos. La **parte 2** (40 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F05_matrices_y_vectores_parte2.md`; la familia completa suma **50**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Resultados comprobados en `ejercicios/verificar/f05_f07.py`.

| Lección | Ejercicios |
|---|---|
| L16 Matrices | N1-01 🎬, N1-02 🎬, N2-03 |
| L17 Vectores | N1-03 🎬, N2-01 🎬, N3-01 🎬 |
| L18 Suma y escalar | N1-04 🎬, N2-02 🎬, N4-01, N5-01 |

---

### F05-N1-01 · [K] Dimensión y elementos 🎬

**Objetivo**: leer la dimensión y localizar elementos $b_{ij}$.
**Dificultad**: N1

**Enunciado.** $B = \begin{bmatrix} 3 & -2 & 0 \\ 1 & 7 & -5 \end{bmatrix}$. a) Dimensión de $B$. b) $b_{12}$, $b_{21}$, $b_{23}$. c) ¿Existe $b_{32}$?

<details><summary>Pista 1</summary>Dimensión: primero filas, después columnas.</details>
<details><summary>Pista 2</summary>$b_{ij}$: fila $i$, columna $j$.</details>
<details><summary>Solución</summary>

a) $2\times 3$. b) $b_{12} = -2$, $b_{21} = 1$, $b_{23} = -5$. c) No: $B$ solo tiene 2 filas.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>Decir "$3\times 2$"; leer $b_{12}$ como fila 2, columna 1.</details>

### F05-N1-02 · [K] Tipos de matrices 🎬

**Objetivo**: reconocer tipos (y que una matriz puede tener varios).
**Dificultad**: N1

**Enunciado.** Clasifica $P = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, $Q = \begin{bmatrix} 0 & 0 \\ 4 & 2 \end{bmatrix}$, $R = \begin{bmatrix} 5 & 1 & 0 \end{bmatrix}$, $S = \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}$.

<details><summary>Pista 1</summary>Primero: ¿cuadrada o rectangular? Después mira dónde están los ceros.</details>
<details><summary>Pista 2</summary>Triangular superior: ceros debajo de la diagonal; inferior: encima.</details>
<details><summary>Solución</summary>

- $P$: cuadrada, identidad $I_2$, diagonal, triangular superior e inferior.
- $Q$: cuadrada, triangular inferior ($q_{12} = 0$). No es superior ($q_{21} = 4$).
- $R$: rectangular $1\times 3$ (vector fila).
- $S$: cuadrada, diagonal, triangular superior e inferior (un elemento de la diagonal puede ser 0).

**Verificación**: se comprueba cada condición posición a posición.
</details>
<details><summary>Errores frecuentes</summary>Creer que una diagonal necesita todos los $a_{ii} \neq 0$.</details>

### F05-N2-03 · [C] Igualdad de matrices

**Objetivo**: convertir una igualdad de matrices en ecuaciones.
**Dificultad**: N2

**Enunciado.** Halla $x, y$: $\begin{bmatrix} x + y & 2 \\ 3 & x - y \end{bmatrix} = \begin{bmatrix} 5 & 2 \\ 3 & 1 \end{bmatrix}$.

<details><summary>Pista 1</summary>Iguala posición a posición.</details>
<details><summary>Pista 2</summary>Quedan $x + y = 5$ y $x - y = 1$: reducción (L15).</details>
<details><summary>Solución</summary>

Sumando: $2x = 6$, $x = 3$; $y = 2$.

**Verificación**: $3 + 2 = 5$, $3 - 2 = 1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar que las demás posiciones también deben coincidir (aquí lo hacen).</details>

### F05-N1-03 · [K] Dibujar vectores 🎬

**Objetivo**: representar vectores y conocer su forma como matriz.
**Dificultad**: N1

**Enunciado.** Dibuja $\mathbf{a} = (-2, 3)$, $\mathbf{b} = (4, 0)$, $\mathbf{c} = (0, -3)$ como flechas desde el origen. ¿Qué dimensión tienen como matrices columna? ¿Y $\mathbf{a}^T$?

<details><summary>Pista 1</summary>Primera componente: horizontal; segunda: vertical.</details>
<details><summary>Pista 2</summary>Un vector columna con $n$ componentes es $n\times 1$.</details>
<details><summary>Solución</summary>

$\mathbf{a}$: 2 a la izquierda y 3 arriba. $\mathbf{b}$: sobre el eje $x$ positivo. $\mathbf{c}$: sobre el eje $y$ negativo. Los tres son $2\times 1$; $\mathbf{a}^T = \begin{bmatrix} -2 & 3 \end{bmatrix}$ es $1\times 2$.

**Verificación**: la punta de cada flecha está en el punto de coordenadas del vector.
</details>
<details><summary>Errores frecuentes</summary>Dibujar $\mathbf{c}$ sobre el eje $x$.</details>

### F05-N2-01 · [C] Operaciones con vectores 🎬

**Objetivo**: sumar, escalar y combinar vectores de $\mathbb{R}^3$.
**Dificultad**: N2

**Enunciado.** $\mathbf{u} = (2, -1, 3)$, $\mathbf{v} = (-1, 4, 0)$. Calcula: a) $\mathbf{u} + \mathbf{v}$ b) $3\mathbf{u}$ c) $2\mathbf{u} - 3\mathbf{v}$ d) $\mathbf{u} - \mathbf{u}$.

<details><summary>Pista 1</summary>Componente a componente.</details>
<details><summary>Pista 2</summary>c) $2\mathbf{u} = (4, -2, 6)$ y $3\mathbf{v} = (-3, 12, 0)$.</details>
<details><summary>Solución</summary>

a) $(1, 3, 3)$. b) $(6, -3, 9)$. c) $(7, -14, 6)$. d) $\mathbf{0} = (0, 0, 0)$.

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>c) $4 - (-3) = 1$ (error de signo).</details>

### F05-N3-01 · [C] Combinación lineal con fracciones 🎬

**Objetivo**: hallar los pesos de una combinación lineal resolviendo un sistema.
**Dificultad**: N3

**Enunciado.** Escribe $\mathbf{w} = (1, 8)$ como combinación lineal de $\mathbf{u} = (1, 2)$ y $\mathbf{v} = (3, -1)$.

<details><summary>Pista 1</summary>$a\mathbf{u} + b\mathbf{v} = \mathbf{w}$ da $a + 3b = 1$ y $2a - b = 8$.</details>
<details><summary>Pista 2</summary>De la segunda, $b = 2a - 8$.</details>
<details><summary>Solución</summary>

$a + 3(2a - 8) = 1 \Rightarrow 7a = 25 \Rightarrow a = \frac{25}{7}$; $b = \frac{50}{7} - 8 = -\frac67$. Así $\mathbf{w} = \frac{25}{7}\mathbf{u} - \frac67\mathbf{v}$.

**Verificación**: $\frac{25}{7} - \frac{18}{7} = 1$ ✓; $\frac{50}{7} + \frac67 = 8$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Plantear $a + 2b = 1$ (mezclar las componentes de $\mathbf{u}$ en vez de usar las columnas).</details>

### F05-N1-04 · [C] Suma de matrices 🎬

**Objetivo**: sumar y reconocer cuándo no se puede.
**Dificultad**: N1

**Enunciado.** $A = \begin{bmatrix} 4 & -1 \\ 0 & 2 \\ -3 & 5 \end{bmatrix}$, $B = \begin{bmatrix} -4 & 6 \\ 1 & 1 \\ 3 & -5 \end{bmatrix}$, $C = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$. Calcula $A + B$. ¿Está definida $A + C$?

<details><summary>Pista 1</summary>Compara dimensiones.</details>
<details><summary>Pista 2</summary>$A$ es $3\times 2$ y $C$ es $2\times 3$.</details>
<details><summary>Solución</summary>

$A + B = \begin{bmatrix} 0 & 5 \\ 1 & 3 \\ 0 & 0 \end{bmatrix}$. $A + C$ no está definida (dimensiones distintas).

**Verificación**: comprobado en `verificar/f05_f07.py`.
</details>
<details><summary>Errores frecuentes</summary>"Girar" $C$ para que encaje.</details>

### F05-N2-02 · [C] Ecuación matricial 🎬

**Objetivo**: operar y despejar una matriz.
**Dificultad**: N2

**Enunciado.** $A = \begin{bmatrix} 2 & 0 \\ -1 & 3 \end{bmatrix}$, $B = \begin{bmatrix} 1 & -4 \\ 5 & 2 \end{bmatrix}$. a) $2A - 3B$. b) Halla $X$ con $A + 2X = B$.

<details><summary>Pista 1</summary>b) Se despeja como con números: $X = \frac12(B - A)$ (propiedades de L18).</details>
<details><summary>Pista 2</summary>$B - A = \begin{bmatrix} -1 & -4 \\ 6 & -1 \end{bmatrix}$.</details>
<details><summary>Solución</summary>

a) $\begin{bmatrix} 1 & 12 \\ -17 & 0 \end{bmatrix}$. b) $X = \begin{bmatrix} -\frac12 & -2 \\ 3 & -\frac12 \end{bmatrix}$.

**Verificación**: $A + 2X = \begin{bmatrix} 2 - 1 & 0 - 4 \\ -1 + 6 & 3 - 1 \end{bmatrix} = B$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar multiplicar por $\frac12$ todas las posiciones.</details>

### F05-N4-01 · [K] Encuentra el error

**Objetivo**: detectar errores en las definiciones.
**Dificultad**: N4

**Enunciado.** Corrige: a) "$3\begin{bmatrix} 1 & 2 \\ 0 & 4 \end{bmatrix} = \begin{bmatrix} 3 & 2 \\ 0 & 4 \end{bmatrix}$" b) "$(2A)_{ij} = 2 + a_{ij}$" c) "$\begin{bmatrix} 1 & 2 \end{bmatrix} + \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 4 & 6 \end{bmatrix}$".

<details><summary>Pista 1</summary>El escalar multiplica a todos los elementos.</details>
<details><summary>Pista 2</summary>c) Compara las dimensiones.</details>
<details><summary>Solución</summary>

a) Hay que multiplicar todos: $\begin{bmatrix} 3 & 6 \\ 0 & 12 \end{bmatrix}$. b) $(2A)_{ij} = 2a_{ij}$. c) No está definida: $1\times 2$ y $2\times 1$.

**Verificación**: aplicar las definiciones de L18.
</details>
<details><summary>Errores frecuentes</summary>Los que muestra el ejercicio.</details>

### F05-N5-01 · [D] Una distributiva

**Objetivo**: demostrar una propiedad posición a posición.
**Dificultad**: N5

**Enunciado.** Demuestra que $c(A + B) = cA + cB$ para matrices $A, B$ de la misma dimensión y un número $c$.

<details><summary>Pista 1</summary>Compara el elemento $(i, j)$ de cada lado.</details>
<details><summary>Pista 2</summary>Usa la distributiva de los números reales.</details>
<details><summary>Solución</summary>

$\big(c(A + B)\big)_{ij} = c\,(a_{ij} + b_{ij}) = c\,a_{ij} + c\,b_{ij} = (cA)_{ij} + (cB)_{ij} = (cA + cB)_{ij}$. Las dos matrices tienen la misma dimensión y coinciden en toda posición: son iguales. $\blacksquare$

**Verificación** (ejemplo): $2\left(\begin{bmatrix} 1 \end{bmatrix} + \begin{bmatrix} 3 \end{bmatrix}\right) = 8 = 2 + 6$.
</details>
<details><summary>Errores frecuentes</summary>Demostrarlo con un ejemplo concreto.</details>
