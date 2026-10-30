# L13 — El método de sustitución

**Objetivo**: resolver sistemas por sustitución, justificar por qué el sistema obtenido es equivalente e interpretar los casos en que la incógnita desaparece.
**Prerrequisitos**: L02, L06, L08, L11.
**Código**: `escenas/l13_sustitucion.py`
**Videos**: `videos/l13_sustitucion/1080p60/` → `SustitucionPasoAPaso.mp4`, `SustitucionCuandoConviene.mp4`, `SustitucionCasosEspeciales.mp4`
**Ejercicios**: F04-N1-01, N1-02, N2-01, N3-01, N4-03, N4-04, N5-01.

---

## Desarrollo matemático

**Método.**

1. Despejar una incógnita en una ecuación (preferiblemente una con coeficiente $\pm 1$).
2. Sustituir esa expresión, **entre paréntesis**, en la **otra** ecuación.
3. Resolver la ecuación resultante, que tiene una incógnita menos.
4. Volver al despeje para calcular la incógnita eliminada.
5. Verificar en las ecuaciones **originales**.

Ejemplo: $3x + y = 11$, $x - 2y = -1$. $y = 11 - 3x$; $x - 2(11 - 3x) = -1 \Rightarrow 7x = 21 \Rightarrow x = 3$; $y = 2$.

**Justificación.** $\{3x + y = 11,\ x - 2y = -1\} \Leftrightarrow \{y = 11 - 3x,\ x - 2(11 - 3x) = -1\}$: el despeje usa reglas reversibles y, si $y = 11 - 3x$, escribir una expresión en lugar de la otra no cambia nada (prueba general: F04-N5-01).

**Geometría.** Con $y = 11 - 3x$ recorremos la primera recta; la segunda ecuación selecciona el punto de esa recta que también está en la otra.

**Casos especiales.** La ecuación final $ay = b$ decide:

| Ecuación final | Sistema |
|---|---|
| $a \neq 0$ | SCD |
| $0y = 0$ | SCI (la incógnita que queda es libre: parámetro) |
| $0y = b$, $b \neq 0$ | SI |

**Cuándo conviene.** Si alguna incógnita tiene coeficiente $\pm 1$. Si no, funciona con fracciones. Con tres o más incógnitas, las expresiones crecen rápidamente.

---

## Guion de narración

### Video 1 — `SustitucionPasoAPaso`

| En pantalla | Narración |
|---|---|
| Sistema $3x + y = 11$, $x - 2y = -1$ | "Ya sabemos resolver ecuaciones con una incógnita. La idea de la sustitución es convertir el sistema en una de ellas." |
| Pasos 1 a 5 numerados | "Despejamos ye en la primera, donde su coeficiente es uno. Escribimos esa expresión, entre paréntesis, en lugar de ye en la segunda. Queda una ecuación solo con equis: equis vale tres. Volvemos al despeje: ye vale dos. Y verificamos en las dos ecuaciones originales." |
| Equivalencia de sistemas | "¿Por qué funciona? El sistema nuevo tiene exactamente las mismas soluciones: despejar no cambia nada y, si ye vale once menos tres equis, escribir una cosa u otra es lo mismo." |
| Punto recorriendo la recta azul | "En el dibujo, al usar ye igual a once menos tres equis solo miramos puntos de la recta azul. La segunda ecuación nos dice cuál de ellos está también en la naranja: el tres, dos." |

### Video 2 — `SustitucionCuandoConviene`

| En pantalla | Narración |
|---|---|
| Cuatro despejes posibles con fracciones | "Si ningún coeficiente es uno o menos uno, cualquier despeje trae fracciones. Se puede igual: multiplicamos por el denominador y seguimos." |
| Sustitución con tres incógnitas | "Con tres incógnitas también funciona, pero cada sustitución alarga las expresiones. Con cinco o diez incógnitas sería inmanejable: necesitaremos un método más ordenado." |

### Video 3 — `SustitucionCasosEspeciales`

| En pantalla | Narración |
|---|---|
| $0\cdot y = 0$ | "A veces la incógnita desaparece. Si queda cero igual a cero, cualquier valor sirve: infinitas soluciones." |
| $0\cdot y = -5$ | "Si queda algo falso, como cero igual a menos cinco, no hay solución." |
| Tabla de tres casos | "La ecuación final con una incógnita decide el tipo de sistema: son los tres casos de la lección seis." |
| Error de sustituir en la misma ecuación | "Cuidado: si sustituimos el despeje en la misma ecuación de la que salió, siempre obtenemos una identidad. Hay que sustituir en la otra." |

---

## Errores frecuentes

- Olvidar el paréntesis al sustituir.
- Sustituir en la misma ecuación del despeje.
- Interpretar $0 = 0$ como "no hay solución".
- No verificar en las ecuaciones originales.

## Resumen y conexión

Sustituir elimina una incógnita y produce un sistema equivalente. En la Lección 14 vemos una variante: la igualación.
