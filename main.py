import logging

import gspread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import BaseWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import config
from controller.spec_controller import SpecController
from model.spec_items_model import SpecItemsModel
from view.spreadsheet_view import SpreadSheetView

logger = logging.getLogger(__name__)
PATH_TO_SERVICE_ACC_JSON = 'specupdater_service_acc.json'
SPREADSHEET_NAME = 'ptzn_spec_test'
WORKSHEET_NAME = 'main_sheet'


def setup_driver(conf: dict) -> BaseWebDriver:
    driver_option = conf['driver']['driver_option']
    is_headless = conf['driver']['headless']
    logger.info(f'Is headless mode - {is_headless}')

    if driver_option == 'Firefox':
        logger.info(f'Driver under use - {driver_option}')
        options = FirefoxOptions()
        options.headless = is_headless
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        logger.info(f'Driver under use - Chrome')
        options = ChromeOptions()
        options.headless = is_headless
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    return driver


def main():
    service_account = gspread.service_account(filename=PATH_TO_SERVICE_ACC_JSON)
    spreadsheet = service_account.open(SPREADSHEET_NAME)
    worksheet = spreadsheet.worksheet(WORKSHEET_NAME)

    conf = config.setup_config()
    driver = setup_driver(conf)

    model = SpecItemsModel(driver)
    view = SpreadSheetView(worksheet)
    controller = SpecController(model, view)
    controller.update_spec()


if __name__ == '__main__':
    main()
