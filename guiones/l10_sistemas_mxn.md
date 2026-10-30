# L10 — Sistemas de m ecuaciones con n incógnitas; sistemas homogéneos

**Objetivo**: leer y escribir un sistema general con doble subíndice, entender qué son los hiperplanos y los límites del dibujo, y conocer las propiedades de los sistemas homogéneos.
**Prerrequisitos**: L04 (subíndices y sumatorio), L07–L09.
**Código**: `escenas/l10_sistemas_mxn.py`
**Videos**: `videos/l10_sistemas_mxn/1080p60/` → `NotacionGeneral.mp4`, `HiperplanosYLimitesDelDibujo.mp4`, `SistemasHomogeneos.mp4`
**Ejercicios**: F03-N1-03, F03-N1-04, F03-N3-02, F03-N2-04, F03-N5-02.

---

## Desarrollo matemático

**Forma general.**
$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ \quad\vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases} \qquad\Longleftrightarrow\qquad \sum_{j=1}^{n} a_{ij}x_j = b_i,\ \ i = 1, \dots, m.$$
$a_{ij}$ es el coeficiente de $x_j$ en la ecuación $i$ (si $x_j$ no aparece, $a_{ij} = 0$). Una *solución* es una lista $(s_1, \dots, s_n)$ que cumple las $m$ ecuaciones. $m$ y $n$ pueden ser distintos.

**Hiperplanos.** Con $n$ incógnitas, una ecuación lineal no degenerada describe un *hiperplano* de $\mathbb{R}^n$: un conjunto con $n - 1$ direcciones libres (punto, recta, plano para $n = 1, 2, 3$). Cada ecuación que aporta información nueva quita una dirección libre; "información nueva" se precisará con el **rango** (L39).

**Límites del dibujo.** Los dibujos dan intuición en 2D y 3D; no existen para $n \ge 4$ y no demuestran nada. Por eso necesitamos métodos algebraicos (Gauss) válidos en cualquier dimensión.

**Sistemas homogéneos.** Todos los $b_i = 0$.

- Siempre tienen la **solución trivial** $(0, \dots, 0)$: nunca son incompatibles.
- Geométricamente, todas sus rectas o planos pasan por el origen.
- Si $u$ y $v$ son soluciones, $u + v$ y $cu$ también lo son: $\sum_j a_{ij}(u_j + v_j) = \sum_j a_{ij}u_j + \sum_j a_{ij}v_j = 0 + 0$. Esto **falla** si algún $b_i \neq 0$.
- Consecuencia: si hay una solución no trivial, hay infinitas (F03-N5-02).

El conjunto de soluciones de un homogéneo será el **núcleo** (L45), y el homogéneo con los mismos coeficientes que un sistema dado, su *homogéneo asociado* (L47).

---

## Guion de narración

### Video 1 — `NotacionGeneral`

| En pantalla | Narración |
|---|---|
| Sistema general con llaves de $m$ y $n$ | "Así se escribe un sistema cualquiera: eme ecuaciones, ene incógnitas. a sub i jota es el coeficiente de la incógnita jota en la ecuación i." |
| Forma con sumatorio | "Con el sumatorio cabe en una línea: para cada ecuación i, la suma de a i jota por equis jota vale be i." |
| Ejemplo $2 \times 3$ y dos candidatos | "En este ejemplo, a uno dos vale dos y be dos vale cero. Uno, uno, menos uno cumple las dos ecuaciones; dos, uno, cero falla la segunda." |

### Video 2 — `HiperplanosYLimitesDelDibujo`

| En pantalla | Narración |
|---|---|
| Cuatro paneles: punto, recta, plano, "?" | "Una ecuación lineal con una incógnita fija un punto; con dos, una recta; con tres, un plano. Con cuatro, un hiperplano que ya no podemos dibujar." |
| Cada ecuación quita libertad | "En el espacio, una ecuación deja un plano; dos, normalmente una recta; tres, normalmente un punto. 'Normalmente' significa: si cada ecuación aporta algo nuevo." |
| Puede / no puede | "Los dibujos dan intuición, pero no sirven en dimensión alta ni demuestran nada." |

### Video 3 — `SistemasHomogeneos`

| En pantalla | Narración |
|---|---|
| Sistema homogéneo y $(0,0,0)$ | "Si todos los términos independientes son cero, poner todas las incógnitas a cero siempre funciona. Un sistema homogéneo nunca es incompatible." |
| Dos paneles con rectas por el origen | "Sus rectas pasan por el origen: o solo se cortan ahí, o coinciden y hay infinitas soluciones." |
| Suma y múltiplos de soluciones | "Y tienen una propiedad especial: la suma de dos soluciones es solución, y cualquier múltiplo también. Si el término independiente no es cero, falla." |

---

## Errores frecuentes

- Confundir $a_{ij}$ con $a_{ji}$; olvidar que una incógnita ausente tiene coeficiente 0.
- Contar las incógnitas de una ecuación en lugar de las del sistema.
- Decir que un homogéneo "no tiene solución".
- Sumar soluciones de un sistema no homogéneo esperando otra solución.

## Resumen y conexión

Ya sabemos escribir cualquier sistema. En la Lección 11 nombramos los tres casos (SCD, SCI, SI) y demostramos que no hay otros.
