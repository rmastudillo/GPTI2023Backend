import json

# Importar la estructura
from jumbo_categories import jumbo_categories

def procesar_json(json_data):
    productos_vistos = set()  # Conjunto para almacenar los productos vistos
    productos_a_eliminar = []  # Lista para almacenar los productos a eliminar

    for categoria, subcategorias in json_data.items():
        for subcategoria, productos in subcategorias.items():
            for producto, detalles in list(productos.items()):
                
                if producto in productos_vistos:
                    productos_a_eliminar.append((categoria, subcategoria, producto))  # Agregar producto duplicado a la lista
                    print("Producto eliminado porque está duplicado:")
                    print(producto)
                else:
                    productos_vistos.add(producto)

                if "pack" in producto.lower():
                    productos_a_eliminar.append((categoria, subcategoria, producto))  # Agregar producto con "pack" a la lista
                    print("Producto eliminado porque contiene 'pack':")
                    print(producto)
                
                if detalles.get("precio", 0) == 0:
                    productos_a_eliminar.append((categoria, subcategoria, producto))  # Agregar producto con precio 0 a la lista
                    print("Producto eliminado por tener precio 0:")
                    print(producto)

    # eliminar productos
    for categoria, subcategoria, producto in productos_a_eliminar:
        if categoria in json_data and subcategoria in json_data[categoria] and producto in json_data[categoria][subcategoria]:
            del json_data[categoria][subcategoria][producto]

    return json_data

# Cargar el JSON
with open('productos_lider.json', 'r') as file:
    json_string = file.read()

# Parsear el JSON
data = json.loads(json_string)

# Procesar el JSON
data_procesada = procesar_json(data)

# Convertir el JSON procesado de nuevo a un string
json_modificado = json.dumps(data_procesada)

# Especificar la ruta y nombre del archivo de salida
ruta_archivo_salida = 'productos_lider_proc.json'

# Guardar el JSON modificado en el archivo de salida
with open(ruta_archivo_salida, 'w') as file:
    file.write(json_modificado)

print("JSON modificado guardado en:", ruta_archivo_salida)
