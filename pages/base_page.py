import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from data import SHORT_WAIT, LONG_WAIT
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, SHORT_WAIT)
        self.long_wait = WebDriverWait(self.driver, LONG_WAIT)

    @allure.step("Поиск элемента с ожиданием пока не будет виден")
    def find_element_with_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов с ожиданием пока не будут видны все")
    def find_elements_with_wait(self, locator):
        self.wait.until(ec.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание пока элемент перестанет быть видимым")
    def waiting_to_invisible_element(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located(locator))

    @allure.step("Длинное ожидание пока элемент перестанет быть видимым")
    def long_waiting_to_invisible_element(self, locator) -> WebElement:
        return self.long_wait.until(ec.invisibility_of_element_located(locator))

    @allure.step("Переход по URL")
    def go_to_url(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Ввести текст в поле ввода")
    def add_text_to_element(self, locator, text: str) -> None:
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator) -> None:
        self.find_element_with_wait(locator).click()

    @allure.step("Навести на элемент")
    def hover_at_element(self, element) -> None:
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Проскролить до элемента")
    def scroll_to_element(self, locator) -> None:
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator) -> str:
        return self.find_element_with_wait(locator).text

    @allure.step("Получить список текстов из двух элементов")
    def get_list_text_from_elements(self, locator_1, locator_2) -> list:
        return [
            self.get_text_from_element(locator_1),
            self.get_text_from_element(locator_2),
        ]

    @allure.step("Проверить что элемент видимый")
    def check_element_visible(self, locator) -> bool:
        try:
            self.find_element_with_wait(locator)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить кликабельность элемента")
    def check_element_is_clickable(self, locator) -> bool:
        self.wait.until(ec.element_to_be_clickable(locator))
        return True

    @allure.step("Ввести адреса отправления и назначения")
    def add_two_address(self, from_address: str, to_address: str) -> None:
        self.add_text_to_element(MainPageLocators.FROM_FIELD, from_address)
        self.add_text_to_element(MainPageLocators.TO_FIELD, to_address)

    @allure.step("Нажать на кнопку Вызвать такси")
    def confirm_order_taxi(self) -> None:
        self.click_on_element(MainPageLocators.CALL_TAXI)
