import logging
import urllib.parse

from model.spec_item import SpecItem
from model.item_page import ItemWebPage
from utils import str_utils

from selenium.webdriver.remote.webdriver import WebDriver

logger = logging.getLogger(__name__)


class SpecItemsModel:
    def __init__(self, driver):
        self._driver: WebDriver = driver

    @staticmethod
    def get_spec_item(spec_item_page: ItemWebPage):
        spec_item_page.open()

        name = spec_item_page.name
        price = str_utils.str_price_to_float(spec_item_page.price)
        image_url = spec_item_page.image_url

        logger.info(f'Item name: {name}')
        logger.info(f'Item price: {price}')
        logger.info(f'Item image_url: {image_url}')
        return SpecItem(name, price, image_url)

    def get_spec_items(self, urls: list[str], locators: dict) -> list[SpecItem]:
        items = []

        for url in urls:
            logger.info(f'Trying to get details for - {url}')
            locator_key = urllib.parse.urlparse(url).netloc
            logger.info(f'Locator key is {locator_key}')

            if locator_key in locators:
                # Switching to a new tab for each page
                self._driver.switch_to.new_window('tab')
                spec_item = self.get_spec_item(ItemWebPage(self._driver, url, locators[locator_key]))
                items.append(spec_item)
            else:
                logger.warning(f'Locator key - {locator_key} is not present in specified locators')
                items.append(SpecItem('NOT FOUND', 0, 'NOT FOUND'))

        # Quit driver after getting all details
        self._driver.quit()
        return items

    # def get_spec_items(self, urls: list[str], locators: dict) -> list[SpecItem]:
    #     items = []
    #
    #     for url in urls:
    #         logger.info(f'Trying to get details for - {url}')
    #         locator_key = urllib.parse.urlparse(url).netloc
    #         logger.info(f'Locator key is {locator_key}')
    #
    #         if locator_key in locators:
    #             # Switching to a new tab for each page
    #             self._driver.switch_to.new_window('tab')
    #             spec_item_page = ItemWebPage(self._driver, url, locators[locator_key])
    #             spec_item_page.open()
    #
    #             name = spec_item_page.name
    #             price = str_utils.str_price_to_float(spec_item_page.price)
    #             image_url = spec_item_page.image_url
    #
    #             logger.info(f'Item name: {name}')
    #             logger.info(f'Item price: {price}')
    #             logger.info(f'Item image_url: {image_url}')
    #             items.append(SpecItem(name, price, image_url))
    #         else:
    #             logger.warning(f'Locator key - {locator_key} is not present in specified locators')
    #             items.append(SpecItem('NOT FOUND', 'NOT FOUND', 'NOT FOUND'))
    #
    #     # Quit driver after getting all details
    #     self._driver.quit()
    #     return items
