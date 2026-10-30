# L37 — Cuando LU falla: permutaciones y PA = LU

**Objetivo**: factorizar matrices que obligan a intercambiar filas ($PA = LU$) y entender el pivoteo parcial.
**Prerrequisitos**: L27 (pivote 0), L35–L36.
**Código**: `escenas/l37_permutaciones_pa_lu.py`
**Videos**: `videos/l37_permutaciones_pa_lu/1080p60/` → `CuandoLUFalla.mp4`, `MatricesDePermutacion.mp4`, `PivoteoParcial.mp4`
**Ejercicios**: F10-N2-05, F10-N3-04, F10-N3-05, F10-N4-03, F10-N5-02.

---

## Desarrollo matemático

**Cuando falla.** $A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 5 \\ 4 & 6 & 8 \end{bmatrix}$: tras $R_2 \leftarrow R_2 - 2R_1$, $R_3 \leftarrow R_3 - 4R_1$, el pivote $(2,2)$ vale $0$ y $m_{32} = 2/0$ no existe. Intercambiando las filas 2 y 3 desde el principio: $PA = \begin{bmatrix} 1 & 1 & 1 \\ 4 & 6 & 8 \\ 2 & 2 & 5 \end{bmatrix} = LU$, $L = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 2 & 0 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 4 \\ 0 & 0 & 3 \end{bmatrix}$.

**Resolver.** $A\mathbf{x} = \mathbf{b} \iff PA\mathbf{x} = P\mathbf{b}$: reordenar $\mathbf{b}$, $L\mathbf{y} = P\mathbf{b}$, $U\mathbf{x} = \mathbf{y}$ (con $\mathbf{b} = (3, 9, 18)$: $P\mathbf{b} = (3, 18, 9)$, $\mathbf{y} = (3, 6, 3)$, $\mathbf{x} = (1, 1, 1)$).

**Permutaciones.** Identidad con las filas reordenadas; hay $n!$; $PA$ reordena filas de $A$; $P^{-1} = P^T$; el producto de permutaciones es permutación. **Teorema**: toda matriz cuadrada invertible admite $PA = LU$.

**Pivoteo parcial.** En cada columna se elige como pivote la entrada de mayor valor absoluto (multiplicadores $|m_{ij}| \le 1$). Ejemplo con 3 cifras significativas, $0{,}0001x + y = 1$, $x + y = 2$ (exacta $x \approx 1{,}0001$): sin intercambiar sale $x = 0$; con intercambio, $x = 1{,}00$ (comprobado con aritmética decimal de precisión 3 en `f10.py`). A mano, con fracciones exactas, no hay redondeo: basta evitar el $0$.

---

## Guion de narración

### Video 1 — `CuandoLUFalla`

| En pantalla | Narración |
|---|---|
| Eliminación que se atasca | "El pivote de la segunda columna vale cero: el multiplicador sería dos entre cero. Con solo reemplazos, ele u falla." |
| $PA = LU$ | "Si intercambiamos las filas dos y tres desde el principio, la eliminación ya no se atasca." |
| Resolver | "Reordenamos be, resolvemos ele ye igual a pe be, y u equis igual a ye." |

### Video 2 — `MatricesDePermutacion`

| En pantalla | Narración |
|---|---|
| $PA$ | "Una permutación es la identidad con las filas reordenadas; pe a reordena las filas de a." |
| Propiedades | "Ene factorial; la inversa es la traspuesta." |
| Teorema | "Toda matriz invertible admite pe a igual a ele u." |

### Video 3 — `PivoteoParcial`

| En pantalla | Narración |
|---|---|
| Regla | "Elegimos el pivote de mayor valor absoluto; los multiplicadores no superan a uno." |
| Con y sin intercambio | "Con tres cifras, sin intercambiar equis sale cero; intercambiando, uno." |
| Moraleja | "Dividir entre un pivote muy pequeño amplifica los errores de redondeo." |

---

## Errores frecuentes

- Olvidar reordenar $\mathbf{b}$ con la misma $P$.
- Confundir $P$ con $P^T$.
- Concluir que $A$ no es invertible porque falla la factorización sin permutar.
- Creer que el pivoteo solo sirve para evitar el cero.

## Resumen y conexión

$PA = LU$ siempre existe para matrices invertibles, y el pivoteo parcial es la forma estándar de calcularla. La L38 compara los métodos de toda la serie.
