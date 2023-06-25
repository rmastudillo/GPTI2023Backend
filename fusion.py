import json

def fusionar_productos(json1, json2, json3, json4):
    resultado = {}

    # Fusionar json1 en resultado
    for categoria, subcategorias in json1.items():
        for subcategoria, productos in subcategorias.items():
            resultado.setdefault(categoria, {}).setdefault(subcategoria, {}).update(productos)

    # Fusionar json2 en resultado, cambiando sutilmente los nombres de los productos duplicados
    for categoria, subcategorias in json2.items():
        for subcategoria, productos in subcategorias.items():
            for nombre, detalles in productos.items():
                if categoria in resultado and subcategoria in resultado[categoria]:
                    for nombre_existente in resultado[categoria][subcategoria]:
                        if nombre == nombre_existente:
                            # Cambiar sutilmente el nombre del producto
                            if nombre[-1] == ' g':
                                nombre += "ramo"
                            elif nombre[-1] == ' l':
                                nombre += "itro"
                            else:
                                nombre += " t"

                resultado.setdefault(categoria, {}).setdefault(subcategoria, {})[nombre] = detalles

    # Fusionar json3 en resultado, cambiando sutilmente los nombres de los productos duplicados
    for categoria, subcategorias in json3.items():
        for subcategoria, productos in subcategorias.items():
            for nombre, detalles in productos.items():
                if categoria in resultado and subcategoria in resultado[categoria]:
                    for nombre_existente in resultado[categoria][subcategoria]:
                        if nombre == nombre_existente:
                            # Cambiar sutilmente el nombre del producto
                            nombre += " l"

                resultado.setdefault(categoria, {}).setdefault(subcategoria, {})[nombre] = detalles

    # Fusionar json4 en resultado, cambiando sutilmente los nombres de los productos duplicados
    for categoria, subcategorias in json4.items():
        for subcategoria, productos in subcategorias.items():
            for nombre, detalles in productos.items():
                if categoria in resultado and subcategoria in resultado[categoria]:
                    for nombre_existente in resultado[categoria][subcategoria]:
                        if nombre == nombre_existente:
                            # Cambiar sutilmente el nombre del producto
                            nombre += " n"

                resultado.setdefault(categoria, {}).setdefault(subcategoria, {})[nombre] = detalles

    return resultado


# Leer los archivos JSON
with open('productos_jumbo_proc.json', 'r') as file1:
    json1 = json.load(file1)

with open('productos_santaisabel_proc.json', 'r') as file2:
    json2 = json.load(file2)

with open('productos_lider_proc.json', 'r') as file3:
    json3 = json.load(file3)

with open('productos_unimarc_proc.json', 'r') as file4:
    json4 = json.load(file4)

# Fusionar los archivos JSON
resultado = fusionar_productos(json1, json2, json3, json4)

# Guardar el resultado en un nuevo archivo JSON
with open('productos_totales.json', 'w') as output_file:
    json.dump(resultado, output_file)
