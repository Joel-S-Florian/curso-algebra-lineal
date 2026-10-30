# L46 — Base del núcleo y nulidad

**Objetivo**: obtener una base del núcleo con las variables libres y definir la nulidad, $\operatorname{nul}(A) = n - \operatorname{rg}(A)$.
**Prerrequisitos**: L32 (básicas y libres), L44, L45.
**Código**: `escenas/l46_base_y_nulidad.py`
**Videos**: `videos/l46_base_y_nulidad/1080p60/` → `VariablesLibresDanLaBase.mp4`, `Nulidad.mp4`
**Ejercicios**: F13-N3-01, F13-N3-02, F13-N3-03, F13-N3-04.

---

## Desarrollo matemático

**Receta.** Reducir $A$; localizar las variables libres; por cada una, vector con esa libre $= 1$ y las demás libres $= 0$; esos vectores son una base de $\ker A$.

**Ejemplo.** $A = \begin{bmatrix} 1&2&0&1\\2&4&1&4\\1&2&1&3 \end{bmatrix}$, reducida $\begin{bmatrix} 1&2&0&1\\0&0&1&2\\0&0&0&0 \end{bmatrix}$; libres $x_2 = s$, $x_4 = t$: $\mathbf{x} = s(-2,1,0,0) + t(-1,0,-2,1)$. Generan (así se obtuvo) y son independientes (componentes 2 y 4 valen $(1,0)$ y $(0,1)$). $\dim\ker A = 2$.

**Nulidad.** $\operatorname{nul}(A) = \dim\ker A$ = número de variables libres $= n - \operatorname{rg}(A)$.

**Consecuencias.** $\ker A = \{\mathbf{0}\} \iff \operatorname{rg}(A) = n$; si $m < n$, $\operatorname{nul} \ge n - m > 0$.

---

## Guion de narración

### Video 1 — `VariablesLibresDanLaBase`

| En pantalla | Narración |
|---|---|
| Reducida con pivotes 1 y 3 | "Las columnas dos y cuatro no tienen pivote: libres." |
| Despeje y vector | "Ese por un vector, más te por otro." |
| ¿Por qué es base? | "Generan por construcción; son independientes por los unos y ceros." |
| Receta | "Cada libre aporta un vector." |

### Video 2 — `Nulidad`

| En pantalla | Narración |
|---|---|
| $\operatorname{nul} = n - \operatorname{rg}$ | "Cada columna tiene pivote o es libre." |
| Tres ejemplos | "Plano, recta y solo el vector nulo." |
| Consecuencias | "Más incógnitas que ecuaciones: siempre soluciones no triviales." |

---

## Errores frecuentes

- Olvidar una variable libre al escribir la base.
- Escribir mal los signos al despejar.
- Dar como nulidad el rango (o $m - \operatorname{rg}$ en lugar de $n - \operatorname{rg}$).

## Resumen y conexión

Base del núcleo = un vector por libre; nulidad = $n - \operatorname{rg}$. La L47 usa el núcleo para describir todas las soluciones de $A\mathbf{x} = \mathbf{b}$.
