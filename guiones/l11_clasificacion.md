# L11 — Clasificación de sistemas: ¿por qué 0, 1 o infinitas soluciones?

**Objetivo**: clasificar sistemas (SCD, SCI, SI) y demostrar que un sistema lineal nunca tiene un número finito de soluciones mayor que 1.
**Prerrequisitos**: L04 (demostraciones), L08–L10.
**Código**: `escenas/l11_clasificacion.py`
**Videos**: `videos/l11_clasificacion/1080p60/` → `ClasificacionDeSistemas.mp4`, `NuncaExactamenteDos.mp4`
**Ejercicios**: F03-N3-03, F03-N5-01.

---

## Desarrollo matemático

**Clasificación.**

- **Compatible**: tiene al menos una solución.
  - **Compatible determinado (SCD)**: exactamente una.
  - **Compatible indeterminado (SCI)**: infinitas.
- **Incompatible (SI)**: ninguna.

**Teorema.** Un sistema lineal tiene ninguna, una o infinitas soluciones.

*Demostración.* Basta ver que si tiene dos soluciones distintas $p \neq q$, tiene infinitas. Para cada $t \in \mathbb{R}$ sea $r = (1 - t)p + tq$ (componente a componente). Para cada ecuación $i$:
$$\sum_j a_{ij}r_j = (1 - t)\sum_j a_{ij}p_j + t\sum_j a_{ij}q_j = (1 - t)b_i + t b_i = b_i.$$
Así $r$ es solución para todo $t$. Si $t \neq s$, $r(t) - r(s) = (t - s)(q - p) \neq 0$, luego son soluciones distintas: una por cada número real. $\blacksquare$

*Dónde se usa la linealidad*: al sacar $(1 - t)$ y $t$ fuera de la suma. Con $x^2 = 1$ (no lineal) hay exactamente dos soluciones, $\pm 1$, y el punto medio $0$ no es solución.

*Geometría*: los puntos $r(t)$ forman la recta que pasa por $p$ y $q$; el teorema dice que si un sistema lineal contiene dos puntos, contiene la recta entera que los une.

**Cómo se reconoce cada caso (por ahora)**: SCD si hay un único punto común; SCI si hay ecuaciones redundantes y parámetros; SI si combinando ecuaciones se llega a una igualdad falsa. En la Unidad 7 se clasificará sin resolver, con el rango.

---

## Guion de narración

### Video 1 — `ClasificacionDeSistemas`

| En pantalla | Narración |
|---|---|
| Árbol de clasificación | "Primera pregunta: ¿tiene solución? Si no, el sistema es incompatible. Si sí, es compatible, y hay una segunda pregunta: ¿cuántas? Una, y es determinado; infinitas, y es indeterminado." |
| Ejemplos bajo cada caja | "Son los tres casos de rectas de la lección ocho: se cortan, coinciden o son paralelas." |
| Criterios provisionales | "Por ahora los reconocemos combinando ecuaciones. En la unidad siete aprenderemos a clasificar sin resolver, con el rango." |

### Video 2 — `NuncaExactamenteDos`

| En pantalla | Narración |
|---|---|
| $p$, $q$ y el punto $r(t)$ moviéndose | "Supongamos que un sistema tiene dos soluciones, pe y cu. Construimos erre de te: con te cero es pe, con te uno es cu, y con cualquier otro te, otro punto de la recta que los une. Todos son soluciones." |
| Demostración | "¿Por qué? Sustituimos erre en la ecuación i. Como las incógnitas aparecen de forma lineal, podemos sacar uno menos te y te fuera de las sumas, y queda be i. Además, valores distintos de te dan puntos distintos. Hay infinitas soluciones." |
| Contraejemplo $x^2 = 1$ | "Si la ecuación no es lineal, el argumento falla: equis al cuadrado igual a uno tiene exactamente dos soluciones, y el punto medio, cero, no es solución." |

---

## Errores frecuentes

- Pensar que "más de una" puede significar "dos o tres".
- Llamar incompatible a un sistema con menos ecuaciones que incógnitas sin comprobarlo.
- Olvidar que un homogéneo nunca es SI.
- En la demostración, olvidar probar que las soluciones obtenidas son distintas.

## Resumen y conexión

Solo hay tres casos: SCD, SCI o SI. En la Lección 12 vemos casos especiales que suelen confundirse y los errores más frecuentes del Bloque I.
