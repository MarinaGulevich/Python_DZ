from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        username_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        )
        username_field.clear()
        username_field.send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        password_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Нажать кнопку 'Login'")
    def click_login(self) -> None:
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()