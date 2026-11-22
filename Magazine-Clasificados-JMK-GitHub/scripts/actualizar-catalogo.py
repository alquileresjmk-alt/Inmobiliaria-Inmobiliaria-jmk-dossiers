"""Regenera el catálogo del navegador sin dependencias externas."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent
items=json.loads((p/'catalogo.json').read_text(encoding='utf-8'))
keys=set()
for item in items:
    assert item['key'] not in keys, 'Clave de flyer duplicada'
    keys.add(item['key'])
    assert item['category'] in ['Alquiler','Venta','Comercial','Proyectos','Otros']
    for field in ['image','thumbnail']:
        assert (p/item[field]).is_file(), f'Falta imagen: {item[field]}'
(p/'catalogo.js').write_text('window.JMK_EDITION = "Colección digital";\nwindow.JMK_CATALOG = '+json.dumps(items,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(f'Catálogo actualizado: {len(items)} flyers.')
