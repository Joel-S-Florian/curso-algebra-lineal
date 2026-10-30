# L04 — Lenguaje matemático: conjuntos, subíndices, sumatorios y lógica

**Objetivo**: leer y escribir la notación que usa el resto del curso (conjuntos, subíndices, $\Sigma$, $\Rightarrow$, $\Leftrightarrow$) y entender qué es una demostración.
**Prerrequisitos**: L01–L03.
**Código**: `escenas/l04_lenguaje_matematico.py`
**Videos**: `videos/l04_lenguaje_matematico/1080p60/` → `ConjuntosYPertenencia.mp4`, `SubindicesYSumatorio.mp4`, `ImplicacionYEquivalencia.mp4`, `ComoSeDemuestraAlgo.mp4`
**Ejercicios**: F00-N1-08, F00-N2-07, F00-N2-08, F00-N3-04, F00-N4-04, F00-N5-04.

---

## Desarrollo matemático

**Conjuntos.** Un conjunto es una colección de objetos (sus *elementos*). Se describe:

- por *extensión*: $A = \{1, 2, 3\}$;
- por *comprensión* (una propiedad): $S = \{x \in \mathbb{R} : 2x + 1 = 7\}$, que se lee "los $x$ reales tales que $2x + 1 = 7$". Aquí $S = \{3\}$.

Notación: $a \in A$ ($a$ pertenece a $A$), $a \notin A$, $\varnothing$ (conjunto vacío), $A \subset B$ (todo elemento de $A$ está en $B$), $A \cap B = \{x : x \in A \text{ y } x \in B\}$ (intersección).

El **conjunto solución de un sistema** es la intersección de los conjuntos solución de sus ecuaciones. Ejemplo: $S_1 = \{(x,y) : x + y = 3\}$, $S_2 = \{(x,y) : x - y = 1\}$, $S_1 \cap S_2 = \{(2, 1)\}$. Ojo: $\{(2,1)\}$ es un conjunto con un elemento y $(2, 1)$ es ese elemento.

**Subíndices.** $x_1, x_2, \dots, x_n$ permiten tener tantas incógnitas como haga falta. Un subíndice es una etiqueta: $x_2$ (la incógnita número 2) no es $x \cdot 2$ ni $x^2$. Con dos subíndices, $a_{ij}$ es el número de la fila $i$, columna $j$; $a_{23} \neq a_{32}$ en general.

**Sumatorio.**
$$\sum_{k=1}^{n} f(k) = f(1) + f(2) + \dots + f(n).$$
El índice $k$ es "mudo": $\sum_{j=1}^3 a_j x_j = \sum_{k=1}^3 a_k x_k$. La ecuación lineal general con $n$ incógnitas se escribe $\sum_{j=1}^{n} a_j x_j = b$.

**Lógica.**

- *Proposición*: afirmación que es verdadera o falsa.
- *Implicación* $P \Rightarrow Q$: siempre que $P$ es verdadera, $Q$ también. Su *recíproco* $Q \Rightarrow P$ es otra afirmación, que puede ser falsa ($x = 2 \Rightarrow x^2 = 4$ es verdadera; $x^2 = 4 \Rightarrow x = 2$ es falsa, contraejemplo $x = -2$).
- En $P \Rightarrow Q$: $P$ es **condición suficiente** para $Q$, y $Q$ es **condición necesaria** para $P$. Si representamos los objetos que cumplen cada propiedad, $P \Rightarrow Q$ significa que el conjunto de $P$ está contenido en el de $Q$.
- *Equivalencia* $P \Leftrightarrow Q$ ("si y solo si"): $P \Rightarrow Q$ y $Q \Rightarrow P$. Cada una es condición necesaria y suficiente para la otra.
- *Contrarrecíproco*: $P \Rightarrow Q$ es lo mismo que $\text{no } Q \Rightarrow \text{no } P$ (no es lo mismo que el recíproco).

**Demostraciones.**

- Comprobar ejemplos no demuestra un "para todo": $n^2 + n + 41$ es primo para $n = 0, 1, \dots, 39$, pero $40^2 + 40 + 41 = 1681 = 41^2$.
- Un *contraejemplo* basta para refutar un "para todo".
- *Demostración directa*: de las hipótesis a la conclusión, justificando cada paso. Ejemplo: si $a = 2k$ y $b = 2m$, entonces $a + b = 2(k + m)$, que es par.
- *Reducción al absurdo*: se supone lo contrario y se llega a una contradicción. Ejemplo: $\sqrt 2$ es irracional (prueba completa en el video 4).

---

## Guion de narración

### Video 1 — `ConjuntosYPertenencia`

| En pantalla | Narración |
|---|---|
| Óvalo con 1, 2, 3; $A = \{1, 2, 3\}$; $2 \in A$, $5 \notin A$ | "Un conjunto es una colección de objetos. Si los escribimos entre llaves, lo describimos por extensión. El símbolo que parece una e redondeada significa 'pertenece a'; tachado, 'no pertenece a'." |
| $S = \{x \in \mathbb{R} : 2x + 1 = 7\}$ con llaves explicativas | "También se puede describir un conjunto con una propiedad. Esto se lee: los equis reales tales que dos equis más uno es siete. Es exactamente el conjunto solución de la ecuación: el conjunto que contiene solo al tres." |
| Vacío, todo $\mathbb{R}$, subconjuntos | "Si ningún número cumple la condición, obtenemos el conjunto vacío. Si todos la cumplen, obtenemos todos los reales. Y un conjunto es subconjunto de otro si todos sus elementos están también en el otro." |
| Diagrama de Venn y dos rectas que se cortan | "La intersección contiene lo que está en los dos conjuntos a la vez. Y aquí está la conexión con los sistemas: las soluciones de un sistema son las que cumplen todas las ecuaciones a la vez, es decir, la intersección de los conjuntos solución. Geométricamente, el punto donde se cortan las rectas." |

### Video 2 — `SubindicesYSumatorio`

| En pantalla | Narración |
|---|---|
| $x, y, z, w, \dots$ → $x_1, x_2, \dots, x_n$ | "Con muchas incógnitas se acaban las letras. La solución es numerarlas con subíndices: equis uno, equis dos, hasta equis ene." |
| $x_2$, $x\cdot 2$, $x^2$ | "Un subíndice no es una operación: equis sub dos es simplemente la segunda incógnita. No es equis por dos, ni equis al cuadrado." |
| Tabla $a_{ij}$; fila 2 y columna 3 marcadas | "Con dos subíndices organizamos números en una tabla: el primero indica la fila y el segundo la columna. a dos tres está en la fila dos, columna tres, y no es lo mismo que a tres dos. Así nombraremos los números de una matriz." |
| $\sum_{k=1}^{4} k$ y el contador $k = 1, 2, 3, 4$ | "La letra griega sigma significa 'suma de'. Debajo se indica dónde empieza el índice, arriba dónde termina. Damos al índice los valores uno, dos, tres y cuatro, y sumamos: diez." |
| Más ejemplos y la ecuación lineal general | "Con sigma, la ecuación lineal general con ene incógnitas cabe en una línea: la suma de a jota por equis jota, con jota de uno a ene, es igual a be." |

### Video 3 — `ImplicacionYEquivalencia`

| En pantalla | Narración |
|---|---|
| Proposiciones verdaderas, falsas y una pregunta | "Una proposición es una frase que es verdadera o falsa. 'Dos más uno es tres' lo es. Una pregunta no." |
| $x = 2 \Rightarrow x^2 = 4$ y su recíproco | "La flecha doble significa 'si... entonces'. Si equis es dos, su cuadrado es cuatro: verdadero. Al revés no: equis igual a menos dos también tiene cuadrado cuatro. Basta un contraejemplo para tumbar una implicación." |
| Óvalos: múltiplos de 4 dentro de los pares | "Si ser múltiplo de cuatro implica ser par, decimos que ser múltiplo de cuatro es suficiente para ser par, y que ser par es necesario para ser múltiplo de cuatro. Pero no suficiente: seis es par y no es múltiplo de cuatro." |
| $P \Leftrightarrow Q$, ejemplo con $2x + 1 = 7$ | "Cuando la implicación vale en los dos sentidos, decimos 'si y solo si': cada afirmación es condición necesaria y suficiente para la otra. Eso es lo que significaba que dos ecuaciones fueran equivalentes." |
| Contrarrecíproco y anticipo de Rouché-Frobenius | "Una implicación dice lo mismo que su contrarrecíproco: si no es par, no es múltiplo de cuatro. Más adelante, el teorema de Rouché-Frobenius será justamente un 'si y solo si' que decide si un sistema tiene solución." |

### Video 4 — `ComoSeDemuestraAlgo`

| En pantalla | Narración |
|---|---|
| $n^2 + n + 41$ para $n = 0..5$ y luego $n = 40$ | "Esta fórmula da números primos para n igual a cero, uno, dos... hasta treinta y nueve. Parece una ley. Pero para n igual a cuarenta da mil seiscientos ochenta y uno, que es cuarenta y uno al cuadrado. Los ejemplos, por muchos que sean, no demuestran un 'para todo'." |
| Demostración directa de "par + par = par" | "Una demostración directa parte de las definiciones: un número es par si es dos por un entero. Escribimos a y be así, sumamos, sacamos factor común, y obtenemos dos por un entero. Cada paso tiene una justificación." |
| Pasos de la prueba de que $\sqrt2$ es irracional | "En la reducción al absurdo suponemos lo contrario de lo que queremos probar. Si raíz de dos fuera una fracción irreducible pe sobre cu, al elevar al cuadrado p al cuadrado sería el doble de q al cuadrado, luego p sería par; sustituyendo, q también sería par. Pero entonces la fracción no era irreducible: contradicción. Luego raíz de dos no es una fracción." |
| Intuición frente a demostración | "En la lección uno, un dibujo nos dijo dónde está raíz de dos. Hoy hemos demostrado que no es una fracción. En este curso, las animaciones ayudan a entender; las demostraciones van aparte y con sus hipótesis." |

---

## Errores frecuentes de la lección

- Confundir $\{(2,1)\}$ (conjunto) con $(2,1)$ (punto), o $\varnothing$ con $\{0\}$ (este último sí tiene un elemento).
- Leer $x_2$ como $x \cdot 2$ o $x^2$; confundir $a_{23}$ con $a_{32}$.
- Dar por demostrado el recíproco de una implicación.
- Confundir condición necesaria con suficiente.
- Creer que varios ejemplos demuestran un "para todo".

## Resumen y conexión

Con esta lección termina la Unidad 0. Ya tenemos los números, el álgebra, la geometría de coordenadas y el lenguaje necesarios para empezar la Unidad 1: qué es exactamente una ecuación lineal (Lección 5).
