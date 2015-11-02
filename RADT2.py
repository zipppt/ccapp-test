import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared import doLogin, doPersonaInformation, doSubmit, doApply, doClean, doOpen, doForm2, doRadt2



class CCAPPRADT2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)

    def doLogin(self):
        doLogin(self.driver)
    def doRadt2(self):
        doRadt2(self.driver)
    def doPersonaInformation(self):
        doPersonaInformation(self.driver)
    def doSubmit(self):
        doSubmit(self.driver)
    def doForm2(self):
        doForm2(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doClean(self):
        doClean(self.driver)

    def test_ccapp_radt2(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doRadt2()
        self.doPersonaInformation()
        self.doSubmit()

        window_parent = driver.current_window_handle
        window_popup = driver.window_handles[-1]
        element = driver.find_element_by_xpath("//div[@class='col-sm-10']/p[8]/a")
        element.click()
        self.driver.implicitly_wait(5)
        driver.switch_to.window(window_popup)

        self.doForm2()

        driver.switch_to.window(window_parent)

        self.doApply()
        self.doClean()



    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()

