import { useEffect, useState } from 'react'
import { Markdown } from './Markdown'
import { useDocumento } from './useDocumento'
import type { Catalogo, FamiliaEjercicios } from './tipos'

export function Doc({
  ruta,
  banco = false,
  ejercicio,
  sinEtiquetaParte2 = false,
}: {
  ruta: string | null
  banco?: boolean
  ejercicio?: string
  sinEtiquetaParte2?: boolean
}) {
  const { texto, error } = useDocumento(ruta)
  if (!ruta)
    return (
      <p className="nota">
        Esta sección no tiene un documento asociado.{' '}
        <a className="accion-estado" href="#/">Volver al inicio</a>
      </p>
    )
  if (error)
    return (
      <p className="error">
        {error} <a className="accion-estado" href="#/">Volver al inicio</a>
      </p>
    )
  if (texto === null) return <p className="cargando">Cargando...</p>
  return (
    <div className="markdown">
      <Markdown
        texto={texto}
        ruta={ruta}
        banco={banco}
        ejercicio={ejercicio}
        sinEtiquetaParte2={sinEtiquetaParte2}
      />
    </div>
  )
}

export function familiaPorId(catalogo: Catalogo, id: string): FamiliaEjercicios | null {
  return catalogo.ejercicios.familias.find((familia) => familia.id === id) ?? null
}

export function SelectorFamilias({
  ids,
  seleccionada,
  onCambiar,
}: {
  ids: string[]
  seleccionada: string
  onCambiar: (id: string) => void
}) {
  if (ids.length <= 1) return null
  return (
    <div className="chips">
      {ids.map((id) => (
        <button
          key={id}
          className={'chip' + (id === seleccionada ? ' activo' : '')}
          onClick={() => onCambiar(id)}
        >
          {id}
        </button>
      ))}
    </div>
  )
}

export function BancoFamilia({
  familia,
  parteInicial,
  ejercicio,
}: {
  familia: FamiliaEjercicios
  parteInicial?: 1 | 2
  ejercicio?: string
}) {
  const partePorDefecto = familia.parte1 ? 1 : 2
  const [parte, setParte] = useState<1 | 2>(partePorDefecto)

  useEffect(() => {
    const pedida = parteInicial ?? partePorDefecto
    if (pedida === 2 && !familia.parte2) setParte(partePorDefecto)
    else if (pedida === 1 && !familia.parte1) setParte(partePorDefecto)
    else setParte(pedida)
  }, [familia.id, parteInicial, partePorDefecto, familia.parte1, familia.parte2])

  const ruta = parte === 2 ? familia.parte2 : familia.parte1
  const dosPartes = Boolean(familia.parte1 && familia.parte2)

  return (
    <>
      {dosPartes && (
        <div className="subpestanas">
          <button
            className={parte === 1 ? 'activa' : ''}
            onClick={() => setParte(1)}
          >
            Parte 1
          </button>
          <button
            className={parte === 2 ? 'activa' : ''}
            onClick={() => setParte(2)}
          >
            Parte 2
          </button>
        </div>
      )}
      <Doc ruta={ruta} ejercicio={ejercicio} sinEtiquetaParte2={!familia.parte1} />
    </>
  )
}

export function VistaEjercicios({
  catalogo,
  familiaId,
  parteInicial,
  ejercicio,
}: {
  catalogo: Catalogo
  familiaId: string
  parteInicial?: 1 | 2
  ejercicio?: string
}) {
  const familia = familiaPorId(catalogo, familiaId)
  if (!familia)
    return (
      <p className="error">
        No existe la familia de ejercicios {familiaId}.{' '}
        <a className="accion-estado" href="#/">Volver al inicio</a>
      </p>
    )
  return (
    <section className="vista-doc">
      <h2>
        Ejercicios {familia.id} — {familia.titulo}
      </h2>
      <BancoFamilia familia={familia} parteInicial={parteInicial} ejercicio={ejercicio} />
    </section>
  )
}

export function VistaSolucionario({
  catalogo,
  familiaId,
}: {
  catalogo: Catalogo
  familiaId: string
}) {
  const familia = familiaPorId(catalogo, familiaId)
  if (!familia)
    return (
      <p className="error">
        No existe la familia de ejercicios {familiaId}.{' '}
        <a className="accion-estado" href="#/">Volver al inicio</a>
      </p>
    )
  return (
    <section className="vista-doc">
      <Doc ruta={familia.solucion} />
    </section>
  )
}

const CLAVES_MATERIAL = {
  formulario: { clave: 'formulario', banco: false, aviso: '' },
  metodos: { clave: 'metodos', banco: false, aviso: '' },
  plan: { clave: 'plan', banco: false, aviso: '' },
  banco: { clave: 'banco', banco: true, aviso: '' },
  prueba: { clave: 'pruebaFinal', banco: false, aviso: '' },
  'solucion-prueba': {
    clave: 'solucionPruebaFinal',
    banco: false,
    aviso: 'Intenta primero la prueba: leer la solución antes no te enseñará a resolverla.',
  },
} as const

export function VistaMaterial({ catalogo, clave }: { catalogo: Catalogo; clave: string }) {
  const entrada = CLAVES_MATERIAL[clave as keyof typeof CLAVES_MATERIAL]
  if (!entrada)
    return (
      <p className="error">
        No existe la sección de material “{clave}”.{' '}
        <a className="accion-estado" href="#/">Volver al inicio</a>
      </p>
    )
  const material = catalogo.material[entrada.clave]
  return (
    <section className="vista-doc">
      {entrada.aviso && <p className="aviso-prueba">{entrada.aviso}</p>}
      <Doc ruta={material.ruta} banco={entrada.banco} />
    </section>
  )
}

export function VistaDocumento({ archivo }: { archivo: string }) {
  return (
    <section className="vista-doc">
      <p className="ruta-documento">Documento: {archivo}</p>
      <Doc ruta={archivo} />
    </section>
  )
}
