from time import sleep
from parser import get_xlsx
from os import system

check_title='init'
system('rm *.xlsx && rm ~/Downloads/*.xlsx')

check_title=get_xlsx(check_title,open('login.txt', 'r').read(), open('pass.txt', 'r').read())
print ('Sleeping')
sleep(600)
while True:
    check_title=get_xlsx(check_title,open('login.txt', 'r').read(), open('pass.txt', 'r').read())
    sleep(600)