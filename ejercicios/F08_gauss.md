# F08 — Eliminación de Gauss

Banco de las lecciones L24–L30. **Parte 1: 22 ejercicios**, ligados a los videos. La **parte 2** (28 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F08_gauss_parte2.md`; la familia completa suma **50**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $R_i$ es la fila $i$; $R_2 \leftarrow R_2 - 3R_1$ significa "la fila 2 se sustituye por ella menos 3 veces la fila 1".
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f08.py`.

| Lección | Ejercicios |
|---|---|
| L24 Operaciones elementales | N1-01 🎬, N2-01 🎬, N4-01, N5-01, N5-02 |
| L25 Forma escalonada | N1-02 🎬, N2-02 🎬 |
| L26 Hacia adelante y hacia atrás | N2-03 🎬, N2-04 🎬, N3-01 |
| L27 Pivotes nulos y filas nulas | N2-05 🎬, N3-02 🎬 |
| L28 Sin solución e infinitas | N2-06 🎬, N3-03 🎬, N4-02, N5-03 |
| L29 Parámetros | N4-03 🎬, N4-04 🎬, N4-05 |
| L30 Errores y verificación | N3-04 🎬, N4-06, N4-07 🎬 |

---

### F08-N1-01 · [C] Aplicar operaciones elementales 🎬

**Objetivo**: aplicar cada operación a la fila entera, columna de $\mathbf{b}$ incluida.
**Dificultad**: N1

**Enunciado.** Sea $M = \left[\begin{array}{cc|c} 2 & -1 & 3 \\ 1 & 4 & 6 \end{array}\right]$. Aplica a $M$, cada una por separado: a) $R_1 \leftrightarrow R_2$; b) $R_2 \leftarrow 3R_2$; c) $R_2 \leftarrow R_2 - 2R_1$. Comprueba que $(2, 1)$ es solución de los cuatro sistemas.

<details><summary>Pista 1</summary>Solo cambia la fila destino; en c) la fila 1 se copia igual.</details>
<details><summary>Pista 2</summary>c) $[\,1 \ \ 4 \mid 6\,] - 2\,[\,2 \ \ -1 \mid 3\,]$.</details>
<details><summary>Solución</summary>

a) $\left[\begin{array}{cc|c} 1 & 4 & 6 \\ 2 & -1 & 3 \end{array}\right]$ · b) $\left[\begin{array}{cc|c} 2 & -1 & 3 \\ 3 & 12 & 18 \end{array}\right]$ · c) $\left[\begin{array}{cc|c} 2 & -1 & 3 \\ -3 & 6 & 0 \end{array}\right]$.

**Verificación**: en $M$: $4 - 1 = 3$, $2 + 4 = 6$; b) $6 + 12 = 18$; c) $-6 + 6 = 0$ ✓ (a) son las mismas ecuaciones en otro orden).
</details>
<details><summary>Errores frecuentes</summary>Olvidar la última columna ($R_2 \leftarrow 3R_2$ con $6$ en lugar de $18$); en c) cambiar también $R_1$.</details>

### F08-N2-01 · [C] Deshacer una operación 🎬

**Objetivo**: usar la operación inversa.
**Dificultad**: N2

**Enunciado.** $N = \left[\begin{array}{cc|c} 1 & 3 & 2 \\ 0 & -5 & 1 \end{array}\right]$ se obtuvo de una matriz $M$ con $R_2 \leftarrow R_2 - 2R_1$. a) Encuentra $M$. b) Resuelve $N$ y comprueba la solución en $M$.

<details><summary>Pista 1</summary>La inversa de $R_2 \leftarrow R_2 - 2R_1$ es $R_2 \leftarrow R_2 + 2R_1$ (la fila 1 no cambió).</details>
<details><summary>Pista 2</summary>b) De la segunda fila, $-5y = 1$.</details>
<details><summary>Solución</summary>

a) $M = \left[\begin{array}{cc|c} 1 & 3 & 2 \\ 2 & 1 & 5 \end{array}\right]$. b) $y = -\tfrac{1}{5}$, $x = 2 - 3y = \tfrac{13}{5}$.

**Verificación** en $M$: $\tfrac{13}{5} - \tfrac{3}{5} = 2$ ✓; $\tfrac{26}{5} - \tfrac{1}{5} = 5$ ✓. Y $R_2 - 2R_1$ sobre $M$ devuelve $N$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Usar $R_2 \leftarrow R_2 - 2R_1$ otra vez, o restar la fila 1 de $N$ multiplicada por $-2$ con el signo cambiado.</details>

### F08-N4-01 · [K] ¿Elemental o no?

**Objetivo**: reconocer qué transformaciones conservan el conjunto solución.
**Dificultad**: N4

**Enunciado.** Para cada transformación de un sistema de dos ecuaciones, di si es una operación elemental, una composición de operaciones elementales o ninguna de las dos, y si conserva siempre las soluciones: a) $R_2 \leftarrow R_2 - 5R_1$; b) $R_1 \leftarrow 0\cdot R_1$; c) $R_2 \leftarrow 2R_2 + R_1$; d) sumar 1 a cada entrada de $R_1$; e) $R_2 \leftarrow R_2 - R_2$.

<details><summary>Pista 1</summary>Solo hay tres operaciones: intercambio, escalar por $k \neq 0$ y sumar $k$ veces <em>otra</em> fila.</details>
<details><summary>Pista 2</summary>c) Escala primero por 2 y después suma $R_1$.</details>
<details><summary>Solución</summary>

a) Elemental: conserva. b) No (escalar por 0): puede añadir soluciones. c) Composición de $R_2 \leftarrow 2R_2$ (con $2 \neq 0$) y $R_2 \leftarrow R_2 + R_1$: conserva. d) No: con $M$ de F08-N1-01, $[\,2 \ \ -1 \mid 3\,]$ pasa a $3x + 0y = 4$, que $(2, 1)$ no cumple. e) No: es $0\cdot R_2$.

**Verificación**: comprobado en `verificar/f08.py` con la matriz de F08-N1-01.
</details>
<details><summary>Errores frecuentes</summary>Rechazar c) por no tener la forma exacta $R_i + kR_j$; aceptar e) porque "es restar una fila".</details>

### F08-N5-01 · [D] El intercambio no hace falta

**Objetivo**: entender la relación entre las tres operaciones.
**Dificultad**: N5

**Enunciado.** Demuestra que el intercambio $R_1 \leftrightarrow R_2$ se puede conseguir con tres reemplazos y un escalado: $R_1 \leftarrow R_1 + R_2$, $R_2 \leftarrow R_2 - R_1$, $R_1 \leftarrow R_1 + R_2$, $R_2 \leftarrow -R_2$.

<details><summary>Pista 1</summary>Llama $a$ y $b$ a las filas iniciales y sigue cada paso.</details>
<details><summary>Pista 2</summary>Tras el segundo paso, la fila 2 es $-a$.</details>
<details><summary>Solución</summary>

$(a, b) \to (a + b,\ b) \to (a + b,\ b - (a + b)) = (a + b,\ -a) \to (a + b - a,\ -a) = (b,\ -a) \to (b,\ a)$. $\blacksquare$

**Verificación**: con las filas $(1, 2, 3)$ y $(4, 5, 6)$ el resultado es el intercambio (en `verificar/f08.py`).
</details>
<details><summary>Errores frecuentes</summary>Usar en el segundo paso la fila 1 original en lugar de $a + b$.</details>

### F08-N5-02 · [D] Una operación combinada

**Objetivo**: demostrar que una transformación conserva el conjunto solución.
**Dificultad**: N5

**Enunciado.** Sean $i \neq j$ y $\alpha, \beta$ números. a) Demuestra que $R_i \leftarrow \alpha R_i + \beta R_j$ con $\alpha \neq 0$ da un sistema equivalente. b) Muestra con un ejemplo que con $\alpha = 0$ puede no serlo.

<details><summary>Pista 1</summary>a) Es la composición de dos operaciones elementales.</details>
<details><summary>Pista 2</summary>b) Prueba $R_2 \leftarrow 0\cdot R_2 + R_1$ en $x + y = 2$, $x - y = 0$.</details>
<details><summary>Solución</summary>

a) Es $R_i \leftarrow \alpha R_i$ (elemental porque $\alpha \neq 0$) seguida de $R_i \leftarrow R_i + \beta R_j$ (elemental porque $i \neq j$); cada una conserva el conjunto solución (L24), luego la composición también. $\blacksquare$
b) $x + y = 2$, $x - y = 0$ tiene solución única $(1, 1)$; tras $R_2 \leftarrow R_1$ queda $x + y = 2$ dos veces: infinitas soluciones, por ejemplo $(2, 0)$, que no cumplía $x - y = 0$.

**Verificación**: SCD frente a SCI con 1 libre (en `verificar/f08.py`).
</details>
<details><summary>Errores frecuentes</summary>Demostrar solo que las soluciones viejas cumplen el sistema nuevo (falta la inversa).</details>

### F08-N1-02 · [K] Reconocer la forma escalonada 🎬

**Objetivo**: aplicar la definición de forma escalonada y localizar pivotes.
**Dificultad**: N1

**Enunciado.** ¿Cuáles están en forma escalonada? En ellas, marca los pivotes y las columnas pivote.
a) $\begin{bmatrix} 3 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{bmatrix}$ b) $\begin{bmatrix} 1 & 2 \\ 0 & 0 \\ 0 & 5 \end{bmatrix}$ c) $\begin{bmatrix} 0 & 4 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ d) $\begin{bmatrix} 1 & 0 & 2 \\ 1 & 3 & 0 \\ 0 & 0 & 4 \end{bmatrix}$

<details><summary>Pista 1</summary>Mira dos cosas: filas nulas abajo, y cada pivote a la derecha del de arriba.</details>
<details><summary>Pista 2</summary>En d), ¿qué hay debajo del primer 1?</details>
<details><summary>Solución</summary>

a) Sí: pivotes $3$ (columna 1) y $2$ (columna 3). b) No: la fila nula está encima de una no nula. c) Sí: pivote $4$ (columna 2); puede empezar con una columna de ceros. d) No: el primer elemento no nulo de la fila 2 está en la misma columna que el de la fila 1.

**Verificación**: función `es_escalonada` en `verificar/f08.py`.
</details>
<details><summary>Errores frecuentes</summary>Exigir pivotes iguales a 1; rechazar a) porque la escalera salta una columna.</details>

### F08-N2-02 · [C] Dos escalonadas distintas 🎬

**Objetivo**: ver que la forma escalonada no es única pero sus pivotes y soluciones sí.
**Dificultad**: N2

**Enunciado.** $M = \left[\begin{array}{cc|c} 2 & 6 & 4 \\ 1 & 4 & 3 \end{array}\right]$. Llévala a forma escalonada por dos caminos: a) $R_2 \leftarrow R_2 - \tfrac12 R_1$; b) $R_1 \leftrightarrow R_2$ y luego $R_2 \leftarrow R_2 - 2R_1$. Compara pivotes y soluciones.

<details><summary>Pista 1</summary>a) $[\,1 \ \ 4 \mid 3\,] - \tfrac12 [\,2 \ \ 6 \mid 4\,]$.</details>
<details><summary>Pista 2</summary>b) Tras el intercambio el pivote es el 1.</details>
<details><summary>Solución</summary>

a) $\left[\begin{array}{cc|c} 2 & 6 & 4 \\ 0 & 1 & 1 \end{array}\right]$; b) $\left[\begin{array}{cc|c} 1 & 4 & 3 \\ 0 & -2 & -2 \end{array}\right]$. Matrices distintas, pivotes en las columnas 1 y 2 en las dos. Solución: $y = 1$, $x = -1$ en ambos casos.

**Verificación** en $M$: $-2 + 6 = 4$ ✓; $-1 + 4 = 3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Pensar que una de las dos está mal porque no coinciden.</details>

### F08-N2-03 · [C] Gauss 2 × 2 🎬

**Objetivo**: aplicar eliminación hacia adelante y sustitución hacia atrás.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss, escribiendo cada operación, y verifica: $3x + 2y = 7$, $6x - y = 4$.

<details><summary>Pista 1</summary>Multiplicador: $m = 6/3 = 2$.</details>
<details><summary>Pista 2</summary>$R_2 \leftarrow R_2 - 2R_1$ da $[\,0 \ \ -5 \mid -10\,]$.</details>
<details><summary>Solución</summary>

$\left[\begin{array}{cc|c} 3 & 2 & 7 \\ 6 & -1 & 4 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{cc|c} 3 & 2 & 7 \\ 0 & -5 & -10 \end{array}\right]$: $y = 2$, $3x + 4 = 7 \Rightarrow x = 1$.

**Verificación**: $3 + 4 = 7$ ✓; $6 - 2 = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$-1 - 2\cdot 2 = -3$ (signo); $4 - 14 = -10$ bien, pero olvidar restar en la última columna.</details>

### F08-N2-04 · [C] Gauss 3 × 3 🎬

**Objetivo**: eliminar columna a columna en un sistema 3 × 3.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss y verifica: $x + y + 2z = 3$, $2x + 3y + z = 2$, $-x + 2y + 3z = -1$.

<details><summary>Pista 1</summary>Columna 1: $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 + R_1$.</details>
<details><summary>Pista 2</summary>Columna 2: el pivote es el 1 de la fila 2 nueva; $R_3 \leftarrow R_3 - 3R_2$.</details>
<details><summary>Solución</summary>

$\left[\begin{array}{ccc|c} 1 & 1 & 2 & 3 \\ 0 & 1 & -3 & -4 \\ 0 & 3 & 5 & 2 \end{array}\right] \to \left[\begin{array}{ccc|c} 1 & 1 & 2 & 3 \\ 0 & 1 & -3 & -4 \\ 0 & 0 & 14 & 14 \end{array}\right]$: $z = 1$, $y = -4 + 3 = -1$, $x = 3 + 1 - 2 = 2$.

**Verificación**: $2 - 1 + 2 = 3$; $4 - 3 + 1 = 2$; $-2 - 2 + 3 = -1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Usar la fila 2 original como pivote de la columna 2.</details>

### F08-N3-01 · [C] Elegir el pivote para evitar fracciones

**Objetivo**: decidir un intercambio que simplifica las cuentas.
**Dificultad**: N3

**Enunciado.** Resuelve $2x + y + z = 3$, $x - y + 2z = 3$, $3x + z = 2$. ¿Qué intercambio conviene hacer primero y por qué?

<details><summary>Pista 1</summary>Con pivote 2, los multiplicadores serían $\tfrac12$ y $\tfrac32$.</details>
<details><summary>Pista 2</summary>$R_1 \leftrightarrow R_2$ pone un 1 de pivote.</details>
<details><summary>Solución</summary>

$R_1 \leftrightarrow R_2$; luego $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 3R_1$: filas $[\,0 \ \ 3 \ \ -3 \mid -3\,]$ y $[\,0 \ \ 3 \ \ -5 \mid -7\,]$; $R_3 \leftarrow R_3 - R_2$: $[\,0 \ \ 0 \ \ -2 \mid -4\,]$. Así $z = 2$, $3y - 6 = -3 \Rightarrow y = 1$, $x = 3 + 1 - 4 = 0$.

**Verificación**: $0 + 1 + 2 = 3$; $0 - 1 + 4 = 3$; $0 + 2 = 2$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Creer que con pivote 2 el resultado sería otro (solo cambia la comodidad).</details>

### F08-N2-05 · [C] Un pivote nulo a mitad de camino 🎬

**Objetivo**: detectar un pivote 0 y resolverlo con un intercambio.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss y verifica: $\left[\begin{array}{ccc|c} 1 & 2 & 1 & 4 \\ 2 & 4 & 3 & 9 \\ 1 & 3 & 2 & 6 \end{array}\right]$.

<details><summary>Pista 1</summary>Tras anular la columna 1, la posición (2, 2) vale 0.</details>
<details><summary>Pista 2</summary>$R_2 \leftrightarrow R_3$.</details>
<details><summary>Solución</summary>

$R_2 \leftarrow R_2 - 2R_1$: $[\,0 \ \ 0 \ \ 1 \mid 1\,]$; $R_3 \leftarrow R_3 - R_1$: $[\,0 \ \ 1 \ \ 1 \mid 2\,]$; $R_2 \leftrightarrow R_3$ deja la matriz escalonada. $z = 1$, $y = 2 - 1 = 1$, $x = 4 - 2 - 1 = 1$.

**Verificación**: $1 + 2 + 1 = 4$; $2 + 4 + 3 = 9$; $1 + 3 + 2 = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Concluir "no tiene solución" al ver el 0; intercambiar con la fila 1.</details>

### F08-N3-02 · [C] Una ecuación redundante 🎬

**Objetivo**: interpretar una fila nula y encontrar la relación entre ecuaciones.
**Dificultad**: N3

**Enunciado.** Resuelve por Gauss $x + 2y = 4$, $2x - y = 3$, $4x + 3y = 11$. ¿Qué ecuación es combinación de las otras? Escribe la relación.

<details><summary>Pista 1</summary>$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 4R_1$.</details>
<details><summary>Pista 2</summary>Sigue la pista de la fila 3: $(R_3 - 4R_1) - (R_2 - 2R_1)$.</details>
<details><summary>Solución</summary>

Filas: $[\,0 \ \ -5 \mid -5\,]$ y $[\,0 \ \ -5 \mid -5\,]$; $R_3 \leftarrow R_3 - R_2$ da $[\,0 \ \ 0 \mid 0\,]$. Solución única: $y = 1$, $x = 2$. Como $R_3 - 2R_1 - R_2 = \mathbf{0}$, $E_3 = 2E_1 + E_2$: $2(x + 2y) + (2x - y) = 4x + 3y$ y $2\cdot 4 + 3 = 11$.

**Verificación**: $2 + 2 = 4$; $4 - 1 = 3$; $8 + 3 = 11$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Leer la fila nula como "sin solución" o como "infinitas soluciones" sin contar pivotes.</details>

### F08-N2-06 · [C] Fila contradictoria 🎬

**Objetivo**: detectar un sistema incompatible y dar la combinación que lo prueba.
**Dificultad**: N2

**Enunciado.** Aplica Gauss y clasifica $x + 2y - z = 1$, $2x + 3y + z = 4$, $3x + 5y = 6$. Encuentra la combinación de ecuaciones que da $0 = c$.

<details><summary>Pista 1</summary>Tras la columna 1, las filas 2 y 3 tienen los mismos coeficientes.</details>
<details><summary>Pista 2</summary>La tercera ecuación se parece mucho a $E_1 + E_2$.</details>
<details><summary>Solución</summary>

$R_2 \leftarrow R_2 - 2R_1$: $[\,0 \ \ -1 \ \ 3 \mid 2\,]$; $R_3 \leftarrow R_3 - 3R_1$: $[\,0 \ \ -1 \ \ 3 \mid 3\,]$; $R_3 \leftarrow R_3 - R_2$: $[\,0 \ \ 0 \ \ 0 \mid 1\,]$. **SI**. La combinación: $E_3 - E_1 - E_2$ da $0x + 0y + 0z = 6 - 1 - 4 = 1$.

**Verificación**: comprobado en `verificar/f08.py`.
</details>
<details><summary>Errores frecuentes</summary>Seguir sustituyendo hacia atrás; leer la última fila como $z = 1$.</details>

### F08-N3-03 · [C] Solución paramétrica 🎬

**Objetivo**: describir infinitas soluciones con un parámetro.
**Dificultad**: N3

**Enunciado.** Resuelve $x + 2y - z = 1$, $2x + 3y + z = 4$, $3x + 5y = 5$, da la solución en forma paramétrica y verifícala para todo $t$.

<details><summary>Pista 1</summary>Es el sistema de F08-N2-06 con un 5 en lugar del 6: la última fila queda nula.</details>
<details><summary>Pista 2</summary>$z$ no tiene pivote: $z = t$.</details>
<details><summary>Solución</summary>

Escalonada: $\left[\begin{array}{ccc|c} 1 & 2 & -1 & 1 \\ 0 & -1 & 3 & 2 \\ 0 & 0 & 0 & 0 \end{array}\right]$. $z = t$; $-y + 3t = 2 \Rightarrow y = 3t - 2$; $x = 1 - 2y + z = 5 - 5t$. Solución: $(5 - 5t,\ -2 + 3t,\ t) = (5, -2, 0) + t(-5, 3, 1)$, $t \in \mathbb{R}$ (SCI).

**Verificación**: $E_1$: $5 - 5t - 4 + 6t - t = 1$; $E_2$: $10 - 10t - 6 + 9t + t = 4$; $E_3$: $15 - 15t - 10 + 15t = 5$ ✓ para todo $t$.
</details>
<details><summary>Errores frecuentes</summary>Tomar $z = 0$ y dar una sola solución; equivocar el signo en $x = 1 - 2y + z$.</details>

### F08-N4-02 · [K] Clasificar a la vista de la escalonada

**Objetivo**: leer el tipo de sistema y el número de variables libres.
**Dificultad**: N4

**Enunciado.** Cada matriz es una forma escalonada de un $[A \mid \mathbf{b}]$. Clasifica (SCD, SCI, SI) y, si es SCI, di cuántas y cuáles son las variables libres.
a) $\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & 4 & 2 \\ 0 & 0 & 0 & 5 \end{array}\right]$ b) $\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{array}\right]$ c) $\left[\begin{array}{cc|c} 2 & 1 & 1 \\ 0 & 3 & 0 \end{array}\right]$ d) $\left[\begin{array}{cccc|c} 1 & -1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 3 & 4 \end{array}\right]$

<details><summary>Pista 1</summary>Primero busca una fila $[\,0 \cdots 0 \mid c\,]$ con $c \neq 0$.</details>
<details><summary>Pista 2</summary>Libres = incógnitas − pivotes (si no es SI).</details>
<details><summary>Solución</summary>

a) SI ($0 = 5$). b) SCI, 1 libre: $x_2$ (columnas pivote 1 y 3). c) SCD ($y = 0$, $x = \tfrac12$). d) SCI, 2 libres: $x_2$ y $x_4$.

**Verificación**: función `clasificar` en `verificar/f08.py`.
</details>
<details><summary>Errores frecuentes</summary>En c), decir SI porque $y = 0$; en b), contar las ecuaciones en lugar de los pivotes.</details>

### F08-N5-03 · [D] Sin fila contradictoria, hay solución

**Objetivo**: justificar la sustitución hacia atrás en general.
**Dificultad**: N5

**Enunciado.** Demuestra: si una forma escalonada de $[A \mid \mathbf{b}]$ no tiene ninguna fila $[\,0 \cdots 0 \mid c\,]$ con $c \neq 0$, el sistema tiene al menos una solución.

<details><summary>Pista 1</summary>Da a las variables libres un valor cualquiera (por ejemplo 0).</details>
<details><summary>Pista 2</summary>Recorre las filas no nulas de abajo arriba: cada una tiene un pivote $p \neq 0$ en la columna de su variable pivote.</details>
<details><summary>Solución</summary>

Las filas nulas son $0 = 0$ (por hipótesis, también en $\mathbf{b}$) y se cumplen siempre. Asignamos valores arbitrarios a las variables libres. La última fila no nula es $p\,x_k + (\text{términos en variables a su derecha}) = c$, con $p \neq 0$ y todas esas variables ya conocidas (son libres, porque no hay pivotes más a la derecha en filas de abajo): $x_k$ se despeja dividiendo por $p$. Cada fila de arriba solo contiene su variable pivote y variables de columnas más a la derecha, ya determinadas; se despeja igual. Así se cumplen todas las ecuaciones del sistema escalonado, y por la L24 también las del original. $\blacksquare$

**Verificación** (ejemplo): $\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 0 & 1 & 2 \end{array}\right]$ con $y = 5$: $z = 2$, $x = 3 - 10 + 2 = -5$ cumple las dos ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar que la división por el pivote es posible precisamente porque $p \neq 0$.</details>

### F08-N4-03 · [C] Discutir un 2 × 2 con parámetro 🎬

**Objetivo**: separar los casos en que un candidato a pivote se anula.
**Dificultad**: N4

**Enunciado.** Discute según $a$ y resuelve en cada caso: $x + 2y = 3$, $2x + ay = 6$.

<details><summary>Pista 1</summary>$R_2 \leftarrow R_2 - 2R_1$ da $[\,0 \ \ a - 4 \mid 0\,]$.</details>
<details><summary>Pista 2</summary>Separa $a = 4$.</details>
<details><summary>Solución</summary>

- $a \neq 4$: $(a - 4)y = 0 \Rightarrow y = 0$, $x = 3$. **SCD**, la misma solución para todo $a \neq 4$.
- $a = 4$: la segunda fila es nula: **SCI**, $y = t$, $x = 3 - 2t$.

Nunca es SI (el término independiente se anula a la vez).

**Verificación**: $(3, 0)$: $3 = 3$, $6 = 6$ ✓; $a = 4$: $3 - 2t + 2t = 3$, $6 - 4t + 4t = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dividir $(a - 4)y = 0$ entre $a - 4$ sin discutir.</details>

### F08-N4-04 · [C] Discutir un 3 × 3 con parámetro 🎬

**Objetivo**: hallar todos los valores críticos y estudiar cada caso.
**Dificultad**: N4

**Enunciado.** Discute según $a$ (SCD, SCI o SI) y resuelve cuando haya solución: $x + y + z = 1$, $x + 2y + 2z = 3$, $x + 2y + (a^2 - 2)z = a + 1$.

<details><summary>Pista 1</summary>$R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, $R_3 \leftarrow R_3 - R_2$.</details>
<details><summary>Pista 2</summary>La última fila queda $[\,0 \ \ 0 \ \ a^2 - 4 \mid a - 2\,]$, y $a^2 - 4 = (a - 2)(a + 2)$.</details>
<details><summary>Solución</summary>

Escalonada: $\left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & a^2 - 4 & a - 2 \end{array}\right]$.

- $a \neq \pm 2$: **SCD**. $z = \frac{a - 2}{a^2 - 4} = \frac{1}{a + 2}$, $y = 2 - z = \frac{2a + 3}{a + 2}$, $x = 1 - (y + z) = -1$.
- $a = 2$: última fila nula: **SCI**, $z = t$, $y = 2 - t$, $x = -1$.
- $a = -2$: $[\,0 \ \ 0 \ \ 0 \mid -4\,]$: **SI**.

**Verificación**: $E_3$: $-1 + 2(2 - z) + (a^2 - 2)z = 3 + (a^2 - 4)z = 3 + (a - 2) = a + 1$ ✓; valores de prueba de $a$ en `verificar/f08.py`.
</details>
<details><summary>Errores frecuentes</summary>Simplificar a $z = \frac{1}{a + 2}$ antes de discutir y perder el caso $a = 2$ (SCI).</details>

### F08-N4-05 · [K] El caso que se perdió

**Objetivo**: encontrar el error de una discusión que simplifica antes de separar casos.
**Dificultad**: N4

**Enunciado.** Para $x + ay = 1$, $ax + y = 1$, un estudiante hace $R_2 \leftarrow R_2 - aR_1$, obtiene $[\,0 \ \ 1 - a^2 \mid 1 - a\,]$, escribe $y = \frac{1 - a}{1 - a^2} = \frac{1}{1 + a}$ y concluye: "SCD salvo $a = -1$, que es SI". ¿Es correcta la operación? ¿Y la conclusión?

<details><summary>Pista 1</summary>Sumar a una fila un múltiplo de otra es legal aunque el multiplicador dependa de $a$ (incluso si vale 0).</details>
<details><summary>Pista 2</summary>¿Qué pasa con $a = 1$?</details>
<details><summary>Solución</summary>

La operación es legal. La conclusión no: simplificar entre $1 - a$ exige $a \neq 1$. Casos: $a \neq \pm 1$: SCD con $x = y = \frac{1}{1 + a}$. $a = 1$: las dos ecuaciones son $x + y = 1$: **SCI**. $a = -1$: $x - y = 1$ y $-x + y = 1$, que suman $0 = 2$: **SI**.

**Verificación**: $x + ay = \frac{1 + a}{1 + a} = 1$ ✓ (y simétricamente la otra); casos especiales en `verificar/f08.py`.
</details>
<details><summary>Errores frecuentes</summary>Pensar que la operación $R_2 - aR_1$ es ilegal "porque $a$ puede ser 0".</details>

### F08-N3-04 · [K] Encontrar el error 🎬

**Objetivo**: localizar un error de signo y comprobar en el original.
**Dificultad**: N3

**Enunciado.** Para $\left[\begin{array}{cc|c} 2 & 1 & 5 \\ 4 & -3 & 5 \end{array}\right]$ un estudiante escribe $R_2 \leftarrow R_2 - 2R_1$: $[\,0 \ \ -1 \mid -5\,]$ y concluye $y = 5$, $x = 0$. Encuentra el error, corrígelo y verifica.

<details><summary>Pista 1</summary>Comprueba $(0, 5)$ en la segunda ecuación original.</details>
<details><summary>Pista 2</summary>Columna 2: $-3 - 2\cdot 1$.</details>
<details><summary>Solución</summary>

El error está en la columna 2: $-3 - 2\cdot 1 = -5$, no $-1$. Fila correcta $[\,0 \ \ -5 \mid -5\,]$: $y = 1$, $2x + 1 = 5 \Rightarrow x = 2$.

**Verificación**: $(0, 5)$ falla: $4\cdot 0 - 15 = -15 \neq 5$. $(2, 1)$: $4 + 1 = 5$, $8 - 3 = 5$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Comprobar $(0, 5)$ en el sistema escalonado erróneo, donde sí "funciona".</details>

### F08-N4-06 · [K] Dos operaciones a la vez

**Objetivo**: entender por qué las operaciones se hacen de una en una.
**Dificultad**: N4

**Enunciado.** Para $x + y = 2$, $x - y = 0$, alguien aplica a la vez $R_1 \leftarrow R_1 - R_2$ y $R_2 \leftarrow R_2 - R_1$ (las dos con las filas originales) y concluye que hay infinitas soluciones. Explica el error.

<details><summary>Pista 1</summary>Calcula las dos filas nuevas: ¿qué relación hay entre ellas?</details>
<details><summary>Pista 2</summary>La segunda operación no usó la fila 1 que dejó la primera.</details>
<details><summary>Solución</summary>

Quedan $[\,0 \ \ 2 \mid 2\,]$ y $[\,0 \ \ -2 \mid -2\,]$: una es $-1$ por la otra, y parece SCI. Pero el par de cambios simultáneos no es una sucesión de operaciones elementales (la segunda usa la $R_1$ vieja) y no se puede deshacer: se perdió una ecuación. El sistema original tiene solución única $(1, 1)$. Hechas de una en una ($R_1 \leftarrow R_1 - R_2$ y después $R_2 \leftarrow R_2 - R_1$ con la $R_1$ nueva) queda $[\,0 \ \ 2 \mid 2\,]$, $[\,1 \ \ -3 \mid -2\,]$, que da otra vez $(1, 1)$.

**Verificación**: $1 + 1 = 2$, $1 - 1 = 0$ ✓; clasificaciones en `verificar/f08.py`.
</details>
<details><summary>Errores frecuentes</summary>Creer que "a la vez" o "en orden" da lo mismo.</details>

### F08-N4-07 · [C] Verificar una solución propuesta 🎬

**Objetivo**: comprobar en el original y, si falla, resolver.
**Dificultad**: N4

**Enunciado.** Un estudiante afirma que $(2, 1, 3)$ resuelve $x + y + z = 6$, $x - y + 2z = 5$, $2x + y - z = 1$. Compruébalo; si no es así, resuelve por Gauss y verifica.

<details><summary>Pista 1</summary>Sustituye en las tres ecuaciones, no solo en la primera.</details>
<details><summary>Pista 2</summary>$R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - 2R_1$, $R_3 \leftarrow R_3 - \tfrac12 R_2$.</details>
<details><summary>Solución</summary>

$(2, 1, 3)$ cumple $E_1$ ($6$) pero no $E_2$: $2 - 1 + 6 = 7 \neq 5$. Gauss: $\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -2 & 1 & -1 \\ 0 & -1 & -3 & -11 \end{array}\right] \to \left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -2 & 1 & -1 \\ 0 & 0 & -\frac72 & -\frac{21}{2} \end{array}\right]$: $z = 3$, $-2y + 3 = -1 \Rightarrow y = 2$, $x = 1$.

**Verificación**: $1 + 2 + 3 = 6$; $1 - 2 + 6 = 5$; $2 + 2 - 3 = 1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Comprobar solo la primera ecuación.</details>
