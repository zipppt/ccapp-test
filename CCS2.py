import unittest
from selenium import webdriver
from shared import doLogin, doPersonaInformation1, doSubmit, doClean, doApply, doOpen, doForm3, doCCS



class CCAPPCCS2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)
    def doLogin(self):
        doLogin(self.driver)
    def doCCS(self):
        doCCS(self.driver)
    def doPersonaInformation1(self):
        doPersonaInformation1(self.driver)
    def doSubmit(self):
        doSubmit(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doForm3(self):
        doForm3(self.driver)
    def doClean(self):
        doClean(self.driver)

    def test_ccapp_CCS2(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doCCS()
        self.doPersonaInformation1()
        self.doSubmit()

        window_parent = driver.current_window_handle
        window_popup = driver.window_handles[-1]
        element = driver.find_element_by_xpath("//div[@class='col-sm-10']/p[14]/a")
        element.click()
        self.driver.implicitly_wait(5)
        driver.switch_to.window(window_popup)

        self.doForm3()

        driver.switch_to.window(window_parent)

        self.doApply()
        self.doClean()


    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


