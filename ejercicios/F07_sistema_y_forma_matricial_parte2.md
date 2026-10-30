# F07 — Sistema y forma matricial (parte 2)

Segunda parte del banco de las lecciones L22–L23: **23 ejercicios** de práctica que completan la parte 1 (`F07_sistema_y_forma_matricial.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N1: 16, N2: 7 · [C] 19, [K] 4.

---

### F07-N1-11 · [C] Del sistema a $A\mathbf{x} = \mathbf{b}$

**Objetivo**: escribir un sistema en forma matricial.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $A\mathbf{x} = \mathbf{b}$ el sistema $\begin{cases} -2x - 3y = 3 \\ x + y + 2z = 8 \\ -2x + 2z = 2 \end{cases}$.

<details><summary>Pista 1</summary>Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} -2 & -3 & 0 \\ 1 & 1 & 2 \\ -2 & 0 & 2 \end{bmatrix}\begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} 3 \\ 8 \\ 2 \end{bmatrix}$, con $A = \begin{bmatrix} -2 & -3 & 0 \\ 1 & 1 & 2 \\ -2 & 0 & 2 \end{bmatrix}$ (coeficientes) y $\mathbf{b} = \begin{bmatrix} 3 \\ 8 \\ 2 \end{bmatrix}$ (términos independientes).

</details>
<details><summary>Errores frecuentes</summary>Meter el término independiente dentro de $A$.</details>

### F07-N1-12 · [C] Del sistema a $A\mathbf{x} = \mathbf{b}$

**Objetivo**: escribir un sistema en forma matricial.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $A\mathbf{x} = \mathbf{b}$ el sistema $\begin{cases} -y = -4 \\ 3x - 3y = -24 \end{cases}$.

<details><summary>Pista 1</summary>Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} 0 & -1 \\ 3 & -3 \end{bmatrix}\begin{bmatrix} x\\ y \end{bmatrix} = \begin{bmatrix} -4 \\ -24 \end{bmatrix}$, con $A = \begin{bmatrix} 0 & -1 \\ 3 & -3 \end{bmatrix}$ (coeficientes) y $\mathbf{b} = \begin{bmatrix} -4 \\ -24 \end{bmatrix}$ (términos independientes).

</details>
<details><summary>Errores frecuentes</summary>Meter el término independiente dentro de $A$.</details>

### F07-N1-13 · [C] Del sistema a $A\mathbf{x} = \mathbf{b}$

**Objetivo**: escribir un sistema en forma matricial.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $A\mathbf{x} = \mathbf{b}$ el sistema $\begin{cases} -y - 3z = -1 \\ -2x - 3y - z = 5 \\ -3x + 3y - 3z = 15 \end{cases}$.

<details><summary>Pista 1</summary>Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} 0 & -1 & -3 \\ -2 & -3 & -1 \\ -3 & 3 & -3 \end{bmatrix}\begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} -1 \\ 5 \\ 15 \end{bmatrix}$, con $A = \begin{bmatrix} 0 & -1 & -3 \\ -2 & -3 & -1 \\ -3 & 3 & -3 \end{bmatrix}$ (coeficientes) y $\mathbf{b} = \begin{bmatrix} -1 \\ 5 \\ 15 \end{bmatrix}$ (términos independientes).

</details>
<details><summary>Errores frecuentes</summary>Meter el término independiente dentro de $A$.</details>

### F07-N1-14 · [C] Del sistema a $A\mathbf{x} = \mathbf{b}$

**Objetivo**: escribir un sistema en forma matricial.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $A\mathbf{x} = \mathbf{b}$ el sistema $\begin{cases} 3x + 3y - 2z = 1 \\ 3y - z = 11 \\ x + 2y + 2z = 7 \end{cases}$.

<details><summary>Pista 1</summary>Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} 3 & 3 & -2 \\ 0 & 3 & -1 \\ 1 & 2 & 2 \end{bmatrix}\begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 11 \\ 7 \end{bmatrix}$, con $A = \begin{bmatrix} 3 & 3 & -2 \\ 0 & 3 & -1 \\ 1 & 2 & 2 \end{bmatrix}$ (coeficientes) y $\mathbf{b} = \begin{bmatrix} 1 \\ 11 \\ 7 \end{bmatrix}$ (términos independientes).

</details>
<details><summary>Errores frecuentes</summary>Meter el término independiente dentro de $A$.</details>

### F07-N1-15 · [C] Del sistema a $A\mathbf{x} = \mathbf{b}$

**Objetivo**: escribir un sistema en forma matricial.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $A\mathbf{x} = \mathbf{b}$ el sistema $\begin{cases} -x - 2z = 12 \\ x - 2y + 2z = -4 \\ -x - y - 3z = 20 \end{cases}$.

<details><summary>Pista 1</summary>Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} -1 & 0 & -2 \\ 1 & -2 & 2 \\ -1 & -1 & -3 \end{bmatrix}\begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} 12 \\ -4 \\ 20 \end{bmatrix}$, con $A = \begin{bmatrix} -1 & 0 & -2 \\ 1 & -2 & 2 \\ -1 & -1 & -3 \end{bmatrix}$ (coeficientes) y $\mathbf{b} = \begin{bmatrix} 12 \\ -4 \\ 20 \end{bmatrix}$ (términos independientes).

</details>
<details><summary>Errores frecuentes</summary>Meter el término independiente dentro de $A$.</details>

### F07-N1-16 · [C] Del sistema a $A\mathbf{x} = \mathbf{b}$

**Objetivo**: escribir un sistema en forma matricial.
**Dificultad**: N1

**Enunciado.** Escribe en la forma $A\mathbf{x} = \mathbf{b}$ el sistema $\begin{cases} 3x + 2y + 2z = 4 \\ -3x - 3y - 2z = -6 \\ x + 2y - z = 4 \end{cases}$.

<details><summary>Pista 1</summary>Cada fila de $A$ contiene los coeficientes de una ecuación, en el orden de las incógnitas.</details>
<details><summary>Solución</summary>

$\begin{bmatrix} 3 & 2 & 2 \\ -3 & -3 & -2 \\ 1 & 2 & -1 \end{bmatrix}\begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} 4 \\ -6 \\ 4 \end{bmatrix}$, con $A = \begin{bmatrix} 3 & 2 & 2 \\ -3 & -3 & -2 \\ 1 & 2 & -1 \end{bmatrix}$ (coeficientes) y $\mathbf{b} = \begin{bmatrix} 4 \\ -6 \\ 4 \end{bmatrix}$ (términos independientes).

</details>
<details><summary>Errores frecuentes</summary>Meter el término independiente dentro de $A$.</details>

### F07-N1-17 · [C] Matriz aumentada

**Objetivo**: escribir $[A \mid \mathbf{b}]$ a partir del sistema.
**Dificultad**: N1

**Enunciado.** Escribe la matriz aumentada de $\begin{cases} -x - 2z = 1 \\ 3z = 0 \\ -2x - y - z = 5 \end{cases}$.

<details><summary>Pista 1</summary>Una fila por ecuación, una columna por incógnita y una última columna para los números.</details>
<details><summary>Solución</summary>

Se pegan los coeficientes y, tras una barra, los términos independientes: $\left[\begin{array}{ccc|c} -1 & 0 & -2 & 1 \\ 0 & 0 & 3 & 0 \\ -2 & -1 & -1 & 5 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar la última columna o ponerla con el signo cambiado.</details>

### F07-N1-18 · [C] Matriz aumentada

**Objetivo**: escribir $[A \mid \mathbf{b}]$ a partir del sistema.
**Dificultad**: N1

**Enunciado.** Escribe la matriz aumentada de $\begin{cases} x + 2y = -8 \\ -2x - 3y = 12 \end{cases}$.

<details><summary>Pista 1</summary>Una fila por ecuación, una columna por incógnita y una última columna para los números.</details>
<details><summary>Solución</summary>

Se pegan los coeficientes y, tras una barra, los términos independientes: $\left[\begin{array}{cc|c} 1 & 2 & -8 \\ -2 & -3 & 12 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar la última columna o ponerla con el signo cambiado.</details>

### F07-N1-19 · [C] Matriz aumentada

**Objetivo**: escribir $[A \mid \mathbf{b}]$ a partir del sistema.
**Dificultad**: N1

**Enunciado.** Escribe la matriz aumentada de $\begin{cases} x + y = 2 \\ x + 3y = 8 \end{cases}$.

<details><summary>Pista 1</summary>Una fila por ecuación, una columna por incógnita y una última columna para los números.</details>
<details><summary>Solución</summary>

Se pegan los coeficientes y, tras una barra, los términos independientes: $\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 1 & 3 & 8 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar la última columna o ponerla con el signo cambiado.</details>

### F07-N1-20 · [C] Matriz aumentada

**Objetivo**: escribir $[A \mid \mathbf{b}]$ a partir del sistema.
**Dificultad**: N1

**Enunciado.** Escribe la matriz aumentada de $\begin{cases} x + 3y - 2z = 11 \\ x + 2y + 3z = 2 \\ 3x + y + z = -6 \end{cases}$.

<details><summary>Pista 1</summary>Una fila por ecuación, una columna por incógnita y una última columna para los números.</details>
<details><summary>Solución</summary>

Se pegan los coeficientes y, tras una barra, los términos independientes: $\left[\begin{array}{ccc|c} 1 & 3 & -2 & 11 \\ 1 & 2 & 3 & 2 \\ 3 & 1 & 1 & -6 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar la última columna o ponerla con el signo cambiado.</details>

### F07-N1-21 · [C] Matriz aumentada

**Objetivo**: escribir $[A \mid \mathbf{b}]$ a partir del sistema.
**Dificultad**: N1

**Enunciado.** Escribe la matriz aumentada de $\begin{cases} -x - 2y + 2z = 0 \\ -3x - y - 2z = 14 \\ -2x + y - z = 5 \end{cases}$.

<details><summary>Pista 1</summary>Una fila por ecuación, una columna por incógnita y una última columna para los números.</details>
<details><summary>Solución</summary>

Se pegan los coeficientes y, tras una barra, los términos independientes: $\left[\begin{array}{ccc|c} -1 & -2 & 2 & 0 \\ -3 & -1 & -2 & 14 \\ -2 & 1 & -1 & 5 \end{array}\right]$.

</details>
<details><summary>Errores frecuentes</summary>Olvidar la última columna o ponerla con el signo cambiado.</details>

### F07-N1-22 · [C] De la matriz aumentada al sistema

**Objetivo**: leer un sistema a partir de $[A \mid \mathbf{b}]$.
**Dificultad**: N1

**Enunciado.** Escribe el sistema que representa $\left[\begin{array}{ccc|c} 0 & 0 & -1 & -3 \\ -3 & 0 & -2 & -3 \\ -1 & -3 & 2 & 7 \end{array}\right]$ (incógnitas x, y, z) y comprueba que $(-1, 0, 3)$ es solución.

<details><summary>Pista 1</summary>La fila $[a\ b\ c \mid d]$ es la ecuación $ax + by + cz = d$.</details>
<details><summary>Solución</summary>

El sistema es $\begin{cases} -z = -3 \\ -3x - 2z = -3 \\ -x - 3y + 2z = 7 \end{cases}$. Comprobación: $0\cdot (-1) + 0\cdot 0 + (-1)\cdot 3 = -3$, $(-3)\cdot (-1) + 0\cdot 0 + (-2)\cdot 3 = -3$, $(-1)\cdot (-1) + (-3)\cdot 0 + 2\cdot 3 = 7$.

</details>
<details><summary>Errores frecuentes</summary>Leer las columnas como si fueran filas.</details>

### F07-N1-23 · [C] De la matriz aumentada al sistema

**Objetivo**: leer un sistema a partir de $[A \mid \mathbf{b}]$.
**Dificultad**: N1

**Enunciado.** Escribe el sistema que representa $\left[\begin{array}{ccc|c} -2 & 0 & -2 & 2 \\ 3 & 1 & 3 & -3 \\ 3 & 2 & -2 & -18 \end{array}\right]$ (incógnitas x, y, z) y comprueba que $(-4, 0, 3)$ es solución.

<details><summary>Pista 1</summary>La fila $[a\ b\ c \mid d]$ es la ecuación $ax + by + cz = d$.</details>
<details><summary>Solución</summary>

El sistema es $\begin{cases} -2x - 2z = 2 \\ 3x + y + 3z = -3 \\ 3x + 2y - 2z = -18 \end{cases}$. Comprobación: $(-2)\cdot (-4) + 0\cdot 0 + (-2)\cdot 3 = 2$, $3\cdot (-4) + 1\cdot 0 + 3\cdot 3 = -3$, $3\cdot (-4) + 2\cdot 0 + (-2)\cdot 3 = -18$.

</details>
<details><summary>Errores frecuentes</summary>Leer las columnas como si fueran filas.</details>

### F07-N1-24 · [C] De la matriz aumentada al sistema

**Objetivo**: leer un sistema a partir de $[A \mid \mathbf{b}]$.
**Dificultad**: N1

**Enunciado.** Escribe el sistema que representa $\left[\begin{array}{ccc|c} -3 & 2 & -1 & -11 \\ 3 & -1 & 0 & 12 \\ 2 & 2 & -2 & 10 \end{array}\right]$ (incógnitas x, y, z) y comprueba que $(4, 0, -1)$ es solución.

<details><summary>Pista 1</summary>La fila $[a\ b\ c \mid d]$ es la ecuación $ax + by + cz = d$.</details>
<details><summary>Solución</summary>

El sistema es $\begin{cases} -3x + 2y - z = -11 \\ 3x - y = 12 \\ 2x + 2y - 2z = 10 \end{cases}$. Comprobación: $(-3)\cdot 4 + 2\cdot 0 + (-1)\cdot (-1) = -11$, $3\cdot 4 + (-1)\cdot 0 + 0\cdot (-1) = 12$, $2\cdot 4 + 2\cdot 0 + (-2)\cdot (-1) = 10$.

</details>
<details><summary>Errores frecuentes</summary>Leer las columnas como si fueran filas.</details>

### F07-N1-25 · [C] De la matriz aumentada al sistema

**Objetivo**: leer un sistema a partir de $[A \mid \mathbf{b}]$.
**Dificultad**: N1

**Enunciado.** Escribe el sistema que representa $\left[\begin{array}{ccc|c} 3 & 2 & 1 & -6 \\ -3 & 2 & 2 & -8 \\ -1 & -1 & -2 & 6 \end{array}\right]$ (incógnitas x, y, z) y comprueba que $(0, -2, -2)$ es solución.

<details><summary>Pista 1</summary>La fila $[a\ b\ c \mid d]$ es la ecuación $ax + by + cz = d$.</details>
<details><summary>Solución</summary>

El sistema es $\begin{cases} 3x + 2y + z = -6 \\ -3x + 2y + 2z = -8 \\ -x - y - 2z = 6 \end{cases}$. Comprobación: $3\cdot 0 + 2\cdot (-2) + 1\cdot (-2) = -6$, $(-3)\cdot 0 + 2\cdot (-2) + 2\cdot (-2) = -8$, $(-1)\cdot 0 + (-1)\cdot (-2) + (-2)\cdot (-2) = 6$.

</details>
<details><summary>Errores frecuentes</summary>Leer las columnas como si fueran filas.</details>

### F07-N1-26 · [C] De la matriz aumentada al sistema

**Objetivo**: leer un sistema a partir de $[A \mid \mathbf{b}]$.
**Dificultad**: N1

**Enunciado.** Escribe el sistema que representa $\left[\begin{array}{ccc|c} -1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 4 \\ -3 & -2 & -3 & -8 \end{array}\right]$ (incógnitas x, y, z) y comprueba que $(0, 4, 0)$ es solución.

<details><summary>Pista 1</summary>La fila $[a\ b\ c \mid d]$ es la ecuación $ax + by + cz = d$.</details>
<details><summary>Solución</summary>

El sistema es $\begin{cases} -x = 0 \\ x + y = 4 \\ -3x - 2y - 3z = -8 \end{cases}$. Comprobación: $(-1)\cdot 0 + 0\cdot 4 + 0\cdot 0 = 0$, $1\cdot 0 + 1\cdot 4 + 0\cdot 0 = 4$, $(-3)\cdot 0 + (-2)\cdot 4 + (-3)\cdot 0 = -8$.

</details>
<details><summary>Errores frecuentes</summary>Leer las columnas como si fueran filas.</details>

### F07-N2-11 · [K] Tamaños en $A\mathbf{x} = \mathbf{b}$

**Objetivo**: relacionar ecuaciones e incógnitas con los tamaños de $A$, $\mathbf{x}$ y $\mathbf{b}$.
**Dificultad**: N2

**Enunciado.** Un sistema tiene 3 ecuaciones y 3 incógnitas. ¿Qué tamaño tienen $A$, $\mathbf{x}$, $\mathbf{b}$ y $[A \mid \mathbf{b}]$?

<details><summary>Pista 1</summary>Filas de $A$ = ecuaciones; columnas de $A$ = incógnitas.</details>
<details><summary>Solución</summary>

$A$ es $3\times 3$; $\mathbf{x}$ es $3\times 1$; $\mathbf{b}$ es $3\times 1$; $[A \mid \mathbf{b}]$ es $3\times 4$. El producto $A\mathbf{x}$ está definido: $(3\times 3)(3\times 1)$ da $3\times 1$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar ecuaciones e incógnitas.</details>

### F07-N2-12 · [K] Tamaños en $A\mathbf{x} = \mathbf{b}$

**Objetivo**: relacionar ecuaciones e incógnitas con los tamaños de $A$, $\mathbf{x}$ y $\mathbf{b}$.
**Dificultad**: N2

**Enunciado.** Un sistema tiene 3 ecuaciones y 4 incógnitas. ¿Qué tamaño tienen $A$, $\mathbf{x}$, $\mathbf{b}$ y $[A \mid \mathbf{b}]$?

<details><summary>Pista 1</summary>Filas de $A$ = ecuaciones; columnas de $A$ = incógnitas.</details>
<details><summary>Solución</summary>

$A$ es $3\times 4$; $\mathbf{x}$ es $4\times 1$; $\mathbf{b}$ es $3\times 1$; $[A \mid \mathbf{b}]$ es $3\times 5$. El producto $A\mathbf{x}$ está definido: $(3\times 4)(4\times 1)$ da $3\times 1$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar ecuaciones e incógnitas.</details>

### F07-N2-13 · [K] Tamaños en $A\mathbf{x} = \mathbf{b}$

**Objetivo**: relacionar ecuaciones e incógnitas con los tamaños de $A$, $\mathbf{x}$ y $\mathbf{b}$.
**Dificultad**: N2

**Enunciado.** Un sistema tiene 4 ecuaciones y 3 incógnitas. ¿Qué tamaño tienen $A$, $\mathbf{x}$, $\mathbf{b}$ y $[A \mid \mathbf{b}]$?

<details><summary>Pista 1</summary>Filas de $A$ = ecuaciones; columnas de $A$ = incógnitas.</details>
<details><summary>Solución</summary>

$A$ es $4\times 3$; $\mathbf{x}$ es $3\times 1$; $\mathbf{b}$ es $4\times 1$; $[A \mid \mathbf{b}]$ es $4\times 4$. El producto $A\mathbf{x}$ está definido: $(4\times 3)(3\times 1)$ da $4\times 1$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar ecuaciones e incógnitas.</details>

### F07-N2-14 · [K] Tamaños en $A\mathbf{x} = \mathbf{b}$

**Objetivo**: relacionar ecuaciones e incógnitas con los tamaños de $A$, $\mathbf{x}$ y $\mathbf{b}$.
**Dificultad**: N2

**Enunciado.** Un sistema tiene 2 ecuaciones y 2 incógnitas. ¿Qué tamaño tienen $A$, $\mathbf{x}$, $\mathbf{b}$ y $[A \mid \mathbf{b}]$?

<details><summary>Pista 1</summary>Filas de $A$ = ecuaciones; columnas de $A$ = incógnitas.</details>
<details><summary>Solución</summary>

$A$ es $2\times 2$; $\mathbf{x}$ es $2\times 1$; $\mathbf{b}$ es $2\times 1$; $[A \mid \mathbf{b}]$ es $2\times 3$. El producto $A\mathbf{x}$ está definido: $(2\times 2)(2\times 1)$ da $2\times 1$.

</details>
<details><summary>Errores frecuentes</summary>Intercambiar ecuaciones e incógnitas.</details>

### F07-N2-15 · [C] ¿Es solución? con $A\mathbf{x} = \mathbf{b}$

**Objetivo**: comprobar candidatos calculando $A\mathbf{x}$.
**Dificultad**: N2

**Enunciado.** Para $A = \begin{bmatrix} -3 & 2 & -1 \\ 0 & -2 & -3 \\ 3 & 1 & 2 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ -2 \end{bmatrix}$, ¿cuáles de los vectores $(0, 0, -1)$, $(1, 1, 0)$ cumplen $A\mathbf{x} = \mathbf{b}$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ para cada candidato y compáralo con $\mathbf{b}$.</details>
<details><summary>Solución</summary>

$(0, 0, -1)$: $A\mathbf{x} = \begin{bmatrix} 1 \\ 3 \\ -2 \end{bmatrix}$ = $\mathbf{b}$ ✓.

$(1, 1, 0)$: $A\mathbf{x} = \begin{bmatrix} -1 \\ -2 \\ 4 \end{bmatrix}$ ≠ $\mathbf{b}$: no es solución.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una ecuación.</details>

### F07-N2-16 · [C] ¿Es solución? con $A\mathbf{x} = \mathbf{b}$

**Objetivo**: comprobar candidatos calculando $A\mathbf{x}$.
**Dificultad**: N2

**Enunciado.** Para $A = \begin{bmatrix} 2 & 2 & -2 \\ 1 & 1 & 1 \\ -3 & -1 & 3 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} 2 \\ 1 \\ 5 \end{bmatrix}$, ¿cuáles de los vectores $(-2, 5, 1)$, $(-3, 4, 0)$ cumplen $A\mathbf{x} = \mathbf{b}$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ para cada candidato y compáralo con $\mathbf{b}$.</details>
<details><summary>Solución</summary>

$(-2, 5, 1)$: $A\mathbf{x} = \begin{bmatrix} 4 \\ 4 \\ 4 \end{bmatrix}$ ≠ $\mathbf{b}$: no es solución.

$(-3, 4, 0)$: $A\mathbf{x} = \begin{bmatrix} 2 \\ 1 \\ 5 \end{bmatrix}$ = $\mathbf{b}$ ✓.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una ecuación.</details>

### F07-N2-17 · [C] ¿Es solución? con $A\mathbf{x} = \mathbf{b}$

**Objetivo**: comprobar candidatos calculando $A\mathbf{x}$.
**Dificultad**: N2

**Enunciado.** Para $A = \begin{bmatrix} -2 & 0 & -2 \\ 0 & 3 & -2 \\ 0 & -1 & 2 \end{bmatrix}$ y $\mathbf{b} = \begin{bmatrix} 4 \\ -1 \\ -5 \end{bmatrix}$, ¿cuáles de los vectores $(3, -2, -3)$, $(2, -3, -4)$ cumplen $A\mathbf{x} = \mathbf{b}$?

<details><summary>Pista 1</summary>Calcula $A\mathbf{x}$ para cada candidato y compáralo con $\mathbf{b}$.</details>
<details><summary>Solución</summary>

$(3, -2, -3)$: $A\mathbf{x} = \begin{bmatrix} 0 \\ 0 \\ -4 \end{bmatrix}$ ≠ $\mathbf{b}$: no es solución.

$(2, -3, -4)$: $A\mathbf{x} = \begin{bmatrix} 4 \\ -1 \\ -5 \end{bmatrix}$ = $\mathbf{b}$ ✓.

</details>
<details><summary>Errores frecuentes</summary>Comprobar solo una ecuación.</details>

