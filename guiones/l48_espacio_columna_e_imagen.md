# L48 — Espacio columna e imagen

**Objetivo**: leer $A\mathbf{x}$ como combinación de columnas, definir $\operatorname{Col}(A)$ y caracterizar la existencia de solución con $\mathbf{b} \in \operatorname{Col}(A)$.
**Prerrequisitos**: L19, L21 (transformaciones), L43.
**Código**: `escenas/l48_espacio_columna_e_imagen.py`
**Videos**: `videos/l48_espacio_columna_e_imagen/1080p60/` → `AxEsCombinacionDeColumnas.mp4`, `ExisteSolucionSiiBEnCol.mp4`
**Ejercicios**: F14-N1-01, F14-N1-02, F14-N2-01, F14-N2-02.

---

## Desarrollo matemático

**Por columnas.** $A\mathbf{x} = x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n$. Con $\mathbf{x} = (2,-1,3,1)$ en $A$ de $3\times 4$: $(1,7,6)$.

**Espacio columna.** $\operatorname{Col}(A) = \operatorname{gen}\{\mathbf{a}_1,\dots,\mathbf{a}_n\} = \{A\mathbf{x}\} \subseteq \mathbb{R}^m$.

**Existencia.** $A\mathbf{x} = \mathbf{b}$ tiene solución $\iff \mathbf{b} \in \operatorname{Col}(A) \iff \operatorname{rg}(A) = \operatorname{rg}[A \mid \mathbf{b}]$.
En el plano, $A = \begin{bmatrix} 1&2\\2&4 \end{bmatrix}$: $\operatorname{Col}(A)$ = recta $y = 2x$; $(3,6)$ sí, $(1,0)$ no. Con $A$ de $3\times 4$: $(1,3,2) = \mathbf{a}_1 + \mathbf{a}_3$ sí; $(1,0,0)$: rangos $2$ y $3$, no.

**Imagen.** $T(\mathbf{x}) = A\mathbf{x}$, $\operatorname{Im}(T) = \operatorname{Col}(A)$: lo alcanzable. Si $\operatorname{Col}(A) = \mathbb{R}^m$, hay solución para todo $\mathbf{b}$.

---

## Guion de narración

### Video 1 — `AxEsCombinacionDeColumnas`

| En pantalla | Narración |
|---|---|
| Producto por columnas | "Los números de equis son los coeficientes." |
| Ejemplo $(1,7,6)$ | "Por filas o por columnas, el mismo resultado." |
| Definición | "Generado por las columnas = todos los productos." |
| Ejemplo 2×2 | "Una recta, aunque haya dos columnas." |

### Video 2 — `ExisteSolucionSiiBEnCol`

| En pantalla | Narración |
|---|---|
| Regla | "Resolver es buscar coeficientes que combinen las columnas en be." |
| Plano | "Sobre la recta, solución; fuera, incompatible." |
| 3×4 | "Mirando los rangos." |
| Imagen | "Lo que se puede alcanzar." |

---

## Errores frecuentes

- Pensar que $\operatorname{Col}(A) \subseteq \mathbb{R}^n$ (vive en $\mathbb{R}^m$).
- Creer que el número de columnas es la dimensión de $\operatorname{Col}(A)$ (es el rango).
- Decidir la compatibilidad sin comparar los dos rangos.

## Resumen y conexión

$\mathbf{b} \in \operatorname{Col}(A)$ $\iff$ hay solución. La L49 da una base de $\operatorname{Col}(A)$.
