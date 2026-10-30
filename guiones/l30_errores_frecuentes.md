# L30 — Errores frecuentes en Gauss y cómo verificar

**Objetivo**: reconocer los errores aritméticos y de procedimiento más comunes y verificar cada tipo de resultado (SCD, SCI, SI) de forma fiable.
**Prerrequisitos**: L22 ($A\mathbf{x} = \mathbf{b}$), L24–L29.
**Código**: `escenas/l30_errores_frecuentes.py`
**Videos**: `videos/l30_errores_frecuentes/1080p60/` → `ErroresFrecuentesGauss.mp4`, `VerificarSiempre.mp4`
**Ejercicios**: F08-N3-04, F08-N4-07 (en video); F08-N4-06.

---

## Desarrollo matemático

**1. Signos.** En $\left[\begin{array}{cc|c} 1 & -2 & 3 \\ 3 & -4 & 5 \end{array}\right]$, $R_2 \leftarrow R_2 - 3R_1$ da en la columna 2: $-4 - 3\cdot(-2) = -4 + 6 = 2$ (no $-10$). Fila correcta $[\,0 \ \ 2 \mid -4\,]$.

**2. Olvidar $\mathbf{b}$.** La misma operación en la última columna: $5 - 3\cdot 3 = -4$; escribir $[\,0 \ \ 2 \mid 5\,]$ es otra ecuación.

**3. Operaciones no elementales.** $R_1 \leftarrow 0\cdot R_1$ (sin inversa); $R_1 \leftarrow R_1\cdot R_2$ entrada a entrada (ni siquiera da una ecuación lineal); $R_1 \leftarrow R_1 + 3$ ($[\,1 \ \ 1 \mid 2\,] \to [\,4 \ \ 4 \mid 5\,]$, otra recta); $R_2 \leftarrow R_2 - R_2$ (es $0\cdot R_2$).

**4. Dos operaciones a la vez.** En $\left[\begin{array}{cc|c} 1 & 1 & 2 \\ 1 & -1 & 0 \end{array}\right]$, hacer simultáneamente $R_1 \leftarrow R_1 - R_2$ y $R_2 \leftarrow R_2 - R_1$ (ambas con las filas viejas) da $\left[\begin{array}{cc|c} 0 & 2 & 2 \\ 0 & -2 & -2 \end{array}\right]$, con filas proporcionales (aparenta SCI), cuando el original tiene solución única $(1, 1)$. El par simultáneo no es una sucesión de operaciones elementales y no se puede deshacer. De una en una no hay problema.

**5. Otros.** Redondear a decimales; copiar mal una fila que no cambia; usar como pivote algo que vale (o puede valer) 0.

**Verificar en el original.** Con el error de signo, la fila $[\,0 \ \ -10 \mid -4\,]$ lleva a $y = \frac25$, $x = \frac{19}{5}$, que cumple el sistema escalonado equivocado ($\frac{19}{5} - \frac45 = 3$, $-10\cdot\frac25 = -4$) pero no el original: $3\cdot\frac{19}{5} - 4\cdot\frac25 = \frac{49}{5} \neq 5$. La solución correcta $(-1, -2)$ sí: $-1 + 4 = 3$, $-3 + 8 = 5$. Equivale a comprobar $A\mathbf{x} = \mathbf{b}$.

**Cómo se verifica cada resultado.**

- SCD: sustituir en todas las ecuaciones originales.
- SCI: sustituir la fórmula con $t$ general (los términos en $t$ deben cancelarse) y además un valor concreto.
- SI: exhibir la combinación de ecuaciones que da $0 = c$, $c \neq 0$ (en la L28, $E_3 - E_1 - E_2$ da $0 = 1$).

**Lista de control.** Escribir cada operación; una por paso; toda la fila; cuentas por columnas con paréntesis; fracciones exactas; con parámetros, separar casos antes de dividir; comprobar en el original.

---

## Guion de narración

### Video 1 — `ErroresFrecuentesGauss`

| En pantalla | Narración |
|---|---|
| Signos | "Menos cuatro menos tres por menos dos es menos cuatro más seis: dos. Restar un negativo es sumar." |
| Columna $\mathbf{b}$ | "La operación es sobre la ecuación entera: el término independiente también se resta." |
| Operaciones ilegales | "Multiplicar por cero, multiplicar filas entre sí, sumar un número a cada entrada… nada de eso es una operación elemental." |
| A la vez | "Si las dos operaciones usan las filas viejas, se pierde información: parece que hay infinitas soluciones y en realidad hay una." |

### Video 2 — `VerificarSiempre`

| En pantalla | Narración |
|---|---|
| Error que no se ve | "La solución equivocada cumple el sistema escalonado equivocado. Solo el sistema original delata el error." |
| $A\mathbf{x} = \mathbf{b}$ | "Es lo mismo que comprobar que A por equis da be." |
| Cada tipo | "Una solución: se sustituye. Infinitas: se sustituye con te general. Ninguna: se muestra la combinación que da cero igual a ce." |
| Lista de control | "Una operación por paso, toda la fila, paréntesis, fracciones exactas, casos antes de dividir y comprobación en el original." |

---

## Errores frecuentes

Los de esta lección son el resumen de toda la unidad: signos, columna de $\mathbf{b}$, operaciones ilegales, operaciones simultáneas, decimales, pivotes nulos o que pueden anularse, y verificar en el sistema transformado.

## Resumen y conexión

Un error de cuentas produce un sistema escalonado coherente pero falso: por eso se verifica siempre en el original. Con esta lección termina la Unidad 4. En la Unidad 5 (L31) continuamos la eliminación hacia arriba hasta la forma escalonada reducida (Gauss-Jordan), donde la solución se lee directamente.
