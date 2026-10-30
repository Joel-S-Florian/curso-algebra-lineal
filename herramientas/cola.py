"""Renderiza en -qh los archivos de escenas que se le pasen, con como mucho MAX renders de manim a la vez.

Uso (desde la raíz del proyecto): python cola.py escenas/l21_x.py escenas/l22_y.py ...
Si existe cola_extra.txt (una ruta por línea), también se encolan esas rutas a medida que aparecen.
"""

import subprocess
import sys
import time
from pathlib import Path

MAX = 3
AQUI = Path(__file__).parent
pendientes = list(sys.argv[1:])
hechos = set()


def en_marcha() -> int:
    salida = subprocess.run(["tasklist", "/FI", "IMAGENAME eq manim.exe", "/NH"], capture_output=True, text=True).stdout
    return salida.count("manim.exe")


while True:
    extra = AQUI / "cola_extra.txt"
    if extra.exists():
        for ruta in extra.read_text(encoding="utf-8").split():
            if ruta not in pendientes and ruta not in hechos:
                pendientes.append(ruta)
    if pendientes and en_marcha() < MAX:
        ruta = pendientes.pop(0)
        hechos.add(ruta)
        nombre = Path(ruta).stem[:3]
        with open(AQUI / f"r_{nombre}.err", "w") as err, open(AQUI / f"r_{nombre}.out", "w") as out:
            subprocess.Popen(["manim", "-qh", ruta, "-a"], stdout=out, stderr=err, creationflags=subprocess.CREATE_NO_WINDOW)
        print("lanzado", ruta, flush=True)
        time.sleep(5)
        continue
    if not pendientes and (AQUI / "cola_fin.txt").exists():
        break
    time.sleep(20)
