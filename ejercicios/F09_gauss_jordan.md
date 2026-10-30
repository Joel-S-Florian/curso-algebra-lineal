# F09 — Gauss-Jordan

Banco de las lecciones L31–L33. **Parte 1: 17 ejercicios**, ligados a los videos. La **parte 2** (23 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F09_gauss_jordan_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $R_i$ es la fila $i$; $R_2 \leftarrow R_2 - 3R_1$ significa "la fila 2 se sustituye por ella menos 3 veces la fila 1".
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f09.py`.

| Lección | Ejercicios |
|---|---|
| L31 Forma escalonada reducida | N1-01 🎬, N1-02, N2-01, N2-02 🎬, N3-01 🎬, N3-02, N3-03 |
| L32 Variables básicas y libres | N2-03 🎬, N2-04, N3-04 🎬, N4-01, N4-02, N5-01 |
| L33 Gauss frente a Gauss-Jordan | N2-05 🎬, N3-06 🎬, N4-03, N4-04 |

---

### F09-N1-01 · [K] ¿Reducida o no? 🎬

**Objetivo**: aplicar la definición de forma escalonada reducida.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de estas matrices están en forma escalonada reducida? Justifica cada respuesta con la definición.
$$A = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 2 \end{bmatrix} \qquad B = \begin{bmatrix} 1 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \qquad C = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$$

<details><summary>Pista 1</summary>Localiza los pivotes (primera entrada no nula de cada fila) y mira su columna entera.</details>
<details><summary>Pista 2</summary>Las columnas <em>sin</em> pivote pueden tener cualquier número.</details>
<details><summary>Solución</summary>

$A$ **sí**: pivotes $1$ en las columnas 1 y 2, y cada uno es la única entrada no nula de su columna.
$B$ **sí**: pivotes $1$ en las columnas 1 y 3, con ceros arriba y abajo; el $3$ está en la columna 2, que no tiene pivote, y eso está permitido.
$C$ **no**: el pivote de la fila 3 vale $2$, no $1$ (dividiendo esa fila entre $2$ sí sería reducida).
</details>
<details><summary>Errores frecuentes</summary>Rechazar $B$ por el $3$ (está en una columna sin pivote); aceptar $C$ por tener la forma de la identidad.</details>

### F09-N1-02 · [C] Un solo paso de Gauss-Jordan

**Objetivo**: hacer un cero encima de un pivote.
**Dificultad**: N1

**Enunciado.** Lleva a forma escalonada reducida $\left[\begin{array}{ccc|c} 1 & 3 & 0 & 2 \\ 0 & 1 & 0 & -1 \end{array}\right]$ y lee la solución del sistema de dos ecuaciones con tres incógnitas.

<details><summary>Pista 1</summary>Ya es escalonada y los pivotes valen 1: falta el cero encima del pivote de la fila 2.</details>
<details><summary>Pista 2</summary>$R_1 \leftarrow R_1 - 3R_2$ (todas las columnas, $\mathbf{b}$ incluida).</details>
<details><summary>Solución</summary>

$R_1 \leftarrow R_1 - 3R_2$ da $\left[\begin{array}{ccc|c} 1 & 0 & 0 & 5 \\ 0 & 1 & 0 & -1 \end{array}\right]$: $x = 5$, $y = -1$, y $z$ **no tiene pivote**: queda libre (se estudia en la L32).

**Verificación**: $5 + 3(-1) + 0z = 2$ ✓ y $-1 + 0z = -1$ ✓ para cualquier $z$.
</details>
<details><summary>Errores frecuentes</summary>Olvidar el $2$ de la última columna: $2 - 3(-1) = 5$.</details>

### F09-N2-01 · [C] Resolver un 2 × 2 por Gauss-Jordan

**Objetivo**: el algoritmo completo en un sistema pequeño.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss-Jordan, escribiendo cada operación, y verifica en el original: $\;x + 2y = 7,\ \ 3x - y = 7.$

<details><summary>Pista 1</summary>Pivote 1 en la posición (1, 1); haz un cero debajo.</details>
<details><summary>Pista 2</summary>Luego divide la fila 2 entre su pivote y haz el cero de arriba.</details>
<details><summary>Solución</summary>

$\left[\begin{array}{cc|c} 1 & 2 & 7 \\ 3 & -1 & 7 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 3R_1} \left[\begin{array}{cc|c} 1 & 2 & 7 \\ 0 & -7 & -14 \end{array}\right] \xrightarrow{R_2 \leftarrow -\frac17 R_2} \left[\begin{array}{cc|c} 1 & 2 & 7 \\ 0 & 1 & 2 \end{array}\right] \xrightarrow{R_1 \leftarrow R_1 - 2R_2} \left[\begin{array}{cc|c} 1 & 0 & 3 \\ 0 & 1 & 2 \end{array}\right]$

Solución $(x, y) = (3, 2)$.

**Verificación**: $3 + 4 = 7$ ✓, $9 - 2 = 7$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dividir solo los coeficientes de la fila 2 y no el $-14$.</details>

### F09-N2-02 · [C] Resolver un 3 × 3 por Gauss-Jordan 🎬

**Objetivo**: ejecutar las tres fases con tres incógnitas.
**Dificultad**: N2

**Enunciado.** Resuelve por Gauss-Jordan y verifica en el original:
$$\begin{cases} x + y + z = 2 \\ 2x + 3y + z = 7 \\ x - y + 2z = -3 \end{cases}$$

<details><summary>Pista 1</summary>Primero ceros debajo del pivote de la columna 1; luego usa la fila 2 para anular la columna 2 de la fila 3.</details>
<details><summary>Pista 2</summary>Tras escalonar: $R_3 = [\,0 \ \ 0 \ \ -1 \mid 1\,]$. Después, pivote a 1 y ceros encima de derecha a izquierda.</details>
<details><summary>Solución</summary>

$R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - R_1$, $R_3 \leftarrow R_3 + 2R_2$ dan $\left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & 1 & -1 & 3 \\ 0 & 0 & -1 & 1 \end{array}\right]$. Luego $R_3 \leftarrow -R_3$, $R_2 \leftarrow R_2 + R_3$, $R_1 \leftarrow R_1 - R_3$, $R_1 \leftarrow R_1 - R_2$:

$\left[\begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & -1 \end{array}\right]$, solución $(1, 2, -1)$.

**Verificación**: $1 + 2 - 1 = 2$ ✓, $2 + 6 - 1 = 7$ ✓, $1 - 2 - 2 = -3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Usar la fila 1 vieja para anular la columna 2; empezar los ceros de arriba por la columna 2 y estropearlos después.</details>

### F09-N3-01 · [C] Dos caminos, una reducida 🎬

**Objetivo**: comprobar la unicidad de la forma reducida.
**Dificultad**: N3

**Enunciado.** Reduce $\left[\begin{array}{cc|c} 0 & 2 & 4 \\ 1 & 1 & 3 \end{array}\right]$ por dos caminos distintos y comprueba que llegas a la misma matriz.

<details><summary>Pista 1</summary>Un camino empieza intercambiando las filas; el otro, dividiendo la fila 1 entre 2.</details>
<details><summary>Pista 2</summary>Las dos formas escalonadas intermedias pueden ser distintas; solo la reducida es única.</details>
<details><summary>Solución</summary>

Camino 1: $R_1 \leftrightarrow R_2$, $R_2 \leftarrow \frac12 R_2$, $R_1 \leftarrow R_1 - R_2$.
Camino 2: $R_1 \leftarrow \frac12 R_1$, $R_1 \leftrightarrow R_2$, $R_1 \leftarrow R_1 - R_2$.

Los dos terminan en $\left[\begin{array}{cc|c} 1 & 0 & 1 \\ 0 & 1 & 2 \end{array}\right]$: solución $(1, 2)$ ($0 + 4 = 4$ ✓, $1 + 2 = 3$ ✓).
</details>
<details><summary>Errores frecuentes</summary>Concluir que se equivocó el otro camino porque las matrices intermedias no coinciden.</details>

### F09-N3-02 · [K] Verdadero o falso

**Objetivo**: manejar el teorema de unicidad.
**Dificultad**: N3

**Enunciado.** Decide y justifica (con una demostración breve o un contraejemplo): a) toda matriz en forma escalonada reducida es escalonada; b) toda matriz escalonada cuyos pivotes valen 1 es reducida; c) si dos matrices son equivalentes por filas, tienen la misma forma escalonada reducida; d) dos matrices con la misma forma escalonada son equivalentes por filas.

<details><summary>Pista 1</summary>Para b) busca una matriz $2\times 2$ con pivotes 1 y un número encima del segundo pivote.</details>
<details><summary>Pista 2</summary>Para c) y d), usa que "equivalentes" es transitiva y que la reducida es única (L31, parte 3).</details>
<details><summary>Solución</summary>

a) **V**: la definición de reducida incluye ser escalonada. b) **F**: $\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ es escalonada con pivotes $1$, pero hay un $2$ encima del segundo pivote; su reducida es $I$. c) **V**: cada una es equivalente a su reducida; si son equivalentes entre sí, comparten reducida por la unicidad. d) **V**: ambas son equivalentes a la misma matriz escalonada, y "equivalente" es transitiva y simétrica.
</details>
<details><summary>Errores frecuentes</summary>Creer que b) es cierto porque los pivotes valen 1; olvidar la condición de los ceros encima.</details>

### F09-N3-03 · [C] Gauss-Jordan con fracciones

**Objetivo**: llegar a la reducida con multiplicadores fraccionarios, sin decimales.
**Dificultad**: N3

**Enunciado.** Resuelve por Gauss-Jordan, con fracciones exactas, y verifica:
$$\begin{cases} 2x + y - z = 8 \\ -3x - y + 2z = -11 \\ -2x + y + 2z = -3 \end{cases}$$

<details><summary>Pista 1</summary>Empieza con $R_1 \leftarrow \frac12 R_1$ para tener pivote 1 (aparecerán medios).</details>
<details><summary>Pista 2</summary>Tras los ceros de debajo, $R_2$ queda $[\,0 \ \ \tfrac12 \ \ \tfrac12 \mid 1\,]$: multiplícala por $2$.</details>
<details><summary>Solución</summary>

$R_1 \leftarrow \frac12 R_1$; $R_2 \leftarrow R_2 + 3R_1$, $R_3 \leftarrow R_3 + 2R_1$; $R_2 \leftarrow 2R_2$; $R_3 \leftarrow R_3 - 2R_2$, $R_3 \leftarrow -R_3$ dan $\left[\begin{array}{ccc|c} 1 & \frac12 & -\frac12 & 4 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & 1 & -1 \end{array}\right]$. Luego $R_2 \leftarrow R_2 - R_3$, $R_1 \leftarrow R_1 + \frac12 R_3$, $R_1 \leftarrow R_1 - \frac12 R_2$:

$\left[\begin{array}{ccc|c} 1 & 0 & 0 & 2 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & -1 \end{array}\right]$, solución $(2, 3, -1)$.

**Verificación**: $4 + 3 + 1 = 8$ ✓, $-6 - 3 - 2 = -11$ ✓, $-4 + 3 - 2 = -3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Pasar $\frac12$ a $0.5$ y arrastrar redondeos; olvidar el $4$ de la columna $\mathbf{b}$ al dividir.</details>

### F09-N2-03 · [C] Leer la solución paramétrica 🎬

**Objetivo**: reducir, identificar básicas y libres y escribir la solución en forma paramétrica y vectorial.
**Dificultad**: N2

**Enunciado.** Resuelve $\;x + 2y + z = 3,\ \ 2x + 4y + 3z = 8$. Indica las variables básicas y las libres, escribe la solución con parámetros y en forma vectorial, y verifica.

<details><summary>Pista 1</summary>$R_2 \leftarrow R_2 - 2R_1$ ya deja la matriz escalonada.</details>
<details><summary>Pista 2</summary>Falta un cero encima del pivote de la columna 3: $R_1 \leftarrow R_1 - R_2$.</details>
<details><summary>Solución</summary>

$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 2 & 4 & 3 & 8 \end{array}\right] \to \left[\begin{array}{ccc|c} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \end{array}\right]$. Básicas: $x, z$. Libre: $y = t$. Solución: $x = 1 - 2t,\ y = t,\ z = 2$, es decir, $(x, y, z) = (1, 0, 2) + t\,(-2, 1, 0)$.

**Verificación**: $(1 - 2t) + 2t + 2 = 3$ ✓ y $2(1 - 2t) + 4t + 6 = 8$ ✓ para todo $t$.
</details>
<details><summary>Errores frecuentes</summary>Tomar $x$ como libre (es básica: su columna tiene pivote); olvidar que $z = 2$ es fijo.</details>

### F09-N2-04 · [C] Una ecuación redundante y dos libres

**Objetivo**: reconocer una fila nula y contar parámetros.
**Dificultad**: N2

**Enunciado.** Resuelve $\;x + y + z + w = 4,\ \ x + 2y + 3z + 4w = 10,\ \ 2x + 3y + 4z + 5w = 14$ y explica por qué sobra una ecuación.

<details><summary>Pista 1</summary>Haz los ceros debajo del primer pivote y compara las filas 2 y 3.</details>
<details><summary>Pista 2</summary>Tras $R_2 \leftarrow R_2 - R_1$ y $R_3 \leftarrow R_3 - 2R_1$, las filas 2 y 3 son iguales.</details>
<details><summary>Solución</summary>

$R_3 \leftarrow R_3 - R_2$ da una fila nula; con $R_1 \leftarrow R_1 - R_2$ queda $\left[\begin{array}{cccc|c} 1 & 0 & -1 & -2 & -2 \\ 0 & 1 & 2 & 3 & 6 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$. Libres: $z = s$, $w = t$ (4 incógnitas $-$ 2 pivotes). Solución: $x = -2 + s + 2t,\ y = 6 - 2s - 3t$.

Sobra una ecuación porque la tercera es la suma de la primera y la segunda: $E_1 + E_2 = (2, 3, 4, 5 \mid 14)$.

**Verificación** (primera ecuación): $(-2 + s + 2t) + (6 - 2s - 3t) + s + t = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dar solo una solución particular; contar tres pivotes por haber tres ecuaciones.</details>

### F09-N3-04 · [C] Clasificar con la reducida 🎬

**Objetivo**: decidir SCD, SCI o SI mirando los pivotes.
**Dificultad**: N3

**Enunciado.** Clasifica el sistema de cada matriz aumentada reducida y, si es compatible, da la solución:
a) $\left[\begin{array}{ccc|c} 1 & 0 & 3 & 2 \\ 0 & 1 & -1 & 4 \end{array}\right]$ b) $\left[\begin{array}{ccc|c} 1 & 0 & 0 & 5 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & 0 \end{array}\right]$ c) $\left[\begin{array}{ccc|c} 1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array}\right]$

<details><summary>Pista 1</summary>Primero: ¿hay un pivote en la última columna?</details>
<details><summary>Pista 2</summary>Si no, compara el número de pivotes con el de incógnitas.</details>
<details><summary>Solución</summary>

a) **SCI**: 2 pivotes, 3 incógnitas; $z = t$ libre: $(2 - 3t,\ 4 + t,\ t)$. b) **SCD**: $(5, 3, 0)$. c) **SI**: la fila $[\,0 \ 0 \ 0 \mid 1\,]$ tiene su pivote en la columna de $\mathbf{b}$ ($0 = 1$).

**Verificación** de a): $(2 - 3t) + 3t = 2$ ✓ y $(4 + t) - t = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>En c) concluir SCI por haber una columna sin pivote antes de mirar la columna de $\mathbf{b}$.</details>

### F09-N4-01 · [C] Sistema homogéneo con parámetro

**Objetivo**: reducir un homogéneo y escribir su solución.
**Dificultad**: N4

**Enunciado.** Resuelve $A\mathbf{x} = \mathbf{0}$ con $A = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & 0 & 8 \\ -1 & -2 & 2 & -4 \end{bmatrix}$. ¿Cuántos parámetros tiene la solución?

<details><summary>Pista 1</summary>En un homogéneo la última columna son ceros y no cambia: puedes trabajar solo con $A$.</details>
<details><summary>Pista 2</summary>$R_2 \leftarrow R_2 - 2R_1$ y $R_3 \leftarrow R_3 + R_1$; después anula con la fila 3 la entrada de la columna 3 de la fila 2.</details>
<details><summary>Solución</summary>

La reducida es $\begin{bmatrix} 1 & 2 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$: tres pivotes (columnas 1, 3 y 4), así que $y = t$ es la única libre. Solución: $(x, y, z, w) = t\,(-2, 1, 0, 0)$. Un parámetro.

**Verificación**: $-2t + 2t = 0$ ✓; $-4t + 4t = 0$ ✓; $2t - 2t = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Pensar que hay dos parámetros por tener 4 incógnitas y 3 ecuaciones: lo que cuenta son los pivotes (3).</details>

### F09-N4-02 · [K] Tres ecuaciones, cinco incógnitas

**Objetivo**: razonar con pivotes sin resolver.
**Dificultad**: N4

**Enunciado.** Un sistema tiene 3 ecuaciones y 5 incógnitas. a) ¿Puede ser SCD? b) ¿Qué finales son posibles? c) Si es SCI y la matriz de coeficientes no es nula, ¿cuántos parámetros puede tener?

<details><summary>Pista 1</summary>Hay a lo sumo un pivote por fila.</details>
<details><summary>Pista 2</summary>Parámetros $= n - r$, con $r$ el número de pivotes.</details>
<details><summary>Solución</summary>

a) **No**: $r \le 3 < 5$, así que siempre queda alguna incógnita sin pivote. b) **SCI o SI**. c) $r \in \{1, 2, 3\}$ y los parámetros son $5 - r \in \{2, 3, 4\}$: entre 2 y 4.
</details>
<details><summary>Errores frecuentes</summary>Afirmar que "con menos ecuaciones que incógnitas siempre hay infinitas": también puede ser incompatible.</details>

### F09-N5-01 · [D] Cuándo hay solución única

**Objetivo**: demostrar el criterio de los pivotes.
**Dificultad**: N5

**Enunciado.** Demuestra: un sistema compatible de $n$ incógnitas tiene solución única si y solo si la forma reducida de $[A \mid \mathbf{b}]$ tiene $n$ pivotes.

<details><summary>Pista 1</summary>Compatible significa que no hay pivote en la columna de $\mathbf{b}$.</details>
<details><summary>Pista 2</summary>Si falta un pivote, esa incógnita es libre: prueba con dos valores distintos.</details>
<details><summary>Solución</summary>

($\Leftarrow$) Con $n$ pivotes y ninguno en $\mathbf{b}$, la reducida es $[\,I_n \mid \mathbf{c}\,]$ más filas nulas, y el sistema dice $x_j = c_j$ para cada $j$: una sola solución. ($\Rightarrow$) Si hay menos de $n$ pivotes, alguna columna $j$ no tiene pivote y $x_j$ es libre. Dando a $x_j$ los valores $0$ y $1$ (y a las demás libres, si las hay, el valor $0$), las variables básicas quedan determinadas y salen dos soluciones distintas; luego no es única. $\blacksquare$
</details>
<details><summary>Errores frecuentes</summary>Olvidar la hipótesis "compatible": con un pivote en $\mathbf{b}$ no hay ninguna solución.</details>

### F09-N2-05 · [C] Contar operaciones 🎬

**Objetivo**: usar las fórmulas de la L33.
**Dificultad**: N2

**Enunciado.** Con $\dfrac{n^3 + 3n^2 - n}{3}$ (Gauss con sustitución hacia atrás) y $\dfrac{n^3 + n^2}{2}$ (Gauss-Jordan), calcula las multiplicaciones y divisiones para $n = 4$ y $n = 5$. ¿Qué método gana y por cuánto?

<details><summary>Pista 1</summary>Sustituye $n$ en cada fórmula; los dos resultados son enteros.</details>
<details><summary>Pista 2</summary>Compara dividiendo: Gauss-Jordan entre Gauss.</details>
<details><summary>Solución</summary>

$n = 4$: Gauss $\frac{64 + 48 - 4}{3} = 36$; Gauss-Jordan $\frac{64 + 16}{2} = 40$. $n = 5$: Gauss $\frac{125 + 75 - 5}{3} = 65$; Gauss-Jordan $\frac{125 + 25}{2} = 75$. Gana Gauss: $40/36 \approx 1{,}11$ y $75/65 \approx 1{,}15$ (Gauss-Jordan hace un 11 % y un 15 % más).
</details>
<details><summary>Errores frecuentes</summary>Usar solo el término principal ($n^3/3$ y $n^3/2$): para $n$ pequeño da resultados muy distintos de los reales.</details>

### F09-N3-06 · [K] Elegir el método 🎬

**Objetivo**: justificar la elección entre Gauss y Gauss-Jordan.
**Dificultad**: N3

**Enunciado.** Elige y justifica el método más adecuado: a) un sistema $2 \times 2$ a mano en un examen; b) un sistema $2000 \times 2000$ en un ordenador; c) decidir si dos sistemas son equivalentes.

<details><summary>Pista 1</summary>Piensa en el número de operaciones (b) y en qué se obtiene de cada método (c).</details>
<details><summary>Pista 2</summary>Recuerda el teorema de unicidad (L31).</details>
<details><summary>Solución</summary>

a) Gauss-Jordan: pocas operaciones y la solución se lee directamente, con menos riesgo de error al sustituir. b) Gauss con sustitución hacia atrás: hace aproximadamente un tercio menos de operaciones ($n^3/3$ frente a $n^3/2$). c) La reducida: dos sistemas son equivalentes si y solo si sus matrices aumentadas tienen la misma, y es única.
</details>
<details><summary>Errores frecuentes</summary>Pensar que uno de los dos métodos "da una solución distinta": dan exactamente el mismo conjunto solución.</details>

### F09-N4-03 · [D] Fórmula de Gauss-Jordan

**Objetivo**: deducir el conteo de operaciones de Gauss-Jordan.
**Dificultad**: N4

**Enunciado.** Contando multiplicaciones y divisiones (sistema $n \times n$, una columna $\mathbf{b}$, sin intercambios), demuestra que Gauss-Jordan hace $\dfrac{n^2(n+1)}{2}$.

<details><summary>Pista 1</summary>En el paso $k$: dividir la fila del pivote cuesta tantas operaciones como entradas a la derecha del pivote (incluida $\mathbf{b}$).</details>
<details><summary>Pista 2</summary>Anular cada una de las otras $n - 1$ filas cuesta lo mismo que dividir la fila del pivote.</details>
<details><summary>Solución</summary>

En el paso $k$, la fila del pivote tiene $n - k + 1$ entradas a su derecha (columnas $k+1, \dots, n$ y $\mathbf{b}$): dividirla cuesta $n - k + 1$. Cada una de las otras $n - 1$ filas se anula con $a_{ik}$ por la fila del pivote: $n - k + 1$ multiplicaciones por fila. Total del paso $k$: $n\,(n - k + 1)$. Sumando, $\sum_{k=1}^{n} n(n - k + 1) = n \cdot \frac{n(n+1)}{2} = \frac{n^2(n+1)}{2}$. $\blacksquare$

**Comprobación**: $n = 3$ da $18$ (contado con un programa en `f09.py`).
</details>
<details><summary>Errores frecuentes</summary>Contar también la entrada del pivote, que pasa a valer $1$ sin operación.</details>

### F09-N4-04 · [D] Fórmula de Gauss y límite del cociente

**Objetivo**: deducir el conteo de Gauss y comparar.
**Dificultad**: N4

**Enunciado.** Demuestra que Gauss con sustitución hacia atrás hace $\dfrac{n^3 + 3n^2 - n}{3}$ multiplicaciones y divisiones, y que el cociente Gauss-Jordan / Gauss tiende a $\tfrac32$.

<details><summary>Pista 1</summary>Eliminación: en el paso $k$ hay $n - k$ filas; cada una cuesta 1 división (el multiplicador) y $n - k + 1$ multiplicaciones.</details>
<details><summary>Pista 2</summary>Usa $\sum j^2 = \frac{m(m+1)(2m+1)}{6}$. La sustitución cuesta $\frac{n(n+1)}{2}$.</details>
<details><summary>Solución</summary>

Eliminación: $\sum_{k=1}^{n-1} (n - k)(n - k + 2) = \sum_{j=1}^{n-1} (j^2 + 2j) = \frac{n(n-1)(2n+5)}{6}$. Sustitución hacia atrás: $\frac{n(n-1)}{2}$ multiplicaciones $+\, n$ divisiones $= \frac{n(n+1)}{2}$. Total $\frac{n^3 + 3n^2 - n}{3}$. El cociente es $\frac{(n^3 + n^2)/2}{(n^3 + 3n^2 - n)/3} = \frac{3(n^2 + n)}{2(n^2 + 3n - 1)} \to \frac32$. $\blacksquare$

**Comprobación**: $n = 3$ da $17$ y $18$.
</details>
<details><summary>Errores frecuentes</summary>Olvidar que cada fila de la eliminación necesita su división para el multiplicador.</details>
