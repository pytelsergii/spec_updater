import logging

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger(__name__)


class ItemWebPage:
    def __init__(self, driver, url, spec_item_locators):
        self._driver: WebDriver = driver
        self.url: str = url
        self._spect_item_locators: dict = spec_item_locators

    def open(self) -> None:
        self._driver.get(self.url)

    def _find_element(self, locator: tuple[By, str]) -> WebElement:
        element = None
        try:
            element = self._driver.find_element(*locator)
        except NoSuchElementException as e:
            logger.warning(e)
        return element

    @property
    def name(self) -> str:
        name = self._find_element(self._spect_item_locators['name'])
        return name.text if name else ''

    @property
    def price(self) -> str:
        price = self._find_element(self._spect_item_locators['price'])
        return price.text if price else ''

    @property
    def image_url(self) -> str:
        image_url = self._find_element(self._spect_item_locators['image'])
        return image_url.get_attribute("src") if image_url else ''
