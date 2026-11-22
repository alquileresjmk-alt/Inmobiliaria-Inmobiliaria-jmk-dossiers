# Magazine Clasificados de Inmobiliaria JMK

Sitio estático listo para GitHub Pages, sin instalación ni compilación.

Esta entrega contiene 360 flyers post y una portada de revista. Incluye variantes de diseño de un mismo inmueble, conservadas como publicaciones individuales.

## Archivos principales

- `index.html`: landing page y colección con búsqueda y categorías.
- `revista.html`: revista con páginas de papel, navegación táctil, teclado, selector de página, índice, ampliación y descarga de flyers.
- `catalogo.js`: catálogo usado por el sitio. Funciona incluso abriendo los archivos localmente.
- `catalogo.json`: versión legible del catálogo para mantenimiento.
- `assets/flyers/`: flyers post optimizados y miniaturas. Se mantienen los diseños originales; no se incluyen versiones de historias.
- `vendor/`: motor de páginas incluido localmente, con licencia MIT.
- `TEXTO-REDES.md`: texto para anunciar el magazine.

## Publicar en GitHub Pages

1. Descomprimí este paquete.
2. Creá un repositorio en tu cuenta de GitHub, por ejemplo `magazine-clasificados-jmk`.
3. Subí todos los archivos y carpetas del paquete a la raíz del repositorio. `index.html` debe quedar en la raíz, no dentro de otra carpeta.
4. En **Settings → Pages**, elegí **Deploy from a branch**, rama **main**, carpeta **/(root)**, y guardá.
5. GitHub mostrará la dirección pública cuando termine la publicación. Para el nombre de repositorio del ejemplo será `https://alquileresjmk-alt.github.io/magazine-clasificados-jmk/`.
6. Abrí la dirección, comprobá la revista y usá esa dirección en el texto de redes. El paquete no publica ni modifica tu sitio principal automáticamente.

Alternativa con Git: `git init`, `git add .`, `git commit`, agregar el remoto de tu nuevo repositorio y hacer push a `main`. No se requieren claves dentro de estos archivos.

## Actualizar los flyers

1. Agregá el nuevo flyer post y su miniatura a `assets/flyers/`. Preferí WebP. Evitá imágenes mayores de 25 MB, que GitHub no admite en la carga web.
2. Copiá una entrada del catálogo en `catalogo.json`, cambiá los datos y usá una `key` única. Categorías: Alquiler, Venta, Comercial, Proyectos u Otros.
3. Conservá el número real de propiedad o usá `null` cuando no exista. No inventés números: sin ID, la consulta va al catálogo general y a WhatsApp.
4. Indicá `archive: true` cuando corresponda a una publicación anterior o retirada. Los flyers conservan el contenido original; siempre hay una aclaración de vigencia.
5. Ejecutá `python3 scripts/actualizar-catalogo.py` para regenerar `catalogo.js` desde `catalogo.json`.
6. Subí los archivos actualizados al repositorio.

Las fechas de publicación vacías corresponden a diseños recuperados de paquetes cuyo archivo original no incluía una fecha individual verificable.

## Accesibilidad y rendimiento

- Controles por teclado, foco visible, texto alternativo e interfaz adaptable.
- La preferencia de movimiento reducido cambia la navegación a saltos sin animación.
- El lector carga las imágenes cercanas a la página abierta; la colección usa miniaturas y carga por grupos.
- No usa fuentes externas, rastreadores, servicios de analítica ni una base de datos.
- Los números de teléfono y las fichas se generan desde datos estructurados, no desde enlaces incrustados en las imágenes.

## Información editorial

Esta colección reúne los flyers post recuperables de los archivos y paquetes disponibles. Pueden existir varios diseños del mismo inmueble. Los anuncios históricos permanecen identificados como archivo cuando no se pudo verificar una ficha o se conocía su retiro. Un enlace de ficha verificable no garantiza que el inmueble siga disponible: confirmar siempre con JMK.

Contacto: +506 6019-0789 · info@realestatejmk.com · https://realestatejmk.com
