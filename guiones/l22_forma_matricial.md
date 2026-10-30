# L22 — De sistema a Ax = b

**Objetivo**: escribir cualquier sistema lineal como $A\mathbf{x} = \mathbf{b}$ y entender por qué el producto reproduce las ecuaciones término a término.
**Prerrequisitos**: L10, L19.
**Código**: `escenas/l22_forma_matricial.py`
**Videos**: `videos/l22_forma_matricial/1080p60/` → `ConstruirAxb.mp4`, `AxReproduceLasEcuaciones.mp4`
**Ejercicios**: F07-N1-01, F07-N2-01, F07-N2-02, F07-N4-01, F07-N5-01.

---

## Desarrollo matemático

**Paso 0: ordenar.** Incógnitas a la izquierda, siempre en el mismo orden; números a la derecha. Si una incógnita no aparece, su coeficiente es 0. Ejemplo: $z = 5 - 4x$ pasa a $4x + 0y + z = 5$.

**Piezas.** Para $\sum_j a_{ij}x_j = b_i$ ($i = 1, \dots, m$):

- $A = [a_{ij}]$, $m\times n$: **matriz de coeficientes** (fila = ecuación, columna = incógnita).
- $\mathbf{x} = (x_1, \dots, x_n)$: **vector de incógnitas**.
- $\mathbf{b} = (b_1, \dots, b_m)$: **vector de términos independientes**.

Ejemplo: $2x + y - z = 2$, $x - 3y + 2z = 0$, $4x + z = 5$ da $A = \begin{bmatrix} 2 & 1 & -1 \\ 1 & -3 & 2 \\ 4 & 0 & 1 \end{bmatrix}$, $\mathbf{b} = (2, 0, 5)$.

**Por qué $A\mathbf{x} = \mathbf{b}$ es el sistema.** Por la definición de L19, $(A\mathbf{x})_i = a_{i1}x_1 + \cdots + a_{in}x_n$, exactamente el lado izquierdo de la ecuación $i$. Dos vectores son iguales si coinciden componente a componente, así que $A\mathbf{x} = \mathbf{b}$ equivale a las $m$ ecuaciones a la vez.

**Por columnas.** $A\mathbf{x} = x_1\mathbf{a}_1 + \cdots + x_n\mathbf{a}_n = \mathbf{b}$: resolver es buscar los pesos que combinan las columnas para obtener $\mathbf{b}$.

**Verificar** una solución es calcular $A\mathbf{x}$ y compararlo con $\mathbf{b}$: $A(1, 1, 1) = (2, 0, 5)$ ✓; $A(1, 0, 1) = (1, 3, 5) \neq \mathbf{b}$.

---

## Guion de narración

### Video 1 — `ConstruirAxb`

| En pantalla | Narración |
|---|---|
| Sistema desordenado → ordenado | "Primero ordenamos: todas las incógnitas a la izquierda y en el mismo orden. La tercera ecuación, zeta igual a cinco menos cuatro equis, pasa a cuatro equis más zeta igual a cinco. Y como no aparece ye, escribimos cero ye." |
| Coeficientes viajando a $A$ | "La matriz A recoge los coeficientes: cada ecuación en una fila y cada incógnita en una columna, con su signo." |
| $\mathbf{x}$, $\mathbf{b}$ y dimensiones | "Equis es el vector de incógnitas y be el de términos independientes. El sistema entero cabe en tres símbolos: A equis igual a be." |

### Video 2 — `AxReproduceLasEcuaciones`

| En pantalla | Narración |
|---|---|
| $A$ por $(x, y, z)$ fila a fila | "Si multiplicamos A por el vector de incógnitas, cada fila produce exactamente el lado izquierdo de una ecuación, término por término." |
| $= \mathbf{b}$ → sistema | "Igualar ese vector a be es escribir las tres ecuaciones a la vez." |
| Por columnas | "Por columnas: buscamos los pesos equis, ye, zeta que combinan las columnas de A para obtener be." |
| Verificación | "Y comprobar una solución es multiplicar: uno, uno, uno da be; uno, cero, uno no." |

---

## Errores frecuentes

- Olvidar los ceros o los signos.
- No pasar todas las incógnitas a la izquierda antes de construir $A$.
- Poner incógnitas dentro de $\mathbf{b}$.
- Cambiar el orden de las incógnitas entre ecuaciones.

## Resumen y conexión

Todo sistema es $A\mathbf{x} = \mathbf{b}$. En la Lección 23 juntamos $A$ y $\mathbf{b}$ en una sola tabla, la matriz aumentada, sobre la que trabajarán todos los métodos.
