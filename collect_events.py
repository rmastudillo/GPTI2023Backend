import datetime as _dt
from datetime import date
from typing import Dict, Iterator
import scraper as _scraper
import json as _json
from jumbo_categories import jumbo_categories
from santaisabel_categories import santaisabel_categories


def create_products_dict(categories_list, website_url, supermarket, selenium=None) -> Dict:
    products = {}

    print("File parsing started...")
    for category_subcategory in categories_list:
        category = category_subcategory[0]
        subcategories = category_subcategory[1:]

        category_dict = {}
        # Jumbo scraper
        for subcategory in subcategories:
            soup = _scraper.get_soup(
                website_url, category, subcategory, selenium)
            raw_prices = soup.find_all(class_="product-sigle-price-wrapper")
            
            price_list = [price.text for price in raw_prices]
            raw_products = soup.find_all(class_="shelf-product-title-text")
            products_list = [product.text for product in raw_products]
            raw_images = soup.find_all("img")
            subcategory_dict = {}
            for product, price, image in zip(products_list, price_list, raw_images):
                price_string = ''.join(
                    caracter for caracter in price if caracter.isdigit())
                price_num = int(price_string)
                product_dict = {
                    "precio": price_num,
                    "supermercado": supermarket,
                    "url_imagen": image["src"]
                }
                subcategory_dict[product] = product_dict
                
            category_dict[subcategory] = subcategory_dict

        products[category] = category_dict

    print("File parsing completed!")
    print("Open products.json file to see the results")
    return products


if __name__ == '__main__':
    # products_jumbo = create_products_dict(jumbo_categories, "https://www.jumbo.cl", "jumbo")
    products_santaisabel = create_products_dict(santaisabel_categories, "https://www.santaisabel.cl", "santa isabel", "selenium")
    # with open("products_jumbo.json", mode="w", encoding='utf8') as products_file:
    #    _json.dump(products_jumbo, products_file, ensure_ascii=False)

    with open("products_santaisabel.json", mode="w", encoding='utf8') as products_file:
        _json.dump(products_santaisabel, products_file, ensure_ascii=False)
