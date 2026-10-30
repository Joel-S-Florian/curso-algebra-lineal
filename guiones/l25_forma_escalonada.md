# L25 — Forma escalonada y pivotes

**Objetivo**: reconocer la forma escalonada, localizar pivotes, columnas pivote y variables pivote, y entender que la forma escalonada no es única.
**Prerrequisitos**: L23, L24.
**Código**: `escenas/l25_forma_escalonada.py` (usa `escalera`, `matriz_gauss`, `operar_filas`)
**Videos**: `videos/l25_forma_escalonada/1080p60/` → `FormaEscalonadaYPivotes.mp4`, `LaEscalonadaNoEsUnica.mp4`
**Ejercicios**: F08-N1-02, F08-N2-02 (en video).

---

## Desarrollo matemático

**Definición.** Una matriz está en forma escalonada si (1) las filas nulas, si las hay, están abajo, y (2) la primera entrada no nula de cada fila está estrictamente más a la derecha que la de la fila de arriba. Esa entrada es el **pivote** de la fila. Consecuencia de (2): debajo de cada pivote solo hay ceros.

- Los pivotes solo tienen que ser distintos de 0 (no iguales a 1; eso llega con la forma reducida, L31).
- La "escalera" puede saltar columnas, y la matriz puede empezar con columnas nulas.

**Ejemplos.** $\begin{bmatrix} 1 & 3 & 2 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{bmatrix}$ sí (pivotes en columnas 1 y 3); $\begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 4 & 5 \end{bmatrix}$ no (fila nula arriba); $\begin{bmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 0 & 1 \end{bmatrix}$ no (bajo el 2 hay un 1); $\begin{bmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{bmatrix}$ sí.

**Columnas y variables pivote.** Una columna pivote contiene un pivote; su incógnita es una variable pivote. En
$\left[\begin{array}{cccc|c} 1 & 2 & 0 & -1 & 3 \\ 0 & 0 & 2 & 4 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$
las variables pivote son $x_1, x_3$; $x_2, x_4$ no tienen pivote (serán libres, L28).

**Pivote en la columna de $\mathbf{b}$.** $\left[\begin{array}{cc|c} 1 & 2 & 3 \\ 0 & 0 & 5 \end{array}\right]$ está escalonada, pero su segunda fila es $0 = 5$: sistema sin solución (L28).

**No unicidad.** Desde $\left[\begin{array}{cc|c} 2 & 4 & 10 \\ 3 & -1 & 1 \end{array}\right]$:
camino A, $R_2 \leftarrow R_2 - \frac32 R_1$: $\left[\begin{array}{cc|c} 2 & 4 & 10 \\ 0 & -7 & -14 \end{array}\right]$;
camino B, $R_1 \leftrightarrow R_2$ y $R_2 \leftarrow R_2 - \frac23 R_1$: $\left[\begin{array}{cc|c} 3 & -1 & 1 \\ 0 & \frac{14}{3} & \frac{28}{3} \end{array}\right]$.
Son distintas, pero equivalentes (L24): misma solución $(1, 2)$. Además los pivotes ocupan las mismas posiciones. Este último hecho es general (todas las formas escalonadas de una matriz tienen los pivotes en las mismas posiciones); se demuestra en la L31 a partir de la unicidad de la forma escalonada reducida, y el número de pivotes será el rango (Unidad 7).

---

## Guion de narración

### Video 1 — `FormaEscalonadaYPivotes`

| En pantalla | Narración |
|---|---|
| Escalera sobre la matriz de la L23 | "Esta es la forma a la que queremos llegar: bajo la escalera solo hay ceros y cada fila empieza más a la derecha. Por eso se resuelve de abajo arriba." |
| Definición | "Filas nulas abajo; cada pivote, a la derecha del de arriba. El pivote es la primera entrada no nula de la fila." |
| Cuatro ejemplos | "Esta sí: la escalera puede saltar columnas. Esta no: hay una fila nula en medio. Esta no: debajo del dos hay un uno. Esta sí: puede empezar con ceros." |
| Variables pivote | "Las columnas uno y tres tienen pivote: equis uno y equis tres son variables pivote. Equis dos y equis cuatro no lo tienen; serán libres." |
| Pivote en $\mathbf{b}$ | "Si el último pivote cae en la columna de be, la ecuación dice cero igual a cinco." |

### Video 2 — `LaEscalonadaNoEsUnica`

| En pantalla | Narración |
|---|---|
| Dos caminos | "Desde la misma matriz, dos caminos llevan a dos escalonadas distintas." |
| Soluciones | "Las dos dan y igual a dos, equis igual a uno: son equivalentes." |
| Qué cambia | "Cambian los números; no cambian las soluciones ni las posiciones de los pivotes. Elegir bien el pivote solo ahorra fracciones." |

---

## Errores frecuentes

- Exigir pivotes iguales a 1.
- Pensar que la escalera baja una columna por fila.
- Llamar pivote a cualquier entrada no nula.
- Dejar filas nulas en medio.
- Creer que una escalonada distinta de la del profesor está mal.

## Resumen y conexión

La forma escalonada tiene filas nulas abajo y pivotes en escalera; no es única, pero sus pivotes sí. En la L26 vemos el procedimiento para llegar a ella (eliminación hacia adelante) y cómo resolver después (sustitución hacia atrás).
