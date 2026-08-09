class PageReady:  # Класс для проверки готовности страницы
    @staticmethod
    def wait_for_page_load(page: Page):
        """Ожидание загрузки страницы: DOM построен и ресурсы загружены."""
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_load_state("load")
        # и флакает на сайтах с фоновыми запросами.