# Dossiers Inmobiliaria JMK

Repositorio de dossiers HTML de propiedades, listos para hostear con GitHub Pages e incrustar en Wix vía iframe.

## Estructura

```
/babylon/index.html
/condado-del-valle/index.html
/plaza-cristal-barrio-dent/index.html
/apartamento-moravia/index.html
```

Cada carpeta es una propiedad independiente. GitHub Pages sirve cada `index.html` en su propia ruta.

## Cómo activar GitHub Pages

1. Subir este repo a GitHub (puede ser público o privado con GitHub Pages en plan pago; si es público, cualquiera con el link puede ver el dossier, pero no aparece indexado salvo que lo enlaces).
2. En el repo: **Settings → Pages**.
3. En "Source" elegir la rama `main` y la carpeta `/ (root)`.
4. Guardar. GitHub da una URL tipo:
   `https://TUUSUARIO.github.io/NOMBRE-REPO/`

Cada propiedad quedará en:
- `https://TUUSUARIO.github.io/NOMBRE-REPO/babylon/`
- `https://TUUSUARIO.github.io/NOMBRE-REPO/condado-del-valle/`
- `https://TUUSUARIO.github.io/NOMBRE-REPO/plaza-cristal-barrio-dent/`
- `https://TUUSUARIO.github.io/NOMBRE-REPO/apartamento-moravia/`

## Cómo insertar en Wix

1. Wix Editor → **Insertar (+) → Insertar código propio → Insertar HTML (iframe)**.
2. Elegir "URL de página web" (no "código HTML").
3. Pegar la URL de GitHub Pages de la propiedad correspondiente.
4. Ajustar el tamaño del iframe (ancho 100%, alto según convenga; se puede activar scroll dentro del iframe).

## Editar un dossier

Editar el `index.html` correspondiente directo en GitHub (con el editor web o clonando el repo) y hacer commit. Los cambios se reflejan en la URL de GitHub Pages en 1-2 minutos, sin tocar nada en Wix.

## Subir el repo por primera vez

Desde esta carpeta:

```bash
git init
git add .
git commit -m "Dossiers iniciales JMK"
git branch -M main
git remote add origin https://github.com/TUUSUARIO/NOMBRE-REPO.git
git push -u origin main
```
