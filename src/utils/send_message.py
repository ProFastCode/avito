import time
from src.utils.wait_for_element import wait_for_element


def send_message(driver):
    """
    Отправляет сообщение через интерфейс мессенджера.

    :param driver: Экземпляр WebDriver.
    """
    try:
        # Находим и кликаем на кнопку быстрых ответов
        quick_replies = wait_for_element(driver, 'span[data-marker="reply/quickRepliesSelectorOpener"]')
        quick_replies.click()

        # Находим и кликаем на первый быстрый ответ
        first_quick_reply = wait_for_element(driver, 'div[data-marker="quickReplies/selectorItem"]')
        first_quick_reply.click()

        # Находим кнопку отправки сообщения
        send_button = wait_for_element(driver, 'span[aria-label="Отправить сообщение"]')

        # Проверяем, активна ли кнопка отправки
        if send_button.get_attribute('aria-disabled') == 'true':
            # Если кнопка неактивна, ждем 0.5 секунды и повторяем попытку
            time.sleep(0.5)
            send_message(driver)
        else:
            # Если кнопка активна, отправляем сообщение
            send_button.click()
            print("Сообщение отправлено!")
    except Exception as e:
        print("Ошибка при отправке сообщения:", e)

