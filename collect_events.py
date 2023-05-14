import datetime as _dt
from datetime import date
from typing import Dict, Iterator
import scraper as _scraper
import json as _json


def create_products_dict() -> Dict:
    products = dict()

    print("File parsing started...")
    price_list = _scraper.get_prices()
    products_list = _scraper.get_products()
    
    for i in range(20):
        products[products_list[i]] = price_list[i]


    products["PROMEDIO"] = round(sum([float(price[1:]) for price in price_list])/len(price_list),3)
        
    print("File parsing completed!")
    print("Open events.json file to see the results")
    return products

if __name__ == '__main__':
    products = create_products_dict()
    with open("products.json", mode="w", encoding='utf8') as products_file:
        _json.dump(products, products_file, ensure_ascii=False)
