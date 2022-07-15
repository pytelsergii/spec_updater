import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from model.item_page import ItemWebPage


@pytest.fixture
def mocked_web_element(mocker):
    return mocker.patch("selenium.webdriver.remote.webelement.WebElement")


@pytest.fixture
def item_web_page(mocked_webdriver):
    return ItemWebPage(mocked_webdriver, 'https://bt.rozetka.com.ua/whirlpool_fwdg86148b_eu/p235895875/',
                       {'name': (By.CSS_SELECTOR, 'h1.product__title'),
                        'image': (By.CSS_SELECTOR, 'img.picture-container__picture'),
                        'price': (By.CSS_SELECTOR, 'p.product-prices__big')})


def test_open(item_web_page, mocked_webdriver):
    item_web_page.open()
    mocked_webdriver.get.assert_called_with(item_web_page.url)


def test_name_when_elements_found(item_web_page, mocked_webdriver, mocked_web_element):
    mocked_web_element.text = 'Name'
    mocked_webdriver.find_element.return_value = mocked_web_element
    item_name = item_web_page.name
    mocked_webdriver.find_element.assert_called_with(*item_web_page._spect_item_locators['name'])
    assert item_name == mocked_web_element.text, 'Incorrect name'


def test_name_when_element_not_found(item_web_page, mocked_webdriver):
    mocked_webdriver.find_element.side_effect = NoSuchElementException
    assert item_web_page.name == '', 'Incorrect name'


def test_price(item_web_page, mocked_webdriver, mocked_web_element):
    mocked_web_element.text = '1500 uah'
    mocked_webdriver.find_element.return_value = mocked_web_element
    price = item_web_page.price
    mocked_webdriver.find_element.assert_called_with(*item_web_page._spect_item_locators['price'])
    assert price == mocked_web_element.text, 'Incorrect price'


def test_price_when_element_not_found(item_web_page, mocked_webdriver):
    mocked_webdriver.find_element.side_effect = NoSuchElementException
    assert item_web_page.price == '', 'Incorrect price'


def test_image_url(item_web_page, mocked_webdriver, mocked_web_element):
    mocked_webdriver.find_element.return_value = mocked_web_element
    mocked_web_element.get_attribute.return_value = 'url'
    image_url = item_web_page.image_url
    mocked_web_element.get_attribute.assert_called_with('src')
    mocked_webdriver.find_element.assert_called_with(*item_web_page._spect_item_locators['image'])
    assert image_url == 'url', 'Incorrect image url'


def test_image_url_when_element_not_found(item_web_page, mocked_webdriver):
    mocked_webdriver.find_element.side_effect = NoSuchElementException
    assert item_web_page.image_url == '', 'Incorrect image url'
