# L33 — Gauss frente a Gauss-Jordan

**Objetivo**: comparar el coste de Gauss con sustitución hacia atrás y el de Gauss-Jordan, y saber cuándo conviene cada uno.
**Prerrequisitos**: L26 (Gauss), L31 (Gauss-Jordan), L32 (leer la solución).
**Código**: `escenas/l33_gauss_frente_a_jordan.py`
**Videos**: `videos/l33_gauss_frente_a_jordan/1080p60/` → `ContarOperaciones.mp4`, `CuandoConvieneCadaUno.mp4`
**Ejercicios**: F09-N2-05, F09-N3-06, F09-N4-03, F09-N4-04.

---

## Desarrollo matemático

**Convenio de conteo.** Sistema $n \times n$, una columna $\mathbf{b}$, sin intercambios de filas; se cuentan multiplicaciones y divisiones.

**Gauss + sustitución hacia atrás.** Eliminación: $\sum_{k=1}^{n-1} (n-k)(n-k+2) = \frac{n(n-1)(2n+5)}{6}$. Sustitución: $\frac{n(n+1)}{2}$. Total
$$\frac{n^3 + 3n^2 - n}{3} \approx \frac{n^3}{3}.$$

**Gauss-Jordan.** En el paso $k$: $n(n - k + 1)$ operaciones. Total
$$\sum_{k=1}^{n} n(n-k+1) = \frac{n^2(n+1)}{2} = \frac{n^3 + n^2}{2} \approx \frac{n^3}{2}.$$

**Comparación.** Cociente Gauss-Jordan / Gauss $= \frac{3(n^2 + n)}{2(n^2 + 3n - 1)} \to \frac32$ por debajo. $n = 3$: $17$ y $18$; $n = 10$: $430$ y $550$; $n = 100$: $343\,300$ y $505\,000$; $n = 1000$: $334\,333\,000$ y $500\,500\,000$ (conteos comprobados con un programa en `ejercicios/verificar/f09.py`). Gauss-Jordan fabrica el doble de ceros ($n(n-1)$ frente a $\frac{n(n-1)}{2}$).

**Qué elegir.** A mano y sistemas pequeños: Gauss-Jordan (lectura directa de la solución). Un sistema grande en ordenador: Gauss con sustitución (un tercio menos de operaciones). Comparar o decidir equivalencia de sistemas: la reducida (única). Muchos lados derechos con la misma $A$: factorización $LU$ (Unidad 6).

---

## Guion de narración

### Video 1 — `ContarOperaciones`

| En pantalla | Narración |
|---|---|
| Dos cuadrículas 5 × 5 | "Gauss fabrica ceros solo debajo de la diagonal; Gauss-Jordan, también encima: el doble." |
| Fórmulas | "Contamos multiplicaciones y divisiones. Gauss con sustitución: ene cubo más tres ene cuadrado menos ene, entre tres. Gauss-Jordan: ene cuadrado por ene más uno, entre dos." |
| Tabla | "Con tres incógnitas, diecisiete frente a dieciocho; con mil, trescientos treinta y cuatro millones frente a quinientos millones." |
| Gráfica | "El cociente sube hacia tres medios: Gauss-Jordan necesita un cincuenta por ciento más para sistemas grandes." |

### Video 2 — `CuandoConvieneCadaUno`

| En pantalla | Narración |
|---|---|
| Tabla comparativa | "Gauss hace menos operaciones y deja una escalonada; Gauss-Jordan deja la reducida única, de la que la solución se lee directamente." |
| Qué elegir | "A mano, Gauss-Jordan; sistemas grandes, Gauss; comparar sistemas, la reducida; muchos lados derechos, ele u." |
| Lo que no cambia | "Las mismas operaciones, el mismo conjunto solución, y siempre verificar en el original." |

---

## Errores frecuentes

- Pensar que uno de los métodos da otra solución: dan el mismo conjunto solución.
- Comparar con $n^3/3$ y $n^3/2$ para $n$ pequeño (en $n = 3$ la diferencia es 17 frente a 18).
- Usar Gauss-Jordan "porque es más completo" en un sistema grande en ordenador.

## Resumen y conexión

Gauss con sustitución hacia atrás cuesta unas $n^3/3$ operaciones y Gauss-Jordan unas $n^3/2$; para sistemas pequeños, a mano, la diferencia no importa y la lectura directa gana. Con muchos lados derechos para la misma matriz, hace falta algo mejor: la factorización $LU$ (Unidad 6).
