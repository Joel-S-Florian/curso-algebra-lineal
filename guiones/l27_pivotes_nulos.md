# L27 — Pivotes nulos y filas nulas

**Objetivo**: resolver un pivote nulo con un intercambio, reconocer una columna sin pivote, e interpretar una fila nula como ecuación redundante.
**Prerrequisitos**: L24–L26, L12 (más ecuaciones que incógnitas).
**Código**: `escenas/l27_pivotes_nulos.py`
**Videos**: `videos/l27_pivotes_nulos/1080p60/` → `PivoteCeroIntercambio.mp4`, `FilaNulaEcuacionRedundante.mp4`
**Ejercicios**: F08-N2-05, F08-N3-02 (en video).

---

## Desarrollo matemático

**Pivote nulo.** Si en la posición del pivote hay un 0, el multiplicador $m = a/0$ no existe. Se busca **más abajo**, en esa columna, una fila con entrada no nula y se intercambia. El intercambio es elemental (conserva soluciones) y no estropea ceros: las dos filas tienen 0 en las columnas ya trabajadas. No se sube una fila de arriba: ya tiene su pivote.

**Ejemplo.** $\left[\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 2 & 2 & 1 & 5 \\ 1 & 2 & 3 & 6 \end{array}\right] \xrightarrow[R_3 \leftarrow R_3 - R_1]{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & 0 & -1 & -1 \\ 0 & 1 & 2 & 3 \end{array}\right] \xrightarrow{R_2 \leftrightarrow R_3} \left[\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & -1 & -1 \end{array}\right]$: $z = 1$, $y = 1$, $x = 1$.

**Columna sin pivote.** Si de la fila actual hacia abajo toda la columna es 0, esa columna no tiene pivote y se pasa a la siguiente. En $\left[\begin{array}{ccc|c} 1 & 2 & 1 & 4 \\ 0 & 0 & 3 & 3 \\ 0 & 0 & 1 & 1 \end{array}\right]$ el pivote de la fila 2 es el 3; $R_3 \leftarrow R_3 - \frac13 R_2$ anula la fila 3. La $y$ queda sin pivote (variable libre, L28).

**Fila nula.** Una fila $[\,0 \cdots 0 \mid 0\,]$ es $0 = 0$: la cumple todo, no aporta información y se puede quitar sin cambiar el conjunto solución. Indica que una ecuación era combinación de las demás.

**Ejemplo.** $x + y = 3$, $x - y = 1$, $3x + y = 7$: $R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - 3R_1$, $R_3 \leftarrow R_3 - R_2$ dejan $[\,0 \ \ 0 \mid 0\,]$. Solución única $(2, 1)$ con 2 pivotes para 2 incógnitas. Rastreando: $R_3^{\text{final}} = (R_3 - 3R_1) - (R_2 - R_1) = R_3 - 2R_1 - R_2 = \mathbf{0}$, luego $E_3 = 2E_1 + E_2$. En el plano: tres rectas por $(2, 1)$.

**Contraste.** Si la tercera fuera $3x + y = 8$, la última fila sería $[\,0 \ \ 0 \mid 1\,]$: $0 = 1$, sin solución. Solo es redundante una fila nula **entera**.

---

## Guion de narración

### Video 1 — `PivoteCeroIntercambio`

| En pantalla | Narración |
|---|---|
| $m = 1/0$ | "Con un cero en el lugar del pivote no hay multiplicador. El remedio: intercambiar con una fila de más abajo." |
| Cero a mitad de camino | "Después de la columna uno, el pivote de la columna dos debería estar en la fila dos, pero vale cero. Debajo hay un uno: intercambiamos y la matriz queda escalonada." |
| Por qué es seguro | "Es una operación elemental, y las dos filas ya tenían ceros en las columnas trabajadas." |
| Columna entera de ceros | "Si toda la columna es cero hacia abajo, no hay pivote: la escalera salta a la columna siguiente." |

### Video 2 — `FilaNulaEcuacionRedundante`

| En pantalla | Narración |
|---|---|
| Eliminación con fila nula | "Tres ecuaciones, dos incógnitas. Al final queda una fila de ceros: cero igual a cero, que no dice nada." |
| Rastreo | "La fila tres final es la tres menos dos veces la uno menos la dos: la tercera ecuación era combinación de las otras." |
| Tres rectas | "En el plano, la tercera recta pasa por el punto donde ya se cortaban las dos primeras." |
| Contraste con $0 = 1$ | "Si el término independiente no se anula, no es redundante: es imposible." |

---

## Errores frecuentes

- Concluir "sin solución" al ver un pivote 0.
- Intercambiar con una fila de arriba.
- Intercambiar solo los coeficientes, no la fila entera.
- Leer una fila nula como "sin solución".
- Clasificar contando ecuaciones en lugar de pivotes.

## Resumen y conexión

Un pivote nulo se arregla con un intercambio hacia abajo; si no se puede, la columna queda sin pivote. Una fila nula es una ecuación redundante. En la L28 vemos las dos situaciones que esto anuncia: la fila $[\,0 \cdots 0 \mid c\,]$ y las variables libres.
