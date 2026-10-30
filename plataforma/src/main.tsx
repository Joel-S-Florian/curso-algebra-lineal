import { createRoot } from 'react-dom/client'
import App from './App'
import { aplicarTema, temaInicial } from './tema'
import './estilos.css'

aplicarTema(temaInicial())
createRoot(document.getElementById('root')!).render(<App />)
