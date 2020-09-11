from time import sleep
from parser import get_xlsx
from os import system
from check_time import check_time
from waiting import wait

while True: #restarts script in the case of an error
    check_title='init'
    system('rm *.xlsx && rm ~/Downloads/*.xlsx')

    check_title=get_xlsx(check_title,open('login.txt', 'r').read(), open('pass.txt', 'r').read())
    print ('Sleeping')
    sleep(600)

    wait(lambda: check_time())

    print('Done waiting')

    while True:
        while check_time():
            check_title=get_xlsx(check_title,open('login.txt', 'r').read(), open('pass.txt', 'r').read())
            sleep(600)
        wait(lambda: check_time())

        print('Done waiting')