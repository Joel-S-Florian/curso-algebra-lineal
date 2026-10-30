# Lo que falta por hacer (estado al 29-10-2026)

Documento de traspaso: con este archivo, el `README.md` y `docs/01_diseno_curso.md` se puede retomar el trabajo en una sesión nueva sin el historial anterior.

## 1. Estado actual

| Unidad | Lecciones | Videos 1080p60 | Guiones | Ejercicios (parte 1 + parte 2) | Estado |
|---|---|---|---|---|---|
| 0 Preliminares | L00–L04 | 16 | ✅ | F00 (30) | ✅ |
| 1 Fundamentos | L05–L12 | 24 | ✅ | F01–F03 (110) | ✅ |
| 2 Métodos elementales | L13–L15 | 8 | ✅ | F04 (50) | ✅ |
| 3 Matrices y Ax = b | L16–L23 | 18 | ✅ | F05–F07 (120) | ✅ |
| 4 Gauss | L24–L30 | 14 | ✅ | F08 (50) | ✅ |
| 5 Gauss-Jordan | L31–L33 | 7 | ✅ | F09 (40) | ✅ |
| 6 Factorización LU | L34–L38 | 13 | ✅ | F10 (40) | ✅ |
| 7 Rango y Rouché-Frobenius | L39–L42 | 10 | ✅ | F11 (50) | ✅ |
| 8 Núcleo e imagen | L43–L50 | 17 | ✅ | F12–F14 (120) | ✅ |
| 9 Síntesis | L51–L55 | 15 | en el código (ver nota) | F15–F16 (55) | ✅ |

**Total**: 142 videos con voz y subtítulos (L00–L55), 665 ejercicios con solución, solucionario, formulario, tabla de métodos con árbol de decisión, plan de estudio y prueba final integradora. El cierre automático (`cierre.py`) comprobó los 142: ninguno sin audio ni subtítulos.

**Nota sobre L51–L55**: las escenas llevan la narración completa en el código (`self.decir(...)`); no se escribieron guiones `guiones/l51…l55_*.md` aparte. Si se quieren, se pueden extraer de las escenas.

## 2. Pendientes inmediatos

1. **Revisión automática de bordes (hecha el 29-10)**: `python herramientas\bordes.py . salida.txt "l*/1080p60/*.mp4"` muestrea un fotograma cada 3 s y marca los videos con contenido pegado al borde. Sobre los 142 videos salieron 10 marcados: 5 eran defectos reales y se corrigieron (L31 `LaReducidaEsUnica` con dos historiales superpuestos; L32 `LeerLaSolucion` con la matriz cortada a la izquierda; L36 `SustitucionHaciaAtrasUx` con una línea cortada a la derecha; L39 `RangoNoEsNumeroDeEcuaciones` con la nota cortada; L52 `ProblemaRotonda` con la nota cortada), y se volvieron a renderizar; los otros eran rejillas a pantalla completa (L21) o un movimiento transitorio (L03). **Causa común**: `ajustar_al_encuadre` escalaba pero no recolocaba; ahora llama a `meter_en_encuadre`. Las herramientas están en `herramientas\` (`bordes.py` revisa bordes, `hoja2.py` hace hojas de fotogramas, `cuadro.py` extrae un fotograma, `cola.py` renderiza de 3 en 3 y `cierre.py` comprueba audio y subtítulos y rellena las duraciones del README).
2. **Fotogramas finales sin revisar a ojo**: los videos de L31–L42 y de la Unidad 3 que el detector no marcó. El detector solo ve contenido pegado al borde, no solapamientos interiores (como el de L31, que sí tenía además un desborde): una pasada visual completa por hojas de fotogramas sigue siendo recomendable.

## 3. Cómo se produjo y se regenera todo

- Escenas: `escenas/lNN_*.py` (Manim CE 0.22, `EscenaCurso`), narración con `self.decir(...)` (voz `es-MX-DaliaNeural`, `curso/voz.py`). Renderizar: `manim -qh escenas/lNN_….py -a` (de 3 en 3; con 7,7 GB de RAM, más provoca `MemoryError`).
- Bancos de ejercicios: parte 1 a mano (`ejercicios/Fnn_*.md`), parte 2 generada (`python ejercicios/generar/generar.py`), banco único y solucionario (`python ejercicios/generar/banco_y_solucionario.py`), prueba final (`python prueba_final/generar_prueba.py`). Verificación: `python ejercicios/verificar/parte2.py` (motor = SymPy; 665 ejercicios sin códigos repetidos), `f12_f14.py`, `unidad9.py` y los de cada unidad. Detalles en `docs/02_plan_tecnico.md`, sección 11.

## 4. Posibles mejoras (opcionales)

- Ampliar el solucionario con una explicación en prosa por ejercicio (hoy cada solución del banco generado es el desarrollo calculado, sin comentario).
- Pasar la prueba final y el formulario a PDF (`pandoc` o el navegador) para imprimirlos.
- Añadir una unidad opcional: inversa y determinante (el tema siguiente natural; L55 lo menciona).
- Escuchar la narración de las lecciones más largas por si algún término suena raro con la voz sintética.

## 5. Trampas técnicas conocidas

- En `Tex`/`MathTex`: nada de «», ª ni `\color{#hex}`. En `Text`: evitar ℝ, ≠, ↦, ∅ y los subíndices Unicode `ₖ ₚ ₙ ᵢ` (salen cuadros blancos).
- En f-strings con LaTeX, `\text{…}` choca con las llaves: concatenar cadenas.
- `Arrow` de longitud 0 falla (usar `Dot`). No animar `VGroup` improvisados de objetos ya en escena (`desplazar`); tras animar piezas de una matriz, `consolidar(matriz)`.
- Dejar sitio abajo para el `pie`. `ajustar_al_encuadre` es una red de seguridad pero **no recoloca**: si el grupo estaba pegado a un lado, tras escalar hay que volver a colocarlo (`to_edge`, `set_x(0)`). Un panel de texto de más de ~6 unidades de ancho pisa unos ejes a la izquierda (usar `panel_derecha`).
- `manim.cfg`: `no_latex_cleanup = True` y rutas de salida cortas (límite de 260 caracteres de Windows). Con varios `manim` en paralelo puede fallar `FileNotFoundError` en `media\Tex\*.svg`: repetir esa escena sola.
- `C:\ffmpeg\ffmpeg.exe` está roto; Manim usa PyAV y no lo necesita.
- Scripts en Bash: un `heredoc` con barras invertidas las duplica o las pierde (y `\1080` en un f-string se convierte en un carácter de control). Para escribir código con LaTeX, usa la herramienta de escritura de archivos.
