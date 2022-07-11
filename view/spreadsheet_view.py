import re

from gspread import Worksheet


class SpreadSheetView:
    COLUMN_PRODUCT_NAME_INDEX = 3
    COLUMN_PRODUCT_IMAGE_INDEX = 2
    COLUMN_PRODUCT_PRICE_INDEX = 6

    def __init__(self, worksheet):
        self._worksheet: Worksheet = worksheet

    @property
    def working_cells(self):
        search_criteria = re.compile(r'(http|https)')
        return self._worksheet.findall(search_criteria)

    def get_spec_items_urls(self):
        return [cell.value for cell in self.working_cells]

    def update(self, products):
        for cell, product in zip(self.working_cells, products):
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_NAME_INDEX, product.name)
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_PRICE_INDEX, product.price)
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_IMAGE_INDEX, f'=image("{product.image}")')

    def clear_previous_values(self, ):
        for cell in self.working_cells:
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_NAME_INDEX, '')
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_PRICE_INDEX, '')
            self._worksheet.update_cell(cell.row, self.COLUMN_PRODUCT_IMAGE_INDEX, '')
