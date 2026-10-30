# L00 — Bienvenida y prueba del entorno

**Objetivo**: comprobar que Python, Manim y LaTeX funcionan, y dar un anticipo de todo el curso en un solo ejemplo.
**Escena**: `PruebaEntorno` en `escenas/l00_prueba_entorno.py`.
**Video**: `videos/l00_prueba_entorno/1080p60/PruebaEntorno.mp4`.

> Esta lección no es todavía una clase "desde cero": usa palabras (coeficiente, matriz, fila) que se definirán con calma en las lecciones L02, L16 y L24. Aquí solo se ve el recorrido completo una vez, para saber hacia dónde vamos.

## Guion de narración

| Sección (método) | En pantalla | Narración |
|---|---|---|
| `portada` | Título "Prueba del entorno" | "Bienvenido. Antes de empezar el curso vamos a recorrer, en un minuto, el camino completo que haremos durante muchas lecciones: de un sistema de ecuaciones a su solución." |
| `sistema_a_matriz` | Pregunta y sistema x + y = 3, x − y = 1 | "Buscamos dos números, x e y, que cumplan las dos igualdades a la vez. Eso es un sistema de ecuaciones." |
| | Aparecen los 1 y el (−1) | "Delante de x hay un 1 que no se escribe, y delante de −y hay un −1. Esos números que multiplican a las incógnitas se llaman coeficientes. El signo menos pertenece al coeficiente." |
| | Los números viajan a la matriz | "Si solo guardamos los números, en el mismo orden, obtenemos una tabla: la matriz aumentada. En azul, los coeficientes; detrás de la barra, en naranja, los términos independientes." |
| | Recuadros ecuación ↔ fila | "Cada fila de la matriz es exactamente una ecuación del sistema. No hemos perdido información, solo hemos dejado de escribir las letras." |
| `operacion_por_filas` | R₂ ← R₂ − R₁ y la cuenta por columnas | "Ahora restamos a la segunda fila la primera, número a número: 1 − 1 = 0, −1 − 1 = −2, 1 − 3 = −2. A la izquierda vemos lo mismo hecho en las ecuaciones." |
| | Aparece el 0 en amarillo | "El objetivo era ese cero: la x desaparece de la segunda ecuación. Por qué esta operación no cambia las soluciones lo demostraremos en la lección 24." |
| `sustitucion_hacia_atras` | −2y = −2 ⇒ y = 1; x + 1 = 3 ⇒ x = 2 | "La segunda ecuación ya solo tiene y: dividimos entre −2 y obtenemos y = 1. Lo sustituimos en la primera: x + 1 = 3, luego x = 2." |
| `interpretacion_geometrica` | Dos rectas y el punto (2, 1) | "Cada ecuación con dos incógnitas es una recta del plano. Resolver el sistema es encontrar el punto que está en las dos rectas a la vez." |
| | 2 + 1 = 3 ✓, 2 − 1 = 1 ✓ | "Y nunca terminamos sin comprobar: sustituimos en el sistema original y ambas igualdades se cumplen." |
| `cierre` | "El entorno funciona." | "Si ves este video, tu entorno está listo. Empezamos de verdad en la lección 1, con los números reales." |

## Ejercicios

Ninguno: es una lección de prueba. El primer banco de ejercicios llega con la Unidad 0.
