# L19 — Producto de una matriz por un vector: dos miradas

**Objetivo**: multiplicar una matriz por un vector, por filas y por columnas, y entender por qué ambas miradas coinciden.
**Prerrequisitos**: L04 (sumatorio), L16, L17.
**Código**: `escenas/l19_matriz_por_vector.py`
**Videos**: `videos/l19_matriz_por_vector/1080p60/` → `FilaPorColumna.mp4`, `ComoCombinacionDeColumnas.mp4`
**Ejercicios**: F06-N1-01, F06-N2-01.

---

## Desarrollo matemático

**Fila por columna (producto escalar).** $\begin{bmatrix} a_1 & \cdots & a_n \end{bmatrix}\begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} = \sum_{j=1}^n a_jx_j$: un número. Exige la misma longitud. Es el lado izquierdo de una ecuación lineal.

**Matriz por vector.** Si $A$ es $m\times n$ y $\mathbf{x}$ tiene $n$ componentes:
$$(A\mathbf{x})_i = \sum_{j=1}^{n} a_{ij}x_j, \qquad i = 1, \dots, m.$$
Cada fila de $A$ por $\mathbf{x}$ da una componente; $(m\times n)(n\times 1) = m\times 1$. Si las columnas de $A$ no coinciden con las componentes de $\mathbf{x}$, no está definido.

Ejemplo: $\begin{bmatrix} 1 & 2 & 0 \\ 3 & -1 & 4 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$.

**Por columnas.** Si $\mathbf{a}_1, \dots, \mathbf{a}_n$ son las columnas de $A$:
$$A\mathbf{x} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n.$$
Ejemplo: $2(1, 3) + 1(2, -1) + (-1)(0, 4) = (4, 1)$.

*Por qué coinciden*: la componente $i$ de las dos expresiones es $a_{i1}x_1 + \cdots + a_{in}x_n$, la misma suma leída de dos maneras.

Filas para **calcular**; columnas para **interpretar** ($A\mathbf{x}$ es una combinación lineal de las columnas).

---

## Guion de narración

### Video 1 — `FilaPorColumna`

| En pantalla | Narración |
|---|---|
| Parejas de colores fila-columna | "Para multiplicar una fila por una columna emparejamos primero con primero, segundo con segundo..., multiplicamos y sumamos. El resultado es un solo número." |
| $A\mathbf{x}$ entrada a entrada | "Para multiplicar una matriz por un vector, cada fila de la matriz se multiplica por el vector. La fila uno da la primera componente; la fila dos, la segunda." |
| Regla de dimensiones | "El número de columnas de A debe coincidir con el número de componentes de equis; el resultado tiene tantas componentes como filas tiene A." |

### Video 2 — `ComoCombinacionDeColumnas`

| En pantalla | Narración |
|---|---|
| Expansión por columnas | "Otra forma de ver el mismo producto: las componentes de equis son pesos para las columnas de A. Dos veces la primera, una vez la segunda y menos una la tercera dan el mismo resultado: cuatro, uno." |
| Columnas encadenadas en el plano | "En el dibujo, cada columna estirada por su peso, una tras otra, nos lleva a A equis." |
| Dos miradas | "Por filas es más cómodo para calcular; por columnas, para entender. Las dos son la misma suma." |

---

## Errores frecuentes

- Multiplicar columna de $A$ por $\mathbf{x}$ "en vertical".
- No comprobar dimensiones.
- Olvidar signos al multiplicar.

## Resumen y conexión

$A\mathbf{x}$ se calcula por filas y se interpreta por columnas. En la Lección 20 multiplicamos matrices entre sí: columna a columna, es lo mismo.
