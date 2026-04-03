import allure

from pages.login_page import LoginPage



@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Успешный вход")
    @allure.title("После входа происходит редирект на главную страницу")
    def test_login_redirects_to_main(self, driver):
        login_page = LoginPage(driver)
        login_page.open()

