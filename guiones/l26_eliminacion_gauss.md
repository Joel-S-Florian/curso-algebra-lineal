# L26 — Eliminación hacia adelante y sustitución hacia atrás

**Objetivo**: resolver sistemas 2 × 2 y 3 × 3 por eliminación de Gauss, con el multiplicador bien calculado, y verificar en el sistema original.
**Prerrequisitos**: L24, L25, L22 (verificar con $A\mathbf{x} = \mathbf{b}$).
**Código**: `escenas/l26_eliminacion_gauss.py`
**Videos**: `videos/l26_eliminacion_gauss/1080p60/` → `GaussDosPorDos.mp4`, `GaussTresPorTres.mp4`
**Ejercicios**: F08-N2-03, F08-N2-04 (en video); F08-N3-01.

---

## Desarrollo matemático

**Algoritmo.**

1. *Eliminación hacia adelante.* Columna a columna, de izquierda a derecha: se toma el pivote $p$ de la fila actual y, para cada fila $i$ de debajo con entrada $a$ en esa columna, $R_i \leftarrow R_i - m\,R_p$ con **multiplicador** $m = a / p$. Así la entrada pasa a ser $a - m\,p = 0$.
2. *Sustitución hacia atrás.* La última ecuación tiene una sola incógnita pivote; se despeja y se sube sustituyendo.
3. *Verificación* en el sistema original.

**Ejemplo 2 × 2.** $2x + 3y = 8$, $4x - y = 2$. $m = 4/2 = 2$:
$\left[\begin{array}{cc|c} 2 & 3 & 8 \\ 4 & -1 & 2 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{cc|c} 2 & 3 & 8 \\ 0 & -7 & -14 \end{array}\right]$, $y = 2$, $2x + 6 = 8 \Rightarrow x = 1$. Verificación: $2 + 6 = 8$, $4 - 2 = 2$.

**Multiplicador fraccionario.** $\left[\begin{array}{cc|c} 2 & 3 & 8 \\ 3 & 1 & 5 \end{array}\right]$ con $m = \frac32$ da $[\,0 \ \ -\frac72 \mid -7\,]$: $y = 2$, $x = 1$. Alternativa sin fracciones: $R_2 \leftarrow 2R_2 - 3R_1$ (escalado por $2 \neq 0$ seguido de reemplazo), que da $[\,0 \ \ -7 \mid -14\,]$.

**Ejemplo 3 × 3.** $x + 2y - z = -3$, $2x + 3y + z = 1$, $-x + y + 2z = 2$:
$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & -3 \\ 2 & 3 & 1 & 1 \\ -1 & 1 & 2 & 2 \end{array}\right] \xrightarrow[R_3 \leftarrow R_3 + R_1]{R_2 \leftarrow R_2 - 2R_1} \left[\begin{array}{ccc|c} 1 & 2 & -1 & -3 \\ 0 & -1 & 3 & 7 \\ 0 & 3 & 1 & -1 \end{array}\right] \xrightarrow{R_3 \leftarrow R_3 + 3R_2} \left[\begin{array}{ccc|c} 1 & 2 & -1 & -3 \\ 0 & -1 & 3 & 7 \\ 0 & 0 & 10 & 20 \end{array}\right]$$
(en la columna 2, $m = 3/(-1) = -3$). Hacia atrás: $z = 2$; $-y + 6 = 7 \Rightarrow y = -1$; $x - 2 - 2 = -3 \Rightarrow x = 1$. Verificación: $1 - 2 - 2 = -3$, $2 - 3 + 2 = 1$, $-1 - 1 + 4 = 2$; es decir, $A(1, -1, 2) = \mathbf{b}$.

**Por qué el orden.** Al trabajar la columna $k$ solo se combinan filas que ya tienen ceros en las columnas $1, \dots, k-1$, así que esos ceros se conservan. Usar una fila de arriba (por ejemplo $R_3 \leftarrow R_3 - 3R_1$ en la columna 2) haría reaparecer la $x$. En un sistema $n \times n$ hay que conseguir $\frac{n(n-1)}{2}$ ceros.

---

## Guion de narración

### Video 1 — `GaussDosPorDos`

| En pantalla | Narración |
|---|---|
| Dos fases y multiplicador | "Primero, ceros debajo de cada pivote; después, de abajo arriba. El multiplicador es la entrada que queremos anular dividida por el pivote." |
| Sistema y matriz juntos | "Cuatro entre dos es dos: a la fila dos le restamos dos veces la fila uno. En el sistema, la equis desaparece de la segunda ecuación." |
| Sustitución hacia atrás | "Menos siete y igual a menos catorce: y vale dos. Arriba, dos equis más seis igual a ocho: equis vale uno." |
| Verificación | "Comprobamos en el sistema original, no en el escalonado." |
| Multiplicador $\frac32$ | "Si el multiplicador es una fracción, se opera con fracciones exactas; o se escala primero para evitarlas." |

### Video 2 — `GaussTresPorTres`

| En pantalla | Narración |
|---|---|
| Columna 1 | "El pivote es el uno de arriba: restamos dos veces la fila uno a la dos y sumamos la fila uno a la tres." |
| Columna 2 | "Ahora el pivote es el menos uno de la fila dos nueva. Tres entre menos uno es menos tres: sumamos tres veces la fila dos." |
| Hacia atrás | "Zeta vale dos, y vale menos uno, equis vale uno." |
| Verificación y orden | "Las tres ecuaciones originales se cumplen. Columna a columna, cada pivote solo anula lo que tiene debajo." |

---

## Errores frecuentes

- Signo del multiplicador: $R_2 \leftarrow R_2 + 2R_1$ no anula nada.
- Invertir el cociente (pivote entre entrada).
- Usar la fila 2 vieja como pivote de la columna 2.
- Con pivote negativo, restar $-3R_2$ es sumar $3R_2$.
- Verificar en el sistema escalonado.

## Resumen y conexión

Gauss = eliminación hacia adelante + sustitución hacia atrás + verificación. En la L27 vemos qué hacer cuando el pivote que toca vale 0 y qué significa una fila entera de ceros.
