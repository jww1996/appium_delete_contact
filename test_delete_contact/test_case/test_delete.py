from test_delete_contact.pages.app import App


class TestDelete:
    def setup(self):
        self.app = App()

    def test_delete(self):
        pages = self.app.goto_main().goto_addresslist().goto_searchpage()
        reslut1 = pages.search_member("测试03")
        reslut2 = pages.goto_memberinfo().goto_datapage().goto_deletecontact().result()
        assert len(reslut1) - len(reslut2) ==1
