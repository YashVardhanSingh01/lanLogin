# make a .env file with two fields
# USERNAME=your_username
# PASSWORD=your_password
# save

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import dotenv_values #comment if hardcoding credentials

config = dotenv_values(".env") #comment if hardcoding credentials

def lan_login():
    driver = webdriver.Chrome()

    driver.get("http://172.16.0.30:8090/")

    username = driver.find_element(by=By.ID, value="username")
    password = driver.find_element(by=By.ID, value="password")
    submit_button = driver.find_element(by=By.ID, value="loginbutton")

    username.send_keys(config['USERNAME'])
    # username.send_keys("your_username") --->use this and comment previous line
    
    password.send_keys(config['PASSWORD'])
    # password.send_keys("your_password") --->use this and comment previous line
    
    submit_button.click()
    
    driver.quit()

lan_login()
