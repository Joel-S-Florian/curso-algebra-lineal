import { existsSync } from 'node:fs'
import { spawnSync } from 'node:child_process'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const aqui = dirname(fileURLToPath(import.meta.url))
const plataforma = join(aqui, '..')

if (!existsSync(join(plataforma, 'dist', 'index.html'))) {
  console.log('Falta dist/: compilando la app…')
  const comando = process.platform === 'win32' ? 'npm.cmd run build' : 'npm run build'
  const resultado = spawnSync(comando, {
    cwd: plataforma,
    stdio: 'inherit',
    shell: true,
  })
  if (resultado.status !== 0) process.exit(resultado.status || 1)
}

await import('../servidor.mjs')
