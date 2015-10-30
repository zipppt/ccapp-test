import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from shared import doLogin
from shared3 import doPersonaInformation


class CCAPPRADT2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def doLogin(self):
        doLogin(self.driver)
    def doPersonaInformation(self):
        doPersonaInformation(self.driver)


    def test_ccapp_radt2(self):
        driver = self.driver
        driver.get("http://ccapp-test.marpasoft.com/")
        self.assertIn("Welcome", driver.title)


        self.doLogin()

        element = driver.find_element_by_xpath("//div[@class='row menu']/div[@class='col-sm-3'][2]/ul[3]/li[3]/a")
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

        window_parent = driver.current_window_handle
        window_popup = driver.window_handles[-1]
        element = driver.find_element_by_xpath("//div[@class='col-sm-10']/p[8]/a")
        element.click()
        self.driver.implicitly_wait(5)
        driver.switch_to.window(window_popup)

        element = driver.find_element_by_xpath("//div[@id='div_id_course_name']/input")
        element.send_keys("Course name")
        element = driver.find_element_by_xpath("//div[@id='div_id_course_id']/input")
        element.send_keys("Course id")
        element = driver.find_element_by_xpath("//div[@id='div_id_school_name']/input")
        element.send_keys("School name")
        element = self.driver.find_element_by_id('id_academic_content_area')
        select = Select(element)
        select.select_by_visible_text("Physiology and Pharmacology")
        element = driver.find_element_by_xpath("//div[@id='div_id_hours']/input")
        element.clear()
        element.send_keys('45')
        element = self.driver.find_element_by_id('id_grade')
        select = Select(element)
        select.select_by_visible_text("A")
        element = driver.find_element_by_xpath("//div[@id='div_id_completion_date']/input")
        element.send_keys("11/20/14")
        element = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
        element.click()

        driver.switch_to.window(window_parent)
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

