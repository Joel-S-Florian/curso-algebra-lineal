import sys
import av
from PIL import Image

video, salida, cada = sys.argv[1], sys.argv[2], float(sys.argv[3])
cuadros, siguiente = [], 0.0
with av.open(video) as c:
    for f in c.decode(video=0):
        if f.time >= siguiente:
            cuadros.append(f.to_image().resize((640, 360)))
            siguiente += cada
cols = 4
filas = (len(cuadros) + cols - 1) // cols
hoja = Image.new("RGB", (640 * cols, 360 * filas))
for i, im in enumerate(cuadros):
    hoja.paste(im, ((i % cols) * 640, (i // cols) * 360))
hoja.save(salida)
