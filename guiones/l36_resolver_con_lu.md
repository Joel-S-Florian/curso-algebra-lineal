# L36 — Resolver con LU

**Objetivo**: resolver $A\mathbf{x} = \mathbf{b}$ con $A = LU$ mediante dos sustituciones.
**Prerrequisitos**: L34 (triangulares), L35 (de dónde sale $L$).
**Código**: `escenas/l36_resolver_con_lu.py`
**Videos**: `videos/l36_resolver_con_lu/1080p60/` → `SustitucionHaciaAdelanteLy.mp4`, `SustitucionHaciaAtrasUx.mp4`, `EjemploCompletoLU.mp4`
**Ejercicios**: F10-N2-04, F10-N3-03, F10-N3-06, F10-N4-02.

---

## Desarrollo matemático

**Método.** $A\mathbf{x} = \mathbf{b} \iff L(U\mathbf{x}) = \mathbf{b}$. Con $\mathbf{y} = U\mathbf{x}$: (1) $L\mathbf{y} = \mathbf{b}$ hacia adelante; (2) $U\mathbf{x} = \mathbf{y}$ hacia atrás; (3) verificar en $A\mathbf{x} = \mathbf{b}$.

**Significado de $\mathbf{y}$.** $\mathbf{y} = L^{-1}\mathbf{b} = E_{32}E_{31}E_{21}\mathbf{b}$: es $\mathbf{b}$ después de la eliminación (la última columna de la aumentada escalonada). Ejemplo: $\mathbf{b} = (-3, 1, 2) \Rightarrow \mathbf{y} = (-3, 7, 20) \Rightarrow \mathbf{x} = (1, -1, 2)$.

**Coste** (multiplicaciones y divisiones, sistema $n \times n$): $L\mathbf{y} = \mathbf{b}$, $\frac{n(n-1)}{2}$; $U\mathbf{x} = \mathbf{y}$, $\frac{n(n+1)}{2}$; total $n^2$ por cada $\mathbf{b}$. Factorizar $A$: $\frac{n^3 - n}{3}$, una sola vez ($n = 3$: $8 + 9 = 17$, igual que Gauss).

**Ejemplo completo.** $A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & -6 & 0 \\ -2 & 7 & 2 \end{bmatrix}$, $\mathbf{b} = (5, -2, 9)$: $L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & -1 & 1 \end{bmatrix}$, $U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & -8 & -2 \\ 0 & 0 & 1 \end{bmatrix}$, $\mathbf{y} = (5, -12, 2)$, $\mathbf{x} = (1, 1, 2)$.

---

## Guion de narración

### Video 1 — `SustitucionHaciaAdelanteLy`

| En pantalla | Narración |
|---|---|
| $A\mathbf{x} = \mathbf{b} \to L\mathbf{y} = \mathbf{b},\ U\mathbf{x} = \mathbf{y}$ | "Llamamos ye al producto u por equis, y el problema se parte en dos sistemas triangulares." |
| $L\mathbf{y} = \mathbf{b}$ | "Hacia adelante: ye uno menos tres, ye dos siete, ye tres veinte." |
| ¿Qué es $\mathbf{y}$? | "Es be después de la eliminación: la última columna de la aumentada escalonada." |

### Video 2 — `SustitucionHaciaAtrasUx`

| En pantalla | Narración |
|---|---|
| $U\mathbf{x} = \mathbf{y}$ | "Hacia atrás: zeta dos, ye menos uno, equis uno." |
| Verificación | "A por la solución da be: es la solución que dio Gauss en la lección veintiséis." |
| Costes | "Ene cuadrado por cada be; factorizar, ene cubo menos ene entre tres, una sola vez." |

### Video 3 — `EjemploCompletoLU`

| En pantalla | Narración |
|---|---|
| Factorizar | "Multiplicadores dos, menos uno y menos uno; u con dos, menos ocho y uno en la diagonal." |
| $L\mathbf{y} = \mathbf{b}$, $U\mathbf{x} = \mathbf{y}$ | "Ye es cinco, menos doce, dos; la solución, uno, uno, dos." |
| Verificar | "Cinco, menos dos, nueve: correcto." |

---

## Errores frecuentes

- Resolver $U\mathbf{x}$ con $\mathbf{b}$ en lugar de con $\mathbf{y}$.
- Verificar en $U\mathbf{x} = \mathbf{y}$ en vez de en $A\mathbf{x} = \mathbf{b}$.
- Contar la columna $\mathbf{b}$ dentro del coste de factorizar.

## Resumen y conexión

Factorizar una vez, resolver con dos sustituciones y verificar. Si $A$ obliga a intercambiar filas, la L37 explica $PA = LU$.
