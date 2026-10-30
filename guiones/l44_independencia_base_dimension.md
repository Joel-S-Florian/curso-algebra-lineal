# L44 — Independencia lineal, base y dimensión

**Objetivo**: definir independencia, comprobarla con un sistema homogéneo y rangos, y definir base y dimensión.
**Prerrequisitos**: L43, L39–L40 (rango), L32 (variables libres).
**Código**: `escenas/l44_independencia_base_dimension.py`
**Videos**: `videos/l44_independencia_base_dimension/1080p60/` → `DependenciaLineal.mp4`, `ComoComprobarIndependencia.mp4`, `BaseYDimension.mp4`
**Ejercicios**: F12-N2-03, F12-N3-01, F12-N3-02, F12-N3-03, F12-N3-04, F12-N4-01, F12-N4-02, F12-N4-03, F12-N5-01.

---

## Desarrollo matemático

**Definición.** $\mathbf{v}_1,\dots,\mathbf{v}_k$ son independientes si $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{0} \Rightarrow$ todos los $c_i = 0$; si no, dependientes (alguno es combinación de los demás). Con $\mathbf{0}$ en el conjunto, siempre dependientes.

**Criterio.** Con $V = [\mathbf{v}_1 \cdots \mathbf{v}_k]$: independientes $\iff V\mathbf{c} = \mathbf{0}$ solo tiene $\mathbf{c} = \mathbf{0}$ $\iff \operatorname{rg}(V) = k$. Más de $n$ vectores en $\mathbb{R}^n$: $\operatorname{rg} \le n < k$, dependientes.

**Ejemplo.** $(1,2,1), (0,1,1), (1,4,3)$: columna 3 sin pivote, $c_3 = t$, $c_1 = -t$, $c_2 = -2t$: $\mathbf{w} = \mathbf{u} + 2\mathbf{v}$.

**Base y dimensión.** Base = independiente + generadora; las coordenadas son únicas; todas las bases de un subespacio tienen el mismo número de vectores (la dimensión). $\dim\mathbb{R}^n = n$. De un generador se extrae una base con las columnas pivote de la matriz original.

---

## Guion de narración

### Video 1 — `DependenciaLineal`

| En pantalla | Narración |
|---|---|
| $(1,2)$ y $(2,4)$ | "Ve es el doble de u: dos u menos ve da el vector nulo; dependientes." |
| $(1,2)$ y $(2,1)$ | "Solo la combinación trivial da cero; independientes." |
| Definición y tres consecuencias | "Con el vector nulo, o con más de ene vectores en ene dimensiones, dependientes." |

### Video 2 — `ComoComprobarIndependencia`

| En pantalla | Narración |
|---|---|
| Ecuación homogénea | "Ce uno u más ce dos ve más ce tres uve doble igual a cero." |
| Escalonar | "Columna tres sin pivote: variable libre y relación." |
| Criterio | "Independientes si y solo si el rango es el número de vectores." |

### Video 3 — `BaseYDimension`

| En pantalla | Narración |
|---|---|
| $\mathbf{e}_1,\mathbf{e}_2$ y $(1,1),(1,-1)$ | "Dos bases del plano; el mismo punto tiene coordenadas distintas en cada una." |
| Definiciones | "Independiente y generadora; la dimensión es el número de vectores de cualquier base." |
| Extraer una base | "Columnas pivote de la matriz original." |

---

## Errores frecuentes

- Pensar que independientes por pares implica independientes todos.
- Tomar las columnas de la reducida como base (L49).
- Confundir las coordenadas con el vector.

## Resumen y conexión

Independencia = rango máximo; base = lo justo para generar. La L45 usa estas ideas con el núcleo: las soluciones del sistema homogéneo.
