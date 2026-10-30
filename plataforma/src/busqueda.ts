import type { Catalogo } from './tipos'

export type TipoResultado = 'unidad' | 'leccion' | 'video' | 'material'

export type ResultadoBusqueda = {
  tipo: TipoResultado
  id: string
  titulo: string
  detalle: string
  destino: string
}

export function normalizar(texto: string): string {
  return texto
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim()
}

function coincide(consulta: string, ...textos: string[]): boolean {
  return textos.some((texto) => normalizar(texto).includes(consulta))
}

export function buscar(catalogo: Catalogo, consulta: string): ResultadoBusqueda[] {
  const q = normalizar(consulta)
  if (!q) return []

  const resultados: ResultadoBusqueda[] = []

  for (const unidad of catalogo.unidades) {
    const videos = unidad.lecciones.flatMap((leccion) => leccion.videos)
    const primero = videos[0]
    if (
      coincide(q, unidad.titulo, `unidad ${unidad.numero}`) &&
      primero
    ) {
      resultados.push({
        tipo: 'unidad',
        id: `unidad-${unidad.numero}`,
        titulo: `Unidad ${unidad.numero} — ${unidad.titulo}`,
        detalle: `${unidad.lecciones.length} lecciones · ${videos.length} videos`,
        destino: `#/video/${primero.leccion}-${primero.numero}`,
      })
    }

    for (const leccion of unidad.lecciones) {
      const primerVideo = leccion.videos[0]
      if (coincide(q, leccion.titulo, leccion.id) && primerVideo) {
        resultados.push({
          tipo: 'leccion',
          id: `leccion-${leccion.id}`,
          titulo: `${leccion.id} — ${leccion.titulo}`,
          detalle: `Unidad ${unidad.numero} · ${unidad.titulo}`,
          destino: `#/video/${primerVideo.leccion}-${primerVideo.numero}`,
        })
      }

      for (const video of leccion.videos) {
        if (coincide(q, video.titulo, leccion.titulo, video.leccion)) {
          resultados.push({
            tipo: 'video',
            id: `video-${video.leccion}-${video.numero}`,
            titulo: video.titulo,
            detalle: `${video.leccion} · ${leccion.titulo} · video ${video.numero}`,
            destino: `#/video/${video.leccion}-${video.numero}`,
          })
        }
      }
    }
  }

  const material = [
    catalogo.material.formulario,
    catalogo.material.metodos,
    catalogo.material.plan,
    catalogo.material.banco,
    catalogo.material.pruebaFinal,
    catalogo.material.solucionPruebaFinal,
  ]
  const destinos = [
    '#/material/formulario',
    '#/material/metodos',
    '#/material/plan',
    '#/material/banco',
    '#/material/prueba',
    '#/material/solucion-prueba',
  ]
  material.forEach((entrada, i) => {
    if (coincide(q, entrada.titulo)) {
      resultados.push({
        tipo: 'material',
        id: 'material-' + i,
        titulo: entrada.titulo,
        detalle: 'Material',
        destino: destinos[i],
      })
    }
  })

  return resultados
}
