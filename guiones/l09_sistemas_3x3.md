# L09 — Sistemas de tres ecuaciones con tres incógnitas: tres planos

**Objetivo**: interpretar un sistema 3×3 como tres planos y reconocer las configuraciones con una, infinitas o ninguna solución.
**Prerrequisitos**: L07 (planos), L08.
**Código**: `escenas/l09_sistemas_3x3.py`
**Videos**: `videos/l09_sistemas_3x3/1080p60/` → `TresPlanosUnPunto.mp4`, `TresPlanosUnaRecta.mp4`, `TresPlanosSinPuntoComun.mp4`
**Ejercicios**: F03-N1-02, F03-N2-03, F03-N4-01.

---

## Desarrollo matemático

Cada ecuación $a_ix + b_iy + c_iz = d_i$ (coeficientes no todos nulos) es un plano de $\mathbb{R}^3$. Las soluciones del sistema son los puntos comunes a los tres.

**Configuraciones.**

| Soluciones | Configuraciones posibles |
|---|---|
| Una (SCD) | Dos planos se cortan en una recta y el tercero corta esa recta en un punto. |
| Infinitas (SCI) | Los tres pasan por una misma recta ("libro abierto"), o dos coinciden y el tercero los corta, o los tres coinciden (un plano de soluciones). |
| Ninguna (SI) | Se cortan dos a dos en tres rectas paralelas ("prisma"); dos paralelos y el tercero los corta; tres paralelos; dos iguales y uno paralelo. |

**Ejemplos de la lección.**

- $x + y + z = 6$, $x - y + z = 2$, $x + y - z = 0$: solución única $(1, 2, 3)$.
- $x + y + z = 3$, $x - y + z = 1$, $x + z = 2$: la tercera es la semisuma de las dos primeras (redundante); soluciones $(2 - t, 1, t)$.
- $x + y + z = 3$, $x - y + z = 1$, $x + z = 3$: sumando las dos primeras, $x + z = 2$, que contradice la tercera ($2 = 3$). Ningún plano es paralelo a otro, y aun así no hay solución.

**Límites del dibujo.** En 3D es difícil leer intersecciones con exactitud: el dibujo sugiere el tipo de sistema, las cuentas lo deciden y la verificación lo confirma.

---

## Guion de narración

### Video 1 — `TresPlanosUnPunto`

| En pantalla | Narración |
|---|---|
| Dos planos y su recta de corte | "Cada ecuación con tres incógnitas es un plano. Dos planos que no son paralelos se cortan en una recta." |
| Tercer plano y el punto $(1, 2, 3)$ | "El tercer plano atraviesa esa recta en un único punto: uno, dos, tres. Es la única solución, y la verificamos en las tres ecuaciones." |
| Rotación; límites del dibujo | "Girando la cámara se entiende mejor, pero leer coordenadas exactas en un dibujo 3D es casi imposible. Para eso están los métodos algebraicos." |

### Video 2 — `TresPlanosUnaRecta`

| En pantalla | Narración |
|---|---|
| Tres planos con una recta común | "Ahora los tres planos comparten la misma recta, como las páginas de un libro abierto. Todos sus puntos son solución: infinitas, con un parámetro." |
| Suma de las dos primeras ecuaciones | "¿Por qué? Sumando las dos primeras y dividiendo entre dos obtenemos la tercera. La tercera no aporta información nueva: es redundante." |

### Video 3 — `TresPlanosSinPuntoComun`

| En pantalla | Narración |
|---|---|
| Tres planos y tres rectas paralelas | "Estos tres planos se cortan de dos en dos, pero las tres rectas de corte son paralelas: forman un prisma y no hay ningún punto común." |
| Cuenta que lleva a $2 = 3$ | "Las cuentas lo confirman: de las dos primeras se deduce equis más zeta igual a dos, y la tercera exige tres. Contradicción." |
| Lista de configuraciones | "En el espacio, no tener solución no exige que haya planos paralelos." |

---

## Errores frecuentes

- Creer que un sistema 3×3 sin planos paralelos siempre tiene solución.
- Verificar una terna solo en una o dos ecuaciones.
- Fiarse de la lectura de un dibujo 3D.

## Resumen y conexión

Con tres incógnitas siguen existiendo exactamente tres posibilidades: una, infinitas o ninguna solución. En la Lección 10 generalizamos a cualquier número de ecuaciones e incógnitas.
