# F02 — Ecuaciones con dos y tres incógnitas: rectas, planos y parámetros

Banco de la lección L07. **Parte 1: 10 ejercicios**, ligados a los videos. La **parte 2** (20 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F02_ecuaciones_varias_incognitas_parte2.md`; la familia completa suma **30**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Resultados comprobados en `ejercicios/verificar/f01_f03.py`.

| Video | Ejercicio |
|---|---|
| InfinitasSolucionesDeUnaEcuacion | N1-01 🎬 |
| EcuacionComoRecta | N2-01 🎬 |
| EcuacionComoPlano | N2-02 🎬 |
| ParametrizarUnaRecta | N3-01 🎬 |
| (adicionales) | N1-02, N2-03, N3-02, N4-01, N4-02, N5-01 |

---

### F02-N1-01 · [C] Cuatro soluciones 🎬

**Objetivo**: generar soluciones eligiendo una incógnita y despejando la otra.
**Dificultad**: N1

**Enunciado.** Encuentra cuatro soluciones de $3x - y = 6$, una de ellas con $x = \frac13$.

<details><summary>Pista 1</summary>Despeja $y = 3x - 6$.</details>
<details><summary>Pista 2</summary>Da a $x$ los valores que quieras.</details>
<details><summary>Solución</summary>

Por ejemplo: $(0, -6)$, $(2, 0)$, $(1, -3)$ y $\left(\frac13, -5\right)$.

**Verificación**: $0 + 6 = 6$; $6 - 0 = 6$; $3 + 3 = 6$; $1 + 5 = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$y = 6 - 3x$ (signo cambiado al despejar).</details>

### F02-N1-02 · [C] ¿Está en la recta?

**Objetivo**: decidir por sustitución si un punto está en la recta.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de $(3, 2)$, $(0, 4)$, $(6, -1)$, $(-3, 6)$ están en la recta $2x + 3y = 12$?

<details><summary>Pista 1</summary>Sustituye y compara con 12.</details>
<details><summary>Pista 2</summary>$2(-3) + 3(6) = -6 + 18$.</details>
<details><summary>Solución</summary>

$(3, 2)$: $12$ ✓. $(0, 4)$: $12$ ✓. $(6, -1)$: $9$ ✗. $(-3, 6)$: $12$ ✓.

**Verificación**: comprobado en `verificar/f01_f03.py`.
</details>
<details><summary>Errores frecuentes</summary>Intercambiar las coordenadas al sustituir.</details>

### F02-N2-01 · [C] Rectas por sus cortes 🎬

**Objetivo**: dibujar rectas con los cortes y reconocer verticales y horizontales.
**Dificultad**: N2

**Enunciado.** Dibuja usando los cortes con los ejes: a) $x - 2y = 4$ b) $3y = 6$ c) $x = -1$. ¿Cuál no corta al eje $x$? ¿Cuál no corta al eje $y$?

<details><summary>Pista 1</summary>Corte con el eje $x$: $y = 0$. Corte con el eje $y$: $x = 0$.</details>
<details><summary>Pista 2</summary>b) es $0x + 3y = 6$: ¿qué pasa al poner $y = 0$?</details>
<details><summary>Solución</summary>

a) Cortes $(4, 0)$ y $(0, -2)$.
b) $y = 2$: recta horizontal; corta al eje $y$ en $(0, 2)$ y **no corta al eje $x$** (con $y = 0$ queda $0 = 6$).
c) Recta vertical; corta al eje $x$ en $(-1, 0)$ y **no corta al eje $y$** (con $x = 0$ queda $0 = -1$).

**Verificación**: $4 - 0 = 4$ y $0 + 4 = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dibujar $y = 2$ como vertical.</details>

### F02-N2-02 · [C] Cortes de un plano 🎬

**Objetivo**: hallar puntos de un plano.
**Dificultad**: N2

**Enunciado.** Halla los cortes con los ejes del plano $2x + 3y + 6z = 12$ y otros tres puntos del plano.

<details><summary>Pista 1</summary>En el eje $x$, $y = z = 0$.</details>
<details><summary>Pista 2</summary>Para otros puntos, elige $y$ y $z$ y despeja $x$.</details>
<details><summary>Solución</summary>

Cortes: $(6, 0, 0)$, $(0, 4, 0)$, $(0, 0, 2)$. Otros: $(3, 2, 0)$, $(0, 2, 1)$, $(3, 0, 1)$.

**Verificación**: $6 + 6 = 12$ en los tres últimos ✓.
</details>
<details><summary>Errores frecuentes</summary>Dividir mal: $6z = 12 \Rightarrow z = 2$, no $z = 6$.</details>

### F02-N2-03 · [K] ¿La misma recta?

**Objetivo**: reconocer ecuaciones proporcionales.
**Dificultad**: N2

**Enunciado.** ¿Representan la misma recta? a) $3x - 6y = 9$ y $x - 2y = 3$ b) $2x + 4y = 8$ y $x + 2y = 3$ c) $-x + y = 1$ y $2x - 2y = -2$

<details><summary>Pista 1</summary>Busca un número $k \neq 0$ tal que una ecuación sea $k$ veces la otra (los tres números).</details>
<details><summary>Pista 2</summary>Si los coeficientes son proporcionales pero el término independiente no, son paralelas.</details>
<details><summary>Solución</summary>

a) Sí ($k = 3$). b) No: $(2, 4) = 2(1, 2)$ pero $8 \neq 2\cdot 3$: paralelas. c) Sí ($k = -2$).

**Verificación**: $(3, 0)$ está en ambas de a); $(-1, 0)$ en ambas de c).
</details>
<details><summary>Errores frecuentes</summary>Comparar solo los coeficientes y olvidar el término independiente.</details>

### F02-N3-01 · [C] Dos parametrizaciones 🎬

**Objetivo**: parametrizar de dos maneras y comprobar que describen lo mismo.
**Dificultad**: N3

**Enunciado.** Parametriza las soluciones de $2x - 3y = 6$ tomando $x$ como parámetro y tomando $y$ como parámetro. Comprueba que $(3, 0)$ aparece en ambas.

<details><summary>Pista 1</summary>Con $x = t$, despeja $y$.</details>
<details><summary>Pista 2</summary>Con $y = s$, despeja $x$.</details>
<details><summary>Solución</summary>

$x = t$: $(t, \frac{2t - 6}{3})$. $y = s$: $(\frac{6 + 3s}{2}, s)$. El punto $(3, 0)$ sale con $t = 3$ y con $s = 0$.

**Verificación**: sustituyendo la primera: $2t - (2t - 6) = 6$ ✓; la segunda: $(6 + 3s) - 3s = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Escribir $y = \frac{6 - 2t}{3}$ (signo).</details>

### F02-N3-02 · [C] Parametrizar un plano

**Objetivo**: usar dos parámetros.
**Dificultad**: N3

**Enunciado.** Parametriza las soluciones de $x - y + 2z = 5$ y da tres soluciones concretas.

<details><summary>Pista 1</summary>Despeja la incógnita de coeficiente más sencillo: $x$.</details>
<details><summary>Pista 2</summary>$y = s$, $z = t$.</details>
<details><summary>Solución</summary>

$(x, y, z) = (5 + s - 2t,\ s,\ t)$. Por ejemplo $(5, 0, 0)$, $(6, 1, 0)$, $(3, 0, 1)$.

**Verificación**: $(5 + s - 2t) - s + 2t = 5$ ✓ para todos $s, t$.
</details>
<details><summary>Errores frecuentes</summary>Usar un solo parámetro (eso describiría solo una recta dentro del plano).</details>

### F02-N4-01 · [K] El mismo dibujo en distintas dimensiones

**Objetivo**: entender que el conjunto solución depende de cuántas incógnitas hay.
**Dificultad**: N4

**Enunciado.** Describe el conjunto de soluciones en $\mathbb{R}^2$ (incógnitas $x, y$) y en $\mathbb{R}^3$ (incógnitas $x, y, z$) de: a) $x = 3$ b) $0x + 0y = 0$ c) $0x + 0y = 2$.

<details><summary>Pista 1</summary>Una incógnita que no aparece es libre.</details>
<details><summary>Pista 2</summary>Piensa cuántas incógnitas libres quedan en cada caso.</details>
<details><summary>Solución</summary>

a) En $\mathbb{R}^2$: recta vertical $\{(3, t)\}$. En $\mathbb{R}^3$: plano $\{(3, s, t)\}$.
b) Todo $\mathbb{R}^2$; todo $\mathbb{R}^3$.
c) Vacío en ambos casos.

**Verificación**: $(3, 7)$ y $(3, 7, -1)$ cumplen a).
</details>
<details><summary>Errores frecuentes</summary>Decir que $x = 3$ "es un punto" sin mirar cuántas incógnitas hay.</details>

### F02-N4-02 · [K] Una parametrización mal hecha

**Objetivo**: verificar una parametrización sustituyéndola.
**Dificultad**: N4

**Enunciado.** Un estudiante dice que las soluciones de $x + 2y = 4$ son $(t, 2 - t)$. ¿Tiene razón?

<details><summary>Pista 1</summary>Sustituye $x = t$, $y = 2 - t$ en la ecuación.</details>
<details><summary>Pista 2</summary>¿Sale 4 para todo $t$?</details>
<details><summary>Solución</summary>

$t + 2(2 - t) = 4 - t$, que vale 4 solo si $t = 0$. **No**. Correcto: $(t, \frac{4 - t}{2})$ o $(4 - 2t, t)$.

**Verificación**: $t = 2$ da $(2, 0)$ con la fórmula del estudiante: $2 + 0 = 2 \neq 4$.
</details>
<details><summary>Errores frecuentes</summary>No verificar las parametrizaciones.</details>

### F02-N5-01 · [D] Todas las soluciones y solo ellas

**Objetivo**: demostrar que una parametrización describe exactamente el conjunto solución.
**Dificultad**: N5

**Enunciado.** Sea $a \neq 0$. Demuestra que las soluciones de $ax + by = c$ son exactamente los pares $\left(\frac{c - bt}{a},\ t\right)$ con $t$ real, y que valores distintos de $t$ dan soluciones distintas.

<details><summary>Pista 1</summary>Hay que probar dos inclusiones: todo par de esa forma es solución, y toda solución es de esa forma.</details>
<details><summary>Pista 2</summary>Para la segunda, dada una solución $(x_0, y_0)$, toma $t = y_0$.</details>
<details><summary>Solución</summary>

*Son soluciones*: $a\cdot\frac{c - bt}{a} + bt = c - bt + bt = c$.
*Son todas*: si $(x_0, y_0)$ es solución, $ax_0 = c - by_0$, y como $a \neq 0$, $x_0 = \frac{c - by_0}{a}$: es el par con $t = y_0$.
*Distintas*: la segunda coordenada es $t$; si $t \neq s$, los pares son distintos. Hay, por tanto, infinitas soluciones. $\blacksquare$

**Verificación** (ejemplo): $2x + 3y = 6$, $t = 0$: $(3, 0)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Probar solo que los pares son soluciones (falta "son todas").</details>
