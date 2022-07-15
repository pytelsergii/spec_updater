import re

from gspread import Worksheet, Cell

from model.spec_item import SpecItem


class SpreadSheetView:
    COLUMN_PRODUCT_NAME_INDEX = 3
    COLUMN_PRODUCT_IMAGE_INDEX = 2
    COLUMN_PRODUCT_PRICE_INDEX = 6

    def __init__(self, worksheet):
        self._worksheet: Worksheet = worksheet

    def get_working_cells(self) -> list[Cell]:
        search_criteria = re.compile(r'(http|https)')
        return self._worksheet.findall(search_criteria)

    def get_spec_items_urls(self) -> list[str]:
        return [cell.value for cell in self.get_working_cells()]

    def update(self, spec_items: list[SpecItem]) -> None:
        for cell, spect_item in zip(self.get_working_cells(), spec_items):
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_NAME_INDEX, spect_item.name)
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_PRICE_INDEX, spect_item.price)
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_IMAGE_INDEX, f'=image("{spect_item.image_url}")')

    def clear_previous_values(self) -> None:
        for cell in self.get_working_cells():
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_NAME_INDEX, '')
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_PRICE_INDEX, '')
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_IMAGE_INDEX, '')
