import allure
from selenium.common.exceptions import NoSuchElementException

from data import Data
from locators.call_taxi_page_locators import CallTaxiPageLocators
from pages.base_page import BasePage


class CallTaxiPage(BasePage):
    _ORDER_FIELD_MAP = {
        "Телефон": CallTaxiPageLocators.PHONE,
        "Способ оплаты": CallTaxiPageLocators.PAYMENT_METHOD,
        "Комментарий водителю": CallTaxiPageLocators.COMMENT,
        "Требования к заказу": CallTaxiPageLocators.REQUIREMENTS_FOR_ORDER,
        "Заказ тарифа Такси": CallTaxiPageLocators.BUTTON_CREATE_ORDER,
    }

    @allure.step("Проверка что отображаются 6 тарифов по ТЗ")
    def is_get_6_taxi_titles(self) -> bool:
        elements = self.find_elements_with_wait(CallTaxiPageLocators.ELEMENTS_TAXI_TITLE)
        actual_titles = {el.text.strip() for el in elements if el.text.strip()}
        expected_titles = set(Data.tariffs.TITLES)
        return actual_titles == expected_titles and len(actual_titles) == len(expected_titles)

    @allure.step("Проверка что один из тарифов активен")
    def is_one_active_taxi_title(self) -> bool:
        elements = self.find_elements_with_wait(CallTaxiPageLocators.ELEMENTS_TAXI_TITLE)
        active_block = self.find_element_with_wait(CallTaxiPageLocators.ACTIVE_TAXI_TITLE)
        for el in elements:
            try:
                active_block.find_element(*CallTaxiPageLocators.active_taxi_by_title(el.text))
                return True
            except NoSuchElementException:
                continue
        return False

    @allure.step("Получение описания тарифа: {taxi_title}")
    def get_tariff_description(self, taxi_title: str) -> str:
        self.click_on_element(CallTaxiPageLocators.taxi_title_locator(taxi_title))
        taxi_info = self.find_element_with_wait(CallTaxiPageLocators.TAXI_INFO)
        self.hover_at_element(taxi_info)
        name = self.get_text_from_element(CallTaxiPageLocators.TARIFF_NAME)
        self.hover_at_element(taxi_info)
        description = self.get_text_from_element(CallTaxiPageLocators.TARIFF_DESCRIPTION)
        return f"{name} - {description}"

    @allure.step("Проверка видимости поля: {field_name}")
    def is_visible_order_field(self, field_name: str) -> bool:
        locator = self._ORDER_FIELD_MAP[field_name]
        return self.check_element_visible(locator)

    @allure.step("Выбор тарифа Рабочий, включение чекбокса, нажатие 'Ввести номер и заказать'")
    def open_waiting_window(self) -> None:
        self.click_on_element(CallTaxiPageLocators.WORKING)
        self.scroll_to_element(CallTaxiPageLocators.RAIDER)
        self.click_on_element(CallTaxiPageLocators.RAIDER)
        self.scroll_to_element(CallTaxiPageLocators.LAPTOP_TABLE_TOGGLE)
        self.click_on_element(CallTaxiPageLocators.LAPTOP_TABLE_TOGGLE)
        self.click_on_element(CallTaxiPageLocators.BUTTON_ENTER_NUMBER_AND_ORDER)

    @allure.step("Ожидание окончания таймера поиска машины")
    def wait_for_timer_to_expire(self) -> None:
        self.long_waiting_to_invisible_element(CallTaxiPageLocators.TIMER)

    @allure.step("Проверка заголовка 'Поиск машины'")
    def is_visible_search_header(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.HEADER_OF_MODAL)

    @allure.step("Проверка таймера обратного отсчёта")
    def is_visible_timer(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.TIMER)

    @allure.step("Проверка кнопки Отменить в окне поиска")
    def is_visible_cancel_button(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.CANCEL)

    @allure.step("Проверка кнопки Детали в окне поиска")
    def is_visible_details_button(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.ORDER_DETAILS)

    @allure.step("Проверка заголовка 'n мин. и приедет'")
    def is_visible_arrival_header(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.HEADER_OF_FINAL_MODAL)

    @allure.step("Проверка номера автомобиля")
    def is_visible_auto_number(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.AUTO_NUMBER)

    @allure.step("Проверка картинки автомобиля")
    def is_visible_auto_image(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.AUTO_IMG)

    @allure.step("Проверка фото водителя")
    def is_visible_driver_photo(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.DRIVER_FOTO)

    @allure.step("Проверка рейтинга водителя")
    def is_visible_driver_rating(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.DRIVER_RATING)

    @allure.step("Проверка кнопки Отменить в финальном окне")
    def is_visible_cancel_in_final(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.CANCEL)

    @allure.step("Проверка кнопки Детали в финальном окне")
    def is_visible_details_in_final(self) -> bool:
        return self.check_element_visible(CallTaxiPageLocators.ORDER_DETAILS)

    @allure.step("Проверка что имя водителя из допустимого списка")
    def is_driver_name_valid(self) -> bool:
        name = self.get_text_from_element(CallTaxiPageLocators.DRIVER_NAME)
        return name in Data.drivers.NAMES

    @allure.step("Проверка совпадения цены до и после оформления заказа")
    def is_price_equal_before_and_after(self) -> bool:
        text = self.get_text_from_element(CallTaxiPageLocators.PRICE_BEFORE_ORDER)
        price_before = text.split()[2]
        self.confirm_order_taxi()
        self.open_waiting_window()
        self.click_on_element(CallTaxiPageLocators.ORDER_DETAILS)
        text_after = self.get_text_from_element(CallTaxiPageLocators.PRICE_AFTER_ORDER)
        price_after = text_after.split()[2].split("₽")[0]
        return price_before == price_after

    @allure.step("Нажатие Отменить и проверка закрытия модального окна")
    def is_modal_closed_after_cancel(self) -> bool:
        self.click_on_element(CallTaxiPageLocators.CANCEL)
        return self.waiting_to_invisible_element(CallTaxiPageLocators.MODAL_WAITING)
