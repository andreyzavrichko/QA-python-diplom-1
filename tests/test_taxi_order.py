import allure
import pytest

from data import Data


class TestTaxiOrder:

    @allure.title("В форме заказа отображаются 6 тарифов по ТЗ")
    def test_six_taxi_tariffs_visible(self, call_taxi_page):
        assert call_taxi_page.is_get_6_taxi_titles(), (
            "Не отображаются 6 тарифов по ТЗ"
        )

    @allure.title("Один из 6 тарифов активен")
    def test_one_tariff_is_active(self, call_taxi_page):
        assert call_taxi_page.is_one_active_taxi_title(), (
            "Ни один тариф не активен"
        )

    @pytest.mark.parametrize(
        "taxi_title, expected_description",
        [
            (Data.tariffs.TITLES[0], Data.tariffs.DESCRIPTIONS[0]),
            pytest.param(
                Data.tariffs.TITLES[1], Data.tariffs.DESCRIPTIONS[1],
                marks=pytest.mark.xfail(reason="Баг: у тарифа Сонный отображается описание от Разговорчивый"),
            ),
            (Data.tariffs.TITLES[2], Data.tariffs.DESCRIPTIONS[2]),
            pytest.param(
                Data.tariffs.TITLES[3], Data.tariffs.DESCRIPTIONS[3],
                marks=pytest.mark.xfail(reason="Баг: у тарифа Разговорчивый отображается описание от Сонный"),
            ),
            (Data.tariffs.TITLES[4], Data.tariffs.DESCRIPTIONS[4]),
            (Data.tariffs.TITLES[5], Data.tariffs.DESCRIPTIONS[5]),
        ],
    )
    @allure.title("Описание тарифа '{taxi_title}' соответствует ТЗ")
    def test_tariff_description_matches_spec(self, call_taxi_page, taxi_title, expected_description):
        actual = call_taxi_page.get_tariff_description(taxi_title)
        assert actual == expected_description, (
            f"Тариф '{taxi_title}': ожидалось '{expected_description}', получено '{actual}'"
        )

    @pytest.mark.parametrize("field_name", Data.order_block.FIELDS)
    @allure.title("Поле '{field_name}' отображается в блоке заказа")
    def test_order_field_is_visible(self, call_taxi_page, field_name):
        assert call_taxi_page.is_visible_order_field(field_name), (
            f"Поле '{field_name}' не отображается в блоке заказа"
        )