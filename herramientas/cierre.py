"""Tras los renders: comprueba audio y subtítulos, borra los .wav y pone las duraciones reales en el README.

Uso (desde la raíz del proyecto): python cierre.py
"""

import re
from pathlib import Path

import av

videos = sorted(Path("videos").glob("l*/1080p60/*.mp4"))
sin_audio, sin_srt = [], []
for v in videos:
    with av.open(str(v)) as c:
        if not any(s.type == "audio" for s in c.streams):
            sin_audio.append(v)
    if not v.with_suffix(".srt").exists():
        sin_srt.append(v)
for w in Path("videos").glob("l*/1080p60/*.wav"):
    w.unlink()

readme = Path("README.md")
texto = readme.read_text(encoding="utf-8")


def duracion(m: re.Match) -> str:
    ruta = Path(m.group(1).replace("\\", "/"))
    if not ruta.exists():
        return m.group(0)
    with av.open(str(ruta)) as c:
        s = round(c.duration / 1e6)
    return f"`{m.group(1)}` | {s // 60}:{s % 60:02d} |"


texto = re.sub(r"`(videos\\[^`]+\.mp4)` \| [^|]* \|", duracion, texto)
readme.write_text(texto, encoding="utf-8")

print(f"{len(videos)} videos; sin audio: {len(sin_audio)}; sin srt: {len(sin_srt)}")
for v in sin_audio:
    print("  sin audio:", v)
