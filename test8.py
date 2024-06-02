from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
driver = 'C:\\Users\\V V PRASAD\\Desktop\\bhel'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://dreams.ntpc.co.in/Account/Login?ReturnUrl=%2F")  
username_input = driver.find_element(By.ID,"Email")
password_input = driver.find_element(By.ID,"Password")
username_input.send_keys("1")
password_input.send_keys("1") #actual login crentials are not given for privacy purpose.
time.sleep(15)
login_button = driver.find_element(By.XPATH,'//*[@id="con"]/div/div/div[2]/div[3]/div[2]/form/div[4]')
login_button.click()
time.sleep(5)  
driver.quit()
