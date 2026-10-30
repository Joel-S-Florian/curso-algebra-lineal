# L05 — ¿Qué es una ecuación lineal?

**Objetivo**: reconocer una ecuación lineal, escribirla en forma estándar y distinguirla de las no lineales.
**Prerrequisitos**: L02 (términos y coeficientes), L03 (gráficas), L04 (subíndices).
**Código**: `escenas/l05_ecuacion_lineal.py`
**Videos**: `videos/l05_ecuacion_lineal/1080p60/` → `DefinicionEcuacionLineal.mp4`, `LinealVsNoLineal.mp4`, `TrampasDeLinealidad.mp4`
**Ejercicios**: F01-N1-01, F01-N1-02, F01-N1-03, F01-N4-01.

---

## Desarrollo matemático

**Definición.** Una ecuación con incógnitas $x_1, \dots, x_n$ es **lineal** si puede escribirse como
$$a_1x_1 + a_2x_2 + \cdots + a_nx_n = b,$$
donde los **coeficientes** $a_1, \dots, a_n$ y el **término independiente** $b$ son números reales fijos. Es la *forma estándar*.

Las incógnitas solo aparecen multiplicadas por números y sumadas: sin potencias ($x^2$), sin productos entre ellas ($xy$), sin estar en un denominador ($1/x$), sin estar dentro de raíces o funciones ($\sqrt x$, $\operatorname{sen} x$). Dividir **entre un número** sí es lineal: $\frac x3 = \frac13 x$.

**Nombre.** Con dos incógnitas, las soluciones de una ecuación lineal forman una **recta** (Lección 3); de ahí "lineal".

**Matices.**

- La linealidad se decide **después de simplificar con pasos válidos**: $(x + 1)^2 = x^2 + 3$ se reduce a $2x = 2$.
- Si al simplificar hace falta multiplicar por una expresión con incógnitas (como $\frac xy = 2$), la ecuación no es lineal: $y$ está en un denominador y el paso exige $y \neq 0$.
- "Lineal" se dice **respecto de unas incógnitas concretas**. En $ax + 3y = 5$, si $a$ es un *parámetro* (número fijo), es lineal en $x, y$.
- Con todos los coeficientes nulos, $0x_1 + \dots + 0x_n = b$ es lineal *degenerada*: si $b \neq 0$ no tiene solución; si $b = 0$, todo es solución.

---

## Guion de narración

### Video 1 — `DefinicionEcuacionLineal`

| En pantalla | Narración |
|---|---|
| $2x + y = 4$; puntos que la cumplen; recta | "Busquemos puntos que cumplan dos equis más ye igual a cuatro. Están todos alineados: forman una recta. Por eso estas ecuaciones se llaman lineales." |
| Forma general con recuadros | "En general, una ecuación lineal tiene esta forma: cada incógnita multiplicada por un número fijo, su coeficiente, todo sumado, e igualado a otro número fijo, el término independiente." |
| Regla en texto | "Las incógnitas solo pueden aparecer así: multiplicadas por números y sumadas. Nada de potencias, ni productos entre incógnitas, ni dividir entre ellas, ni raíces o senos." |
| Cuatro ejemplos llevados a forma estándar | "Para reconocer los coeficientes, pasamos todas las incógnitas a un lado. Los coeficientes pueden ser fracciones, o incluso raíz de dos o pi: lo que importa es cómo aparecen las incógnitas, no qué números las acompañan." |

### Video 2 — `LinealVsNoLineal`

| En pantalla | Narración |
|---|---|
| Ecuaciones que caen en dos columnas | "Clasifiquemos. Equis al cuadrado: no lineal. Equis por ye: no lineal. Equis tercios menos dos ye: sí, porque dividir entre tres es multiplicar por un tercio. Uno entre equis: no, la incógnita está en el denominador." |
| Recta, parábola e hipérbola | "Las gráficas lo delatan: la ecuación lineal da una recta; las otras, curvas. Esa regularidad es la que hará posible un método que resuelve cualquier sistema lineal: la eliminación de Gauss." |

### Video 3 — `TrampasDeLinealidad`

| En pantalla | Narración |
|---|---|
| $(x+1)^2 = x^2 + 3 \to 2x = 2$ | "Esta ecuación parece no lineal por los cuadrados, pero al desarrollar se cancelan: queda dos equis igual a dos. Se decide después de simplificar." |
| $\frac xy = 2$, el punto $(0,0)$ | "Esta parece lineal, pero ye está en un denominador. Si multiplicamos por ye obtenemos equis igual a dos ye, que admite el punto cero cero, donde la ecuación original ni siquiera está definida." |
| $ax + 3y = 5$ | "¿Es lineal? Depende de quién sea incógnita. Si a es un número fijo, un parámetro, sí. Si también fuera incógnita, a por equis sería un producto de incógnitas." |
| $0x + 0y = 5$ y $0x + 0y = 0$ | "Cuando todos los coeficientes son cero, la ecuación dice cero igual a algo. Si ese algo no es cero, ninguna solución; si lo es, todas. Volveremos a encontrarlas al final de la eliminación de Gauss." |

---

## Errores frecuentes

- Decir que $\frac x5$ no es lineal, o que $\frac 5x$ sí lo es.
- Creer que $\sqrt2\,x$ no es lineal porque tiene una raíz.
- Clasificar sin simplificar antes.
- Olvidar que la linealidad depende de qué letras son incógnitas.

## Resumen y conexión

Una ecuación lineal es $a_1x_1 + \dots + a_nx_n = b$. En la Lección 6 resolvemos la más sencilla, con una sola incógnita, y descubrimos que puede tener una, infinitas o ninguna solución.
