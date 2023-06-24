import datetime as _dt
from datetime import date
from typing import Dict, Iterator
import scraper as _scraper
import json as _json
from jumbo_categories import jumbo_categories
from unimarc_categories import unimarc_categories

def create_products_dict(categories_list, website_url, supermarket,categories_list_secondary, selenium=None) -> Dict:
    products = {}

    print("File parsing started...")
    for category_subcategory, category_subcategory_second in zip(categories_list, categories_list_secondary):
        category = category_subcategory[0]
        category2 = category_subcategory_second[0]
        subcategories = category_subcategory[1:]
        subcategories2 = category_subcategory_second[1:]
        category_dict = {}
        # Jumbo scraper
        for subcategory, subcategory2 in zip(subcategories, subcategories2):
            for i in range(1,3):
                soup = _scraper.get_soup(
                    website_url, category, subcategory, i, selenium)
            
                raw_products = soup.find_all(class_="Text_text__cB7NM Shelf_nameProduct__CXI5M Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--regular__KSs6J Text_text--sm__KnF3l Text_text--black__zYYxI Text_text__cursor--pointer__WZsQE Text_text--none__zez2n")
                # raw_products= soup.find_all(class_="shelf-product-title-text")
                products_list = [product.text for product in raw_products]
                # raw_prices= soup.find_all(class_="product-sigle-price-wrapper")
                raw_prices = soup.find_all(class_="Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--semibold__MukSj Text_text--md__H7JI_ Text_text--guardsman-red__wr1D8 Text_text__cursor--auto__cMaN1 Text_text--none__zez2n")
                price_list = [price.text for price in raw_prices]
                raw_images = soup.find_all(class_="Shelf_defaultImgStyle__ylyx2")
                # raw_images=soup.find_all("img")

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
                    
                category_dict[subcategory2] = subcategory_dict

            products[category2] = category_dict

    print("File parsing completed!")
    print("Open products.json file to see the results")
    return products


if __name__ == '__main__':
    # products_jumbo = create_products_dict(jumbo_categories, "https://www.jumbo.cl", "jumbo", jumbo_categories, "selenium")
    # with open("products_jumbo_3.json", mode="w", encoding='utf8') as products_file:
    #    _json.dump(products_jumbo, products_file, ensure_ascii=False)


    # products_santaisabel = create_products_dict(jumbo_categories, "https://www.santaisabel.cl", "santa isabel",jumbo_categories, "selenium")
    # with open("products_santaisabel.json", mode="w", encoding='utf8') as products_file:
    #     _json.dump(products_santaisabel, products_file, ensure_ascii=False)

    products_unimarc = create_products_dict(unimarc_categories, "https://www.unimarc.cl/category/", "unimarc",jumbo_categories, "selenium")

    with open("products_unimarc_2.json", mode="w", encoding='utf8') as products_file:
        _json.dump(products_unimarc, products_file, ensure_ascii=False)