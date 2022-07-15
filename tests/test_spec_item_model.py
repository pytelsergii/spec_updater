from unittest.mock import call

import pytest
from selenium.webdriver.common.by import By

from model.spec_item import SpecItem
from model.spec_items_model import SpecItemsModel


@pytest.fixture
def spec_items_model(mocked_webdriver):
    return SpecItemsModel(mocked_webdriver)


@pytest.fixture
def mocked_item_web_page(mocker):
    mocked_page = mocker.patch("model.item_page.ItemWebPage")
    mocked_page.url = 'url1'
    mocked_page.name = 'Item Name'
    mocked_page.price = '1500.5'
    mocked_page.image_url = 'Item Image url'
    return mocked_page


@pytest.fixture
def spec_items_model_with_fake_get_spec_item(spec_items_model):
    spec_items_model.get_spec_item = lambda x: SpecItem("Item", 1500, 'url1')
    return spec_items_model


def test_get_spec_item(spec_items_model, mocked_item_web_page):
    spec_item = spec_items_model.get_spec_item(mocked_item_web_page)
    mocked_item_web_page.open.assert_called_once()
    assert spec_item.name == mocked_item_web_page.name, 'Name is incorrect'
    assert spec_item.price == 1500.5, 'Price is incorrect'
    assert spec_item.image_url == mocked_item_web_page.image_url, 'Image url is incorrect'


def test_get_spec_items_successful(spec_items_model_with_fake_get_spec_item, mocked_webdriver):
    urls = ['https://shoploft.com.ua/products/lyustra-tulip-15p--',
            'https://jysk.ua/dlya-sadu/mebli-dlya-vidpochinku/launzh-stilec/launzh-stilets-ubberup-chornyy']

    locators = {
        'jysk.ua': {
            'name': (By.CSS_SELECTOR, 'div.product-name-sku span.product-name'),
            'image': (By.CSS_SELECTOR, 'img.img-responsive.carousel-image'),
            'price': (By.CSS_SELECTOR, 'span.ssr-product-price__value')
        },
        'shoploft.com.ua': {
            'name': (By.CSS_SELECTOR, 'h1.product_information_title'),
            'image': (By.CSS_SELECTOR, 'div.product span.product__img img'),
            'price': (By.CSS_SELECTOR, 'div.product_information_price span.current_price')
        }}

    items = spec_items_model_with_fake_get_spec_item.get_spec_items(urls, locators)
    expected_switch_calls = [call('tab'), call('tab')]
    # Check if we call webdriver.switch_to.new_window only tww times, one for each url
    assert mocked_webdriver.switch_to.new_window.mock_calls == expected_switch_calls
    mocked_webdriver.quit.assert_called_once()
    assert items == [SpecItem("Item", 1500, 'url1'), SpecItem("Item", 1500, 'url1')]


def test_get_spec_items_no_locators_available(spec_items_model):
    items = spec_items_model.get_spec_items(['url1', 'url2'], locators={})
    assert items == [SpecItem('NOT FOUND', 0, 'NOT FOUND'), SpecItem('NOT FOUND', 0, 'NOT FOUND')]
