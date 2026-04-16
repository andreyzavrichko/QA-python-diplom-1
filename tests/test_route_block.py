import allure

from data import Data


class TestRouteBlock:

    @allure.title("При вводе двух разных адресов отображается блок выбора маршрута")
    def test_route_block_visible_with_different_addresses(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        assert main_page.is_route_block_visible(), (
            "Блок выбора маршрута не отображается при вводе двух разных адресов"
        )

    @allure.title("При вводе одинакового адреса отображается текст 'Авто Бесплатно' и 'В пути 0 мин.'")
    def test_route_text_with_same_address(self, main_page):
        actual_text = main_page.get_same_address_route_text()
        assert actual_text == list(Data.route.SAME_ADDRESS_TEXT), (
            f"Ожидался текст {Data.route.SAME_ADDRESS_TEXT}, получен {actual_text}"
        )
