"""Busca contenido pegado al borde del encuadre (texto cortado) en los videos finales.

Uso: python bordes.py <carpeta_raiz> <salida.txt> [patron]
Muestrea un fotograma cada 3 s y mira una banda de 14 px en los cuatro lados.
"""

import sys
from pathlib import Path

import av
import numpy as np

raiz, salida = Path(sys.argv[1]), Path(sys.argv[2])
patron = sys.argv[3] if len(sys.argv) > 3 else "l*/1080p60/*.mp4"
BANDA, PASO, UMBRAL = 14, 3.0, 45

informe = []
videos = sorted(raiz.glob(f"videos/{patron}"))
for ruta in videos:
    marcas = {}
    with av.open(str(ruta)) as c:
        flujo = c.streams.video[0]
        dur = float(c.duration) / 1e6
        t = 1.0
        fondo = None
        while t < dur - 0.5:
            c.seek(int(t * 1e6))
            try:
                f = next(c.decode(video=0))
            except StopIteration:
                break
            a = f.to_ndarray(format="rgb24").astype(np.int16)
            if fondo is None:
                fondo = a[2, 2].copy()
            d = np.abs(a - fondo).max(axis=2) > UMBRAL
            lados = {
                "izq": d[:, :BANDA].sum(), "der": d[:, -BANDA:].sum(),
                "arriba": d[:BANDA, :].sum(), "abajo": d[-BANDA:, :].sum(),
            }
            for lado, n in lados.items():
                if n >= 6:
                    marcas.setdefault(lado, []).append((round(f.time, 1), int(n)))
            t += PASO
    if marcas:
        resumen = "; ".join(f"{lado}: {len(v)} muestras (primera a {v[0][0]} s, {v[0][1]} px)" for lado, v in marcas.items())
        informe.append(f"{ruta.relative_to(raiz)}  ->  {resumen}")
    print(ruta.name, "ok" if not marcas else "MARCADO", flush=True)
salida.write_text("\n".join(informe) + f"\n\n{len(videos)} videos revisados, {len(informe)} marcados\n", encoding="utf-8")
