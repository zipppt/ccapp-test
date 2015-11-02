import unittest
from selenium import webdriver
from shared import doLogin, doForm, doApply, doShining_Star_Award, doOpen

class CCAPPShining_Star_Award(unittest.TestCase):

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
    def doShining_Star_Award(self):
        doShining_Star_Award(self.driver)
    def test_ccapp_Shining_Star_Award(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doShining_Star_Award()
        self.doForm()
        self.doApply()
        self.assertIn("Award nomination forms", driver.page_source)

    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()
