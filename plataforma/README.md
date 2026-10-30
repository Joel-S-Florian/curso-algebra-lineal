# Plataforma de Álgebra Lineal

Visor local del curso: videos con subtítulos, guiones, ejercicios, solucionario, material de estudio, búsqueda y progreso. No modifica los archivos originales del curso.

## Arrancar

Requiere Node.js y npm.

```bash
cd plataforma
npm install
npm start
```

Abre http://127.0.0.1:5173.

- `npm run dev`: modo desarrollo con recarga.
- `npm test`: pruebas de búsqueda y cálculo de progreso.
- `npm run build`: genera `dist/` (es lo que sirve `npm start`).

## Regenerar el catálogo

Si añades o cambias videos, guiones, ejercicios o material en el curso:

```bash
npm run catalogo
npm run verificar
npm run build
```

`npm run catalogo` lee la carpeta del curso, convierte los `.srt` a `.vtt` y escribe `public/catalogo.json`; `npm run verificar` comprueba que todas las rutas existan. `npm start` sirve `dist/`, así que hay que reconstruir después de regenerar.

## Límites conocidos

- Un solo usuario local; el progreso vive en el `localStorage` del navegador. Exportar/importar JSON lo respalda, pero importar reemplaza el progreso actual.
- F15 y F16 solo tienen archivo de parte 2; L51–L55 no tienen guion escrito (el contenido está en el video).
- La búsqueda cubre títulos de unidades, lecciones, videos y material, no el texto completo de los documentos.
- Mermaid se carga solo al abrir Métodos y genera un paquete grande; el primer render puede tardar.
- El servidor escucha solo en `127.0.0.1`, sin autenticación: no está pensado para exponerse en red.
- La reproducción depende de los códecs del navegador; los subtítulos se sirven como VTT.
