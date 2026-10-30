# F00 — Preliminares: números, álgebra, coordenadas y lenguaje

Banco de la Unidad 0 (lecciones L01–L04). **30 ejercicios**.

- **Niveles**: N1 fundamentos · N2 rutinarios con varios pasos · N3 elegir método o razonar · N4 casos especiales y errores · N5 integradores y demostraciones.
- **Tipos**: [C] cálculo · [K] conceptual · [D] demostración.
- **Cómo usarlo**: intenta el ejercicio y abre las pistas una a una solo si te atascas. La solución va al final, plegada.
- Los resultados numéricos están comprobados con aritmética exacta en `ejercicios/verificar/f00.py`.
- Los ejercicios marcados con 🎬 aparecen al final de un video.

| Lección | Ejercicios |
|---|---|
| L01 Números reales | N1-01 🎬, N1-02 🎬, N1-03, N1-04, N2-01 🎬, N2-02 🎬, N3-01, N4-01, N5-01, N5-05 |
| L02 Expresiones y ecuaciones | N1-05 🎬, N1-06, N2-03 🎬, N2-04 🎬, N3-02, N3-05, N4-02, N5-02 |
| L03 Coordenadas | N1-07 🎬, N2-05 🎬, N2-06 🎬, N3-03, N4-03, N5-03 🎬 |
| L04 Lenguaje matemático | N1-08 🎬, N2-07 🎬, N2-08, N3-04 🎬, N4-04, N5-04 🎬 |

---

## Lección 1 — Números reales

### F00-N1-01 · [K] El conjunto más pequeño 🎬

**Objetivo**: distinguir naturales, enteros, racionales e irracionales.
**Dificultad**: N1

**Enunciado.** Indica el conjunto más pequeño ($\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ o $\mathbb{R}$) al que pertenece cada número: $-7$, $0$, $\tfrac34$, $\sqrt9$, $\sqrt5$, $0.25$, $-\pi$.

<details><summary>Pista 1</summary>Antes de clasificar, simplifica: ¿cuánto vale $\sqrt 9$? ¿Y $0.25$ como fracción?</details>
<details><summary>Pista 2</summary>Un número es racional si se puede escribir como $p/q$ con $p, q$ enteros y $q \neq 0$. Las raíces cuadradas de números que no son cuadrados perfectos no lo son (ver N5-05).</details>
<details><summary>Solución</summary>

| Número | Conjunto más pequeño | Por qué |
|---|---|---|
| $-7$ | $\mathbb{Z}$ | entero negativo |
| $0$ | $\mathbb{Z}$ | con la convención del curso, $\mathbb{N} = \{1, 2, \dots\}$. Si tu libro incluye el 0 en $\mathbb{N}$, la respuesta es $\mathbb{N}$ |
| $\tfrac34$ | $\mathbb{Q}$ | cociente de enteros que no es entero |
| $\sqrt9 = 3$ | $\mathbb{N}$ | primero se simplifica |
| $\sqrt5$ | $\mathbb{R}$ (irracional) | 5 no es un cuadrado perfecto; la prueba es igual que la de $\sqrt2$ (ver N5-05 para $\sqrt3$) |
| $0.25 = \tfrac14$ | $\mathbb{Q}$ | decimal finito |
| $-\pi$ | $\mathbb{R}$ (irracional) | el opuesto de un irracional es irracional (si $-\pi = p/q$, entonces $\pi = -p/q$ sería racional) |

**Verificación**: cada número está también en todos los conjuntos "más grandes" ($\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$).
</details>
<details><summary>Errores frecuentes</summary>

- Clasificar $\sqrt9$ como irracional "porque tiene raíz".
- Creer que $0.25$ no es racional "porque es decimal".
</details>

### F00-N1-02 · [C] Operaciones con signos 🎬

**Objetivo**: aplicar las reglas de los signos y la prioridad de la potencia sobre el signo.
**Dificultad**: N1

**Enunciado.** Calcula: a) $(-4)(-5) - 3\cdot(-2)$ b) $-2^2 + (-2)^2$ c) $7 - (-3) - (+5)$

<details><summary>Pista 1</summary>Primero los productos y las potencias; después las sumas y restas.</details>
<details><summary>Pista 2</summary>$-2^2$ es el opuesto de $2^2$; en cambio $(-2)^2 = (-2)(-2)$.</details>
<details><summary>Solución</summary>

a) $(-4)(-5) = 20$ (signos iguales) y $3\cdot(-2) = -6$. Entonces $20 - (-6) = 20 + 6 = 26$.
b) $-2^2 = -4$ y $(-2)^2 = 4$, así que $-4 + 4 = 0$.
c) Restar es sumar el opuesto: $7 + 3 - 5 = 5$.

**Verificación**: comprobado en `verificar/f00.py`.
</details>
<details><summary>Errores frecuentes</summary>

- $-2^2 = 4$.
- $20 - (-6) = 14$: olvidar que restar un negativo es sumar.
</details>

### F00-N1-03 · [C] Opuestos y paréntesis

**Objetivo**: manejar signos anidados y el signo menos delante de un paréntesis.
**Dificultad**: N1

**Enunciado.** Calcula: a) $-(-(-6))$ b) $-(3 - 5)$ c) $-(-2)^3$ d) $(-1)^{10}$ y $-1^{10}$

<details><summary>Pista 1</summary>Cada signo menos delante es "tomar el opuesto": cuenta cuántos hay.</details>
<details><summary>Pista 2</summary>En b) calcula primero el paréntesis, o reparte el signo a <b>todos</b> los términos.</details>
<details><summary>Solución</summary>

a) Tres opuestos seguidos: $-(-(-6)) = -(6) = -6$.
b) $3 - 5 = -2$, y $-(-2) = 2$. Repartiendo: $-3 + 5 = 2$. Coincide.
c) $(-2)^3 = (-2)(-2)(-2) = -8$, y $-(-8) = 8$.
d) $(-1)^{10} = 1$ (un número par de factores negativos); $-1^{10} = -(1^{10}) = -1$.

**Verificación**: comprobado en `verificar/f00.py`.
</details>
<details><summary>Errores frecuentes</summary>

- b) $-(3 - 5) = -3 - 5 = -8$: el signo solo se aplicó al primer término.
- d) confundir $(-1)^{10}$ con $-1^{10}$.
</details>

### F00-N1-04 · [K] El 0 en la división

**Objetivo**: justificar por qué no se divide entre 0 y detectar cuándo una expresión no está definida.
**Dificultad**: N1

**Enunciado.** a) Explica por qué $0/5 = 0$ pero $5/0$ no está definido. b) ¿Para qué valores de $a$ está definida $\dfrac{3}{a - 2}$? c) Halla, si existe, el inverso de $0$, de $-4$ y de $\tfrac23$.

<details><summary>Pista 1</summary>Usa la definición: $\frac{p}{q} = r$ significa $q \cdot r = p$.</details>
<details><summary>Pista 2</summary>El inverso de $a$ es el número $b$ con $a\cdot b = 1$.</details>
<details><summary>Solución</summary>

a) $0/5 = 0$ porque $5 \cdot 0 = 0$. Para $5/0$ necesitaríamos $r$ con $0\cdot r = 5$, pero $0 \cdot r = 0$ para todo $r$: no existe.
b) Hace falta que el denominador no sea 0: $a - 2 \neq 0$, es decir, $a \neq 2$.
c) $0$ no tiene inverso ($0\cdot b = 0 \neq 1$). El inverso de $-4$ es $-\tfrac14$, porque $(-4)(-\tfrac14) = 1$. El de $\tfrac23$ es $\tfrac32$.

**Verificación**: $(-4)(-\tfrac14) = 1$ y $\tfrac23\cdot\tfrac32 = 1$.
</details>
<details><summary>Errores frecuentes</summary>

- Decir que $5/0 = 0$ o que $5/0 = \infty$ (no es un número real).
- Responder en b) "$a \neq 0$".
</details>

### F00-N2-01 · [C] Operaciones con fracciones 🎬

**Objetivo**: sumar con denominador común y dividir multiplicando por la inversa.
**Dificultad**: N2

**Enunciado.** a) $\dfrac23 - \dfrac56 + \dfrac14$ b) $\dfrac35 \div \left(-\dfrac{9}{10}\right)$

<details><summary>Pista 1</summary>a) El menor denominador común de 3, 6 y 4 es 12.</details>
<details><summary>Pista 2</summary>b) Dividir entre $-\frac{9}{10}$ es multiplicar por $-\frac{10}{9}$.</details>
<details><summary>Solución</summary>

a) $\frac23 = \frac{8}{12}$, $\frac56 = \frac{10}{12}$, $\frac14 = \frac{3}{12}$. Entonces $\frac{8 - 10 + 3}{12} = \frac{1}{12}$.
b) $\frac35 \cdot \left(-\frac{10}{9}\right) = -\frac{30}{45} = -\frac23$.

**Verificación**: comprobado con `Fraction` en `verificar/f00.py`. Además, $-\frac23 \cdot \left(-\frac{9}{10}\right) = \frac{18}{30} = \frac35$ ✓.
</details>
<details><summary>Errores frecuentes</summary>

- Sumar numeradores y denominadores.
- Perder el signo al dividir.
</details>

### F00-N2-02 · [C] Orden de las operaciones y distributiva 🎬

**Objetivo**: aplicar la jerarquía de operaciones y reconocer la distributiva.
**Dificultad**: N2

**Enunciado.** a) $2 + 4\cdot(5 - 3)^2 \div 8$ b) Calcula $7\cdot(10 + 3)$ de dos formas distintas. ¿Qué propiedad usa la segunda?

<details><summary>Pista 1</summary>Orden: paréntesis, potencias, × y ÷ de izquierda a derecha, + y −.</details>
<details><summary>Pista 2</summary>b) Una forma: resolver primero el paréntesis. Otra: repartir el 7.</details>
<details><summary>Solución</summary>

a) $(5 - 3) = 2$; $2^2 = 4$; $4 \cdot 4 = 16$; $16 \div 8 = 2$; $2 + 2 = 4$.
b) $7 \cdot 13 = 91$. También $7\cdot 10 + 7 \cdot 3 = 70 + 21 = 91$. La segunda usa la **propiedad distributiva**.

**Verificación**: ambas formas dan 91.
</details>
<details><summary>Errores frecuentes</summary>

- a) sumar $2 + 4$ al principio (da 3, incorrecto).
- b) $7\cdot 10 + 3 = 73$: la distributiva multiplica **todos** los términos del paréntesis.
</details>

### F00-N3-01 · [K] ¿Qué propiedades se cumplen?

**Objetivo**: decidir si una igualdad es una propiedad general y refutarla con un contraejemplo si no lo es.
**Dificultad**: N3

**Enunciado.** Decide si cada igualdad es cierta para todos los reales (con los denominadores distintos de 0). Si lo es, nombra la propiedad; si no, da un contraejemplo.
a) $a - b = b - a$ b) $(ab)c = a(bc)$ c) $a \div (b + c) = a \div b + a \div c$ d) $a(b - c) = ab - ac$

<details><summary>Pista 1</summary>Para refutar un "para todo" basta un ejemplo numérico donde falle.</details>
<details><summary>Pista 2</summary>d) Escribe $b - c = b + (-c)$.</details>
<details><summary>Solución</summary>

a) Falsa: $5 - 2 = 3$ y $2 - 5 = -3$.
b) Cierta: propiedad **asociativa** del producto.
c) Falsa: $12 \div (2 + 4) = 2$, pero $12 \div 2 + 12 \div 4 = 6 + 3 = 9$.
d) Cierta: es la **distributiva**, porque $a(b + (-c)) = ab + a(-c) = ab - ac$.

**Verificación**: los contraejemplos se comprueban con la calculadora.
</details>
<details><summary>Errores frecuentes</summary>

- Creer que la división se "reparte" sobre una suma en el denominador.
- Dar como "prueba" de b) un solo ejemplo numérico: los ejemplos no demuestran (L04).
</details>

### F00-N4-01 · [K] Encuentra el error

**Objetivo**: detectar errores típicos con fracciones.
**Dificultad**: N4

**Enunciado.** Cada resolución tiene un error. Encuéntralo y corrígelo.
a) $\dfrac34 + \dfrac14 = \dfrac{4}{8} = \dfrac12$ b) $\dfrac{2 + 3}{2} = 3$ ("se tachan los doses") c) $\dfrac{1}{x} + \dfrac{1}{y} = \dfrac{2}{x + y}$

<details><summary>Pista 1</summary>a) ¿Tiene sentido que $\frac34 + \frac14$ sea menor que $\frac34$?</details>
<details><summary>Pista 2</summary>b) Solo se simplifican <b>factores</b> comunes, no sumandos. c) Prueba con $x = y = 1$.</details>
<details><summary>Solución</summary>

a) Se sumaron los denominadores. Con el mismo denominador: $\frac{3 + 1}{4} = 1$.
b) El 2 de arriba es un sumando, no un factor. Correcto: $\frac{5}{2}$.
c) Con $x = y = 1$: izquierda $= 2$, derecha $= 1$. Lo correcto es $\frac1x + \frac1y = \frac{y + x}{xy}$ (con $x, y \neq 0$).

**Verificación**: el valor correcto de a) es $1 = \frac44$; el de b) es $2.5$; la fórmula de c) da $2$ con $x = y = 1$.
</details>
<details><summary>Errores frecuentes</summary>Simplificar sumandos como si fueran factores; sumar denominadores.</details>

### F00-N5-01 · [D] Entre dos racionales siempre hay otro

**Objetivo**: hacer una demostración directa con fracciones.
**Dificultad**: N5

**Enunciado.** Demuestra que si $a$ y $b$ son racionales con $a < b$, entonces $m = \frac{a + b}{2}$ es racional y cumple $a < m < b$. Deduce que entre dos racionales distintos hay infinitos racionales.

<details><summary>Pista 1</summary>Escribe $a = \frac{p}{q}$, $b = \frac{r}{s}$ y calcula $m$ como una sola fracción.</details>
<details><summary>Pista 2</summary>Calcula $m - a$ y $b - m$: ¿qué signo tienen?</details>
<details><summary>Solución</summary>

*Racional*: si $a = \frac pq$ y $b = \frac rs$ ($q, s \neq 0$), entonces $m = \frac{ps + rq}{2qs}$, cociente de enteros con denominador $2qs \neq 0$.
*Orden*: $m - a = \frac{b - a}{2} > 0$ y $b - m = \frac{b - a}{2} > 0$, porque $b - a > 0$. Luego $a < m < b$.
*Infinitos*: aplicando lo mismo a $a$ y $m$ se obtiene otro racional entre ellos, y así sucesivamente sin fin; todos son distintos porque cada uno es estrictamente menor que el anterior. $\blacksquare$

**Verificación** (ejemplo, no prueba): $a = \frac13$, $b = \frac12$ dan $m = \frac{5}{12}$, y $\frac{4}{12} < \frac{5}{12} < \frac{6}{12}$.
</details>
<details><summary>Errores frecuentes</summary>Dar solo un ejemplo como demostración; olvidar justificar que $2qs \neq 0$.</details>

### F00-N5-05 · [D] $\sqrt 3$ es irracional

**Objetivo**: adaptar la reducción al absurdo de $\sqrt2$ a otro caso.
**Dificultad**: N5

**Enunciado.** a) Demuestra: si $p$ es un entero y $p^2$ es múltiplo de 3, entonces $p$ es múltiplo de 3. b) Usa a) para demostrar que $\sqrt3$ no es racional.

<details><summary>Pista 1</summary>a) Todo entero es de la forma $3k$, $3k + 1$ o $3k + 2$. Usa el contrarrecíproco: si $p$ no es múltiplo de 3, $p^2$ tampoco.</details>
<details><summary>Pista 2</summary>b) Copia la prueba de $\sqrt2$ cambiando "par" por "múltiplo de 3".</details>
<details><summary>Solución</summary>

a) Si $p = 3k + 1$: $p^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$. Si $p = 3k + 2$: $p^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$. En ambos casos $p^2$ deja resto 1 al dividir entre 3, así que no es múltiplo de 3. Por contrarrecíproco, si $p^2$ es múltiplo de 3, $p$ también.
b) Supongamos $\sqrt3 = \frac pq$ irreducible. Entonces $p^2 = 3q^2$: $p^2$ es múltiplo de 3 y, por a), $p = 3k$. Sustituyendo, $9k^2 = 3q^2$, o sea $q^2 = 3k^2$: $q$ también es múltiplo de 3. Entonces $p$ y $q$ tienen el factor común 3, lo que contradice que la fracción fuera irreducible. $\blacksquare$

**Verificación**: comprobación numérica de a) para $p = 1, \dots, 30$ en `verificar/f00.py` (es solo una comprobación, no la prueba).
</details>
<details><summary>Errores frecuentes</summary>Afirmar a) sin demostrarlo; olvidar suponer la fracción irreducible.</details>

---

## Lección 2 — Expresiones y ecuaciones

### F00-N1-05 · [K] Anatomía de una expresión 🎬

**Objetivo**: identificar términos, coeficientes y término independiente, y evaluar.
**Dificultad**: N1

**Enunciado.** En $4x - y + 7 - 2z$: a) ¿cuántos términos tiene? b) ¿qué coeficiente tiene cada variable? c) ¿cuál es el término independiente? d) Evalúala en $x = 1$, $y = -2$, $z = 3$.

<details><summary>Pista 1</summary>El signo que precede a un término es parte del término.</details>
<details><summary>Pista 2</summary>$-y = (-1)\cdot y$. Al sustituir, pon cada número entre paréntesis.</details>
<details><summary>Solución</summary>

a) Cuatro: $4x$, $-y$, $+7$, $-2z$.
b) $x$: 4; $y$: $-1$; $z$: $-2$.
c) $7$.
d) $4(1) - (-2) + 7 - 2(3) = 4 + 2 + 7 - 6 = 7$.

**Verificación**: comprobado en `verificar/f00.py`.
</details>
<details><summary>Errores frecuentes</summary>Decir que $y$ tiene coeficiente 1 o que $z$ tiene coeficiente 2; escribir $-(-2) = -2$.</details>

### F00-N1-06 · [C] Simplificar expresiones

**Objetivo**: agrupar términos semejantes y quitar paréntesis correctamente.
**Dificultad**: N1

**Enunciado.** Simplifica: a) $5x - 2 + 3x + 7$ b) $2(x - 3) - (4 - x)$ c) $3x + 2y - x + 4 - 5y$. Después comprueba b) evaluando la expresión original y la simplificada en $x = -1$.

<details><summary>Pista 1</summary>Quita primero los paréntesis (distributiva, y cuidado con el signo menos delante).</details>
<details><summary>Pista 2</summary>Junta las $x$ con las $x$, las $y$ con las $y$ y los números con los números.</details>
<details><summary>Solución</summary>

a) $8x + 5$.
b) $2x - 6 - 4 + x = 3x - 10$.
c) $2x - 3y + 4$ (no se puede simplificar más: $x$ e $y$ no son semejantes).

**Verificación** de b) con $x = -1$: original $2(-4) - (5) = -13$; simplificada $3(-1) - 10 = -13$ ✓.
</details>
<details><summary>Errores frecuentes</summary>

- $-(4 - x) = -4 - x$ (el signo no se repartió al segundo término).
- Escribir $2x - 3y = -xy$: solo se suman términos semejantes.
</details>

### F00-N2-03 · [C] ¿Es solución? 🎬

**Objetivo**: verificar soluciones por sustitución.
**Dificultad**: N2

**Enunciado.** ¿Cuáles de los valores $x = -2$, $x = 0$, $x = 4$ son solución de $3x - 2 = x + 6$?

<details><summary>Pista 1</summary>Sustituye cada valor en <b>los dos lados</b> por separado y compara.</details>
<details><summary>Pista 2</summary>Solo es solución si ambos lados dan exactamente el mismo número.</details>
<details><summary>Solución</summary>

| $x$ | izquierda $3x - 2$ | derecha $x + 6$ | ¿solución? |
|---|---|---|---|
| $-2$ | $-8$ | $4$ | no |
| $0$ | $-2$ | $6$ | no |
| $4$ | $10$ | $10$ | **sí** |

**Verificación**: resolviendo, $2x = 8$, $x = 4$: coincide.
</details>
<details><summary>Errores frecuentes</summary>Evaluar solo un lado; equivocarse con $3\cdot(-2)$.</details>

### F00-N2-04 · [C] Resolver justificando cada paso 🎬

**Objetivo**: resolver una ecuación lineal nombrando la regla de cada paso.
**Dificultad**: N2

**Enunciado.** Resuelve $3x - 5 = 7 - x$ indicando qué regla aplicas en cada paso, y verifica.

<details><summary>Pista 1</summary>Reúne las $x$ en un lado: ¿qué hay que sumar a ambos lados para que desaparezca $-x$ de la derecha?</details>
<details><summary>Pista 2</summary>Después reúne los números en el otro lado y divide entre el coeficiente de $x$ (que no es 0).</details>
<details><summary>Solución</summary>

- Sumar $x$ a ambos lados (regla 1): $4x - 5 = 7$.
- Sumar 5 a ambos lados (regla 1): $4x = 12$.
- Dividir ambos lados entre 4, que es distinto de 0 (regla 2): $x = 3$.

Cada paso es reversible, así que las ecuaciones son equivalentes y la única solución es $x = 3$.

**Verificación**: $3(3) - 5 = 4$ y $7 - 3 = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Pasar $-x$ al otro lado como $-x$ (sin cambiar el signo); dividir solo un lado.</details>

### F00-N3-02 · [K] ¿Una, infinitas o ninguna?

**Objetivo**: reconocer identidades y ecuaciones sin solución.
**Dificultad**: N3

**Enunciado.** Sin resolver "a ciegas", decide cuántas soluciones tiene cada ecuación y justifícalo.
a) $3(x - 2) = 3x - 6$ b) $4x + 1 = 4x - 3$ c) $2x + 3 = x - 1$ d) $5x = 0$

<details><summary>Pista 1</summary>Simplifica cada lado y luego intenta reunir las $x$ en un lado. ¿Qué queda?</details>
<details><summary>Pista 2</summary>Si las $x$ desaparecen, mira si lo que queda es verdadero siempre o falso siempre.</details>
<details><summary>Solución</summary>

a) La izquierda es $3x - 6$, igual que la derecha: identidad, **infinitas** soluciones (todo $\mathbb{R}$).
b) Restando $4x$: $1 = -3$, falso siempre: **ninguna**.
c) Restando $x$ y 3: $x = -4$: **una**.
d) Dividiendo entre 5: $x = 0$: **una** (que la solución sea 0 no significa que no haya solución).

**Verificación**: c) $2(-4) + 3 = -5 = -4 - 1$ ✓; d) $5\cdot 0 = 0$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Confundir "la solución es 0" con "no hay solución"; en a), decir "0 = 0, no tiene solución".</details>

### F00-N3-05 · [C] Ecuaciones con fracciones

**Objetivo**: elegir el multiplicador adecuado (distinto de 0) para quitar denominadores.
**Dificultad**: N3

**Enunciado.** Resuelve y verifica: a) $\dfrac{x}{2} + \dfrac{x}{3} = 5$ b) $2(x + 1) - 3 = 5x + 4$

<details><summary>Pista 1</summary>a) Multiplica ambos lados por 6 (múltiplo común de 2 y 3, distinto de 0).</details>
<details><summary>Pista 2</summary>b) Quita el paréntesis, reúne las $x$ a un lado y los números al otro. La solución puede ser una fracción.</details>
<details><summary>Solución</summary>

a) Multiplicando por 6: $3x + 2x = 30$, $5x = 30$, $x = 6$.
b) $2x + 2 - 3 = 5x + 4$, o sea $2x - 1 = 5x + 4$. Restando $2x$ y $4$: $-5 = 3x$, $x = -\frac53$.

**Verificación**: a) $3 + 2 = 5$ ✓. b) izquierda: $2(-\frac23) - 3 = -\frac{13}{3}$; derecha: $5(-\frac53) + 4 = -\frac{13}{3}$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Multiplicar por 6 solo un término; dar la solución como decimal redondeado ($-1.67$) en vez de $-\frac53$.</details>

### F00-N4-02 · [K] Pasos que cambian las soluciones

**Objetivo**: detectar pasos no reversibles.
**Dificultad**: N4

**Enunciado.** Explica el error en cada razonamiento y da el conjunto solución correcto.
a) "$x^2 = 3x$. Divido entre $x$: $x = 3$. Solución: $\{3\}$."
b) "$x + 2 = 5$. Multiplico por 0: $0 = 0$, que siempre es cierto. Solución: todo $\mathbb{R}$."

<details><summary>Pista 1</summary>a) ¿Se puede dividir entre $x$ si $x$ vale 0? Estudia ese caso aparte.</details>
<details><summary>Pista 2</summary>b) ¿Se puede deshacer una multiplicación por 0?</details>
<details><summary>Solución</summary>

a) Dividir entre $x$ exige $x \neq 0$. Por casos: si $x \neq 0$, dividir es válido y da $x = 3$; si $x = 0$, sustituyendo: $0 = 0$, así que **también es solución**. Conjunto solución: $\{0, 3\}$.
b) Multiplicar por 0 no se puede deshacer, así que la nueva ecuación no es equivalente: se ganan soluciones falsas. Correcto: $x = 3$, conjunto $\{3\}$.

**Verificación**: $0^2 = 3\cdot 0$ ✓, $3^2 = 3 \cdot 3$ ✓; $3 + 2 = 5$ ✓, y por ejemplo $x = 0$ no cumple $x + 2 = 5$.
</details>
<details><summary>Errores frecuentes</summary>Dividir entre expresiones con la incógnita sin estudiar el caso cero. Este error reaparecerá en los sistemas con parámetros (L29, L42).</details>

### F00-N5-02 · [D] La regla 2, demostrada

**Objetivo**: demostrar que multiplicar por $c \neq 0$ da una ecuación equivalente y por qué hace falta $c \neq 0$.
**Dificultad**: N5

**Enunciado.** Sean $a, b, c$ reales. a) Demuestra que si $c \neq 0$, entonces $a = b \Leftrightarrow ca = cb$. b) Muestra con un contraejemplo que la implicación $ca = cb \Rightarrow a = b$ falla si $c = 0$.

<details><summary>Pista 1</summary>"⇒": si dos números son iguales, al multiplicarlos por lo mismo siguen siendo iguales.</details>
<details><summary>Pista 2</summary>"⇐": multiplica ambos lados de $ca = cb$ por $\frac1c$, que existe porque $c \neq 0$, y usa asociativa e inverso.</details>
<details><summary>Solución</summary>

a) (⇒) Si $a = b$, son el mismo número, y multiplicar el mismo número por $c$ da el mismo resultado: $ca = cb$.
(⇐) Como $c \neq 0$, existe $\frac1c$. Multiplicando $ca = cb$ por $\frac1c$: $\frac1c(ca) = \frac1c(cb)$. Por la asociativa, $(\frac1c c) a = (\frac1c c) b$, es decir, $1\cdot a = 1 \cdot b$, luego $a = b$. $\blacksquare$
b) $c = 0$, $a = 2$, $b = 3$: $0\cdot 2 = 0 \cdot 3$, pero $2 \neq 3$.

**Verificación**: el contraejemplo se comprueba directamente.
</details>
<details><summary>Errores frecuentes</summary>Demostrar solo una dirección; usar $\frac1c$ sin decir que existe porque $c \neq 0$.</details>

---

## Lección 3 — Coordenadas

### F00-N1-07 · [C] Ubicar puntos 🎬

**Objetivo**: situar pares ordenados e identificar cuadrantes y ejes.
**Dificultad**: N1

**Enunciado.** Dibuja $A(2, -1)$, $B(-3, 2)$, $C(0, 4)$ y $D(-1, 0)$. ¿En qué cuadrante (o en qué eje) está cada uno?

<details><summary>Pista 1</summary>Primera coordenada: horizontal. Segunda: vertical.</details>
<details><summary>Pista 2</summary>Si una coordenada es 0, el punto está sobre un eje y no pertenece a ningún cuadrante.</details>
<details><summary>Solución</summary>

$A$: cuadrante IV $(+,-)$. $B$: cuadrante II $(-,+)$. $C$: eje $y$ ($x = 0$). $D$: eje $x$ ($y = 0$).

**Verificación**: los signos de las coordenadas coinciden con los del cuadrante.
</details>
<details><summary>Errores frecuentes</summary>Ubicar $C(0,4)$ sobre el eje $x$ (intercambiar coordenadas).</details>

### F00-N2-05 · [C] Puntos de una gráfica 🎬

**Objetivo**: decidir por sustitución si un punto pertenece a la gráfica, y generar puntos nuevos.
**Dificultad**: N2

**Enunciado.** ¿Cuáles de los puntos $(2, 0)$, $(0, -4)$, $(3, 2)$, $(1, 1)$ están en la gráfica de $2x - y = 4$? Encuentra otros dos puntos de esa gráfica.

<details><summary>Pista 1</summary>Un punto está en la gráfica si y solo si sus coordenadas cumplen la ecuación.</details>
<details><summary>Pista 2</summary>Para generar puntos, despeja $y = 2x - 4$ y elige valores de $x$.</details>
<details><summary>Solución</summary>

- $(2, 0)$: $4 - 0 = 4$ ✓
- $(0, -4)$: $0 + 4 = 4$ ✓
- $(3, 2)$: $6 - 2 = 4$ ✓
- $(1, 1)$: $2 - 1 = 1 \neq 4$ ✗

Otros puntos: con $x = 4$, $y = 4$: $(4, 4)$. Con $x = -1$, $y = -6$: $(-1, -6)$.

**Verificación**: $2\cdot 4 - 4 = 4$ ✓; $2\cdot(-1) - (-6) = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Con $(0, -4)$: escribir $0 - 4 = 4$, olvidando que se resta $y = -4$.</details>

### F00-N2-06 · [C] Recta por dos puntos 🎬

**Objetivo**: calcular pendiente, ordenada en el origen y ecuación de una recta.
**Dificultad**: N2

**Enunciado.** Halla la pendiente, la ordenada en el origen y la ecuación de la recta que pasa por $(-1, 4)$ y $(2, -2)$.

<details><summary>Pista 1</summary>$m = \frac{y_2 - y_1}{x_2 - x_1}$, restando en el mismo orden arriba y abajo.</details>
<details><summary>Pista 2</summary>Sustituye uno de los puntos en $y = mx + n$ para hallar $n$.</details>
<details><summary>Solución</summary>

$m = \frac{-2 - 4}{2 - (-1)} = \frac{-6}{3} = -2$. Con $(-1, 4)$: $4 = -2(-1) + n = 2 + n$, así que $n = 2$. Ecuación: $y = -2x + 2$, o en forma general $2x + y = 2$.

**Verificación**: $(2, -2)$: $-2\cdot 2 + 2 = -2$ ✓; $(-1, 4)$: $2 + 2 = 4$ ✓.
</details>
<details><summary>Errores frecuentes</summary>$2 - (-1) = 1$ (error de signo); calcular $\frac{x_2 - x_1}{y_2 - y_1}$.</details>

### F00-N3-03 · [C] Forma general y forma explícita

**Objetivo**: pasar de $ax + by = c$ a $y = mx + n$ y reconocer cuándo no se puede.
**Dificultad**: N3

**Enunciado.** a) Escribe $3x + 2y = 6$ como $y = mx + n$, y halla dónde corta a cada eje. b) ¿Se puede escribir $x = -1$ como $y = mx + n$? Escríbela en la forma $ax + by = c$.

<details><summary>Pista 1</summary>a) Despeja $y$ (aplica las reglas de L02). Para el corte con el eje $x$, pon $y = 0$.</details>
<details><summary>Pista 2</summary>b) ¿Qué pendiente tendría una recta vertical?</details>
<details><summary>Solución</summary>

a) $2y = -3x + 6$, $y = -\frac32 x + 3$: $m = -\frac32$, $n = 3$. Corte con el eje $y$: $(0, 3)$. Corte con el eje $x$ ($y = 0$): $3x = 6$, $(2, 0)$.
b) No: es vertical, y su "pendiente" exigiría dividir entre 0. En forma general: $1\cdot x + 0 \cdot y = -1$.

**Verificación**: $(0,3)$ y $(2,0)$ cumplen $3x + 2y = 6$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Dividir solo un término entre 2; decir que una recta vertical tiene pendiente 0.</details>

### F00-N4-03 · [K] ¿Se cortan, son paralelas o son la misma?

**Objetivo**: comparar rectas a partir de su ecuación (anticipo de la clasificación de sistemas).
**Dificultad**: N4

**Enunciado.** Compara la recta $r: y = 2x + 1$ con: a) $s: 4x - 2y = 6$ b) $t: 6x - 3y = -3$ c) $u: x + y = 4$.

<details><summary>Pista 1</summary>Pasa cada ecuación a la forma $y = mx + n$.</details>
<details><summary>Pista 2</summary>Misma pendiente y misma $n$: la misma recta. Misma pendiente y distinta $n$: paralelas. Distinta pendiente: se cortan en un punto.</details>
<details><summary>Solución</summary>

a) $-2y = -4x + 6$, $y = 2x - 3$: misma pendiente, distinta $n$: **paralelas**, sin puntos comunes.
b) $-3y = -6x - 3$, $y = 2x + 1$: **la misma recta** (infinitos puntos comunes).
c) $y = -x + 4$: pendientes distintas: **se cortan en un punto**. Igualando, $2x + 1 = -x + 4$, $x = 1$, $y = 3$: el punto $(1, 3)$.

**Verificación**: $(1, 3)$ está en $r$ ($2 + 1 = 3$) y en $u$ ($1 + 3 = 4$) ✓.
</details>
<details><summary>Errores frecuentes</summary>Comparar los coeficientes de la forma general sin dividir: $4x - 2y = 6$ y $2x - y = -1$ no se reconocen como paralelas a simple vista.</details>

### F00-N5-03 · [C] Puntos y cortes de un plano 🎬

**Objetivo**: trabajar con ternas y planos (integra L02 y L03).
**Dificultad**: N5

**Enunciado.** a) ¿Están $(1, 2, 0)$ y $(2, 2, 1)$ en el plano $x + y + z = 3$? b) Encuentra el punto donde el plano $x + 2y - z = 4$ corta a cada eje.

<details><summary>Pista 1</summary>a) Sustituye.</details>
<details><summary>Pista 2</summary>b) Sobre el eje $x$ los puntos son de la forma $(x, 0, 0)$; análogamente para los otros ejes.</details>
<details><summary>Solución</summary>

a) $(1, 2, 0)$: $1 + 2 + 0 = 3$ ✓, está. $(2, 2, 1)$: $5 \neq 3$, no está.
b) Eje $x$ ($y = z = 0$): $x = 4$, punto $(4, 0, 0)$. Eje $y$ ($x = z = 0$): $2y = 4$, $(0, 2, 0)$. Eje $z$ ($x = y = 0$): $-z = 4$, $(0, 0, -4)$.

**Verificación**: cada punto cumple $x + 2y - z = 4$ (comprobado en `verificar/f00.py`).
</details>
<details><summary>Errores frecuentes</summary>Olvidar el signo de $-z$ y obtener $(0, 0, 4)$.</details>

---

## Lección 4 — Lenguaje matemático

### F00-N1-08 · [C] Conjuntos por extensión 🎬

**Objetivo**: leer la notación de conjuntos y escribir conjuntos solución.
**Dificultad**: N1

**Enunciado.** Escribe por extensión: a) $\{x \in \mathbb{R} : 3x - 1 = 5\}$ b) $\{x \in \mathbb{R} : x - 4 = x\}$ c) $\{n \in \mathbb{N} : n < 4\}$

<details><summary>Pista 1</summary>Lee cada conjunto en voz alta: "los $x$ reales tales que...".</details>
<details><summary>Pista 2</summary>b) Resta $x$ a ambos lados: ¿qué queda?</details>
<details><summary>Solución</summary>

a) $3x = 6$, $x = 2$: $\{2\}$.
b) $-4 = 0$ es falso para todo $x$: $\varnothing$.
c) $\{1, 2, 3\}$ (con $\mathbb{N} = \{1, 2, \dots\}$; si tu libro incluye el 0, $\{0, 1, 2, 3\}$).

**Verificación**: $3\cdot 2 - 1 = 5$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Escribir b) como $\{0\}$ o $\{\varnothing\}$ (este último es un conjunto con un elemento, no el vacío).</details>

### F00-N2-07 · [C] Sumatorios 🎬

**Objetivo**: desarrollar y escribir sumatorios.
**Dificultad**: N2

**Enunciado.** a) $\displaystyle\sum_{k=1}^{5} (2k - 1)$ b) $\displaystyle\sum_{j=1}^{3} a_j x_j$ con $a_1 = 2$, $a_2 = -1$, $a_3 = 3$, $x_1 = 1$, $x_2 = 4$, $x_3 = -2$ c) Escribe con $\Sigma$: $3 + 6 + 9 + 12$.

<details><summary>Pista 1</summary>Da al índice cada valor, de inicio a fin, y suma.</details>
<details><summary>Pista 2</summary>c) Cada sumando es 3 por algo.</details>
<details><summary>Solución</summary>

a) $1 + 3 + 5 + 7 + 9 = 25$.
b) $2\cdot 1 + (-1)\cdot 4 + 3 \cdot(-2) = 2 - 4 - 6 = -8$.
c) $\sum_{k=1}^{4} 3k$.

**Verificación**: comprobado en `verificar/f00.py`.
</details>
<details><summary>Errores frecuentes</summary>a) Empezar en $k = 0$; c) escribir $\sum_{k=3}^{12} k$ (suma todos los números del 3 al 12).</details>

### F00-N2-08 · [C] Doble subíndice

**Objetivo**: localizar $a_{ij}$ y desarrollar sumatorios con doble subíndice (anticipo de matrices).
**Dificultad**: N2

**Enunciado.** Considera la tabla
$$\begin{array}{ccc} a_{11} = 2 & a_{12} = -1 & a_{13} = 0 \\ a_{21} = 4 & a_{22} = 3 & a_{23} = -5 \\ a_{31} = 1 & a_{32} = 7 & a_{33} = 6 \end{array}$$
a) ¿Cuánto valen $a_{23}$ y $a_{32}$? b) Calcula $\sum_{j=1}^{3} a_{2j} x_j$ con $x_1 = 1$, $x_2 = 2$, $x_3 = -1$. c) Calcula $\sum_{i=1}^{3} a_{ii}$.

<details><summary>Pista 1</summary>Primer subíndice: fila. Segundo: columna.</details>
<details><summary>Pista 2</summary>b) Solo varía $j$: recorres la fila 2.</details>
<details><summary>Solución</summary>

a) $a_{23} = -5$ y $a_{32} = 7$.
b) $a_{21}x_1 + a_{22}x_2 + a_{23}x_3 = 4\cdot 1 + 3\cdot 2 + (-5)(-1) = 4 + 6 + 5 = 15$.
c) $a_{11} + a_{22} + a_{33} = 2 + 3 + 6 = 11$.

**Verificación**: comprobado en `verificar/f00.py`.
</details>
<details><summary>Errores frecuentes</summary>Recorrer la columna 2 en lugar de la fila 2 en b).</details>

### F00-N3-04 · [K] Necesaria, suficiente, ambas o ninguna 🎬

**Objetivo**: clasificar condiciones lógicas.
**Dificultad**: N3

**Enunciado.** ¿$P$ es condición necesaria, suficiente, ambas o ninguna para $Q$?
a) $P: x = 3$, $Q: x^2 = 9$ b) $P: x > 0$, $Q: x > 5$ c) $P: 2x = 6$, $Q: x = 3$

<details><summary>Pista 1</summary>Estudia por separado $P \Rightarrow Q$ (¿es $P$ suficiente?) y $Q \Rightarrow P$ (¿es $P$ necesaria?).</details>
<details><summary>Pista 2</summary>Busca contraejemplos para las implicaciones que te parezcan falsas.</details>
<details><summary>Solución</summary>

a) $P \Rightarrow Q$ es cierta; $Q \Rightarrow P$ es falsa ($x = -3$). $P$ es **suficiente, no necesaria**.
b) $P \Rightarrow Q$ es falsa ($x = 1$); $Q \Rightarrow P$ es cierta. $P$ es **necesaria, no suficiente**.
c) $2x = 6 \Leftrightarrow x = 3$. **Ambas**.

**Verificación**: los contraejemplos $x = -3$ y $x = 1$ se comprueban sustituyendo.
</details>
<details><summary>Errores frecuentes</summary>Invertir los papeles: en $P \Rightarrow Q$, la necesaria es $Q$, no $P$.</details>

### F00-N4-04 · [K] Contraejemplos

**Objetivo**: refutar afirmaciones generales que "parecen" ciertas.
**Dificultad**: N4

**Enunciado.** Da un contraejemplo para cada afirmación:
a) Si $a^2 = b^2$, entonces $a = b$.
b) Toda ecuación de la forma $ax = b$ tiene exactamente una solución.
c) $(a + b)^2 = a^2 + b^2$ para todos los reales.
d) Si $x < y$, entonces $x^2 < y^2$.

<details><summary>Pista 1</summary>Prueba con números negativos y con el 0.</details>
<details><summary>Pista 2</summary>b) Recuerda los tres casos de L02.</details>
<details><summary>Solución</summary>

a) $a = 1$, $b = -1$: $1 = 1$ pero $1 \neq -1$.
b) $a = 0$, $b = 1$: $0x = 1$ no tiene solución (o $a = b = 0$: infinitas).
c) $a = b = 1$: $(1 + 1)^2 = 4 \neq 2$.
d) $x = -3$, $y = 1$: $-3 < 1$, pero $9 > 1$.

**Verificación**: cada contraejemplo se comprueba sustituyendo.
</details>
<details><summary>Errores frecuentes</summary>Dar un ejemplo en el que la afirmación se cumple: eso no la refuta.</details>

### F00-N5-04 · [D] Demostrar y refutar 🎬

**Objetivo**: hacer una demostración directa y una refutación por contraejemplo.
**Dificultad**: N5

**Enunciado.** a) Demuestra que la suma de dos números impares es par. b) Refuta con un contraejemplo: "si $x^2 > 4$, entonces $x > 2$".

<details><summary>Pista 1</summary>Un número es impar si se escribe $2k + 1$ con $k$ entero.</details>
<details><summary>Pista 2</summary>b) Piensa en números negativos.</details>
<details><summary>Solución</summary>

a) Sean $a = 2k + 1$ y $b = 2m + 1$ con $k, m$ enteros. Entonces $a + b = 2k + 2m + 2 = 2(k + m + 1)$, y $k + m + 1$ es entero, así que $a + b$ es par. $\blacksquare$
b) $x = -3$: $x^2 = 9 > 4$, pero $-3 > 2$ es falso.

**Verificación**: ejemplo (no prueba): $3 + 5 = 8$.
</details>
<details><summary>Errores frecuentes</summary>Usar la misma letra para los dos impares ($a = 2k + 1$, $b = 2k + 1$): eso solo prueba que un impar más sí mismo es par.</details>
