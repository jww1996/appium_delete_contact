from selenium.webdriver.common.by import By

from test_delete_contact.pages.basepage import BasePage


class DeleteContact(BasePage):

    def goto_deletecontact(self):
        self.steps("../pages/page_yaml/delete_contact_page.yaml", "goto_deletecontact")
        return self
    def result(self):
        self._eles2 = self.driver.find_elements(By.XPATH, '//*[@text="联系人"]/../..//*[@resource-id="com.tencent.wework:id/avi"]')
        return self._eles2