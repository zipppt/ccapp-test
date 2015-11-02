import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared import doLogin, doPersonaInformation, doSubmit, doApply, doClean, doOpen, doRadt1, doRegHis




class CCAPPRADT1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)

    def doLogin(self):
        doLogin(self.driver)
    def doRadt1(self):
        doRadt1(self.driver)
    def doPersonaInformation(self):
        doPersonaInformation(self.driver)
    def doSubmit(self):
        doSubmit(self.driver)
    def doRegHis(self):
        doRegHis(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doClean(self):
        doClean(self.driver)
    def test_ccapp_radt1(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doRadt1()
        self.doPersonaInformation()
        self.doSubmit()
        self.doRegHis()
        self.doApply()

        element = driver.find_element_by_xpath("//input[@id='id_type_0']")
        element.click()
        self.doApply()
        self.doClean()



    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()
