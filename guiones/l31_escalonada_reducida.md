# L31 — Forma escalonada reducida (Gauss-Jordan)

**Objetivo**: definir la forma escalonada reducida, llegar a ella con el algoritmo de Gauss-Jordan y entender por qué es única.
**Prerrequisitos**: L24 (operaciones elementales), L25 (escalonada y pivotes), L26 (Gauss), L27–L28 (pivotes nulos, solución).
**Código**: `escenas/l31_escalonada_reducida.py`
**Videos**: `videos/l31_escalonada_reducida/1080p60/` → `DeEscalonadaAReducida.mp4`, `EliminarArribaYAbajo.mp4`, `LaReducidaEsUnica.mp4`
**Ejercicios**: F09-N1-01, F09-N1-02, F09-N2-01, F09-N2-02, F09-N3-01, F09-N3-02, F09-N3-03.

---

## Desarrollo matemático

**Definición.** Una matriz está en **forma escalonada reducida** si (1) es escalonada, (2) cada pivote vale $1$ y (3) cada pivote es la **única** entrada no nula de su columna. Las columnas sin pivote pueden contener cualquier número.

**Algoritmo de Gauss-Jordan.** (1) Eliminación hacia adelante hasta la forma escalonada. (2) Dividir cada fila no nula entre su pivote. (3) Hacer ceros encima de cada pivote, de derecha a izquierda. (4) Leer la solución. Cada cero de arriba es un paso de la sustitución hacia atrás, hecho sobre la matriz.

**Por qué de derecha a izquierda.** La fila de un pivote tiene ceros a su izquierda: al usarla, solo cambian su columna y las de la derecha, así que los ceros ya conseguidos no se estropean.

**Teorema (unicidad).** Toda matriz es equivalente por filas a **una única** matriz en forma escalonada reducida. Consecuencia: dos sistemas son equivalentes si y solo si sus matrices aumentadas tienen la misma reducida.

**Idea de la demostración.** (1) Si $M$ y $R$ son equivalentes por filas, $Mx = 0 \iff Rx = 0$: se conservan las relaciones entre columnas. (2) En una reducida, una columna es pivote si y solo si no es combinación de las anteriores, y cada columna sin pivote es la suma de las columnas pivote anteriores multiplicadas por sus propias entradas. (3) Dos reducidas equivalentes tendrían las mismas relaciones, luego las mismas columnas pivote y las mismas entradas. Los detalles requieren combinaciones lineales (Unidad 8).

---

## Guion de narración

### Video 1 — `DeEscalonadaAReducida`

| En pantalla | Narración |
|---|---|
| Escalonada de L26 y su reducida | "Esta es la forma escalonada del sistema de la lección veintiséis; para leer la solución hay que sustituir hacia atrás. Si seguimos operando, llegamos a otra matriz equivalente que se lee directamente: equis uno, ye menos uno, zeta dos. Es la forma escalonada reducida." |
| Definición | "Está en forma escalonada reducida si es escalonada, cada pivote vale uno, y cada pivote es la única entrada no nula de su columna: ceros arriba y abajo." |
| Cuatro ejemplos | "Sí; no, un pivote vale dos; no, encima del pivote hay un dos; sí, la columna sin pivote puede tener cualquier número." |

### Video 2 — `EliminarArribaYAbajo`

| En pantalla | Narración |
|---|---|
| $[A \mid b]$ del sistema de L15 | "Primero Gauss: ceros debajo del pivote, restando la fila uno a la dos y a la tres." |
| Pivotes a 1 | "Segundo, cada pivote a uno: multiplicamos las filas dos y tres por menos un medio." |
| Ceros encima | "Tercero, ceros encima de los pivotes, de derecha a izquierda: a la fila uno le restamos la tres y después la dos." |
| Lectura | "Ya está reducida: equis uno, ye dos, zeta tres." |
| Algoritmo y orden | "Los cuatro pasos del algoritmo. Y de derecha a izquierda porque la fila de un pivote tiene ceros a su izquierda: los ceros ya hechos no se estropean." |

### Video 3 — `LaReducidaEsUnica`

| En pantalla | Narración |
|---|---|
| Dos caminos | "La misma matriz, por dos caminos distintos, termina en la misma matriz reducida." |
| Teorema | "Toda matriz es equivalente por filas a una única matriz escalonada reducida. Dos sistemas son equivalentes si y solo si tienen la misma reducida." |
| Idea de la demostración | "Las operaciones por filas conservan las relaciones entre columnas; en una reducida esas relaciones determinan las entradas; luego dos reducidas equivalentes son iguales." |

---

## Errores frecuentes

- Olvidar los ceros encima de un pivote: eso es solo escalonada.
- Dejar un pivote distinto de $1$ (dividir la fila entera, $\mathbf{b}$ incluida).
- Creer que las columnas sin pivote deben ser ceros.
- Empezar los ceros de arriba por la izquierda y estropearlos después.

## Resumen y conexión

La reducida es la escalonada llevada al extremo: pivotes $1$ y ceros arriba y abajo. Es única, así que es la "huella" de un sistema. En la L32 la usaremos para leer la solución cuando hay variables libres.
