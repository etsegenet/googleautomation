#name : etsegenet melese id: ATR/8845/08
from selenium import webdriver
import time
 
driver = webdriver.Firefox(executable_path=r'C:\Users\DarkShadow\Downloads\geckodriver-v0.15.0-win64\geckodriver.exe')
driver.get("https://facebook.com")
email = "email"password = "pass"login="loginbutton"emailelement = driver.find_element_by_name(email)
passwordelement = driver.find_element_by_name(password)
emailelement.send_keys("0920014760")
passwordelement.send_keys("0925256437")
loginelement = driver.find_element_by_id(login)
loginelement.click()
time.sleep(10)
logout1 = driver.find_element_by_css_selector("#userNavigationLabel")
logout1.click()
time.sleep(10)
logout2 = driver.find_element_by_css_selector("._w0d[action='https://www.facebook.com/logout.php']").submit()
