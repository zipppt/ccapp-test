def doLogin(driver):
    element = driver.find_element_by_css_selector('a.btn.btn-primary.log-in')
    element.click()
    username = driver.find_element_by_id('id_username')
    username.send_keys("zipppt@gmail.com")
    password = driver.find_element_by_id('id_password')
    password.send_keys("zipppt2016")
    log = driver.find_element_by_id('submit_button')
    log.click()

