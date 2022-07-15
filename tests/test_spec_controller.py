import pytest

from controller.spec_controller import SpecController
from model.locators import locators
from model.spec_item import SpecItem


@pytest.fixture
def mocked_spreadsheet_view(mocker):
    return mocker.patch("view.spreadsheet_view.SpreadSheetView")


@pytest.fixture
def mocked_spec_items_model(mocker):
    return mocker.patch("model.spec_items_model.SpecItemsModel")


@pytest.fixture
def mocked_spec_controller(mocked_spec_items_model, mocked_spreadsheet_view):
    return SpecController(mocked_spec_items_model, mocked_spreadsheet_view)


def test_update_spec(mocked_spec_controller, mocked_spec_items_model, mocked_spreadsheet_view):
    mocked_spreadsheet_view.get_spec_items_urls.return_value = ['url1', ['url2']]
    spect_items = [SpecItem('Name1', 'price1', 'image_url1'), SpecItem('Name2', 'price2', 'image_url2')]
    mocked_spec_items_model.get_spec_items.return_value = spect_items
    mocked_spec_controller.update_spec()
    mocked_spreadsheet_view.get_spec_items_urls.assert_called_once()
    mocked_spec_items_model.get_spec_items.assert_called_with(['url1', ['url2']], locators)
    mocked_spreadsheet_view.update.assert_called_with(spect_items)


def test_clear_spec(mocked_spreadsheet_view, mocked_spec_controller):
    mocked_spec_controller.clear_spec()
    mocked_spreadsheet_view.clear_previous_values.assert_called_once()
