import allure

from data import Data


class TestTaxiPreparation:

    @allure.title("При переключении Быстрый → Оптимальный пересчитываются время и стоимость")
    def test_route_data_changes_on_tab_switch(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        assert main_page.is_route_data_changed_on_tab_switch(), (
            "Время и стоимость не изменились после переключения таба"
        )

    @allure.title("После переключения на Оптимальный активен таб 'Оптимальный'")
    def test_active_tab_is_optima_after_switch(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        active_tab = main_page.get_active_tab_text()
        assert active_tab == Data.route.ACTIVE_TAB, (
            f"Ожидался активный таб '{Data.route.ACTIVE_TAB}', получен '{active_tab}'"
        )

    @allure.title("В маршруте Свой все виды транспорта становятся кликабельными")
    def test_all_transport_types_clickable_in_own(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        assert main_page.is_all_transport_clickable_in_own(), (
            "Один или несколько видов транспорта не кликабельны в маршруте Свой"
        )

    @allure.title("В маршруте Быстрый активна кнопка 'Вызвать такси'")
    def test_call_taxi_button_is_active(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        assert main_page.is_call_taxi_button_active(), (
            "Кнопка 'Вызвать такси' не активна в маршруте Быстрый"
        )

    @allure.title("В маршруте Свой, транспорт Драйв, активна кнопка 'Забронировать'")
    def test_confirmation_button_is_active_for_drive(self, main_page):
        main_page.add_two_address(Data.addresses.LOCATION_1, Data.addresses.LOCATION_2)
        assert main_page.is_confirmation_button_active(), (
            "Кнопка 'Забронировать' не активна в маршруте Свой, транспорт Драйв"
        )
