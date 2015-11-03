import unittest
from selenium import webdriver
from shared import doLogin, doOpen, doCCAPP2, doApply, doPayment_form

class CCAPPCCAPP2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def doOpen(self):
        doOpen(self.driver)

    def doLogin(self):
        doLogin(self.driver)
    def doCCAPP2(self):
        doCCAPP2(self.driver)
    def doApply(self):
        doApply(self.driver)
    def doPayment_form(self):
        doPayment_form(self.driver)

    def test_ccapp_CCAPP2(self):
        driver = self.driver
        self.doOpen()
        self.assertIn("Welcome", driver.title)
        self.doLogin()
        self.doCCAPP2()
        self.doApply()
        self.doApply()
        self.doPayment_form()
        self.doApply()

        driver.get("http://ccapp-test.marpasoft.com/admin/conference/registration/?q=Trofimchuk")
        element = driver.find_element_by_xpath("//tr[@class='row1']/th/a")
        element.click()
        element = driver.find_element_by_xpath("//div[@class='submit-row']/p[1]/a")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='content']/form[1]/div[2]/input[2]")
        element.click()



    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


