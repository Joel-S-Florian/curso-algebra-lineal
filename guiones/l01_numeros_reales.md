# L01 — Números reales y sus operaciones

**Objetivo**: conocer los conjuntos numéricos y operar con signos, fracciones y propiedades sin errores, porque todo despeje y toda eliminación del curso se apoya en estas reglas.
**Prerrequisitos**: saber sumar, restar, multiplicar y dividir enteros positivos.
**Código**: `escenas/l01_numeros_reales.py`
**Videos**: `videos/l01_numeros_reales/1080p60/` → `ConjuntosNumericos.mp4`, `ReglasDeSignos.mp4`, `Fracciones.mp4`, `PropiedadesDeLasOperaciones.mp4`
**Ejercicios**: F00-N1-01 a F00-N1-04, F00-N2-01, F00-N2-02, F00-N3-01, F00-N4-01, F00-N5-01, F00-N5-05 (en `ejercicios/F00_preliminares.md`).

---

## Desarrollo matemático

**Conjuntos numéricos.** Cada conjunto nace para resolver una operación que el anterior no permite:

- Naturales $\mathbb{N} = \{1, 2, 3, \dots\}$: contar. (Algunos libros incluyen el 0; en este curso no cambia nada).
- Enteros $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$: restar siempre ($3 - 5 = -2$).
- Racionales $\mathbb{Q} = \{p/q : p, q \text{ enteros}, q \neq 0\}$: dividir siempre (entre un número distinto de 0). Su expresión decimal termina o es periódica.
- Reales $\mathbb{R}$: todos los puntos de la recta. Incluyen los **irracionales**, números que no son fracciones, como $\sqrt 2$ (la diagonal del cuadrado de lado 1) o $\pi$.

Se cumple $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$. Los coeficientes y las soluciones de todos los sistemas del curso son números reales.

**Signos.** El opuesto $-a$ es el simétrico de $a$ respecto del 0; por eso $-(-a) = a$. Restar es sumar el opuesto: $a - b = a + (-b)$. En productos y cocientes, signos iguales dan $+$ y distintos dan $-$. La regla $(-)\cdot(-) = (+)$ no es un capricho: es la única coherente con la distributiva (ver el patrón de la escena 2). Cuidado: $-3^2 = -(3^2) = -9$, pero $(-3)^2 = 9$.

**Fracciones.** $a/b$ significa partir la unidad en $b$ partes iguales y tomar $a$; además $a/b = a \div b$. **No se divide entre 0**: $6/0$ exigiría un número que multiplicado por 0 diera 6 (no existe), y $0/0$ admitiría cualquiera (no hay respuesta única). Para sumar se busca denominador común; para multiplicar, numerador por numerador y denominador por denominador; para dividir, se multiplica por la inversa.

**Propiedades.** Suma y producto son conmutativos y asociativos (resta y división, no). Distributiva: $a(b + c) = ab + ac$. Neutros: $a + 0 = a$, $a\cdot 1 = a$. Opuesto: $a + (-a) = 0$. Inverso: $a \cdot \frac1a = 1$ **solo si $a \neq 0$**. Orden de las operaciones: paréntesis, potencias, multiplicaciones y divisiones (de izquierda a derecha), sumas y restas (de izquierda a derecha).

---

## Guion de narración

### Video 1 — `ConjuntosNumericos`

| En pantalla | Narración |
|---|---|
| Recta numérica; aparecen puntos en 1, 2, 3… | "Los primeros números que aprendemos sirven para contar: uno, dos, tres. Se llaman números naturales y los representamos como puntos de una recta, separados siempre la misma distancia." |
| $3 - 5 = \,?$ y una flecha de 5 pasos a la izquierda | "Pero con ellos no siempre se puede restar. Si a 3 le quito 5, me salgo por la izquierda del 1." |
| Los naturales se reflejan al otro lado del 0 | "Para que la resta siempre tenga respuesta, reflejamos los naturales al otro lado del cero: aparecen los negativos. Naturales, cero y negativos forman los números enteros." |
| $1 \div 2$; aparecen $\tfrac12$, $-\tfrac34$, $\tfrac53$, $-\tfrac72$ | "Con los enteros tampoco se puede dividir siempre: uno entre dos no es entero. Las fracciones de enteros, con denominador distinto de cero, son los números racionales. Llenan muchísimos huecos de la recta." |
| Cuadrado de lado 1, su diagonal gira hasta la recta | "Pero no todos. La diagonal de un cuadrado de lado uno mide raíz de dos, por el teorema de Pitágoras. Si la giramos hasta la recta, marca un punto. Ese punto no corresponde a ninguna fracción. Lo mismo pasa con pi. El dibujo nos dice dónde está raíz de dos; que no es una fracción lo demostraremos en la lección 4, porque un dibujo no es una demostración." |
| Rectángulos anidados $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$ | "Juntando racionales e irracionales obtenemos los números reales: todos los puntos de la recta. Cada conjunto está contenido en el siguiente. En este curso, los coeficientes y las soluciones serán números reales." |

### Video 2 — `ReglasDeSignos`

| En pantalla | Narración |
|---|---|
| El 3 se refleja en el −3 y vuelve | "El signo menos delante de un número significa 'el opuesto': su reflejo respecto del cero. Reflejar dos veces nos devuelve al punto de partida; por eso menos menos tres es tres." |
| Flechas: +3 y luego −5 | "Sumar es desplazarse por la recta. Tres más menos cinco: avanzo tres y retrocedo cinco, llego a menos dos. Y restar cinco es exactamente lo mismo que sumar menos cinco: toda resta es una suma." |
| Patrón $(-3)\cdot 2, (-3)\cdot 1, \dots$ con saltos $+3$ | "¿Por qué menos por menos es más? Mira la tabla del menos tres. Cada vez que el segundo factor baja una unidad, el resultado sube tres. Si el patrón sigue, menos tres por menos uno tiene que ser tres. Cualquier otra regla rompería la propiedad distributiva." |
| Tabla de signos y divisiones | "En resumen: signos iguales dan positivo, signos distintos dan negativo, tanto al multiplicar como al dividir." |
| Errores: $-3^2$, $(-3)^2$, $-(2+5)$ | "Dos errores muy frecuentes. Primero: la potencia actúa antes que el signo, así que menos tres al cuadrado es menos nueve. Si queremos elevar el menos tres, hay que escribir paréntesis. Segundo: un signo menos delante de un paréntesis cambia el signo de todos los términos de dentro, no solo del primero." |

### Video 3 — `Fracciones`

| En pantalla | Narración |
|---|---|
| Barra de 4 trozos con 3 coloreados | "Tres cuartos significa: parto la unidad en cuatro trozos iguales y tomo tres. Además, tres cuartos es tres dividido entre cuatro." |
| $6/2 = 3$ porque $2\cdot 3 = 6$; $6/0$ y $0/0$ en rojo | "Dividir es la operación inversa de multiplicar: seis entre dos es tres porque dos por tres es seis. Entonces, seis entre cero debería ser un número que multiplicado por cero dé seis: no existe. Y cero entre cero, uno que multiplicado por cero dé cero: sirve cualquiera. En ningún caso hay una respuesta única, así que dividir entre cero no está definido. Esta regla la usaremos constantemente: antes de dividir, comprueba que no divides entre cero." |
| Barras de $6/8$ y $3/4$ con la misma longitud | "Seis octavos y tres cuartos ocupan exactamente lo mismo: son la misma cantidad. Dividir numerador y denominador por el mismo número distinto de cero no cambia la fracción. Eso es simplificar." |
| Medios y tercios se convierten en sextos | "Para sumar un medio y un tercio, primero partimos ambos en trozos del mismo tamaño, sextos. Tres sextos más dos sextos son cinco sextos. Sumar numeradores y denominadores por separado da dos quintos, que es menor que un medio: absurdo." |
| Producto, cociente y signo de una fracción | "Para multiplicar, numerador por numerador y denominador por denominador. Para dividir, multiplicamos por la fracción inversa. Y el signo menos puede ir delante, arriba o abajo: es la misma fracción." |

### Video 4 — `PropiedadesDeLasOperaciones`

| En pantalla | Narración |
|---|---|
| Conmutativa y asociativa; contraejemplos en rojo | "En la suma y en el producto el orden no importa, y tampoco cómo agrupemos. En la resta y la división sí importa: cinco menos dos no es dos menos cinco. Más adelante veremos que el producto de matrices tampoco es conmutativo." |
| Rectángulo $2\times(3+2)$ partido en dos | "La propiedad distributiva tiene una imagen sencilla: el área de un rectángulo de altura dos y base tres más dos es la suma de las áreas de sus dos partes. Leída al revés, es 'sacar factor común': tres equis más cinco equis es ocho equis." |
| Neutros, opuesto, inverso; $0\cdot x \ne 1$ | "El cero no cambia una suma; el uno no cambia un producto. Todo número tiene opuesto, y todo número distinto de cero tiene inverso. El cero no: cero por cualquier cosa da cero, nunca uno. Por eso dividir entre a, que es multiplicar por su inverso, exige a distinto de cero." |
| $2 + 3\cdot 4$: 20 tachado, 14 correcto | "Por último, el orden de las operaciones: paréntesis, potencias, multiplicaciones y divisiones, y al final sumas y restas, siempre de izquierda a derecha cuando hay empate." |

---

## Errores frecuentes de la lección

- Escribir $-3^2 = 9$. Comprobación: ¿la potencia afecta al signo? Solo si hay paréntesis.
- Repartir mal el signo: $-(a + b) = -a + b$. Correcto: $-a - b$.
- Sumar fracciones sumando numeradores y denominadores.
- Dividir entre una expresión sin comprobar que no vale 0.
- Hacer las operaciones de izquierda a derecha sin respetar la jerarquía.

## Resumen y conexión

Los números reales son todos los puntos de la recta; con ellos se suma, resta, multiplica y divide (salvo entre 0). Las propiedades de esta lección son las que justifican cada paso al despejar una ecuación (Lección 2) y cada operación por filas en la eliminación de Gauss (Lección 24).
