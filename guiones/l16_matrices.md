# L16 — Matrices: dimensión, filas, columnas, elementos y tipos

**Objetivo**: saber qué es una matriz, leer su dimensión y sus elementos $a_{ij}$, y reconocer los tipos que se usan en el curso.
**Prerrequisitos**: L04 (subíndices).
**Código**: `escenas/l16_matrices.py`
**Videos**: `videos/l16_matrices/1080p60/` → `QueEsUnaMatriz.mp4`, `TiposDeMatrices.mp4`
**Ejercicios**: F05-N1-01, F05-N1-02, F05-N2-03.

---

## Desarrollo matemático

**Matriz.** Tabla rectangular de números ordenados en filas (horizontales) y columnas (verticales). Si tiene $m$ filas y $n$ columnas, su **dimensión** es $m\times n$ (se lee "$m$ por $n$"; siempre primero las filas).

**Elementos.** $a_{ij}$ es el número de la fila $i$ y la columna $j$. Notación: $A = [a_{ij}]_{m\times n}$. Ejemplo: en $A = \begin{bmatrix} 4 & -1 & 0 & 7 \\ 2 & 5 & 3 & -2 \\ 1 & 0 & 6 & 8 \end{bmatrix}$ ($3\times 4$), $a_{23} = 3$, $a_{32} = 0$, $a_{14} = 7$.

**Igualdad.** $A = B$ si tienen la misma dimensión y $a_{ij} = b_{ij}$ para toda posición. Una igualdad de matrices equivale a muchas igualdades de números.

**Tipos.**

| Tipo | Condición |
|---|---|
| Cuadrada | $m = n$; su **diagonal principal** son los $a_{ii}$ |
| Rectangular | $m \neq n$ |
| Nula $O$ | todos los $a_{ij} = 0$ (cualquier dimensión) |
| Identidad $I_n$ | cuadrada, 1 en la diagonal y 0 fuera |
| Diagonal | cuadrada, $a_{ij} = 0$ si $i \neq j$ |
| Triangular superior | cuadrada, $a_{ij} = 0$ si $i > j$ (ceros debajo de la diagonal) |
| Triangular inferior | cuadrada, $a_{ij} = 0$ si $i < j$ (ceros encima) |

Una matriz puede ser de varios tipos: la identidad es diagonal y triangular superior e inferior. Las triangulares serán protagonistas de Gauss (forma escalonada) y de LU.

---

## Guion de narración

### Video 1 — `QueEsUnaMatriz`

| En pantalla | Narración |
|---|---|
| Tabla de ventas → matriz | "Una tabla de ventas: cada fila es una tienda y cada columna un producto. Si quitamos los rótulos y nos quedamos con los números en su sitio, tenemos una matriz." |
| Fila 2 y columna 3 resaltadas; llaves 3 y 4 | "Las filas son horizontales y las columnas verticales. Esta matriz tiene tres filas y cuatro columnas: es de dimensión tres por cuatro. Siempre se dice primero el número de filas." |
| Cruces fila-columna para $a_{23}$, $a_{32}$, $a_{14}$ | "El elemento a sub i jota está donde se cruzan la fila i y la columna jota. a dos tres vale tres; a tres dos vale cero: el orden importa." |
| Igualdad de matrices | "Dos matrices son iguales si tienen la misma dimensión y el mismo número en cada posición. Por eso una igualdad de matrices son muchas igualdades a la vez." |

### Video 2 — `TiposDeMatrices`

| En pantalla | Narración |
|---|---|
| Cuadrada y rectangular; diagonal principal | "Si tiene tantas filas como columnas es cuadrada. En una cuadrada, los elementos con fila igual a columna forman la diagonal principal." |
| Cinco tarjetas | "La matriz nula tiene todo ceros. La identidad, unos en la diagonal y ceros fuera. Una diagonal solo puede tener números distintos de cero en la diagonal. Una triangular superior tiene ceros debajo de la diagonal; una inferior, encima." |
| Varios tipos a la vez | "Una misma matriz puede pertenecer a varios tipos: la identidad es diagonal, triangular superior e inferior." |

---

## Errores frecuentes

- Decir la dimensión al revés (columnas × filas).
- Confundir $a_{ij}$ con $a_{ji}$.
- Creer que la identidad existe para matrices rectangulares.
- Pensar que una matriz diagonal no puede tener ceros en la diagonal.

## Resumen y conexión

Una matriz es una tabla de números con dimensión $m\times n$. En la Lección 17 estudiamos las matrices de una sola columna: los vectores.
