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
    for n in range(1,6):
        try:
            path_to_title='/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[{}]/div[1]/h3'.format(n)
            title=driver.find_element_by_xpath(path_to_title).text[5:].split(" ")
            if ("Расписание" in title) and (title!=check_title):
                system('rm *.xlsx')
                path_to_link='/html/body/div[2]/div[1]/div/div/div/form/div/div/div/div[{}]/div[1]/div[3]/div/div/span/a'.format(n)
                file_title=driver.find_element_by_xpath(path_to_link).text.split(' ')[0]
                driver.find_element_by_xpath(path_to_link).click()
                print('Downloading')
                check_title=title
                sleep(1)
                system('mv ~/Downloads/*.xlsx ~/Downloads/{}.xlsx'.format(file_title))
                system('mv ~/Downloads/*  ./tables')
                #system('touch ./texts/raspА_{0}.txt ./texts/raspБ_{0}.txt ./texts/raspВ_{0}.txt ./texts/raspГ_{0}.txt ./texts/raspД_{0}'.format(file_title))
                f=open('./texts/raspА_{}.txt'.format(file_title), 'w')
                f.write(decoupler.decouple('10А',file_title))
                f.close()
                f=open('./texts/raspБ_{}.txt'.format(file_title), 'w')
                f.write(decoupler.decouple('10Б',file_title))
                f.close()
                f=open('./texts/raspВ_{}.txt'.format(file_title), 'w')
                f.write(decoupler.decouple('10В',file_title))
                f.close()
                f=open('./texts/raspГ_{}.txt'.format(file_title), 'w')
                f.write(decoupler.decouple('10Г',file_title))
                f.close()
                f=open('./texts/raspД_{}.txt'.format(file_title), 'w')
                f.write(decoupler.decouple('10Д',file_title))
                f.close()
                continue
            else:
                print('Skipping')
                continue
        except:
            pass
    driver.close()
    return check_title
