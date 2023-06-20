import json
import requests
import json
import time
import functools

jumbo_to_lider = {
    "lacteos": "Frescos y Lácteos",
    "leches": "Leche",
    "yoghurt": "Yoghurt",
    "postres": "Postres Refrigerados",
    "mantequillas-y-margarinas": "Huevos y Mantequillas",
    "huevos": "Huevos y Mantequillas",
    "leches-cultivadas-y-bebidas-lacteas": "Leche",
    "probioticos-y-defensas": "Leche",
    "despensa": "Despensa",
    "arroz-y-legumbres": "Arroz y Legumbres",
    "pastas-y-salsas": "Pastas y Salsas",
    "coctel": "Cóctel y Snack",
    "conservas": "Conservas",
    "aderezos-y-salsas": "Aceites y Aderezos",
    "reposteria": "Harinas y Polvos",
    "harina-y-complementos": "Harinas y Polvos",
    "aceites-sal-y-condimentos": "Aceites y Aderezos",
    "instantaneos-y-sopas": "Alimentos Instantáneos",
    "comidas-etnicas": "Cocina Internacional",
    "frutas-y-verduras": "Frutas y Verduras",
    "frutas": "Frutas",
    "verduras": "Verduras",
    "frutos-secos-y-semillas": "Frutos Secos",
    "carniceria": "Carnes y Pescados",
    "vacuno": "Vacuno",
    "cerdo": "Cerdo",
    "pollo": "Pollo",
    "pavo": "Pavo",
    "cordero": "Cordero",
    "botilleria": "Bebidas y Licores",
    "bebidas-gaseosas": "Bebidas",
    "aguas-minerales": "Aguas",
    "jugos": "Jugos",
    "bebidas-energeticas": "Bebidas",
    "bebidas-isotonicas": "Bebidas",
    "limpieza": "Limpieza y Aseo",
    "papeles-hogar": "Papeles",
    "limpieza-de-ropa": "Detergentes",
    "bano-y-cocina": "Baño y Cocina",
    "pisos-y-muebles": "Pisos y Muebles",
    "aerosoles-y-desinfectantes": "Desinfección",
    "accesorios-de-limpieza": "Accesorios Aseo",
    "mascotas": "Mascotas",
    "perros": "Perro",
    "gatos": "Gato",
    "otras-mascotas": "Otras Mascotas",
}

jumbo_categories = [
    [
        "lacteos",
        "leches",
        "yoghurt",
        "postres",
        "mantequillas-y-margarinas",
        "huevos",
        "leches-cultivadas-y-bebidas-lacteas",
        "probioticos-y-defensas"
    ],
    [
        "despensa",
        "arroz-y-legumbres",
        "pastas-y-salsas",
        "coctel",
        "conservas",
        "aderezos-y-salsas",
        "reposteria",
        "harina-y-complementos",
        "aceites-sal-y-condimentos",
        "instantaneos-y-sopas",
        "comidas-etnicas"
    ],
    ["frutas-y-verduras",
        "frutas",
        "verduras",
        "frutos-secos-y-semillas"
    ],
    ["carniceria",
        "vacuno",
        "cerdo",
        "pollo",
        "pavo",
        "cordero"
    ],
    ["botilleria",
        "bebidas-gaseosas",
        "aguas-minerales",
        "jugos",
        "bebidas-energeticas",
        "bebidas-isotonicas"
    ],
    ["limpieza",
        "papeles-hogar",
        "limpieza-de-ropa",
        "bano-y-cocina",
        "pisos-y-muebles",
        "aerosoles-y-desinfectantes",
        "accesorios-de-limpieza"
    ],
    ["mascotas",
        "perros",
        "gatos",
        "otras-mascotas"
    ]
]
        
def session_with_proxy(extra_args):
    session = requests.Session()
    session.request = functools.partial(session.request, timeout=30)

    if extra_args and 'proxy' in extra_args:
        proxy = extra_args['proxy']

        session.proxies = {
            'http': proxy,
            'https': proxy,
        }

    return session


def make_request(category, subcategory, page=1, facets=[], sortBy="", hitsPerPage=16):
    session = session_with_proxy({})
    url = 'https://apps.lider.cl/supermercado/bff/category'
    headers = {
        'Content-Type': 'application/json',
        'tenant': 'supermercado',
        'x-channel': 'SOD',
    }
    session.headers = headers
    data = {
        "categories": f"{category}/{subcategory}",
        "page": page,
        "facets": facets,
        "sortBy": sortBy,
        "hitsPerPage": hitsPerPage
    }
    query_params = {
                    "categories": f"{category}/{subcategory}",
                    "page": 1,
                    "facets": [],
                    "sortBy": "",
                    "hitsPerPage": 16
                }

    serialized_params = json.dumps(query_params,
                                    ensure_ascii=False)
    response = session.post(url, serialized_params.encode('utf-8'))
    data = json.loads(response.text)
    converted_response = [convert_product(product) for product in data['products']]
    return converted_response

def convert_product(product):
    # Convert the product object to the new format
    new_product = {
        product['displayName'] : {
            'precio': product['price']['BasePriceSales'],
            'supermercado': 'lider',
            'url_imagen': product['images']['defaultImage']   
        }
    }
    return new_product

def gather_data():
    all_products_by_category_and_subcategories = {}
    
    # Iterates through all the categories and subcategories.
    for categories in jumbo_categories:
        for subcategory_jumbo in categories[1:]:
            category = jumbo_to_lider[categories[0]]
            category_jumbo = categories[0]
            subcategory = jumbo_to_lider[subcategory_jumbo]
            #print(f"Obteniendo productos para {category}/{subcategory}...")
            try:
                # Calls the request function for each category and subcategory.
                products = make_request(category, subcategory)
                if category_jumbo not in all_products_by_category_and_subcategories:
                    all_products_by_category_and_subcategories[category_jumbo] = {}
                all_products_by_category_and_subcategories[category_jumbo][subcategory_jumbo] = {}
                for product in products:
                    all_products_by_category_and_subcategories[category_jumbo][subcategory_jumbo] = {**all_products_by_category_and_subcategories[category_jumbo][subcategory_jumbo], **product}
            except Exception as e:
                print(f"Error al obtener productos para {category}/{subcategory}: {str(e)}")
                
            # Waits a bit to avoid getting blocked for making too many fast requests.
            time.sleep(0.5)
            
    return all_products_by_category_and_subcategories

# Collects all the products and saves them in a JSON file.
def save_to_json():
    all_products = gather_data()
    with open("productos_lider.json", "w", encoding='utf8') as f:
        json.dump(all_products, f, ensure_ascii=False)

save_to_json()