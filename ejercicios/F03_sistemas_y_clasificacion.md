# F03 — Sistemas: geometría, notación general, homogéneos y clasificación

Banco de las lecciones L08–L12. **Parte 1: 19 ejercicios**, ligados a los videos. La **parte 2** (21 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F03_sistemas_y_clasificacion_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Resultados comprobados en `ejercicios/verificar/f01_f03.py`.
- Todavía no se han visto métodos de resolución (Lecciones 13–15): los ejercicios se resuelven comprobando, combinando ecuaciones o razonando con la geometría.

| Lección | Ejercicios |
|---|---|
| L08 Sistemas 2×2 | N1-01 🎬, N2-01 🎬, N2-02 🎬, N3-01 🎬, N2-05, N3-04 |
| L09 Sistemas 3×3 | N1-02 🎬, N2-03 🎬, N4-01 🎬 |
| L10 m×n y homogéneos | N1-03 🎬, N1-04, N3-02 🎬, N2-04 🎬, N5-02 |
| L11 Clasificación | N3-03 🎬, N5-01 🎬 |
| L12 Casos especiales | N4-02 🎬, N4-03 🎬, N4-04 🎬 |

---

## Lección 8 — Sistemas 2×2

### F03-N1-01 · [C] ¿Cuáles son solución? 🎬

**Objetivo**: entender que una solución debe cumplir todas las ecuaciones.
**Dificultad**: N1

**Enunciado.** ¿Cuáles de $(1, 2)$, $(2, 0)$ y $(4, 3)$ son solución del sistema $2x + y = 4$, $x - 3y = -5$?

<details><summary>Pista 1</summary>Sustituye cada par en <b>las dos</b> ecuaciones.</details>
<details><summary>Pista 2</summary>Basta que falle una ecuación para descartar el par.</details>
<details><summary>Solución</summary>

| Par | $2x + y$ | $x - 3y$ | ¿Solución? |
|---|---|---|---|
| $(1, 2)$ | $4$ ✓ | $-5$ ✓ | **sí** |
| $(2, 0)$ | $4$ ✓ | $2$ ✗ | no |
| $(4, 3)$ | $11$ ✗ | $-5$ ✓ | no |

**Verificación**: comprobado en `verificar/f01_f03.py`.
</details>
<details><summary>Errores frecuentes</summary>Aceptar $(2, 0)$ porque cumple la primera.</details>

### F03-N2-01 · [C] ¿Un único punto? 🎬

**Objetivo**: usar el criterio de proporcionalidad y hallar un punto de corte.
**Dificultad**: N2

**Enunciado.** Sin resolver, ¿se cortan en un único punto? a) $3x - 2y = 1$, $6x - 4y = 5$ b) $x + 4y = 2$, $2x - y = 7$. En b), halla el punto y verifícalo.

<details><summary>Pista 1</summary>¿Es $(a_2, b_2)$ un múltiplo de $(a_1, b_1)$?</details>
<details><summary>Pista 2</summary>b) De la primera, $x = 2 - 4y$; sustitúyelo en la segunda.</details>
<details><summary>Solución</summary>

a) $(6, -4) = 2(3, -2)$: proporcionales, **no** hay punto único. Además $5 \neq 2\cdot 1$: son paralelas, sin solución.
b) $(1, 4)$ y $(2, -1)$ no son proporcionales: **un único punto**. $2(2 - 4y) - y = 7 \Rightarrow 4 - 9y = 7 \Rightarrow y = -\frac13$, $x = 2 + \frac43 = \frac{10}{3}$.

**Verificación**: $\frac{10}{3} - \frac43 = 2$ ✓; $\frac{20}{3} + \frac13 = 7$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Concluir en a) "infinitas" sin mirar el término independiente.</details>

### F03-N2-02 · [C] Paralelas o coincidentes según c 🎬

**Objetivo**: estudiar un parámetro en el término independiente.
**Dificultad**: N2

**Enunciado.** ¿Para qué $c$ no tiene solución el sistema $x - 2y = 3$, $-2x + 4y = c$? ¿Para cuáles tiene infinitas?

<details><summary>Pista 1</summary>$(-2, 4) = -2\cdot(1, -2)$.</details>
<details><summary>Pista 2</summary>¿Cuánto debería valer $c$ para que la 2.ª sea exactamente $-2$ veces la 1.ª?</details>
<details><summary>Solución</summary>

Los coeficientes son proporcionales ($k = -2$). Si $c = -2\cdot 3 = -6$, la segunda ecuación es la primera multiplicada por $-2$: **infinitas** soluciones, $(3 + 2t, t)$. Si $c \neq -6$: rectas paralelas, **ninguna**. Nunca hay solución única.

**Verificación**: $c = -6$, $t = 1$: $(5, 1)$: $5 - 2 = 3$ ✓, $-10 + 4 = -6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Escribir $c = 6$ (olvidar el signo de $k$).</details>

### F03-N3-01 · [K] Diseñar sistemas 🎬

**Objetivo**: construir ejemplos de cada caso.
**Dificultad**: N3

**Enunciado.** Escribe un sistema 2×2 que tenga: a) solución única $(2, -1)$ b) ninguna solución c) infinitas soluciones, todas cumpliendo $x + y = 3$.

<details><summary>Pista 1</summary>a) Elige coeficientes cualesquiera (no proporcionales) y calcula los términos independientes sustituyendo $(2, -1)$.</details>
<details><summary>Pista 2</summary>b) Coeficientes proporcionales, términos independientes no. c) Todo proporcional.</details>
<details><summary>Solución</summary>

Hay muchas respuestas. Por ejemplo: a) $x + y = 1$, $x - y = 3$. b) $x + y = 1$, $x + y = 2$. c) $x + y = 3$, $2x + 2y = 6$.

**Verificación**: a) $2 - 1 = 1$ ✓, $2 + 1 = 3$ ✓, y $(1, 1)$, $(1, -1)$ no son proporcionales.
</details>
<details><summary>Errores frecuentes</summary>En a), elegir coeficientes proporcionales (no habría solución única).</details>

### F03-N2-05 · [C] Resolver dibujando

**Objetivo**: usar la geometría como intuición y la sustitución como confirmación.
**Dificultad**: N2

**Enunciado.** Dibuja $x + y = 4$ y $x - y = 2$, lee el punto de corte y verifícalo.

<details><summary>Pista 1</summary>Cortes de la 1.ª: $(4, 0)$, $(0, 4)$. De la 2.ª: $(2, 0)$, $(0, -2)$.</details>
<details><summary>Pista 2</summary>El dibujo sugiere; la sustitución confirma.</details>
<details><summary>Solución</summary>

El corte es $(3, 1)$.

**Verificación**: $3 + 1 = 4$ ✓, $3 - 1 = 2$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Confiar en un dibujo impreciso sin verificar.</details>

### F03-N3-04 · [K] Elegir el parámetro

**Objetivo**: clasificar un sistema con parámetro mediante la proporcionalidad.
**Dificultad**: N3

**Enunciado.** Sistema: $x + ay = 2$, $2x + 6y = 4$. ¿Para qué $a$ hay infinitas soluciones? ¿Puede no tener solución?

<details><summary>Pista 1</summary>¿Cuándo es $(2, 6)$ múltiplo de $(1, a)$?</details>
<details><summary>Pista 2</summary>Compara también $4$ con $2\cdot 2$.</details>
<details><summary>Solución</summary>

$(2, 6) = 2(1, a) \Leftrightarrow a = 3$. Y $4 = 2\cdot 2$ siempre. Si $a = 3$: **infinitas** (la 2.ª es el doble de la 1.ª). Si $a \neq 3$: coeficientes no proporcionales, **solución única**. **Nunca** es incompatible.

**Verificación**: para cualquier $a$, $(2, 0)$ cumple ambas ($2 = 2$, $4 = 4$): por eso nunca puede ser incompatible.
</details>
<details><summary>Errores frecuentes</summary>Olvidar comprobar los términos independientes.</details>

---

## Lección 9 — Sistemas 3×3

### F03-N1-02 · [C] Verificar en tres ecuaciones 🎬

**Objetivo**: verificar ternas.
**Dificultad**: N1

**Enunciado.** Comprueba que $(2, -1, 3)$ es solución de $x + y + z = 4$, $2x - y + z = 8$, $x + 3y - z = -4$, y que $(1, 0, 3)$ no lo es.

<details><summary>Pista 1</summary>Sustituye en las tres ecuaciones.</details>
<details><summary>Pista 2</summary>Para descartar una terna basta una ecuación que falle.</details>
<details><summary>Solución</summary>

$(2, -1, 3)$: $4$ ✓, $4 + 1 + 3 = 8$ ✓, $2 - 3 - 3 = -4$ ✓.
$(1, 0, 3)$: $4$ ✓, pero $2 + 0 + 3 = 5 \neq 8$ ✗.

**Verificación**: comprobado en `verificar/f01_f03.py`.
</details>
<details><summary>Errores frecuentes</summary>Detenerse tras comprobar la primera ecuación.</details>

### F03-N2-03 · [C] Una recta de soluciones 🎬

**Objetivo**: comprobar una familia de soluciones y reconocer una ecuación redundante.
**Dificultad**: N2

**Enunciado.** Comprueba que todos los puntos $(1 + t,\ 2 - t,\ t)$ son solución de $x + y = 3$, $y + z = 2$, $x - z = 1$. ¿Qué ecuación es combinación de las otras dos?

<details><summary>Pista 1</summary>Sustituye y simplifica: la $t$ debe desaparecer.</details>
<details><summary>Pista 2</summary>Prueba a restar las dos primeras.</details>
<details><summary>Solución</summary>

$(1 + t) + (2 - t) = 3$ ✓, $(2 - t) + t = 2$ ✓, $(1 + t) - t = 1$ ✓. La tercera es la primera menos la segunda: $(x + y) - (y + z) = 3 - 2$.

**Verificación**: $t = 5$: $(6, -3, 5)$: $3$ ✓, $2$ ✓, $1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Comprobar solo para un valor de $t$ y decir "para todos".</details>

### F03-N4-01 · [C] Demostrar que no hay solución 🎬

**Objetivo**: detectar una contradicción combinando ecuaciones.
**Dificultad**: N4

**Enunciado.** Demuestra, sumando ecuaciones, que $x + 2y - z = 1$, $2x - y + z = 3$, $3x + y = 5$ no tiene solución.

<details><summary>Pista 1</summary>Suma las dos primeras: ¿qué le pasa a $z$?</details>
<details><summary>Pista 2</summary>Compara el resultado con la tercera.</details>
<details><summary>Solución</summary>

Si $(x, y, z)$ fuese solución, sumando las dos primeras: $3x + y = 4$. Pero la tercera exige $3x + y = 5$: entonces $4 = 5$, contradicción. No hay solución (SI). $\blacksquare$

**Verificación**: la suma de los lados izquierdos es $(x + 2y - z) + (2x - y + z) = 3x + y$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Intentar "dibujar" para concluir (no demuestra nada).</details>

---

## Lección 10 — Sistemas m × n y homogéneos

### F03-N1-03 · [C] Leer la notación general 🎬

**Objetivo**: identificar $m$, $n$, $a_{ij}$ y $b_i$.
**Dificultad**: N1

**Enunciado.** Sistema: $2x_1 - x_2 + 4x_3 - x_4 = 1$; $x_1 + 5x_3 = 0$; $-x_2 + x_3 + 2x_4 = 6$. a) $m$ y $n$. b) $a_{13}$, $a_{22}$, $a_{34}$, $a_{31}$, $b_3$. c) ¿Es $(5, 1, -1, 4)$ solución?

<details><summary>Pista 1</summary>$a_{ij}$: ecuación $i$, incógnita $x_j$. Si $x_j$ no aparece en la ecuación $i$, $a_{ij} = 0$.</details>
<details><summary>Pista 2</summary>c) Sustituye en las tres.</details>
<details><summary>Solución</summary>

a) $m = 3$, $n = 4$. b) $a_{13} = 4$, $a_{22} = 0$, $a_{34} = 2$, $a_{31} = 0$, $b_3 = 6$.
c) $10 - 1 - 4 - 4 = 1$ ✓; $5 - 5 = 0$ ✓; $-1 - 1 + 8 = 6$ ✓: **sí**.

**Verificación**: comprobado en `verificar/f01_f03.py`.
</details>
<details><summary>Errores frecuentes</summary>Contar $n = 3$ en la segunda ecuación (las incógnitas son las del sistema, no las de cada ecuación).</details>

### F03-N1-04 · [K] Clasificar por su forma

**Objetivo**: reconocer dimensiones y homogeneidad.
**Dificultad**: N1

**Enunciado.** Para cada sistema, da $m \times n$ y di si es homogéneo: a) $x - y = 0$, $3x + y = 0$ b) $x + y + z = 1$ c) $2x = 0$, $x + y = 0$, $y - z = 2$.

<details><summary>Pista 1</summary>Homogéneo: todos los términos independientes son 0.</details>
<details><summary>Pista 2</summary>$n$ cuenta todas las incógnitas que aparecen en el sistema.</details>
<details><summary>Solución</summary>

a) $2\times 2$, homogéneo. b) $1\times 3$, no homogéneo. c) $3\times 3$, no homogéneo (la tercera tiene $b_3 = 2$).

**Verificación**: a) $(0, 0)$ es solución, como corresponde a un homogéneo.
</details>
<details><summary>Errores frecuentes</summary>Decir que c) es homogéneo porque "casi todos" los términos son 0.</details>

### F03-N3-02 · [K] Contar parámetros 🎬

**Objetivo**: relacionar número de incógnitas y libertad.
**Dificultad**: N3

**Enunciado.** ¿Cuántos parámetros necesitan las soluciones de: a) $2x - y + z - 3w = 5$ b) $x_1 + \dots + x_{10} = 1$ c) $0x + 0y + 0z = 0$ d) $0x + 0y = 3$?

<details><summary>Pista 1</summary>Una ecuación no degenerada con $n$ incógnitas deja $n - 1$ libres.</details>
<details><summary>Pista 2</summary>c) y d) son degeneradas.</details>
<details><summary>Solución</summary>

a) 3. b) 9. c) 3 (todo $\mathbb{R}^3$: las tres incógnitas son libres). d) Ninguno: no hay soluciones.

**Verificación**: a) con $y = s$, $z = t$, $w = u$: $x = \frac{5 + s - t + 3u}{2}$.
</details>
<details><summary>Errores frecuentes</summary>Responder "2" en c) por analogía con un plano.</details>

### F03-N2-04 · [C] Un homogéneo 🎬

**Objetivo**: usar la estructura de las soluciones de un homogéneo.
**Dificultad**: N2

**Enunciado.** Sistema homogéneo: $x + y - z = 0$, $2x + 3y - z = 0$. a) Comprueba que $(2, -1, 1)$ es solución. b) Sin cuentas nuevas, da otras dos soluciones. c) ¿Puede ser incompatible?

<details><summary>Pista 1</summary>En un homogéneo, los múltiplos de una solución son soluciones.</details>
<details><summary>Pista 2</summary>c) ¿Qué pasa con $(0, 0, 0)$?</details>
<details><summary>Solución</summary>

a) $2 - 1 - 1 = 0$ ✓; $4 - 3 - 1 = 0$ ✓. b) $(0, 0, 0)$, $(4, -2, 2)$, $(-2, 1, -1)$ (múltiplos). c) No: $(0, 0, 0)$ siempre es solución.

**Verificación**: $(4, -2, 2)$: $4 - 2 - 2 = 0$ ✓; $8 - 6 - 2 = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Sumar soluciones en un sistema NO homogéneo (allí no funciona).</details>

### F03-N5-02 · [D] Una solución no trivial da infinitas

**Objetivo**: demostrar una propiedad de los homogéneos.
**Dificultad**: N5

**Enunciado.** Demuestra que si un sistema homogéneo tiene una solución $u \neq (0, \dots, 0)$, entonces tiene infinitas.

<details><summary>Pista 1</summary>Prueba que $t\,u$ es solución para todo real $t$.</details>
<details><summary>Pista 2</summary>¿Por qué $t\,u \neq s\,u$ si $t \neq s$?</details>
<details><summary>Solución</summary>

Para cada ecuación $i$: $\sum_j a_{ij}(t u_j) = t\sum_j a_{ij} u_j = t\cdot 0 = 0$. Así $t\,u$ es solución para todo $t$. Si $t \neq s$, $t\,u - s\,u = (t - s)u \neq 0$ porque $u$ tiene alguna componente no nula. Hay una solución distinta por cada real $t$. $\blacksquare$

**Verificación** (ejemplo): $x + 2y = 0$, $u = (-2, 1)$: $3u = (-6, 3)$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar justificar que las soluciones obtenidas son distintas.</details>

---

## Lección 11 — Clasificación

### F03-N3-03 · [K] SCD, SCI o SI 🎬

**Objetivo**: clasificar razonando.
**Dificultad**: N3

**Enunciado.** Clasifica: a) $x - y = 1$, $2x - 2y = 2$ b) $x + y = 1$, $x + y = 0$ c) $x = 2$, $y = -1$ d) $x + y + z = 0$, $x - y = 0$.

<details><summary>Pista 1</summary>a) y b): compara las ecuaciones (¿proporcionales?).</details>
<details><summary>Pista 2</summary>d) es homogéneo con menos ecuaciones que incógnitas: busca una incógnita libre.</details>
<details><summary>Solución</summary>

a) SCI (la 2.ª es el doble de la 1.ª). b) SI ($1 = 0$). c) SCD, solución $(2, -1)$. d) De la 2.ª, $x = y$; en la 1.ª, $z = -2x$: soluciones $(t, t, -2t)$: SCI.

**Verificación**: d) $t = 1$: $(1, 1, -2)$: $0$ ✓, $0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Llamar SI a d) "porque hay menos ecuaciones".</details>

### F03-N5-01 · [D] Nunca exactamente dos 🎬

**Objetivo**: aplicar y entender la demostración de la Lección 11.
**Dificultad**: N5

**Enunciado.** a) Un sistema lineal tiene las soluciones $(1, 2)$ y $(3, -2)$. Da otras tres. b) Demuestra que si $p$ y $q$ son soluciones de un sistema homogéneo, $p - q$ también lo es. c) Muestra que el argumento de la lección falla para $x^2 + y^2 = 1$ con $(1, 0)$ y $(0, 1)$.

<details><summary>Pista 1</summary>a) $r(t) = (1 - t)p + tq = p + t(q - p)$.</details>
<details><summary>Pista 2</summary>c) Mira el punto medio ($t = \frac12$).</details>
<details><summary>Solución</summary>

a) $q - p = (2, -4)$. $t = 2$: $(5, -6)$; $t = -1$: $(-1, 6)$; $t = \frac12$: $(2, 0)$.
b) $\sum_j a_{ij}(p_j - q_j) = \sum_j a_{ij}p_j - \sum_j a_{ij}q_j = 0 - 0 = 0$. $\blacksquare$
c) $\left(\frac12, \frac12\right)$: $\frac14 + \frac14 = \frac12 \neq 1$: el punto medio no es solución.

**Verificación**: a) un sistema concreto con esas soluciones es $2x + y = 4$: $(5, -6)$, $(-1, 6)$ y $(2, 0)$ dan $4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>a) Calcular $p + q$ en vez de puntos de la recta que pasa por $p$ y $q$.</details>

---

## Lección 12 — Casos especiales

### F03-N4-02 · [C] Tres ecuaciones, dos incógnitas 🎬

**Objetivo**: resolver con dos ecuaciones y comprobar la tercera.
**Dificultad**: N4

**Enunciado.** ¿Para qué $k$ es compatible $x + 2y = 5$, $3x - y = 1$, $2x + 3y = k$? ¿Cuál es entonces la solución?

<details><summary>Pista 1</summary>Resuelve las dos primeras: $y = 3x - 1$.</details>
<details><summary>Pista 2</summary>Sustituye la solución en la tercera.</details>
<details><summary>Solución</summary>

$x + 2(3x - 1) = 5 \Rightarrow 7x = 7 \Rightarrow x = 1$, $y = 2$. La tercera da $2 + 6 = 8$. Compatible (SCD) solo si $k = 8$, con solución $(1, 2)$; si $k \neq 8$, SI.

**Verificación**: $1 + 4 = 5$ ✓, $3 - 2 = 1$ ✓, $2 + 6 = 8$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Decir que es incompatible "porque hay más ecuaciones que incógnitas".</details>

### F03-N4-03 · [C] Dos ecuaciones, tres incógnitas 🎬

**Objetivo**: estudiar planos paralelos o coincidentes.
**Dificultad**: N4

**Enunciado.** $x + y - z = 2$, $2x + 2y - 2z = c$. ¿Para qué $c$ es compatible? Describe entonces las soluciones.

<details><summary>Pista 1</summary>Los coeficientes de la 2.ª son el doble de los de la 1.ª.</details>
<details><summary>Pista 2</summary>Si la 2.ª es exactamente el doble, sobra.</details>
<details><summary>Solución</summary>

Si $c = 4$, la 2.ª es el doble de la 1.ª: queda un plano, $(2 - s + t,\ s,\ t)$, SCI con dos parámetros. Si $c \neq 4$: planos paralelos, SI.

**Verificación**: $c = 4$, $s = t = 1$: $(2, 1, 1)$: $2 + 1 - 1 = 2$ ✓, $4 + 2 - 2 = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Usar un solo parámetro (con una ecuación efectiva y tres incógnitas quedan dos libres).</details>

### F03-N4-04 · [K] Verdadero o falso 🎬

**Objetivo**: no confundir la forma del sistema con su clasificación.
**Dificultad**: N4

**Enunciado.** ¿Verdadero o falso? Da ejemplo o contraejemplo. a) Un sistema 3×3 siempre tiene solución. b) Si un sistema lineal tiene dos soluciones distintas, tiene infinitas. c) Si un sistema tiene solución única, al quitarle una ecuación puede seguir teniéndola.

<details><summary>Pista 1</summary>a) Piensa en dos planos paralelos.</details>
<details><summary>Pista 2</summary>c) Piensa en tres rectas que pasan por el mismo punto.</details>
<details><summary>Solución</summary>

a) **Falso**: $x + y + z = 1$, $x + y + z = 2$, $x - y = 0$ no tiene solución.
b) **Verdadero** (teorema de la Lección 11).
c) **Verdadero**: $x + y = 2$, $x - y = 0$, $2x + y = 3$ tiene la única solución $(1, 1)$; sin la tercera, sigue siendo $(1, 1)$.

**Verificación**: c) $1 + 1 = 2$, $1 - 1 = 0$, $2 + 1 = 3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Contestar a) "verdadero" porque "hay tantas ecuaciones como incógnitas".</details>
