# L24 — Operaciones elementales por filas

**Objetivo**: conocer las tres operaciones elementales, aplicarlas a la fila entera de $[A \mid \mathbf{b}]$ y demostrar que conservan el conjunto solución.
**Prerrequisitos**: L15 (reducción), L23 (matriz aumentada, sistemas equivalentes), L04 (inclusión e igualdad de conjuntos).
**Código**: `escenas/l24_operaciones_elementales.py` (usa `EscenaCurso.operar_filas` y `matriz_gauss` de `curso/componentes.py`)
**Videos**: `videos/l24_operaciones_elementales/1080p60/` → `OperacionesElementales.mp4`, `CadaOperacionSeDeshace.mp4`
**Ejercicios**: F08-N1-01, F08-N2-01 (en video); F08-N4-01, F08-N5-01, F08-N5-02.

---

## Desarrollo matemático

**Notación.** $R_i$ es la fila $i$ de $[A \mid \mathbf{b}]$; $R_i \leftarrow (\text{expresión})$ significa "la fila $i$ se sustituye por". Solo cambia la fila de la izquierda de la flecha.

**Las tres operaciones elementales.**

1. Intercambio: $R_i \leftrightarrow R_j$.
2. Escalado: $R_i \leftarrow k R_i$ con $k \neq 0$.
3. Reemplazo: $R_i \leftarrow R_i + k R_j$ con $i \neq j$ ($k$ cualquiera).

Se aplican a la fila entera, columna de $\mathbf{b}$ incluida, porque cada fila es una ecuación completa.

**Ejemplos del video.** $\left[\begin{array}{cc|c} 0 & 3 & 6 \\ 1 & 1 & 3 \end{array}\right] \xrightarrow{R_1 \leftrightarrow R_2} \left[\begin{array}{cc|c} 1 & 1 & 3 \\ 0 & 3 & 6 \end{array}\right]$ y la cadena
$$\left[\begin{array}{cc|c} 2 & 4 & 10 \\ 3 & -1 & 1 \end{array}\right] \xrightarrow{R_1 \leftarrow \frac12 R_1} \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 3 & -1 & 1 \end{array}\right] \xrightarrow{R_2 \leftarrow R_2 - 3R_1} \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & -7 & -14 \end{array}\right] \xrightarrow{R_2 \leftarrow -\frac17 R_2} \left[\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 2 \end{array}\right],$$
todos con solución $(1, 2)$.

**Por qué $k \neq 0$.** $R_2 \leftarrow 0\cdot R_2$ convierte $3x - y = 1$ en $0 = 0$: el par $(5, 0)$ cumple el sistema nuevo pero no el original. Se pierde información y no hay vuelta atrás.

**Teorema.** Si $S'$ se obtiene de $S$ con una operación elemental, $\mathrm{Sol}(S) = \mathrm{Sol}(S')$.

*Demostración.* (1) Sea $\mathbf{s}$ solución de $S$. Cada ecuación de $S'$ es una ecuación de $S$, o $k$ veces una ecuación de $S$, o $E_i + kE_j$. Si las igualdades $E_i$ y $E_j$ son ciertas en $\mathbf{s}$, también lo son $kE_i$ y $E_i + kE_j$ (se multiplican y suman igualdades). Luego $\mathrm{Sol}(S) \subseteq \mathrm{Sol}(S')$.
(2) Cada operación tiene una inversa elemental: $R_i \leftrightarrow R_j$ se deshace con ella misma; $R_i \leftarrow kR_i$ con $R_i \leftarrow \frac1k R_i$ (necesita $k \neq 0$); $R_i \leftarrow R_i + kR_j$ con $R_i \leftarrow R_i - kR_j$ (necesita $i \neq j$: así $R_j$ no ha cambiado). Por tanto $S$ se obtiene de $S'$ con una operación elemental y, por (1), $\mathrm{Sol}(S') \subseteq \mathrm{Sol}(S)$.
(3) Las dos inclusiones dan la igualdad; para una cadena de operaciones se aplica en cada paso. $\blacksquare$

**Sin inversa solo vale (1).** Con $0 \cdot R_2$ la inclusión (1) se cumple, pero aparecen soluciones nuevas: la (2) falla.

---

## Guion de narración

### Video 1 — `OperacionesElementales`

| En pantalla | Narración |
|---|---|
| Las tres operaciones | "En la reducción cambiábamos ecuaciones por otras más sencillas. Ahora lo hacemos con filas y solo con tres movimientos: intercambiar, multiplicar por un número distinto de cero y sumar a una fila un múltiplo de otra." |
| Intercambio | "Arriba hay un cero: conviene empezar por la otra ecuación. Cambiar el orden no cambia las soluciones." |
| Escalado por $\frac12$ y caso $k = 0$ | "Multiplicar por un medio simplifica la fila. Pero multiplicar por cero convierte una ecuación en cero igual a cero: aparecen soluciones falsas, como cinco cero." |
| Reemplazo $R_2 \leftarrow R_2 - 3R_1$ | "A la fila dos le restamos tres veces la fila uno: debajo del pivote aparece un cero. La fila uno no cambia." |
| Cadena con $\sim$ | "Todas las matrices de la cadena tienen la misma solución, uno dos." |

### Video 2 — `CadaOperacionSeDeshace`

| En pantalla | Narración |
|---|---|
| Combinación de igualdades | "Si dos igualdades son ciertas, cualquier combinación también lo es: la solución vieja cumple las ecuaciones nuevas." |
| Tabla de inversas | "Cada operación se deshace con otra del mismo tipo. Por eso pedimos k distinto de cero e i distinto de j." |
| Ida y vuelta | "Restamos tres veces la fila uno y la volvemos a sumar: regresamos a la matriz de partida." |
| Demostración | "Primera inclusión: lo viejo cumple lo nuevo. Segunda: lo nuevo vuelve a lo viejo con la inversa. Las dos juntas dan la igualdad de conjuntos." |
| Sin inversa | "Con cero por la fila dos solo vale la primera mitad: el sistema gana soluciones que no tenía." |

---

## Errores frecuentes

- Operar solo los coeficientes y olvidar la columna de $\mathbf{b}$.
- Cambiar también la fila de origen en $R_2 \leftarrow R_2 - 3R_1$.
- Multiplicar una fila por 0 o sumarle un múltiplo de sí misma.
- Escribir "=" entre matrices equivalentes (se escribe $\sim$).
- Demostrar la equivalencia con una sola inclusión.

## Resumen y conexión

Tres operaciones —intercambio, escalado por $k \neq 0$ y reemplazo con $i \neq j$— transforman el sistema sin cambiar sus soluciones, porque cada una se deshace. En la L25 definimos la forma a la que queremos llegar con ellas: la forma escalonada.
