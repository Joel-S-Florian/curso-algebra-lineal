"""Comprueba la segunda parte de los bancos (ejercicios generados) y el motor de álgebra exacta que los calcula.

1. El motor (ejercicios/generar/algebra.py) coincide con SymPy en rref, rango, núcleo, determinante, LU y PA = LU
   sobre cientos de matrices al azar.
2. Los bancos tienen en total 665 ejercicios, sin códigos repetidos, y todos con enunciado y solución.

Ejecutar desde la raíz del proyecto:  python ejercicios/verificar/parte2.py
"""

import random
import re
import sys
from fractions import Fraction as F
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "ejercicios" / "generar"))

import sympy as sp  # noqa: E402

import algebra as al  # noqa: E402

r = random.Random(7)


def a_sympy(A):
    return sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in f] for f in A])


def de_sympy(S):
    return [[F(int(v.p), int(v.q)) for v in S.row(i)] for i in range(S.rows)]


for _ in range(400):
    m, n = r.randint(1, 5), r.randint(1, 5)
    A = [[F(r.randint(-3, 4)) for _ in range(n)] for _ in range(m)]
    S = a_sympy(A)
    red, piv = al.rref(A)
    Sred, Spiv = S.rref()
    assert red == de_sympy(Sred) and tuple(piv) == tuple(Spiv)
    assert al.rango(A) == S.rank()
    base = al.nucleo(A)
    assert len(base) == n - S.rank()
    assert all(al.por_vec(A, v) == [0] * m for v in base)
    if m == n:
        assert al.det(A) == de_sympy(sp.Matrix([[S.det()]]))[0][0]
        lu_ = al.lu(A)
        if lu_:
            L, U = lu_
            assert al.mul(L, U) == A
        if S.det() != 0:
            P, L, U = al.plu(A)
            assert al.mul(P, A) == al.mul(L, U)
            assert all(U[i][j] == 0 for i in range(n) for j in range(i))
            assert all(L[i][j] == 0 for i in range(n) for j in range(i + 1, n)) and all(L[i][i] == 1 for i in range(n))
    b = [F(r.randint(-3, 4)) for _ in range(m)]
    res = al.resolver(A, b)
    Sb = sp.Matrix([[sp.Rational(v.numerator, v.denominator)] for v in b])
    consistente = S.rank() == S.row_join(Sb).rank()
    assert (res[0] != "SI") == consistente
    if res[0] != "SI":
        assert al.por_vec(A, res[1]) == b

# --- recuento de los bancos
codigos, total = [], 0
for archivo in sorted((RAIZ / "ejercicios").glob("F*.md")):
    texto = archivo.read_text(encoding="utf-8")
    bloques = re.split(r"^### ", texto, flags=re.M)[1:]
    for bloque in bloques:
        codigo = re.match(r"(F\d\d-N\d-\d+)", bloque)
        assert codigo, (archivo.name, bloque[:40])
        codigos.append(codigo.group(1))
        assert "Enunciado" in bloque and "<summary>Solución</summary>" in bloque, (codigo.group(1), "falta enunciado o solución")
total = len(codigos)
repetidos = {c for c in codigos if codigos.count(c) > 1}
assert not repetidos, repetidos
assert total == 665, total
print(f"Motor de álgebra exacta = SymPy en 400 matrices; {total} ejercicios, sin códigos repetidos: todo correcto")
