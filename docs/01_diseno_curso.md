# Fase 1 — Diseño del curso

**Curso visual de Sistemas de Ecuaciones Lineales con Python y Manim**

Este documento es el mapa del curso: qué se aprende, en qué orden, por qué en ese orden, cómo se divide en videos y cómo se organizan los ejercicios. Todo lo que se produzca en las fases siguientes se ajusta a este mapa.

---

## 1. Punto de partida: qué se supone que ya sabes

Casi nada, a propósito. Solo se supone:

- Leer y escribir números enteros y decimales.
- Sumar, restar, multiplicar y dividir números enteros "a mano" o con calculadora.

Todo lo demás se enseña dentro del curso, en el momento en que hace falta. La Unidad 0 (lecciones L01–L04) existe para eso.

### 1.1 Prerrequisitos que el curso enseña y dónde se usan

| Concepto previo | Se enseña en | Se usa por primera vez en |
|---|---|---|
| Números naturales, enteros, racionales y reales; la recta real | L01 | L05 |
| Reglas de los signos, fracciones, jerarquía de operaciones | L01 | L06 |
| Propiedades conmutativa, asociativa, distributiva; opuesto e inverso | L01 | L06 (despejar), L18 (matrices) |
| Variable, incógnita, constante, expresión, término, coeficiente | L02 | L05 |
| Igualdad, ecuación, solución, ecuaciones equivalentes | L02 | L05 |
| Por qué "pasar un término al otro lado" es válido (sumar lo mismo a ambos lados) | L02 | L06, L13–L15 |
| Par y terna ordenada, plano cartesiano, espacio de 3 coordenadas | L03 | L07 |
| Gráfica de una ecuación como conjunto de puntos; pendiente de una recta | L03 | L07, L08 |
| Conjuntos: pertenencia ∈, conjunto vacío ∅, notación {x : …} | L04 | L08 (conjunto solución) |
| Subíndices (x₁, a₂₃) y sumatorio Σ | L04 | L10 (sistemas m×n) |
| Lógica: implicación ⇒, equivalencia ⇔, condición necesaria y suficiente, contraejemplo | L04 | L11, L40 (Rouché-Frobenius) |
| Demostración directa y por contradicción (reducción al absurdo) | L04 | L11, L54 |
| Vector, combinación lineal (idea inicial) | L17, L19 | L19 (Ax como combinación de columnas) |
| Matrices elementales | L34 | L35 (origen de LU) |
| Combinación lineal, espacio generado, independencia, base, dimensión (formal) | L43–L44 | L45–L50 (núcleo e imagen) |

### 1.2 Convenciones de todo el curso

- **Notación**: incógnitas `x, y, z` en sistemas pequeños; `x₁, x₂, …, xₙ` en general. Matriz `A` de tamaño `m×n` (m filas, n columnas); `aᵢⱼ` es el elemento de la fila `i`, columna `j`. Vectores en negrita en el texto (**x**, **b**) y como columnas en las fórmulas.
- **Filas**: `Rᵢ` es la fila `i`. Una operación se escribe `R₂ ← R₂ − 3R₁` ("la nueva fila 2 es la fila 2 menos tres veces la fila 1").
- **Números**: se trabaja con fracciones exactas, no con decimales redondeados. El punto decimal solo aparece en la lección de errores numéricos.
- **Código de colores** (fijo en `curso/estilo.py`; un color significa siempre lo mismo):

| Color | Significado |
|---|---|
| Azul | coeficientes / matriz A |
| Naranja | términos independientes / vector b |
| Amarillo | pivotes y elemento que se está usando |
| Verde | variables libres y parámetros |
| Verde claro con recuadro | solución final |
| Violeta | operación por filas que se aplica |
| Rojo | error, contradicción, caso prohibido |

- **Intuición frente a demostración**: cada vez que una animación sugiera un resultado, el video lo dirá explícitamente ("esto es una intuición visual, no una demostración") y la demostración aparecerá aparte, con hipótesis enunciadas.

---

## 2. Secuencia pedagógica

### 2.1 La idea que guía el orden

El curso cuenta una sola historia: **"¿cuántas soluciones tiene un sistema lineal, cómo las encuentro y por qué?"**. Cada unidad responde una parte:

1. **Unidad 0–1**: qué es un sistema y qué aspecto tienen sus soluciones (geometría: rectas y planos).
2. **Unidad 2**: cómo se resuelven a mano los sistemas pequeños.
3. **Unidad 3**: un lenguaje compacto para escribir cualquier sistema (matrices, `Ax = b`).
4. **Unidades 4–6**: algoritmos que funcionan para cualquier tamaño (Gauss, Gauss-Jordan, LU).
5. **Unidad 7**: decidir cuántas soluciones hay sin resolver del todo (rango, Rouché-Frobenius).
6. **Unidad 8**: entender la *estructura* del conjunto de soluciones (núcleo, imagen, rango-nulidad).
7. **Unidad 9**: juntar todo para resolver problemas nuevos.

### 2.2 Dos cambios de orden respecto al temario, justificados

1. **Los métodos elementales (Bloque III-A) van justo después del Bloque I**, antes de las matrices (Bloque II). Motivo: el método de reducción *es* la eliminación de Gauss escrita sin matrices. Si el estudiante ya lo domina, la matriz aumentada aparece como una forma de "ahorrarse escribir las letras", no como algo nuevo. El temario pide explicarlos "antes de los métodos matriciales", y así se cumple.
2. **Combinaciones lineales, independencia, base y dimensión (puntos C.3 y C.4 del Bloque IV-C) van antes del núcleo (IV-B)**. Motivo: para "encontrar una base del núcleo" (IV-B.5) hay que saber qué es una base. Se introducen una vez y se reutilizan en núcleo e imagen.

### 2.3 Plantilla de cada lección (los 10 pasos)

Cada lección se construye con la misma estructura. En los videos, los pasos 1–7 y 10 se animan; los pasos 8–9 viven en el material escrito (para que el estudiante intente antes de ver la solución).

| Paso | Dónde aparece |
|---|---|
| 1. Intuición | Video, primera escena |
| 2. Definición formal | Video + guion |
| 3. Representación visual | Video |
| 4. Ejemplo guiado | Video, paso a paso |
| 5. Justificación | Video (y demostración escrita si aplica) |
| 6. Caso alternativo | Video |
| 7. Errores frecuentes | Video corto final + guion |
| 8. Ejercicio propuesto | Fin del video (enunciado en pantalla) + archivo de ejercicios |
| 9. Solución explicada | Archivo de ejercicios (bloques desplegables) |
| 10. Resumen y conexión | Última escena del video |

### 2.4 Mapa de dependencias entre unidades

```
U0 Preliminares
 └─► U1 Ecuaciones y sistemas (Bloque I)
      ├─► U2 Métodos elementales (III-A)
      │    └─► U4 Gauss (III-B) ◄── U3
      └─► U3 Matrices y Ax=b (Bloque II)
                U4 Gauss ─► U5 Gauss-Jordan (III-C)
                U4 Gauss ─► U6 LU (III-D)
                U4 + U5 ─► U7 Rango y Rouché-Frobenius (IV-A)
                U3 + U5 + U7 ─► U8 Núcleo e imagen (IV-B, IV-C)
                Todo ─► U9 Síntesis (Bloque V)
```

---

## 3. Índice completo y división en lecciones

Cada lección (`Lnn`) es un archivo de escenas Manim y un guion. Cada **escena** es un video corto independiente (normalmente 2–6 minutos). No se fija duración: una escena termina cuando su idea está completa. Entre paréntesis, el punto del temario que cubre.

### Unidad 0 — Preliminares (lo que hace falta antes de empezar)

| Lección | Título | Escenas (videos) previstas |
|---|---|---|
| L00 | Bienvenida y prueba del entorno | `PruebaEntorno` — **ya producida** |
| L01 | Números reales y sus operaciones | `ConjuntosNumericos` (N⊂Z⊂Q⊂R en la recta), `ReglasDeSignos`, `Fracciones`, `PropiedadesDeLasOperaciones` (conmutativa, asociativa, distributiva, opuesto, inverso; por qué 0 no tiene inverso) |
| L02 | Expresiones, igualdades y ecuaciones | `VariableIncognitaCoeficiente`, `QueEsUnaEcuacion` (solución = valor que hace verdadera la igualdad), `TransformacionesQueConservanSoluciones` (sumar/multiplicar por ≠0 ambos lados; por qué multiplicar por 0 o elevar al cuadrado puede crear/perder soluciones) |
| L03 | Coordenadas: recta, plano y espacio | `ParesOrdenados`, `GraficaComoConjuntoDePuntos`, `PendienteDeUnaRecta`, `EspacioTresCoordenadas` |
| L04 | Lenguaje matemático | `ConjuntosYPertenencia`, `SubindicesYSumatorio`, `ImplicacionYEquivalencia` (necesaria vs suficiente con ejemplos cotidianos y numéricos), `ComoSeDemuestraAlgo` (directa, contradicción, contraejemplo) |

### Unidad 1 — Bloque I: Fundamentos de ecuaciones lineales

| Lección | Título (temario) | Escenas previstas |
|---|---|---|
| L05 | ¿Qué es una ecuación lineal? (I.1, I.2) | `DefinicionEcuacionLineal`, `LinealVsNoLineal` (x², xy, 1/x, sen x, √x: por qué cada una rompe la linealidad), `TrampasDeLinealidad` (2x + 3 = 0 sí; x·y = 1 no; "lineal en las incógnitas" vs en los parámetros) |
| L06 | Una incógnita: `ax = b` (I.3) | `DespejeJustificado`, `LosTresCasos` (a≠0 → una; a=0,b=0 → todas; a=0,b≠0 → ninguna) — semilla de toda la clasificación posterior |
| L07 | Dos y tres incógnitas (I.4, I.9) | `InfinitasSolucionesDeUnaEcuacion`, `EcuacionComoRecta`, `EcuacionComoPlano`, `ParametrizarUnaRecta` |
| L08 | Sistemas 2×2 (I.5, I.9) | `QueEsUnSistema` (solución simultánea; verificar sustituyendo), `RectasQueSeCortan`, `RectasParalelas`, `RectasCoincidentes` |
| L09 | Sistemas 3×3 (I.6, I.9) | `TresPlanosUnPunto`, `TresPlanosUnaRecta`, `TresPlanosSinPuntoComun` (paralelos, "prisma triangular", dos paralelos) |
| L10 | Sistemas m×n y homogéneos (I.7, I.8, I.9) | `NotacionGeneral` (aᵢⱼ, Σ), `HiperplanosYLimitesDelDibujo` (qué se puede y qué no se puede dibujar), `SistemasHomogeneos` (siempre tienen la solución trivial) |
| L11 | SCD, SCI, SI: ¿por qué 0, 1 o ∞? (I.10, I.11) | `ClasificacionDeSistemas`, `NuncaExactamenteDos` (demostración: si p y q son soluciones distintas, p + t(q − p) lo es para todo t real) |
| L12 | Casos especiales y errores frecuentes (I.12) | `MasEcuacionesQueIncognitas`, `MenosEcuacionesQueIncognitas` (no garantiza infinitas: puede ser incompatible), `ErroresFrecuentesBloqueI` |

### Unidad 2 — Bloque III-A: Métodos elementales

| Lección | Título | Escenas previstas |
|---|---|---|
| L13 | Sustitución | `SustitucionPasoAPaso`, `SustitucionCuandoConviene`, `SustitucionCasosEspeciales` (llegar a 0 = 0 o a 0 = 5) |
| L14 | Igualación | `IgualacionPasoAPaso`, `IgualacionInterpretacion` (igualar dos expresiones de y = cortar dos rectas) |
| L15 | Reducción y comparación | `ReduccionPasoAPaso`, `PorQueReduccionConservaSoluciones`, `ComparacionDeMetodos` (por qué ninguno escala bien a 4×4 o 10×10 → motivación de Gauss) |

### Unidad 3 — Bloque II: Representación matricial

| Lección | Título (temario) | Escenas previstas |
|---|---|---|
| L16 | Matrices (II.1, II.2) | `QueEsUnaMatriz` (tabla de números; dimensión m×n; elemento aᵢⱼ; igualdad), `TiposDeMatrices` (cuadrada, rectangular, nula, identidad, diagonal, triangular superior/inferior) ✅ |
| L17 | Vectores (II.3) | `VectorComoFlechaYComoPunto` (incluye fila, columna y traspuesta), `SumaYEscalarGeometricos`, `PrimeraCombinacionLineal` ✅ |
| L18 | Suma y producto por escalar (II.4) | `SumaDeMatrices` (solo misma dimensión), `ProductoPorEscalarYPropiedades` ✅ |
| L19 | Producto matriz-vector (II.5) | `FilaPorColumna` (producto escalar), `ComoCombinacionDeColumnas` (incluye las dos miradas) ✅ |
| L20 | Producto matricial (II.5) | `DimensionesYProcedimiento` ((m×n)(n×p) = m×p), `NoConmutatividadEIdentidad` ✅ |
| L21 | La matriz como transformación lineal (II.6) | `LaRejillaSeDeforma`, `ColumnasSonImagenesDeLaBase`, `QueSignificaLineal` (T(u+v) = T(u)+T(v), T(cu) = cT(u)) ✅ |
| L22 | De sistema a `Ax = b` (II.7, II.8, II.9) | `ConstruirAxb`, `AxReproduceLasEcuaciones` (término a término, fila por fila) ✅ |
| L23 | Matriz aumentada (II.10, II.11, II.12) | `SistemaAMatrizAumentada` (incluye A frente a [A∣b]), `SistemasEquivalentes` ✅ |

### Unidad 4 — Bloque III-B: Eliminación de Gauss

| Lección | Título (temario) | Escenas (✅ producidas; las pequeñas se agruparon) |
|---|---|---|
| L24 | Operaciones elementales (B.1–B.4) | `OperacionesElementales` (intercambio, escalar por k ≠ 0 y por qué, sumar múltiplo de otra fila), `CadaOperacionSeDeshace` (inversas ⇒ conservan el conjunto solución; demostración) |
| L25 | Forma escalonada y pivotes (B.5, B.6) | `FormaEscalonadaYPivotes` (definición, ejemplos, columnas y variables pivote), `LaEscalonadaNoEsUnica` (distintas escalonadas, mismos pivotes) |
| L26 | Eliminación hacia adelante y sustitución hacia atrás (B.7, B.8) | `GaussDosPorDos` (sistema y matriz a la vez, multiplicador, verificación), `GaussTresPorTres` (completo, con verificación) |
| L27 | Pivotes nulos y filas nulas (B.10, B.11) | `PivoteCeroIntercambio` (y columna sin pivote), `FilaNulaEcuacionRedundante` |
| L28 | Sin solución e infinitas (B.12) | `FilaContradictoria` ([0 0 0 ∣ c], c≠0), `VariablesLibresYSolucionParametrica` |
| L29 | Sistemas con parámetros (B.9) | `GaussConParametro`, `DiscutirPorCasos` (nunca dividir por una expresión que puede valer 0) |
| L30 | Errores frecuentes (B.13) | `ErroresFrecuentesGauss` (signos, columna b, operaciones ilegales, dos operaciones a la vez), `VerificarSiempre` |

### Unidad 5 — Bloque III-C: Gauss-Jordan

| Lección | Título (temario) | Escenas previstas |
|---|---|---|
| L31 | Forma escalonada reducida (C.1–C.3) | `DeEscalonadaAReducida`, `EliminarArribaYAbajo`, `LaReducidaEsUnica` (enunciado; idea de la demostración) |
| L32 | Variables básicas y libres (C.4–C.6) | `LeerLaSolucion`, `TresFinalesPosibles` (una, infinitas, ninguna) |
| L33 | Gauss frente a Gauss-Jordan (C.7) | `ContarOperaciones` (≈ n³/3 frente a ≈ n³/2 multiplicaciones), `CuandoConvieneCadaUno` |

### Unidad 6 — Bloque III-D: Factorización LU

| Lección | Título (temario) | Escenas previstas |
|---|---|---|
| L34 | Factorizar y matrices triangulares (D.1–D.3) | `QueEsFactorizar` (12 = 3·4; A = LU), `TriangularesYSustitucion`, `MatricesElementales` (cada operación por filas = multiplicar por una matriz) |
| L35 | De dónde sale A = LU (D.4, D.5) | `LosMultiplicadoresSeGuardan`, `ConstruirLyU` (L = producto de inversas de las elementales; por qué los multiplicadores caen en su sitio) |
| L36 | Resolver con LU (D.6–D.8) | `SustitucionHaciaAdelanteLy`, `SustitucionHaciaAtrasUx`, `EjemploCompletoLU` |
| L37 | Permutaciones y PA = LU (D.9, D.10) | `CuandoLUFalla` (pivote 0 en la posición diagonal), `MatricesDePermutacion`, `PivoteoParcial` (elegir el mayor en valor absoluto y por qué reduce errores de redondeo) |
| L38 | Comparación y aplicaciones (D.11, D.12) | `MuchosLadosDerechos` (factorizar una vez, resolver muchas), `TablaComparativa` |

### Unidad 7 — Bloque IV-A: Rango y Rouché-Frobenius

| Lección | Título (temario) | Escenas previstas |
|---|---|---|
| L39 | Rango (A.1–A.4) | `RangoComoNumeroDePivotes`, `RangoDeAyDeAumentada`, `RangoNoEsNumeroDeEcuaciones` |
| L40 | Teorema de Rouché-Frobenius (A.5–A.7) | `EnunciadoRF`, `DemostracionRF` (vía forma escalonada), `IncognitasRangoYLibres` (n − r variables libres) |
| L41 | Clasificación con ejemplos (A.8–A.10) | `EjemplosSCD`, `EjemplosSCI`, `EjemplosSI`, `ArbolDeDecision` |
| L42 | Discusión con parámetros (A.11, A.12) | `DiscusionConParametro`, `ClasificarSinResolver` (y por qué "A cuadrada" no implica "A invertible") |

### Unidad 8 — Bloques IV-B y IV-C: Núcleo e imagen

| Lección | Título (temario) | Escenas previstas |
|---|---|---|
| L43 | Combinaciones lineales y espacio generado (C.3) | `CombinacionLinealGeometrica`, `EspacioGenerado` (recta, plano, todo R²) |
| L44 | Independencia, subespacio, base, dimensión (C.4) | `DependenciaLineal`, `ComoComprobarIndependencia` (reducir a un sistema homogéneo), `BaseYDimension` |
| L45 | El núcleo (B.1–B.4, B.10) | `DefinicionNucleo`, `VectorNuloFrenteAEspacioNulo`, `ComprobarSiUnVectorEstaEnElNucleo` |
| L46 | Base y dimensión del núcleo (B.5–B.7) | `VariablesLibresDanLaBase`, `Nulidad` |
| L47 | Estructura de las soluciones (B.9) | `SolucionParticularMasNucleo` (x = xₚ + n, n ∈ ker A), `RectaTrasladada` (visual en R²/R³) |
| L48 | Espacio columna e imagen (C.1, C.2, C.8, C.9) | `AxEsCombinacionDeColumnas`, `ExisteSolucionSiiBEnCol`, `ImagenComoConjuntoAlcanzable` |
| L49 | Base del espacio columna (C.5–C.7) | `ColumnasPivote`, `PorQueEnLaMatrizOriginal` (las operaciones por filas cambian el espacio columna pero conservan las relaciones de dependencia entre columnas) |
| L50 | Teorema rango-nulidad (B.8, C.10) | `NucleoColapsaImagenSobrevive` (animación: R³ → R² aplastando una recta al origen), `DemostracionRangoNulidad` |

### Unidad 9 — Bloque V: Síntesis

| Lección | Título | Escenas previstas |
|---|---|---|
| L51 | Elegir el método | `ArbolDeDecisionDeMetodos` |
| L52 | Problemas integradores I (numéricos) | Una escena por problema (4–6 problemas) |
| L53 | Problemas integradores II (parámetros y estructura) | Una escena por problema (4–6 problemas) |
| L54 | Demostraciones | `DemostracionesClave` (no hay exactamente 2 soluciones; operaciones conservan soluciones; RF; rango-nulidad; estructura xₚ + ker A) |
| L55 | Repaso final | `MapaConceptual`, `PruebaIntegradora` (enunciados; solucionario escrito) |

**Total previsto**: 56 lecciones, ≈ 170 escenas (videos cortos).

---

## 4. Plan de ejercicios

### 4.1 Familias y volumen

Las familias siguen las unidades. El objetivo es "hasta 50" donde tiene sentido; en familias pequeñas se ponen menos para no repetir el mismo ejercicio con otros números.

| Familia | Contenido | N1 | N2 | N3 | N4 | N5 | Total |
|---|---|---|---|---|---|---|---|
| F00 | Preliminares: números, álgebra, coordenadas, lenguaje (✅ entregada) | 8 | 8 | 5 | 4 | 5 | 30 |
| F01 | Ecuaciones lineales: identificar, una incógnita (parte 1 ✅: 13) | 10 | 10 | 5 | 10 | 5 | 40 |
| F02 | Ecuaciones con 2–3 incógnitas y su geometría (parte 1 ✅: 10) | 8 | 8 | 4 | 6 | 4 | 30 |
| F03 | Sistemas 2×2 y 3×3: clasificación geométrica (parte 1 ✅: 19) | 10 | 10 | 6 | 8 | 6 | 40 |
| F04 | Métodos elementales (parte 1 ✅: 19) | 10 | 15 | 12 | 8 | 5 | 50 |
| F05 | Matrices y vectores: operaciones básicas (parte 1 ✅: 9) | 12 | 15 | 5 | 10 | 8 | 50 |
| F06 | Producto matricial y transformaciones (parte 1 ✅: 10) | 8 | 12 | 6 | 8 | 6 | 40 |
| F07 | Sistema ⇄ forma matricial (Ax = b, [A∣b]) (parte 1 ✅: 7) | 8 | 8 | 4 | 6 | 4 | 30 |
| F08 | Eliminación de Gauss (parte 1 ✅: 22) | 10 | 15 | 8 | 12 | 5 | 50 |
| F09 | Gauss-Jordan | 8 | 12 | 6 | 9 | 5 | 40 |
| F10 | Factorización LU y PA = LU | 6 | 12 | 6 | 10 | 6 | 40 |
| F11 | Rango y Rouché-Frobenius | 10 | 12 | 10 | 12 | 6 | 50 |
| F12 | Combinaciones lineales, independencia, base | 8 | 10 | 6 | 8 | 8 | 40 |
| F13 | Núcleo | 8 | 10 | 6 | 8 | 8 | 40 |
| F14 | Espacio columna e imagen | 8 | 10 | 6 | 8 | 8 | 40 |
| F15 | Problemas integradores | — | 5 | 10 | 10 | 5 | 30 |
| F16 | Demostraciones | — | — | 5 | 8 | 12 | 25 |
| | **Total** | | | | | | **665** |

Niveles: **N1** fundamentos y aplicación directa · **N2** rutinarios con varios pasos · **N3** elegir método · **N4** casos especiales, parámetros, errores comunes · **N5** integradores y demostraciones.

### 4.2 Tipo de ejercicio

Cada ejercicio lleva una etiqueta de tipo:

- **[C] Cálculo**: resolver, operar, factorizar, calcular rangos, bases.
- **[K] Conceptual**: decidir, explicar, clasificar sin calcular, encontrar el error en una resolución dada.
- **[D] Demostración**: probar una afirmación general o refutarla con un contraejemplo.

Reparto aproximado por familia: 60 % [C], 30 % [K], 10 % [D] (en F16, 100 % [D]).

### 4.3 Formato de cada ejercicio

Identificador: `F08-N4-03` (familia, nivel, número). Cada ejercicio tiene:

1. **Enunciado** (con tipo [C]/[K]/[D]).
2. **Objetivo de aprendizaje** (una frase: "Detectar una fila contradictoria").
3. **Dificultad** (N1–N5).
4. **Pistas progresivas** (2–3, cada una en un bloque desplegable; la primera orienta, la última casi resuelve).
5. **Solución completa y justificada** (desplegable).
6. **Verificación** (sustitución en el sistema original, o comprobación del producto `LU = A`, etc.).
7. **Errores frecuentes** asociados.

Los archivos se guardan en `ejercicios/Fnn_nombre.md` con bloques `<details>` (se ven plegados en VS Code, GitHub y la mayoría de visores Markdown).

### 4.4 Control de calidad de los ejercicios

- Todo resultado numérico se comprueba con un script de Python con aritmética exacta (fracciones, sin decimales redondeados) antes de publicarse; el script vivirá en `ejercicios/verificar/`.
- Los sistemas se diseñan "al revés" (se elige la solución y se construye el sistema) para que las cuentas a mano sean razonables, salvo en los ejercicios cuyo objetivo es precisamente manejar fracciones.

### 4.5 Orden de entrega

Los ejercicios de cada familia se entregan junto con su unidad (Fase 3), no antes. La Fase 5 los reúne en un banco único, un solucionario y una prueba final.

---

## 5. Plan de producción por fases

| Fase | Entregable | Estado |
|---|---|---|
| 1 | Este documento | ✅ |
| 2 | Entorno técnico, estructura del proyecto, escena de prueba renderizada | ✅ (ver `02_plan_tecnico.md`) |
| 3 | Unidades 0 → 9, una entrega por unidad: guiones, código, videos, ejercicios con soluciones | Unidades 0–9 ✅ (142 videos, L00–L55) |
| 4 | Revisión matemática y de render de cada unidad (se hace al cerrar cada entrega de la Fase 3) | Continua |
| 5 | Formulario, tabla comparativa de métodos, árbol de decisión, banco y solucionario, prueba final | ✅ (`material/`, `ejercicios/BANCO.md`, `solucionario/`, `prueba_final/`) |
