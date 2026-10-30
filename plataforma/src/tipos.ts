export type Video = {
  leccion: string
  numero: number
  titulo: string
  ruta: string
  duracion: string
  segundos: number
  srt: string | null
  vtt: string | null
}

export type Leccion = {
  id: string
  titulo: string
  guion: string | null
  ejercicios: string[]
  videos: Video[]
}

export type Unidad = {
  numero: number
  titulo: string
  lecciones: Leccion[]
}

export type FamiliaEjercicios = {
  id: string
  titulo: string
  parte1: string | null
  parte2: string | null
  solucion: string
}

export type EntradaMaterial = { titulo: string; ruta: string }

export type Catalogo = {
  totales: { unidades: number; lecciones: number; videos: number }
  unidades: Unidad[]
  material: {
    formulario: EntradaMaterial
    metodos: EntradaMaterial
    plan: EntradaMaterial
    banco: EntradaMaterial
    solucionario: EntradaMaterial & { familias: EntradaMaterial[] }
    pruebaFinal: EntradaMaterial
    solucionPruebaFinal: EntradaMaterial
  }
  ejercicios: {
    familias: FamiliaEjercicios[]
    indice: Record<string, { familia: string; parte: 1 | 2 }>
  }
}
