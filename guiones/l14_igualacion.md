# L14 — El método de igualación

**Objetivo**: resolver sistemas por igualación, justificar el método e interpretarlo como "buscar la misma altura".
**Prerrequisitos**: L03 (pendiente), L13.
**Código**: `escenas/l14_igualacion.py`
**Videos**: `videos/l14_igualacion/1080p60/` → `IgualacionPasoAPaso.mp4`, `IgualacionInterpretacion.mp4`
**Ejercicios**: F04-N1-03, N2-02, N3-02.

---

## Desarrollo matemático

**Método.**

1. Despejar **la misma** incógnita en las dos ecuaciones: $y = A(x)$, $y = B(x)$.
2. Igualar: $A(x) = B(x)$.
3. Resolver esa ecuación con una incógnita.
4. Calcular la otra incógnita con cualquiera de los despejes (deben coincidir).
5. Verificar.

Ejemplo: $2x - y = 1$, $x + 3y = 11$. $y = 2x - 1$, $y = \frac{11 - x}{3}$; $2x - 1 = \frac{11 - x}{3} \Rightarrow 7x = 14 \Rightarrow x = 2$, $y = 3$.

**Justificación.** Si $y = A$ e $y = B$, entonces $A = B$ (dos cantidades iguales a una tercera son iguales entre sí). Recíprocamente, $A = B$ e $y = A$ implican $y = B$. Así $\{y = A,\ y = B\} \Leftrightarrow \{y = A,\ A = B\}$. Igualar es una sustitución disfrazada.

**Geometría.** Para cada $x$, cada despeje da una altura. Resolver $A(x) = B(x)$ es buscar el $x$ donde las dos rectas tienen la misma altura, es decir, donde se cortan.

**Casos especiales.** Si se llega a una igualdad falsa ($-1 = 3$): rectas paralelas, SI. Si se llega a $0 = 0$: la misma recta, SCI.

**Cuándo conviene.** Cuando la misma incógnita ya está despejada en las dos ecuaciones (problemas del tipo "tarifa fija + precio por unidad"). No escala a tres o más incógnitas.

---

## Guion de narración

### Video 1 — `IgualacionPasoAPaso`

| En pantalla | Narración |
|---|---|
| Dos despejes de $y$ | "Despejamos ye en cada ecuación." |
| $2x - 1 = \frac{11 - x}{3}$ | "Si ye es igual a las dos expresiones, las dos expresiones son iguales entre sí. Ya tenemos una ecuación con una incógnita." |
| Pasos 3 a 5 | "Equis vale dos. Con cualquiera de los despejes, ye vale tres: los dos deben coincidir, lo que sirve de control. Y verificamos." |
| Justificación | "Dos cantidades iguales a una tercera son iguales entre sí; y al revés, con una igualdad y un despeje recuperamos el otro. El sistema no cambia de soluciones." |

### Video 2 — `IgualacionInterpretacion`

| En pantalla | Narración |
|---|---|
| Línea vertical que recorre $x$, con la diferencia de alturas | "Para cada equis, cada recta tiene una altura. Igualar es buscar el equis donde la diferencia de alturas es cero: el punto de corte." |
| Taxis A y B | "La igualación es natural cuando las incógnitas ya vienen despejadas: tarifa A, tres euros más dos por kilómetro; tarifa B, siete más uno por kilómetro. Cuestan lo mismo a los cuatro kilómetros." |
| Casos especiales | "Si al igualar sale algo falso, las rectas son paralelas; si sale cero igual a cero, son la misma." |

---

## Errores frecuentes

- Despejar incógnitas distintas en cada ecuación.
- Errores de signo al despejar.
- No comprobar que los dos despejes dan el mismo valor.

## Resumen y conexión

La igualación es útil cuando ya hay despejes, pero no escala. En la Lección 15 vemos la reducción: el método que sí generaliza y que da lugar a la eliminación de Gauss.
