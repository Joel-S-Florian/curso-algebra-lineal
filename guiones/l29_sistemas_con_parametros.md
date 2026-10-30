# L29 — Sistemas con parámetros

**Objetivo**: aplicar Gauss a sistemas con un parámetro y discutirlos por casos sin dividir nunca por una expresión que pueda valer 0.
**Prerrequisitos**: L06 (los tres casos de $ax = b$), L24–L28.
**Código**: `escenas/l29_sistemas_con_parametros.py` (usa `operar_filas(..., nueva=...)` para filas con parámetros)
**Videos**: `videos/l29_sistemas_con_parametros/1080p60/` → `GaussConParametro.mp4`, `DiscutirPorCasos.mp4`
**Ejercicios**: F08-N4-03, F08-N4-04 (en video); F08-N4-05.

---

## Desarrollo matemático

**Qué operaciones son seguras.** Sumar a una fila $k$ veces otra es siempre legal, aunque $k$ dependa del parámetro (con $k = 0$ la fila no cambia, y la inversa sigue existiendo). Intercambiar, también. Multiplicar o dividir una fila por una expresión como $a - 2$ solo es legal si $a - 2 \neq 0$: antes hay que separar el caso $a = 2$. Lo mismo para despejar.

**Ejemplo 2 × 2.** $x + y = 1$, $2x + ay = 3$. $R_2 \leftarrow R_2 - 2R_1$ da $[\,0 \ \ a - 2 \mid 1\,]$.

- $a \neq 2$: $a - 2$ es pivote, SCD: $y = \frac{1}{a - 2}$, $x = 1 - y = \frac{a - 3}{a - 2}$.
- $a = 2$: $[\,0 \ \ 0 \mid 1\,]$, SI (rectas paralelas $x + y = 1$, $2x + 2y = 3$).

Verificación: $x + y = \frac{a - 2}{a - 2} = 1$ y $2x + ay = \frac{3a - 6}{a - 2} = 3$ (simplificar es legítimo porque $a \neq 2$); con $a = 3$, $(0, 1)$.

**Ejemplo 3 × 3.** $x + y + z = 1$, $x + 2y + 2z = 2$, $x + 2y + (a^2 + 1)z = a + 1$. Con $R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - R_1$, $R_3 \leftarrow R_3 - R_2$:
$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & a^2 - 1 & a - 1 \end{array}\right], \qquad a^2 - 1 = (a - 1)(a + 1).$$

- $a \neq \pm 1$: SCD, $z = \frac{a - 1}{a^2 - 1} = \frac{1}{a + 1}$, $y = 1 - z = \frac{a}{a + 1}$, $x = 1 - y - z = 0$.
- $a = 1$: última fila nula, SCI: $(x, y, z) = (0, 1 - t, t)$.
- $a = -1$: $[\,0 \ \ 0 \ \ 0 \mid -2\,]$, SI.

**La trampa.** Escribir directamente $z = \frac{1}{a + 1}$ (simplificando entre $a - 1$) hace creer que solo $a = -1$ es especial y pierde el caso $a = 1$, que tiene infinitas soluciones.

**Verificación.** Para $a \neq \pm 1$: $E_1$ y $E_2$ se cumplen porque $x = 0$ e $y + z = 1$; $E_3 = 2\frac{a}{a + 1} + (a^2 + 1)\frac{1}{a + 1} = \frac{(a + 1)^2}{a + 1} = a + 1$. Con $a = 0$, $(0, 0, 1)$. Con $a = 1$, $E_3 = 2(1 - t) + 2t = 2$.

---

## Guion de narración

### Video 1 — `GaussConParametro`

| En pantalla | Narración |
|---|---|
| Sistema con $a$ | "a es un número fijo pero desconocido: hay que responder para cada valor." |
| $[\,0 \ \ a - 2 \mid 1\,]$ | "¿Es a menos dos un pivote? Solo si no vale cero. Antes de dividir, separamos el caso a igual a dos." |
| Casos | "Si a es distinto de dos, solución única. Si a vale dos, sustituimos en toda la matriz: cero igual a uno, sin solución." |
| Operaciones seguras | "Sumar múltiplos de otra fila es siempre legal; multiplicar o dividir por a menos dos, solo si no es cero." |

### Video 2 — `DiscutirPorCasos`

| En pantalla | Narración |
|---|---|
| Eliminación | "Eliminamos hasta que el parámetro queda en el último candidato a pivote: a al cuadrado menos uno." |
| Factorización | "Se anula en uno y en menos uno: son los valores que hay que estudiar aparte." |
| Tres casos | "Para a distinto de más y menos uno, una solución. Para a igual a uno, infinitas. Para a igual a menos uno, ninguna." |
| La trampa | "Si simplificamos antes de discutir, perdemos el caso a igual a uno." |
| Verificación | "Comprobamos cada caso en el sistema original." |

---

## Errores frecuentes

- Escribir $y = \frac{1}{a - 2}$ sin "si $a \neq 2$".
- Multiplicar una fila por $a - 2$ o dividir por $a$ sin discutir.
- Simplificar fracciones con parámetro antes de separar los casos.
- No hallar todas las raíces del candidato a pivote.
- Estudiar el caso especial sustituyendo solo en $A$ y no en $\mathbf{b}$.

## Resumen y conexión

Con parámetros, Gauss funciona igual, pero cada candidato a pivote puede anularse: se separan todos esos valores y cada caso se clasifica con la forma escalonada. En la L30 recopilamos los errores más frecuentes de toda la unidad y cómo verificar.
