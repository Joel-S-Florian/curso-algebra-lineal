# L17 — Vectores: flecha, punto, fila y columna; suma, escalar y combinación lineal

**Objetivo**: entender un vector como lista de números y como flecha, operar con vectores y descubrir que buscar los pesos de una combinación lineal es resolver un sistema.
**Prerrequisitos**: L03 (coordenadas), L16.
**Código**: `escenas/l17_vectores.py`
**Videos**: `videos/l17_vectores/1080p60/` → `VectorComoFlechaYComoPunto.mp4`, `SumaYEscalarGeometricos.mp4`, `PrimeraCombinacionLineal.mp4`
**Ejercicios**: F05-N1-03, F05-N2-01, F05-N3-01.

---

## Desarrollo matemático

**Vector.** Lista ordenada de $n$ números reales (sus *componentes*); el conjunto de todos es $\mathbb{R}^n$. En $\mathbb{R}^2$ y $\mathbb{R}^3$ se dibuja como un punto o como una flecha desde el origen (un desplazamiento). Flechas con la misma longitud, dirección y sentido representan el mismo desplazamiento.

**Fila y columna.** Vector columna: matriz $n\times 1$; vector fila: $1\times n$. La **traspuesta** $^T$ convierte una en la otra. Convenio del curso: los vectores son columnas; a veces se escriben en línea, $(3, 2, -1)$, para ahorrar espacio.

**Operaciones** (solo entre vectores con el mismo número de componentes):

- Suma: $\mathbf{u} + \mathbf{v}$ componente a componente. Geométricamente, punta con cola; $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ (paralelogramo).
- Producto por un escalar: $c\mathbf{u}$ multiplica cada componente. Estira ($|c| > 1$), encoge ($|c| < 1$) o invierte ($c < 0$). Todos los $c\mathbf{u}$ están en una recta por el origen.
- Opuesto: $-\mathbf{u} = (-1)\mathbf{u}$; resta: $\mathbf{u} - \mathbf{v} = \mathbf{u} + (-1)\mathbf{v}$; vector nulo $\mathbf{0}$, neutro de la suma.

**Combinación lineal.** $a\mathbf{u} + b\mathbf{v}$ con $a, b$ reales (los *pesos*). ¿Qué pesos dan $\mathbf{w} = (5, 3)$ con $\mathbf{u} = (1, 2)$, $\mathbf{v} = (3, -1)$? Igualando componentes: $a + 3b = 5$, $2a - b = 3$, de donde $a = 2$, $b = 1$. **Encontrar los pesos de una combinación lineal es resolver un sistema lineal.**

---

## Guion de narración

### Video 1 — `VectorComoFlechaYComoPunto`

| En pantalla | Narración |
|---|---|
| $\mathbf{v} = (3, 2)$ como punto y como flecha | "Un vector es una lista ordenada de números. El vector tres, dos se puede dibujar como un punto, o como una flecha desde el origen: avanza tres y sube dos." |
| Copias trasladadas | "Una flecha con la misma longitud, dirección y sentido representa el mismo desplazamiento, esté donde esté. Pero en el curso, salvo aviso, dibujaremos los vectores desde el origen." |
| Columna, fila y traspuesta | "Los mismos números se pueden escribir en columna o en fila. La traspuesta cambia uno por otro. En este curso los vectores son columnas." |

### Video 2 — `SumaYEscalarGeometricos`

| En pantalla | Narración |
|---|---|
| $\mathbf{u} + \mathbf{v}$ y paralelogramo | "Sumar es sumar componentes. En el dibujo, un desplazamiento tras otro; en cualquier orden se llega al mismo sitio." |
| $c\mathbf{u}$ con $c$ variando | "Multiplicar por un número estira o encoge la flecha; con un número negativo, la da la vuelta. Con cero, se reduce al vector nulo." |
| Resta y vector nulo | "Restar es sumar el opuesto. Y solo se suman vectores con el mismo número de componentes." |

### Video 3 — `PrimeraCombinacionLineal`

| En pantalla | Narración |
|---|---|
| $a\mathbf{u} + b\mathbf{v}$ con pesos variables | "Mezclando dos vectores con dos pesos obtenemos una combinación lineal. Al cambiar los pesos, llegamos a puntos distintos." |
| Llegar a $\mathbf{w} = (5, 3)$ | "Con a igual a dos y be igual a uno llegamos exactamente a cinco, tres. ¿Cómo encontrarlos sin tantear?" |
| Sistema $a + 3b = 5$, $2a - b = 3$ | "Igualando componentes aparece un sistema de ecuaciones. Resolver un sistema lineal es lo mismo que buscar los pesos de una combinación lineal." |

---

## Errores frecuentes

- Intercambiar componentes al dibujar.
- Sumar vectores de distinto tamaño.
- Al plantear los pesos, usar las componentes de un mismo vector en la misma ecuación.

## Resumen y conexión

Vectores = listas de números; se suman y se escalan componente a componente, y las combinaciones lineales conectan con los sistemas. En la Lección 18 extendemos suma y escalar a matrices.
