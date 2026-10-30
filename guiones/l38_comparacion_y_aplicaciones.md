# L38 — Comparación y aplicaciones

**Objetivo**: ver cuándo compensa factorizar (muchos lados derechos) y comparar todos los métodos de resolución.
**Prerrequisitos**: L33 (Gauss frente a Gauss-Jordan), L36–L37.
**Código**: `escenas/l38_comparacion_y_aplicaciones.py`
**Videos**: `videos/l38_comparacion_y_aplicaciones/1080p60/` → `MuchosLadosDerechos.mp4`, `TablaComparativa.mp4`
**Ejercicios**: F10-N2-06, F10-N3-07, F10-N4-04.

---

## Desarrollo matemático

**Muchos lados derechos.** Con la misma $A$ y $k$ vectores $\mathbf{b}_i$: LU cuesta $\frac{n^3 - n}{3} + kn^2$; Gauss repetido, $k\,\frac{n^3 + 3n^2 - n}{3}$. La diferencia es $(k - 1)\,\frac{n^3 - n}{3} \ge 0$: con $k = 1$ cuestan igual y para $k \ge 2$ gana LU. Con $n = 100$ y $k = 50$: $833\,300$ frente a $17\,165\,000$ (unas 21 veces menos).

**Ejemplo.** Con la $L$ y la $U$ de la L34: $\mathbf{b}_1 = (-3, 1, 2) \to \mathbf{x} = (1, -1, 2)$; $\mathbf{b}_2 = (0, 1, -3) \to (2, -1, 0)$; $\mathbf{b}_3 = (2, 5, 1) \to (1, \frac45, \frac35)$.

**Tabla.** Sustitución e igualación: 2–3 incógnitas a mano. Reducción/Gauss: un sistema, $\approx n^3/3$. Gauss-Jordan: a mano y para comparar sistemas, $\approx n^3/2$. $PA = LU$: misma $A$ con muchos $\mathbf{b}$, $\approx n^3/3$ una vez más $n^2$ por $\mathbf{b}$. Todos dan el mismo conjunto solución y exigen verificar en el original.

---

## Guion de narración

### Video 1 — `MuchosLadosDerechos`

| En pantalla | Narración |
|---|---|
| $A\mathbf{x}_i = \mathbf{b}_i$ | "La misma matriz y muchos lados derechos: por ejemplo, una estructura con muchas cargas." |
| Gauss repetido frente a LU | "Gauss rehace la eliminación cada vez; ele u la hace una vez y cada be cuesta ene cuadrado." |
| Tres lados derechos | "Ele y u no cambian: solo las dos sustituciones." |
| Ahorro | "La diferencia es ka menos uno por ene cubo menos ene entre tres: con cien por cien y cincuenta lados derechos, unas veintiuna veces menos." |

### Video 2 — `TablaComparativa`

| En pantalla | Narración |
|---|---|
| Tabla | "Sustitución e igualación, a mano; Gauss, un sistema; Gauss-Jordan, lectura directa; ele u, la misma matriz con muchos lados derechos." |
| Qué comparten | "Las mismas operaciones, el mismo conjunto solución, y siempre verificar en el original." |
| Lo que viene | "El número de pivotes es el rango: en la unidad siete, Rouché-Frobenius." |

---

## Errores frecuentes

- Pensar que LU siempre gana: con un solo $\mathbf{b}$ cuesta lo mismo que Gauss.
- Refactorizar $A$ para cada $\mathbf{b}$.
- Elegir un método sin pensar cuántas veces se reutiliza la eliminación.

## Resumen y conexión

Con pocas incógnitas, a mano, cualquiera sirve; para un sistema grande, Gauss; con la misma $A$ y muchos $\mathbf{b}$, $PA = LU$. En la Unidad 7 dejamos de resolver para **clasificar**: el rango.
