# L06 — Ecuaciones lineales con una incógnita: $ax = b$

**Objetivo**: resolver cualquier ecuación lineal con una incógnita justificando cada paso, y dominar los tres casos posibles.
**Prerrequisitos**: L02 (reglas 1 y 2), L05.
**Código**: `escenas/l06_una_incognita.py`
**Videos**: `videos/l06_una_incognita/1080p60/` → `DespejeJustificado.mp4`, `LosTresCasos.mp4`
**Ejercicios**: F01-N1-04, F01-N2-01 a N2-03, F01-N3-01, F01-N3-02, F01-N4-02, F01-N4-03, F01-N5-01.

---

## Desarrollo matemático

**Receta.** Toda ecuación lineal con una incógnita se lleva a la forma $ax = b$:

1. Quitar paréntesis (distributiva) y denominadores (multiplicar ambos lados por un número no nulo, normalmente un múltiplo común de los denominadores).
2. Pasar los términos con $x$ a un lado y los números al otro (regla 1).
3. Agrupar: $ax = b$.
4. Si $a \neq 0$, dividir entre $a$ (regla 2): $x = \frac ba$.
5. Verificar en la ecuación **original**.

Cada paso es reversible, así que todas las ecuaciones de la cadena son equivalentes.

**Los tres casos de $ax = b$.**

| Condición | Conjunto solución | Tipo |
|---|---|---|
| $a \neq 0$ | $\{b/a\}$ | una solución |
| $a = 0$, $b = 0$ | $\mathbb{R}$ | infinitas |
| $a = 0$, $b \neq 0$ | $\varnothing$ | ninguna |

*Justificación* (ejercicio F01-N5-01): si $a \neq 0$, $x = \frac ba$ cumple la ecuación y, si $ax_1 = ax_2 = b$, restando $a(x_1 - x_2) = 0$ y multiplicando por $\frac1a$, $x_1 = x_2$. Si $a = 0$, la ecuación dice $0 = b$, que no depende de $x$.

**Interpretación geométrica.** Las soluciones son los $x$ donde la recta $y = ax$ alcanza la altura $b$ (la recta horizontal $y = b$). Si $a \neq 0$, la recta inclinada corta a la horizontal en un punto; si $a = 0$, la "recta inclinada" es el eje $x$: paralela a $y = b$ (ningún corte) o igual a ella si $b = 0$ (todos).

**Parámetros.** En $(m - 2)x = m - 2$ no se puede dividir entre $m - 2$ sin separar el caso $m = 2$. *Discutir* una ecuación es estudiar por separado los valores del parámetro que anulan el coeficiente.

---

## Guion de narración

### Video 1 — `DespejeJustificado`

| En pantalla | Narración |
|---|---|
| $3x + 4 = 10 \to 3x = 6 \to x = 2$ con la regla de cada paso | "Restamos cuatro en ambos lados: regla uno. Dividimos entre tres, que no es cero: regla dos. Cada paso se puede deshacer, así que la ecuación final tiene las mismas soluciones que la inicial. Y verificamos: tres por dos más cuatro, diez." |
| Receta en cinco pasos | "Esta es la receta para cualquier ecuación lineal con una incógnita. Fíjate en el paso cuatro: solo se puede dividir entre a si a no es cero." |
| Ejemplo con fracciones | "Con fracciones, multiplicamos ambos lados por seis, que es múltiplo de tres y de dos: desaparecen todos los denominadores." |
| Ejemplo con paréntesis | "Con paréntesis, cuidado con los signos: el menos dos multiplica a equis y a menos tres, y menos dos por menos tres es más seis." |

### Video 2 — `LosTresCasos`

| En pantalla | Narración |
|---|---|
| Recta $y = ax$, horizontal $y = b$ y el punto de corte | "Resolver a equis igual a be es buscar dónde la recta y igual a a equis alcanza la altura be. Mientras la recta esté inclinada, la corta exactamente una vez." |
| $a \to 0$ | "Pero si a vale cero, la recta y igual a cero por equis es el eje horizontal. Si be es uno, nunca se cortan: ninguna solución. Si be también es cero, coinciden: todos los equis son solución." |
| Tabla de los tres casos | "Una, infinitas o ninguna. Son exactamente los mismos tres casos que tendrán los sistemas de ecuaciones." |
| $(m - 2)x = m - 2$ | "Cuando el coeficiente depende de un parámetro, hay que separar casos: si eme no es dos, se divide y equis vale uno; si eme es dos, queda cero igual a cero y todo equis es solución. Dividir sin separar ese caso es el error más común." |

---

## Errores frecuentes

- Dividir entre una expresión que puede valer 0.
- Interpretar "$x = 0$" como "no hay solución".
- Concluir algo de una igualdad falsa como $-3 = -2$ (indica que no hay solución).
- Aplicar la distributiva sin repartir el signo.
- No verificar.

## Resumen y conexión

$ax = b$ tiene una solución si $a \neq 0$, y si $a = 0$, infinitas o ninguna según $b$. En la Lección 7 añadimos una segunda incógnita: aparecen las rectas y los parámetros.
