import { readFileSync, existsSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const aqui = dirname(fileURLToPath(import.meta.url))
const plataforma = join(aqui, '..')
const raiz = join(plataforma, '..')
const rutaCatalogo = join(plataforma, 'public', 'catalogo.json')

const errores = []
if (!existsSync(rutaCatalogo)) {
  console.error('ERROR: no existe public/catalogo.json. Ejecuta "npm run catalogo".')
  process.exit(1)
}

const catalogo = JSON.parse(readFileSync(rutaCatalogo, 'utf8'))
const unidades = catalogo.unidades || []
const lecciones = unidades.flatMap((u) => u.lecciones || [])
const videos = lecciones.flatMap((l) => l.videos || [])

if (unidades.length !== 10) errores.push(`se esperaban 10 unidades y hay ${unidades.length}`)
if (videos.length !== 142) errores.push(`se esperaban 142 videos y hay ${videos.length}`)

for (const unidad of unidades) {
  if (!unidad.lecciones || unidad.lecciones.length === 0)
    errores.push(`la unidad ${unidad.numero} no tiene lecciones`)
}

for (const video of videos) {
  const nombre = `${video.leccion} · ${video.numero}`
  if (!video.ruta || !existsSync(join(raiz, video.ruta)))
    errores.push(`${nombre}: no existe el mp4 "${video.ruta}"`)
  if (!video.vtt || !existsSync(join(plataforma, 'public', video.vtt)))
    errores.push(`${nombre}: falta el vtt "${video.vtt}"`)
  if (!video.duracion || !Number.isFinite(video.segundos) || video.segundos <= 0)
    errores.push(`${nombre}: duración vacía o inválida`)
}

for (const leccion of lecciones) {
  if (leccion.guion && !existsSync(join(raiz, leccion.guion)))
    errores.push(`${leccion.id}: no existe el guion "${leccion.guion}"`)
}

for (const familia of catalogo.ejercicios?.familias || []) {
  for (const ruta of [familia.parte1, familia.parte2, familia.solucion]) {
    if (ruta && !existsSync(join(raiz, ruta)))
      errores.push(`${familia.id}: no existe "${ruta}"`)
  }
  if (!familia.parte1 && !familia.parte2)
    errores.push(`${familia.id}: no tiene ningún archivo de ejercicios`)
}

if (errores.length) {
  console.error(`FALLÓ la verificación (${errores.length} problemas):`)
  for (const error of errores) console.error(' - ' + error)
  process.exit(1)
}

console.log(
  `OK: ${unidades.length} unidades, ${lecciones.length} lecciones, ${videos.length} videos, ` +
    `todas las rutas y subtítulos existen.`
)
