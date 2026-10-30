import { useEffect, useState } from 'react'

const cache = new Map<string, string>()

export function useDocumento(ruta: string | null) {
  const [texto, setTexto] = useState<string | null>(() => (ruta ? cache.get(ruta) ?? null : null))
  const [error, setError] = useState('')

  useEffect(() => {
    if (!ruta) {
      setTexto(null)
      setError('')
      return
    }
    const guardado = cache.get(ruta)
    if (guardado !== undefined) {
      setTexto(guardado)
      setError('')
      return
    }

    let vigente = true
    setTexto(null)
    setError('')
    fetch('/raw/' + ruta)
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error('HTTP ' + respuesta.status)
        return respuesta.text()
      })
      .then((contenido) => {
        cache.set(ruta, contenido)
        if (vigente) setTexto(contenido)
      })
      .catch((e: Error) => {
        if (vigente) setError('No se pudo cargar ' + ruta + ' (' + e.message + ').')
      })

    return () => {
      vigente = false
    }
  }, [ruta])

  return { texto, error }
}
