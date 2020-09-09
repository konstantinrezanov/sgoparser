from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from os import system
from time import sleep

check_title="init"
  
def get_xlsx(check_title):
    driver = webdriver.Chrome('./chromedriver') 
    driver.get("http://sg.lyceum130.ru") 
    driver.find_element_by_xpath('//select/option[text()="МАОУ Лицей №130"]').click()
    driver.find_element_by_name('UN').send_keys("")
    driver.find_element_by_name('PW').send_keys("")
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div[14]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div/button[2]').click()
    print('Logged In')
    title=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/h3').text[5:].split(" ")
    if ("Расписание" in title) and (title!=check_title):
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/div[3]/div/div/span/a').click()
        print('Downloading')
        check_title=title
        system('mv ~/Downloads/*.xlsx  ~/GitHub/lyceum130parser')
    else:
        print('Skipping')
    sleep(1)
    driver.close()
    return check_title
check_title=get_xlsx(check_title)
print ('Sleeping')
sleep(10)
while True:
    system('rm ~/GitHub/lyceum130parser/*.xlsx')
    check_title=get_xlsx(check_title)
    sleep(10)