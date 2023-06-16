from typing import List
import requests as _requests
import bs4 as _bs4




# def _get_page(url: str) -> _bs4.BeautifulSoup:
#     page = _requests.get(url)
#     soup = _bs4.BeautifulSoup(page.content, "html.parser")
#     return soup

# def get_products() -> List[str]:
#     url = "https://www.jumbo.cl/carniceria/vacuno"
#     page = _get_page(url)
#     raw_products = page.find_all(class_="shelf-product-title-text")
#     #print('This are the raw products',raw_products)
#     products = [product.text for product in raw_products]
#     return products

# def get_prices() -> List[str]:
#     url = "https://www.jumbo.cl/carniceria/vacuno"
#     page = _get_page(url)
#     raw_prices = page.find_all(class_="product-sigle-price-wrapper")
#     prices = [price.text for price in raw_prices]
#     return prices


# def scrape_categories():
#     url = "https://www.jumbo.cl/"
#     page = _get_page(url)
#     category_buttons = page.find_all("div", class_="new-header-supermarket-button")

#     categories = []

#     for category_button in category_buttons:
#         category_name = category_button.find("h3").text
#         print("Category:", category_name)

#         # Obtener URL de la categoría
#         category_url = category_button.find("a")["href"]

#         # Realizar solicitud HTTP a la URL de la categoría
#         category_page = _get_page(category_url)
#         product_titles = category_page.find_all(class_="shelf-product-title-text")

#         products = [product_title.text for product_title in product_titles]

#         category_data = {
#             "category": category_name,
#             "products": products
#         }

#         categories.append(category_data)

#     return categories


def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def get_products(category: str, subcategory: str) -> List[str]:
    base_url = "https://www.jumbo.cl/"
    url = base_url + category + "/" + subcategory
    page = _get_page(url)
    raw_products = page.find_all(class_="shelf-product-title-text")
    products = [product.text for product in raw_products]
    return products

def get_prices(category: str, subcategory: str) -> List[str]:
    base_url = "https://www.jumbo.cl/"
    url = base_url + category + "/" + subcategory
    page = _get_page(url)
    raw_prices = page.find_all(class_="product-sigle-price-wrapper")
    prices = [price.text for price in raw_prices]
    return prices


