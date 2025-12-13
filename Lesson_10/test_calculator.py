import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для управления WebDriver."""
    service = Service()  # Chromedriver должен быть в PATH
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор с задержкой")
class TestCalculator:

    @allure.title("Проверка сложения 7 + 8 с задержкой")
    def test_calculator_addition(self, driver):
        """Тест сложения с задержкой 45 секунд."""

        # Открываем страницу
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Создаем Page Object
        calc = CalculatorPage(driver)

        # Устанавливаем задержку
        calc.set_delay("45")

        # Выполняем операцию
        calc.click_button_7()
        calc.click_button_plus()
        calc.click_button_8()
        calc.click_equals()

        # Ждем и проверяем результат (используем метод из Page Object)
        result = calc.get_result()

        # Ждем, пока результат не станет "15" (максимум 60 секунд)
        import time
        start_time = time.time()
        while time.time() - start_time < 60:
            result = calc.get_result()
            if result == "15":
                break
            time.sleep(1)

        # Финальная проверка
        assert result == "15", f"Ожидалось '15', получено '{result}'"
