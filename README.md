# Яндекс.Маршруты — автотесты

Учебный проект UI-автотестирования сервиса «Яндекс.Маршруты».  
Стек: **Python · Selenium · pytest · Allure · Page Object Model**

---

## Структура проекта

```
project/
├── data.py                        # Тестовые данные (датаклассы)
├── pytest.ini                     # Конфигурация pytest
├── requirements.txt               # Зависимости
├── locators/
│   ├── main_page_locators.py      # Локаторы главной страницы
│   └── call_taxi_page_locators.py # Локаторы формы заказа такси
├── pages/
│   ├── base_page.py               # Базовый page object
│   ├── main_page.py               # Главная страница
│   └── call_taxi_page.py          # Форма заказа такси
└── tests/
    ├── conftest.py                # Фикстуры
    ├── test_route_drawing.py      # Отрисовка маршрута
    ├── test_route_block.py        # Блок выбора маршрута
    ├── test_taxi_preparation.py   # Подготовка к заказу такси
    ├── test_taxi_order.py         # Форма заказа тарифа
    └── test_taxi_flow.py          # Полный флоу заказа
```

---

## Установка

```bash
pip install -r requirements.txt
```

Требуется установленный браузер **Google Chrome** и совместимый `chromedriver`.

---

## Запуск тестов

```bash
# Все тесты
pytest

# Конкретный модуль
pytest tests/test_taxi_flow.py

# С подробным выводом
pytest -v
```

---

## Allure-отчёт

```bash
# Запустить тесты и собрать данные
pytest --alluredir=allure-results

# Открыть отчёт
allure serve allure-results
```

---

## Покрытие

| Модуль | Блок по ТЗ | 
|---|---|
| `test_route_drawing` | Отрисовка маршрута |
| `test_route_block` | Блок выбора маршрута |
| `test_taxi_preparation` | Подготовка к заказу такси |
| `test_taxi_order` | Форма заказа тарифа |
| `test_taxi_flow` | Полный флоу заказа |

Тесты с известными багами помечены `@pytest.mark.xfail`.
