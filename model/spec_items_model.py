import urllib.parse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from model.locators import locators
from model.web_page import ProductWebPage
from model.product import Product


class SpecItemsModel:
    def __init__(self):
        pass

    @staticmethod
    def price_str_to_float(price_str):
        price_str = price_str.replace(',', '.')
        formatted_price = ''.join(i for i in price_str if i.isdigit() or i == '.')
        if formatted_price.endswith('.'):
            formatted_price = formatted_price[:-1]
        try:
            price = float(''.join(formatted_price))
        except ValueError:
            price = 0
        return price

    def get_products(self, urls):
        products = []

        for url in urls:
            locator_key = urllib.parse.urlparse(url).netloc
            print(locator_key)

            if locator_key in locators:
                options = Options()
                options.headless = False

                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

                product_page = ProductWebPage(driver, url, locators[locator_key])
                product_page.open()

                name = product_page.product_name()
                price = self.price_str_to_float(product_page.product_price())
                image = product_page.product_image()

                products.append(Product(name, price, image))
            else:
                products.append(Product('NOT FOUND', 'NOT FOUND', ''))

        return products
