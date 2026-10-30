"""Voz sintética de la narración: texto -> mp3 con edge-tts (voces neuronales de Microsoft).

El texto se envía al servicio en línea de Microsoft; cada frase se descarga una sola vez
y queda en caché en media/voz/ (si se cambia el texto, la voz o la velocidad, se genera otra).
"""

import hashlib
from pathlib import Path

import av
import edge_tts
from manim import config

VOZ = "es-MX-DaliaNeural"
VELOCIDAD = "-5%"  # algo más pausada que la voz por defecto: hay fórmulas que leer


def audio(texto: str) -> tuple[Path, float]:
    """Devuelve el mp3 con `texto` leído y su duración en segundos."""
    texto = " ".join(texto.split())
    clave = hashlib.sha1(f"{VOZ}|{VELOCIDAD}|{texto}".encode()).hexdigest()[:16]
    ruta = Path(config.media_dir) / "voz" / f"{clave}.mp3"
    if not ruta.exists():
        ruta.parent.mkdir(parents=True, exist_ok=True)
        temporal = ruta.with_suffix(".tmp")  # un render interrumpido no deja un mp3 a medias en la caché
        edge_tts.Communicate(texto, VOZ, rate=VELOCIDAD).save_sync(str(temporal))
        temporal.replace(ruta)
    with av.open(str(ruta)) as contenedor:
        return ruta, contenedor.duration / 1e6
