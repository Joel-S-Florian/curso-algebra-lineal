# Formulario de conceptos y teoremas

Resumen de todo el curso en una sola página de consulta. Entre paréntesis, la lección donde se explica (L00–L55). Notación: $A$ es una matriz $m \times n$ ($m$ ecuaciones, $n$ incógnitas), $\mathbf{x} \in \mathbb{R}^n$, $\mathbf{b} \in \mathbb{R}^m$.

---

## 1. Ecuaciones lineales (L05–L07)

- **Ecuación lineal** en $x_1,\dots,x_n$: $a_1x_1 + \dots + a_nx_n = b$ (cada término es un número o un número por una incógnita elevada a $1$).
- **Una incógnita**, $ax = b$: si $a \ne 0$, $x = b/a$; si $a = 0$ y $b \ne 0$, sin solución; si $a = 0$ y $b = 0$, todo $x$ sirve.
- **Geometría**: una ecuación con 2 incógnitas es una recta; con 3, un plano; con $n$, un hiperplano. El conjunto solución tiene $n - 1$ parámetros libres.
- **Comprobar** una solución = sustituirla en el sistema **original**.

## 2. Sistemas y clasificación (L08–L12)

- **Sistema lineal** $m \times n$: $m$ ecuaciones, $n$ incógnitas. **Solución**: valores que cumplen todas las ecuaciones a la vez.
- **Compatible determinado (SCD)**: una solución. **Compatible indeterminado (SCI)**: infinitas. **Incompatible (SI)**: ninguna. Nunca hay exactamente $2$ (L54).
- **Geometría $2\times 2$**: rectas secantes (SCD), paralelas (SI), coincidentes (SCI). **$3\times 3$**: tres planos que se cortan en un punto, en una recta, o sin punto común.
- **Homogéneo** ($\mathbf{b} = \mathbf{0}$): siempre compatible; si $m < n$ tiene infinitas soluciones.

## 3. Métodos elementales (L13–L15)

- **Sustitución**: despejar una incógnita y sustituirla. **Igualación**: despejar la misma en dos ecuaciones e igualar. **Reducción**: combinar ecuaciones para eliminar una incógnita.
- Todos dan las mismas soluciones; sirven a mano con 2–3 incógnitas.

## 4. Matrices y vectores (L16–L21)

- **Suma y escalar**: entrada a entrada, mismo tamaño. $(A + B)^T = A^T + B^T$, $(cA)^T = cA^T$.
- **Producto** $AB$ ($m\times n$ por $n\times p$ da $m\times p$): entrada $(i,j)$ = fila $i$ de $A$ por columna $j$ de $B$. **No conmuta**; $(AB)^T = B^TA^T$; $AB = 0$ no implica $A = 0$ ni $B = 0$.
- **Producto matriz-vector**: $A\mathbf{x} = x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n$ (combinación de las columnas).
- **Transformación** $T(\mathbf{x}) = A\mathbf{x}$: las columnas de $A$ son las imágenes de $\mathbf{e}_1,\dots,\mathbf{e}_n$. Composición $T \circ S$: matriz $BA$ (primero $S$).
- Matrices especiales: identidad $I$, diagonal, triangular superior/inferior, simétrica ($A = A^T$).

## 5. Forma matricial (L22–L23)

- Sistema $\iff A\mathbf{x} = \mathbf{b}$. **Matriz aumentada** $[A \mid \mathbf{b}]$: tamaño $m \times (n+1)$.
- $A\mathbf{x} = \mathbf{b}$ tiene solución $\iff \mathbf{b}$ es combinación lineal de las columnas de $A$.

## 6. Eliminación (L24–L33)

- **Operaciones elementales por filas**: $R_i \leftrightarrow R_j$; $R_i \leftarrow cR_i$ ($c \ne 0$); $R_i \leftarrow R_i + cR_j$. Son reversibles y **no cambian el conjunto solución** (L54).
- **Escalonada**: pivotes en escalera, filas nulas abajo. **Reducida (Gauss-Jordan)**: además pivotes $= 1$ y ceros arriba y abajo; es **única**.
- **Gauss**: escalonar y sustituir hacia atrás. Coste $\approx \frac{n^3 + 3n^2 - n}{3}$ multiplicaciones y divisiones. **Gauss-Jordan**: $\frac{n^3 + n^2}{2}$.
- **Pivote nulo**: intercambiar con una fila inferior. **Fila** $[0\ \dots\ 0 \mid c]$ con $c \ne 0$: incompatible. Fila de ceros: ecuación redundante.
- **Variables básicas** (columnas con pivote) y **libres** (sin pivote). Con $r$ pivotes hay $n - r$ parámetros.
- **Con parámetros**: estudiar por separado los valores que anulan un pivote (determinante).

## 7. Factorización LU (L34–L38)

- $A = LU$: $L$ triangular inferior con unos en la diagonal (guarda los multiplicadores $\ell_{ik} = a_{ik}/a_{kk}$ de la eliminación), $U$ la escalonada.
- **Resolver** $A\mathbf{x} = \mathbf{b}$: $L\mathbf{y} = \mathbf{b}$ (hacia adelante), $U\mathbf{x} = \mathbf{y}$ (hacia atrás).
- **$PA = LU$**: con pivoteo parcial (intercambios) cuando falla $A = LU$; siempre existe si $A$ es invertible.
- **Coste**: factorizar $\frac{n^3 - n}{3}$ (una vez); cada $\mathbf{b}$, $n^2$. Conviene con la misma $A$ y muchos $\mathbf{b}$.
- $A = LU$ es **única** (A invertible) con $L$ unitaria (L54).

## 8. Rango y clasificación (L39–L42)

- **Rango** $\operatorname{rg}(A)$ = número de pivotes de una escalonada = número de ecuaciones independientes. $\operatorname{rg}(A) \le \min(m,n)$; $\operatorname{rg}(A) = \operatorname{rg}(A^T)$.
- $\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1$.
- **Rouché-Frobenius**: $A\mathbf{x} = \mathbf{b}$ es compatible $\iff \operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$. Entonces: $\operatorname{rg} = n \Rightarrow$ SCD; $\operatorname{rg} < n \Rightarrow$ SCI con $n - \operatorname{rg}$ parámetros.

| $\operatorname{rg}(A)$ vs $\operatorname{rg}[A \mid \mathbf{b}]$ vs $n$ | Clasificación |
|---|---|
| $\operatorname{rg}(A) < \operatorname{rg}[A \mid \mathbf{b}]$ | SI |
| $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = n$ | SCD |
| $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] < n$ | SCI |

## 9. Combinaciones, independencia, base (L43–L44)

- **Combinación lineal**: $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k$. **Espacio generado** $\operatorname{gen}\{\mathbf{v}_i\}$: todas las combinaciones (recta, plano, …; contiene a $\mathbf{0}$).
- $\mathbf{b} \in \operatorname{gen}\{\mathbf{v}_i\} \iff [\mathbf{v}_1\cdots\mathbf{v}_k \mid \mathbf{b}]$ compatible.
- **Independientes**: $\sum c_i\mathbf{v}_i = \mathbf{0} \Rightarrow$ todos $c_i = 0$ $\iff \operatorname{rg}[\mathbf{v}_1\cdots\mathbf{v}_k] = k$. Con $\mathbf{0}$, o más de $n$ vectores en $\mathbb{R}^n$: dependientes.
- **Base**: independiente + generadora; las coordenadas son únicas. **Dimensión** = número de vectores de cualquier base ($\dim\mathbb{R}^n = n$).

## 10. Núcleo (L45–L47)

- $\ker A = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$, subespacio de $\mathbb{R}^n$. **Base**: un vector por variable libre (esa libre $=1$, las demás $=0$). **Nulidad** $\operatorname{nul}(A) = \dim\ker A = n - \operatorname{rg}(A)$.
- $\ker A = \{\mathbf{0}\} \iff$ columnas independientes $\iff \operatorname{rg}(A) = n$.
- **Estructura**: si $A\mathbf{x}_p = \mathbf{b}$, las soluciones son $\mathbf{x}_p + \ker A$ (el núcleo trasladado; no es subespacio si $\mathbf{b} \ne \mathbf{0}$).

## 11. Espacio columna e imagen (L48–L50)

- $\operatorname{Col}(A) = \operatorname{gen}\{\mathbf{a}_1,\dots,\mathbf{a}_n\} = \{A\mathbf{x}\} \subseteq \mathbb{R}^m$ = imagen de $T(\mathbf{x}) = A\mathbf{x}$.
- $A\mathbf{x} = \mathbf{b}$ tiene solución $\iff \mathbf{b} \in \operatorname{Col}(A)$. Tiene solución para todo $\mathbf{b} \iff \operatorname{rg}(A) = m$.
- **Base de $\operatorname{Col}(A)$**: las columnas de la matriz **original** con pivote; $\dim\operatorname{Col}(A) = \operatorname{rg}(A)$. (Las operaciones por filas cambian $\operatorname{Col}(A)$ pero conservan $\ker A$.)
- **Rango y nulidad**: $\operatorname{rg}(A) + \operatorname{nul}(A) = n$.
- **Cuadrada** $n \times n$: $\operatorname{rg}(A) = n \iff \ker A = \{\mathbf{0}\} \iff \operatorname{Col}(A) = \mathbb{R}^n \iff A\mathbf{x} = \mathbf{b}$ tiene solución única para todo $\mathbf{b}$.

## 12. Errores que más se repiten

- Aplicar una operación a los coeficientes y no a la columna de $\mathbf{b}$.
- Dividir por una expresión con parámetro sin estudiar el caso en que vale cero.
- Contar ecuaciones en lugar de pivotes (el rango no es el número de ecuaciones).
- Tomar las columnas de la **reducida** como base de $\operatorname{Col}(A)$.
- Confundir $\ker A \subseteq \mathbb{R}^n$ con $\operatorname{Col}(A) \subseteq \mathbb{R}^m$.
- Dar solo el núcleo como solución de $A\mathbf{x} = \mathbf{b}$ ($\mathbf{b} \ne \mathbf{0}$): falta $\mathbf{x}_p$.
- No verificar en el sistema original.
