import { useState } from 'react'
import { progresoInicial, type Progreso } from './progreso'
import { calcularProgreso, leccionesPendientes } from './progresoCalculo'
import type { Catalogo } from './tipos'

export function VistaProgreso({
  catalogo,
  progreso,
  onCambiar,
  onIrVideo,
}: {
  catalogo: Catalogo
  progreso: Progreso
  onCambiar: (progreso: Progreso) => void
  onIrVideo: (id: string) => void
}) {
  const [mensaje, setMensaje] = useState('')
  const resumen = calcularProgreso(catalogo, progreso.vistos)
  const pendientes = leccionesPendientes(catalogo, progreso.vistos)

  const exportar = () => {
    const datos = JSON.stringify(progreso, null, 2)
    const url = URL.createObjectURL(new Blob([datos], { type: 'application/json' }))
    const enlace = document.createElement('a')
    enlace.href = url
    enlace.download = 'progreso-algebra-lineal.json'
    enlace.click()
    URL.revokeObjectURL(url)
    setMensaje('Progreso exportado.')
  }

  const importar = async (archivo: File | undefined) => {
    if (!archivo) return
    try {
      const datos = JSON.parse(await archivo.text())
      if (
        !datos ||
        typeof datos !== 'object' ||
        typeof datos.vistos !== 'object' ||
        typeof datos.posiciones !== 'object' ||
        Array.isArray(datos.vistos) ||
        Array.isArray(datos.posiciones)
      ) {
        throw new Error('formato')
      }
      onCambiar({
        vistos: datos.vistos,
        posiciones: datos.posiciones,
        ultimo: typeof datos.ultimo === 'string' ? datos.ultimo : null,
      })
      setMensaje('Progreso importado.')
    } catch {
      setMensaje('El archivo no tiene un progreso válido.')
    }
  }

  const reiniciar = () => {
    if (confirm('¿Seguro que quieres borrar todo tu progreso? No se puede deshacer.')) {
      onCambiar(progresoInicial())
      setMensaje('Progreso reiniciado.')
    }
  }

  return (
    <section className="vista-doc vista-progreso">
      <h2>Mi progreso</h2>

      <div className="resumen-progreso">
        <span className="porcentaje-grande">{resumen.porcentaje}%</span>
        <span>
          {resumen.vistos} de {resumen.total} videos vistos
        </span>
      </div>

      <div className="barras-progreso">
        {resumen.unidades.map((unidad) => (
          <div className="barra-unidad" key={unidad.numero}>
            <div className="barra-cabecera">
              <span>
                Unidad {unidad.numero} — {unidad.titulo}
              </span>
              <span>
                {unidad.vistos}/{unidad.total} · {unidad.porcentaje}%
              </span>
            </div>
            <div
              className="barra"
              role="progressbar"
              aria-label={`Progreso de la unidad ${unidad.numero}: ${unidad.titulo}`}
              aria-valuenow={unidad.porcentaje}
              aria-valuemin={0}
              aria-valuemax={100}
            >
              <div className="barra-relleno" style={{ width: `${unidad.porcentaje}%` }} />
            </div>
          </div>
        ))}
      </div>

      <h3>Lecciones pendientes ({pendientes.length})</h3>
      {pendientes.length === 0 ? (
        <p className="nota">
          No queda ninguna lección pendiente. ¡Curso terminado!{' '}
          <a className="accion-estado" href="#/">Volver al inicio</a>
        </p>
      ) : (
        <ul className="lista-pendientes">
          {pendientes.map((pendiente) => (
            <li key={pendiente.leccionId}>
              <span>
                <strong>{pendiente.leccionId}</strong> — {pendiente.leccionTitulo}
                <span className="tenue">
                  {' '}
                  · Unidad {pendiente.unidad} · {pendiente.vistos}/{pendiente.total}
                </span>
              </span>
              <button onClick={() => onIrVideo(pendiente.primerPendiente)}>Ver</button>
            </li>
          ))}
        </ul>
      )}

      <div className="acciones-progreso">
        <button onClick={exportar}>Exportar progreso</button>
        <label className="boton-archivo">
          Importar progreso
          <input
            type="file"
            accept="application/json,.json"
            onChange={(evento) => {
              void importar(evento.target.files?.[0])
              evento.target.value = ''
            }}
          />
        </label>
        <button className="peligro" onClick={reiniciar}>
          Reiniciar progreso
        </button>
      </div>
      {mensaje && <p className="nota">{mensaje}</p>}
    </section>
  )
}
