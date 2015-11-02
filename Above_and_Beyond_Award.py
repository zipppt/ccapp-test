import unittest
from selenium import webdriver
from shared import doLogin, doForm, doApply, doOpen, doAbove

class CCAPPAbove(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)

    def doLogin(self):
        doLogin(self.driver)
    def doAbove(self):
        doAbove(self.driver)

    def doForm(self):
        doForm(self.driver)
    def doApply(self):
        doApply(self.driver)

    def test_ccapp_Above(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)

        self.doLogin()
        self.doAbove()

        self.doForm()


        self.doApply()
        self.assertIn("Award nomination forms", driver.page_source)

    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


