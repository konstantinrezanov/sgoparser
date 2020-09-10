from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from os import system
from time import sleep
import decoupler
  
def get_xlsx(check_title, login, passw):
    driver = webdriver.Chrome('./chromedriver') 
    driver.get("http://sg.lyceum130.ru") 
    driver.find_element_by_xpath('//select/option[text()="МАОУ Лицей №130"]').click()
    driver.find_element_by_name('UN').send_keys(login)
    driver.find_element_by_name('PW').send_keys(passw)
    try:
        driver.find_element_by_name('PW').send_keys(Keys.RETURN)
    except:
        pass
    #driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div[14]/a').click()
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[4]/div/div/div/div/button[2]').click()
    except:
        pass
    print('Logged In')
    title=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/h3').text[5:].split(" ")
    if ("Расписание" in title) and (title!=check_title):
        system('rm *.xlsx && rm ~/Downloads/*.xlsx')
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[1]/div[1]/div[3]/div/div/span/a').click()
        print('Downloading')
        check_title=title
        sleep(1)
        system('mv ~/Downloads/*  ./')
        system('mv *.xlsx init.xlsx')
        f=open('raspa.txt', 'w')
        f.write(decoupler.decouple('10А','D'))
        f.close()
        f=open('raspb.txt', 'w')
        f.write(decoupler.decouple('10Б','E'))
        f.close()
        f=open('raspv.txt', 'w')
        f.write(decoupler.decouple('10В','F'))
        f.close()
        f=open('raspg.txt', 'w')
        f.write(decoupler.decouple('10Г','G'))
        f.close()
        f=open('raspd.txt', 'w')
        f.write(decoupler.decouple('10Д','H'))
        f.close()
    else:
        print('Skipping')
    driver.close()
    return check_title
