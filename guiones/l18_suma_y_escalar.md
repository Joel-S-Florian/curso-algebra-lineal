# L18 — Suma de matrices y producto por un escalar

**Objetivo**: sumar matrices y multiplicarlas por números, conocer sus propiedades y saber demostrarlas.
**Prerrequisitos**: L01 (propiedades de los reales), L16.
**Código**: `escenas/l18_suma_y_escalar.py`
**Videos**: `videos/l18_suma_y_escalar/1080p60/` → `SumaDeMatrices.mp4`, `ProductoPorEscalarYPropiedades.mp4`
**Ejercicios**: F05-N1-04, F05-N2-02, F05-N4-01, F05-N5-01.

---

## Desarrollo matemático

**Suma.** Si $A$ y $B$ son $m\times n$: $(A + B)_{ij} = a_{ij} + b_{ij}$. Si las dimensiones difieren, la suma **no está definida**.

**Producto por un escalar.** $(cA)_{ij} = c\,a_{ij}$. Opuesta: $-A = (-1)A$. Resta: $A - B = A + (-1)B$.

**Propiedades** ($A, B, C$ de la misma dimensión; $c, d$ reales):

- $A + B = B + A$; $(A + B) + C = A + (B + C)$
- $A + O = A$; $A + (-A) = O$
- $c(A + B) = cA + cB$; $(c + d)A = cA + dA$; $c(dA) = (cd)A$; $1A = A$

*Demostración (conmutativa).* $(A + B)_{ij} = a_{ij} + b_{ij} = b_{ij} + a_{ij} = (B + A)_{ij}$ para toda $(i, j)$. $\blacksquare$ Todas se prueban igual: comparando una posición cualquiera y usando la propiedad correspondiente de los números reales.

Consecuencia práctica: las ecuaciones con matrices se despejan como con números, por ejemplo $A + 2X = B \Rightarrow X = \frac12(B - A)$.

---

## Guion de narración

### Video 1 — `SumaDeMatrices`

| En pantalla | Narración |
|---|---|
| Elementos emparejados y sumados | "Para sumar matrices se suman los números que ocupan la misma posición: uno más dos, menos dos más cinco..." |
| $2\times 3$ más $2\times 2$ | "Si las matrices tienen distinta dimensión, algún número se queda sin pareja: la suma no está definida." |

### Video 2 — `ProductoPorEscalarYPropiedades`

| En pantalla | Narración |
|---|---|
| $3A$ | "Multiplicar una matriz por un número es multiplicar cada elemento por ese número." |
| $-A$ y $A - B$ | "Con menos uno obtenemos la opuesta; restar es sumar la opuesta." |
| Tabla de propiedades | "Estas operaciones cumplen las mismas propiedades que los números, porque se hacen posición a posición." |
| Demostración de la conmutativa | "Para demostrarlo miramos una posición cualquiera: a i jota más be i jota es igual a be i jota más a i jota, por la conmutativa de los números reales. Como vale en todas las posiciones, las matrices son iguales." |

---

## Errores frecuentes

- Sumar matrices de distinta dimensión.
- Multiplicar por el escalar solo una fila o un elemento.
- "Demostrar" una propiedad con un ejemplo.

## Resumen y conexión

Suma y escalar funcionan posición a posición y conservan las propiedades de los números. El producto de matrices (L19–L20) es muy distinto: no es posición a posición.
