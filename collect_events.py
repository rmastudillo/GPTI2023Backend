import datetime as _dt
from datetime import date
from typing import Dict, Iterator
import scraper as _scraper
import json as _json
from jumbo_categories import jumbo_categories

def create_products_dict(categories_list, website_url, supermarket) -> Dict:
    products = {}

    print("File parsing started...")

    for category_subcategory in categories_list:
        category = category_subcategory[0]
        subcategories = category_subcategory[1:]

        category_dict = {}
        # Jumbo scraper    
        for subcategory in subcategories:
            price_list = _scraper.get_prices(website_url, category, subcategory)
            products_list = _scraper.get_products(website_url,category, subcategory)

            subcategory_dict = {}
            for product, price in zip(products_list, price_list):
                product_dict = {
                    "precio": price,
                    "supermercado": supermarket
                }
                subcategory_dict[product] = product_dict

        

            category_dict[subcategory] = subcategory_dict

        products[category] = category_dict

    print("File parsing completed!")
    print("Open products.json file to see the results")
    return products




if __name__ == '__main__':
    products_jumbo = create_products_dict(jumbo_categories, "https://www.jumbo.cl/", "jumbo")
    # products_santaisabel = create_products_dict(jumbo_categories, "https://www.santaisabel.cl/")
    with open("products_jumbo.json", mode="w", encoding='utf8') as products_file:
        _json.dump(products_jumbo, products_file, ensure_ascii=False)
    
    # with open("products_santaisabel.json", mode="w", encoding='utf8') as products_file:
    #     _json.dump(products_santaisabel, products_file, ensure_ascii=False)
