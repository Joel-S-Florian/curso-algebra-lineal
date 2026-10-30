# F12 — Combinaciones lineales, independencia, base y dimensión

Banco de las lecciones L43–L44. **Parte 1: 13 ejercicios**, ligados a los videos. La **parte 2** (27 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F12_combinaciones_independencia_base_parte2.md`; la familia completa suma **40**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $\operatorname{gen}\{\dots\}$ es el espacio generado; "independientes" significa linealmente independientes.
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f12_f14.py`.

| Lección | Ejercicios |
|---|---|
| L43 Combinaciones y espacio generado | N1-01, N1-02, N2-01 🎬, N2-02 🎬 |
| L44 Independencia, base y dimensión | N2-03 🎬, N3-01 🎬, N3-02, N3-03, N3-04, N4-01 🎬, N4-02, N4-03, N5-01 |

---

### F12-N1-01 · [C] Calcular una combinación lineal

**Objetivo**: efectuar $c_1\mathbf{u} + c_2\mathbf{v}$.
**Dificultad**: N1

**Enunciado.** Calcula $2\mathbf{u} - 3\mathbf{v}$ con $\mathbf{u} = (1, -1, 3)$ y $\mathbf{v} = (0, 2, 1)$.

<details><summary>Pista 1</summary>Multiplica cada vector por su coeficiente y luego resta componente a componente.</details>
<details><summary>Solución</summary>$2\mathbf{u} = (2, -2, 6)$, $3\mathbf{v} = (0, 6, 3)$; la diferencia es $(2, -8, 3)$.</details>
<details><summary>Errores frecuentes</summary>Restar solo la primera componente, o no repartir el signo menos entre las tres.</details>

### F12-N1-02 · [C] Hallar los coeficientes (2×2)

**Objetivo**: escribir un vector como combinación de otros dos.
**Dificultad**: N1

**Enunciado.** Escribe $(7, 4)$ como combinación lineal de $(1, 2)$ y $(3, 1)$.

<details><summary>Pista 1</summary>Plantea $c_1(1,2) + c_2(3,1) = (7,4)$ y separa en dos ecuaciones.</details>
<details><summary>Pista 2</summary>$c_1 + 3c_2 = 7$, $\;2c_1 + c_2 = 4$.</details>
<details><summary>Solución</summary>$c_1 = 1$, $c_2 = 2$: $(7, 4) = 1\cdot(1,2) + 2\cdot(3,1)$. Comprobación: $(1+6,\ 2+2) = (7, 4)$.</details>
<details><summary>Errores frecuentes</summary>Dar el resultado sin comprobarlo en las dos componentes.</details>

### F12-N2-01 · [C] ¿Pertenece al espacio generado? 🎬

**Objetivo**: decidir si $\mathbf{b} \in \operatorname{gen}\{\mathbf{u}, \mathbf{v}\}$ resolviendo un sistema.
**Dificultad**: N2

**Enunciado.** Con $\mathbf{u} = (1,1,0)$ y $\mathbf{v} = (0,1,1)$: ¿es $\mathbf{b} = (3,5,2)$ combinación lineal de ellos? ¿Y $\mathbf{b}' = (3,5,3)$? Si lo es, halla los coeficientes.

<details><summary>Pista 1</summary>$c_1\mathbf{u} + c_2\mathbf{v} = (c_1,\ c_1 + c_2,\ c_2)$. Iguala componente a componente.</details>
<details><summary>Pista 2</summary>La primera y la tercera componente dan $c_1$ y $c_2$; la segunda es la comprobación.</details>
<details><summary>Solución</summary>Para $\mathbf{b}$: $c_1 = 3$, $c_2 = 2$, y la segunda componente $3 + 2 = 5$ coincide: sí, $\mathbf{b} = 3\mathbf{u} + 2\mathbf{v}$. Para $\mathbf{b}'$: $c_1 = 3$, $c_2 = 3$, pero la segunda daría $6 \ne 5$: no es combinación lineal (sistema incompatible).</details>
<details><summary>Errores frecuentes</summary>Despejar solo con dos componentes y olvidar comprobar la tercera.</details>

### F12-N2-02 · [K] Describir el espacio generado 🎬

**Objetivo**: ver el espacio generado como recta, plano o todo $\mathbb{R}^2$.
**Dificultad**: N2

**Enunciado.** Describe geométricamente: a) $\operatorname{gen}\{(1,2),\ (2,4)\}$; b) $\operatorname{gen}\{(1,2),\ (2,1)\}$.

<details><summary>Pista 1</summary>¿Es uno de los vectores múltiplo del otro?</details>
<details><summary>Solución</summary>a) $(2,4) = 2(1,2)$: el segundo no añade nada; el espacio generado es la recta $y = 2x$. b) No son múltiplos y la matriz con esas columnas tiene rango 2: el espacio generado es todo $\mathbb{R}^2$.</details>
<details><summary>Errores frecuentes</summary>Decir que dos vectores siempre generan un plano.</details>

### F12-N2-03 · [C] Independencia de dos vectores 🎬

**Objetivo**: reconocer una dependencia y exhibir la relación.
**Dificultad**: N2

**Enunciado.** ¿Son independientes $\mathbf{u} = (1,2)$ y $\mathbf{v} = (2,4)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>¿Es uno múltiplo del otro?</details>
<details><summary>Solución</summary>No son independientes: $\mathbf{v} = 2\mathbf{u}$, es decir, $2\mathbf{u} - 1\mathbf{v} = \mathbf{0}$ con coeficientes no todos nulos.</details>
<details><summary>Errores frecuentes</summary>Dar una relación con todos los coeficientes cero (siempre existe y no prueba nada).</details>

### F12-N3-01 · [C] Independencia de tres vectores 🎬

**Objetivo**: decidir con rangos.
**Dificultad**: N3

**Enunciado.** Decide si son independientes: $(1,0,1)$, $(0,1,1)$, $(1,1,0)$. Si no, da una relación.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Pista 2</summary>Mira si cada columna tiene pivote.</details>
<details><summary>Solución</summary>La matriz $\begin{bmatrix} 1&0&1\\0&1&1\\1&1&0 \end{bmatrix}$ tiene rango 3 (su determinante vale $-2 \ne 0$): las tres columnas tienen pivote y los vectores son independientes.</details>
<details><summary>Errores frecuentes</summary>Pensar que, como cada par es independiente, el trío también lo es (no es cierto en general).</details>

### F12-N3-02 · [C] Una dependencia escondida

**Objetivo**: hallar la relación entre vectores dependientes.
**Dificultad**: N3

**Enunciado.** Decide si son independientes $(1,1,1)$, $(1,2,3)$, $(2,3,4)$. Si no, da una relación.

<details><summary>Pista 1</summary>Mira si algún vector es suma de otros.</details>
<details><summary>Pista 2</summary>$(1,1,1) + (1,2,3) = (2,3,4)$.</details>
<details><summary>Solución</summary>Son dependientes: $1\cdot(1,1,1) + 1\cdot(1,2,3) - 1\cdot(2,3,4) = \mathbf{0}$. La matriz tiene rango 2 < 3.</details>
<details><summary>Errores frecuentes</summary>Buscar solo múltiplos de un vector e ignorar las sumas.</details>

### F12-N3-03 · [K] Demasiados vectores

**Objetivo**: usar el rango para acotar.
**Dificultad**: N3

**Enunciado.** Explica por qué cuatro vectores cualesquiera de $\mathbb{R}^3$ son siempre linealmente dependientes.

<details><summary>Pista 1</summary>La matriz con esos vectores por columnas es $3 \times 4$; ¿cuánto puede valer su rango?</details>
<details><summary>Solución</summary>El rango de una matriz $3 \times 4$ es a lo sumo 3, así que como mínimo una de las 4 columnas no tiene pivote. Entonces $V\mathbf{c} = \mathbf{0}$ tiene una variable libre y, por tanto, soluciones no triviales: hay una combinación no trivial que da $\mathbf{0}$.</details>
<details><summary>Errores frecuentes</summary>Pensar que depende de los vectores concretos.</details>

### F12-N3-04 · [K] El vector nulo

**Objetivo**: aplicar la definición.
**Dificultad**: N3

**Enunciado.** Prueba que un conjunto que contiene al vector nulo es linealmente dependiente.

<details><summary>Solución</summary>Si $\mathbf{v}_1 = \mathbf{0}$, entonces $1\cdot\mathbf{v}_1 + 0\cdot\mathbf{v}_2 + \dots + 0\cdot\mathbf{v}_k = \mathbf{0}$ es una combinación con un coeficiente distinto de cero. Por definición, el conjunto es dependiente.</details>

### F12-N4-01 · [C] Base a partir de un generador 🎬

**Objetivo**: extraer una base con las columnas pivote.
**Dificultad**: N4

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} 1&2&0&1\\2&4&1&4\\1&2&1&3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Pista 2</summary>Toma esas columnas de la matriz original, no de la reducida.</details>
<details><summary>Solución</summary>La reducida es $\begin{bmatrix} 1&2&0&1\\0&0&1&2\\0&0&0&0 \end{bmatrix}$: pivotes en las columnas 1 y 3. Una base es $\{(1,2,1),\ (0,1,1)\}$ y la dimensión es 2.</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la reducida (sobre eso trata la L49).</details>

### F12-N4-02 · [C] Coordenadas respecto de una base

**Objetivo**: comprobar una base y hallar coordenadas.
**Dificultad**: N4

**Enunciado.** Comprueba que $\{(1,1),\ (1,-1)\}$ es una base de $\mathbb{R}^2$ y halla las coordenadas de $(3,1)$ en ella.

<details><summary>Pista 1</summary>Dos vectores de $\mathbb{R}^2$ son una base si la matriz con ellos por columnas tiene rango 2.</details>
<details><summary>Pista 2</summary>Resuelve $a + b = 3$, $\;a - b = 1$.</details>
<details><summary>Solución</summary>Rango 2 (los vectores no son múltiplos), luego son independientes y, siendo 2 en $\mathbb{R}^2$, generan: base. $a = 2$, $b = 1$: $(3,1) = 2(1,1) + 1(1,-1)$. Coordenadas: $(2, 1)$.</details>
<details><summary>Errores frecuentes</summary>Confundir las coordenadas $(2,1)$ con el vector $(3,1)$.</details>

### F12-N4-03 · [D] Independencia conservada

**Objetivo**: demostrar con la definición.
**Dificultad**: N4

**Enunciado.** Si $\mathbf{u}, \mathbf{v}$ son independientes, prueba que $\mathbf{u} + \mathbf{v}$ y $\mathbf{u} - \mathbf{v}$ también lo son.

<details><summary>Pista 1</summary>Parte de $c_1(\mathbf{u} + \mathbf{v}) + c_2(\mathbf{u} - \mathbf{v}) = \mathbf{0}$ y reagrupa.</details>
<details><summary>Solución</summary>Reagrupando: $(c_1 + c_2)\mathbf{u} + (c_1 - c_2)\mathbf{v} = \mathbf{0}$. Como $\mathbf{u}, \mathbf{v}$ son independientes, $c_1 + c_2 = 0$ y $c_1 - c_2 = 0$; sumando, $2c_1 = 0$, y restando, $2c_2 = 0$. Luego $c_1 = c_2 = 0$. $\blacksquare$</details>

### F12-N5-01 · [D] Unicidad de las coordenadas

**Objetivo**: usar la independencia para probar unicidad.
**Dificultad**: N5

**Enunciado.** Sea $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ una base de un subespacio $S$. Prueba que todo vector de $S$ se escribe de una **única** manera como combinación lineal de ellos.

<details><summary>Pista 1</summary>La existencia viene de que generan. Para la unicidad, supón dos escrituras y réstalas.</details>
<details><summary>Solución</summary>Existencia: la base genera $S$. Unicidad: si $\mathbf{x} = \sum a_i\mathbf{v}_i = \sum b_i\mathbf{v}_i$, restando, $\sum (a_i - b_i)\mathbf{v}_i = \mathbf{0}$. Por independencia, $a_i - b_i = 0$ para todo $i$, es decir, $a_i = b_i$. $\blacksquare$</details>
