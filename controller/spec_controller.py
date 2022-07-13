from model.spec_items_model import SpecItemsModel
from view.spreadsheet_view import SpreadSheetView


class SpecController:
    def __init__(self, model, view):
        self._model: SpecItemsModel = model
        self._view: SpreadSheetView = view

    def update_spec(self) -> None:
        urls = self._view.get_spec_items_urls()
        products = self._model.get_spec_items(urls)
        self._view.update(products)

    def clear_spec(self) -> None:
        self._view.clear_previous_values()
