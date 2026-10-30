import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'node:fs'
import { join, dirname, basename } from 'node:path'
import { fileURLToPath } from 'node:url'

const aqui = dirname(fileURLToPath(import.meta.url))
const plataforma = join(aqui, '..')
const raiz = join(plataforma, '..')
const publico = join(plataforma, 'public')

const leer = (rel) => readFileSync(join(raiz, rel), 'utf8')
const tituloMd = (rel) => {
  const m = leer(rel).match(/^#\s+(.+)$/m)
  return m ? m[1].trim() : basename(rel)
}
const normalizar = (p) => p.replace(/\\/g, '/').replace(/^\.?\//, '')
const aSegundos = (texto) =>
  texto.split(':').map(Number).reduce((total, parte) => total * 60 + parte, 0)

const guiones = new Map()
for (const archivo of readdirSync(join(raiz, 'guiones'))) {
  const m = archivo.match(/^(l\d{2})_.*\.md$/)
  if (m) guiones.set(m[1].toUpperCase(), `guiones/${archivo}`)
}

// L51–L55 no tienen guion propio: el título real está en el diseño del curso.
const titulosDiseno = new Map()
for (const linea of leer('docs/01_diseno_curso.md').split(/\r?\n/)) {
  const m = linea.match(/^\|\s*(L\d{2})\s*\|\s*(.+?)\s*\|/)
  if (m && !titulosDiseno.has(m[1])) titulosDiseno.set(m[1], m[2].trim())
}

const cx = (n) => String(n).padStart(2, '0')
const aTexto = (segundos) =>
  Math.floor(segundos / 3600) > 0
    ? `${Math.floor(segundos / 3600)}:${cx(Math.floor((segundos % 3600) / 60))}:${cx(segundos % 60)}`
    : `${Math.floor(segundos / 60)}:${cx(segundos % 60)}`

const duracionDeSrt = (srt) => {
  const finales = [...leer(srt).matchAll(/-->\s*(\d{2}):(\d{2}):(\d{2}),\d{3}/g)]
  if (!finales.length) return null
  const [, h, m, s] = finales[finales.length - 1]
  return aTexto(Number(h) * 3600 + Number(m) * 60 + Number(s))
}

const unidades = []
const huerfanos = []
let unidadActual = null

for (const linea of leer('README.md').split(/\r?\n/)) {
  const mUnidad = linea.match(/^\|\s*\*\*Unidad\s+(\d+)\s+—\s+(.+?)\*\*\s*\|/)
  if (mUnidad) {
    unidadActual = { numero: Number(mUnidad[1]), titulo: mUnidad[2].trim(), lecciones: [] }
    unidades.push(unidadActual)
    continue
  }

  const mVid = linea.match(
    /^\|\s*(L(\d{2}))(?:\s*·\s*(\d+))?\s+(.+?)\s*\|\s*`([^`]+\.mp4)`\s*\|\s*(\d+:\d{2}(?::\d{2})?)?\s*\|/
  )
  if (!mVid) continue

  const leccion = mVid[1]
  const ruta = normalizar(mVid[5])
  const srt = ruta.replace(/\.mp4$/, '.srt')
  const tieneSrt = existsSync(join(raiz, srt))
  // Algunas filas (Unidad 3) no traen duración: se toma el último subtítulo.
  const duracion = mVid[6] || (tieneSrt ? duracionDeSrt(srt) : null)
  const video = {
    leccion,
    numero: mVid[3] ? Number(mVid[3]) : 1,
    titulo: mVid[4].trim(),
    ruta,
    duracion,
    segundos: duracion ? aSegundos(duracion) : null,
    srt: tieneSrt ? srt : null,
    vtt: tieneSrt ? 'subs/' + srt.slice('videos/'.length).replace(/\.srt$/, '.vtt') : null,
  }
  ;(unidadActual ? unidadActual.lecciones : huerfanos).push(video)
}

// L00 aparece en el README antes de la primera unidad: pertenece a la Unidad 0.
if (unidades.length && huerfanos.length) {
  unidadActual = unidades[0]
  for (const video of huerfanos) unidadActual.lecciones.push(video)
}

const crearLeccion = (id) => {
  const guion = guiones.get(id) || null
  const texto = guion ? leer(guion) : ''
  const lineaEjercicios = texto.match(/^\*\*Ejercicios\*\*:(.*)$/m)
  return {
    id,
    titulo: guion
      ? texto.match(/^#\s+(.+)$/m)[1].trim().replace(/^L\d{2}\s*[—-]\s*/, '')
      : titulosDiseno.get(id) || id,
    guion,
    ejercicios: lineaEjercicios
      ? [...new Set(lineaEjercicios[1].match(/F\d{2}/g) || [])]
      : [],
    videos: [],
  }
}

for (const unidad of unidades) {
  const lecciones = new Map()
  for (const video of unidad.lecciones) {
    if (!lecciones.has(video.leccion)) lecciones.set(video.leccion, crearLeccion(video.leccion))
    lecciones.get(video.leccion).videos.push(video)
  }
  unidad.lecciones = [...lecciones.values()]
}
unidades.sort((a, b) => a.numero - b.numero)

const srtAConvertir = new Set()
for (const unidad of unidades)
  for (const leccion of unidad.lecciones)
    for (const video of leccion.videos) if (video.srt) srtAConvertir.add(video.srt)

for (const srt of srtAConvertir) {
  const destino = join(publico, 'subs', srt.slice('videos/'.length).replace(/\.srt$/, '.vtt'))
  mkdirSync(dirname(destino), { recursive: true })
  const texto = leer(srt)
    .replace(/^\uFEFF/, '')
    .split(/\r?\n/)
    .map((linea) => linea.replace(/(\d{2}:\d{2}:\d{2}),(\d{3})/g, '$1.$2'))
    .join('\n')
  writeFileSync(destino, 'WEBVTT\n\n' + texto.trim() + '\n', 'utf8')
}

const familias = (() => {
  const texto = leer('solucionario/README.md')
  const lista = []
  for (const linea of texto.split(/\r?\n/)) {
    const m = linea.match(/^\|\s*(F\d{2})\s*\|\s*(.+?)\s*\|\s*\d+\s*\|\s*\[[^\]]+\]\(([^)]+)\)\s*\|/)
    if (m) lista.push({ id: m[1], titulo: m[2].trim(), ruta: 'solucionario/' + normalizar(m[3]) })
  }
  return lista
})()

const titulosFamilias = new Map(familias.map((familia) => [familia.id, familia.titulo]))
const familiasEjercicios = new Map()
const indiceEjercicios = {}

for (const archivo of readdirSync(join(raiz, 'ejercicios'))) {
  const m = archivo.match(/^(F\d{2})_(.+)\.md$/)
  if (!m) continue
  const id = m[1]
  const ruta = 'ejercicios/' + archivo
  const parte = m[2].endsWith('_parte2') ? 2 : 1
  const familia = familiasEjercicios.get(id) || {
    id,
    titulo: titulosFamilias.get(id) || m[2].replace(/_/g, ' '),
    parte1: null,
    parte2: null,
    solucion: `solucionario/${id}.md`,
  }
  if (parte === 2) familia.parte2 = ruta
  else familia.parte1 = ruta
  familiasEjercicios.set(id, familia)

  for (const encabezado of leer(ruta).matchAll(/^#{2,3}\s+(F\d{2}-[A-Z]\d-\d{2})\b/gm)) {
    indiceEjercicios[encabezado[1]] = { familia: id, parte }
  }
}

const ejercicios = {
  familias: [...familiasEjercicios.values()].sort((a, b) => a.id.localeCompare(b.id)),
  indice: indiceEjercicios,
}

const material = {
  formulario: { titulo: tituloMd('material/formulario.md'), ruta: 'material/formulario.md' },
  metodos: { titulo: tituloMd('material/metodos.md'), ruta: 'material/metodos.md' },
  plan: { titulo: tituloMd('material/plan_de_estudio.md'), ruta: 'material/plan_de_estudio.md' },
  banco: { titulo: tituloMd('ejercicios/BANCO.md'), ruta: 'ejercicios/BANCO.md' },
  solucionario: {
    titulo: tituloMd('solucionario/README.md'),
    ruta: 'solucionario/README.md',
    familias,
  },
  pruebaFinal: {
    titulo: tituloMd('prueba_final/PRUEBA_FINAL.md'),
    ruta: 'prueba_final/PRUEBA_FINAL.md',
  },
  solucionPruebaFinal: {
    titulo: tituloMd('prueba_final/SOLUCION_PRUEBA_FINAL.md'),
    ruta: 'prueba_final/SOLUCION_PRUEBA_FINAL.md',
  },
}

const totalLecciones = unidades.reduce((n, u) => n + u.lecciones.length, 0)
const totalVideos = unidades.reduce(
  (n, u) => n + u.lecciones.reduce((m, l) => m + l.videos.length, 0),
  0
)

const catalogo = {
  totales: { unidades: unidades.length, lecciones: totalLecciones, videos: totalVideos },
  unidades,
  material,
  ejercicios,
}

mkdirSync(publico, { recursive: true })
writeFileSync(join(publico, 'catalogo.json'), JSON.stringify(catalogo, null, 2) + '\n', 'utf8')

console.log(
  `Catálogo generado: ${unidades.length} unidades, ${totalLecciones} lecciones, ${totalVideos} videos, ` +
    `${srtAConvertir.size} subtítulos convertidos.`
)
