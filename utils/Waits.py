from playwright.sync_api import Page, expect  # Импортируем Page и expect из Playwright

class Waits:  # Создаем класс для группировки методов ожидания
    @staticmethod  # Декоратор, делает метод статическим (не требует создания объекта класса)
    def wait_for_element(page: Page, selector: str, timeout: int = 30):  # Статический метод ожидания элемента
        """Ожидание появления элемента"""  # Докстринг
        expect(page.locator(selector)).to_be_visible(timeout=timeout * 1000)  
        # expect() - функция Playwright для проверки ожиданий
        # to_be_visible() - ожидание, что элемент станет видимым
        # timeout - таймаут в миллисекундах (по умолчанию 30 секунд)
        # timeout * 1000 - переводим секунды в миллисекунды
    
    @staticmethod
    def wait_for_text(page: Page, text: str, timeout: int = 30):  # Статический метод ожидания текста
        """Ожидание появления текста"""  # Докстринг
        expect(page.get_by_text(text)).to_be_visible(timeout=timeout * 1000)  
        # page.get_by_text(text) - ищем элемент по тексту