# F04 — Métodos elementales: sustitución, igualación y reducción

Banco de las lecciones L13–L15. **Parte 1: 19 ejercicios**, ligados a los videos. La **parte 2** (31 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F04_metodos_elementales_parte2.md`; la familia completa suma **50**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Resultados comprobados con aritmética exacta en `ejercicios/verificar/f04.py`.

| Lección | Ejercicios |
|---|---|
| L13 Sustitución | N1-01 🎬, N1-02, N2-01 🎬, N3-01 🎬, N4-03, N4-04, N5-01 |
| L14 Igualación | N1-03, N2-02 🎬, N3-02 🎬 |
| L15 Reducción | N1-04, N2-03 🎬, N2-04, N2-05, N3-03 🎬, N3-04, N4-01 🎬, N4-02, N5-02 |

---

## Lección 13 — Sustitución

### F04-N1-01 · [C] Primera sustitución 🎬

**Objetivo**: aplicar los cinco pasos de la sustitución.
**Dificultad**: N1

**Enunciado.** Resuelve por sustitución y verifica: $2x + y = 8$, $x - y = 1$.

<details><summary>Pista 1</summary>¿Qué incógnita tiene coeficiente 1 o −1? Despéjala.</details>
<details><summary>Pista 2</summary>De la primera, $y = 8 - 2x$. Sustitúyelo, entre paréntesis, en la segunda.</details>
<details><summary>Solución</summary>

$y = 8 - 2x$. En la segunda: $x - (8 - 2x) = 1 \Rightarrow 3x - 8 = 1 \Rightarrow x = 3$. Entonces $y = 8 - 6 = 2$.

**Verificación**: $6 + 2 = 8$ ✓, $3 - 2 = 1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Escribir $x - 8 - 2x$ (sin paréntesis, el signo menos no afecta a $-2x$).</details>

### F04-N1-02 · [C] Despejar x

**Objetivo**: elegir la incógnita a despejar.
**Dificultad**: N1

**Enunciado.** Resuelve por sustitución: $x + 3y = 10$, $2x - y = 6$.

<details><summary>Pista 1</summary>Hay dos coeficientes $\pm1$: el de $x$ en la primera y el de $y$ en la segunda. Cualquiera sirve.</details>
<details><summary>Pista 2</summary>Con $x = 10 - 3y$: $2(10 - 3y) - y = 6$.</details>
<details><summary>Solución</summary>

$20 - 6y - y = 6 \Rightarrow -7y = -14 \Rightarrow y = 2$; $x = 10 - 6 = 4$.

**Verificación**: $4 + 6 = 10$ ✓, $8 - 2 = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$2(10 - 3y) = 20 - 3y$ (no repartir el 2).</details>

### F04-N2-01 · [C] Sustitución con fracciones 🎬

**Objetivo**: sustituir cuando ningún coeficiente es $\pm 1$.
**Dificultad**: N2

**Enunciado.** Resuelve por sustitución y verifica: $3x + 2y = 12$, $4x - 5y = -7$.

<details><summary>Pista 1</summary>Despeja $y = \frac{12 - 3x}{2}$.</details>
<details><summary>Pista 2</summary>Al sustituir, multiplica toda la ecuación por 2 para quitar el denominador.</details>
<details><summary>Solución</summary>

$4x - 5\cdot\frac{12 - 3x}{2} = -7$. Por 2: $8x - 60 + 15x = -14 \Rightarrow 23x = 46 \Rightarrow x = 2$; $y = \frac{12 - 6}{2} = 3$.

**Verificación**: $6 + 6 = 12$ ✓, $8 - 15 = -7$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$-5\cdot\frac{12 - 3x}{2} = \frac{-60 - 15x}{2}$ (el signo de $-3x$ cambia al multiplicar por $-5$: queda $+15x$).</details>

### F04-N3-01 · [K] Clasificar por sustitución 🎬

**Objetivo**: interpretar $0 = 0$ y $0 = c$.
**Dificultad**: N3

**Enunciado.** Clasifica y, si hay infinitas soluciones, parametrízalas: a) $x - 3y = 2$, $-2x + 6y = -4$ b) $x - 3y = 2$, $-2x + 6y = 1$.

<details><summary>Pista 1</summary>Despeja $x = 2 + 3y$ y sustitúyelo en la segunda.</details>
<details><summary>Pista 2</summary>Si la $y$ desaparece, mira si lo que queda es verdadero o falso.</details>
<details><summary>Solución</summary>

a) $-2(2 + 3y) + 6y = -4 \Rightarrow -4 = -4$, es decir, $0y = 0$: **SCI**, $(x, y) = (2 + 3t, t)$.
b) $-4 = 1$, es decir, $0y = 5$: **SI**.

**Verificación**: a) con $t = 1$: $(5, 1)$: $5 - 3 = 2$ ✓, $-10 + 6 = -4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Interpretar $-4 = -4$ como "$y = -4$".</details>

### F04-N4-03 · [K] Sustituir en la misma ecuación

**Objetivo**: detectar el error de sustituir el despeje en su propia ecuación.
**Dificultad**: N4

**Enunciado.** Para $x + y = 5$, $2x - y = 1$, un estudiante despeja $y = 5 - x$ de la primera, lo sustituye en la primera, obtiene $5 = 5$ y concluye "infinitas soluciones". Corrige.

<details><summary>Pista 1</summary>¿Qué información nueva aporta sustituir en la ecuación de la que se despejó?</details>
<details><summary>Pista 2</summary>Sustituye en la segunda.</details>
<details><summary>Solución</summary>

Sustituir en la misma ecuación siempre da una identidad: no aporta nada. En la segunda: $2x - (5 - x) = 1 \Rightarrow 3x = 6 \Rightarrow x = 2$, $y = 3$. **SCD**.

**Verificación**: $2 + 3 = 5$ ✓, $4 - 3 = 1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>El que el ejercicio muestra.</details>

### F04-N4-04 · [K] El paréntesis olvidado

**Objetivo**: detectar un error de sustitución con la verificación.
**Dificultad**: N4

**Enunciado.** Sistema: $3x - 2y = 4$, $x + y = 3$. Un estudiante escribe $x = 3 - y$ y luego "$3\cdot 3 - y - 2y = 4$", y obtiene $y = \frac53$. Encuentra el error, resuelve bien y explica cómo la verificación lo habría detectado.

<details><summary>Pista 1</summary>¿Qué debería haber escrito en lugar de $3\cdot 3 - y$?</details>
<details><summary>Pista 2</summary>$3(3 - y) = 9 - 3y$.</details>
<details><summary>Solución</summary>

Faltó el paréntesis: $3(3 - y) - 2y = 4 \Rightarrow 9 - 5y = 4 \Rightarrow y = 1$, $x = 2$.

Con la respuesta errónea, $x = 3 - \frac53 = \frac43$, y en la primera ecuación: $4 - \frac{10}{3} = \frac23 \neq 4$. La verificación lo habría detectado.

**Verificación**: $6 - 2 = 4$ ✓, $2 + 1 = 3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>No verificar en las ecuaciones originales.</details>

### F04-N5-01 · [D] La sustitución da un sistema equivalente

**Objetivo**: demostrar por qué la sustitución es válida.
**Dificultad**: N5

**Enunciado.** Sea $E_1$ equivalente a $y = A(x)$, donde $A(x)$ es una expresión en $x$. Demuestra que $\{E_1,\ E_2(x, y)\}$ tiene las mismas soluciones que $\{y = A(x),\ E_2(x, A(x))\}$.

<details><summary>Pista 1</summary>Prueba las dos inclusiones: toda solución del primero lo es del segundo, y al revés.</details>
<details><summary>Pista 2</summary>Si $(x_0, y_0)$ cumple $y_0 = A(x_0)$, entonces "$E_2$ en $(x_0, y_0)$" y "$E_2$ en $(x_0, A(x_0))$" son la misma afirmación.</details>
<details><summary>Solución</summary>

($\Rightarrow$) Si $(x_0, y_0)$ cumple $E_1$, entonces $y_0 = A(x_0)$ (porque $E_1 \Leftrightarrow y = A(x)$). Como cumple $E_2(x_0, y_0)$ y $y_0 = A(x_0)$, cumple $E_2(x_0, A(x_0))$.
($\Leftarrow$) Si $y_0 = A(x_0)$ y se cumple $E_2(x_0, A(x_0))$, escribiendo $y_0$ en lugar de $A(x_0)$ se cumple $E_2(x_0, y_0)$, y $y_0 = A(x_0)$ equivale a $E_1$. $\blacksquare$

**Verificación**: con el ejemplo de la Lección 13, $(3, 2)$ cumple los dos sistemas.
</details>
<details><summary>Errores frecuentes</summary>Probar solo una dirección.</details>

---

## Lección 14 — Igualación

### F04-N1-03 · [C] Ya despejadas

**Objetivo**: aplicar la igualación cuando ya hay despejes.
**Dificultad**: N1

**Enunciado.** Resuelve: $y = 3x - 2$, $y = -x + 6$.

<details><summary>Pista 1</summary>Iguala los lados derechos.</details>
<details><summary>Pista 2</summary>$3x - 2 = -x + 6$.</details>
<details><summary>Solución</summary>

$4x = 8$, $x = 2$; $y = 3\cdot 2 - 2 = 4$.

**Verificación**: $-2 + 6 = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar calcular $y$ después de hallar $x$.</details>

### F04-N2-02 · [C] Igualación despejando x 🎬

**Objetivo**: despejar la misma incógnita en ambas ecuaciones.
**Dificultad**: N2

**Enunciado.** Resuelve por igualación (despeja $x$ en ambas) y verifica: $x + 2y = 7$, $3x - y = 7$.

<details><summary>Pista 1</summary>$x = 7 - 2y$ y $x = \frac{7 + y}{3}$.</details>
<details><summary>Pista 2</summary>Multiplica por 3 tras igualar.</details>
<details><summary>Solución</summary>

$7 - 2y = \frac{7 + y}{3} \Rightarrow 21 - 6y = 7 + y \Rightarrow 7y = 14 \Rightarrow y = 2$, $x = 3$.

**Verificación**: $3 + 4 = 7$ ✓, $9 - 2 = 7$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Despejar $x = \frac{7 - y}{3}$ (signo).</details>

### F04-N3-02 · [C] Dos tarifas 🎬

**Objetivo**: plantear y resolver un problema con igualación e interpretar la respuesta.
**Dificultad**: N3

**Enunciado.** Plan A: 10 € al mes + 2 € por GB. Plan B: 4 € al mes + 3 € por GB. ¿Con cuántos GB cuestan lo mismo? ¿Cuál conviene si usas 8 GB?

<details><summary>Pista 1</summary>Con $g$ GB: $A = 10 + 2g$, $B = 4 + 3g$.</details>
<details><summary>Pista 2</summary>Para comparar con 8 GB basta sustituir.</details>
<details><summary>Solución</summary>

$10 + 2g = 4 + 3g \Rightarrow g = 6$: con 6 GB ambos cuestan 22 €. Con 8 GB: A cuesta 26 € y B, 28 €: **conviene A**. (A partir de 6 GB, A es más barato porque cada GB extra cuesta 1 € menos).

**Verificación**: $10 + 12 = 22 = 4 + 18$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Responder solo "6" sin decir qué significa.</details>

---

## Lección 15 — Reducción

### F04-N1-04 · [C] Coeficientes opuestos

**Objetivo**: sumar ecuaciones para eliminar.
**Dificultad**: N1

**Enunciado.** Resuelve por reducción: $x + y = 7$, $x - y = 3$.

<details><summary>Pista 1</summary>Los coeficientes de $y$ ya son opuestos.</details>
<details><summary>Pista 2</summary>Sumando: $2x = 10$.</details>
<details><summary>Solución</summary>

$x = 5$; $y = 7 - 5 = 2$.

**Verificación**: $5 - 2 = 3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Sumar mal los términos independientes.</details>

### F04-N2-03 · [C] Fabricar coeficientes opuestos 🎬

**Objetivo**: elegir multiplicadores.
**Dificultad**: N2

**Enunciado.** Resuelve por reducción y verifica: $4x + 3y = 10$, $6x - 5y = -4$.

<details><summary>Pista 1</summary>Para eliminar $x$: $3E_1$ y $2E_2$ tienen ambos $12x$.</details>
<details><summary>Pista 2</summary>$3E_1 - 2E_2$.</details>
<details><summary>Solución</summary>

$3E_1$: $12x + 9y = 30$. $2E_2$: $12x - 10y = -8$. Restando: $19y = 38$, $y = 2$. Entonces $4x + 6 = 10$, $x = 1$.

**Verificación**: $4 + 6 = 10$ ✓, $6 - 10 = -4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$-(-10y) = -10y$, o $30 - (-8) = 22$: errores de signo al restar.</details>

### F04-N2-04 · [C] Reducción con fracciones

**Objetivo**: quitar denominadores antes de reducir.
**Dificultad**: N2

**Enunciado.** Resuelve: $\frac x2 + \frac y3 = 3$, $\frac x4 - \frac y6 = 0$.

<details><summary>Pista 1</summary>Multiplica la primera por 6 y la segunda por 12.</details>
<details><summary>Pista 2</summary>Quedan $3x + 2y = 18$ y $3x - 2y = 0$.</details>
<details><summary>Solución</summary>

Sumando: $6x = 18$, $x = 3$. Restando: $4y = 18$, $y = \frac92$.

**Verificación**: $\frac32 + \frac32 = 3$ ✓, $\frac34 - \frac34 = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Multiplicar solo un término por 6.</details>

### F04-N2-05 · [C] Reducción con tres incógnitas

**Objetivo**: eliminar una incógnita de dos ecuaciones usando una tercera.
**Dificultad**: N2

**Enunciado.** Resuelve: $x + y + z = 2$, $x - y + 2z = -3$, $2x + y - z = 5$.

<details><summary>Pista 1</summary>Elimina $x$: $E_2 - E_1$ y $E_3 - 2E_1$.</details>
<details><summary>Pista 2</summary>Quedan $-2y + z = -5$ y $-y - 3z = 1$: un sistema 2×2.</details>
<details><summary>Solución</summary>

De $-2y + z = -5$ y $-y - 3z = 1$: multiplicando la segunda por 2 y restando, $7z = -7$, $z = -1$. Entonces $-2y - 1 = -5$, $y = 2$, y $x = 2 - 2 + 1 = 1$.

**Verificación**: $1 + 2 - 1 = 2$ ✓, $1 - 2 - 2 = -3$ ✓, $2 + 2 + 1 = 5$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Eliminar $x$ de una ecuación y otra incógnita de la otra: quedan dos ecuaciones con incógnitas distintas.</details>

### F04-N3-03 · [C] Elegir el método 🎬

**Objetivo**: elegir el método más cómodo según la forma del sistema.
**Dificultad**: N3

**Enunciado.** Elige el método más cómodo y resuelve: a) $y = 2x + 1$, $3x + y = 11$ b) $5x + 2y = 1$, $3x - 2y = 15$ c) $y = 4 - x$, $y = 2x - 5$.

<details><summary>Pista 1</summary>a) ya tiene $y$ despejada; b) coeficientes de $y$ opuestos; c) las dos despejadas.</details>
<details><summary>Pista 2</summary>a) sustitución; b) reducción; c) igualación.</details>
<details><summary>Solución</summary>

a) $3x + 2x + 1 = 11 \Rightarrow x = 2$, $y = 5$.
b) Sumando: $8x = 16$, $x = 2$; $10 + 2y = 1$, $y = -\frac92$.
c) $4 - x = 2x - 5 \Rightarrow x = 3$, $y = 1$.

**Verificación**: a) $6 + 5 = 11$ ✓; b) $6 + 9 = 15$ ✓; c) $6 - 5 = 1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Usar un método largo cuando la forma del sistema sugiere otro (no es un error matemático, pero aumenta el riesgo de errores de cálculo).</details>

### F04-N3-04 · [C] Gallinas y conejos

**Objetivo**: plantear un sistema a partir de un enunciado.
**Dificultad**: N3

**Enunciado.** En una granja hay gallinas y conejos: 30 cabezas y 84 patas. ¿Cuántos hay de cada uno?

<details><summary>Pista 1</summary>$g + c = 30$ (cabezas), $2g + 4c = 84$ (patas).</details>
<details><summary>Pista 2</summary>Reducción: $E_2 - 2E_1$.</details>
<details><summary>Solución</summary>

$E_2 - 2E_1$: $2c = 24$, $c = 12$; $g = 18$.

**Verificación**: $18 + 12 = 30$ ✓, $36 + 48 = 84$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Plantear $4g + 2c = 84$ (intercambiar patas).</details>

### F04-N4-01 · [K] Cambiar las dos ecuaciones a la vez 🎬

**Objetivo**: entender por qué se debe conservar una ecuación.
**Dificultad**: N4

**Enunciado.** Un estudiante transforma $2x + y = 5$, $x - y = 1$ en $\{E_1 - E_2:\ x + 2y = 4;\ E_2 - E_1:\ -x - 2y = -4\}$ y concluye "infinitas soluciones". ¿Dónde está el error? Resuélvelo bien.

<details><summary>Pista 1</summary>¿Qué relación hay entre las dos ecuaciones nuevas?</details>
<details><summary>Pista 2</summary>Busca un punto que cumpla el sistema nuevo pero no el original.</details>
<details><summary>Solución</summary>

La segunda ecuación nueva es la primera multiplicada por $-1$: el sistema nuevo tiene una sola ecuación útil y se perdió información. Por ejemplo, $(0, 2)$ lo cumple, pero $2\cdot 0 + 2 = 2 \neq 5$. Hay que cambiar **una** ecuación conservando la otra.

Correcto: $E_1 + E_2$: $3x = 6$, $x = 2$, $y = 1$.

**Verificación**: $4 + 1 = 5$ ✓, $2 - 1 = 1$ ✓.
</details>
<details><summary>Errores frecuentes</summary>El que el ejercicio muestra.</details>

### F04-N4-02 · [C] Reducción con un parámetro

**Objetivo**: discutir un sistema según un parámetro.
**Dificultad**: N4

**Enunciado.** Discute según $a$ y $b$: $x + ay = 1$, $2x + 4y = b$.

<details><summary>Pista 1</summary>$E_2 - 2E_1$ elimina $x$.</details>
<details><summary>Pista 2</summary>Queda $(4 - 2a)y = b - 2$: los tres casos de la Lección 6.</details>
<details><summary>Solución</summary>

$E_2 - 2E_1$: $(4 - 2a)\,y = b - 2$.

- $a \neq 2$: **SCD**, $y = \frac{b - 2}{4 - 2a}$, $x = 1 - a y$.
- $a = 2$, $b = 2$: $0y = 0$, **SCI**: $(1 - 2t, t)$.
- $a = 2$, $b \neq 2$: $0y = b - 2 \neq 0$, **SI**.

**Verificación**: $a = 0$, $b = 6$: $y = 1$, $x = 1$: $1 = 1$ ✓, $2 + 4 = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dividir entre $4 - 2a$ sin estudiar $a = 2$.</details>

### F04-N5-02 · [D] Multiplicar y sumar a la vez

**Objetivo**: generalizar la justificación de la reducción.
**Dificultad**: N5

**Enunciado.** a) Demuestra que sustituir $E_2$ por $c\,E_2 + k\,E_1$ (conservando $E_1$) no cambia las soluciones si $c \neq 0$. b) Muestra con un ejemplo que, si $c = 0$, pueden aparecer soluciones nuevas.

<details><summary>Pista 1</summary>a) ¿Cómo recuperas $E_2$ a partir de $E_1$ y de $cE_2 + kE_1$?</details>
<details><summary>Pista 2</summary>b) Con $c = 0$ y $k = 1$, la nueva segunda ecuación es una copia de $E_1$.</details>
<details><summary>Solución</summary>

a) Una solución de $E_1$ y $E_2$ cumple cualquier combinación, en particular $cE_2 + kE_1$. Recíprocamente, si cumple $E_1$ y $cE_2 + kE_1$, restando $kE_1$ cumple $cE_2$, y multiplicando por $\frac1c$ (existe porque $c \neq 0$), cumple $E_2$. $\blacksquare$
b) $x + y = 2$, $x - y = 0$ (solución única $(1, 1)$). Con $c = 0$, $k = 1$: $\{x + y = 2,\ x + y = 2\}$, que admite $(2, 0)$, que no cumplía $x - y = 0$.

**Verificación**: $(2, 0)$: $2 - 0 = 2 \neq 0$ ✓ (no era solución del original).
</details>
<details><summary>Errores frecuentes</summary>Olvidar usar $c \neq 0$ en la vuelta atrás.</details>
