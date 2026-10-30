"""Reúne los bancos de ejercicios (parte 1 y parte 2) en un banco único y un solucionario por familia.

Ejecutar desde la raíz del proyecto:  python ejercicios/generar/banco_y_solucionario.py
Salida: ejercicios/BANCO.md y solucionario/Fnn.md (+ solucionario/README.md).
"""

import re
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
EJ = RAIZ / "ejercicios"
SOL = RAIZ / "solucionario"
SOL.mkdir(exist_ok=True)

NOMBRES = {
    "F00": "Preliminares", "F01": "Ecuaciones lineales", "F02": "Ecuaciones con varias incógnitas", "F03": "Sistemas y clasificación",
    "F04": "Métodos elementales", "F05": "Matrices y vectores", "F06": "Producto matricial y transformaciones", "F07": "Sistema y forma matricial",
    "F08": "Eliminación de Gauss", "F09": "Gauss-Jordan", "F10": "Factorización LU", "F11": "Rango y Rouché-Frobenius",
    "F12": "Combinaciones, independencia y base", "F13": "Núcleo", "F14": "Espacio columna e imagen", "F15": "Problemas integradores", "F16": "Demostraciones",
}


def leer_ejercicios():
    """Devuelve {familia: [dict(codigo, tipo, titulo, nivel, enunciado, solucion, archivo)]}."""
    familias = defaultdict(list)
    for archivo in sorted(EJ.glob("F*.md")):
        texto = archivo.read_text(encoding="utf-8")
        for bloque in re.split(r"^### ", texto, flags=re.M)[1:]:
            cab = re.match(r"(F(\d\d)-N(\d)-(\d+)) · \[(\w)\] (.*)", bloque)
            enun = re.search(r"\*\*Enunciado\.\*\*\s*(.*?)(?=\n\s*<details>|\Z)", bloque, re.S)
            sol = re.search(r"<summary>Solución</summary>\s*(.*?)\s*</details>", bloque, re.S)
            assert cab and enun and sol, bloque[:60]
            familias["F" + cab.group(2)].append(dict(
                codigo=cab.group(1), tipo=cab.group(5), titulo=cab.group(6).replace(" 🎬", "").strip(), nivel=int(cab.group(3)),
                num=int(cab.group(4)), enunciado=enun.group(1).strip(), solucion=sol.group(1).strip(), archivo=archivo.name,
            ))
    for fam in familias:
        familias[fam].sort(key=lambda e: (e["nivel"], e["num"]))
    return familias


def main():
    familias = leer_ejercicios()
    total = sum(len(v) for v in familias.values())

    # ---------------------------------------------------------------- solucionario
    indice = ["# Solucionario\n", f"Soluciones completas de los **{total} ejercicios** del curso, una página por familia. Cada entrada repite el enunciado y da la solución justificada; las pistas y los errores frecuentes están en el banco (`ejercicios/`).\n",
              "Cómo usarlo: intenta el ejercicio, mira solo una pista del banco si te atascas y comprueba aquí tu resultado. Si tu respuesta difiere, revisa los pasos: las soluciones calculadas se han comprobado con aritmética exacta.\n",
              "| Familia | Tema | Ejercicios | Página |", "|---|---|---|---|"]
    for fam in sorted(familias):
        ejs = familias[fam]
        partes = [f"# Solucionario {fam} — {NOMBRES[fam]}\n", f"{len(ejs)} ejercicios. Bancos de origen: " + ", ".join(sorted({f'`{e["archivo"]}`' for e in ejs})) + ".\n"]
        nivel_actual = None
        for e in ejs:
            if e["nivel"] != nivel_actual:
                nivel_actual = e["nivel"]
                partes.append(f"\n## Nivel N{nivel_actual}\n")
            partes.append(f"### {e['codigo']} · [{e['tipo']}] {e['titulo']}\n\n**Enunciado.** {e['enunciado']}\n\n**Solución.** {e['solucion']}\n")
        (SOL / f"{fam}.md").write_text("\n".join(partes), encoding="utf-8")
        indice.append(f"| {fam} | {NOMBRES[fam]} | {len(ejs)} | [{fam}.md]({fam}.md) |")
    (SOL / "README.md").write_text("\n".join(indice) + "\n", encoding="utf-8")

    # ---------------------------------------------------------------- banco único
    por_nivel = {fam: Counter(e["nivel"] for e in ejs) for fam, ejs in familias.items()}
    por_tipo = Counter(e["tipo"] for ejs in familias.values() for e in ejs)
    banco = [
        "# Banco único de ejercicios\n",
        f"**{total} ejercicios** en 17 familias (F00–F16). Cada familia tiene una parte 1 (ligada a los videos) y, desde F01, una parte 2 de práctica generada y comprobada con aritmética exacta (`ejercicios/generar/`). Soluciones completas: `solucionario/`.\n",
        "- **Niveles**: N1 fundamentos · N2 rutinarios · N3 elegir método · N4 casos especiales y parámetros · N5 integradores y demostraciones.",
        "- **Tipos**: [C] cálculo · [K] conceptual · [D] demostración. Reparto total: " + ", ".join(f"[{k}] {v}" for k, v in sorted(por_tipo.items())) + ".\n",
        "## Resumen por familia y nivel\n",
        "| Familia | Tema | N1 | N2 | N3 | N4 | N5 | Total |", "|---|---|---|---|---|---|---|---|",
    ]
    suma = Counter()
    for fam in sorted(familias):
        c = por_nivel[fam]
        banco.append(f"| {fam} | {NOMBRES[fam]} | " + " | ".join(str(c.get(n, 0)) for n in range(1, 6)) + f" | {sum(c.values())} |")
        suma.update(c)
    banco.append("| | **Total** | " + " | ".join(str(suma.get(n, 0)) for n in range(1, 6)) + f" | **{total}** |\n")
    banco.append("## Índice\n")
    for fam in sorted(familias):
        banco.append(f"### {fam} — {NOMBRES[fam]}\n")
        banco.append("| Código | Tipo | Título | Archivo |\n|---|---|---|---|")
        for e in familias[fam]:
            banco.append(f"| {e['codigo']} | {e['tipo']} | {e['titulo']} | `{e['archivo']}` |")
        banco.append("")
    (EJ / "BANCO.md").write_text("\n".join(banco), encoding="utf-8")
    print(total, "ejercicios;", len(familias), "familias")


if __name__ == "__main__":
    main()
