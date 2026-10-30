import type { Catalogo, Unidad } from './tipos'

export type ProgresoUnidad = {
  numero: number
  titulo: string
  total: number
  vistos: number
  porcentaje: number
}

export type ResumenProgreso = {
  unidades: ProgresoUnidad[]
  total: number
  vistos: number
  porcentaje: number
}

export type LeccionPendiente = {
  unidad: number
  unidadTitulo: string
  leccionId: string
  leccionTitulo: string
  total: number
  vistos: number
  primerPendiente: string
}

export function porcentaje(vistos: number, total: number): number {
  if (total <= 0) return 0
  return Math.round((vistos / total) * 100)
}

export function duracionUnidad(unidad: Unidad): number {
  return unidad.lecciones
    .flatMap((leccion) => leccion.videos)
    .reduce((suma, video) => suma + (video.segundos || 0), 0)
}

export function formatearDuracion(segundos: number): string {
  const total = Math.max(0, Math.round(segundos))
  const horas = Math.floor(total / 3600)
  const minutos = Math.floor((total % 3600) / 60)
  const resto = total % 60
  if (horas > 0) return `${horas} h ${String(minutos).padStart(2, '0')} min`
  if (minutos > 0) return `${minutos} min ${String(resto).padStart(2, '0')} s`
  return `${resto} s`
}

export function calcularProgreso(
  catalogo: Catalogo,
  vistos: Record<string, boolean>
): ResumenProgreso {
  const unidades: ProgresoUnidad[] = []
  let total = 0
  let vistosTotal = 0

  for (const unidad of catalogo.unidades) {
    const videos = unidad.lecciones.flatMap((leccion) => leccion.videos)
    const vistosUnidad = videos.filter(
      (video) => vistos[`${video.leccion}-${video.numero}`]
    ).length
    total += videos.length
    vistosTotal += vistosUnidad
    unidades.push({
      numero: unidad.numero,
      titulo: unidad.titulo,
      total: videos.length,
      vistos: vistosUnidad,
      porcentaje: porcentaje(vistosUnidad, videos.length),
    })
  }

  return { unidades, total, vistos: vistosTotal, porcentaje: porcentaje(vistosTotal, total) }
}

export function leccionesPendientes(
  catalogo: Catalogo,
  vistos: Record<string, boolean>
): LeccionPendiente[] {
  const pendientes: LeccionPendiente[] = []

  for (const unidad of catalogo.unidades) {
    for (const leccion of unidad.lecciones) {
      const total = leccion.videos.length
      const vistosLeccion = leccion.videos.filter(
        (video) => vistos[`${video.leccion}-${video.numero}`]
      ).length
      if (vistosLeccion >= total) continue
      const primero = leccion.videos.find(
        (video) => !vistos[`${video.leccion}-${video.numero}`]
      )
      if (!primero) continue
      pendientes.push({
        unidad: unidad.numero,
        unidadTitulo: unidad.titulo,
        leccionId: leccion.id,
        leccionTitulo: leccion.titulo,
        total,
        vistos: vistosLeccion,
        primerPendiente: `${primero.leccion}-${primero.numero}`,
      })
    }
  }

  return pendientes
}
