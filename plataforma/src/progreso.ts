const CLAVE = 'algebra-lineal:progreso'

export type Progreso = {
  vistos: Record<string, boolean>
  ultimo: string | null
  posiciones: Record<string, number>
}

export const progresoInicial = (): Progreso => ({ vistos: {}, ultimo: null, posiciones: {} })

export function cargarProgreso(): Progreso {
  try {
    const guardado = JSON.parse(localStorage.getItem(CLAVE) || 'null')
    if (guardado && typeof guardado === 'object') {
      return { ...progresoInicial(), ...guardado }
    }
  } catch {
    // Datos corruptos: se empieza de cero.
  }
  return progresoInicial()
}

export function guardarProgreso(progreso: Progreso) {
  try {
    localStorage.setItem(CLAVE, JSON.stringify(progreso))
  } catch {
    // Sin espacio o sin permiso: la sesión sigue funcionando sin persistir.
  }
}
