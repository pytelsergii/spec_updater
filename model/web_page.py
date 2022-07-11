from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class ProductWebPage:
    def __init__(self, driver, url, product_locators):
        self._driver: WebDriver = driver
        self.url = url
        self._product_locators = product_locators

    def open(self):
        self._driver.get(self.url)

    def product_name(self):
        try:
            name = self._driver.find_element(*self._product_locators['name']).text
        except NoSuchElementException:
            name = ''
        return name

    def product_price(self):
        try:
            price = self._driver.find_element(*self._product_locators['price']).text
        except NoSuchElementException:
            price = ''
        return price

    def product_image(self):
        try:
            image = self._driver.find_element(*self._product_locators['image']).get_attribute("src")
        except NoSuchElementException:
            print('No element')
            image = ''
        return image
