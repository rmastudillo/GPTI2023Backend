import json


# Leer los archivos JSON
with open('products_jumbo.json', 'r') as file1:
    json1 = json.load(file1)

with open('products_santaisabel.json', 'r') as file2:
    json2 = json.load(file2)




# productos_unicos_jumbo = {}

# for categoria, productos in json1.items():
#     for subcategoria, productos_subcategoria in productos.items():
#         for producto, detalles in productos_subcategoria.items():
#             nombre_producto = producto
#             precio = detalles["precio"]
#             supermercado = detalles["supermercado"]
            
#             # Imprimir los datos
#             print("Producto:", nombre_producto)
#             print("Precio:", precio)
#             print("Supermercado:", supermercado)
#             print("--------------------")



# productos_unicos_santaisabel = {}

# for producto, detalles in json2.items():
    
#     if producto not in productos_unicos_santaisabel:
#         productos_unicos_santaisabel[producto] = detalles




# with open("productos_santaisabel_unico.json", mode="w", encoding='utf8') as products_file:
#     json.dump(productos_unicos_santaisabel, products_file, ensure_ascii=False)



# with open("productos_unicos_jumbo.json", mode="w", encoding='utf8') as products_file:
#     json.dump(productos_unicos_jumbo, products_file, ensure_ascii=False)



def fusionar_productos(json1, json2):
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

                            if nombre[-1]  == 'g':
                                nombre += "ramo"
                            elif nombre[-1] == 'l':
                                nombre += "itro"
                            else:
                                nombre += "_t"

                resultado.setdefault(categoria, {}).setdefault(subcategoria, {})[nombre] = detalles

    return resultado


# Fusionar los archivos JSON
resultado = fusionar_productos(json1, json2)

# Guardar el resultado en un nuevo archivo JSON
with open('productos_totales.json', 'w') as output_file:
    json.dump(resultado, output_file)

# def verificar_duplicados(json_data):
#     nombres = []
#     duplicados = []

#     # Recorrer el JSON y verificar duplicados
#     for categoria, subcategorias in json_data.items():
#         for subcategoria, productos in subcategorias.items():
#             for nombre, detalles in productos.items():
#                 if nombre in nombres:
#                     duplicados.append(nombre)
#                 else:
#                     nombres.append(nombre)

#     if duplicados:
#         print("Se encontraron duplicados de nombres:")
#         for nombre in duplicados:
#             print(nombre)
#     else:
#         print("No se encontraron duplicados de nombres.")

# # Leer el archivo JSON
# with open('productos_totales.json', 'r') as file:
#     json_data = json.load(file)

# # Verificar duplicados de nombres
# verificar_duplicados(json_data)



