# L23 — Matriz aumentada y sistemas equivalentes

**Objetivo**: construir e interpretar $[A \mid \mathbf{b}]$, distinguirla de $A$, y entender que operar con ecuaciones es operar con filas.
**Prerrequisitos**: L15 (reducción), L22.
**Código**: `escenas/l23_matriz_aumentada.py`
**Videos**: `videos/l23_matriz_aumentada/1080p60/` → `SistemaAMatrizAumentada.mp4`, `SistemasEquivalentes.mp4`
**Ejercicios**: F07-N1-02, F07-N3-01.

---

## Desarrollo matemático

**Matriz aumentada.** $[A \mid \mathbf{b}]$ es $A$ con $\mathbf{b}$ añadida como última columna; la barra recuerda el "=". Con $m$ ecuaciones y $n$ incógnitas es $m\times(n + 1)$. Cada fila es una ecuación; cada columna, una incógnita, y la última, los términos independientes.

**Leer al revés.** $\left[\begin{array}{ccc|c} 1 & 0 & 2 & 3 \\ 0 & 1 & -1 & 4 \end{array}\right]$ es $x + 2z = 3$, $y - z = 4$ (un 0 = la incógnita no aparece).

**$A$ frente a $[A \mid \mathbf{b}]$.** $A$ sola no basta: los sistemas con $A = \begin{bmatrix} 2 & 1 & -1 \\ 1 & -3 & 2 \\ 4 & 0 & 1 \end{bmatrix}$ y $\mathbf{b} = (2, 0, 5)$ o $\mathbf{b} = \mathbf{0}$ tienen soluciones distintas. En un homogéneo la última columna es nula.

**Sistemas equivalentes.** Mismo conjunto de soluciones. Las operaciones de reducción (L15) actúan solo sobre los números: "restar la ecuación 1" es "restar la fila 1", $R_2 \leftarrow R_2 - R_1$. Se escribe $\sim$ entre matrices aumentadas de sistemas equivalentes (las matrices son distintas; las soluciones, no).

$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 1 & -1 & 1 & 2 \\ 1 & 1 & -1 & 0 \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -2 & 0 & -4 \\ 0 & 0 & -2 & -6 \end{array}\right]$$

El segundo, con ceros bajo la diagonal, se resuelve de abajo arriba: $z = 3$, $y = 2$, $x = 1$. Llegar a esa forma sistemáticamente es la eliminación de Gauss.

---

## Guion de narración

### Video 1 — `SistemaAMatrizAumentada`

| En pantalla | Narración |
|---|---|
| Ecuaciones → filas | "Cada ecuación se convierte en una fila: los coeficientes y, tras la barra, el término independiente. Es la matriz aumentada, de tres por cuatro." |
| Leer al revés | "Para volver al sistema, cada columna es una incógnita; un cero significa que esa incógnita no aparece." |
| Misma $A$, distinto $\mathbf{b}$ | "Estos dos sistemas tienen la misma matriz A y distintas soluciones: A sola no basta, hace falta be." |

### Video 2 — `SistemasEquivalentes`

| En pantalla | Narración |
|---|---|
| Filas restadas | "Restar la primera ecuación a la segunda es restar la primera fila a la segunda. El símbolo de equivalencia indica que las matrices son distintas pero los sistemas tienen las mismas soluciones." |
| Comprobación con $(1, 2, 3)$ | "Uno, dos, tres cumple los dos sistemas." |
| Resolver de abajo arriba | "El sistema de la derecha se resuelve de abajo arriba gracias a los ceros bajo la diagonal. Llegar ahí con operaciones permitidas es la eliminación de Gauss." |

---

## Errores frecuentes

- Olvidar ceros o poner incógnitas en la última columna.
- Confundir $A$ con $[A \mid \mathbf{b}]$ (y sus dimensiones).
- Aplicar una operación a una fila sin incluir la columna de $\mathbf{b}$.
- Escribir "=" entre matrices de sistemas equivalentes (son distintas).

## Resumen y conexión

$[A \mid \mathbf{b}]$ contiene todo el sistema, y operar con ecuaciones es operar con filas. Con esta lección termina la Unidad 3. En la Unidad 4 (Lección 24) definimos las operaciones elementales por filas y demostramos que conservan las soluciones.
