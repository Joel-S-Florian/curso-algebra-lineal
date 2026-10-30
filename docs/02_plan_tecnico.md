# Fase 2 — Plan técnico

## 1. Versión de Python

- **Recomendada: Python 3.12 o 3.13.** Manim Community 0.22 funciona en 3.10–3.13.
- En este equipo: **Python 3.13.13** con **Manim Community 0.22.0** ya instalado. La escena de prueba se renderizó con esa combinación.

## 2. Instalación de Manim

En Windows, desde la carpeta del proyecto:

```bash
python -m pip install -r requirements.txt
```

`requirements.txt` fija `manim==0.22.0` para que el proyecto se renderice igual dentro de un año. Si prefieres aislarlo del resto de tu Python:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\python -m pip install -r requirements.txt
```

(después, usa `.venv\Scripts\manim` en lugar de `manim`).

Manim 0.22 trae su propio códec de video (PyAV): **no necesita un ffmpeg instalado aparte**. (El `C:\ffmpeg\ffmpeg.exe` de este equipo está roto, le falta `swscale-10.dll`; Manim no lo usa, así que no afecta).

## 3. Dependencias adicionales

- `edge-tts` (en `requirements.txt`): genera la voz de la narración con las voces neuronales de Microsoft. **Necesita internet** la primera vez que se renderiza cada frase: el texto se envía a ese servicio, y el mp3 queda en caché en `media/voz/`, así que volver a renderizar no lo descarga otra vez.
- Los ejercicios se verifican con `fractions` de la biblioteca estándar (no hace falta nada más).

### Narración

- `curso/voz.py`: elige la voz (`VOZ = "es-MX-DaliaNeural"`) y la velocidad (`VELOCIDAD = "-5%"`). Cambiarlas ahí cambia todas las lecciones al volver a renderizar.
- En una escena, dos formas:
  - `self.decir("frase")` (la habitual): la voz empieza y las animaciones siguientes van a la vez. La frase siguiente, `limpiar`, `cambiar_encabezado` y el final del video esperan a que termine (`callar`), así que nunca se pisan dos frases ni se borra la pantalla a mitad de frase.
  - `with self.narrar("frase"):` y dentro, las animaciones de esa frase; al salir del bloque se espera a que la frase termine.
- `mostrar_portada`, `ejercicio_propuesto` y `resumen` narran solos (título de la parte, «pausa el video e inténtalo», las ideas del resumen); con `voz="…"` se cambia el texto. Si las ideas del resumen tienen fórmulas, conviene pasar `voz=` con la lectura en palabras.
- En el texto de la voz, los números y las letras se escriben como se dicen ("equis más ye igual a cinco", "el punto tres, dos"): leídas tal cual, las fórmulas suenan mal.
- Cada video narrado sale con su `.srt` (subtítulos) al lado. Manim deja también un `.wav` (la mezcla de audio) que se puede borrar.
- No se usa `manim-voiceover`: depende de `pkg_resources` (que va a desaparecer de setuptools), rebaja `python-dotenv` y pide SoX; lo que hacía falta de él son unas 20 líneas en `narrar`.

## 4. LaTeX

Manim usa LaTeX para todo lo que se escribe con `MathTex` y `Tex` (fórmulas, matrices). El texto normal en español (`Text`) no usa LaTeX.

- En este equipo: **MiKTeX** ya instalado (`latex.exe` y `dvisvgm.exe` en `C:\Program Files\MiKTeX`). Funciona con tildes en `Tex`.
- En otro equipo con Windows: instalar MiKTeX y activar *"Install missing packages on the fly: Yes"* en MiKTeX Console. Paquetes que usa el curso: `amsmath`, `amssymb` (vienen por defecto).

## 5. Comandos para renderizar

Siempre **desde la carpeta raíz del proyecto** (donde está `manim.cfg`):

| Para qué | Comando |
|---|---|
| Borrador rápido (480p, 15 fps) y abrir el video | `manim -pql escenas/l00_prueba_entorno.py PruebaEntorno` |
| Calidad final (1080p, 60 fps) | `manim -qh escenas/l00_prueba_entorno.py PruebaEntorno` |
| Todas las escenas de un archivo | `manim -qh escenas/lNN_nombre.py -a` |
| Solo el último fotograma (revisar la composición) | `manim -sql escenas/l00_prueba_entorno.py PruebaEntorno` |

## 6. Calidad recomendada

| Uso | Resolución | Relación | fps | Bandera |
|---|---|---|---|---|
| Mientras se escribe una escena | 854×480 | 16:9 | 15 | `-ql` |
| Video para estudiar | 1920×1080 | 16:9 | 60 | `-qh` |

1080p60 es la calidad final: fórmulas nítidas en pantalla completa y movimientos suaves. 4K (`-qk`) cuadruplica el tiempo de render y no mejora la lectura de fórmulas.

## 7. Estructura de carpetas

```
(raíz del proyecto)
├── README.md               ← empieza aquí: dónde están los videos y cómo regenerarlos
├── manim.cfg               ← configuración de Manim (carpetas de salida, color de fondo)
├── requirements.txt
├── docs/
│   ├── 01_diseno_curso.md  ← Fase 1: mapa del curso, lecciones, plan de ejercicios
│   └── 02_plan_tecnico.md  ← este documento
├── curso/                  ← código compartido por todas las lecciones
│   ├── estilo.py           ← código de colores y tamaños
│   └── componentes.py      ← títulos, ecuaciones alineadas, matriz aumentada…
├── escenas/                ← un archivo por lección: lNN_nombre.py
├── guiones/                ← un guion por lección: lNN_nombre.md
├── ejercicios/             ← (Fase 3) banco por familias Fnn_nombre.md
├── videos/                 ← SALIDA: videos/<lección>/<calidad>/<Escena>.mp4
└── media/                  ← caché de Manim (se puede borrar)
```

## 8. Organización del código

- **Una lección = un archivo** en `escenas/`; **una escena = un video corto** (una clase `Scene`).
- Dentro de cada escena, la clase se divide en métodos por sección pedagógica (`portada`, `sistema_a_matriz`, …): el código se lee en el mismo orden que el guion.
- Lo que se repite entre lecciones vive en `curso/`:
  - `estilo.py`: el código de colores del curso (pivote = amarillo, libre = verde…). Nunca se escribe un color "a mano" en una escena.
  - `componentes.py`:
    - `EscenaCurso`: clase base de todas las escenas. Ofrece `mostrar_portada`, `encabezado` / `cambiar_encabezado`, `pie` (sustituye solo al pie anterior), `ejercicio_propuesto` (paso 8 de la metodología), `resumen` (paso 10), `limpiar` y `desplazar`. Para escenas 3D: `class X(EscenaCurso, ThreeDScene)`; los rótulos quedan fijos en pantalla automáticamente.
    - `ajustar_al_encuadre`: red de seguridad que reduce un objeto que no cabe.
    - `alinear_por_igual` (sistemas con los `=` alineados), `sustituir_alineado` (cambiar una ecuación sin que salte de sitio), `matriz_aumentada` (matriz con la barra de `[A | b]`), `lista`.
  - Unidad 4: `matriz_gauss` (matriz aumentada a partir de números o textos, con `b` en naranja y pivotes en amarillo) y `EscenaCurso.operar_filas` (anima intercambio, escalado o reemplazo: rótulo violeta, filas resaltadas, cuenta de la fila y fila nueva en su sitio; calcula el resultado con fracciones exactas, o lo recibe en `nueva=` si hay parámetros); `escalera` (línea bajo los pivotes), `parrafo` (líneas de `Tex` alineadas a la izquierda: un `Tex` de más de unos 75 caracteres se corta solo) y `meter_en_encuadre`.
  - Se añadirán componentes cuando una segunda lección los necesite.
  - En `Text` (Pango) los subíndices ₁ ₂ ₃ sí se ven, pero ᵢ ⱼ no: para filas genéricas, escribe con palabras o usa `MathTex`.
- **Texto**: la prosa va con `Text` (Pango, tipografía del sistema); las fórmulas con `MathTex`, y las frases con fórmulas dentro con `Tex`. Dentro de `Tex` las comillas se escriben ``` ``así'' ``` (las comillas « » no existen en la fuente de LaTeX por defecto).
- **Revisión visual**: tras cada render de borrador se genera una hoja de fotogramas (uno cada 5 s) y se revisa que nada se salga del encuadre ni se solape.

## 9. Aviso: límite de 260 caracteres de Windows

Windows, por defecto, no admite rutas de más de 260 caracteres, y Manim crea archivos intermedios con nombres de 64 caracteres. Si el proyecto está en una carpeta con una ruta muy larga, el render termina el video pero luego muestra un error `FileNotFoundError` al limpiar. Soluciones (cualquiera vale):

- Tener el proyecto en una ruta corta, por ejemplo `C:\Users\<tú>\Documents\Desarrollo\curso-sistemas-lineales`.
- O activar las rutas largas en Windows (requiere permisos de administrador; lo haces tú, desde PowerShell como administrador):
  `New-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem -Name LongPathsEnabled -Value 1 -PropertyType DWORD -Force`

## 10. Escena de prueba: resultado

`escenas/l00_prueba_entorno.py`, clase `PruebaEntorno`. Ejercita todo lo que usará el curso: texto con tildes, fórmulas LaTeX, matrices, `TransformMatchingTex`, una operación por filas, ejes con rectas y una comprobación final.

- Renderizada en 480p15 y 1080p60 (≈ 77 s). Fotogramas revisados: sin solapamientos ni elementos fuera del encuadre (se corrigieron dos desbordes en el borde derecho tras el primer render).
- Durante la prueba, la ruta larga de la carpeta temporal de esta sesión provocó el error de la sección 9 después de generar el video; el video está completo.

## 11. Material de estudio de la Fase 5 y cómo se regenera

Todo lo que no es video se genera o se comprueba con scripts de aritmética exacta (`fractions.Fraction`), y se puede volver a ejecutar desde la raíz del proyecto:

| Qué | Dónde | Cómo se genera o comprueba |
|---|---|---|
| Parte 2 de los bancos (434 ejercicios de práctica) | `ejercicios/Fnn_*_parte2.md` | `python ejercicios/generar/generar.py` (plantillas en `plantillas_a.py` a `plantillas_d.py`; semilla fija, el resultado es reproducible) |
| Banco único e índice (665 ejercicios) | `ejercicios/BANCO.md` | `python ejercicios/generar/banco_y_solucionario.py` |
| Solucionario por familia | `solucionario/Fnn.md` | el mismo script (lee las soluciones de los bancos) |
| Prueba final integradora (2 h, 100 puntos) y su solución con baremo | `prueba_final/` | `python prueba_final/generar_prueba.py` |
| Formulario y tabla/árbol de decisión de métodos | `material/formulario.md`, `material/metodos.md` | escritos a mano |
| Verificadores | `ejercicios/verificar/` | `parte2.py` (motor de álgebra = SymPy en 400 matrices; 665 ejercicios sin códigos repetidos), `f12_f14.py`, `unidad9.py` y los anteriores |

Notas de diseño:

- `ejercicios/generar/algebra.py` es el motor: rref, rango, núcleo, LU, PA = LU, sustituciones y formato LaTeX. Todo ejercicio generado calcula su solución con él, no a mano.
- Los códigos de la parte 2 empiezan en 11 dentro de cada nivel (`F08-N3-21`); la parte 1 usa 01–10. `curso/componentes.py` (`archivo_de`) dirige el rótulo «Pistas y solución» de un video al archivo correcto.
- Los ejercicios de las lecciones L51–L55 apuntan a ejercicios del banco por código (`F15-N3-11`, `F16-N5-11`…); si se cambian los números de las plantillas hay que revisar esas referencias.
- Con scripts en Bash: evita `heredoc` con barras invertidas (se duplican o se pierden); usa la herramienta de escritura de archivos.
