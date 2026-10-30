# L12 — Casos especiales y errores frecuentes del Bloque I

**Objetivo**: entender que el número de ecuaciones e incógnitas no basta para clasificar un sistema, y corregir las creencias falsas más comunes.
**Prerrequisitos**: L08–L11.
**Código**: `escenas/l12_casos_especiales.py`
**Videos**: `videos/l12_casos_especiales/1080p60/` → `MasEcuacionesQueIncognitas.mp4`, `MenosEcuacionesQueIncognitas.mp4`, `ErroresFrecuentesBloqueI.mp4`
**Ejercicios**: F03-N4-02, F03-N4-03, F03-N4-04.

---

## Desarrollo matemático

**Más ecuaciones que incógnitas ($m > n$).** Puede ser SCD, SCI o SI. Ejemplo: $x + y = 2$, $x - y = 0$, $2x + y = c$. Las dos primeras dan $(1, 1)$; la tercera se cumple si y solo si $c = 3$. Con $c = 3$: SCD; con $c \neq 3$: SI (las tres rectas se cortan dos a dos formando un triángulo). Método: resolver con algunas ecuaciones y comprobar en las demás.

**Menos ecuaciones que incógnitas ($m < n$).** Puede ser SCI o SI, pero **nunca SCD**. Ejemplo: dos planos se cortan en una recta (SCI), son paralelos (SI) o coinciden (SCI); nunca en un único punto. La justificación general llega con el rango (L40): el número de pivotes es como mucho $m < n$, así que siempre queda alguna incógnita libre si hay solución.

**Seis creencias falsas.**

1. "Tantas ecuaciones como incógnitas ⇒ una solución": $x + y = 1$, $2x + 2y = 2$ tiene infinitas.
2. "Más ecuaciones que incógnitas ⇒ ninguna": el ejemplo anterior con $c = 3$ tiene una.
3. "Menos ecuaciones que incógnitas ⇒ infinitas": $x + y + z = 1$, $x + y + z = 3$ no tiene ninguna.
4. "Si cumple una ecuación, es solución": debe cumplirlas todas.
5. "Llegar a $0 = 0$ significa que no hay solución": $0 = 0$ indica una ecuación que sobraba; lo que indica SI es $0 = c$ con $c \neq 0$.
6. "Un homogéneo puede no tener solución": siempre tiene la trivial.

---

## Guion de narración

### Video 1 — `MasEcuacionesQueIncognitas`

| En pantalla | Narración |
|---|---|
| Tres rectas por $(1, 1)$ | "Tres ecuaciones y dos incógnitas, y aun así hay solución: las tres rectas pasan por el mismo punto." |
| La tercera recta se desplaza; aparece el triángulo | "Si cambiamos el término independiente de la tercera, las rectas se cortan dos a dos, pero ya no hay un punto común. Mismo número de ecuaciones, distinta respuesta." |
| Método | "Para decidir: resolvemos con dos ecuaciones y comprobamos la solución en la tercera." |

### Video 2 — `MenosEcuacionesQueIncognitas`

| En pantalla | Narración |
|---|---|
| Dos planos que se cortan en una recta | "Dos ecuaciones con tres incógnitas: dos planos. Si se cortan, lo hacen en una recta, infinitas soluciones." |
| Dos planos paralelos | "Si son paralelos, ninguna. Lo que nunca puede pasar es que dos planos se corten en un solo punto." |
| Resumen general | "Con menos ecuaciones que incógnitas, el sistema es indeterminado o incompatible, nunca determinado. La prueba completa la daremos con el rango." |

### Video 3 — `ErroresFrecuentesBloqueI`

| En pantalla | Narración |
|---|---|
| Seis tarjetas: creencia y contraejemplo | "Repasemos seis creencias falsas, cada una con un contraejemplo que la desmiente." |
| Moraleja | "Contar ecuaciones e incógnitas no basta para clasificar un sistema. Hace falta analizar las ecuaciones." |

---

## Errores frecuentes

Son el contenido del video 3; además:

- Resolver con dos ecuaciones y olvidar comprobar la tercera.
- Parametrizar con un solo parámetro cuando quedan dos incógnitas libres.

## Resumen y conexión

Con esta lección termina la Unidad 1 (Bloque I). Sabemos qué es un sistema, qué aspecto tienen sus soluciones y por qué solo hay tres casos. En la Unidad 2 aprendemos a resolverlos a mano: sustitución (L13), igualación (L14) y reducción (L15).
