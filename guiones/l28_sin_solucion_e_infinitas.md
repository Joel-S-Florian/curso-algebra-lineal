# L28 — Sistemas sin solución y con infinitas soluciones

**Objetivo**: detectar un sistema incompatible por una fila $[\,0 \cdots 0 \mid c\,]$, $c \neq 0$, y describir las infinitas soluciones de un SCI con variables libres y parámetros.
**Prerrequisitos**: L07 (parámetros), L09 (tres planos), L11 (clasificación), L24–L27.
**Código**: `escenas/l28_sin_solucion_e_infinitas.py`
**Videos**: `videos/l28_sin_solucion_e_infinitas/1080p60/` → `FilaContradictoria.mp4`, `VariablesLibresYSolucionParametrica.mp4`
**Ejercicios**: F08-N2-06, F08-N3-03 (en video); F08-N4-02, F08-N5-03.

---

## Desarrollo matemático

**Fila contradictoria.** $x + y + z = 2$, $x + 2y + 3z = 5$, $2x + 3y + 4z = 8$. Con $R_2 \leftarrow R_2 - R_1$, $R_3 \leftarrow R_3 - 2R_1$, $R_3 \leftarrow R_3 - R_2$ queda la fila $[\,0 \ \ 0 \ \ 0 \mid 1\,]$: $0 = 1$.

*Por qué se concluye SI.* Las operaciones conservan el conjunto solución (L24); el sistema final contiene una ecuación que nadie cumple, así que su conjunto solución es vacío, y el del original también. Prueba directa: $E_3 - E_1 - E_2$ da $0x + 0y + 0z = 8 - 2 - 5 = 1$.

**Regla.** Si una forma escalonada de $[A \mid \mathbf{b}]$ tiene una fila $[\,0 \cdots 0 \mid c\,]$ con $c \neq 0$ (un pivote en la columna de $\mathbf{b}$), el sistema es incompatible. Si no la tiene, el sistema tiene solución (F08-N5-03: se dan valores a las libres y se sustituye hacia atrás, siempre dividiendo por pivotes no nulos).

**Variables libres.** Con $7$ en lugar de $8$, la última fila es nula: $\left[\begin{array}{ccc|c} 1 & 1 & 1 & 2 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{array}\right]$. Las columnas sin pivote dan **variables libres** (aquí $z$), que pueden tomar cualquier valor: $z = t$ (parámetro). Hacia atrás:
$y = 3 - 2t$, $x = 2 - y - z = -1 + t$, es decir
$$(x, y, z) = (-1 + t,\ 3 - 2t,\ t) = (-1, 3, 0) + t\,(1, -2, 1), \qquad t \in \mathbb{R},$$
una recta: la intersección de los tres planos (L09).

**Verificación para todo $t$.** $E_1$: $(-1 + t) + (3 - 2t) + t = 2$; $E_2$: $(-1 + t) + 2(3 - 2t) + 3t = 5$; $E_3$: $2(-1 + t) + 3(3 - 2t) + 4t = 7$. Los términos en $t$ se cancelan.

**Cuenta.** Libres $=$ incógnitas $-$ pivotes $= 3 - 2 = 1$. Sin fila contradictoria: SCD si no hay libres, SCI si las hay (antesala del teorema de Rouché-Frobenius, L40).

**Dos libres.** $x + 2y - z = 3$: $y = s$, $z = t$, $x = 3 - 2s + t$ ($s, t \in \mathbb{R}$), un plano.

---

## Guion de narración

### Video 1 — `FilaContradictoria`

| En pantalla | Narración |
|---|---|
| Eliminación | "Eliminamos como siempre… y la última fila dice cero igual a uno." |
| Por qué | "Las operaciones no cambian las soluciones, y el sistema final no tiene ninguna. Además, la tercera ecuación menos las otras dos da directamente cero igual a uno." |
| Regla | "Un pivote en la columna de be significa: sin solución. Vale cualquier c distinto de cero." |

### Video 2 — `VariablesLibresYSolucionParametrica`

| En pantalla | Narración |
|---|---|
| Mismo sistema con 7 | "Con un siete, la última fila se anula: no hay contradicción, pero quedan dos pivotes para tres incógnitas." |
| Variable libre | "La columna de zeta no tiene pivote: zeta es libre. La llamamos te." |
| Hacia atrás con $t$ | "Y vale tres menos dos te; equis, menos uno más te. Una solución para cada valor de te: una recta." |
| Verificación | "Sustituimos con te general: los términos en te se cancelan en cada ecuación." |
| Dos libres | "Una ecuación con tres incógnitas: dos libres, dos parámetros, un plano." |

---

## Errores frecuentes

- Seguir sustituyendo tras ver $0 = 1$, o leer esa fila como $z = 1$ o $x = y = z = 0$.
- Confundir $[\,0 \ 0 \ 0 \mid 0\,]$ con $[\,0 \ 0 \ 0 \mid c\,]$.
- Dar a la libre un valor y decir que la solución es única.
- Elegir como libre una variable pivote.
- Olvidar "$t \in \mathbb{R}$" o que $x$ depende de $t$.

## Resumen y conexión

La forma escalonada clasifica el sistema: fila $[\,0 \cdots 0 \mid c\,]$ ⇒ SI; si no, cada columna sin pivote es una variable libre ⇒ SCI, y sin libres ⇒ SCD. En la L29 aplicamos esto a sistemas con parámetros, donde cada caso depende de un número desconocido.
