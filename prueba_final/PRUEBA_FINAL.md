# Prueba final integradora

**Duración**: 2 horas · **Puntos**: 100 · **Material**: sin apuntes ni calculadora (todas las cuentas son con fracciones sencillas).

Justifica cada respuesta. Verifica en el sistema original siempre que sea posible. Las soluciones y el baremo están en `SOLUCION_PRUEBA_FINAL.md`: corrígete **después** de entregar.

| Problema | Tema | Puntos |
|---|---|---|
| 1 | Eliminación gaussiana | 10 |
| 2 | Gauss-Jordan y solución general | 10 |
| 3 | Factorización LU | 10 |
| 4 | Sistema con un parámetro | 12 |
| 5 | Rango, núcleo y espacio columna | 12 |
| 6 | Modelado | 8 |
| 7 | Verdadero o falso | 8 |
| 8 | Clasificar sin resolver | 10 |
| 9 | Demostración | 10 |
| 10 | Problema integrador | 10 |

## Problema 1 — Eliminación gaussiana (10 puntos)

Resuelve por eliminación gaussiana $\begin{cases} x - 2z = 1 \\ 2x - y = 6 \\ -x - 2y + 2z = -1 \end{cases}$ y comprueba el resultado.

## Problema 2 — Gauss-Jordan y solución general (10 puntos)

Halla, por Gauss-Jordan, la reducida de $\left[\begin{array}{cccc|c} -1 & -2 & -2 & 5 & 5 \\ 1 & 2 & 6 & -9 & -5 \\ 1 & 2 & 4 & -7 & -5 \end{array}\right]$ y escribe la solución general.

## Problema 3 — Factorización LU (10 puntos)

Factoriza $A = \begin{bmatrix} -2 & -3 & 3 \\ 4 & 7 & -8 \\ 4 & 7 & -5 \end{bmatrix}$ como $A = LU$ y resuelve $A\mathbf{x} = \mathbf{b}_k$ para $\mathbf{b}_1 = (-3, -1, 3)$ y $\mathbf{b}_2 = (0, 2, -2)$ usando la factorización.

## Problema 4 — Sistema con un parámetro (12 puntos)

Discute y resuelve según $a$: $\begin{cases} x + y + z = 1 \\ x + ay + z = 1 \\ x + y + az = 1 \end{cases}$. Para los valores en que haya infinitas soluciones, escribe la solución general con una base del núcleo.

## Problema 5 — Rango, núcleo y espacio columna (12 puntos)

Sea $A = \begin{bmatrix} -1 & -1 & 4 & 0 & 1 \\ 2 & -2 & 4 & 6 & -2 \\ -2 & 2 & -4 & -6 & 2 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} 0 \\ 24 \\ -24 \end{bmatrix}$. a) Calcula la forma reducida y el rango de $A$. b) Clasifica $A\mathbf{x} = \mathbf{b}$ y, si es compatible, da la solución general. c) Halla una base de $\ker A$. d) Halla una base de $\operatorname{Col}(A)$ y decide si $\mathbf{b} \in \operatorname{Col}(A)$. e) Comprueba el teorema del rango y la nulidad.

## Problema 6 — Modelado (8 puntos)

Se mezclan tres productos. Por kilogramo:

- 1 kg de pienso A aporta 3 g de nitrógeno, 1 g de fósforo, 4 g de potasio.
- 1 kg de pienso B aporta 3 g de nitrógeno, 5 g de fósforo, 1 g de potasio.
- 1 kg de pienso C aporta 2 g de nitrógeno, 3 g de fósforo, 2 g de potasio.

Se quiere una mezcla con 26 g de nitrógeno, 38 g de fósforo y 17 g de potasio. ¿Cuántos kg de cada producto hay que mezclar?

## Problema 7 — Verdadero o falso (8 puntos)

Di si cada afirmación es verdadera o falsa y justifícalo (con una demostración corta o un contraejemplo):

a) El conjunto solución de $A\mathbf{x} = \mathbf{b}$ con $\mathbf{b} \ne \mathbf{0}$ es un subespacio.
b) Si $AB = 0$, entonces $A = 0$ o $B = 0$.
c) Tres vectores de $\mathbb{R}^2$ son siempre linealmente dependientes.
d) Si $\operatorname{rg}(A) = m$ (filas), $A\mathbf{x} = \mathbf{b}$ tiene solución para todo $\mathbf{b}$.

## Problema 8 — Clasificar sin resolver (10 puntos)

Sin resolverlos, clasifica cada sistema (y di cuántos parámetros libres tiene si es indeterminado):

a) $\begin{cases} -2x + 3y + z = 1 \\ 5x - 5y - z = -3 \\ -6x + 6y + 4z = -2 \end{cases}$

b) $\begin{cases} -x - y + z + 2w = -5 \\ 2x + 2y - 2z - 4w = 10 \\ -3x - 3y + 3z + 6w = -15 \end{cases}$

c) $\begin{cases} -3x + 6z = 13 \\ -x + y + 3z = 9 \\ 2x + 2y - 2z = 2 \end{cases}$

## Problema 9 — Demostración (10 puntos)

Prueba que si $\mathbf{x}_1, \mathbf{x}_2$ son soluciones de $A\mathbf{x} = \mathbf{b}$, entonces $\mathbf{x}_1 - \mathbf{x}_2 \in \ker A$; y que la solución es única si y solo si $\ker A = \{\mathbf{0}\}$ (cuando hay alguna).

## Problema 10 — Problema integrador (10 puntos)

Sea $A = \begin{bmatrix} 7 & 5 & -4 & 4 \\ 0 & 6 & 4 & -1 \\ -3 & 3 & 5 & -2 \\ 5 & -7 & -9 & 1 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} -17 \\ -1 \\ 7 \\ -12 \end{bmatrix}$. a) Calcula la forma reducida y el rango de $A$. b) Clasifica $A\mathbf{x} = \mathbf{b}$ y, si es compatible, da la solución general. c) Halla una base de $\ker A$. d) Halla una base de $\operatorname{Col}(A)$ y decide si $\mathbf{b} \in \operatorname{Col}(A)$. e) Comprueba el teorema del rango y la nulidad.
