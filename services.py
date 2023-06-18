from typing import Dict, List
import json as _json
import datetime as _dt


# ojo que modifique a products_jumbo.json
def get_products() -> Dict:
    with open("products_jumbo.json", encoding='utf-8') as products_file:
        data = _json.load(products_file)

    return data


def buscar_productos(palabra_clave: str = None, supermercado: str = None, categoriaQuery: str = None, subcategoriaQuery: str = None) -> List[Dict[str, str]]:
    with open("productos_totales.json", encoding='utf-8') as products_file:
        data = _json.load(products_file)

    productos_encontrados = []

    for categoria, subcategorias in data.items():
        if categoriaQuery and categoriaQuery.lower() != categoria.lower():
            continue

        for subcategoria, productos in subcategorias.items():
            for producto, datos in productos.items():
                if palabra_clave is None or palabra_clave.lower() in producto.lower():
                    if supermercado and supermercado.lower() != datos["supermercado"].lower():
                        continue

                    if subcategoriaQuery and subcategoriaQuery.lower() != subcategoria.lower():
                        continue

                    producto_encontrado = {
                        "nombre": producto,
                        "categoria": categoria,
                        "subcategoria": subcategoria,
                        "precio": datos["precio"],
                        "supermercado": datos["supermercado"],
                        "url_imagen": datos["url_imagen"]
                    }
                    productos_encontrados.append(producto_encontrado)

    productos_encontrados.sort(key=lambda x: float(x["precio"]))
    return productos_encontrados
