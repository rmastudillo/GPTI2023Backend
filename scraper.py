from typing import List
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import requests as _requests
import bs4 as _bs4


def get_page_source(url: str) -> str:
    chrome_options = Options()
    # Ejecuta el navegador en modo headless (sin interfaz gráfica)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # Espera un tiempo suficiente para que se carguen los datos dinámicos (puedes ajustar el tiempo según sea necesario)
    time.sleep(1)
    page_source = driver.page_source
    driver.quit()
    return page_source


def _get_page(url: str) -> BeautifulSoup:
    page = requests.get(url)
    return page.content


def get_soup(url: str, category: str, subcategory: str, selenium=None) -> List[str]:
    if category == "":
        url = url + "/" + subcategory
    else:
        url = url + "/" + category + "/" + subcategory
    page_source = get_page_source(url) if selenium else _get_page(url)
    soup = BeautifulSoup(page_source, "html.parser")
    return soup

