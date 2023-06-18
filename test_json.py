
# import json

# # Cargar el archivo JSON
# with open("products.json", mode="r", encoding="utf8") as json_file:
#     products_data = json.load(json_file)

# # Obtener el detalle de productos por subcategoría de cada categoría
# for category, subcategories in products_data.items():
#     print(f"{category}:")
#     for subcategory, products in subcategories.items():
#         if subcategory == "PROMEDIO":
#             continue
#         num_products = len(products)
#         print(f"- {subcategory}: {num_products} productos")
#     print()


import json

with open('products_jumbo.json', 'r') as file1:
    json1 = json.load(file1)

with open('products_santaisabel.json', 'r') as file2:
    json2 = json.load(file2)


with open('productos_totales.json', 'r') as file3:
    json3 = json.load(file3)
# Diccionario para realizar un seguimiento de los productos encontrados
productos_encontrados = {}

# Iterar a través de las categorías, subcategorías y productos
for categoria, subcategorias in json3.items():
    for subcategoria, productos in subcategorias.items():
        for producto, detalles in productos.items():
            # Obtener los atributos del producto
            nombre = producto
            precio = detalles["precio"]
            supermercado = detalles["supermercado"]
            url = detalles["url_imagen"]
            
            # Comprobar si el producto ya ha sido encontrado
            if (nombre, precio, supermercado, url) in productos_encontrados:
                print("Duplicado encontrado:")
                print("Nombre: ", nombre)
                print("Precio: ", precio)
                print("Supermercado: ", supermercado)
                print("URL: ", url)
                print()
            
            # Agregar el producto al diccionario de productos encontrados
            productos_encontrados[(nombre, precio, supermercado, url)] = True
