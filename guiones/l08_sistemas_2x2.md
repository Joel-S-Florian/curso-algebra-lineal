# L08 — Sistemas de dos ecuaciones con dos incógnitas

**Objetivo**: entender qué es un sistema y qué es su solución, e interpretar geométricamente los tres casos (rectas que se cortan, paralelas, coincidentes).
**Prerrequisitos**: L04 (intersección de conjuntos), L07.
**Código**: `escenas/l08_sistemas_2x2.py`
**Videos**: `videos/l08_sistemas_2x2/1080p60/` → `QueEsUnSistema.mp4`, `RectasQueSeCortan.mp4`, `RectasParalelas.mp4`, `RectasCoincidentes.mp4`
**Ejercicios**: F03-N1-01, F03-N2-01, F03-N2-02, F03-N3-01, F03-N2-05, F03-N3-04.

---

## Desarrollo matemático

**Sistema y solución.** Un *sistema* es un conjunto de ecuaciones que deben cumplirse **simultáneamente**. Una *solución* asigna un valor a cada incógnita de modo que **todas** las ecuaciones se cumplen. El conjunto solución es la **intersección** de los conjuntos solución de cada ecuación (L04).

**Geometría 2×2.** Cada ecuación $a_ix + b_iy = c_i$ (con $a_i, b_i$ no ambos 0) es una recta. Dos rectas del plano solo pueden:

| Posición | Soluciones | Criterio con los coeficientes |
|---|---|---|
| Se cortan | una | $(a_1, b_1)$ y $(a_2, b_2)$ **no** proporcionales |
| Paralelas distintas | ninguna | $(a_2, b_2) = k(a_1, b_1)$ pero $c_2 \neq k c_1$ |
| Coincidentes | infinitas | $(a_2, b_2, c_2) = k(a_1, b_1, c_1)$ |

($k \neq 0$.) "No proporcionales" equivale a "pendientes distintas" cuando las rectas no son verticales, y el criterio también vale para verticales.

**Detección algebraica.** En el caso paralelo, combinar ecuaciones lleva a una igualdad falsa ($5 = 2$): el sistema es contradictorio. En el caso coincidente, una ecuación es redundante: las soluciones llevan un parámetro, como $(5 - t, t)$.

Nunca hay exactamente dos soluciones: dos rectas distintas se cortan como mucho en un punto (la prueba general, en L11).

---

## Guion de narración

### Video 1 — `QueEsUnSistema`

| En pantalla | Narración |
|---|---|
| Problema y sistema $x + y = 5$, $x - y = 1$ | "Dos números suman cinco y su diferencia es uno. Son dos condiciones que deben cumplirse a la vez: eso es un sistema." |
| Tabla de candidatos | "Cuatro uno cumple la primera, pero no la segunda: no es solución del sistema. Dos tres tampoco. Tres dos cumple las dos: esa es la solución." |
| Dos rectas y el punto $(3, 2)$ | "Cada ecuación es una recta; el sistema pide estar en las dos. La solución es su punto común, la intersección. Cómo encontrarlo sin probar ni dibujar lo veremos en las lecciones trece a quince." |

### Video 2 — `RectasQueSeCortan`

| En pantalla | Narración |
|---|---|
| Rectas de pendientes $2$ y $-\frac13$ | "Dos rectas con pendientes distintas se cortan exactamente en un punto. Aquí, en dos tres; lo verificamos en las dos ecuaciones." |
| La segunda recta gira alrededor del punto | "Aunque giremos la segunda recta, mientras no tenga la misma pendiente que la primera, el corte es único." |
| Criterio de proporcionalidad | "Sin dibujar: si los pares de coeficientes no son proporcionales, las rectas se cortan en un único punto." |

### Video 3 — `RectasParalelas`

| En pantalla | Narración |
|---|---|
| $x + y = 5$ y $2x + 2y = 4$ | "Estas rectas son paralelas: nunca se cortan. Algebraicamente, dividiendo la segunda entre dos, queda equis más ye igual a dos. Pero el mismo número no puede valer cinco y dos a la vez: contradicción, ninguna solución." |
| Criterio | "Coeficientes proporcionales y términos independientes no: sistema sin solución." |

### Video 4 — `RectasCoincidentes`

| En pantalla | Narración |
|---|---|
| $x + y = 5$ y $2x + 2y = 10$ superpuestas | "Aquí la segunda ecuación es la primera multiplicada por dos: no añade nada, es redundante. Todos los puntos de la recta son solución, cinco menos te coma te." |
| Los tres casos en paralelo | "Se cortan: una solución. Paralelas: ninguna. Coincidentes: infinitas. Nunca exactamente dos." |

---

## Errores frecuentes

- Aceptar un punto que solo cumple una de las ecuaciones.
- Comparar coeficientes sin mirar los términos independientes (confundir paralelas con coincidentes).
- Fiarse de un dibujo impreciso sin verificar.

## Resumen y conexión

Un sistema 2×2 tiene una, ninguna o infinitas soluciones según sus rectas se corten, sean paralelas o coincidan. En la Lección 9 pasamos a tres ecuaciones con tres incógnitas: tres planos.
