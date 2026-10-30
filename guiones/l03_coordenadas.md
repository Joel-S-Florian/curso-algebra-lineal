# L03 — Coordenadas: la recta, el plano y el espacio

**Objetivo**: ubicar puntos con pares y ternas ordenadas, entender la gráfica de una ecuación como el conjunto de sus soluciones, y manejar la pendiente y la forma general $ax + by = c$ de una recta.
**Prerrequisitos**: L01, L02.
**Código**: `escenas/l03_coordenadas.py`
**Videos**: `videos/l03_coordenadas/1080p60/` → `ParesOrdenados.mp4`, `GraficaComoConjuntoDePuntos.mp4`, `PendienteDeUnaRecta.mp4`, `EspacioTresCoordenadas.mp4`
**Ejercicios**: F00-N1-07, F00-N2-05, F00-N2-06, F00-N3-03, F00-N4-03, F00-N5-03.

---

## Desarrollo matemático

**Plano cartesiano.** Dos rectas numéricas perpendiculares que se cortan en el 0 (el *origen*). Un punto se describe con un *par ordenado* $(x, y)$: $x$ es el desplazamiento horizontal desde el origen, $y$ el vertical. El orden importa: $(3, 2) \neq (2, 3)$. Los ejes dividen el plano en cuatro cuadrantes según los signos: I $(+,+)$, II $(-,+)$, III $(-,-)$, IV $(+,-)$. $\mathbb{R}^2$ es el conjunto de todos los pares de números reales.

**Gráfica de una ecuación.** Es el conjunto de **todos** los puntos cuyas coordenadas cumplen la ecuación. Un punto está en la gráfica si y solo si sus coordenadas la cumplen (se comprueba sustituyendo). La gráfica de $x + y = 3$ es una recta; la de $y = x^2$ es una curva (parábola).

**Pendiente.** En $y = mx + n$:

- $n$ es la *ordenada en el origen*: el valor de $y$ cuando $x = 0$.
- $m$ es la *pendiente*: lo que sube $y$ cuando $x$ aumenta 1. Si $m > 0$ la recta sube; si $m = 0$ es horizontal; si $m < 0$ baja.
- Con dos puntos $(x_1, y_1)$, $(x_2, y_2)$ y $x_1 \neq x_2$: $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.

Las rectas verticales ($x_1 = x_2$) no tienen pendiente (habría que dividir entre 0) y no se pueden escribir como $y = mx + n$. Por eso usaremos la **forma general** $ax + by = c$ (con $a$ y $b$ no ambos 0), que describe **todas** las rectas: $x = 2$ es $1\cdot x + 0 \cdot y = 2$. Si $b \neq 0$ se despeja $y = -\frac{a}{b}x + \frac{c}{b}$.

Dos rectas con la misma pendiente y distinta ordenada en el origen son *paralelas*: no se cortan. (En la Lección 8 veremos que esto corresponde a un sistema sin solución).

**Espacio.** Tres ejes perpendiculares; un punto es una *terna* $(x, y, z)$; el conjunto de todas es $\mathbb{R}^3$. La gráfica de una ecuación lineal con tres incógnitas, como $x + y + z = 3$, es un plano. Con $n$ incógnitas una solución es una lista de $n$ números, un elemento de $\mathbb{R}^n$: no se puede dibujar si $n > 3$, pero el álgebra funciona igual.

**Limitación de los dibujos.** Las imágenes en 2D y 3D sirven para la intuición. No demuestran nada y no existen para $n \geq 4$; por eso el curso siempre acompaña la geometría con álgebra.

---

## Guion de narración

### Video 1 — `ParesOrdenados`

| En pantalla | Narración |
|---|---|
| Una recta numérica gira y forma una cruz; aparece la cuadrícula | "Una recta numérica sirve para ubicar un número. Si cruzamos dos rectas perpendiculares en el cero, podemos ubicar cualquier punto del plano." |
| El punto viaja 3 a la derecha y 2 arriba | "Para llegar al punto tres coma dos, avanzamos tres en horizontal y subimos dos. La primera coordenada siempre es la horizontal, x; la segunda, la vertical, y." |
| Aparece $(2, 3)$ en otro sitio | "Dos coma tres es otro punto. Por eso hablamos de pares ordenados: el orden importa." |
| Puntos con coordenadas negativas y cuadrantes | "Los números negativos significan ir a la izquierda o hacia abajo. Los ejes dividen el plano en cuatro cuadrantes, según los signos de las coordenadas." |
| $\mathbb{R}^2$ y la conexión con ecuaciones | "Al conjunto de todos los pares de números reales lo llamamos erre dos. La idea clave: una solución de una ecuación con dos incógnitas es un par, es decir, un punto del plano." |

### Video 2 — `GraficaComoConjuntoDePuntos`

| En pantalla | Narración |
|---|---|
| Se prueban seis puntos en $x + y = 3$ | "¿Qué puntos cumplen x más y igual a tres? Probemos. Uno coma dos: sí. Cero coma tres: sí. Dos coma dos: no, suma cuatro. Cuatro coma menos uno: sí..." |
| Muchos puntos verdes y la recta | "Si dibujamos muchísimos puntos que la cumplen, aparece una recta. La gráfica de una ecuación es el conjunto de todos los puntos que la cumplen." |
| $y = x^2$ | "No toda ecuación da una recta: y igual a equis al cuadrado da una curva. Las ecuaciones cuyas gráficas son rectas, o planos, son las ecuaciones lineales, protagonistas del curso." |

### Video 3 — `PendienteDeUnaRecta`

| En pantalla | Narración |
|---|---|
| La recta $y = mx + n$ cambia con $n$ | "En y igual a eme equis más ene, el número ene es la altura a la que la recta corta al eje vertical. Si cambiamos ene, la recta se desplaza sin girar." |
| El escalón 1 / $m$; la recta gira | "El número eme dice cuánto sube la recta cuando avanzamos una unidad a la derecha. Es la pendiente. Con eme positiva sube, con eme cero es horizontal, con eme negativa baja." |
| Dos puntos y la fórmula de la pendiente | "Si conocemos dos puntos, la pendiente es lo que sube dividido entre lo que avanza. Luego, sustituyendo un punto, obtenemos ene." |
| Recta vertical, $4/0$ | "Una recta vertical no avanza: tendríamos que dividir entre cero. No tiene pendiente y no se puede escribir como y igual a eme equis más ene. Pero sí como uno por equis más cero por y igual a dos. La forma a equis más be ye igual a ce sirve para todas las rectas, y será la que usemos en los sistemas." |
| Dos rectas paralelas | "Dos rectas con la misma pendiente y distinta altura nunca se cortan. Recuérdalo: en la lección 8 descubriremos que eso significa un sistema sin solución." |

### Video 4 — `EspacioTresCoordenadas`

| En pantalla | Narración |
|---|---|
| Ejes 3D; el punto $(2, 1, 3)$ se alcanza en tres tramos | "En el espacio necesitamos tres números. Para llegar al punto dos, uno, tres avanzamos dos en la dirección x, uno en la dirección y, y subimos tres." |
| Triángulo azul del plano $x + y + z = 3$; la cámara gira | "Las soluciones de x más y más z igual a tres forman un plano. Dibujamos solo el trozo que cae en la zona positiva; el plano real es infinito. El punto uno, uno, uno está en él porque uno más uno más uno es tres." |
| $(x_1, x_2, x_3, x_4) \in \mathbb{R}^4$ | "¿Y con cuatro incógnitas? Una solución es una lista de cuatro números. No podemos dibujarla, pero el álgebra funciona exactamente igual. Los dibujos nos ayudan a entender; no son demostraciones." |

---

## Errores frecuentes de la lección

- Intercambiar las coordenadas: ubicar $(3, 2)$ en $(2, 3)$.
- Creer que una recta vertical tiene pendiente 0 (la horizontal tiene pendiente 0; la vertical no tiene).
- Calcular la pendiente restando en órdenes distintos arriba y abajo: $\frac{y_2 - y_1}{x_1 - x_2}$.
- Pensar que un dibujo en 3D demuestra un resultado general.

## Resumen y conexión

Cada solución de una ecuación con dos incógnitas es un punto del plano; con tres, un punto del espacio. Resolver un sistema de dos ecuaciones lineales con dos incógnitas será, geométricamente, buscar los puntos comunes de dos rectas (Lección 8).
