# F02 — Ecuaciones con varias incógnitas (parte 2)

Segunda parte del banco de las lecciones L07: **20 ejercicios** de práctica que completan la parte 1 (`F02_ecuaciones_varias_incognitas.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N1: 4, N2: 8, N3: 6, N4: 2 · [C] 17, [K] 3.

---

### F02-N1-11 · [C] ¿Es solución?

**Objetivo**: comprobar una solución sustituyendo.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de estos puntos son solución de $3x - 3y = -18$?

$(0, 6)$,  $(-4, 2)$,  $(-7, -1)$,  $(-3, 2)$

<details><summary>Pista 1</summary>Sustituye $x$ e $y$ por las coordenadas y mira si sale el término independiente.</details>
<details><summary>Solución</summary>

$(0, 6)$: $3\cdot 0 + (-3)\cdot 6 = -18$ ✓ es solución.

$(-4, 2)$: $3\cdot (-4) + (-3)\cdot 2 = -18$ ✓ es solución.

$(-7, -1)$: $3\cdot (-7) + (-3)\cdot (-1) = -18$ ✓ es solución.

$(-3, 2)$: $3\cdot (-3) + (-3)\cdot 2 = -15$ ≠ -18: no es solución.

</details>
<details><summary>Errores frecuentes</summary>Sustituir las coordenadas en el orden contrario.</details>

### F02-N1-12 · [C] ¿Es solución?

**Objetivo**: comprobar una solución sustituyendo.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de estos puntos son solución de $x - 2y = -3$?

$(-1, 1)$,  $(3, 3)$,  $(2, 2)$,  $(1, 2)$

<details><summary>Pista 1</summary>Sustituye $x$ e $y$ por las coordenadas y mira si sale el término independiente.</details>
<details><summary>Solución</summary>

$(-1, 1)$: $1\cdot (-1) + (-2)\cdot 1 = -3$ ✓ es solución.

$(3, 3)$: $1\cdot 3 + (-2)\cdot 3 = -3$ ✓ es solución.

$(2, 2)$: $1\cdot 2 + (-2)\cdot 2 = -2$ ≠ -3: no es solución.

$(1, 2)$: $1\cdot 1 + (-2)\cdot 2 = -3$ ✓ es solución.

</details>
<details><summary>Errores frecuentes</summary>Sustituir las coordenadas en el orden contrario.</details>

### F02-N1-13 · [C] ¿Es solución?

**Objetivo**: comprobar una solución sustituyendo.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de estos puntos son solución de $5x - 2y = -12$?

$(0, 6)$,  $(-4, -4)$,  $(-6, -9)$,  $(-3, -4)$

<details><summary>Pista 1</summary>Sustituye $x$ e $y$ por las coordenadas y mira si sale el término independiente.</details>
<details><summary>Solución</summary>

$(0, 6)$: $5\cdot 0 + (-2)\cdot 6 = -12$ ✓ es solución.

$(-4, -4)$: $5\cdot (-4) + (-2)\cdot (-4) = -12$ ✓ es solución.

$(-6, -9)$: $5\cdot (-6) + (-2)\cdot (-9) = -12$ ✓ es solución.

$(-3, -4)$: $5\cdot (-3) + (-2)\cdot (-4) = -7$ ≠ -12: no es solución.

</details>
<details><summary>Errores frecuentes</summary>Sustituir las coordenadas en el orden contrario.</details>

### F02-N1-14 · [C] ¿Es solución?

**Objetivo**: comprobar una solución sustituyendo.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de estos puntos son solución de $3x - 2y = 1$?

$(4, 4)$,  $(5, 7)$,  $(1, 1)$,  $(3, 4)$

<details><summary>Pista 1</summary>Sustituye $x$ e $y$ por las coordenadas y mira si sale el término independiente.</details>
<details><summary>Solución</summary>

$(4, 4)$: $3\cdot 4 + (-2)\cdot 4 = 4$ ≠ 1: no es solución.

$(5, 7)$: $3\cdot 5 + (-2)\cdot 7 = 1$ ✓ es solución.

$(1, 1)$: $3\cdot 1 + (-2)\cdot 1 = 1$ ✓ es solución.

$(3, 4)$: $3\cdot 3 + (-2)\cdot 4 = 1$ ✓ es solución.

</details>
<details><summary>Errores frecuentes</summary>Sustituir las coordenadas en el orden contrario.</details>

### F02-N2-11 · [C] Cortes, pendiente y solución general

**Objetivo**: describir el conjunto de soluciones de una ecuación con dos incógnitas.
**Dificultad**: N2

**Enunciado.** Para la ecuación $4x + y = 12$: a) halla los cortes con los ejes; b) la pendiente; c) escribe todas las soluciones con un parámetro; d) da tres soluciones.

<details><summary>Pista 1</summary>Para el corte con el eje $x$ haz $y = 0$.</details>
<details><summary>Pista 2</summary>Despeja $y$ para ver la pendiente.</details>
<details><summary>Solución</summary>

a) Con $y = 0$: $x = 3$, punto $(3, 0)$. Con $x = 0$: $y = 12$, punto $(0, 12)$.

b) Despejando, $y = -4x + 12$: pendiente $-4$.

c) Con $x = s$ libre: $y = 12 - 4s$; las soluciones son $(s, 12 - 4s)$.

d) Por ejemplo, con $s = 0, 1, 2$: $(0, 12)$, $(1, 8)$, $(2, 4)$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el signo de la pendiente al despejar.</details>

### F02-N2-12 · [C] Cortes, pendiente y solución general

**Objetivo**: describir el conjunto de soluciones de una ecuación con dos incógnitas.
**Dificultad**: N2

**Enunciado.** Para la ecuación $6x - 3y = -54$: a) halla los cortes con los ejes; b) la pendiente; c) escribe todas las soluciones con un parámetro; d) da tres soluciones.

<details><summary>Pista 1</summary>Para el corte con el eje $x$ haz $y = 0$.</details>
<details><summary>Pista 2</summary>Despeja $y$ para ver la pendiente.</details>
<details><summary>Solución</summary>

a) Con $y = 0$: $x = -9$, punto $(-9, 0)$. Con $x = 0$: $y = 18$, punto $(0, 18)$.

b) Despejando, $y = 2x + 18$: pendiente $2$.

c) Con $x = s$ libre: $y = 18 + 2s$; las soluciones son $(s, 18 + 2s)$.

d) Por ejemplo, con $s = 0, 1, 2$: $(0, 18)$, $(1, 20)$, $(2, 22)$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el signo de la pendiente al despejar.</details>

### F02-N2-13 · [C] Cortes, pendiente y solución general

**Objetivo**: describir el conjunto de soluciones de una ecuación con dos incógnitas.
**Dificultad**: N2

**Enunciado.** Para la ecuación $5x - 3y = -30$: a) halla los cortes con los ejes; b) la pendiente; c) escribe todas las soluciones con un parámetro; d) da tres soluciones.

<details><summary>Pista 1</summary>Para el corte con el eje $x$ haz $y = 0$.</details>
<details><summary>Pista 2</summary>Despeja $y$ para ver la pendiente.</details>
<details><summary>Solución</summary>

a) Con $y = 0$: $x = -6$, punto $(-6, 0)$. Con $x = 0$: $y = 10$, punto $(0, 10)$.

b) Despejando, $y = \frac{5}{3}x + 10$: pendiente $\frac{5}{3}$.

c) Con $x = s$ libre: $y = 10 + \frac{5}{3}s$; las soluciones son $(s, 10 + \frac{5}{3}s)$.

d) Por ejemplo, con $s = 0, 1, 2$: $(0, 10)$, $(1, \frac{35}{3})$, $(2, \frac{40}{3})$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el signo de la pendiente al despejar.</details>

### F02-N2-14 · [C] Cortes, pendiente y solución general

**Objetivo**: describir el conjunto de soluciones de una ecuación con dos incógnitas.
**Dificultad**: N2

**Enunciado.** Para la ecuación $3x - 3y = -27$: a) halla los cortes con los ejes; b) la pendiente; c) escribe todas las soluciones con un parámetro; d) da tres soluciones.

<details><summary>Pista 1</summary>Para el corte con el eje $x$ haz $y = 0$.</details>
<details><summary>Pista 2</summary>Despeja $y$ para ver la pendiente.</details>
<details><summary>Solución</summary>

a) Con $y = 0$: $x = -9$, punto $(-9, 0)$. Con $x = 0$: $y = 9$, punto $(0, 9)$.

b) Despejando, $y = 1x + 9$: pendiente $1$.

c) Con $x = s$ libre: $y = 9 + 1s$; las soluciones son $(s, 9 + 1s)$.

d) Por ejemplo, con $s = 0, 1, 2$: $(0, 9)$, $(1, 10)$, $(2, 11)$.

</details>
<details><summary>Errores frecuentes</summary>Confundir el signo de la pendiente al despejar.</details>

### F02-N2-15 · [C] Un plano en el espacio

**Objetivo**: hallar los cortes con los ejes y puntos de un plano.
**Dificultad**: N2

**Enunciado.** Sea el plano $x + 4y + 4z = 32$. Halla sus cortes con los tres ejes y comprueba que el punto $(32, 0, 0)$ le pertenece.

<details><summary>Pista 1</summary>En cada eje, las otras dos coordenadas valen cero.</details>
<details><summary>Solución</summary>

Con $y = z = 0$: $x = 32$. Con $x = z = 0$: $y = 8$. Con $x = y = 0$: $z = 8$. Los cortes son $(32,0,0)$, $(0,8,0)$ y $(0,0,8)$.

Comprobación: $1\cdot 32 + 0 + 0 = 32 = 32$.

</details>
<details><summary>Errores frecuentes</summary>Dividir por un coeficiente equivocado.</details>

### F02-N2-16 · [C] Un plano en el espacio

**Objetivo**: hallar los cortes con los ejes y puntos de un plano.
**Dificultad**: N2

**Enunciado.** Sea el plano $2x + 3y + 4z = 24$. Halla sus cortes con los tres ejes y comprueba que el punto $(12, 0, 0)$ le pertenece.

<details><summary>Pista 1</summary>En cada eje, las otras dos coordenadas valen cero.</details>
<details><summary>Solución</summary>

Con $y = z = 0$: $x = 12$. Con $x = z = 0$: $y = 8$. Con $x = y = 0$: $z = 6$. Los cortes son $(12,0,0)$, $(0,8,0)$ y $(0,0,6)$.

Comprobación: $2\cdot 12 + 0 + 0 = 24 = 24$.

</details>
<details><summary>Errores frecuentes</summary>Dividir por un coeficiente equivocado.</details>

### F02-N2-17 · [C] Un plano en el espacio

**Objetivo**: hallar los cortes con los ejes y puntos de un plano.
**Dificultad**: N2

**Enunciado.** Sea el plano $4x + 2y + z = 8$. Halla sus cortes con los tres ejes y comprueba que el punto $(2, 0, 0)$ le pertenece.

<details><summary>Pista 1</summary>En cada eje, las otras dos coordenadas valen cero.</details>
<details><summary>Solución</summary>

Con $y = z = 0$: $x = 2$. Con $x = z = 0$: $y = 4$. Con $x = y = 0$: $z = 8$. Los cortes son $(2,0,0)$, $(0,4,0)$ y $(0,0,8)$.

Comprobación: $4\cdot 2 + 0 + 0 = 8 = 8$.

</details>
<details><summary>Errores frecuentes</summary>Dividir por un coeficiente equivocado.</details>

### F02-N2-18 · [C] Un plano en el espacio

**Objetivo**: hallar los cortes con los ejes y puntos de un plano.
**Dificultad**: N2

**Enunciado.** Sea el plano $4x + 2y + 3z = 48$. Halla sus cortes con los tres ejes y comprueba que el punto $(12, 0, 0)$ le pertenece.

<details><summary>Pista 1</summary>En cada eje, las otras dos coordenadas valen cero.</details>
<details><summary>Solución</summary>

Con $y = z = 0$: $x = 12$. Con $x = z = 0$: $y = 24$. Con $x = y = 0$: $z = 16$. Los cortes son $(12,0,0)$, $(0,24,0)$ y $(0,0,16)$.

Comprobación: $4\cdot 12 + 0 + 0 = 48 = 48$.

</details>
<details><summary>Errores frecuentes</summary>Dividir por un coeficiente equivocado.</details>

### F02-N3-11 · [C] Un coeficiente desconocido

**Objetivo**: usar un punto dado para hallar un coeficiente.
**Dificultad**: N3

**Enunciado.** Halla $k$ para que el punto $(3, 3)$ sea solución de $4x + ky = -4$.

<details><summary>Pista 1</summary>Sustituye $x = 3$ e $y = 3$ y despeja $k$.</details>
<details><summary>Solución</summary>

Sustituyendo: $4\cdot 3 + k\cdot 3 = -4$, es decir, $12 + 3k = -4$; luego $k = -\frac{16}{3}$.

</details>
<details><summary>Errores frecuentes</summary>Sustituir solo una de las coordenadas.</details>

### F02-N3-12 · [C] Un coeficiente desconocido

**Objetivo**: usar un punto dado para hallar un coeficiente.
**Dificultad**: N3

**Enunciado.** Halla $k$ para que el punto $(-1, 2)$ sea solución de $5x + ky = 6$.

<details><summary>Pista 1</summary>Sustituye $x = -1$ e $y = 2$ y despeja $k$.</details>
<details><summary>Solución</summary>

Sustituyendo: $5\cdot (-1) + k\cdot 2 = 6$, es decir, $-5 + 2k = 6$; luego $k = \frac{11}{2}$.

</details>
<details><summary>Errores frecuentes</summary>Sustituir solo una de las coordenadas.</details>

### F02-N3-13 · [C] Un coeficiente desconocido

**Objetivo**: usar un punto dado para hallar un coeficiente.
**Dificultad**: N3

**Enunciado.** Halla $k$ para que el punto $(-3, 4)$ sea solución de $4x + ky = -7$.

<details><summary>Pista 1</summary>Sustituye $x = -3$ e $y = 4$ y despeja $k$.</details>
<details><summary>Solución</summary>

Sustituyendo: $4\cdot (-3) + k\cdot 4 = -7$, es decir, $-12 + 4k = -7$; luego $k = \frac{5}{4}$.

</details>
<details><summary>Errores frecuentes</summary>Sustituir solo una de las coordenadas.</details>

### F02-N3-14 · [K] Parámetros libres y geometría

**Objetivo**: relacionar incógnitas, ecuaciones independientes y dimensión del conjunto solución.
**Dificultad**: N3

**Enunciado.** Para cada caso indica cuántos parámetros libres tiene el conjunto solución y qué objeto geométrico es:

a) dos ecuaciones independientes con 4 incógnitas.
b) una ecuación con 2 incógnitas.
c) una ecuación con 3 incógnitas.

<details><summary>Pista 1</summary>Cada ecuación independiente quita un grado de libertad.</details>
<details><summary>Solución</summary>

a) 2 parámetros libres: un plano dentro del espacio de 4 dimensiones.

b) 1 parámetro libre: una recta en el plano.

c) 2 parámetros libres: un plano en el espacio.

Regla: parámetros libres $=$ incógnitas $-$ ecuaciones independientes.

</details>
<details><summary>Errores frecuentes</summary>Contar ecuaciones que son combinación de otras.</details>

### F02-N3-15 · [K] Parámetros libres y geometría

**Objetivo**: relacionar incógnitas, ecuaciones independientes y dimensión del conjunto solución.
**Dificultad**: N3

**Enunciado.** Para cada caso indica cuántos parámetros libres tiene el conjunto solución y qué objeto geométrico es:

a) una ecuación con 4 incógnitas.
b) una ecuación con 2 incógnitas.
c) dos ecuaciones independientes con 4 incógnitas.

<details><summary>Pista 1</summary>Cada ecuación independiente quita un grado de libertad.</details>
<details><summary>Solución</summary>

a) 3 parámetros libres: un «hiperplano» de dimensión 3 (no se puede dibujar).

b) 1 parámetro libre: una recta en el plano.

c) 2 parámetros libres: un plano dentro del espacio de 4 dimensiones.

Regla: parámetros libres $=$ incógnitas $-$ ecuaciones independientes.

</details>
<details><summary>Errores frecuentes</summary>Contar ecuaciones que son combinación de otras.</details>

### F02-N3-16 · [K] Parámetros libres y geometría

**Objetivo**: relacionar incógnitas, ecuaciones independientes y dimensión del conjunto solución.
**Dificultad**: N3

**Enunciado.** Para cada caso indica cuántos parámetros libres tiene el conjunto solución y qué objeto geométrico es:

a) tres ecuaciones independientes con 3 incógnitas.
b) dos ecuaciones independientes con 4 incógnitas.
c) dos ecuaciones independientes con 3 incógnitas.

<details><summary>Pista 1</summary>Cada ecuación independiente quita un grado de libertad.</details>
<details><summary>Solución</summary>

a) 0 parámetros libres: un único punto.

b) 2 parámetros libres: un plano dentro del espacio de 4 dimensiones.

c) 1 parámetro libre: una recta en el espacio.

Regla: parámetros libres $=$ incógnitas $-$ ecuaciones independientes.

</details>
<details><summary>Errores frecuentes</summary>Contar ecuaciones que son combinación de otras.</details>

### F02-N4-11 · [C] Solución general con dos parámetros

**Objetivo**: describir un plano con dos parámetros y hallar una solución concreta.
**Dificultad**: N4

**Enunciado.** Escribe la solución general de $2x - 2y - 3z = 6$ con dos parámetros y halla la solución con $y = -2$, $z = 2$.

<details><summary>Pista 1</summary>Despeja $x$ y deja $y$, $z$ libres.</details>
<details><summary>Solución</summary>

Con $y = s$, $z = u$ libres: $x = 3 + s + \frac{3}{2}u$. Con $s = -2$, $u = 2$ sale $x = 4$; la solución es $(4, -2, 2)$. Comprobación: $2\cdot 4 + (-2)\cdot (-2) + (-3)\cdot 2 = 6$.

</details>
<details><summary>Errores frecuentes</summary>Dar solo un parámetro cuando hay dos libres.</details>

### F02-N4-12 · [C] Solución general con dos parámetros

**Objetivo**: describir un plano con dos parámetros y hallar una solución concreta.
**Dificultad**: N4

**Enunciado.** Escribe la solución general de $2x - 3y - 3z = 6$ con dos parámetros y halla la solución con $y = 2$, $z = 1$.

<details><summary>Pista 1</summary>Despeja $x$ y deja $y$, $z$ libres.</details>
<details><summary>Solución</summary>

Con $y = s$, $z = u$ libres: $x = 3 + \frac{3}{2}s + \frac{3}{2}u$. Con $s = 2$, $u = 1$ sale $x = \frac{15}{2}$; la solución es $(\frac{15}{2}, 2, 1)$. Comprobación: $2\cdot (\frac{15}{2}) + (-3)\cdot 2 + (-3)\cdot 1 = 6$.

</details>
<details><summary>Errores frecuentes</summary>Dar solo un parámetro cuando hay dos libres.</details>

