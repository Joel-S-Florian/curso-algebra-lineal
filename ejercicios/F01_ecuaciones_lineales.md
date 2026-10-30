# F01 — Ecuaciones lineales y ecuaciones con una incógnita

Banco de las lecciones L05–L06. **Parte 1: 13 ejercicios**, ligados a los videos. La **parte 2** (27 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F01_ecuaciones_lineales_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1 fundamentos · N2 rutinarios · N3 elegir método o razonar · N4 casos especiales, parámetros y errores · N5 demostraciones.
- **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. 🎬 = aparece al final de un video.
- Resultados comprobados con aritmética exacta en `ejercicios/verificar/f01_f03.py`.

| Lección | Ejercicios |
|---|---|
| L05 ¿Qué es una ecuación lineal? | N1-01 🎬, N1-02 🎬, N1-03, N4-01 🎬 |
| L06 Una incógnita | N1-04, N2-01 🎬, N2-02, N2-03, N3-01, N3-02, N4-02 🎬, N4-03, N5-01 |

---

### F01-N1-01 · [C] Llevar a la forma estándar 🎬

**Objetivo**: escribir una ecuación lineal como $a_1x + a_2y + a_3z = b$ e identificar sus datos.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $a_1x + a_2y + a_3z = b$ e indica coeficientes y término independiente: a) $4x = 2y - z + 3$ b) $\frac{x - y}{2} = z$ c) $5 = x$

<details><summary>Pista 1</summary>Pasa todas las incógnitas a la izquierda y los números a la derecha (regla 1).</details>
<details><summary>Pista 2</summary>Si una incógnita no aparece, su coeficiente es 0.</details>
<details><summary>Solución</summary>

a) Restando $2y$ y sumando $z$: $4x - 2y + z = 3$. Coeficientes $(4, -2, 1)$, $b = 3$.
b) $\frac x2 - \frac y2 = z$, luego $\frac12 x - \frac12 y - z = 0$. Coeficientes $(\frac12, -\frac12, -1)$, $b = 0$.
c) $x = 5$, es decir, $1x + 0y + 0z = 5$. Coeficientes $(1, 0, 0)$, $b = 5$.

**Verificación**: el punto $(1, 1, 1)$ cumple a) en la forma original ($4 = 2 - 1 + 3$) y en la estándar ($4 - 2 + 1 = 3$); al ser equivalentes, debe cumplir ambas o ninguna.
</details>
<details><summary>Errores frecuentes</summary>Olvidar cambiar el signo de $-z$ al pasarlo de lado; decir que en c) "no hay coeficientes".</details>

### F01-N1-02 · [K] ¿Lineal o no lineal? 🎬

**Objetivo**: reconocer los rasgos que hacen no lineal una ecuación.
**Dificultad**: N1

**Enunciado.** ¿Lineal o no lineal? Si no lo es, di por qué. a) $3x - y = 2z$ b) $xy + z = 1$ c) $\frac{x}{5} + 4 = y$ d) $\frac{5}{x} + y = 1$ e) $x + y^2 = 3$ f) $\pi x - \sqrt3\, y = 0$

<details><summary>Pista 1</summary>Busca potencias, productos entre incógnitas, incógnitas en denominadores o dentro de raíces y funciones.</details>
<details><summary>Pista 2</summary>Los coeficientes pueden ser cualquier número real: $\pi$ y $\sqrt3$ son números fijos.</details>
<details><summary>Solución</summary>

a) Lineal ($3x - y - 2z = 0$). b) No: producto $xy$. c) Lineal ($\frac15 x - y = -4$). d) No: $x$ en el denominador. e) No: $y^2$. f) Lineal.

**Verificación**: las lineales se pueden escribir en la forma $a_1x + a_2y + a_3z = b$; las otras no.
</details>
<details><summary>Errores frecuentes</summary>Confundir $\frac x5$ (lineal) con $\frac5x$ (no lineal); creer que $\sqrt3\,y$ es no lineal por llevar una raíz.</details>

### F01-N1-03 · [K] Coeficientes con signo

**Objetivo**: identificar coeficientes y término independiente con sus signos.
**Dificultad**: N1

**Enunciado.** En la ecuación $2x_1 - x_3 + 7 = 4x_2$, con incógnitas $x_1, x_2, x_3$, escribe la forma estándar y da $a_1, a_2, a_3, b$.

<details><summary>Pista 1</summary>El 7 está a la izquierda: hay que pasarlo a la derecha.</details>
<details><summary>Pista 2</summary>Ordena las incógnitas por su subíndice.</details>
<details><summary>Solución</summary>

$2x_1 - 4x_2 - x_3 = -7$: $a_1 = 2$, $a_2 = -4$, $a_3 = -1$, $b = -7$.

**Verificación**: $(0, 0, 7)$ cumple la original ($-7 + 7 = 0 = 4\cdot 0$) y la estándar ($-7 = -7$).
</details>
<details><summary>Errores frecuentes</summary>Dar $b = 7$; dar $a_3 = 1$.</details>

### F01-N1-04 · [C] Comprobar una solución

**Objetivo**: verificar por sustitución, también con fracciones.
**Dificultad**: N1

**Enunciado.** ¿Es $x = -\frac32$ solución de $4x + 7 = 1$? ¿Y $x = \frac32$?

<details><summary>Pista 1</summary>Sustituye entre paréntesis.</details>
<details><summary>Pista 2</summary>$4\cdot\left(-\frac32\right) = -6$.</details>
<details><summary>Solución</summary>

$4(-\frac32) + 7 = -6 + 7 = 1$: **sí**. $4(\frac32) + 7 = 13 \neq 1$: **no**.

**Verificación**: resolviendo, $4x = -6$, $x = -\frac32$.
</details>
<details><summary>Errores frecuentes</summary>Olvidar el signo al multiplicar.</details>

### F01-N2-01 · [C] Resolver justificando cada paso 🎬

**Objetivo**: llevar una ecuación con paréntesis y fracciones a $ax = b$.
**Dificultad**: N2

**Enunciado.** Resuelve $4(x - 1) - (2x + 3) = \frac{x}{2}$ justificando cada paso, y verifica.

<details><summary>Pista 1</summary>Quita los paréntesis; el signo menos afecta a $2x$ y a $3$.</details>
<details><summary>Pista 2</summary>Multiplica ambos lados por 2 para quitar el denominador.</details>
<details><summary>Solución</summary>

- Distributiva: $4x - 4 - 2x - 3 = \frac x2$, es decir, $2x - 7 = \frac x2$.
- Multiplicar por 2 (regla 2): $4x - 14 = x$.
- Restar $x$ y sumar 14 (regla 1): $3x = 14$.
- Dividir entre 3, que no es 0 (regla 2): $x = \frac{14}{3}$.

**Verificación**: izquierda $4\cdot\frac{11}{3} - \left(\frac{28}{3} + 3\right) = \frac{44}{3} - \frac{37}{3} = \frac73$; derecha $\frac{14}{3}\cdot\frac12 = \frac73$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$-(2x + 3) = -2x + 3$; multiplicar por 2 solo el lado derecho.</details>

### F01-N2-02 · [C] Varios paréntesis

**Objetivo**: aplicar la distributiva con signos negativos.
**Dificultad**: N2

**Enunciado.** Resuelve y verifica: $3(2x - 1) - 2(x + 4) = 5 - (x - 2)$.

<details><summary>Pista 1</summary>El $-2$ multiplica a $x$ y a $4$; el signo menos final afecta a $x$ y a $-2$.</details>
<details><summary>Pista 2</summary>Deberías llegar a $4x - 11 = 7 - x$.</details>
<details><summary>Solución</summary>

$6x - 3 - 2x - 8 = 5 - x + 2$, es decir, $4x - 11 = 7 - x$. Sumando $x$ y 11: $5x = 18$, $x = \frac{18}{5}$.

**Verificación**: izquierda $3\cdot\frac{31}{5} - 2\cdot\frac{38}{5} = \frac{93 - 76}{5} = \frac{17}{5}$; derecha $5 - \frac{8}{5} = \frac{17}{5}$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$-2(x + 4) = -2x + 8$; $-(x - 2) = -x - 2$.</details>

### F01-N2-03 · [C] Con denominadores

**Objetivo**: elegir el multiplicador adecuado para quitar denominadores.
**Dificultad**: N2

**Enunciado.** Resuelve y verifica: $\dfrac{x - 1}{4} - \dfrac{2x + 1}{6} = \dfrac13$.

<details><summary>Pista 1</summary>El menor múltiplo común de 4, 6 y 3 es 12.</details>
<details><summary>Pista 2</summary>Al multiplicar por 12, cada numerador debe ir entre paréntesis.</details>
<details><summary>Solución</summary>

Por 12: $3(x - 1) - 2(2x + 1) = 4$, es decir, $3x - 3 - 4x - 2 = 4$, $-x - 5 = 4$, $x = -9$.

**Verificación**: $\frac{-10}{4} - \frac{-17}{6} = -\frac52 + \frac{17}{6} = \frac{-15 + 17}{6} = \frac13$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$-2(2x + 1) = -4x + 2$ (el signo menos de la fracción afecta a todo el numerador).</details>

### F01-N3-01 · [K] ¿Cuántas soluciones?

**Objetivo**: reconocer los tres casos de $ax = b$ sin resolver "a ciegas".
**Dificultad**: N3

**Enunciado.** Lleva cada ecuación a la forma $ax = b$ y di cuántas soluciones tiene: a) $2(x + 3) = 2x + 5$ b) $3x - (x - 4) = 2(x + 2)$ c) $\frac12 x = 0$

<details><summary>Pista 1</summary>Simplifica cada lado por separado.</details>
<details><summary>Pista 2</summary>Mira si $a$ (el coeficiente de $x$ que queda) es 0.</details>
<details><summary>Solución</summary>

a) $2x + 6 = 2x + 5$, o sea $0x = -1$: **ninguna**.
b) $2x + 4 = 2x + 4$, o sea $0x = 0$: **infinitas** (todo $\mathbb{R}$).
c) $a = \frac12 \neq 0$: **una**, $x = 0$.

**Verificación**: en b), por ejemplo $x = 10$: $30 - 6 = 24 = 2\cdot 12$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Pensar que "$x = 0$" significa "no hay solución".</details>

### F01-N3-02 · [C] Un problema con palabras

**Objetivo**: traducir un enunciado a una ecuación lineal.
**Dificultad**: N3

**Enunciado.** Un número más su mitad es 21. ¿Cuál es el número?

<details><summary>Pista 1</summary>Llama $x$ al número. "Su mitad" es $\frac x2$.</details>
<details><summary>Pista 2</summary>Multiplica por 2 para quitar el denominador.</details>
<details><summary>Solución</summary>

$x + \frac x2 = 21 \Rightarrow 2x + x = 42 \Rightarrow 3x = 42 \Rightarrow x = 14$.

**Verificación**: $14 + 7 = 21$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Escribir $\frac{x + x}{2} = 21$ ("la mitad de la suma").</details>

### F01-N4-01 · [K] Trampas de linealidad 🎬

**Objetivo**: decidir la linealidad después de simplificar y detectar denominadores con incógnitas.
**Dificultad**: N4

**Enunciado.** ¿Son lineales en $x, y$? a) $(x - 2)(x + 2) = x^2 + y$ b) $\dfrac{x}{y + 1} = 3$ c) $k\,x - k^2 y = 1$ ($k$ número fijo) d) $2x + 3y = 2x + 3y + 1$

<details><summary>Pista 1</summary>a) Desarrolla el producto y simplifica.</details>
<details><summary>Pista 2</summary>b) ¿Qué pasa en el punto $(0, -1)$?</details>
<details><summary>Solución</summary>

a) $x^2 - 4 = x^2 + y \Leftrightarrow y = -4$: **lineal** ($0x + y = -4$).
b) **No lineal**: $y$ aparece en un denominador. Multiplicando por $y + 1$ se obtiene $x = 3y + 3$, pero eso exige $y \neq -1$: el punto $(0, -1)$ cumple $x = 3y + 3$ y no la original (no está definida).
c) **Lineal** en $x, y$: los coeficientes $k$ y $-k^2$ son números fijos.
d) Restando: $0 = 1$, es decir, $0x + 0y = 1$: **lineal degenerada**, sin solución.

**Verificación**: a) $(1, -4)$: $(-1)(3) = -3 = 1 - 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Decidir a) como no lineal "porque tiene $x^2$"; considerar b) lineal sin estudiar $y = -1$.</details>

### F01-N4-02 · [C] Discutir con un parámetro 🎬

**Objetivo**: separar los valores del parámetro que anulan el coeficiente.
**Dificultad**: N4

**Enunciado.** Discute según el valor de $k$: $(k^2 - 1)\,x = k + 1$.

<details><summary>Pista 1</summary>¿Para qué valores de $k$ vale 0 el coeficiente $k^2 - 1$?</details>
<details><summary>Pista 2</summary>$k^2 - 1 = (k - 1)(k + 1)$ (compruébalo con la distributiva).</details>
<details><summary>Solución</summary>

$k^2 - 1 = 0 \Leftrightarrow k = 1$ o $k = -1$.

- $k \neq \pm 1$: se puede dividir: $x = \frac{k + 1}{(k - 1)(k + 1)} = \frac{1}{k - 1}$ (una solución).
- $k = 1$: $0x = 2$: **ninguna**.
- $k = -1$: $0x = 0$: **infinitas**.

**Verificación**: $k = 3$: $8x = 4$, $x = \frac12 = \frac{1}{3 - 1}$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dar $x = \frac{1}{k - 1}$ "para todo $k$" (falla en $k = \pm1$).</details>

### F01-N4-03 · [K] Encuentra el error

**Objetivo**: detectar conclusiones falsas en los casos degenerados.
**Dificultad**: N4

**Enunciado.** a) Un estudiante resuelve $2x - 3 = 2(x - 1)$: "$2x - 3 = 2x - 2$, luego $-3 = -2$, así que $x = 0$". b) Otro resuelve $(a - 1)x = a - 1$: "dividiendo, $x = 1$". Corrige ambos.

<details><summary>Pista 1</summary>a) ¿Qué significa llegar a una igualdad falsa?</details>
<details><summary>Pista 2</summary>b) ¿Se puede dividir entre $a - 1$ siempre?</details>
<details><summary>Solución</summary>

a) $-3 = -2$ es falsa para todo $x$: **no hay solución**. "$x = 0$" no se deduce de nada.
b) Si $a \neq 1$, $x = 1$. Si $a = 1$, queda $0x = 0$: **todo $x$** es solución.

**Verificación**: a) $x = 0$: $-3 \neq -2$ ✓ (no es solución). b) $a = 1$, $x = 7$: $0 = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Los mismos que el ejercicio pretende detectar.</details>

### F01-N5-01 · [D] Existencia y unicidad para $ax = b$

**Objetivo**: demostrar el caso $a \neq 0$ y justificar los otros dos.
**Dificultad**: N5

**Enunciado.** a) Demuestra que si $a \neq 0$, la ecuación $ax = b$ tiene exactamente una solución. b) Demuestra que si $a = 0$, tiene todas las soluciones o ninguna, según $b$.

<details><summary>Pista 1</summary>"Exactamente una" son dos afirmaciones: hay al menos una (existencia) y no hay dos distintas (unicidad).</details>
<details><summary>Pista 2</summary>Unicidad: supón $ax_1 = b$ y $ax_2 = b$ y resta.</details>
<details><summary>Solución</summary>

a) *Existencia*: $x = \frac ba$ existe porque $a \neq 0$, y $a\cdot\frac ba = b$. *Unicidad*: si $ax_1 = b$ y $ax_2 = b$, restando, $a(x_1 - x_2) = 0$; multiplicando por $\frac1a$, $x_1 - x_2 = 0$, o sea $x_1 = x_2$. $\blacksquare$
b) Si $a = 0$, $ax = 0$ para todo $x$. Entonces la ecuación dice $0 = b$: si $b = 0$, es cierta para todo $x$; si $b \neq 0$, es falsa para todo $x$. $\blacksquare$

**Verificación**: ejemplos $3x = 6$ ($x = 2$), $0x = 0$, $0x = 5$.
</details>
<details><summary>Errores frecuentes</summary>Probar solo la existencia; usar $\frac1a$ sin decir que existe porque $a \neq 0$.</details>
