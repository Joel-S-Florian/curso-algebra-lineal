import { useEffect, useMemo, useRef, useState } from 'react'
import { buscar, type ResultadoBusqueda } from './busqueda'
import { cargarProgreso, guardarProgreso, type Progreso } from './progreso'
import { calcularProgreso, duracionUnidad, formatearDuracion } from './progresoCalculo'
import {
  BancoFamilia,
  Doc,
  familiaPorId,
  SelectorFamilias,
  VistaDocumento,
  VistaEjercicios,
  VistaMaterial,
  VistaSolucionario,
} from './Contenido'
import { VistaProgreso } from './VistaProgreso'
import { aplicarTema, temaInicial, type Tema } from './tema'
import type { Catalogo, Leccion, Unidad, Video } from './tipos'

type Item = Video & {
  id: string
  unidad: Unidad
  datosLeccion: Leccion
  posicion: number
  total: number
}

type Ruta =
  | { tipo: 'inicio' }
  | { tipo: 'video'; id: string }
  | { tipo: 'ejercicios'; familia: string; parte: 1 | 2; ejercicio?: string }
  | { tipo: 'solucionario'; familia: string }
  | { tipo: 'material'; clave: string }
  | { tipo: 'doc'; archivo: string }
  | { tipo: 'progreso' }

const VELOCIDADES = [0.75, 1, 1.25, 1.5, 2]

const GRUPOS_BUSQUEDA: { tipo: ResultadoBusqueda['tipo']; etiqueta: string }[] = [
  { tipo: 'unidad', etiqueta: 'Unidades' },
  { tipo: 'leccion', etiqueta: 'Lecciones' },
  { tipo: 'video', etiqueta: 'Videos' },
  { tipo: 'material', etiqueta: 'Material' },
]

const ENLACES_MATERIAL: { clave: string; texto: string }[] = [
  { clave: 'formulario', texto: 'Formulario' },
  { clave: 'metodos', texto: 'Métodos' },
  { clave: 'plan', texto: 'Plan de estudio' },
  { clave: 'banco', texto: 'BANCO de ejercicios' },
  { clave: 'prueba', texto: 'Prueba final' },
  { clave: 'solucion-prueba', texto: 'Solución de la prueba' },
]

function useHash() {
  const [hash, setHash] = useState(() => location.hash || '#/')
  useEffect(() => {
    const alCambiar = () => setHash(location.hash || '#/')
    addEventListener('hashchange', alCambiar)
    return () => removeEventListener('hashchange', alCambiar)
  }, [])
  return hash
}

function analizarRuta(hash: string): Ruta {
  const [camino, consulta = ''] = hash.replace(/^#\/?/, '').split('?')
  const parametros = new URLSearchParams(consulta)
  const partes = camino.split('/').filter(Boolean)
  const resto = (inicio: number) => decodeURIComponent(partes.slice(inicio).join('/'))

  if (partes[0] === 'video' && partes[1]) return { tipo: 'video', id: resto(1) }
  if (partes[0] === 'ejercicios' && partes[1]) {
    return {
      tipo: 'ejercicios',
      familia: partes[1].toUpperCase(),
      parte: parametros.get('parte') === '2' ? 2 : 1,
      ejercicio: parametros.get('ej') || undefined,
    }
  }
  if (partes[0] === 'solucionario' && partes[1]) {
    return { tipo: 'solucionario', familia: partes[1].toUpperCase() }
  }
  if (partes[0] === 'material' && partes[1]) return { tipo: 'material', clave: partes[1] }
  if (partes[0] === 'doc' && partes[1]) return { tipo: 'doc', archivo: resto(1) }
  if (partes[0] === 'progreso') return { tipo: 'progreso' }
  return { tipo: 'inicio' }
}

export default function App() {
  const [catalogo, setCatalogo] = useState<Catalogo | null>(null)
  const [error, setError] = useState('')
  const [progreso, setProgreso] = useState<Progreso>(cargarProgreso)
  const [velocidad, setVelocidad] = useState(1)
  const [terminado, setTerminado] = useState<string | null>(null)
  const [menuAbierto, setMenuAbierto] = useState(false)
  const [unidadesAbiertas, setUnidadesAbiertas] = useState<Set<number>>(() => new Set())
  const [leccionesAbiertas, setLeccionesAbiertas] = useState<Set<string>>(() => new Set())
  const [pestana, setPestana] = useState<'video' | 'guion' | 'ejercicios' | 'soluciones'>('video')
  const [familiaElegida, setFamiliaElegida] = useState('')
  const [consulta, setConsulta] = useState('')
  const [tema, setTema] = useState<Tema>(temaInicial)
  const buscadorRef = useRef<HTMLInputElement>(null)
  const hash = useHash()
  const ruta = useMemo(() => analizarRuta(hash), [hash])

  useEffect(() => {
    guardarProgreso(progreso)
  }, [progreso])

  useEffect(() => {
    aplicarTema(tema)
  }, [tema])

  useEffect(() => {
    fetch('/catalogo.json')
      .then((respuesta) => {
        if (!respuesta.ok) throw new Error('HTTP ' + respuesta.status)
        return respuesta.json() as Promise<Catalogo>
      })
      .then(setCatalogo)
      .catch((e: Error) => setError('No se pudo cargar el catálogo: ' + e.message))
  }, [])

  useEffect(() => {
    const alPulsar = (evento: KeyboardEvent) => {
      const objetivo = evento.target as HTMLElement | null
      const escribiendo = Boolean(
        objetivo &&
          (['INPUT', 'TEXTAREA', 'SELECT'].includes(objetivo.tagName) ||
            objetivo.isContentEditable)
      )
      if (evento.key === '/' && !escribiendo) {
        evento.preventDefault()
        setMenuAbierto(true)
        buscadorRef.current?.focus()
      }
    }
    addEventListener('keydown', alPulsar)
    return () => removeEventListener('keydown', alPulsar)
  }, [])

  const resultados = useMemo(
    () => (catalogo && consulta.trim() ? buscar(catalogo, consulta) : []),
    [catalogo, consulta]
  )

  const resumenProgreso = useMemo(
    () => (catalogo ? calcularProgreso(catalogo, progreso.vistos) : null),
    [catalogo, progreso.vistos]
  )

  const items = useMemo<Item[]>(() => {
    if (!catalogo) return []
    return catalogo.unidades.flatMap((unidad) =>
      unidad.lecciones.flatMap((leccion) => {
        const total = leccion.videos.length
        return leccion.videos.map((video, i) => ({
          ...video,
          id: `${video.leccion}-${video.numero}`,
          unidad,
          datosLeccion: leccion,
          posicion: i + 1,
          total,
        }))
      })
    )
  }, [catalogo])

  const indice = ruta.tipo === 'video' ? items.findIndex((item) => item.id === ruta.id) : -1
  const actual = indice >= 0 ? items[indice] : null
  const anterior = indice > 0 ? items[indice - 1] : null
  const siguiente = indice >= 0 && indice < items.length - 1 ? items[indice + 1] : null
  const ultimoItem = items.find((item) => item.id === progreso.ultimo) ?? null

  useEffect(() => {
    if (!actual) return
    const unidad = actual.unidad.numero
    const leccion = actual.datosLeccion.id
    setUnidadesAbiertas((previas) => (previas.has(unidad) ? previas : new Set(previas).add(unidad)))
    setLeccionesAbiertas((previas) => (previas.has(leccion) ? previas : new Set(previas).add(leccion)))
    setProgreso((previo) => (previo.ultimo === actual.id ? previo : { ...previo, ultimo: actual.id }))
  }, [actual])

  useEffect(() => {
    setPestana('video')
    setFamiliaElegida(actual?.datosLeccion.ejercicios[0] ?? '')
  }, [actual?.id])

  useEffect(() => {
    if (!actual || pestana !== 'video') return
    const alPulsar = (evento: KeyboardEvent) => {
      const objetivo = evento.target as HTMLElement | null
      if (
        objetivo &&
        (['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON', 'A', 'SUMMARY'].includes(objetivo.tagName) ||
          objetivo.isContentEditable)
      ) {
        return
      }
      const video = document.querySelector('video')
      if (!video) return
      if (evento.code === 'Space' || evento.key === ' ') {
        evento.preventDefault()
        if (video.paused) void video.play()
        else video.pause()
      } else if (evento.key === 'ArrowLeft') {
        evento.preventDefault()
        video.currentTime = Math.max(0, video.currentTime - 5)
      } else if (evento.key === 'ArrowRight') {
        evento.preventDefault()
        video.currentTime = Math.min(
          Number.isFinite(video.duration) ? video.duration : Number.POSITIVE_INFINITY,
          video.currentTime + 5
        )
      } else if (evento.key.toLowerCase() === 'n' && siguiente) {
        location.hash = '/video/' + encodeURIComponent(siguiente.id)
      }
    }
    addEventListener('keydown', alPulsar)
    return () => removeEventListener('keydown', alPulsar)
  }, [actual, siguiente, pestana])

  const ir = (id: string) => {
    location.hash = '/video/' + encodeURIComponent(id)
    setMenuAbierto(false)
  }

  const alternarUnidad = (numero: number) =>
    setUnidadesAbiertas((previas) => {
      const copia = new Set(previas)
      if (copia.has(numero)) copia.delete(numero)
      else copia.add(numero)
      return copia
    })

  const alternarLeccion = (id: string) =>
    setLeccionesAbiertas((previas) => {
      const copia = new Set(previas)
      if (copia.has(id)) copia.delete(id)
      else copia.add(id)
      return copia
    })

  const guardarPosicion = (id: string, segundos: number) =>
    setProgreso((previo) => ({
      ...previo,
      posiciones: { ...previo.posiciones, [id]: segundos },
    }))

  const marcarVisto = (id: string) => {
    setTerminado(id)
    setProgreso((previo) => ({
      ...previo,
      vistos: { ...previo.vistos, [id]: true },
      posiciones: { ...previo.posiciones, [id]: 0 },
    }))
  }

  const familiasLeccion = actual?.datosLeccion.ejercicios ?? []
  const familiaSeleccionada =
    catalogo && familiaElegida ? familiaPorId(catalogo, familiaElegida) : null
  const indiceEjercicio =
    ruta.tipo === 'ejercicios' && ruta.ejercicio && catalogo
      ? catalogo.ejercicios.indice[ruta.ejercicio]
      : undefined

  return (
    <div className="aplicacion">
      <header className="barra-movil">
        <button
          className="hamburguesa"
          onClick={() => setMenuAbierto((abierto) => !abierto)}
          aria-label={menuAbierto ? 'Cerrar menú' : 'Abrir menú'}
          aria-expanded={menuAbierto}
        >
          {menuAbierto ? 'Cerrar' : 'Menú'}
        </button>
        <span className="barra-titulo">Álgebra Lineal</span>
      </header>

      <aside className={'lateral' + (menuAbierto ? ' abierta' : '')}>
        <button className="cerrar-menu" onClick={() => setMenuAbierto(false)}>
          Cerrar menú
        </button>
        <a className="marca" href="#/" onClick={() => setMenuAbierto(false)}>
          Álgebra Lineal
        </a>

        <button
          className="boton-tema"
          onClick={() => setTema((actual) => (actual === 'oscuro' ? 'claro' : 'oscuro'))}
          aria-label={tema === 'oscuro' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro'}
        >
          {tema === 'oscuro' ? 'Tema claro' : 'Tema oscuro'}
        </button>

        <div className="buscador">
          <input
            ref={buscadorRef}
            type="text"
            value={consulta}
            onChange={(evento) => setConsulta(evento.target.value)}
            onKeyDown={(evento) => {
              if (evento.key === 'Escape') {
                setConsulta('')
                buscadorRef.current?.blur()
              }
            }}
            placeholder="Buscar (tecla /)"
            aria-label="Buscar en títulos de unidades, lecciones, videos y material"
          />
        </div>

        {consulta.trim() && (
          <div className="resultados-busqueda" aria-label="Resultados de búsqueda">
            {resultados.length === 0 ? (
              <p className="nota">Sin resultados para “{consulta}”.</p>
            ) : (
              GRUPOS_BUSQUEDA.map(({ tipo, etiqueta }) => {
                const delTipo = resultados.filter((resultado) => resultado.tipo === tipo)
                if (delTipo.length === 0) return null
                return (
                  <div className="grupo-resultados" key={tipo}>
                    <p className="titulo-grupo">{etiqueta}</p>
                    {delTipo.map((resultado) => (
                      <a
                        key={resultado.tipo + resultado.id}
                        className="resultado"
                        href={resultado.destino}
                        onClick={() => {
                          setConsulta('')
                          setMenuAbierto(false)
                        }}
                      >
                        <span className="resultado-titulo">{resultado.titulo}</span>
                        <span className="resultado-detalle">{resultado.detalle}</span>
                      </a>
                    ))}
                  </div>
                )
              })
            )}
          </div>
        )}

        <nav className="navegacion">
          <a
            className={'enlace-inicio' + (ruta.tipo === 'inicio' ? ' actual' : '')}
            href="#/"
            onClick={() => setMenuAbierto(false)}
          >
            Inicio
          </a>
          <a
            className={'enlace-inicio' + (ruta.tipo === 'progreso' ? ' actual' : '')}
            href="#/progreso"
            onClick={() => setMenuAbierto(false)}
          >
            Mi progreso
          </a>

          <div className="grupo-material">
            <p className="titulo-grupo">Material</p>
            {ENLACES_MATERIAL.map((enlace) => (
              <a
                key={enlace.clave}
                className={
                  'enlace-material' +
                  (ruta.tipo === 'material' && ruta.clave === enlace.clave ? ' actual' : '')
                }
                href={'#/material/' + enlace.clave}
                onClick={() => setMenuAbierto(false)}
              >
                {enlace.texto}
              </a>
            ))}
          </div>

          {catalogo?.unidades.map((unidad) => {
            const abierta = unidadesAbiertas.has(unidad.numero)
            const unidadActual = actual?.unidad.numero === unidad.numero
            return (
              <section className="unidad" key={unidad.numero}>
                <button
                  className={'unidad-cabecera' + (unidadActual ? ' actual' : '')}
                  aria-expanded={abierta}
                  onClick={() => alternarUnidad(unidad.numero)}
                >
                  <span className="unidad-numero">Unidad {unidad.numero}</span>
                  <span className="unidad-titulo">{unidad.titulo}</span>
                  <span className="estado-grupo">{abierta ? 'Cerrar' : 'Abrir'}</span>
                </button>
                {abierta &&
                  unidad.lecciones.map((leccion) => {
                    const abiertaLeccion = leccionesAbiertas.has(leccion.id)
                    const leccionActual = actual?.datosLeccion.id === leccion.id
                    return (
                      <div className="leccion" key={leccion.id}>
                        <button
                          className={'leccion-cabecera' + (leccionActual ? ' actual' : '')}
                          aria-expanded={abiertaLeccion}
                          onClick={() => alternarLeccion(leccion.id)}
                        >
                          <span className="leccion-id">{leccion.id}</span>
                          <span className="leccion-titulo">{leccion.titulo}</span>
                          <span className="estado-grupo">{abiertaLeccion ? 'Cerrar' : 'Abrir'}</span>
                        </button>
                        {abiertaLeccion &&
                          leccion.videos.map((video, i) => {
                            const id = `${video.leccion}-${video.numero}`
                            const visto = Boolean(progreso.vistos[id])
                            return (
                              <a
                                key={id}
                                className={
                                  'video-enlace' +
                                  (visto ? ' visto' : '') +
                                  (actual?.id === id ? ' actual' : '')
                                }
                                href={'#/video/' + encodeURIComponent(id)}
                                onClick={() => setMenuAbierto(false)}
                              >
                                <span className="video-marca">{visto ? 'Visto' : i + 1}</span>
                                <span>{video.titulo}</span>
                              </a>
                            )
                          })}
                      </div>
                    )
                  })}
              </section>
            )
          })}
        </nav>
      </aside>
      {menuAbierto && <div className="fondo-menu" onClick={() => setMenuAbierto(false)} />}

      <main className="principal">
        {error && (
          <p className="error">
            {error} <a className="accion-estado" href="#/">Volver al inicio</a>
          </p>
        )}
        {!catalogo && !error && <p className="cargando">Cargando...</p>}

        {catalogo && ruta.tipo === 'video' && actual && (
          <section className="vista-video">
            <div className="pestanas" role="tablist">
              {(
                [
                  ['video', 'Video'],
                  ['guion', 'Guion y teoría'],
                  ['ejercicios', 'Ejercicios'],
                  ['soluciones', 'Soluciones'],
                ] as const
              ).map(([clave, texto]) => (
                <button
                  key={clave}
                  role="tab"
                  aria-selected={pestana === clave}
                  className={'pestana' + (pestana === clave ? ' activa' : '')}
                  onClick={() => setPestana(clave)}
                >
                  {texto}
                </button>
              ))}
            </div>

            {pestana === 'video' && (
              <div className="panel-video">
                <Reproductor
                  key={actual.id}
                  item={actual}
                  posicion={progreso.posiciones[actual.id] ?? 0}
                  velocidad={velocidad}
                  onAvance={(segundos) => guardarPosicion(actual.id, segundos)}
                  onFin={() => marcarVisto(actual.id)}
                />

                <div className="info-video">
                  <h2>{actual.titulo}</h2>
                  <p className="meta">
                    Unidad {actual.unidad.numero} · {actual.datosLeccion.id} —{' '}
                    {actual.datosLeccion.titulo} · Video {actual.posicion} de {actual.total}
                    {progreso.vistos[actual.id] ? ' · Visto' : ''}
                  </p>
                </div>

                <div className="controles">
                  <button disabled={!anterior} onClick={() => anterior && ir(anterior.id)}>
                    Anterior
                  </button>
                  <label className="velocidad">
                    Velocidad
                    <select
                      value={velocidad}
                      onChange={(e) => setVelocidad(Number(e.target.value))}
                    >
                      {VELOCIDADES.map((v) => (
                        <option key={v} value={v}>
                          {String(v).replace('.', ',')}x
                        </option>
                      ))}
                    </select>
                  </label>
                  <button
                    className="boton-principal"
                    disabled={!siguiente}
                    onClick={() => siguiente && ir(siguiente.id)}
                  >
                    Siguiente
                  </button>
                </div>

                <p className="atajos">
                  Atajos:{' '}
                  <span className="atajo">
                    <kbd>espacio</kbd> reproducir o pausar
                  </span>{' '}
                  ·{' '}
                  <span className="atajo">
                    <kbd>izquierda</kbd> <kbd>derecha</kbd> 5 segundos
                  </span>{' '}
                  ·{' '}
                  <span className="atajo">
                    <kbd>N</kbd> siguiente video
                  </span>
                </p>

                {terminado === actual.id && (
                  <div className="aviso">
                    <span>Video completado.</span>
                    {siguiente ? (
                      <button className="boton-principal" onClick={() => ir(siguiente.id)}>
                        Ir al siguiente: {siguiente.titulo}
                      </button>
                    ) : (
                      <span>Has llegado al final del curso.</span>
                    )}
                  </div>
                )}

                {familiasLeccion.length > 0 && (
                  <p className="nota">Ejercicios de esta lección: {familiasLeccion.join(', ')}</p>
                )}
              </div>
            )}

            {pestana === 'guion' && (
              <div className="panel-estudio">
                {actual.datosLeccion.guion ? (
                  <Doc ruta={actual.datosLeccion.guion} />
                ) : (
                  <p className="nota">
                    Esta lección no tiene guion escrito; su contenido está en la narración del video.{' '}
                    <a className="accion-estado" href="#/">Volver al inicio</a>
                  </p>
                )}
              </div>
            )}

            {pestana === 'ejercicios' && (
              <div className="panel-estudio">
                {familiasLeccion.length === 0 ? (
                  <p className="nota">
                    Esta lección no tiene familias de ejercicios asociadas.{' '}
                    <a className="accion-estado" href="#/">Volver al inicio</a>
                  </p>
                ) : (
                  <>
                    <SelectorFamilias
                      ids={familiasLeccion}
                      seleccionada={familiaElegida}
                      onCambiar={setFamiliaElegida}
                    />
                    {familiaSeleccionada ? (
                      <BancoFamilia familia={familiaSeleccionada} />
                    ) : (
                      <p className="error">
                        No se encontró la familia {familiaElegida}.{' '}
                        <a className="accion-estado" href="#/">Volver al inicio</a>
                      </p>
                    )}
                  </>
                )}
              </div>
            )}

            {pestana === 'soluciones' && (
              <div className="panel-estudio">
                {familiasLeccion.length === 0 ? (
                  <p className="nota">
                    Esta lección no tiene solucionario asociado.{' '}
                    <a className="accion-estado" href="#/">Volver al inicio</a>
                  </p>
                ) : (
                  <>
                    <SelectorFamilias
                      ids={familiasLeccion}
                      seleccionada={familiaElegida}
                      onCambiar={setFamiliaElegida}
                    />
                    {familiaSeleccionada && <Doc ruta={familiaSeleccionada.solucion} />}
                  </>
                )}
              </div>
            )}
          </section>
        )}

        {catalogo && ruta.tipo === 'video' && !actual && (
          <p className="error">
            No existe el video indicado en el enlace.{' '}
            <a className="accion-estado" href="#/">Volver al inicio</a>
          </p>
        )}

        {catalogo && ruta.tipo === 'ejercicios' && (
          <VistaEjercicios
            catalogo={catalogo}
            familiaId={ruta.familia}
            parteInicial={indiceEjercicio?.parte ?? ruta.parte}
            ejercicio={ruta.ejercicio}
          />
        )}

        {catalogo && ruta.tipo === 'solucionario' && (
          <VistaSolucionario catalogo={catalogo} familiaId={ruta.familia} />
        )}

        {catalogo && ruta.tipo === 'material' && (
          <VistaMaterial catalogo={catalogo} clave={ruta.clave} />
        )}

        {ruta.tipo === 'doc' && <VistaDocumento archivo={ruta.archivo} />}

        {catalogo && ruta.tipo === 'progreso' && (
          <VistaProgreso
            catalogo={catalogo}
            progreso={progreso}
            onCambiar={setProgreso}
            onIrVideo={ir}
          />
        )}

        {catalogo && ruta.tipo === 'inicio' && (
          <section className="inicio">
            <h2>Curso de Álgebra Lineal</h2>
            <p className="resumen">
              {catalogo.totales.unidades} unidades · {catalogo.totales.lecciones} lecciones ·{' '}
              {catalogo.totales.videos} videos con subtítulos
            </p>
            {ultimoItem && (
              <button className="boton-continuar" onClick={() => ir(ultimoItem.id)}>
                <span className="continuar-etiqueta">Continuar donde lo dejé</span>
                <span className="continuar-titulo">{ultimoItem.titulo}</span>
              </button>
            )}
            <div className="lista-unidades">
              {catalogo.unidades.map((unidad) => {
                const videos = unidad.lecciones.flatMap((leccion) => leccion.videos)
                const primero = videos[0]
                const progresoUnidad = resumenProgreso?.unidades.find(
                  (resumen) => resumen.numero === unidad.numero
                )
                const clave = unidad.numero === 8 || unidad.numero === 9
                return (
                  <article
                    className={'tarjeta-unidad' + (clave ? ' clave' : '')}
                    key={unidad.numero}
                  >
                    {clave && <span className="etiqueta-clave">Unidad clave</span>}
                    <h3>
                      Unidad {unidad.numero} — {unidad.titulo}
                    </h3>
                    <p className="unidad-meta">
                      {unidad.lecciones.length} lecciones · {videos.length} videos ·{' '}
                      {formatearDuracion(duracionUnidad(unidad))}
                    </p>
                    {progresoUnidad && (
                      <div className="progreso-tarjeta">
                        <div
                          className="barra"
                          role="progressbar"
                          aria-label={`Progreso de la unidad ${unidad.numero}`}
                          aria-valuenow={progresoUnidad.porcentaje}
                          aria-valuemin={0}
                          aria-valuemax={100}
                        >
                          <div
                            className="barra-relleno"
                            style={{ width: `${progresoUnidad.porcentaje}%` }}
                          />
                        </div>
                        <span>
                          {progresoUnidad.porcentaje}% visto ({progresoUnidad.vistos}/
                          {progresoUnidad.total})
                        </span>
                      </div>
                    )}
                    {primero && (
                      <button onClick={() => ir(`${primero.leccion}-${primero.numero}`)}>
                        Empezar la unidad
                      </button>
                    )}
                  </article>
                )
              })}
            </div>
          </section>
        )}
      </main>
    </div>
  )
}

function Reproductor({
  item,
  posicion,
  velocidad,
  onAvance,
  onFin,
}: {
  item: Item
  posicion: number
  velocidad: number
  onAvance: (segundos: number) => void
  onFin: () => void
}) {
  const referencia = useRef<HTMLVideoElement>(null)
  const ultimoGuardado = useRef(0)

  useEffect(() => {
    if (referencia.current) referencia.current.playbackRate = velocidad
  }, [velocidad])

  return (
    <div className="reproductor">
      <video
        ref={referencia}
        controls
        preload="metadata"
        playsInline
        onLoadedMetadata={() => {
          const video = referencia.current
          if (!video) return
          video.playbackRate = velocidad
          if (posicion > 3 && Number.isFinite(video.duration) && posicion < video.duration - 3) {
            video.currentTime = posicion
          }
        }}
        onTimeUpdate={() => {
          const video = referencia.current
          if (!video) return
          if (video.currentTime - ultimoGuardado.current >= 5) {
            ultimoGuardado.current = video.currentTime
            onAvance(video.currentTime)
          }
        }}
        onPause={() => {
          const video = referencia.current
          if (video && video.currentTime > 0) onAvance(video.currentTime)
        }}
        onEnded={() => {
          onAvance(0)
          onFin()
        }}
      >
        <source src={'/raw/' + item.ruta} type="video/mp4" />
        {item.vtt && (
          <track kind="subtitles" src={'/' + item.vtt} srcLang="es" label="Español" default />
        )}
        Tu navegador no admite la reproducción de video HTML5.
      </video>
    </div>
  )
}
