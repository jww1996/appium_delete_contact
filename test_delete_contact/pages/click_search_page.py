from test_delete_contact.pages.basepage import BasePage
from test_delete_contact.pages.search_page import SearchPage


class ClickSearch(BasePage):
    def goto_searchpage(self):
        self.steps("../pages/page_yaml/click_search_page.yaml", "goto_searchpage")
        return SearchPage(self.driver)