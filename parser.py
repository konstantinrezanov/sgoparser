from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from os import system
from time import sleep

chrome_options = Options()
  
def get_xlsx():
    driver = webdriver.Chrome('./chromedriver') 
    driver.get("http://sg.lyceum130.ru") 
    driver.find_element_by_xpath('//select/option[text()="МАОУ Лицей №130"]').click()
    driver.find_element_by_name('UN').send_keys("")
    driver.find_element_by_name('PW').send_keys("")
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div[14]/a').click()
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div/button[2]').click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    title=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/h3').text[5:].split(" ")
    if "Расписание" in title:
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/div[3]/div/div/span/a').click()
    sleep(1)
    driver.close()
    system('mv ~/Downloads/*.xlsx  ~/GitHub/lyceum130parser')

get_xlsx()
sleep(300)
while True:
    system('rm ~/GitHub/lyceum130parser/*.xlsx')
    get_xlsx()
    sleep(300)