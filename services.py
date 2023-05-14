from typing import Dict
import json as _json
import datetime as _dt

def get_products() -> Dict:
    with open("products.json", encoding='utf-8') as products_file:
        data = _json.load(products_file)
        
    return data

