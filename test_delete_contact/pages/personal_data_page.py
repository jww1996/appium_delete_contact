from test_delete_contact.pages.basepage import BasePage
from test_delete_contact.pages.delete_contact_page import DeleteContact


class PersonalData(BasePage):

    def goto_datapage(self):
        self.steps("../pages/page_yaml/personal_data.yaml", "goto_datapage")
        return DeleteContact(self.driver)
