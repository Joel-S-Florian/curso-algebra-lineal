# L15 — El método de reducción y comparación de métodos

**Objetivo**: resolver sistemas por reducción, demostrar que sumar un múltiplo de una ecuación a otra conserva las soluciones, y elegir el método más adecuado.
**Prerrequisitos**: L02, L13, L14.
**Código**: `escenas/l15_reduccion.py`
**Videos**: `videos/l15_reduccion/1080p60/` → `ReduccionPasoAPaso.mp4`, `PorQueReduccionConservaSoluciones.mp4`, `ComparacionDeMetodos.mp4`
**Ejercicios**: F04-N1-04, N2-03, N2-04, N2-05, N3-03, N3-04, N4-01, N4-02, N5-02.

---

## Desarrollo matemático

**Método.**

1. Elegir la incógnita a eliminar.
2. Si sus coeficientes no son opuestos, multiplicar las ecuaciones por números **no nulos** para que lo sean (por ejemplo, ambos coeficientes iguales al mínimo común múltiplo).
3. Sumar (o restar) las ecuaciones: la incógnita desaparece.
4. Resolver la ecuación resultante y sustituir en una ecuación original.
5. Verificar.

Ejemplos: $3x + 2y = 7$, $5x - 2y = 9$: sumando, $8x = 16$. $2x + 3y = 8$, $3x - 4y = -5$: $3E_1 - 2E_2$ da $17y = 34$.

**Teorema.** Sustituir $E_2$ por $E_2 + kE_1$, conservando $E_1$, no cambia el conjunto de soluciones.

*Demostración.* ($\Rightarrow$) Si $(x, y)$ cumple $E_1$ y $E_2$, al sumar igualdades ciertas obtenemos una igualdad cierta, $E_2 + kE_1$. ($\Leftarrow$) Si cumple $E_1$ y $E_2 + kE_1$, restando $kE_1$ cumple $E_2$. $\blacksquare$

Multiplicar una ecuación por $c \neq 0$ también es reversible (regla 2). Por eso:

- se cambia **una** ecuación usando otra que se **conserva**;
- nunca se multiplica por 0;
- no se cambian las dos ecuaciones a la vez (se puede perder información).

**Geometría.** $E_2 + kE_1$ es, para cada $k$, una recta que pasa por la solución: al variar $k$, gira alrededor de ella. Reducir es elegir el $k$ que la deja vertical ($x$ despejada) u horizontal ($y$ despejada).

**Comparación.**

| Método | Conviene cuando… | Limitación |
|---|---|---|
| Sustitución | hay un coeficiente $\pm 1$ | fracciones; crece con más incógnitas |
| Igualación | la misma incógnita ya está despejada | no escala a 3 incógnitas |
| Reducción | hay coeficientes opuestos o múltiplos fáciles | elegir multiplicadores; es la base de Gauss |

**Hacia Gauss.** Con tres incógnitas, usando $E_1$ para eliminar $x$ de $E_2$ y $E_3$ queda un sistema más pequeño. Hacerlo de forma ordenada es la eliminación de Gauss (Unidad 4). Como solo cambian los números, conviene guardarlos en una matriz (Unidad 3).

---

## Guion de narración

### Video 1 — `ReduccionPasoAPaso`

| En pantalla | Narración |
|---|---|
| Suma en columna con $+2y$ y $-2y$ | "Los coeficientes de ye son opuestos. Sumamos las ecuaciones: los lados izquierdos entre sí y los derechos entre sí. Ye desaparece y queda ocho equis igual a dieciséis." |
| $3E_1$ y $2E_2$; resta | "Si no hay coeficientes opuestos, los fabricamos multiplicando cada ecuación por un número distinto de cero. Tres veces la primera y dos veces la segunda tienen seis equis; al restarlas, equis desaparece." |

### Video 2 — `PorQueReduccionConservaSoluciones`

| En pantalla | Narración |
|---|---|
| Demostración en dos direcciones | "Cambiamos la segunda ecuación por ella misma más ka veces la primera, conservando la primera. Toda solución del sistema cumple la combinación. Y al revés, restando ka veces la primera recuperamos la segunda. Mismas soluciones." |
| Recta violeta girando alrededor de $(2, 1)$ | "En el dibujo, la recta combinada gira alrededor de la solución sin despegarse de ella. Con ka igual a uno queda vertical: equis igual a dos. Con ka igual a menos uno, horizontal: ye igual a uno. Reducir es girar la recta hasta que la respuesta se lea directamente." |
| Error de cambiar las dos ecuaciones | "Si cambiamos las dos ecuaciones a la vez, podemos quedarnos con dos copias de la misma información y ganar soluciones falsas." |

### Video 3 — `ComparacionDeMetodos`

| En pantalla | Narración |
|---|---|
| Tabla comparativa | "Los tres métodos llegan a la misma solución. Elegir bien solo ahorra cuentas y errores." |
| Reducción 3×3 | "Con tres incógnitas, usamos la primera ecuación para eliminar equis de las otras dos. Hacer esto de forma ordenada es la eliminación de Gauss." |
| Sistema → matriz | "Y como las letras solo ocupan sitio, guardamos los números en una tabla: una matriz." |

---

## Errores frecuentes

- Errores de signo al restar ecuaciones.
- Multiplicar solo un lado, o solo un término, de una ecuación.
- Cambiar las dos ecuaciones a la vez.
- Multiplicar por 0.

## Resumen y conexión

La reducción es el método más general: se basa en una operación reversible que conserva las soluciones. Con esta lección termina la Unidad 2. En la Unidad 3 (Lección 16) aprendemos el lenguaje de las matrices para escribir cualquier sistema de forma compacta.
