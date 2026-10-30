# L35 — De dónde sale A = LU

**Objetivo**: entender que los multiplicadores de la eliminación forman $L$ y por qué caen en su sitio.
**Prerrequisitos**: L26 (Gauss), L34 (matrices elementales).
**Código**: `escenas/l35_de_donde_sale_lu.py`
**Videos**: `videos/l35_de_donde_sale_lu/1080p60/` → `LosMultiplicadoresSeGuardan.mp4`, `ConstruirLyU.mp4`
**Ejercicios**: F10-N2-03, F10-N3-01, F10-N3-02, F10-N4-01, F10-N5-01.

---

## Desarrollo matemático

**Regla.** Si la eliminación hace $R_i \leftarrow R_i - m_{ij}R_j$ para $i > j$ (sin intercambios), entonces $A = LU$ con $U$ la matriz escalonada y $L_{ij} = m_{ij}$ (unos en la diagonal, ceros encima). En el ejemplo: $m_{21} = 2$, $m_{31} = -1$, $m_{32} = -3$.

**Por qué.** $E_{32}E_{31}E_{21}A = U$, así que $A = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}U$ y $L = E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}$. Cada inversa solo cambia el signo del multiplicador. En ese orden el producto coloca cada $m_{ij}$ en su posición; en el orden contrario, $E_{32}^{-1}E_{31}^{-1}E_{21}^{-1}$, aparece $-1 + (-3)(2) = -7$ en la posición $(3,1)$.

**Condiciones.** Solo operaciones de reemplazo hacia abajo (sin intercambios) y un pivote $\ne 0$ en cada paso (si no, $PA = LU$, L37). Si $A$ es invertible y existe $A = LU$ con $L$ de unos en la diagonal, es **única** (se demuestra con $L_2^{-1}L_1 = U_2U_1^{-1}$: triangular inferior con unos e igual a una superior, luego es $I$).

---

## Guion de narración

### Video 1 — `LosMultiplicadoresSeGuardan`

| En pantalla | Narración |
|---|---|
| Eliminación con $L$ empezando en $I$ | "Repetimos la eliminación guardando cada multiplicador en su posición de ele: el dos, el menos uno y el menos tres." |
| $L$ y $U$ finales | "A la izquierda queda u, la escalonada; a la derecha, ele. Y a es ele por u." |
| Comprobación de filas | "La fila dos de ele u es dos veces la fila uno más la fila dos; la tres, menos la uno, menos tres veces la dos, más la tres." |

### Video 2 — `ConstruirLyU`

| En pantalla | Narración |
|---|---|
| $E_{32}E_{31}E_{21}A = U$ | "Despejando a, ele es el producto de las inversas de las elementales." |
| Inversas | "Deshacer restar el doble es sumar el doble: cada inversa cambia el signo del multiplicador." |
| Orden correcto y contrario | "En este orden los multiplicadores caen en su sitio; en el contrario aparece un menos siete." |
| Condiciones | "Sin intercambios y con pivotes distintos de cero; si no, la lección treinta y siete." |

---

## Errores frecuentes

- Anotar en $L$ el multiplicador con el signo cambiado.
- Multiplicar las inversas en el orden contrario.
- Calcular $m_{32}$ con la fila 3 original en lugar de la ya modificada.

## Resumen y conexión

$L$ es la eliminación "grabada": sus entradas son los multiplicadores. Con ella, resolver con $LU$ es casi gratis (L36).
