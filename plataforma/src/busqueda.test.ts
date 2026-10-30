import { describe, expect, it } from 'vitest'
import { buscar, normalizar } from './busqueda'
import type { Catalogo, Leccion, Unidad, Video } from './tipos'

function video(leccion: string, numero: number, titulo: string): Video {
  return {
    leccion,
    numero,
    titulo,
    ruta: `videos/${leccion}-${numero}.mp4`,
    duracion: '10:00',
    segundos: 600,
    srt: null,
    vtt: null,
  }
}

function leccion(id: string, titulo: string, videos: Video[]): Leccion {
  return { id, titulo, guion: null, ejercicios: [], videos }
}

const unidades: Unidad[] = [
  {
    numero: 8,
    titulo: 'Núcleo e imagen',
    lecciones: [leccion('L43', 'El núcleo y la imagen', [video('L43', 1, 'Qué es el núcleo')])],
  },
  {
    numero: 9,
    titulo: 'Síntesis',
    lecciones: [leccion('L50', 'Repaso final', [video('L50', 1, 'Cierre del curso')])],
  },
]

const catalogo: Catalogo = {
  totales: { unidades: 2, lecciones: 2, videos: 2 },
  unidades,
  material: {
    formulario: { titulo: 'Formulario de conceptos', ruta: 'material/formulario.md' },
    metodos: { titulo: 'Métodos de resolución', ruta: 'material/metodos.md' },
    plan: { titulo: 'Plan de estudio sugerido', ruta: 'material/plan_de_estudio.md' },
    banco: { titulo: 'Banco de ejercicios', ruta: 'ejercicios/BANCO.md' },
    solucionario: { titulo: 'Solucionario', ruta: 'solucionario/README.md', familias: [] },
    pruebaFinal: { titulo: 'Prueba final', ruta: 'prueba_final/PRUEBA_FINAL.md' },
    solucionPruebaFinal: {
      titulo: 'Solución de la prueba final',
      ruta: 'prueba_final/SOLUCION_PRUEBA_FINAL.md',
    },
  },
  ejercicios: { familias: [], indice: {} },
}

describe('normalizar', () => {
  it('quita tildes y mayúsculas', () => {
    expect(normalizar('NÚCLEO e Imagen')).toBe('nucleo e imagen')
    expect(normalizar('Métodos')).toBe('metodos')
  })
})

describe('buscar', () => {
  it('encuentra con y sin tildes, sin distinguir mayúsculas', () => {
    const conTilde = buscar(catalogo, 'núcleo')
    const sinTilde = buscar(catalogo, 'NUCLEO')
    expect(conTilde).toEqual(sinTilde)
    expect(conTilde.some((resultado) => resultado.tipo === 'unidad')).toBe(true)
    expect(conTilde.some((resultado) => resultado.tipo === 'leccion')).toBe(true)
    expect(conTilde.some((resultado) => resultado.tipo === 'video')).toBe(true)
  })

  it('agrupa por tipo y devuelve destinos válidos', () => {
    const resultados = buscar(catalogo, 'sintesis')
    expect(resultados).toHaveLength(1)
    expect(resultados[0]).toMatchObject({
      tipo: 'unidad',
      destino: '#/video/L50-1',
    })
    expect(buscar(catalogo, 'metodos')).toContainEqual(
      expect.objectContaining({ tipo: 'material', destino: '#/material/metodos' })
    )
  })

  it('devuelve vacío para consultas en blanco o sin coincidencias', () => {
    expect(buscar(catalogo, '   ')).toEqual([])
    expect(buscar(catalogo, 'zzzz')).toEqual([])
  })
})
