import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://ccapp-test.marpasoft.com/")
        self.assertIn("Welcom", driver.title)
        #ниже две строки для разлогина
        #RADTII = driver.find_element_by_xpath("//div[@id='main-nav']/div[@id='tools-nav']/ul[1]/li[5]/a")
        #RADTII.click()
        CADCI = driver.find_element_by_css_selector('a.btn.btn-primary.log-in')
        CADCI.click()
        username = driver.find_element_by_id('id_username')
        username.send_keys("zipppt@gmail.com")
        password = driver.find_element_by_id('id_password')
        password.send_keys("zipppt2016")
        log = driver.find_element_by_id('submit_button')
        log.click()
        CADCI = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][2]/ul[3]/li[5]/a")
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//div[@class='wrapit']/h4[1]/a")
        CADCI.click()

        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-first_name']/input")
        CADCI.clear()
        CADCI.send_keys("Andrew")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-last_name']/input")
        CADCI.clear()
        CADCI.send_keys("Trofimchuk")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-middle_name']/input")
        CADCI.clear()
        CADCI.send_keys("Nikola")
        element = self.driver.find_element_by_id('id_personal_info-date_of_birth_month')
        select = Select(element)
        select.select_by_visible_text("July")
        element = self.driver.find_element_by_id('id_personal_info-date_of_birth_day')
        select = Select(element)
        select.select_by_visible_text("6")
        element = self.driver.find_element_by_id('id_personal_info-date_of_birth_year')
        select = Select(element)
        select.select_by_visible_text("1978")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-ssn']/input")
        CADCI.clear()
        CADCI.send_keys("2222")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-street']/input")
        CADCI.clear()
        CADCI.send_keys("Golosiivska St.")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-city']/input")
        CADCI.clear()
        CADCI.send_keys("Sacramento")
        element = self.driver.find_element_by_id('id_personal_info-state')
        select = Select(element)
        select.select_by_visible_text("California")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-zip']/input")
        CADCI.clear()
        CADCI.send_keys("11111")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-phone']/input")
        CADCI.clear()
        CADCI.send_keys("111-111-1111")
        CADCI = driver.find_element_by_xpath("//div[@id='div_id_personal_info-email']/input")
        CADCI.clear()
        CADCI.send_keys("zipppt@gmail.com")
        CADCI = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//input[@id='id_agree']")
        #тут два клика захуярил
        CADCI.click()
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//a[@id='submit_button']/span")
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//input[@id='id_agree']")
        CADCI.click()
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//a[@id='submit_button']/span")
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//input[@id='id_education_method_0']")
        CADCI.click()
        CADCI = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
        CADCI.click()




    def tearDown(self):
        # self.driver.close()
        pass



if __name__ == "__main__":
    unittest.main()


