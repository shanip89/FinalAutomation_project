import time

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def add_text(self, locator, text):
        self._page.locator(locator).fill(text)

    def click(self, my_locator):
        time.sleep(1)
        self._page.locator(my_locator).click()

    def click_first(self, my_first_locator):
        time.sleep(1)
        self._page.locator(my_first_locator).first.click()

    def get_text(self, locator_text):
        return self._page.locator(locator_text).first.text_content()

    def get_all_text(self, locator_all):
        return self._page.locator(locator_all).all_text_contents()

    def nav(self, nav_selector, title):
        self._page.locator(nav_selector).hover()
        nav_list = self._page.locator(f"{nav_selector}  >> li >> a")
        count = nav_list.count()
        for i in range(count):
            nav_item = nav_list.nth(i)
            nav_text = nav_item.inner_text().strip()

            if nav_text == title:
                nav_item.hover()
                nav_item.click()
                return nav_item  # מחזיר את האלמנט שמצא
        raise Exception(f"'{title}' not found in navigation '{nav_selector}'")
