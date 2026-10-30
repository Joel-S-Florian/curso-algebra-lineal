# L43 — Combinaciones lineales y espacio generado

**Objetivo**: entender una combinación lineal geométricamente, definir el espacio generado y traducir «¿está $\mathbf{b}$ en el generado?» a un sistema.
**Prerrequisitos**: L17–L19 (vectores, suma, escalar, producto matriz-vector), L40 (Rouché-Frobenius).
**Código**: `escenas/l43_combinaciones_y_generado.py`
**Videos**: `videos/l43_combinaciones_y_generado/1080p60/` → `CombinacionLinealGeometrica.mp4`, `EspacioGenerado.mp4`
**Ejercicios**: F12-N1-01, F12-N1-02, F12-N2-01, F12-N2-02.

---

## Desarrollo matemático

**Combinación lineal.** $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k$ con coeficientes $c_i \in \mathbb{R}$ cualesquiera. Con $\mathbf{u} = (2,1)$, $\mathbf{v} = (-1,1)$: $2\mathbf{u} + \mathbf{v} = (3,3)$ y $\mathbf{u} - 2\mathbf{v} = (4,-1)$.

**Espacio generado.** $\operatorname{gen}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}$ = conjunto de todas las combinaciones lineales. Un vector no nulo genera una recta por el origen; dos que no son múltiplos, un plano (en $\mathbb{R}^2$, todo el plano); siempre contiene a $\mathbf{0}$.

**Conexión con los sistemas.** $\mathbf{b} \in \operatorname{gen}\{\mathbf{v}_i\} \iff [\mathbf{v}_1 \cdots \mathbf{v}_k \mid \mathbf{b}]$ es compatible $\iff \operatorname{rg}[V] = \operatorname{rg}[V \mid \mathbf{b}]$.

---

## Guion de narración

### Video 1 — `CombinacionLinealGeometrica`

| En pantalla | Narración |
|---|---|
| Dos vectores, $2\mathbf{u} + \mathbf{v}$ | "Solo se puede estirar y sumar; dos veces u, más una vez ve, da el vector tres, tres." |
| $\mathbf{u} - 2\mathbf{v}$ | "Un coeficiente negativo invierte el sentido." |
| Definición | "Suma de múltiplos con coeficientes cualesquiera." |
| Sistema | "Preguntar si un vector es combinación de otros es preguntar si un sistema tiene solución." |

### Video 2 — `EspacioGenerado`

| En pantalla | Narración |
|---|---|
| Recta | "Un solo vector genera una recta por el origen." |
| Vector extra proporcional | "No añade nada." |
| Plano | "Dos vectores en otra dirección generan todo el plano." |
| Regla de pertenencia | "Es compatible el sistema con los vectores por columnas y $\mathbf{b}$; por Rouché-Frobenius, los rangos coinciden." |

---

## Errores frecuentes

- Pensar que dos vectores siempre generan un plano (si son múltiplos, solo una recta).
- Olvidar que el vector nulo siempre está en el espacio generado.
- Resolver con dos componentes y no comprobar la tercera.

## Resumen y conexión

Combinación = suma de múltiplos; generado = todas. La L44 pregunta cuándo sobra un vector: independencia, base y dimensión.
