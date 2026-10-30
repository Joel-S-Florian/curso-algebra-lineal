"""Genera la prueba final integradora (enunciados y solucionario con baremo), con aritmética exacta.

Ejecutar desde la raíz del proyecto:  python prueba_final/generar_prueba.py
Salida: prueba_final/PRUEBA_FINAL.md y prueba_final/SOLUCION_PRUEBA_FINAL.md
"""

import random
import sys
from fractions import Fraction as F
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "ejercicios" / "generar"))

import algebra as al  # noqa: E402
import plantillas_a  # noqa: E402,F401
import plantillas_b as pb  # noqa: E402
import plantillas_c as pc  # noqa: E402
import plantillas_d as pd  # noqa: E402
from algebra import Ejercicio, aug, fila_vec, mat, t, vec  # noqa: E402

r = random.Random(20261029)

# (puntos, título, ejercicio)
problemas = []

# 1. Gauss 3x3 (SCD)
problemas.append((10, "Eliminación gaussiana", pb.f08_unica(r)))

# 2. Gauss-Jordan y solución general (SCI)
problemas.append((10, "Gauss-Jordan y solución general", pc.f09_indeterminado(r)))

# 3. LU con dos lados derechos
A, L, U = pc.lu_azar(r)
bs = [[F(r.randint(-4, 5)) for _ in range(3)] for _ in range(2)]
sol_lu = f"$L = {mat(L)}$, $U = {mat(U)}$ (multiplicadores: " + ", ".join(f"$\\ell_{{{i + 1}{j + 1}}} = {t(L[i][j])}$" for j in range(3) for i in range(j + 1, 3)) + ").\n\n"
for k, b in enumerate(bs, 1):
    y = al.sust_adelante(L, b)
    x = al.sust_atras(U, y)
    assert al.por_vec(A, x) == b
    sol_lu += f"Para $\\mathbf{{b}}_{k}$: $L\\mathbf{{y}} = \\mathbf{{b}}_{k}$ da $\\mathbf{{y}} = {fila_vec(y)}$; $U\\mathbf{{x}} = \\mathbf{{y}}$ da $\\mathbf{{x}} = {fila_vec(x)}$.\n\n"
ej3 = Ejercicio(
    "C", 3, "LU", "", f"Factoriza $A = {mat(A)}$ como $A = LU$ y resuelve $A\\mathbf{{x}} = \\mathbf{{b}}_k$ para $\\mathbf{{b}}_1 = {fila_vec(bs[0])}$ y $\\mathbf{{b}}_2 = {fila_vec(bs[1])}$ usando la factorización.",
    sol_lu.strip() + "\n\nCoste: factorizar una vez; cada lado derecho, dos sustituciones.",
)
problemas.append((10, "Factorización LU", ej3))

# 4. Parámetro
problemas.append((12, "Sistema con un parámetro", pd.f15_param_completo(r)))

# 5. Rango, núcleo, espacio columna
problemas.append((12, "Rango, núcleo y espacio columna", pd.f15_ficha(r, tam=(3, 5))))

# 6. Modelado
problemas.append((8, "Modelado", pd.f15_mezcla(r)))

# 7. Verdadero o falso
problemas.append((8, "Verdadero o falso", pd.f15_vf(r)))

# 8. Clasificar sin resolver (tres sistemas)
partes, soluciones = [], []
for tipo in ("SCD", "SCI", "SI"):
    A8, b8 = pc.sistema_tipo(r, 3, 4 if tipo == "SCI" else 3, tipo)
    ra, rab, cl = pc.clasifica_rf(A8, b8)
    assert cl == tipo
    partes.append(f"${al.sistema(A8, b8)}$")
    extra = f" Parámetros libres: $n - \\operatorname{{rg}}(A) = {len(A8[0])} - {ra} = {len(A8[0]) - ra}$." if cl == "SCI" else ""
    soluciones.append(f"$\\operatorname{{rg}}(A) = {ra}$, $\\operatorname{{rg}}[A \\mid \\mathbf{{b}}] = {rab}$, $n = {len(A8[0])}$: {pc.NOMBRE[cl]}.{extra}")
ej8 = Ejercicio(
    "C", 3, "Rouché-Frobenius", "", "Sin resolverlos, clasifica cada sistema (y di cuántos parámetros libres tiene si es indeterminado):\n\n" + "\n\n".join(f"{chr(97 + i)}) {p}" for i, p in enumerate(partes)),
    "\n\n".join(f"{chr(97 + i)}) {s}" for i, s in enumerate(soluciones)),
)
problemas.append((10, "Clasificar sin resolver", ej8))

# 9. Demostración
problemas.append((10, "Demostración", next(d for d in pd.DEMOS if d.titulo == "Diferencia de soluciones")))

# 10. Integrador (4x4)
problemas.append((10, "Problema integrador", pd.f15_ficha(r, tam=(4, 4))))

assert sum(p for p, _, _ in problemas) == 100

enunciados = ["# Prueba final integradora\n",
              "**Duración**: 2 horas · **Puntos**: 100 · **Material**: sin apuntes ni calculadora (todas las cuentas son con fracciones sencillas).\n",
              "Justifica cada respuesta. Verifica en el sistema original siempre que sea posible. Las soluciones y el baremo están en `SOLUCION_PRUEBA_FINAL.md`: corrígete **después** de entregar.\n",
              "| Problema | Tema | Puntos |", "|---|---|---|"]
for i, (p, nombre, _) in enumerate(problemas, 1):
    enunciados.append(f"| {i} | {nombre} | {p} |")
enunciados.append("")
soluciones_md = ["# Prueba final integradora: soluciones y baremo\n",
                 "Todos los resultados se calcularon con aritmética exacta (`prueba_final/generar_prueba.py`). Si falta una comprobación en tu respuesta, resta la quinta parte de los puntos del apartado.\n"]
for i, (p, nombre, e) in enumerate(problemas, 1):
    enunciados.append(f"## Problema {i} — {nombre} ({p} puntos)\n\n{e.enunciado}\n")
    soluciones_md.append(f"## Problema {i} — {nombre} ({p} puntos)\n\n**Enunciado.** {e.enunciado}\n\n**Solución.** {e.solucion}\n")
    soluciones_md.append("**Baremo.** Planteamiento correcto: 30 %. Cálculo sin errores: 40 %. Verificación e interpretación: 20 %. Presentación y justificación: 10 %.\n")

(RAIZ / "prueba_final" / "PRUEBA_FINAL.md").write_text("\n".join(enunciados), encoding="utf-8")
(RAIZ / "prueba_final" / "SOLUCION_PRUEBA_FINAL.md").write_text("\n".join(soluciones_md), encoding="utf-8")
print("prueba generada:", len(problemas), "problemas,", sum(p for p, _, _ in problemas), "puntos")
