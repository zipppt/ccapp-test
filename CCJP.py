import unittest
from selenium import webdriver
from shared import doLogin, doPersonaInformation, doSubmit1, doClean, doApply, doOpen, doForm4, doCCJP



class CCAPPCCJP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)
    def doLogin(self):
        doLogin(self.driver)
    def doCCJP(self):
        doCCJP(self.driver)
    def doPersonaInformation(self):
        doPersonaInformation(self.driver)
    def doSubmit1(self):
        doSubmit1(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doForm4(self):
        doForm4(self.driver)
    def doClean(self):
        doClean(self.driver)

    def test_ccapp_CCJP(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doCCJP()
        self.doPersonaInformation()
        self.doSubmit1()

        window_parent = driver.current_window_handle
        window_popup = driver.window_handles[-1]
        element = driver.find_element_by_xpath("//div[@class='col-sm-10']/p[4]/a")
        element.click()
        self.driver.implicitly_wait(5)
        driver.switch_to.window(window_popup)

        self.doForm4()

        driver.switch_to.window(window_parent)

        self.doApply()
        self.doClean()


    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


