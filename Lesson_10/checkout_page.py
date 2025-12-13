from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить поле 'Имя' значением: {first_name}")
    def fill_first_name(self, first_name: str) -> None:
        first_name_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    @allure.step("Заполнить поле 'Фамилия' значением: {last_name}")
    def fill_last_name(self, last_name: str) -> None:
        last_name_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    @allure.step("Заполнить поле 'Почтовый индекс' значением: {postal_code}")
    def fill_postal_code(self, postal_code: str) -> None:
        postal_code_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "postal-code"))
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self) -> None:
        continue_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total_price(self) -> float:
        # Ждем завершения загрузки страницы
        import time
        time.sleep(1)  # Небольшая пауза для стабильности

        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )

        total_text = total_element.text
        # Извлекаем число из строки вида "Total: $58.29"
        total_str = total_text.split("$")[-1]
        return float(total_str)