from typing import Dict
import json as _json
import datetime as _dt


# ojo que modifique a products_jumbo.json
def get_products() -> Dict:
    with open("products_jumbo.json", encoding='utf-8') as products_file:
        data = _json.load(products_file)
        
    return data

