import allure

from data import Data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Проверка отображения двух точек маршрута на карте")
    def drawing_a_route(self) -> tuple[bool, bool]:
        return (
            self.check_element_visible(MainPageLocators.FROM_DOT),
            self.check_element_visible(MainPageLocators.TO_DOT),
        )

    @allure.step("Проверка видимости блока выбора маршрута")
    def is_route_block_visible(self) -> bool:
        for locator in MainPageLocators.LOCATORS_OF_CHOICE:
            if not self.check_element_visible(locator):
                return False
        return True

    @allure.step("Ввод одинакового адреса и получение текста блока маршрута")
    def get_same_address_route_text(self) -> list:
        self.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_1)
        return self.get_list_text_from_elements(
            MainPageLocators.TYPE_AND_PRICE_DELIVERY,
            MainPageLocators.TRAVEL_TIME,
        )

    @allure.step("Проверка изменения данных маршрута при переключении Быстрый → Оптимальный")
    def is_route_data_changed_on_tab_switch(self) -> bool:
        text_quick = self.get_list_text_from_elements(
            MainPageLocators.TYPE_AND_PRICE_DELIVERY,
            MainPageLocators.TRAVEL_TIME,
        )
        self.click_on_element(MainPageLocators.OPTIMA)
        text_optima = self.get_list_text_from_elements(
            MainPageLocators.TYPE_AND_PRICE_DELIVERY,
            MainPageLocators.TRAVEL_TIME,
        )
        return text_quick != text_optima

    @allure.step("Получение текста активного таба после переключения на Оптимальный")
    def get_active_tab_text(self) -> str:
        self.click_on_element(MainPageLocators.OPTIMA)
        return self.get_text_from_element(MainPageLocators.ACTIVE_TAB)

    @allure.step("Проверка кликабельности всех типов транспорта в маршруте Свой")
    def is_all_transport_clickable_in_own(self) -> bool:
        self.click_on_element(MainPageLocators.OWN)
        for locator in MainPageLocators.LOCATORS_OF_TRANSPORT:
            if not self.check_element_is_clickable(locator):
                return False
        return True

    @allure.step("Проверка активности кнопки 'Вызвать такси'")
    def is_call_taxi_button_active(self) -> bool:
        return self.check_element_is_clickable(MainPageLocators.CALL_TAXI)

    @allure.step("Проверка активности кнопки 'Забронировать' для маршрута Свой, тип Драйв")
    def is_confirmation_button_active(self) -> bool:
        self.click_on_element(MainPageLocators.OWN)
        self.find_element_with_wait(MainPageLocators.TYPE_DRIVE)
        self.click_on_element(MainPageLocators.TYPE_DRIVE)
        self.find_element_with_wait(MainPageLocators.CONFIRMATION)
        return self.check_element_is_clickable(MainPageLocators.CONFIRMATION)

    @allure.step("Нажать на кнопку Вызвать такси")
    def confirm_order_taxi(self) -> None:
        self.click_on_element(MainPageLocators.CALL_TAXI)
