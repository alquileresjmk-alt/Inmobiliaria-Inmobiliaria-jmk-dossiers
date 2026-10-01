# Landing page: Terreno de 4 hectáreas en San Mateo de Alajuela

Referencia JMK-SANMATEO-001. Sitio estático (HTML, CSS y un JS pequeño), sin dependencias ni compilación.

## Contenido

```
index.html            Español (página principal)
en/index.html         English
fr/index.html         Français
assets/style.css      Estilos
assets/main.js        Visor de imágenes
assets/img/           Fotos, logo, banderas
assets/docs/          Dossier en PDF (es, en, fr)
.nojekyll             Indica a GitHub Pages que publique los archivos tal cual
```

## Publicar en GitHub Pages

Opción A, repositorio propio:

1. Crear un repositorio nuevo, por ejemplo `hacienda-la-maravilla`.
2. Subir el contenido de esta carpeta a la raíz del repositorio (que `index.html` quede en la raíz).
3. En Settings > Pages, elegir "Deploy from a branch", rama `main`, carpeta `/ (root)`.
4. La página queda en `https://<usuario>.github.io/hacienda-la-maravilla/`.

Opción B, dentro de `jmk-dossiers`:

1. Copiar esta carpeta completa al repositorio `jmk-dossiers`.
2. La página queda en `https://<usuario>.github.io/jmk-dossiers/landing-hacienda-la-maravilla/`.

Todas las rutas son relativas, así que funciona en cualquiera de las dos opciones sin cambios.

## Para editar

- Textos: directamente en los tres `index.html`.
- Precio o datos: buscar `4,480,000` (es, en) y `4 480 000` (fr).
- WhatsApp: los enlaces `wa.me/50660190789` llevan un mensaje predefinido por idioma.
- Vista previa al compartir (og:image): al tener la URL definitiva, conviene cambiar
  `assets/img/og.jpg` por la URL completa en la etiqueta `og:image` de cada página.
