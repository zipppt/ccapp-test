import unittest
from selenium import webdriver
from shared import doLogin, doForm, doApply, doVIP_Award, doOpen

class CCAPPVIP_Award(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)
    def doLogin(self):
        doLogin(self.driver)
    def doForm(self):
        doForm(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doVIP_Award(self):
        doVIP_Award(self.driver)
    def test_ccapp_Spotlight_Award(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doVIP_Award()
        self.doForm()
        self.doApply()
        self.assertIn("Award nomination forms", driver.page_source)

    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()

