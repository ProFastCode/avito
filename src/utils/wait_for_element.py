from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, selector, timeout=5):
    """
    Ожидает появления элемента на странице по заданному CSS-селектору.

    :param driver: Экземпляр WebDriver.
    :param selector: CSS-селектор элемента.
    :param timeout: Время ожидания в секундах.
    :return: Найденный элемент.
    :raises TimeoutException: Если элемент не найден в течение указанного времени.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Элемент {selector} не найден за {timeout} секунд")
