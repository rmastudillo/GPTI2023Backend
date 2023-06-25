
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
        # categories_list_secondary, categori2 y subcategori2 sirven para pasar de unimarc a jumbo
        category = category_subcategory[0]
        category2 = category_subcategory_second[0]
        subcategories = category_subcategory[1:]
        subcategories2 = category_subcategory_second[1:]
        category_dict = {}
     
        for subcategory, subcategory2 in zip(subcategories, subcategories2):
            soup = _scraper.get_soup(
                website_url, category, subcategory, selenium)
            
            if supermarket == "unimarc":
                raw_products = soup.find_all(class_="Text_text__cB7NM Shelf_nameProduct__CXI5M Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--regular__KSs6J Text_text--sm__KnF3l Text_text--black__zYYxI Text_text__cursor--pointer__WZsQE Text_text--none__zez2n")
                products_list = [product.text for product in raw_products]
                raw_prices = soup.find_all(class_="Text_text__cB7NM Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--semibold__MukSj Text_text--md__H7JI_ Text_text--guardsman-red__wr1D8 Text_text__cursor--auto__cMaN1 Text_text--none__zez2n")
                price_list = [price.text for price in raw_prices]
                raw_images = soup.find_all(class_="Shelf_defaultImgStyle__ylyx2")
                raw_brands = soup.find_all(class_="Text_text__cB7NM Shelf_brandText__sGfsS Text_text--left__1v2Xw Text_text--flex__F7yuI Text_text--semibold__MukSj Text_text--sm__KnF3l Text_text--black__zYYxI Text_text__cursor--pointer__WZsQE Text_text--none__zez2n")
                raw_brands = soup.find_all(class_="shelf-product-brand")
            else:
                raw_products= soup.find_all(class_="shelf-product-title-text")
                products_list = [product.text for product in raw_products]
                raw_prices= soup.find_all(class_="product-sigle-price-wrapper")
                price_list = [price.text for price in raw_prices]
                raw_images=soup.find_all("img")
                raw_brands = soup.find_all(class_="shelf-product-brand")
                brand_list = [brand.text for brand in raw_brands]

            subcategory_dict = {}
            for product, price, image, brand in zip(products_list, price_list, raw_images, brand_list):
                price_string = ''.join(
                    caracter for caracter in price if caracter.isdigit())
                price_num = int(price_string)
                product_dict = {
                    "precio": price_num,
                    "marca" : brand,
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
    products_jumbo = create_products_dict(jumbo_categories, "https://www.jumbo.cl", "jumbo", jumbo_categories)
    with open("products_jumbo_3.json", mode="w", encoding='utf8') as products_file:
       _json.dump(products_jumbo, products_file, ensure_ascii=False)


    # products_santaisabel = create_products_dict(jumbo_categories, "https://www.santaisabel.cl", "santa isabel",jumbo_categories, "selenium")
    # with open("products_santaisabel.json", mode="w", encoding='utf8') as products_file:
    #     _json.dump(products_santaisabel, products_file, ensure_ascii=False)

    # products_unimarc = create_products_dict(unimarc_categories, "https://www.unimarc.cl/category", "unimarc",jumbo_categories, "selenium")

    # with open("products_unimarc.json", mode="w", encoding='utf8') as products_file:
    #     _json.dump(products_unimarc, products_file, ensure_ascii=False)