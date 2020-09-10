from time import sleep
from parser import get_xlsx
from os import system

check_title='init'
system('rm *.xlsx && rm ~/Downloads/*.xlsx')

check_title=get_xlsx(check_title,YOUR_LOGIN, YOUR_PASSWORD)
print ('Sleeping')
sleep(10)
while True:
    check_title=get_xlsx(check_title,YOUR_LOGIN, YOUR_PASSWORD)
    sleep(10)