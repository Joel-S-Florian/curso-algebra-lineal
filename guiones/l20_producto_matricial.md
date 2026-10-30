# L20 — Producto de matrices

**Objetivo**: saber cuándo se pueden multiplicar dos matrices, calcular el producto y conocer qué propiedades se conservan y cuáles no.
**Prerrequisitos**: L19.
**Código**: `escenas/l20_producto_matricial.py`
**Videos**: `videos/l20_producto_matricial/1080p60/` → `DimensionesYProcedimiento.mp4`, `NoConmutatividadEIdentidad.mp4`
**Ejercicios**: F06-N2-02, F06-N2-03, F06-N3-01, F06-N4-01.

---

## Desarrollo matemático

**Dimensiones.** $(m\times n)(n\times p) = m\times p$. Los números "de dentro" deben coincidir (columnas de $A$ = filas de $B$); los "de fuera" dan la dimensión del resultado.

**Definición.**
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj} = (\text{fila } i \text{ de } A)\cdot(\text{columna } j \text{ de } B).$$
Equivalentemente, la columna $j$ de $AB$ es $A\mathbf{b}_j$: $AB = [\,A\mathbf{b}_1 \ \cdots \ A\mathbf{b}_p\,]$.

Ejemplo: $\begin{bmatrix} 1 & 2 & 0 \\ -1 & 3 & 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \\ 0 & -1 \\ 4 & 2 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ 2 & -2 \end{bmatrix}$.

**Lo que NO se cumple.**

- $AB \neq BA$ en general (ejemplo: $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, $B = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$). A veces ni siquiera tienen la misma dimensión.
- $AB = O$ no implica $A = O$ o $B = O$: $\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = O$.
- $AB = AC$ no implica $B = C$.
- $(AB)_{ij} \neq a_{ij}b_{ij}$.

**Lo que sí se cumple** (con dimensiones compatibles): $(AB)C = A(BC)$; $A(B + C) = AB + AC$; $(A + B)C = AC + BC$; $c(AB) = (cA)B = A(cB)$; $I_mA = A = AI_n$.

---

## Guion de narración

### Video 1 — `DimensionesYProcedimiento`

| En pantalla | Narración |
|---|---|
| $(m\times n)(n\times p) = m\times p$ | "Para multiplicar dos matrices, los números de dentro deben coincidir: columnas de la primera, filas de la segunda. Los de fuera dan el tamaño del resultado." |
| Cuatro productos fila-columna | "El elemento i jota del producto es la fila i de A por la columna jota de B. Así, entrada a entrada." |
| $AB = [A\mathbf{b}_1\ A\mathbf{b}_2]$ | "Otra forma: cada columna del producto es A por la columna correspondiente de B." |

### Video 2 — `NoConmutatividadEIdentidad`

| En pantalla | Narración |
|---|---|
| $AB$ y $BA$ distintas | "Cambiar el orden cambia el resultado: el producto de matrices no es conmutativo." |
| Propiedades que sí se cumplen | "Pero sí es asociativo y distributivo, y la identidad hace el papel del uno." |
| Identidad en acción | "Los ceros de la identidad anulan todos los términos menos uno: cada fila queda igual." |
| $AB = O$ con $A, B \neq O$ | "Y un aviso: con matrices, un producto puede ser cero sin que ningún factor lo sea. Por eso no se puede 'simplificar' como con números." |

---

## Errores frecuentes

- Multiplicar posición a posición.
- Suponer $AB = BA$ (por ejemplo, $(A + B)^2 = A^2 + 2AB + B^2$).
- Comparar las dimensiones "de fuera".
- "Dividir" entre una matriz.

## Resumen y conexión

$(AB)_{ij}$ = fila $i$ por columna $j$; el orden importa. En la Lección 21 vemos qué *hace* una matriz: transforma el plano.
