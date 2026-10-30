import express from 'express'
import { extname, join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const aqui = dirname(fileURLToPath(import.meta.url))
const raiz = join(aqui, '..')
const dist = join(aqui, 'dist')
const PUERTO = 5173
const PERMITIDAS = new Set(['.mp4', '.srt', '.vtt', '.md', '.json', '.png'])

const app = express()
app.disable('x-powered-by')

app.use(
  '/raw',
  (req, res, next) => {
    if (req.method !== 'GET' && req.method !== 'HEAD') {
      return res.status(405).send('Método no permitido')
    }
    let ruta
    try {
      ruta = decodeURIComponent(req.path)
    } catch {
      return res.status(400).send('Ruta inválida')
    }
    if (ruta.includes('\0') || ruta.includes('\\') || /(^|\/)\.\.(\/|$)/.test(ruta)) {
      return res.status(403).send('Ruta prohibida')
    }
    if (!PERMITIDAS.has(extname(ruta).toLowerCase())) {
      return res.status(403).send('Extensión no permitida')
    }
    next()
  },
  express.static(raiz, {
    dotfiles: 'deny',
    index: false,
    redirect: false,
    fallthrough: true,
    setHeaders: (respuesta) => respuesta.setHeader('Cache-Control', 'no-store'),
  })
)

app.use('/raw', (_req, res) => res.status(404).send('No encontrado'))

app.use(express.static(dist, { index: 'index.html' }))

app.use((_req, res) => res.status(404).send('No encontrado'))

app.listen(PUERTO, '127.0.0.1', () => {
  console.log(`Plataforma en http://127.0.0.1:${PUERTO}`)
})
