import allure

from data import Data


class TestRouteDrawing:

    @allure.title("При вводе двух разных адресов на карте отображаются две точки маршрута")
    def test_two_route_dots_visible_on_map(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        assert main_page.drawing_a_route(), (
            "Одна или обе точки маршрута не отображаются на карте"
        )
