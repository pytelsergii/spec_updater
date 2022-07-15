import pytest


@pytest.fixture
def mocked_webdriver(mocker):
    mocked = mocker.patch("selenium.webdriver.remote.webdriver.WebDriver")
    return mocked
