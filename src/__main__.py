from selenium import webdriver
from selenium.webdriver.common.by import By

from src.utils.wait_for_element import wait_for_element
from src.utils.handle_write_buttons import handle_write_buttons


def start_process(driver):
    """
    Запускает процесс обработки кнопок для отправки сообщений.

    :param driver: Экземпляр WebDriver.
    """
    try:
        # Ожидаем появления кнопок для отправки сообщений
        buttons = wait_for_element(driver, 'button[data-marker="messenger-button/button"]', timeout=10)
        if buttons:
            # Если кнопки найдены, получаем их список
            button_list = driver.find_elements(By.CSS_SELECTOR, 'button[data-marker="messenger-button/button"]')
            # Начинаем обработку кнопок
            handle_write_buttons(driver, button_list)
        else:
            print("Кнопки не найдены.")
    except Exception as e:
        print("Ошибка при ожидании кнопок:", e)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.avito.ru/")
    input("Войдите в аккаунт, выставьте фильтры, а после нажмите <Enter>")
    start_process(driver)
