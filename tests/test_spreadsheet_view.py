import re
from unittest.mock import call

import pytest
from gspread import Cell

from model.spec_item import SpecItem
from view.spreadsheet_view import SpreadSheetView


@pytest.fixture
def mocked_worksheet(mocker):
    worksheet = mocker.patch("gspread.worksheet.Worksheet")
    worksheet.findall.return_value = [Cell(1, 1, 'url1'), Cell(2, 2, 'url2')]
    return worksheet


@pytest.fixture
def spreadsheet_view(mocked_worksheet):
    return SpreadSheetView(mocked_worksheet)


def test_get_working_cells(spreadsheet_view, mocked_worksheet):
    spreadsheet_view.get_working_cells()
    mocked_worksheet.findall.assert_called_with(re.compile(r'(http|https)'))


def test_get_spec_items_urls(spreadsheet_view, mocked_worksheet):
    assert spreadsheet_view.get_spec_items_urls() == ['url1', 'url2'], 'Incorrect urls'


def test_update(mocked_worksheet, spreadsheet_view):
    spec_items = [SpecItem('Item1', 2050, 'img_url1'), SpecItem('Item2', 100.5, 'img_url2')]
    spreadsheet_view.update(spec_items)
    expected_calls = [
        call(1, spreadsheet_view.COLUMN_PRODUCT_NAME_INDEX, 'Item1'),
        call(1, spreadsheet_view.COLUMN_PRODUCT_PRICE_INDEX, 2050),
        call(1, spreadsheet_view.COLUMN_PRODUCT_IMAGE_INDEX, '=image("img_url1")'),
        call(2, spreadsheet_view.COLUMN_PRODUCT_NAME_INDEX, 'Item2'),
        call(2, spreadsheet_view.COLUMN_PRODUCT_PRICE_INDEX, 100.5),
        call(2, spreadsheet_view.COLUMN_PRODUCT_IMAGE_INDEX, '=image("img_url2")')
    ]
    assert mocked_worksheet.update_cell.mock_calls == expected_calls, 'Incorrect calls triggered'


def test_clear_previous_values(mocked_worksheet, spreadsheet_view):
    spreadsheet_view.clear_previous_values()
    expected_calls = [
        call(1, spreadsheet_view.COLUMN_PRODUCT_NAME_INDEX, ''),
        call(1, spreadsheet_view.COLUMN_PRODUCT_PRICE_INDEX, ''),
        call(1, spreadsheet_view.COLUMN_PRODUCT_IMAGE_INDEX, ''),
        call(2, spreadsheet_view.COLUMN_PRODUCT_NAME_INDEX, ''),
        call(2, spreadsheet_view.COLUMN_PRODUCT_PRICE_INDEX, ''),
        call(2, spreadsheet_view.COLUMN_PRODUCT_IMAGE_INDEX, '')
    ]
    assert mocked_worksheet.update_cell.mock_calls == expected_calls, 'Incorrect calls triggered'
