# L41 — Clasificación con ejemplos y árbol de decisión

**Objetivo**: clasificar sistemas variados con los rangos y resumir el criterio en un árbol de decisión.
**Prerrequisitos**: L39–L40.
**Código**: `escenas/l41_clasificacion_con_ejemplos.py`
**Videos**: `videos/l41_clasificacion_con_ejemplos/1080p60/` → `EjemplosClasificados.mp4`, `ArbolDeDecision.mp4`
**Ejercicios**: F11-N2-04, F11-N3-04.

*(Los cuatro ejemplos de $\texttt{EjemplosSCD}$, $\texttt{EjemplosSCI}$ y $\texttt{EjemplosSI}$ del diseño original se reúnen en un solo video, `EjemplosClasificados`.)*

---

## Desarrollo matemático

**Ejemplos.** (1) $x + y + z = 6$, $x - y + z = 2$, $x + y - z = 0$: $\operatorname{rg} = 3 = n$, SCD, $(1, 2, 3)$. (2) Tres ecuaciones con cuatro incógnitas (L32): $\operatorname{rg} = 2 < 4$, SCI con $2$ parámetros. (3) $x + y = 2$, $x - y = 0$, $2x + y = 4$: $\operatorname{rg}(A) = 2 \ne 3$, SI. (4) $x + y + z = 1$, $x + y + z = 3$: $1 \ne 2$, SI.

**Árbol de decisión.** ¿$\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$? No: SI. Sí: ¿$\operatorname{rg}(A) = n$? Sí: SCD; no: SCI con $n - r$ parámetros.

**Atajos.** $m < n$: nunca SCD. $\operatorname{rg}(A) = m$: siempre compatible. Homogéneo: siempre compatible. $m = n$ y $r = n$: SCD para todo $\mathbf{b}$.

---

## Guion de narración

### Video 1 — `EjemplosClasificados`

| En pantalla | Narración |
|---|---|
| Cuatro sistemas | "Determinado con tres rangos tres; indeterminado con dos parámetros; dos incompatibles, uno con más ecuaciones que incógnitas y otro con menos." |
| Lecciones | "Tantas ecuaciones como incógnitas no basta; una ecuación puede sobrar; con más o menos ecuaciones puede ser incompatible." |

### Video 2 — `ArbolDeDecision`

| En pantalla | Narración |
|---|---|
| Árbol | "Primera pregunta: ¿los rangos coinciden? Si no, incompatible. Segunda: ¿el rango es ene? Sí: determinado; no: indeterminado." |
| Atajos | "Menos ecuaciones que incógnitas nunca es determinado; rango eme, siempre compatible; homogéneo, siempre compatible." |

---

## Errores frecuentes

- Clasificar por el número de ecuaciones.
- Concluir SCI sin comprobar la compatibilidad.
- Creer que $m > n$ implica incompatible.

## Resumen y conexión

Dos rangos y $n$ deciden el tipo. La L42 añade parámetros a $A$ y a $\mathbf{b}$.
