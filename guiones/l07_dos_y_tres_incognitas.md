# L07 — Ecuaciones con dos y tres incógnitas: rectas, planos y parámetros

**Objetivo**: entender por qué una ecuación lineal con varias incógnitas tiene infinitas soluciones, dibujarlas (recta o plano) y describirlas con parámetros.
**Prerrequisitos**: L03, L05, L06.
**Código**: `escenas/l07_dos_y_tres_incognitas.py`
**Videos**: `videos/l07_dos_y_tres_incognitas/1080p60/` → `InfinitasSolucionesDeUnaEcuacion.mp4`, `EcuacionComoRecta.mp4`, `EcuacionComoPlano.mp4`, `ParametrizarUnaRecta.mp4`
**Ejercicios**: F02 completo (10 ejercicios).

---

## Desarrollo matemático

**Infinitas soluciones.** En $ax + by = c$ con $a \neq 0$, cada valor de $y$ da exactamente un $x = \frac{c - by}{a}$. Hay tantas soluciones como valores de $y$: infinitas. Si $a = 0$ y $b \neq 0$, al revés ($x$ libre, $y = c/b$). Si $a = b = 0$, es el caso degenerado de L05.

**Rectas.** Si $a, b$ no son ambos 0, las soluciones forman una recta. Para dibujarla bastan dos soluciones, por ejemplo los cortes con los ejes. $b = 0$: recta vertical $x = c/a$; $a = 0$: horizontal $y = c/b$. Dos ecuaciones **proporcionales** (una es $k \neq 0$ veces la otra, incluido el término independiente) describen la misma recta.

**Planos.** Con tres incógnitas, $ax + by + cz = d$ (coeficientes no todos nulos) es un plano: dos incógnitas libres y la tercera despejada. Los cortes con los ejes (anulando dos incógnitas) ayudan a dibujarlo.

**Parámetros.** Un *parámetro* es un nombre para el valor libre: $x + 2y = 4$ tiene las soluciones $(x, y) = (4 - 2t, t)$, $t \in \mathbb{R}$. Esta *parametrización* da **todas** las soluciones y **solo** ellas (demostración: F02-N5-01). No es única: $(s, \frac{4 - s}{2})$ describe el mismo conjunto.

Una ecuación lineal no degenerada con $n$ incógnitas necesita $n - 1$ parámetros: recta ($n = 2$), plano ($n = 3$), hiperplano ($n \ge 4$, L10).

---

## Guion de narración

### Video 1 — `InfinitasSolucionesDeUnaEcuacion`

| En pantalla | Narración |
|---|---|
| Tabla $y \to x = 4 - 2y$ y puntos | "Elegimos ye cero: equis vale cuatro. Ye uno: equis dos. Ye un medio: equis tres. Cada valor de ye da un único equis, así que hay infinitas soluciones." |
| Muchos puntos y la recta | "Todas juntas forman una recta." |
| Caso general | "Siempre que a o be no sean cero, podemos elegir una incógnita libremente y despejar la otra. Una sola ecuación con dos incógnitas nunca fija un único punto: para eso harán falta más ecuaciones, es decir, un sistema." |

### Video 2 — `EcuacionComoRecta`

| En pantalla | Narración |
|---|---|
| Cortes $(0, 4)$ y $(2, 0)$ | "Para dibujar dos equis más ye igual a cuatro, buscamos dónde corta a los ejes: con equis cero, ye vale cuatro; con ye cero, equis vale dos. Dos puntos determinan la recta." |
| $x = 2$ e $y = 2$ | "Si falta una incógnita, esa incógnita es libre: dos equis igual a cuatro es la recta vertical equis igual a dos." |
| $2x + y = 4$ y $4x + 2y = 8$ superpuestas | "Multiplicar toda la ecuación por dos no cambia sus soluciones: es la misma recta escrita de otra forma." |

### Video 3 — `EcuacionComoPlano`

| En pantalla | Narración |
|---|---|
| Ejes 3D, tres cortes, triángulo y plano | "Con tres incógnitas, anulamos dos para encontrar cada corte con los ejes. Los tres puntos determinan un plano; el triángulo es solo un trozo de él. El punto uno, uno, uno también está: uno más dos más uno, cuatro." |
| $x = 4 - 2y - z$ | "Ahora hay dos incógnitas libres. Dos libres, un plano; una libre, una recta." |

### Video 4 — `ParametrizarUnaRecta`

| En pantalla | Narración |
|---|---|
| El punto $(4 - 2t, t)$ recorre la recta | "Llamemos te al valor libre de ye. Entonces equis vale cuatro menos dos te. Al mover te, el punto recorre toda la recta: cada te da un punto y cada punto viene de algún te." |
| Dos parametrizaciones | "Podríamos haber llamado ese al valor de equis: otra fórmula, el mismo conjunto." |
| Plano con dos parámetros | "Para un plano hacen falta dos parámetros. En general, ene incógnitas y una ecuación: ene menos uno parámetros." |

---

## Errores frecuentes

- Despejar con el signo cambiado ($y = 6 - 3x$ en vez de $3x - 6$).
- Confundir recta vertical y horizontal.
- Comparar solo los coeficientes al decidir si dos ecuaciones son la misma recta.
- Parametrizar un plano con un solo parámetro.
- No comprobar una parametrización sustituyéndola.

## Resumen y conexión

Una ecuación con varias incógnitas tiene infinitas soluciones (recta, plano…), descritas con parámetros. En la Lección 8 juntamos dos ecuaciones: el sistema pide los puntos comunes de dos rectas.
