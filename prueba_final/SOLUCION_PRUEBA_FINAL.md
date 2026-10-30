# Prueba final integradora: soluciones y baremo

Todos los resultados se calcularon con aritmética exacta (`prueba_final/generar_prueba.py`). Si falta una comprobación en tu respuesta, resta la quinta parte de los puntos del apartado.

## Problema 1 — Eliminación gaussiana (10 puntos)

**Enunciado.** Resuelve por eliminación gaussiana $\begin{cases} x - 2z = 1 \\ 2x - y = 6 \\ -x - 2y + 2z = -1 \end{cases}$ y comprueba el resultado.

**Solución.** $$ \left[\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\ 2 & -1 & 0 & 6 \\ -1 & -2 & 2 & -1 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\ 0 & -1 & 4 & 4 \\ -1 & -2 & 2 & -1 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + R_1} \left[\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\ 0 & -1 & 4 & 4 \\ 0 & -2 & 0 & 0 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - 2R_2} \left[\begin{array}{ccc|c} 1 & 0 & -2 & 1 \\ 0 & -1 & 4 & 4 \\ 0 & 0 & -8 & -8 \end{array}\right]$$

Sustitución hacia atrás: $(3, 0, 1)$. Comprobación en la primera ecuación: $1\cdot 3 + 0\cdot 0 + (-2)\cdot 1 = 1$.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 2 — Gauss-Jordan y solución general (10 puntos)

**Enunciado.** Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} -1 & -2 & -2 & 5 & 5 \\ 1 & 2 & 6 & -9 & -5 \\ 1 & 2 & 4 & -7 & -5 \end{array}\right]$ y escribe la solución general.

**Solución.** Operaciones: $R_1 \leftarrow (-1)R_1,\ R_2 \leftarrow R_2 - R_1,\ R_3 \leftarrow R_3 - R_1,\ R_2 \leftarrow (\frac{1}{4})R_2,\ R_1 \leftarrow R_1 - 2R_2,\ R_3 \leftarrow R_3 - 2R_2$.

Resultado: $$\left[\begin{array}{cccc|c} 1 & 2 & 0 & -3 & -5 \\ 0 & 0 & 1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right]$$
Variables libres: $x_2$, $x_4$. Solución general: $(-5, 0, 0, 0) + s\,(-2, 1, 0, 0) + t\,(3, 0, 1, 1)$ (parámetros reales).

Comprobación con los parámetros en cero: $A\mathbf{x}_p = (5, -5, -5) = (5, -5, -5)$.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 3 — Factorización LU (10 puntos)

**Enunciado.** Factoriza $A = \begin{bmatrix} -2 & -3 & 3 \\ 4 & 7 & -8 \\ 4 & 7 & -5 \end{bmatrix}$ como $A = LU$ y resuelve $A\mathbf{x} = \mathbf{b}_k$ para $\mathbf{b}_1 = (-3, -1, 3)$ y $\mathbf{b}_2 = (0, 2, -2)$ usando la factorización.

**Solución.** $L = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ -2 & 1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} -2 & -3 & 3 \\ 0 & 1 & -2 \\ 0 & 0 & 3 \end{bmatrix}$ (multiplicadores: $\ell_{21} = -2$, $\ell_{31} = -2$, $\ell_{32} = 1$).

Para $\mathbf{b}_1$: $L\mathbf{y} = \mathbf{b}_1$ da $\mathbf{y} = (-3, -7, 4)$; $U\mathbf{x} = \mathbf{y}$ da $\mathbf{x} = (10, -\frac{13}{3}, \frac{4}{3})$.

Para $\mathbf{b}_2$: $L\mathbf{y} = \mathbf{b}_2$ da $\mathbf{y} = (0, 2, -4)$; $U\mathbf{x} = \mathbf{y}$ da $\mathbf{x} = (-1, -\frac{2}{3}, -\frac{4}{3})$.

Coste: factorizar una vez; cada lado derecho, dos sustituciones.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 4 — Sistema con un parámetro (12 puntos)

**Enunciado.** Discute y resuelve según $a$: $\begin{cases} x + y + z = 1 \\ x + ay + z = 1 \\ x + y + az = 1 \end{cases}$. Para los valores en que haya infinitas soluciones, escribe la solución general con una base del núcleo.

**Solución.** $\det A = \left(a - 1\right)^{2}$, que se anula en $a \in \{1\}$. Si $a$ es otro valor, $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 3$: solución única.

$a = 1$: $\operatorname{rg}(A) = 1$, $\operatorname{rg}[A \mid \mathbf{b}] = 1$, compatible indeterminado (infinitas soluciones). Solución general: $(1, 0, 0) + s\,(-1, 1, 0) + t\,(-1, 0, 1)$; núcleo de dimensión 2.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 5 — Rango, núcleo y espacio columna (12 puntos)

**Enunciado.** Sea $A = \begin{bmatrix} -1 & -1 & 4 & 0 & 1 \\ 2 & -2 & 4 & 6 & -2 \\ -2 & 2 & -4 & -6 & 2 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} 0 \\ 24 \\ -24 \end{bmatrix}$. a) Calcula la forma reducida y el rango de $A$. b) Clasifica $A\mathbf{x} = \mathbf{b}$ y, si es compatible, da la solución general. c) Halla una base de $\ker A$. d) Halla una base de $\operatorname{Col}(A)$ y decide si $\mathbf{b} \in \operatorname{Col}(A)$. e) Comprueba el teorema del rango y la nulidad.

**Solución.** **a)** Reduciendo, $\begin{bmatrix} -1 & -1 & 4 & 0 & 1 \\ 2 & -2 & 4 & 6 & -2 \\ -2 & 2 & -4 & -6 & 2 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & -1 & \frac{3}{2} & -1 \\ 0 & 1 & -3 & -\frac{3}{2} & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$: pivotes en las columnas 1, 2, luego $\operatorname{rg}(A) = 2$.

**b)** $\operatorname{rg}[A \mid \mathbf{b}] = 2$. Los rangos coinciden: compatible indeterminado (infinitas soluciones).

Solución general: $(6, -6, 0, 0, 0) + s\,(1, 3, 1, 0, 0) + t\,(-\frac{3}{2}, \frac{3}{2}, 0, 1, 0) + u\,(1, 0, 0, 0, 1)$.

**c)** Base de $\ker A$: $(1, 3, 1, 0, 0)$, $(-\frac{3}{2}, \frac{3}{2}, 0, 1, 0)$, $(1, 0, 0, 0, 1)$ (dimensión 3).

**d)** Base de $\operatorname{Col}(A)$ (columnas pivote de $A$): $(-1, 2, -2)$, $(-1, -2, 2)$ (dimensión 2). Además $\mathbf{b} \in \operatorname{Col}(A)$.

**e)** $\operatorname{rg} + \operatorname{nul} = 2 + 3 = 5 = n$ ✓.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 6 — Modelado (8 puntos)

**Enunciado.** Se mezclan tres productos. Por kilogramo:

- 1 kg de pienso A aporta 3 g de nitrógeno, 1 g de fósforo, 4 g de potasio.
- 1 kg de pienso B aporta 3 g de nitrógeno, 5 g de fósforo, 1 g de potasio.
- 1 kg de pienso C aporta 2 g de nitrógeno, 3 g de fósforo, 2 g de potasio.

Se quiere una mezcla con 26 g de nitrógeno, 38 g de fósforo y 17 g de potasio. ¿Cuántos kg de cada producto hay que mezclar?

**Solución.** Con $x, y, z$ los kg de pienso A, pienso B y pienso C: $\begin{cases} 3x + 3y + 2z = 26 \\ x + 5y + 3z = 38 \\ 4x + y + 2z = 17 \end{cases}$.

$$ \left[\begin{array}{ccc|c} 3 & 3 & 2 & 26 \\ 1 & 5 & 3 & 38 \\ 4 & 1 & 2 & 17 \end{array}\right] $$
$$\xrightarrow{R_2 \leftarrow R_2 - \frac{1}{3}R_1} \left[\begin{array}{ccc|c} 3 & 3 & 2 & 26 \\ 0 & 4 & \frac{7}{3} & \frac{88}{3} \\ 4 & 1 & 2 & 17 \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 - \frac{4}{3}R_1} \left[\begin{array}{ccc|c} 3 & 3 & 2 & 26 \\ 0 & 4 & \frac{7}{3} & \frac{88}{3} \\ 0 & -3 & -\frac{2}{3} & -\frac{53}{3} \end{array}\right]$$
$$\xrightarrow{R_3 \leftarrow R_3 + \frac{3}{4}R_2} \left[\begin{array}{ccc|c} 3 & 3 & 2 & 26 \\ 0 & 4 & \frac{7}{3} & \frac{88}{3} \\ 0 & 0 & \frac{13}{12} & \frac{13}{3} \end{array}\right]$$

Solución: $(1, 5, 4)$ kg. Todas las cantidades son positivas, así que es una mezcla posible.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 7 — Verdadero o falso (8 puntos)

**Enunciado.** Di si cada afirmación es verdadera o falsa y justifícalo (con una demostración corta o un contraejemplo):

a) El conjunto solución de $A\mathbf{x} = \mathbf{b}$ con $\mathbf{b} \ne \mathbf{0}$ es un subespacio.
b) Si $AB = 0$, entonces $A = 0$ o $B = 0$.
c) Tres vectores de $\mathbb{R}^2$ son siempre linealmente dependientes.
d) Si $\operatorname{rg}(A) = m$ (filas), $A\mathbf{x} = \mathbf{b}$ tiene solución para todo $\mathbf{b}$.

**Solución.** a) Falso: no contiene a $\mathbf{0}$ (es un núcleo trasladado).

b) Falso: $\begin{bmatrix} 1&0\\0&0 \end{bmatrix}\begin{bmatrix} 0&0\\0&1 \end{bmatrix} = 0$.

c) Verdadero: la matriz $2 \times 3$ tiene rango $\le 2 < 3$.

d) Verdadero: entonces $\operatorname{Col}(A) = \mathbb{R}^m$.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 8 — Clasificar sin resolver (10 puntos)

**Enunciado.** Sin resolverlos, clasifica cada sistema (y di cuántos parámetros libres tiene si es indeterminado):

a) $\begin{cases} -2x + 3y + z = 1 \\ 5x - 5y - z = -3 \\ -6x + 6y + 4z = -2 \end{cases}$

b) $\begin{cases} -x - y + z + 2w = -5 \\ 2x + 2y - 2z - 4w = 10 \\ -3x - 3y + 3z + 6w = -15 \end{cases}$

c) $\begin{cases} -3x + 6z = 13 \\ -x + y + 3z = 9 \\ 2x + 2y - 2z = 2 \end{cases}$

**Solución.** a) $\operatorname{rg}(A) = 3$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, $n = 3$: compatible determinado (solución única).

b) $\operatorname{rg}(A) = 1$, $\operatorname{rg}[A \mid \mathbf{b}] = 1$, $n = 4$: compatible indeterminado (infinitas soluciones). Parámetros libres: $n - \operatorname{rg}(A) = 4 - 1 = 3$.

c) $\operatorname{rg}(A) = 2$, $\operatorname{rg}[A \mid \mathbf{b}] = 3$, $n = 3$: incompatible (sin solución).

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 9 — Demostración (10 puntos)

**Enunciado.** Prueba que si $\mathbf{x}_1, \mathbf{x}_2$ son soluciones de $A\mathbf{x} = \mathbf{b}$, entonces $\mathbf{x}_1 - \mathbf{x}_2 \in \ker A$; y que la solución es única si y solo si $\ker A = \{\mathbf{0}\}$ (cuando hay alguna).

**Solución.** $A(\mathbf{x}_1 - \mathbf{x}_2) = \mathbf{b} - \mathbf{b} = \mathbf{0}$. Si $\ker A = \{\mathbf{0}\}$, la diferencia es $\mathbf{0}$ y hay una sola solución. Si hay $\mathbf{n} \ne \mathbf{0}$ en $\ker A$ y $\mathbf{x}_p$ es solución, $\mathbf{x}_p + \mathbf{n}$ es otra solución distinta. $\blacksquare$

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.

## Problema 10 — Problema integrador (10 puntos)

**Enunciado.** Sea $A = \begin{bmatrix} 7 & 5 & -4 & 4 \\ 0 & 6 & 4 & -1 \\ -3 & 3 & 5 & -2 \\ 5 & -7 & -9 & 1 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} -17 \\ -1 \\ 7 \\ -12 \end{bmatrix}$. a) Calcula la forma reducida y el rango de $A$. b) Clasifica $A\mathbf{x} = \mathbf{b}$ y, si es compatible, da la solución general. c) Halla una base de $\ker A$. d) Halla una base de $\operatorname{Col}(A)$ y decide si $\mathbf{b} \in \operatorname{Col}(A)$. e) Comprueba el teorema del rango y la nulidad.

**Solución.** **a)** Reduciendo, $\begin{bmatrix} 7 & 5 & -4 & 4 \\ 0 & 6 & 4 & -1 \\ -3 & 3 & 5 & -2 \\ 5 & -7 & -9 & 1 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & 0 & -\frac{7}{2} \\ 0 & 1 & 0 & \frac{5}{2} \\ 0 & 0 & 1 & -4 \\ 0 & 0 & 0 & 0 \end{bmatrix}$: pivotes en las columnas 1, 2, 3, luego $\operatorname{rg}(A) = 3$.

**b)** $\operatorname{rg}[A \mid \mathbf{b}] = 4$. Los rangos son distintos: incompatible (sin solución).

**c)** Base de $\ker A$: $(\frac{7}{2}, -\frac{5}{2}, 4, 1)$ (dimensión 1).

**d)** Base de $\operatorname{Col}(A)$ (columnas pivote de $A$): $(7, 0, -3, 5)$, $(5, 6, 3, -7)$, $(-4, 4, 5, -9)$ (dimensión 3). Además $\mathbf{b} \notin \operatorname{Col}(A)$.

**e)** $\operatorname{rg} + \operatorname{nul} = 3 + 1 = 4 = n$ ✓.

**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.
