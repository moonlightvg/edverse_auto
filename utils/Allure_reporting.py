import allure  # Импортируем библиотеку Allure для отчетов
from playwright.sync_api import Page  # Импортируем Page

class AllureReporting:  # Создаем класс для методов Allure
    @staticmethod  # Статический метод
    def attach_screenshot(page: Page, name: str = "screenshot"):  # Метод для прикрепления скриншота
        """Прикрепляет скриншот к Allure отчету"""  # Докстринг
        screenshot = page.screenshot()  # Делаем скриншот (возвращает байты)
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)  
        # allure.attach() - прикрепляем файл к отчету
        # screenshot - содержимое файла (байты)
        # name - имя вложения
        # attachment_type - тип файла (PNG, JSON, TEXT, WEBM и т.д.)
    
    @staticmethod
    def attach_video(path: str):  # Метод для прикрепления видео
        """Прикрепляет видео к Allure отчету"""  # Докстринг
        with open(path, "rb") as f:  # Открываем файл в бинарном режиме для чтения
            # "rb" - read binary, читаем как бинарные данные
            allure.attach(f.read(), name="video", attachment_type=allure.attachment_type.WEBM)  
            # f.read() - читаем содержимое файла
            # WEBM - формат видео из Playwright