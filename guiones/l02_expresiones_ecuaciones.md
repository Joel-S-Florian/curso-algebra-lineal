# L02 — Expresiones, igualdades y ecuaciones

**Objetivo**: saber qué es una variable, un término, un coeficiente y un término independiente; qué significa que un número sea solución de una ecuación; y qué transformaciones de una ecuación conservan sus soluciones y por qué.
**Prerrequisitos**: L01 (signos, fracciones, propiedades).
**Código**: `escenas/l02_expresiones_ecuaciones.py`
**Videos**: `videos/l02_expresiones_ecuaciones/1080p60/` → `VariableIncognitaCoeficiente.mp4`, `QueEsUnaEcuacion.mp4`, `TransformacionesQueConservanSoluciones.mp4`
**Ejercicios**: F00-N1-05, F00-N1-06, F00-N2-03, F00-N2-04, F00-N3-02, F00-N3-05, F00-N4-02, F00-N5-02.

---

## Desarrollo matemático

**Vocabulario.**

- **Variable**: símbolo (normalmente una letra) que representa un número y puede tomar distintos valores.
- **Incógnita**: variable cuyo valor buscamos.
- **Constante**: número fijo.
- **Expresión algebraica**: combinación de números y variables con operaciones, como $3x + 2y - 5$.
- **Término**: cada sumando, **con su signo**. En $3x + 2y - 5$ los términos son $3x$, $+2y$ y $-5$.
- **Coeficiente**: número que multiplica a una variable (3 para $x$, 2 para $y$). Si no se ve, es 1 o $-1$: $x = 1\cdot x$, $-y = (-1)\cdot y$.
- **Término independiente**: el término sin variable ($-5$, con su signo).
- **Términos semejantes**: los que tienen la misma variable; se suman sus coeficientes por la distributiva: $3x + 5x = 8x$. $2x + 3y$ no se puede simplificar.
- **Evaluar**: sustituir cada variable por un número, **entre paréntesis**.

**Ecuaciones.** Una *igualdad* afirma que dos expresiones valen lo mismo. Una *ecuación* es una igualdad con incógnitas; una *solución* es un valor que la hace verdadera; *resolver* es encontrar todas las soluciones (el *conjunto solución*); *verificar* es sustituir y comprobar. Una ecuación puede tener una solución ($2x + 1 = 7$), infinitas ($2(x+1) = 2x + 2$, una *identidad*) o ninguna ($x + 1 = x + 2$).

**Transformaciones que conservan las soluciones.** Dos ecuaciones son *equivalentes* si tienen exactamente las mismas soluciones.

- Regla 1: sumar o restar la misma cantidad a ambos lados.
- Regla 2: multiplicar o dividir ambos lados por el mismo número **distinto de 0**.

*Justificación (regla 1).* Si $a = b$, entonces $a + c = b + c$ (sumar el mismo número a dos números iguales da resultados iguales). Recíprocamente, si $a + c = b + c$, restando $c$ se vuelve a $a = b$. Como cada paso puede deshacerse, un número satisface la ecuación original si y solo si satisface la nueva. La regla 2 se justifica igual, deshaciendo con el inverso $1/c$, que existe porque $c \neq 0$ (la prueba completa es el ejercicio F00-N5-02).

"Pasar restando" es la regla 1 escrita deprisa, no una regla nueva.

**Pasos que NO conservan las soluciones** (no se pueden deshacer con seguridad):

- multiplicar por 0 ($x = 2 \to 0 = 0$: aparecen soluciones falsas);
- elevar al cuadrado ($x = 2 \to x^2 = 4$, que también cumple $x = -2$);
- dividir entre una expresión que puede valer 0 ($x^2 = x \to x = 1$: se pierde $x = 0$).

---

## Guion de narración

### Video 1 — `VariableIncognitaCoeficiente`

| En pantalla | Narración |
|---|---|
| Una caja con «?» se convierte en $x$; $x$ toma valores | "Imagina una caja con un número dentro que no conoces. En matemáticas esa caja se escribe con una letra. Como puede valer uno, dos, menos siete o un medio, decimos que es una variable. Cuando buscamos el valor concreto que cumple una condición, la llamamos incógnita, que significa 'desconocida'." |
| $3x + 2y - 5$ con llaves bajo cada término | "Una expresión está formada por términos, que son los sumandos. El signo que va delante pertenece al término: el tercer término no es cinco, es menos cinco." |
| Coeficientes en azul, término independiente en naranja | "El número que multiplica a cada variable es su coeficiente. El término sin variable es el término independiente. Estos colores serán los mismos durante todo el curso." |
| $x - y + 4 \to 1x + (-1)y + 4$ | "Cuando no se ve un número delante de la letra, el coeficiente es uno, o menos uno si hay un signo menos. Esto será fundamental al escribir matrices." |
| Evaluación con paréntesis; $(-3)^2$ frente a $-3^2$ | "Evaluar es sustituir las letras por números. Pon siempre el número entre paréntesis: así no se pierde ningún signo." |
| Términos semejantes | "Solo se pueden juntar términos con la misma variable, sumando sus coeficientes. Dos equis más tres ye no es cinco equis ye: no se puede simplificar." |

### Video 2 — `QueEsUnaEcuacion`

| En pantalla | Narración |
|---|---|
| Balanza con $2x + 1$ y $7$ | "Una igualdad es como una balanza en equilibrio: afirma que lo de la izquierda pesa lo mismo que lo de la derecha." |
| Pruebas con $x = 1, 5, 3$; la balanza se inclina | "Si $x$ vale uno, la izquierda pesa tres y la balanza cae hacia la derecha. Con cinco pesa once y cae hacia la izquierda. Solo con tres se equilibra: tres es la solución." |
| Vocabulario | "Una ecuación es una igualdad con incógnitas. Solución es el valor que la hace verdadera. Resolver es encontrar todas las soluciones, y verificar es sustituir y comprobar." |
| Tres ecuaciones: una, infinitas, ninguna | "No todas las ecuaciones se comportan igual. Unas tienen una solución. Otras se cumplen para cualquier valor: se llaman identidades. Y otras no se cumplen nunca. Estos tres casos, una, infinitas o ninguna, son la columna vertebral de todo el curso." |

### Video 3 — `TransformacionesQueConservanSoluciones`

| En pantalla | Narración |
|---|---|
| Balanza: $2x+1 \mid 7 \to 2x \mid 6 \to x \mid 3$ | "Si quitamos uno de cada plato, la balanza sigue equilibrada. Si dejamos la mitad en cada plato, también. Así llegamos de dos equis más uno igual a siete hasta equis igual a tres sin romper nunca el equilibrio." |
| Reglas 1 y 2; el $+1$ «pasa» al otro lado como $-1$ | "Las dos reglas seguras son: sumar o restar lo mismo en ambos lados, y multiplicar o dividir ambos lados por un número distinto de cero. Lo que en el colegio se llama 'pasar restando' es la regla uno escrita deprisa." |
| Flechas de ida y vuelta entre ecuaciones | "¿Por qué no cambian las soluciones? Porque cada paso se puede deshacer: si resto uno, puedo volver sumando uno; si divido entre dos, vuelvo multiplicando por dos. Así, un número cumple la primera ecuación si y solo si cumple la última. Decimos que son equivalentes." |
| Pasos peligrosos en rojo | "Hay pasos que no se pueden deshacer. Multiplicar por cero convierte cualquier ecuación en cero igual a cero. Elevar al cuadrado puede añadir soluciones falsas. Y dividir entre equis puede hacer perder la solución equis igual a cero. Por eso la regla dos dice 'distinto de cero'." |
| Verificación | "Y al final, siempre, verificar en la ecuación original." |

---

## Errores frecuentes de la lección

- Olvidar el signo del término: decir que el término independiente de $3x - 5$ es 5.
- Creer que $x$ no tiene coeficiente (lo tiene: 1).
- Juntar términos no semejantes: $2x + 3y = 5xy$.
- Aplicar una operación solo a un lado, o solo a un término de un lado.
- Dividir entre una expresión con la incógnita sin estudiar el caso en que vale 0.
- No verificar.

## Resumen y conexión

Resolver una ecuación es sustituirla por otras equivalentes cada vez más simples. En la Lección 15 (reducción) y en la Lección 24 (operaciones elementales por filas) usaremos exactamente la misma idea con varias ecuaciones a la vez: operaciones reversibles que no cambian el conjunto de soluciones.
