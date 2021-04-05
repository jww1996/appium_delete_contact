from selenium.webdriver.common.by import By

from test_delete_contact.pages.basepage import BasePage
from test_delete_contact.pages.personal_data_page import PersonalData


class SearchPage(BasePage):
    def search_member(self, username):
        self._params["name"] = username
        self.steps("../pages/page_yaml/search_page.yaml", "search_member")
        self._eles1 = self.driver.find_elements(By.XPATH, '//*[@text="联系人"]/../..//*[@resource-id="com.tencent.wework:id/avi"]')
        return self._eles1

    def goto_memberinfo(self):
        if len(self._eles1) > 0:
            self._eles1[0].click()
        return PersonalData(self.driver)
