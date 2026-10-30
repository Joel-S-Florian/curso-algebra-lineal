# L40 — El teorema de Rouché-Frobenius

**Objetivo**: enunciar y demostrar el teorema que clasifica un sistema con los rangos.
**Prerrequisitos**: L28 (sin solución e infinitas), L32 (tres finales), L39 (rango).
**Código**: `escenas/l40_rouche_frobenius.py`
**Videos**: `videos/l40_rouche_frobenius/1080p60/` → `EnunciadoRF.mp4`, `DemostracionRF.mp4`, `IncognitasRangoYLibres.mp4`
**Ejercicios**: F11-N2-03, F11-N3-02, F11-N3-06, F11-N4-01, F11-N4-02.

---

## Desarrollo matemático

**Teorema (Rouché-Frobenius).** Sea $A\mathbf{x} = \mathbf{b}$ con $A$ de $m \times n$ y $r = \operatorname{rg}(A)$. (1) Es compatible $\iff \operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$. (2) Si es compatible y $r = n$: solución única (SCD). (3) Si es compatible y $r < n$: infinitas, con $n - r$ parámetros (SCI).

**Demostración (vía la forma escalonada).** Las operaciones por filas conservan soluciones y rangos; basta tomar $[A \mid \mathbf{b}]$ escalonada. (1) ($\Rightarrow$) Si es compatible no hay fila $[\,0\ \cdots\ 0 \mid c\,]$, $c \ne 0$: no hay pivote en $\mathbf{b}$ y los rangos coinciden. ($\Leftarrow$) Rangos iguales: sin pivote en $\mathbf{b}$; dando $0$ a las libres y leyendo las básicas se construye una solución. (2)–(3) Las $r$ básicas se despejan hacia atrás y quedan $n - r$ libres: ninguna si $r = n$ (solución única) y al menos una si $r < n$ (cada valor real da una solución distinta: infinitas).

**Consecuencias.** $m < n \Rightarrow$ nunca SCD. $\operatorname{rg}(A) = m \Rightarrow$ siempre compatible. Homogéneo $\Rightarrow$ siempre compatible, con solución única (la trivial) si y solo si $r = n$. Dimensión del conjunto de soluciones $= n - r$.

---

## Guion de narración

### Video 1 — `EnunciadoRF`

| En pantalla | Narración |
|---|---|
| Enunciado | "Compatible si y solo si los dos rangos coinciden; si además el rango es ene, una solución; si no, infinitas, con ene menos erre parámetros." |
| Tres casos | "Los dos rangos valen tres con tres incógnitas: determinado. Dos y dos con tres: un parámetro. Dos y tres: incompatible." |
| Consecuencias | "Menos ecuaciones que incógnitas, nunca determinado; rango igual a eme, siempre compatible; homogéneo, siempre compatible." |

### Video 2 — `DemostracionRF`

| En pantalla | Narración |
|---|---|
| Idea | "Basta con la matriz aumentada escalonada: las operaciones conservan soluciones y rangos." |
| Parte 1 | "Un pivote en be da cero igual a ce: incompatible; sin él, se construye una solución sustituyendo hacia atrás." |
| Partes 2 y 3 | "Hay erre variables básicas y ene menos erre libres: ninguna libre, una solución; alguna, infinitas." |

### Video 3 — `IncognitasRangoYLibres`

| En pantalla | Narración |
|---|---|
| $n - r$ | "El número de variables libres es el de incógnitas menos el rango." |
| Geometría | "En el espacio: punto, recta, plano o todo, según valga cero, uno, dos o tres." |

---

## Errores frecuentes

- Contar pivotes dentro de la columna $\mathbf{b}$ como si fuesen de $A$.
- Concluir SCI por tener menos ecuaciones que incógnitas sin comprobar que sea compatible.
- Olvidar que, con $\mathbf{b} = \mathbf{0}$, los dos rangos coinciden siempre.

## Resumen y conexión

Los rangos clasifican sin resolver; $n - r$ cuenta los parámetros. La L41 lo practica con ejemplos y un árbol de decisión.
