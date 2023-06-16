
import json

# Cargar el archivo JSON
with open("products.json", mode="r", encoding="utf8") as json_file:
    products_data = json.load(json_file)

# Obtener el detalle de productos por subcategoría de cada categoría
for category, subcategories in products_data.items():
    print(f"{category}:")
    for subcategory, products in subcategories.items():
        if subcategory == "PROMEDIO":
            continue
        num_products = len(products)
        print(f"- {subcategory}: {num_products} productos")
    print()
