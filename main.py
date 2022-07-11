import gspread

from controller.spec_controller import SpecController
from model.spec_items_model import SpecItemsModel
from view.spreadsheet_view import SpreadSheetView

PATH_TO_SERVICE_ACC = 'specupdater_service_acc.json'
SPREADSHEET_NAME = 'ptzn_spec_test'
WORKSHEET_NAME = 'main_sheet'


def main():
    sa = gspread.service_account(filename=PATH_TO_SERVICE_ACC)
    sh = sa.open(SPREADSHEET_NAME)
    worksheet = sh.worksheet(WORKSHEET_NAME)

    model = SpecItemsModel()
    view = SpreadSheetView(worksheet)
    controller = SpecController(model, view)
    controller.update_spec()


if __name__ == '__main__':
    main()
