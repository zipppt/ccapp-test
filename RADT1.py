import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared import doLogin
from shared3 import doPersonaInformation


class CCAPPRADT1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def doLogin(self):
        doLogin(self.driver)
    def doPersonaInformation(self):
        doPersonaInformation(self.driver)

    def test_ccapp_radt1(self):
        driver = self.driver
        driver.get("http://ccapp-test.marpasoft.com/")
        self.assertIn("Welcom", driver.title)
        self.doLogin()

        element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][2]/ul[3]/li[2]/a")
        element.click()
        self.doPersonaInformation()


        element = driver.find_element_by_xpath("//input[@id='id_agree']")
        element.click()
        element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
        element.click()
        element = driver.find_element_by_xpath("//input[@id='id_agree']")
        element.click()
        element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
        element.click()
        element = driver.find_element_by_xpath("//div[@id='div_id_registered']/input")
        element.click()
        element = self.driver.find_element_by_id('id_initial_date_month')
        select = Select(element)
        select.select_by_visible_text("July")
        element = self.driver.find_element_by_id('id_initial_date_day')
        select = Select(element)
        select.select_by_visible_text("6")
        element = self.driver.find_element_by_id('id_initial_date_year')
        select = Select(element)
        select.select_by_visible_text("2015")
        element = driver.find_element_by_xpath("//input[@id='id_current_organization_0']")
        element.click()
        element = driver.find_element_by_xpath("//input[@id='id_certified']")
        element.click()
        element = driver.find_element_by_xpath("//input[@id='id_have_ever_revoked_0']")
        element.click()
        element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
        element.click()
        element = driver.find_element_by_xpath("//input[@id='id_type_0']")
        element.click()
        element = driver.find_element_by_xpath("//a[@id='submit_button']/span")
        element.click()

        driver.get("http://ccapp-test.marpasoft.com/admin/profiles/profile/148208/")
        #self.assertIn("Registered Alcohol & Drug Trainee II", driver.page_source)
        element = driver.find_element_by_xpath("//input[@id='id_application_set-0-DELETE']")
        element.click()
        element = driver.find_element_by_xpath("//input[@class='default']")
        element.click()


    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()
