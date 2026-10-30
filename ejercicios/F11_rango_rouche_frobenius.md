# F11 — Rango y teorema de Rouché-Frobenius

Banco de las lecciones L39–L42. **Parte 1: 16 ejercicios**, ligados a los videos. La **parte 2** (34 ejercicios de práctica, generados y comprobados con aritmética exacta) está en `F11_rango_rouche_frobenius_parte2.md`; la familia completa suma **50**.

- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración · 🎬 = aparece en un video.
- Notación: $\operatorname{rg}(A)$ es el rango (número de pivotes); $[A \mid \mathbf{b}]$ la matriz aumentada; $n$ el número de incógnitas.
- Resultados comprobados con fracciones exactas en `ejercicios/verificar/f11.py`.

| Lección | Ejercicios |
|---|---|
| L39 El rango | N1-01, N2-01 🎬, N2-02 🎬, N3-01 🎬, N3-03 |
| L40 Rouché-Frobenius | N2-03 🎬, N3-02 🎬, N3-06, N4-01, N4-02 🎬 |
| L41 Clasificación con ejemplos | N2-04 🎬, N3-04 🎬 |
| L42 Discusión con parámetros | N3-05 🎬, N4-05 🎬, N4-06, N5-01 |

---

### F11-N1-01 · [C] Leer el rango en la reducida

**Objetivo**: contar pivotes.
**Dificultad**: N1

**Enunciado.** Da el rango de: a) $\begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{bmatrix}$; b) $\begin{bmatrix} 0 & 1 & 0 & 5 \\ 0 & 0 & 1 & 6 \end{bmatrix}$; c) la matriz nula $2\times 3$; d) $I_3$.

<details><summary>Pista 1</summary>Cuenta las filas no nulas de la forma escalonada.</details>
<details><summary>Pista 2</summary>Ya están escalonadas: no hay que operar.</details>
<details><summary>Solución</summary>a) 2; b) 2 (los pivotes están en las columnas 2 y 3); c) 0; d) 3.</details>
<details><summary>Errores frecuentes</summary>Contar las columnas con algún elemento no nulo (b tiene tres, pero solo dos pivotes).</details>

### F11-N2-01 · [C] Rango escalonando 🎬

**Objetivo**: calcular el rango y la reducida.
**Dificultad**: N2

**Enunciado.** Calcula el rango de $A = \begin{bmatrix} 1 & 3 & 2 \\ 2 & 6 & 5 \\ 1 & 3 & 3 \end{bmatrix}$ y su forma reducida.

<details><summary>Pista 1</summary>Haz ceros debajo del primer pivote.</details>
<details><summary>Pista 2</summary>Tras eso, las filas 2 y 3 son iguales.</details>
<details><summary>Solución</summary>

$R_2 \leftarrow R_2 - 2R_1 = [0, 0, 1]$, $R_3 \leftarrow R_3 - R_1 = [0, 0, 1]$, $R_3 \leftarrow R_3 - R_2 = [0, 0, 0]$. Escalonada $\begin{bmatrix} 1 & 3 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$, **rango 2**; reducida $\begin{bmatrix} 1 & 3 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$ (pivotes en las columnas 1 y 3).
</details>
<details><summary>Errores frecuentes</summary>Esperar un pivote en la columna 2: el pivote de la fila 2 está en la columna 3.</details>

### F11-N2-02 · [C] Los dos rangos 🎬

**Objetivo**: $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$.
**Dificultad**: N2

**Enunciado.** Halla $\operatorname{rg}(A)$ y $\operatorname{rg}[A \mid \mathbf{b}]$ de $\left[\begin{array}{ccc|c} 1 & 2 & 1 & 4 \\ 2 & 4 & 2 & 7 \\ 1 & 1 & 3 & 5 \end{array}\right]$ y di qué indican.

<details><summary>Pista 1</summary>$R_2 \leftarrow R_2 - 2R_1$ da una fila con un número solo en la última columna.</details>
<details><summary>Pista 2</summary>Compara los dos rangos.</details>
<details><summary>Solución</summary>

$R_2 \leftarrow R_2 - 2R_1 = [0, 0, 0 \mid -1]$ y $R_3 \leftarrow R_3 - R_1 = [0, -1, 2 \mid 1]$. Sin contar la última columna hay 2 pivotes; con ella, 3. $\operatorname{rg}(A) = 2 \ne 3 = \operatorname{rg}[A \mid \mathbf{b}]$: el sistema es **incompatible** (la fila $[0\ 0\ 0 \mid -1]$ dice $0 = -1$).
</details>
<details><summary>Errores frecuentes</summary>Calcular un solo rango.</details>

### F11-N3-01 · [C] El rango no es el número de ecuaciones 🎬

**Objetivo**: detectar ecuaciones que sobran.
**Dificultad**: N3

**Enunciado.** Sin resolver, halla el rango de la matriz aumentada de $\;x + y + z = 1,\ 2x + 2y + 2z = 2,\ x - y = 0,\ 3x + y + 2z = 2$ y di qué ecuaciones sobran.

<details><summary>Pista 1</summary>Compara la segunda con la primera.</details>
<details><summary>Pista 2</summary>¿Es la cuarta combinación de la primera y la tercera?</details>
<details><summary>Solución</summary>

$E_2 = 2E_1$ y $E_4 = 2E_1 + E_3$ (coeficientes $(3, 1, 2)$ y término independiente $2$ ✓). Quedan dos ecuaciones independientes: **rango 2** (tanto de $A$ como de la aumentada). Sobran $E_2$ y $E_4$.
</details>
<details><summary>Errores frecuentes</summary>Decir que el rango es 4 por haber 4 ecuaciones.</details>

### F11-N3-03 · [D] Cotas del rango

**Objetivo**: demostrar $\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1$.
**Dificultad**: N3

**Enunciado.** Demuestra las dos desigualdades.

<details><summary>Pista 1</summary>Escalona $[A \mid \mathbf{b}]$: las operaciones por filas dejan escalonada también $A$.</details>
<details><summary>Pista 2</summary>¿Cuántos pivotes puede haber en la última columna?</details>
<details><summary>Solución</summary>

Al escalonar $[A \mid \mathbf{b}]$ con operaciones por filas, las $n$ primeras columnas quedan escalonadas, así que los pivotes de $A$ también lo son de $[A \mid \mathbf{b}]$: $\operatorname{rg}(A) \le \operatorname{rg}[A \mid \mathbf{b}]$. Además, la columna $\mathbf{b}$ contiene como mucho **un** pivote (hay a lo sumo un pivote por columna): $\operatorname{rg}[A \mid \mathbf{b}] \le \operatorname{rg}(A) + 1$. $\blacksquare$
</details>
<details><summary>Errores frecuentes</summary>Olvidar que los pivotes de $A$ no cambian al añadir la columna $\mathbf{b}$.</details>

### F11-N2-03 · [C] Clasificar con Rouché-Frobenius 🎬

**Objetivo**: aplicar el teorema y resolver.
**Dificultad**: N2

**Enunciado.** Clasifica y resuelve $\;x + 2y + z = 4,\ 2x + 4y + 3z = 9,\ 3x + 6y + 4z = 13$.

<details><summary>Pista 1</summary>Reduce $[A \mid \mathbf{b}]$ y cuenta pivotes dentro y fuera de la columna $\mathbf{b}$.</details>
<details><summary>Pista 2</summary>La columna de $y$ no tiene pivote.</details>
<details><summary>Solución</summary>

Reducida $\left[\begin{array}{ccc|c} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$: $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 2 < 3 = n$: **SCI**, con $3 - 2 = 1$ parámetro. Con $y = t$: $(x, y, z) = (3 - 2t,\ t,\ 1)$.

**Verificación**: $2(3 - 2t) + 4t + 3 = 9$ ✓ y $3(3 - 2t) + 6t + 4 = 13$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Contar tres pivotes por haber tres ecuaciones.</details>

### F11-N3-02 · [D] Rangos distintos ⇒ incompatible 🎬

**Objetivo**: demostrar un sentido del teorema.
**Dificultad**: N3

**Enunciado.** Demuestra con la forma escalonada que, si $\operatorname{rg}(A) < \operatorname{rg}[A \mid \mathbf{b}]$, el sistema es incompatible.

<details><summary>Pista 1</summary>Si los rangos difieren, el pivote extra está en la columna de $\mathbf{b}$.</details>
<details><summary>Pista 2</summary>¿Qué ecuación representa esa fila?</details>
<details><summary>Solución</summary>

Los pivotes de $A$ también lo son de $[A \mid \mathbf{b}]$, luego un rango mayor exige un pivote en la columna $\mathbf{b}$: una fila $[\,0\ \cdots\ 0 \mid c\,]$ con $c \ne 0$, es decir, la ecuación $0 = c$, imposible. Como las operaciones por filas conservan las soluciones, el sistema original tampoco tiene ninguna. $\blacksquare$
</details>
<details><summary>Errores frecuentes</summary>No justificar que las operaciones conservan las soluciones.</details>

### F11-N3-06 · [K] Sistemas homogéneos

**Objetivo**: aplicar el teorema a $\mathbf{b} = \mathbf{0}$.
**Dificultad**: N3

**Enunciado.** Demuestra que un sistema homogéneo es siempre compatible y que tiene solo la solución trivial si y solo si $\operatorname{rg}(A) = n$. Aplícalo a $\;x + 2y = 0,\ 2x + 4y = 0$.

<details><summary>Pista 1</summary>Añadir una columna de ceros, ¿cambia el rango?</details>
<details><summary>Pista 2</summary>Usa $n - r$ parámetros.</details>
<details><summary>Solución</summary>

$\operatorname{rg}[A \mid \mathbf{0}] = \operatorname{rg}(A)$ (una columna de ceros no tiene pivote): compatible. Entonces la solución es única (la trivial) si y solo si $r = n$; si $r < n$ hay $n - r$ parámetros. En el ejemplo $r = 1 < 2$: soluciones $(-2t, t)$, infinitas.
</details>
<details><summary>Errores frecuentes</summary>Pensar que un homogéneo con $m < n$ puede ser incompatible.</details>

### F11-N4-01 · [D] Rangos iguales ⇒ compatible

**Objetivo**: demostrar el otro sentido, construyendo una solución.
**Dificultad**: N4

**Enunciado.** Demuestra que, si $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$, el sistema tiene solución.

<details><summary>Pista 1</summary>Mira la forma reducida de $[A \mid \mathbf{b}]$: ¿hay pivote en la última columna?</details>
<details><summary>Pista 2</summary>Da el valor $0$ a las variables libres y lee las básicas.</details>
<details><summary>Solución</summary>

Con rangos iguales no hay pivote en la columna $\mathbf{b}$, así que ninguna fila es $[\,0\ \cdots\ 0 \mid c\,]$ con $c \ne 0$. En la reducida, cada fila con pivote en la columna $j_i$ dice $x_{j_i} + (\text{libres}) = c_i$. Poniendo todas las libres a $0$ y $x_{j_i} = c_i$, cada ecuación se cumple (las filas nulas dicen $0 = 0$). Es una solución del sistema reducido y, por equivalencia, del original. $\blacksquare$
</details>
<details><summary>Errores frecuentes</summary>Olvidar que las filas nulas son $0 = 0$ solo si su término independiente también es $0$.</details>

### F11-N4-02 · [C] Contar parámetros 🎬

**Objetivo**: $n - r$.
**Dificultad**: N4

**Enunciado.** Un sistema tiene 4 ecuaciones y 5 incógnitas, con $\operatorname{rg}(A) = 3$. ¿Cuántos parámetros tiene la solución si es compatible? ¿Qué pasa si $\operatorname{rg}[A \mid \mathbf{b}] = 4$?

<details><summary>Pista 1</summary>Parámetros $= n - r$.</details>
<details><summary>Pista 2</summary>Compara los dos rangos.</details>
<details><summary>Solución</summary>

Compatible implica $\operatorname{rg}[A \mid \mathbf{b}] = 3$ y $5 - 3 = 2$ parámetros (SCI). Si $\operatorname{rg}[A \mid \mathbf{b}] = 4 \ne 3$, es **incompatible**.
</details>
<details><summary>Errores frecuentes</summary>Restar al número de ecuaciones en lugar de al rango.</details>

### F11-N2-04 · [C] Tres clasificaciones 🎬

**Objetivo**: clasificar con rangos y resolver.
**Dificultad**: N2

**Enunciado.** Clasifica y, si es compatible, resuelve: a) $\;x + 2y - z = 1,\ 2x + 4y - 2z = 2$; b) $\;x + 2y = 3,\ 2x + 4y = 7$; c) $\;x + y = 1,\ x - y = 3,\ 2x + y = 3$.

<details><summary>Pista 1</summary>En a) y b) la segunda fila es casi el doble de la primera.</details>
<details><summary>Pista 2</summary>En c) resuelve con dos ecuaciones y comprueba la tercera.</details>
<details><summary>Solución</summary>

a) $\operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}] = 1 < 3$: **SCI**, $2$ parámetros: $(1 - 2s + t,\ s,\ t)$. b) $\operatorname{rg}(A) = 1 \ne 2 = \operatorname{rg}[A \mid \mathbf{b}]$ ($2\cdot 3 = 6 \ne 7$): **SI**. c) $\operatorname{rg} = 2 = n$ en $A$ y en la aumentada: **SCD**, $(2, -1)$ ($4 - 1 = 3$ ✓).
</details>
<details><summary>Errores frecuentes</summary>En b) concluir SCI por tener una ecuación proporcional: los términos independientes también tienen que serlo.</details>

### F11-N3-04 · [K] Posibilidades según la forma 🎬

**Objetivo**: usar el rango para acotar las clasificaciones.
**Dificultad**: N3

**Enunciado.** ¿Qué clasificaciones (SCD, SCI, SI) son posibles en un sistema de 3 ecuaciones con 5 incógnitas? ¿Y en uno de 5 ecuaciones con 3 incógnitas? Da un ejemplo de cada posibilidad.

<details><summary>Pista 1</summary>$r \le \min(m, n)$.</details>
<details><summary>Pista 2</summary>Para SCD hace falta $r = n$.</details>
<details><summary>Solución</summary>

$3 \times 5$: $r \le 3 < 5$, así que **nunca SCD**; posibles SCI (p. ej. una ecuación repetida y homogéneas) y SI (p. ej. $x + y = 1$ y $x + y = 3$). $5 \times 3$: **los tres**: SCD (tres ecuaciones independientes más dos combinaciones de ellas), SCI (cinco veces la misma ecuación $x + y + z = 1$) y SI (por ejemplo $x = 1$ y $x = 2$ entre las cinco).
</details>
<details><summary>Errores frecuentes</summary>Creer que con más ecuaciones que incógnitas siempre hay una única solución.</details>

### F11-N3-05 · [C] Discutir con un parámetro 🎬

**Objetivo**: clasificar según $m$ con los rangos.
**Dificultad**: N3

**Enunciado.** Discute según $m$: $\;mx + y = 1,\ \ x + my = m$.

<details><summary>Pista 1</summary>El coeficiente $m^2 - 1$ aparece al escalonar.</details>
<details><summary>Pista 2</summary>Estudia por separado $m = 1$ y $m = -1$.</details>
<details><summary>Solución</summary>

Intercambia las filas (así no se divide entre $m$) y haz $R_2 \leftarrow R_2 - mR_1$: $\left[\begin{array}{cc|c} 1 & m & m \\ 0 & 1 - m^2 & 1 - m^2 \end{array}\right]$. Si $m^2 \ne 1$: $1 - m^2$ es pivote, $\operatorname{rg}(A) = 2 = n$: **SCD**. Si $m = 1$ o $m = -1$: la segunda fila es $[\,0\ 0 \mid 0\,]$, $\operatorname{rg} = 1 < 2$ y **SCI** (en $m = 1$: $x + y = 1$; en $m = -1$: $-x + y = 1$). Nunca es SI.
</details>
<details><summary>Errores frecuentes</summary>Dividir por $m$ sin estudiar $m = 0$; concluir SI en $m = -1$ por ver signos opuestos.</details>

### F11-N4-05 · [C] Parámetro en el término independiente 🎬

**Objetivo**: discutir y resolver.
**Dificultad**: N4

**Enunciado.** Discute según $k$ y resuelve cuando sea compatible: $\;x + y + z = 1,\ x + 2y + 3z = 2,\ x + 3y + 5z = k$. Variante: con $m$ en lugar del $2$ del segundo término independiente, discute según $k$ y $m$.

<details><summary>Pista 1</summary>$R_3 \leftarrow R_3 - R_1 - 2(R_2 - R_1)$ deja una fila $[\,0\ 0\ 0 \mid \cdot\,]$.</details>
<details><summary>Pista 2</summary>Para la variante, el valor crítico depende de $m$.</details>
<details><summary>Solución</summary>

$[\,0\ 0\ 0 \mid k - 3\,]$: $k = 3$ es **SCI** ($1$ parámetro): $(t,\ 1 - 2t,\ t)$; $k \ne 3$ es **SI**. Nunca SCD ($\operatorname{rg}(A) = 2 < 3$). Variante: la última fila es $[\,0\ 0\ 0 \mid k - 2m + 1\,]$: SCI si $k = 2m - 1$, SI en otro caso.

**Verificación** ($k = 3$): $t + 3(1 - 2t) + 5t = 3$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Decir que hay un caso SCD por ser $3 \times 3$.</details>

### F11-N4-06 · [C] Dos parámetros

**Objetivo**: discutir en $a$ y $b$.
**Dificultad**: N4

**Enunciado.** Discute según $a$ y $b$: $\;x + y = 1,\ \ x + ay = b$, y resuelve cuando sea SCD.

<details><summary>Pista 1</summary>$R_2 \leftarrow R_2 - R_1 = [\,0\ \ a - 1 \mid b - 1\,]$.</details>
<details><summary>Pista 2</summary>Estudia $a \ne 1$ y $a = 1$.</details>
<details><summary>Solución</summary>

$a \ne 1$: **SCD** para todo $b$, con $x = \frac{a - b}{a - 1}$, $y = \frac{b - 1}{a - 1}$. $a = 1$, $b = 1$: **SCI** ($x = 1 - t$, $y = t$). $a = 1$, $b \ne 1$: **SI**.

**Verificación** ($a \ne 1$): $x + y = \frac{a - 1}{a - 1} = 1$ ✓ y $x + ay = \frac{a - b + ab - a}{a - 1} = b$ ✓.
</details>
<details><summary>Errores frecuentes</summary>Olvidar el subcaso $a = 1$, $b = 1$.</details>

### F11-N5-01 · [K] Cuadrada no es invertible

**Objetivo**: ver que $m = n$ no basta.
**Dificultad**: N5

**Enunciado.** Para $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$, calcula $\operatorname{rg}(A)$ y clasifica $A\mathbf{x} = \mathbf{b}$ para $\mathbf{b} = (1, 1)$ y $\mathbf{b} = (1, 3)$. ¿Por qué no puede ser SCD para ningún $\mathbf{b}$? ¿Qué condición sobre el rango garantiza SCD para todo $\mathbf{b}$?

<details><summary>Pista 1</summary>$\operatorname{rg}(A) = 1 < n = 2$.</details>
<details><summary>Pista 2</summary>SCD exige $r = n$.</details>
<details><summary>Solución</summary>

$\operatorname{rg}(A) = 1$. Para $\mathbf{b} = (1, 1)$: $\operatorname{rg}[A \mid \mathbf{b}] = 1$, **SCI**. Para $\mathbf{b} = (1, 3)$: $\operatorname{rg}[A \mid \mathbf{b}] = 2 \ne 1$, **SI**. Nunca SCD porque $r = 1 < 2 = n$. Si $A$ es $n \times n$ con $\operatorname{rg}(A) = n$, entonces $\operatorname{rg}[A \mid \mathbf{b}] = n$ para todo $\mathbf{b}$ (no cabe un pivote más) y el sistema es SCD siempre.
</details>
<details><summary>Errores frecuentes</summary>Creer que "cuadrada" ya implica invertible.</details>
