import datetime as _dt
from datetime import date
from typing import Dict, Iterator
import scraper as _scraper
import json as _json
from jumbo_categories import jumbo_categories

def create_products_dict(categories_list, website_url) -> Dict:
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
                subcategory_dict[product] = price

            # if len(price_list) > 0:
            #     subcategory_dict["PROMEDIO"] = round(sum([float(price[1:]) for price in price_list])/len(price_list), 3)
            # else:
            #     subcategory_dict["PROMEDIO"] = 0.0

            category_dict[subcategory] = subcategory_dict

        products[category] = category_dict

    print("File parsing completed!")
    print("Open products.json file to see the results")
    return products




if __name__ == '__main__':
    products_jumbo = create_products_dict(jumbo_categories, "https://www.jumbo.cl/")
    # products_santaisabel = create_products_dict(jumbo_categories, "https://www.santaisabel.cl/")
    with open("products_jumbo.json", mode="w", encoding='utf8') as products_file:
        _json.dump(products_jumbo, products_file, ensure_ascii=False)
    
    # with open("products_santaisabel.json", mode="w", encoding='utf8') as products_file:
    #     _json.dump(products_santaisabel, products_file, ensure_ascii=False)
