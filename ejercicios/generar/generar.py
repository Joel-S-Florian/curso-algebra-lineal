"""Genera la segunda parte de los bancos de ejercicios (ejercicios/Fnn_*_parte2.md) con aritmética exacta.

Ejecutar desde la raíz del proyecto:  python ejercicios/generar/generar.py [F01 F02 ...]
Cada ejercicio se construye a partir de una plantilla y su solución se calcula, no se escribe a mano.
Los códigos de la parte 2 empiezan en 11 dentro de cada nivel (la parte 1 usa 01–10).
"""

import random
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
RAIZ = AQUI.parents[1]

import plantillas_a  # noqa: E402
import plantillas_b  # noqa: E402
import plantillas_c  # noqa: E402
import plantillas_d  # noqa: E402

PLAN = {**plantillas_a.PLAN, **plantillas_b.PLAN, **plantillas_c.PLAN, **plantillas_d.PLAN}

# familia -> (archivo de la parte 1 sin extensión, título, lecciones)
FAMILIAS = {
    "F01": ("F01_ecuaciones_lineales", "Ecuaciones lineales", "L05–L06"),
    "F02": ("F02_ecuaciones_varias_incognitas", "Ecuaciones con varias incógnitas", "L07"),
    "F03": ("F03_sistemas_y_clasificacion", "Sistemas y clasificación", "L08–L12"),
    "F04": ("F04_metodos_elementales", "Métodos elementales", "L13–L15"),
    "F05": ("F05_matrices_y_vectores", "Matrices y vectores", "L16–L18"),
    "F06": ("F06_producto_y_transformaciones", "Producto matricial y transformaciones", "L19–L21"),
    "F07": ("F07_sistema_y_forma_matricial", "Sistema y forma matricial", "L22–L23"),
    "F08": ("F08_gauss", "Eliminación de Gauss", "L24–L30"),
    "F09": ("F09_gauss_jordan", "Gauss-Jordan", "L31–L33"),
    "F10": ("F10_factorizacion_lu", "Factorización LU", "L34–L38"),
    "F11": ("F11_rango_rouche_frobenius", "Rango y Rouché-Frobenius", "L39–L42"),
    "F12": ("F12_combinaciones_independencia_base", "Combinaciones, independencia y base", "L43–L44"),
    "F13": ("F13_nucleo", "Núcleo", "L45–L47"),
    "F14": ("F14_espacio_columna_imagen", "Espacio columna e imagen", "L48–L50"),
    "F15": ("F15_problemas_integradores", "Problemas integradores", "L51–L53"),
    "F16": ("F16_demostraciones", "Demostraciones", "L54"),
}


def formatear(familia: str, codigo: str, e) -> str:
    s = f"### {codigo} · [{e.tipo}] {e.titulo}\n\n**Objetivo**: {e.objetivo}\n**Dificultad**: N{e.nivel}\n\n**Enunciado.** {e.enunciado}\n\n"
    for i, p in enumerate(e.pistas, 1):
        s += f"<details><summary>Pista {i}</summary>{p}</details>\n"
    s += f"<details><summary>Solución</summary>\n\n{e.solucion}\n\n</details>\n"
    if e.errores:
        s += f"<details><summary>Errores frecuentes</summary>{e.errores}</details>\n"
    return s + "\n"


def generar_familia(familia: str, semilla: int = 2026) -> list:
    r = random.Random(semilla + int(familia[1:]))
    ejercicios, vistos = [], set()
    for plantilla, veces in PLAN[familia]:
        hechos, intentos = 0, 0
        while hechos < veces:
            intentos += 1
            if intentos > 60:
                raise RuntimeError(f"{familia}: {plantilla.__name__} no produce {veces} ejercicios distintos")
            e = plantilla(r)
            if e.enunciado in vistos:
                continue
            vistos.add(e.enunciado)
            ejercicios.append(e)
            hechos += 1
    return ejercicios


def escribir(familia: str) -> int:
    archivo, titulo, lecciones = FAMILIAS[familia]
    ejercicios = sorted(generar_familia(familia), key=lambda e: e.nivel)  # estable: conserva el orden dentro del nivel
    contador = Counter()
    cuerpo = ""
    por_nivel = Counter()
    for e in ejercicios:
        contador[e.nivel] += 1
        codigo = f"{familia}-N{e.nivel}-{10 + contador[e.nivel]}"
        e.codigo = codigo
        por_nivel[e.nivel] += 1
        cuerpo += formatear(familia, codigo, e)
    tipos = Counter(e.tipo for e in ejercicios)
    cabecera = (
        f"# {familia} — {titulo} (parte 2)\n\n"
        f"Segunda parte del banco de las lecciones {lecciones}: **{len(ejercicios)} ejercicios** de práctica que completan la parte 1 (`{archivo}.md`).\n\n"
        "- **Niveles**: N1–N5 · **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Los códigos de esta parte empiezan en 11 dentro de cada nivel.\n"
        "- Cada ejercicio se generó con una plantilla y su solución se **calculó con aritmética exacta** (fracciones); el generador está en `ejercicios/generar/` y se puede volver a ejecutar.\n"
        "- Reparto: " + ", ".join(f"N{n}: {por_nivel[n]}" for n in sorted(por_nivel)) + " · " + ", ".join(f"[{k}] {v}" for k, v in sorted(tipos.items())) + ".\n\n---\n\n"
    )
    (RAIZ / "ejercicios" / f"{archivo}_parte2.md").write_text(cabecera + cuerpo, encoding="utf-8")
    return len(ejercicios)


if __name__ == "__main__":
    objetivo = sys.argv[1:] or sorted(PLAN)
    total = 0
    for fam in objetivo:
        n = escribir(fam)
        total += n
        print(fam, n)
    print("total", total)
