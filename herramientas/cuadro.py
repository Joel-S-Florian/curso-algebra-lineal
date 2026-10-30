import sys

import av
from PIL import Image

video, t, salida = sys.argv[1], float(sys.argv[2]), sys.argv[3]
with av.open(video) as c:
    c.seek(int(t * 1e6))
    for f in c.decode(video=0):
        if f.time >= t:
            f.to_image().resize((1280, 720)).save(salida)
            break
