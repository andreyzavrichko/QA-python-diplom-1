import pytest

from data import Data
from selenium import webdriver
from pages.main_page import MainPage
from pages.call_taxi_page import CallTaxiPage


@pytest.fixture(scope="function")
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.fixture
def main_page(driver) -> MainPage:
    page = MainPage(driver)
    page.go_to_url(Data.urls.MAIN_PAGE)
    return page


@pytest.fixture
def call_taxi_page(main_page) -> CallTaxiPage:
    main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
    main_page.confirm_order_taxi()
    return CallTaxiPage(main_page.driver)


@pytest.fixture
def call_taxi_page_waiting(call_taxi_page) -> CallTaxiPage:
    call_taxi_page.open_waiting_window()
    return call_taxi_page


@pytest.fixture
def call_taxi_page_final(call_taxi_page_waiting) -> CallTaxiPage:
    call_taxi_page_waiting.wait_for_timer_to_expire()
    return call_taxi_page_waiting


@pytest.fixture
def call_taxi_page_price(main_page) -> CallTaxiPage:
    main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
    return CallTaxiPage(main_page.driver)