# L21 — La matriz como transformación lineal del plano

**Objetivo**: ver una matriz $2\times 2$ como una transformación del plano, entender que sus columnas son las imágenes de $\mathbf{e}_1$ y $\mathbf{e}_2$, y saber qué significa "lineal".
**Prerrequisitos**: L17, L19.
**Código**: `escenas/l21_transformaciones.py`
**Videos**: `videos/l21_transformaciones/1080p60/` → `LaRejillaSeDeforma.mp4`, `ColumnasSonImagenesDeLaBase.mp4`, `QueSignificaLineal.mp4`
**Ejercicios**: F06-N1-02, F06-N3-02, F06-N5-01, F06-N5-02.

---

## Desarrollo matemático

**Transformación.** Una matriz $A$ de $2\times 2$ mueve cada punto $\mathbf{x}$ del plano al punto $A\mathbf{x}$. Ejemplos: $\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ (cizalla: $(1, 2) \mapsto (3, 2)$), $\begin{bmatrix} 2 & -1 \\ 1 & 1 \end{bmatrix}$.

Observación visual: las rectas siguen siendo rectas, las paralelas siguen paralelas y equiespaciadas, y el origen queda fijo ($A\mathbf{0} = \mathbf{0}$).

**Columnas.** Con $\mathbf{e}_1 = (1, 0)$ y $\mathbf{e}_2 = (0, 1)$: $A\mathbf{e}_1$ es la columna 1 de $A$ y $A\mathbf{e}_2$ la columna 2 (en general, $A\mathbf{e}_j$ es la columna $j$: F06-N5-02). Como $\mathbf{x} = x_1\mathbf{e}_1 + x_2\mathbf{e}_2$, $A\mathbf{x} = x_1A\mathbf{e}_1 + x_2A\mathbf{e}_2$: conocer adónde van $\mathbf{e}_1$ y $\mathbf{e}_2$ determina $A$. Ejemplo: $A(1, 2) = 1(2, 1) + 2(-1, 1) = (0, 3)$.

**Definición.** Una transformación $T$ es **lineal** si para todos los vectores $\mathbf{u}, \mathbf{v}$ y números $c$:
$$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}), \qquad T(c\mathbf{u}) = cT(\mathbf{u}).$$

**Teorema.** $\mathbf{x} \mapsto A\mathbf{x}$ es lineal (para $A$ de cualquier dimensión).
*Demostración.* $\big(A(\mathbf{u} + \mathbf{v})\big)_i = \sum_j a_{ij}(u_j + v_j) = \sum_j a_{ij}u_j + \sum_j a_{ij}v_j$, y $\big(A(c\mathbf{u})\big)_i = c\sum_j a_{ij}u_j$. $\blacksquare$

**No lineales**: transformaciones que curvan rectas, o traslaciones ($T(\mathbf{0}) \neq \mathbf{0}$).

**Intuición frente a demostración**: la animación del paralelogramo sugiere la propiedad; la cuenta con sumatorios la demuestra.

---

## Guion de narración

### Video 1 — `LaRejillaSeDeforma`

| En pantalla | Narración |
|---|---|
| La rejilla se cizalla | "Una matriz mueve cada punto x al punto A x. Con esta matriz, cada punto se desplaza en horizontal tanto como vale su altura: la rejilla se inclina." |
| Otra matriz; tres propiedades | "Con otra matriz la rejilla gira y se estira, pero las rectas siguen rectas, las paralelas siguen paralelas e igual de separadas, y el origen no se mueve." |

### Video 2 — `ColumnasSonImagenesDeLaBase`

| En pantalla | Narración |
|---|---|
| $\mathbf{x} = 1\mathbf{e}_1 + 2\mathbf{e}_2$ | "Todo vector se escribe con e uno y e dos: uno, dos es un paso por e uno y dos por e dos." |
| Tras transformar: $A\mathbf{e}_1$, $A\mathbf{e}_2$ | "Después de transformar, e uno ha ido a dos, uno, la primera columna de A, y e dos a menos uno, uno, la segunda. Las columnas son las imágenes de la base." |
| $A\mathbf{x} = 1(2, 1) + 2(-1, 1)$ | "Y el camino se transforma igual: un paso por A e uno y dos por A e dos. Es A x como combinación de columnas." |

### Video 3 — `QueSignificaLineal`

| En pantalla | Narración |
|---|---|
| Paralelogramo transformado | "Lineal significa dos cosas: la imagen de una suma es la suma de las imágenes, y la imagen del doble es el doble de la imagen. El paralelogramo sigue siendo paralelogramo." |
| Rejilla curvada y traslación | "Esto no es lineal: las rectas se curvan. Y trasladar tampoco: el origen se mueve." |
| Demostración con sumatorios | "Que multiplicar por una matriz es lineal se demuestra con una línea: la propiedad distributiva de los números." |

---

## Errores frecuentes

- Poner las imágenes de $\mathbf{e}_1$, $\mathbf{e}_2$ como filas.
- Creer que una traslación es lineal.
- Tomar la animación como demostración.

## Resumen y conexión

Una matriz es una transformación lineal; sus columnas dicen adónde van los vectores de la base. En la Lección 22 volvemos a los sistemas: todo sistema se escribe $A\mathbf{x} = \mathbf{b}$.
