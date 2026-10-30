# F12 — Combinaciones, independencia y base (parte 2)

Segunda parte del banco de las lecciones L43–L44: **27 ejercicios** de práctica que completan la parte 1 (`F12_combinaciones_independencia_base.md`).

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.
- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.
- Reparto: N2: 11, N3: 16 · [C] 20, [K] 7.

---

### F12-N2-11 · [C] ¿Es combinación lineal?

**Objetivo**: decidir pertenencia al espacio generado con un sistema.
**Dificultad**: N2

**Enunciado.** ¿Es $\mathbf{b} = \begin{bmatrix} 13 \\ -2 \\ 4 \end{bmatrix}$ combinación lineal de $\mathbf{u} = \begin{bmatrix} -3 \\ 0 \\ -3 \end{bmatrix}$ y $\mathbf{v} = \begin{bmatrix} -3 \\ 1 \\ 1 \end{bmatrix}$?

<details><summary>Pista 1</summary>Plantea $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$ componente a componente.</details>
<details><summary>Solución</summary>

Hay que resolver $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$. Los rangos son $\operatorname{rg}[\mathbf{u}\ \mathbf{v}] = 2$ y $\operatorname{rg}[\mathbf{u}\ \mathbf{v}\mid\mathbf{b}] = 3$: el sistema es incompatible, $\mathbf{b}$ no es combinación lineal.

</details>
<details><summary>Errores frecuentes</summary>Resolver solo con dos componentes y no comprobar la tercera.</details>

### F12-N2-12 · [C] ¿Es combinación lineal?

**Objetivo**: decidir pertenencia al espacio generado con un sistema.
**Dificultad**: N2

**Enunciado.** ¿Es $\mathbf{b} = \begin{bmatrix} 0 \\ 8 \\ 3 \end{bmatrix}$ combinación lineal de $\mathbf{u} = \begin{bmatrix} -1 \\ -3 \\ -1 \end{bmatrix}$ y $\mathbf{v} = \begin{bmatrix} -3 \\ -1 \\ 0 \end{bmatrix}$?

<details><summary>Pista 1</summary>Plantea $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$ componente a componente.</details>
<details><summary>Solución</summary>

Hay que resolver $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$. Sale $c_1 = -3$, $c_2 = 1$: sí, $\mathbf{b} = (-3)\mathbf{u} + 1\mathbf{v}$.

</details>
<details><summary>Errores frecuentes</summary>Resolver solo con dos componentes y no comprobar la tercera.</details>

### F12-N2-13 · [C] ¿Es combinación lineal?

**Objetivo**: decidir pertenencia al espacio generado con un sistema.
**Dificultad**: N2

**Enunciado.** ¿Es $\mathbf{b} = \begin{bmatrix} -3 \\ -8 \\ -1 \end{bmatrix}$ combinación lineal de $\mathbf{u} = \begin{bmatrix} 0 \\ 3 \\ 0 \end{bmatrix}$ y $\mathbf{v} = \begin{bmatrix} 3 \\ -1 \\ 1 \end{bmatrix}$?

<details><summary>Pista 1</summary>Plantea $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$ componente a componente.</details>
<details><summary>Solución</summary>

Hay que resolver $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$. Sale $c_1 = -3$, $c_2 = -1$: sí, $\mathbf{b} = (-3)\mathbf{u} + (-1)\mathbf{v}$.

</details>
<details><summary>Errores frecuentes</summary>Resolver solo con dos componentes y no comprobar la tercera.</details>

### F12-N2-14 · [C] ¿Es combinación lineal?

**Objetivo**: decidir pertenencia al espacio generado con un sistema.
**Dificultad**: N2

**Enunciado.** ¿Es $\mathbf{b} = \begin{bmatrix} -6 \\ 12 \\ 3 \end{bmatrix}$ combinación lineal de $\mathbf{u} = \begin{bmatrix} 2 \\ -3 \\ 0 \end{bmatrix}$ y $\mathbf{v} = \begin{bmatrix} -1 \\ 2 \\ 1 \end{bmatrix}$?

<details><summary>Pista 1</summary>Plantea $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$ componente a componente.</details>
<details><summary>Solución</summary>

Hay que resolver $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$. Los rangos son $\operatorname{rg}[\mathbf{u}\ \mathbf{v}] = 2$ y $\operatorname{rg}[\mathbf{u}\ \mathbf{v}\mid\mathbf{b}] = 3$: el sistema es incompatible, $\mathbf{b}$ no es combinación lineal.

</details>
<details><summary>Errores frecuentes</summary>Resolver solo con dos componentes y no comprobar la tercera.</details>

### F12-N2-15 · [C] ¿Es combinación lineal?

**Objetivo**: decidir pertenencia al espacio generado con un sistema.
**Dificultad**: N2

**Enunciado.** ¿Es $\mathbf{b} = \begin{bmatrix} 0 \\ 1 \\ -4 \end{bmatrix}$ combinación lineal de $\mathbf{u} = \begin{bmatrix} -1 \\ 2 \\ -1 \end{bmatrix}$ y $\mathbf{v} = \begin{bmatrix} 0 \\ 1 \\ 3 \end{bmatrix}$?

<details><summary>Pista 1</summary>Plantea $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$ componente a componente.</details>
<details><summary>Solución</summary>

Hay que resolver $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$. Los rangos son $\operatorname{rg}[\mathbf{u}\ \mathbf{v}] = 2$ y $\operatorname{rg}[\mathbf{u}\ \mathbf{v}\mid\mathbf{b}] = 3$: el sistema es incompatible, $\mathbf{b}$ no es combinación lineal.

</details>
<details><summary>Errores frecuentes</summary>Resolver solo con dos componentes y no comprobar la tercera.</details>

### F12-N2-16 · [C] ¿Es combinación lineal?

**Objetivo**: decidir pertenencia al espacio generado con un sistema.
**Dificultad**: N2

**Enunciado.** ¿Es $\mathbf{b} = \begin{bmatrix} -6 \\ 6 \\ 0 \end{bmatrix}$ combinación lineal de $\mathbf{u} = \begin{bmatrix} -3 \\ 3 \\ -3 \end{bmatrix}$ y $\mathbf{v} = \begin{bmatrix} 3 \\ -3 \\ -3 \end{bmatrix}$?

<details><summary>Pista 1</summary>Plantea $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$ componente a componente.</details>
<details><summary>Solución</summary>

Hay que resolver $c_1\mathbf{u} + c_2\mathbf{v} = \mathbf{b}$. Sale $c_1 = 1$, $c_2 = -1$: sí, $\mathbf{b} = 1\mathbf{u} + (-1)\mathbf{v}$.

</details>
<details><summary>Errores frecuentes</summary>Resolver solo con dos componentes y no comprobar la tercera.</details>

### F12-N2-17 · [K] ¿Qué es el espacio generado?

**Objetivo**: relacionar el rango con la figura geométrica generada.
**Dificultad**: N2

**Enunciado.** Describe geométricamente el espacio generado por $(0, 1)$ en $\mathbb{R}^2$.

<details><summary>Pista 1</summary>Su dimensión es el rango de la matriz con los vectores por columnas.</details>
<details><summary>Solución</summary>

La matriz con esos vectores por columnas tiene rango 1: el espacio generado es una recta por el origen (dimensión 1).

</details>
<details><summary>Errores frecuentes</summary>Contar los vectores en vez de los independientes.</details>

### F12-N2-18 · [K] ¿Qué es el espacio generado?

**Objetivo**: relacionar el rango con la figura geométrica generada.
**Dificultad**: N2

**Enunciado.** Describe geométricamente el espacio generado por $(0, -2)$ en $\mathbb{R}^2$.

<details><summary>Pista 1</summary>Su dimensión es el rango de la matriz con los vectores por columnas.</details>
<details><summary>Solución</summary>

La matriz con esos vectores por columnas tiene rango 1: el espacio generado es una recta por el origen (dimensión 1).

</details>
<details><summary>Errores frecuentes</summary>Contar los vectores en vez de los independientes.</details>

### F12-N2-19 · [K] ¿Qué es el espacio generado?

**Objetivo**: relacionar el rango con la figura geométrica generada.
**Dificultad**: N2

**Enunciado.** Describe geométricamente el espacio generado por $(-1, 2, 2)$ en $\mathbb{R}^3$.

<details><summary>Pista 1</summary>Su dimensión es el rango de la matriz con los vectores por columnas.</details>
<details><summary>Solución</summary>

La matriz con esos vectores por columnas tiene rango 1: el espacio generado es una recta por el origen (dimensión 1).

</details>
<details><summary>Errores frecuentes</summary>Contar los vectores en vez de los independientes.</details>

### F12-N2-20 · [K] ¿Qué es el espacio generado?

**Objetivo**: relacionar el rango con la figura geométrica generada.
**Dificultad**: N2

**Enunciado.** Describe geométricamente el espacio generado por $(2, -2, 0)$, $(4, -4, 0)$ en $\mathbb{R}^3$.

<details><summary>Pista 1</summary>Su dimensión es el rango de la matriz con los vectores por columnas.</details>
<details><summary>Solución</summary>

La matriz con esos vectores por columnas tiene rango 1: el espacio generado es una recta por el origen (dimensión 1).

</details>
<details><summary>Errores frecuentes</summary>Contar los vectores en vez de los independientes.</details>

### F12-N2-21 · [K] ¿Qué es el espacio generado?

**Objetivo**: relacionar el rango con la figura geométrica generada.
**Dificultad**: N2

**Enunciado.** Describe geométricamente el espacio generado por $(-1, -2, -2)$ en $\mathbb{R}^3$.

<details><summary>Pista 1</summary>Su dimensión es el rango de la matriz con los vectores por columnas.</details>
<details><summary>Solución</summary>

La matriz con esos vectores por columnas tiene rango 1: el espacio generado es una recta por el origen (dimensión 1).

</details>
<details><summary>Errores frecuentes</summary>Contar los vectores en vez de los independientes.</details>

### F12-N3-11 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (-3, -3, 1, 0)$, $\mathbf{v}_2 = (3, 1, 0, 1)$, $\mathbf{v}_3 = (1, 2, -1, 3)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 3$ y hay $k = 3$ vectores. El rango es igual al número de vectores: son **independientes**.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-12 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (1, 3, 1, -1)$, $\mathbf{v}_2 = (0, 3, 0, -3)$, $\mathbf{v}_3 = (-2, 0, -2, -3)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 3$ y hay $k = 3$ vectores. El rango es igual al número de vectores: son **independientes**.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-13 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (1, 1, -2, 2)$, $\mathbf{v}_2 = (0, -3, 2, 1)$, $\mathbf{v}_3 = (-1, 5, -2, -4)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 2$ y hay $k = 3$ vectores. El rango es menor que 3: son **dependientes**. Una relación: $1\mathbf{v}_1 + 2\mathbf{v}_2 + 1\mathbf{v}_3 = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-14 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (0, 2, -1)$, $\mathbf{v}_2 = (0, -1, 3)$, $\mathbf{v}_3 = (0, 6, -8)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 2$ y hay $k = 3$ vectores. El rango es menor que 3: son **dependientes**. Una relación: $(-2)\mathbf{v}_1 + 2\mathbf{v}_2 + 1\mathbf{v}_3 = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-15 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (1, -4, -6)$, $\mathbf{v}_2 = (2, -2, -3)$, $\mathbf{v}_3 = (1, 2, 3)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 2$ y hay $k = 3$ vectores. El rango es menor que 3: son **dependientes**. Una relación: $1\mathbf{v}_1 + (-1)\mathbf{v}_2 + 1\mathbf{v}_3 = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-16 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (4, 2, -12)$, $\mathbf{v}_2 = (-1, 0, 3)$, $\mathbf{v}_3 = (1, 1, -3)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 2$ y hay $k = 3$ vectores. El rango es menor que 3: son **dependientes**. Una relación: $(-\frac{1}{2})\mathbf{v}_1 + (-1)\mathbf{v}_2 + 1\mathbf{v}_3 = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-17 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (2, 2, 1, 3)$, $\mathbf{v}_2 = (0, 0, 2, 3)$, $\mathbf{v}_3 = (2, 2, -1, 0)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 2$ y hay $k = 3$ vectores. El rango es menor que 3: son **dependientes**. Una relación: $(-1)\mathbf{v}_1 + 1\mathbf{v}_2 + 1\mathbf{v}_3 = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-18 · [C] Independencia lineal

**Objetivo**: decidir con el rango y, si es dependiente, dar una relación.
**Dificultad**: N3

**Enunciado.** ¿Son linealmente independientes $\mathbf{v}_1 = (2, 2, -2)$, $\mathbf{v}_2 = (2, 3, -3)$, $\mathbf{v}_3 = (-2, 3, -1)$, $\mathbf{v}_4 = (2, -1, 2)$? Si no, da una relación entre ellos.

<details><summary>Pista 1</summary>Forma la matriz con los vectores por columnas y escalónala.</details>
<details><summary>Solución</summary>

Con los vectores por columnas, $\operatorname{rg}(V) = 3$ y hay $k = 4$ vectores. El rango es menor que 4: son **dependientes**. Una relación: $(-7)\mathbf{v}_1 + (\frac{11}{2})\mathbf{v}_2 + (-\frac{1}{2})\mathbf{v}_3 + 1\mathbf{v}_4 = \mathbf{0}$.

</details>
<details><summary>Errores frecuentes</summary>Creer que basta que ningún par sea proporcional.</details>

### F12-N3-19 · [C] Base del espacio generado

**Objetivo**: extraer una base con las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} 2 & -5 & 6 & -2 \\ -4 & -8 & 3 & 7 \\ 3 & 0 & 4 & 2 \\ 0 & 0 & -1 & -5 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Solución</summary>

La reducida tiene pivotes en las columnas 1, 2, 3. Una base son las columnas de $A$ (la original): $(2, -4, 3, 0)$, $(-5, -8, 0, 0)$, $(6, 3, 4, -1)$. Dimensión: 3.

</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la matriz reducida.</details>

### F12-N3-20 · [C] Base del espacio generado

**Objetivo**: extraer una base con las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} -2 & -4 & -4 & -2 & -4 \\ 0 & 6 & 6 & 6 & 8 \\ 0 & 3 & 3 & 3 & 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Solución</summary>

La reducida tiene pivotes en las columnas 1, 2. Una base son las columnas de $A$ (la original): $(-2, 0, 0)$, $(-4, 6, 3)$. Dimensión: 2.

</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la matriz reducida.</details>

### F12-N3-21 · [C] Base del espacio generado

**Objetivo**: extraer una base con las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} -2 & 6 & 3 & 4 \\ 0 & -3 & -1 & -2 \\ -6 & 6 & 5 & 4 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Solución</summary>

La reducida tiene pivotes en las columnas 1, 2. Una base son las columnas de $A$ (la original): $(-2, 0, -6)$, $(6, -3, 6)$. Dimensión: 2.

</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la matriz reducida.</details>

### F12-N3-22 · [C] Base del espacio generado

**Objetivo**: extraer una base con las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} -2 & 4 & -6 & 4 \\ -4 & -7 & 3 & -7 \\ 0 & -2 & -9 & -2 \\ -8 & -3 & 3 & -3 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Solución</summary>

La reducida tiene pivotes en las columnas 1, 2, 3. Una base son las columnas de $A$ (la original): $(-2, -4, 0, -8)$, $(4, -7, -2, -3)$, $(-6, 3, -9, 3)$. Dimensión: 3.

</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la matriz reducida.</details>

### F12-N3-23 · [C] Base del espacio generado

**Objetivo**: extraer una base con las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} 2 & -1 & 2 & 0 \\ -1 & -2 & -1 & -1 \\ -4 & -3 & -4 & -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Solución</summary>

La reducida tiene pivotes en las columnas 1, 2. Una base son las columnas de $A$ (la original): $(2, -1, -4)$, $(-1, -2, -3)$. Dimensión: 2.

</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la matriz reducida.</details>

### F12-N3-24 · [C] Base del espacio generado

**Objetivo**: extraer una base con las columnas pivote de la matriz original.
**Dificultad**: N3

**Enunciado.** Halla una base y la dimensión del espacio generado por las columnas de $A = \begin{bmatrix} 1 & 0 & 1 & -6 \\ -6 & -9 & 3 & 0 \\ -1 & -3 & 2 & -6 \\ 3 & 4 & -1 & -2 \end{bmatrix}$.

<details><summary>Pista 1</summary>Reduce $A$ y mira dónde están los pivotes.</details>
<details><summary>Solución</summary>

La reducida tiene pivotes en las columnas 1, 2. Una base son las columnas de $A$ (la original): $(1, -6, -1, 3)$, $(0, -9, -3, 4)$. Dimensión: 2.

</details>
<details><summary>Errores frecuentes</summary>Tomar las columnas de la matriz reducida.</details>

### F12-N3-25 · [K] Preguntas de base y dimensión

**Objetivo**: razonar con rangos sobre independencia y generadores.
**Dificultad**: N3

**Enunciado.** a) ¿Pueden cuatro vectores de $\mathbb{R}^3$ ser linealmente independientes?

b) ¿Cuántos vectores tiene cualquier base de $\mathbb{R}^3$?

<details><summary>Pista 1</summary>Piensa en el rango de la matriz que forman los vectores.</details>
<details><summary>Solución</summary>

a) No: el rango de una matriz $3 \times 4$ es a lo sumo $3 < 4$.

b) Tres: todas las bases tienen el mismo número de vectores, la dimensión $3$.

</details>
<details><summary>Errores frecuentes</summary>Confundir independencia con generar.</details>

### F12-N3-26 · [K] Preguntas de base y dimensión

**Objetivo**: razonar con rangos sobre independencia y generadores.
**Dificultad**: N3

**Enunciado.** a) ¿Puede un conjunto linealmente independiente contener al vector nulo?

b) ¿Genera $\mathbb{R}^3$ un conjunto de dos vectores?

<details><summary>Pista 1</summary>Piensa en el rango de la matriz que forman los vectores.</details>
<details><summary>Solución</summary>

a) No: $1\cdot\mathbf{0} = \mathbf{0}$ es una combinación no trivial.

b) No: el rango de una matriz $3 \times 2$ es a lo sumo $2 < 3$.

</details>
<details><summary>Errores frecuentes</summary>Confundir independencia con generar.</details>

