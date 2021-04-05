from test_delete_contact.pages.basepage import BasePage
from test_delete_contact.pages.click_search_page import ClickSearch
from test_delete_contact.pages.search_page import SearchPage


class InformationPage(BasePage):

    def goto_addresslist(self):
        self.steps("../pages/page_yaml/information_page.yaml", "goto_addresslist")
        return ClickSearch(self.driver)
