from selenium.webdriver.support.ui import Select


def doPersonaInformation(driver):


    element = driver.find_element_by_xpath("//div[@class='wrapit']/h4[1]/a")
    element.click()
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-first_name']/input")
    element.clear()
    element.send_keys("Andrew")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-last_name']/input")
    element.clear()
    element.send_keys("Trofimchuk")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-middle_name']/input")
    element.clear()
    element.send_keys("Nikola")
    element = driver.find_element_by_id('id_personal_info-date_of_birth_month')
    select = Select(element)
    select.select_by_visible_text("July")
    element = driver.find_element_by_id('id_personal_info-date_of_birth_day')
    select = Select(element)
    select.select_by_visible_text("6")
    element = driver.find_element_by_id('id_personal_info-date_of_birth_year')
    select = Select(element)
    select.select_by_visible_text("1978")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-ssn']/input")
    element.clear()
    element.send_keys("2222")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-street']/input")
    element.clear()
    element.send_keys("Golosiivska St.")
    element = driver.find_element_by_id('id_personal_info-state')
    select = Select(element)
    select.select_by_visible_text("California")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-city']/input")
    element.clear()
    element.send_keys("Sacramento")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-zip']/input")
    element.clear()
    element.send_keys("11111")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-phone']/input")
    element.clear()
    element.send_keys("111-111-1111")
    element = driver.find_element_by_xpath("//div[@id='div_id_personal_info-email']/input")
    element.clear()
    element.send_keys("zipppt@gmail.com")
    element = driver.find_element_by_xpath("//div[@class='form_block']/a[1]/span")
    element.click()

