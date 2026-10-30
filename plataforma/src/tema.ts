export type Tema = 'claro' | 'oscuro'

const CLAVE = 'algebra-lineal:tema'

export function temaInicial(): Tema {
  try {
    return localStorage.getItem(CLAVE) === 'claro' ? 'claro' : 'oscuro'
  } catch {
    return 'oscuro'
  }
}

function actualizarFavicon(tema: Tema) {
  const lienzo = document.createElement('canvas')
  lienzo.width = 64
  lienzo.height = 64
  const contexto = lienzo.getContext('2d')
  if (!contexto) return
  contexto.fillStyle = tema === 'claro' ? '#2f52c8' : '#93a9ff'
  contexto.fillRect(0, 0, 64, 64)
  contexto.fillStyle = tema === 'claro' ? '#ffffff' : '#10141d'
  contexto.font = 'bold 42px system-ui, sans-serif'
  contexto.textAlign = 'center'
  contexto.textBaseline = 'middle'
  contexto.fillText('Á', 32, 35)
  let enlace = document.querySelector<HTMLLinkElement>('link[rel="icon"]')
  if (!enlace) {
    enlace = document.createElement('link')
    enlace.rel = 'icon'
    document.head.appendChild(enlace)
  }
  enlace.href = lienzo.toDataURL('image/png')
}

export function aplicarTema(tema: Tema) {
  document.documentElement.dataset.tema = tema
  try {
    localStorage.setItem(CLAVE, tema)
  } catch {
    // Sin almacenamiento: el tema sigue funcionando en esta sesión.
  }
  actualizarFavicon(tema)
}
