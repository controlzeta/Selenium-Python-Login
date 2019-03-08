from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

usernameStr = 'PCARDENAS'
passwordStr = 'C2SNJXKEW9'

browser = webdriver.Chrome()
browser.get(('http://pruebas.acefianzasmonterrey.com.mx/iConfianzaPruebaUAT/'))
			 
			 
# fill in username and hit the next button
username = browser.find_element_by_id('txtUsuario')
username.send_keys(usernameStr)

contra = browser.find_element_by_id('txtPassword')
contra.send_keys(passwordStr)
contra.send_keys(Keys.RETURN)

btnEmision = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'ulGristerApps_7')))
	
btnEmision.click()