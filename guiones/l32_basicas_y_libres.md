# L32 — Variables básicas y libres: leer la solución

**Objetivo**: leer directamente la solución de un sistema a partir de su forma reducida, con variables básicas y libres, y clasificar el sistema (SCD, SCI, SI) por sus pivotes.
**Prerrequisitos**: L28 (variables libres), L31 (forma reducida).
**Código**: `escenas/l32_basicas_y_libres.py`
**Videos**: `videos/l32_basicas_y_libres/1080p60/` → `LeerLaSolucion.mp4`, `TresFinalesPosibles.mp4`
**Ejercicios**: F09-N2-03, F09-N2-04, F09-N3-04, F09-N4-01, F09-N4-02, F09-N5-01.

---

## Desarrollo matemático

**Básicas y libres.** En la reducida de $[A \mid \mathbf{b}]$, las columnas con pivote dan las **variables básicas**; las columnas sin pivote, las **variables libres**. Cada libre recibe un parámetro; cada básica se despeja de la fila de su pivote: $x_{\text{básica}} = b_i - \sum (\text{entrada})\cdot(\text{libre})$.

**Forma vectorial.** La solución es un vector fijo (los valores con todas las libres $= 0$: la columna $\mathbf{b}$ de la reducida) más un múltiplo de un vector por cada libre: tiene un $1$ en la posición de su libre y, en las posiciones básicas, la columna de esa libre cambiada de signo. Ejemplo: $[\,1\ 2\ 0\ {-1} \mid 3\,]$, $[\,0\ 0\ 1\ 4 \mid 2\,]$ da $(3, 0, 2, 0) + s(-2, 1, 0, 0) + t(1, 0, -4, 1)$.

**Número de parámetros** $= n - r$ (incógnitas menos pivotes).

**Tres finales.** (1) Pivote en la columna de $\mathbf{b}$ ⇒ incompatible (SI). (2) Si no, pivote en cada columna de incógnitas ⇒ una solución (SCD). (3) Si no, alguna libre ⇒ infinitas (SCI), con $n - r$ parámetros. Como $r \le m$ y $r \le n$: con $m < n$ nunca hay una única solución. El número $r$ de pivotes se llamará **rango** (Unidad 7).

---

## Guion de narración

### Video 1 — `LeerLaSolucion`

| En pantalla | Narración |
|---|---|
| Reducida con columnas pivote y no pivote | "Las columnas con pivote dan las variables básicas; las que no, las variables libres." |
| Parámetros y despeje fila a fila | "Cada libre recibe un parámetro; cada básica se despeja de su fila. La fila de ceros no dice nada." |
| Forma vectorial | "Un vector fijo, la columna de be, más un vector por cada libre: un uno en su posición, y la columna de esa libre cambiada de signo en las básicas." |
| Verificación y cuenta | "Se verifica con valores concretos y con los parámetros generales. Incógnitas menos pivotes: parámetros." |

### Video 2 — `TresFinalesPosibles`

| En pantalla | Narración |
|---|---|
| Tres reducidas | "Un pivote por incógnita, ninguno en be: una solución. Alguna incógnita sin pivote: infinitas. Pivote en la columna de be: incompatible." |
| Tres preguntas | "¿Pivote en be? ¿Pivote en cada incógnita? Si no, infinitas, con ene menos erre parámetros." |
| Lo que explican los pivotes | "Con menos ecuaciones que incógnitas nunca hay una única solución. Lo que cuenta son los pivotes, no las ecuaciones: el rango." |

---

## Errores frecuentes

- Tomar como libre una variable con pivote (libres son las columnas **sin** pivote).
- Dar un valor a la libre y decir que la solución es única.
- Mirar las columnas de incógnitas antes de comprobar si hay un pivote en la de $\mathbf{b}$.
- Contar ecuaciones en lugar de pivotes para saber cuántos parámetros hay.

## Resumen y conexión

La reducida convierte la solución en una lectura: básicas, libres, parámetros y vector fijo. Los pivotes deciden el tipo de sistema. La L33 compara el coste de llegar a ella frente a la eliminación de Gauss.
