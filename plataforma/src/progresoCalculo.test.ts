import { describe, expect, it } from 'vitest'
import {
  calcularProgreso,
  formatearDuracion,
  leccionesPendientes,
  porcentaje,
} from './progresoCalculo'
import type { Catalogo, Leccion, Unidad, Video } from './tipos'

function video(leccion: string, numero: number, segundos = 600): Video {
  return {
    leccion,
    numero,
    titulo: `Video ${numero}`,
    ruta: `videos/${leccion}-${numero}.mp4`,
    duracion: '10:00',
    segundos,
    srt: null,
    vtt: null,
  }
}

function leccion(id: string, titulo: string, videos: Video[]): Leccion {
  return { id, titulo, guion: null, ejercicios: [], videos }
}

const unidades: Unidad[] = [
  {
    numero: 1,
    titulo: 'Sistemas',
    lecciones: [
      leccion('L01', 'Introducción', [video('L01', 1), video('L01', 2)]),
      leccion('L02', 'Métodos', [video('L02', 1)]),
    ],
  },
  {
    numero: 2,
    titulo: 'Matrices',
    lecciones: [leccion('L03', 'Operaciones', [video('L03', 1, 1800)])],
  },
]

const catalogo: Catalogo = {
  totales: { unidades: 2, lecciones: 3, videos: 4 },
  unidades,
  material: {
    formulario: { titulo: '', ruta: '' },
    metodos: { titulo: '', ruta: '' },
    plan: { titulo: '', ruta: '' },
    banco: { titulo: '', ruta: '' },
    solucionario: { titulo: '', ruta: '', familias: [] },
    pruebaFinal: { titulo: '', ruta: '' },
    solucionPruebaFinal: { titulo: '', ruta: '' },
  },
  ejercicios: { familias: [], indice: {} },
}

describe('calcularProgreso', () => {
  it('calcula porcentajes por unidad y total', () => {
    const resumen = calcularProgreso(catalogo, { 'L01-1': true, 'L02-1': true })
    expect(resumen.unidades[0]).toMatchObject({ total: 3, vistos: 2, porcentaje: 67 })
    expect(resumen.unidades[1]).toMatchObject({ total: 1, vistos: 0, porcentaje: 0 })
    expect(resumen).toMatchObject({ total: 4, vistos: 2, porcentaje: 50 })
  })

  it('redondea y evita división por cero', () => {
    expect(porcentaje(1, 3)).toBe(33)
    expect(porcentaje(2, 3)).toBe(67)
    expect(porcentaje(0, 0)).toBe(0)
  })
})

describe('leccionesPendientes', () => {
  it('lista solo lecciones con videos sin ver', () => {
    const pendientes = leccionesPendientes(catalogo, {
      'L01-1': true,
      'L01-2': true,
      'L02-1': true,
      'L03-1': true,
    })
    expect(pendientes).toEqual([])

    const parcial = leccionesPendientes(catalogo, { 'L01-1': true })
    expect(parcial.map((item) => item.leccionId)).toEqual(['L01', 'L02', 'L03'])
    expect(parcial[0]).toMatchObject({
      unidad: 1,
      vistos: 1,
      total: 2,
      primerPendiente: 'L01-2',
    })
  })
})

describe('formatearDuracion', () => {
  it('muestra horas, minutos o segundos', () => {
    expect(formatearDuracion(1800)).toBe('30 min 00 s')
    expect(formatearDuracion(3661)).toBe('1 h 01 min')
    expect(formatearDuracion(45)).toBe('45 s')
  })
})
