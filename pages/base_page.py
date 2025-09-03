import time

from playwright.sync_api import Page


class BasePage:
    script = f"""
                    () => {{
                        document.addEventListener("mousedown", (e) => {{
                          const ripple = document.createElement("div");
                          ripple.style.position = "fixed";
                          ripple.style.left = e.clientX + "px";
                          ripple.style.top = e.clientY + "px";
                          ripple.style.width = "30px";
                          ripple.style.height = "30px";
                          ripple.style.border = "2px solid red";
                          ripple.style.borderRadius = "50%";
                          ripple.style.pointerEvents = "none";
                          ripple.style.transform = "translate(-50%, -50%) scale(0)";
                          ripple.style.opacity = "0.8";
                          ripple.style.transition = "transform 0.2s ease-out, opacity 0.3s ease-out";
                          document.body.appendChild(ripple);
                          requestAnimationFrame(() => {{
                            ripple.style.transform = "translate(-50%, -50%) scale(2.5)";
                            ripple.style.opacity = "0";
                          }});
                          setTimeout(() => ripple.remove(), 700);
                        }});
                    }}
                    """

    def __init__(self, page: Page):
        self._page = page

    def add_text(self, locator, text):
        element = self._page.locator(locator)
        element.evaluate(f"""
               (el) => {{
                   const origShadow = el.style.boxShadow;
                   const origBackground = el.style.backgroundColor;
                   el.style.border = '3px solid red'; 
                   el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
                   el.style.backgroundColor = '#eeebd0';

                   setTimeout(() => {{
                       el.style.boxShadow = origShadow;
                       el.style.backgroundColor = origBackground;
                   }}, 300);
               }}
           """)
        self._page.locator(locator).fill(text)

    def click(self, my_locator):
        time.sleep(0.5)
        self._page.evaluate(BasePage.script)
        self._page.locator(my_locator).click()

    def click_first(self, my_first_locator):
        time.sleep(1)
        self._page.evaluate(BasePage.script)
        self._page.locator(my_first_locator).first.click()

    def get_text(self, locator_text):
        return self._page.locator(locator_text).first.text_content()

    def get_all_text(self, locator_all):
        return self._page.locator(locator_all).all_text_contents()

    def nav(self, nav_selector, title):
        self._page.evaluate(BasePage.script)
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
