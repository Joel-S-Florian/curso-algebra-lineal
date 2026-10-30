# L39 — El rango de una matriz

**Objetivo**: definir el rango como número de pivotes, entender por qué está bien definido y distinguir el rango de $A$ del de $[A \mid \mathbf{b}]$.
**Prerrequisitos**: L25 (pivotes), L31 (reducida única), L32.
**Código**: `escenas/l39_rango.py`
**Videos**: `videos/l39_rango/1080p60/` → `RangoComoNumeroDePivotes.mp4`, `RangoDeAyDeAumentada.mp4`, `RangoNoEsNumeroDeEcuaciones.mp4`
**Ejercicios**: F11-N1-01, F11-N2-01, F11-N2-02, F11-N3-01, F11-N3-03.

---

## Desarrollo matemático

**Definición.** $\operatorname{rg}(A)$ es el número de pivotes de cualquier forma escalonada de $A$ (= número de filas no nulas). Está bien definido: las posiciones de los pivotes no dependen del camino (L25) y la reducida es única (L31). Como hay a lo sumo un pivote por fila y por columna, $\operatorname{rg}(A) \le \min(m, n)$.

**Ejemplo.** $\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 1 & 1 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & 3 \\ 0 & -1 & -2 \\ 0 & 0 & 0 \end{bmatrix}$: rango $2$.

**Dos rangos.** $\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1$: al escalonar $[A \mid \mathbf{b}]$ se escalona $A$, y la columna $\mathbf{b}$ aporta a lo sumo un pivote.

**El rango no es el número de ecuaciones**: es el de ecuaciones independientes (las que traen un pivote nuevo).

---

## Guion de narración

### Video 1 — `RangoComoNumeroDePivotes`

| En pantalla | Narración |
|---|---|
| Escalonar | "A la fila dos le restamos dos veces la uno: queda de ceros. A la tres, la uno; y se intercambian las filas dos y tres. Dos pivotes: rango dos." |
| Definición | "El rango es el número de pivotes de una forma escalonada; está bien definido porque la reducida es única; y no supera ni a las filas ni a las columnas." |

### Video 2 — `RangoDeAyDeAumentada`

| En pantalla | Narración |
|---|---|
| Dos escalonadas de L28 | "En el primero los dos rangos valen dos; en el segundo, hay un pivote más en la columna de be: rango dos y rango tres." |
| Desigualdades | "El rango de a es menor o igual que el de la aumentada, y este, menor o igual que el de a más uno." |

### Video 3 — `RangoNoEsNumeroDeEcuaciones`

| En pantalla | Narración |
|---|---|
| Tres ecuaciones, rango 2 | "La tercera ecuación es la suma de las otras dos: queda una fila de ceros." |
| Qué mide | "El rango cuenta las ecuaciones realmente independientes: cada una quita una libertad." |

---

## Errores frecuentes

- Contar ecuaciones en lugar de pivotes.
- Calcular solo el rango de $A$ (o solo el de $[A \mid \mathbf{b}]$).
- Contar las columnas con algún elemento no nulo como pivotes.

## Resumen y conexión

Rango = pivotes. Con él, la L40 clasifica sistemas sin resolverlos: el teorema de Rouché-Frobenius.
