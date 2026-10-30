# L42 — Discusión con parámetros y clasificación sin resolver

**Objetivo**: discutir sistemas con parámetros usando los rangos, y distinguir "cuadrada" de "invertible".
**Prerrequisitos**: L29 (sistemas con parámetros), L40–L41.
**Código**: `escenas/l42_discusion_con_parametros.py`
**Videos**: `videos/l42_discusion_con_parametros/1080p60/` → `DiscusionConParametro.mp4`, `ClasificarSinResolver.mp4`
**Ejercicios**: F11-N3-05, F11-N4-05, F11-N4-06, F11-N5-01.

---

## Desarrollo matemático

**Receta.** (1) Escalonar $[A \mid \mathbf{b}]$ sin dividir por expresiones que puedan valer $0$. (2) Hallar los valores que anulan cada candidato a pivote. (3) Para cada caso, sustituir en toda la matriz y calcular $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$. (4) Aplicar Rouché-Frobenius.

**Ejemplo 1.** $x + y = 1$, $x + ay = b \to [\,0\ \ a - 1 \mid b - 1\,]$: $a \ne 1$: SCD; $a = 1$, $b = 1$: SCI (1 parámetro); $a = 1$, $b \ne 1$: SI.

**Ejemplo 2.** $x + y + z = 1$, $x + 2y + 3z = 2$, $x + 3y + 5z = k \to [\,0\ 0\ 0 \mid k - 3\,]$: $k = 3$: SCI, $(t,\ 1 - 2t,\ t)$; $k \ne 3$: SI; nunca SCD.

**Cuadrada no es invertible.** $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ es $2 \times 2$ con $\operatorname{rg}(A) = 1 < 2$: nunca SCD. Con $\operatorname{rg}(A) = n$ el sistema es SCD para todo $\mathbf{b}$ (invertibilidad: Unidad 8).

---

## Guion de narración

### Video 1 — `DiscusionConParametro`

| En pantalla | Narración |
|---|---|
| Sistema con $a$ y $b$ | "Discutir es clasificar para cada valor de los parámetros. Restamos la fila uno a la dos." |
| Tres casos | "a distinto de uno: determinado. a uno y be uno: indeterminado. a uno y be distinto de uno: incompatible." |
| Receta | "Escalonar sin dividir por lo que puede valer cero, estudiar los valores críticos, calcular los dos rangos y aplicar el teorema." |

### Video 2 — `ClasificarSinResolver`

| En pantalla | Narración |
|---|---|
| Parámetro $k$ | "La última fila queda cero, cero, cero, ka menos tres: con ka igual a tres, indeterminado; si no, incompatible." |
| Solución | "Para ka igual a tres, la solución es te, uno menos dos te, te." |
| Cuadrada | "Que la matriz sea cuadrada no significa que sea invertible: hace falta rango ene." |

---

## Errores frecuentes

- Dividir por un parámetro sin estudiar el caso en que vale $0$.
- Olvidar un subcaso (como $a = 1$, $b = 1$).
- Creer que un sistema cuadrado es siempre SCD.

## Resumen y conexión

Los parámetros se estudian con los mismos dos rangos y $n$. En la Unidad 8 pasamos de resolver a entender la estructura: combinaciones lineales, núcleo e imagen.
