import os
from selenium import webdriver
import time
# You need to download the google chrome driver https://sites.google.com/a/chromium.org/chromedriver/
# Put the ChromeDriver & The Bot in a folder.

os.system("cls")
username = input("Username: ")
password = input("Password: ")

driver = webdriver.Chrome()

# The URL your script must visit
time.sleep(2)
driver.get("https://www.instagram.com/")
time.sleep(2)

User_Login = username
user = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
user.click()
time.sleep(1)
user.send_keys(User_Login)

time.sleep(2)

User_Pass = password
passwrd = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
passwrd.click()
time.sleep(1)
passwrd.send_keys(User_Pass)

time.sleep(2)
# login button
driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
time.sleep(4)
# say no to save login.
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
time.sleep(3)
