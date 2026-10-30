# L49 — Una base del espacio columna

**Objetivo**: hallar una base de $\operatorname{Col}(A)$ con las columnas pivote **de la matriz original** y entender por qué.
**Prerrequisitos**: L44, L46, L48.
**Código**: `escenas/l49_base_del_espacio_columna.py`
**Videos**: `videos/l49_base_del_espacio_columna/1080p60/` → `ColumnasPivote.mp4`, `PorQueEnLaMatrizOriginal.mp4`
**Ejercicios**: F14-N3-01, F14-N3-02, F14-N3-03, F14-N3-04, F14-N4-04.

---

## Desarrollo matemático

**Receta.** Reducir $A$; las columnas de $A$ (original) donde la reducida tiene pivote son una base de $\operatorname{Col}(A)$; $\dim\operatorname{Col}(A) = \operatorname{rg}(A)$. Las otras columnas se escriben con las pivote leyendo la reducida.
Ejemplo: pivotes en 1 y 3, base $\{(1,2,1),(0,1,1)\}$; $\mathbf{a}_2 = 2\mathbf{a}_1$, $\mathbf{a}_4 = \mathbf{a}_1 + 2\mathbf{a}_3$.

**Por qué la original.** Las operaciones por filas cambian el espacio columna: $(1,2,1) \in \operatorname{Col}(A)$ pero no está en $\operatorname{Col}(R)$ (tercera componente $0$). Lo que se conserva: $A\mathbf{x} = \mathbf{0} \iff R\mathbf{x} = \mathbf{0}$ (mismas relaciones entre columnas).

**Demostración.** En $R$ las columnas pivote son $\mathbf{e}_1,\dots,\mathbf{e}_r$ (independientes) y las libres son combinación de ellas; las mismas relaciones valen en $A$.

---

## Guion de narración

### Video 1 — `ColumnasPivote`

| En pantalla | Narración |
|---|---|
| $A \to R$ | "Los pivotes caen en las columnas uno y tres." |
| Base | "Las columnas de la original donde hay pivote." |
| Relaciones | "Los coeficientes se leen en la reducida." |
| Receta | "Cuatro pasos." |

### Video 2 — `PorQueEnLaMatrizOriginal`

| En pantalla | Narración |
|---|---|
| $\operatorname{Col}(R) \ne \operatorname{Col}(A)$ | "La tercera componente es cero en la reducida." |
| $R = EA$ | "Mismo núcleo: mismas relaciones entre columnas." |
| Demostración | "Las pivote son independientes y generan las demás." |

---

## Errores frecuentes

- Tomar las columnas pivote de la reducida.
- Pensar que $\operatorname{Col}(A)$ y $\operatorname{Col}(R)$ son iguales porque tienen la misma dimensión.
- Olvidar que el número de vectores de la base es el rango.

## Resumen y conexión

Base de $\operatorname{Col}(A)$ = pivote de $A$. La L50 junta núcleo e imagen: rango + nulidad = $n$.
