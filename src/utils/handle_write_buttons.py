import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from src.utils.send_message import send_message


def handle_write_buttons(driver, button_list):
    """
    Обрабатывает список кнопок для отправки сообщений.

    :param driver: Экземпляр WebDriver.
    :param button_list: Список кнопок для обработки.
    """
    sent_count = 0
    max_messages = 300

    def click_next_button():
        """
        Рекурсивно обрабатывает следующую кнопку из списка.
        """
        nonlocal sent_count
        # Проверяем, достигнут ли лимит отправленных сообщений
        if sent_count >= max_messages:
            print(f"Отправлено {max_messages} сообщений. Процесс остановлен.")
            return

        # Проверяем, остались ли кнопки для обработки
        if not button_list:
            print("Все кнопки обработаны. Успешно отправлено сообщений:", sent_count)
            return

        # Берем следующую кнопку из списка и кликаем на нее
        button = button_list.pop(0)
        button.click()

        try:
            # Проверяем, есть ли уже сообщение в чате
            is_message = driver.find_element(By.CSS_SELECTOR, 'span[data-marker="messageText"]')
            if not is_message:
                # Если сообщения нет, отправляем новое
                send_message(driver)
                sent_count += 1
        except NoSuchElementException:
            # Если элемент не найден, отправляем сообщение
            send_message(driver)
            sent_count += 1
        except Exception as e:
            print("Ошибка при обработке кнопки:", e)

        # Ждем 20 секунд перед обработкой следующей кнопки
        time.sleep(20)
        click_next_button()

    # Запускаем обработку кнопок
    click_next_button()
