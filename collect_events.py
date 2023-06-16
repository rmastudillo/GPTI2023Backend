import datetime as _dt
from datetime import date
from typing import Dict, Iterator
import scraper as _scraper
import json as _json
from jumbo_categories import jumbo_categories

def create_products_dict(categories_list) -> Dict:
    products = {}

    print("File parsing started...")

    for category_subcategory in categories_list:
        category = category_subcategory[0]
        subcategories = category_subcategory[1:]

        category_dict = {}
        for subcategory in subcategories:
            price_list = _scraper.get_prices(category, subcategory)
            products_list = _scraper.get_products(category, subcategory)

            subcategory_dict = {}
            for product, price in zip(products_list, price_list):
                subcategory_dict[product] = price

            if len(price_list) > 0:
                subcategory_dict["PROMEDIO"] = round(sum([float(price[1:]) for price in price_list])/len(price_list), 3)
            else:
                subcategory_dict["PROMEDIO"] = 0.0

            category_dict[subcategory] = subcategory_dict

        products[category] = category_dict

    print("File parsing completed!")
    print("Open products.json file to see the results")
    return products

if __name__ == '__main__':
    products = create_products_dict(jumbo_categories)
    with open("products.json", mode="w", encoding='utf8') as products_file:
        _json.dump(products, products_file, ensure_ascii=False)
