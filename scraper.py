from typing import List
import requests as _requests
import bs4 as _bs4




def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def get_products() -> List[str]:
    url = "https://www.jumbo.cl/carniceria/vacuno"
    page = _get_page(url)
    raw_products = page.find_all(class_="shelf-product-title-text")
    #print('This are the raw products',raw_products)
    products = [product.text for product in raw_products]
    return products

def get_prices() -> List[str]:
    url = "https://www.jumbo.cl/carniceria/vacuno"
    page = _get_page(url)
    raw_prices = page.find_all(class_="product-sigle-price-wrapper")
    prices = [price.text for price in raw_prices]
    return prices

