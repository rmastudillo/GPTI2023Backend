from typing import Dict, List
import json as _json
import datetime as _dt


# ojo que modifique a products_jumbo.json
def get_products() -> Dict:
    with open("products_jumbo.json", encoding='utf-8') as products_file:
        data = _json.load(products_file)

    return data


def buscar_productos(palabra_clave: str, supermercado: str = None, categoriaQuery: str = None, subcategoriaQuery: str = None) -> List[Dict[str, str]]:
    with open("products_jumbo.json", encoding='utf-8') as products_file:
        data = _json.load(products_file)

    productos_encontrados = []

    def buscador(subcategorias: Dict) -> None:
        for subcategoria, productos in subcategorias.items():
            for producto, datos in productos.items():
                if palabra_clave.lower() in producto.lower():
                    if (
                        supermercado and
                        supermercado.lower() != datos["supermercado"].lower()
                    ):
                        continue

                    if (
                        subcategoriaQuery and
                        subcategoriaQuery.lower() != subcategoria.lower()
                    ):
                        continue

                    producto_encontrado = {
                        "nombre": producto,
                        "precio": datos["precio"],
                        "supermercado": datos["supermercado"]
                    }
                    productos_encontrados.append(producto_encontrado)

    for categoria, subcategoria in data.items():
        if categoriaQuery and categoriaQuery.lower() != categoria.lower():
            continue
        buscador(subcategoria)

    return productos_encontrados
