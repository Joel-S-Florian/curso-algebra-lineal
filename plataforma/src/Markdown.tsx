import { useEffect, useRef, useState } from 'react'
import ReactMarkdown, { type Components } from 'react-markdown'
import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'
import rehypeRaw from 'rehype-raw'
import rehypeKatex from 'rehype-katex'
import * as katex from 'katex'
import 'katex/dist/katex.min.css'

const OPCIONES_KATEX = { output: 'html' as const, throwOnError: false, strict: false }

const RUTAS_CONOCIDAS = [
  'ejercicios/',
  'solucionario/',
  'material/',
  'prueba_final/',
  'guiones/',
  'docs/',
]

function unirRutas(documento: string, relativa: string) {
  const base = documento.split('/').slice(0, -1)
  const partes = relativa.split('/')
  const pila: string[] = []
  for (const parte of [...base, ...partes]) {
    if (!parte || parte === '.') continue
    if (parte === '..') pila.pop()
    else pila.push(parte)
  }
  return pila.join('/')
}

function rutaAppParaArchivo(archivo: string): string {
  if (archivo === 'ejercicios/BANCO.md') return '#/material/banco'
  if (archivo === 'material/formulario.md') return '#/material/formulario'
  if (archivo === 'material/metodos.md') return '#/material/metodos'
  if (archivo === 'material/plan_de_estudio.md') return '#/material/plan'
  if (archivo === 'prueba_final/PRUEBA_FINAL.md') return '#/material/prueba'
  if (archivo === 'prueba_final/SOLUCION_PRUEBA_FINAL.md') return '#/material/solucion-prueba'

  const ejercicio = archivo.match(/^ejercicios\/(F\d{2})_(.+)\.md$/)
  if (ejercicio) {
    const parte = ejercicio[2].endsWith('_parte2') ? '?parte=2' : ''
    return `#/ejercicios/${ejercicio[1]}${parte}`
  }

  const solucion = archivo.match(/^solucionario\/(F\d{2})\.md$/)
  if (solucion) return `#/solucionario/${solucion[1]}`

  return '#/doc/' + encodeURIComponent(archivo)
}

function destinoDeEnlace(href: string, documento: string): string | null {
  const [ruta, ancla] = href.split('#')
  if (!ruta || !/\.md$/i.test(ruta)) return null
  let archivo: string
  if (ruta.startsWith('/')) archivo = ruta.slice(1)
  else if (RUTAS_CONOCIDAS.some((prefijo) => ruta.startsWith(prefijo))) archivo = ruta
  else archivo = unirRutas(documento, ruta)
  const destino = rutaAppParaArchivo(archivo)
  return ancla ? destino + (destino.includes('?') ? '&' : '?') + 'ej=' + encodeURIComponent(ancla) : destino
}

function recursoDeImagen(src: string, documento: string) {
  if (/^(https?:|data:)/i.test(src)) return src
  if (src.startsWith('/')) return '/raw' + src
  return '/raw/' + unirRutas(documento, src)
}

function textoDeHast(nodo: any): string {
  if (!nodo) return ''
  if (typeof nodo === 'string') return nodo
  if (Array.isArray(nodo)) return nodo.map(textoDeHast).join('')
  if (nodo.value) return String(nodo.value)
  return textoDeHast(nodo.children)
}

function textoDeHijos(hijos: any): string {
  if (typeof hijos === 'string' || typeof hijos === 'number') return String(hijos)
  if (Array.isArray(hijos)) return hijos.map(textoDeHijos).join('')
  if (hijos && typeof hijos === 'object' && 'props' in hijos) return textoDeHijos(hijos.props?.children)
  return ''
}

// Convierte $...$ y $$...$$ que quedaron dentro de HTML crudo (<details>, <summary>).
function rehypeMatematicaEnTextoCrudo() {
  const partirTexto = (texto: string) => {
    const partes = texto.split(/(\$\$[\s\S]+?\$\$|\$[^$\n]+?\$)/g)
    if (partes.length === 1) return [{ type: 'text', value: texto }]
    return partes
      .filter((parte: string) => parte)
      .map((parte: string) => {
        const bloque = parte.startsWith('$$') && parte.endsWith('$$')
        const inline = !bloque && parte.startsWith('$') && parte.endsWith('$')
        if (!bloque && !inline) return { type: 'text', value: parte }
        const tex = parte.slice(bloque ? 2 : 1, bloque ? -2 : -1)
        if (!tex.trim()) return { type: 'text', value: parte }
        return {
          type: 'element',
          tagName: 'span',
          properties: {
            className: bloque
              ? ['matematica-manual', 'matematica-bloque']
              : ['matematica-manual'],
          },
          children: [{ type: 'text', value: tex }],
        }
      })
  }

  return (arbol: any) => {
    const visitar = (nodo: any) => {
      if (!nodo || typeof nodo !== 'object') return
      if (nodo.type === 'element') {
        const clases: string[] = nodo.properties?.className || []
        if (['code', 'pre', 'script', 'style'].includes(nodo.tagName) || clases.includes('math')) return
      }
      if (nodo.children) {
        const nuevos: any[] = []
        for (const hijo of nodo.children) {
          if (hijo.type === 'text' && hijo.value.includes('$')) {
            nuevos.push(...partirTexto(hijo.value))
          } else {
            nuevos.push(hijo)
            visitar(hijo)
          }
        }
        nodo.children = nuevos
      }
    }
    visitar(arbol)
  }
}

// Da id a los encabezados de ejercicios para que el BANCO pueda enlazarlos.
function rehypeIdsEjercicios() {
  return (arbol: any) => {
    const visitar = (nodo: any) => {
      if (nodo.type === 'element' && /^h[1-6]$/.test(nodo.tagName)) {
        const codigo = textoDeHast(nodo).match(/F\d{2}-[A-Z]\d-\d{2}/)
        if (codigo) nodo.properties = { ...(nodo.properties || {}), id: codigo[0] }
      }
      if (nodo.children) nodo.children.forEach(visitar)
    }
    visitar(arbol)
  }
}

function DiagramaMermaid({ codigo }: { codigo: string }) {
  const contenedor = useRef<HTMLDivElement>(null)
  const [error, setError] = useState('')

  useEffect(() => {
    let vigente = true
    import('mermaid')
      .then(async ({ default: mermaid }) => {
        mermaid.initialize({ startOnLoad: false, theme: 'dark', securityLevel: 'strict' })
        try {
          const id = 'mermaid-' + Math.random().toString(36).slice(2)
          const { svg } = await mermaid.render(id, codigo)
          if (vigente && contenedor.current) contenedor.current.innerHTML = svg
        } catch {
          if (vigente) setError('No se pudo dibujar el diagrama.')
        }
      })
      .catch(() => {
        if (vigente) setError('No se pudo cargar el dibujante de diagramas.')
      })
    return () => {
      vigente = false
    }
  }, [codigo])

  return (
    <div className="diagrama-mermaid" ref={contenedor}>
      {error || 'Cargando diagrama…'}
    </div>
  )
}

const componentes = {
  table: ({ children }: any) => (
    <div className="tabla-desplazable">
      <table>{children}</table>
    </div>
  ),
  pre: ({ children, node }: any) => {
    const codigo = node?.children?.[0]
    const clases: string[] = codigo?.properties?.className || []
    if (clases.includes('language-mermaid')) {
      return <DiagramaMermaid codigo={textoDeHast(codigo)} />
    }
    return <pre>{children}</pre>
  },
} as Components

export function Markdown({
  texto,
  ruta,
  banco = false,
  ejercicio,
  sinEtiquetaParte2 = false,
}: {
  texto: string
  ruta: string
  banco?: boolean
  ejercicio?: string
  sinEtiquetaParte2?: boolean
}) {
  useEffect(() => {
    if (!ejercicio) return
    const objetivo = document.getElementById(ejercicio)
    if (!objetivo) return
    objetivo.scrollIntoView({ block: 'start' })
    objetivo.classList.add('destacado')
    const temporizador = setTimeout(() => objetivo.classList.remove('destacado'), 3000)
    return () => clearTimeout(temporizador)
  }, [ejercicio, texto])

  const enlaces: Components = {
    a: ({ href, children }: any) => {
      if (!href) return <a>{children}</a>
      if (href.startsWith('#')) {
        return (
          <a
            href={href}
            onClick={(evento) => {
              evento.preventDefault()
              document.getElementById(decodeURIComponent(href.slice(1)))?.scrollIntoView({ block: 'start' })
            }}
          >
            {children}
          </a>
        )
      }
      const destino = destinoDeEnlace(href, ruta)
      if (destino) return <a href={destino}>{children}</a>
      return (
        <a href={href} target="_blank" rel="noreferrer">
          {children}
        </a>
      )
    },
    img: ({ src, alt }: any) =>
      src ? <img src={recursoDeImagen(src, ruta)} alt={alt || ''} loading="lazy" /> : null,
    table: componentes.table,
    pre: componentes.pre,
    span: ({ node, children, ...props }: any) => {
      const clases: string[] = node?.properties?.className || []
      if (clases.includes('matematica-manual')) {
        const bloque = clases.includes('matematica-bloque')
        const tex = textoDeHast(node)
        return (
          <span
            className={bloque ? 'matematica-bloque' : undefined}
            dangerouslySetInnerHTML={{
              __html: katex.renderToString(tex, { ...OPCIONES_KATEX, displayMode: bloque }),
            }}
          />
        )
      }
      return <span {...props}>{children}</span>
    },
    td: ({ children }: any) => {
      if (banco) {
        const contenido = textoDeHijos(children).trim()
        const codigo = contenido.match(/^F\d{2}-[A-Z]\d-\d{2}$/)
        if (codigo) {
          return (
            <td>
              <a href={`#/ejercicios/${codigo[0].slice(0, 3)}?ej=${codigo[0]}`}>{children}</a>
            </td>
          )
        }
        const archivo = contenido.match(/^(F\d{2})_.*\.md$/)
        if (archivo) {
          return (
            <td>
              <a href={`#/ejercicios/${archivo[1]}${contenido.includes('_parte2') ? '?parte=2' : ''}`}>
                {children}
              </a>
            </td>
          )
        }
      }
      return <td>{children}</td>
    },
  }

  const contenido = sinEtiquetaParte2
    ? texto.replace(/^(#\s+.+?)\s*\(parte 2\)\s*$/im, '$1')
    : texto

  return (
    <ReactMarkdown
      remarkPlugins={[remarkGfm, remarkMath]}
      rehypePlugins={[
        rehypeRaw,
        rehypeMatematicaEnTextoCrudo,
        [rehypeKatex, OPCIONES_KATEX],
        rehypeIdsEjercicios,
      ] as any}
      components={{ ...componentes, ...enlaces }}
    >
      {contenido}
    </ReactMarkdown>
  )
}
