from time import sleep
from parser import get_xlsx
from os import system
from check_time import check_time
from waiting import wait
from datetime import datetime

while True: #restarts script in the case of an error
    if datetime.now().hour>=16:
        tim=7200
    else:
        tim=600
    check_title='init'
    system('rm *.xlsx && rm ~/Downloads/*.xlsx')

    check_title=get_xlsx(check_title,open('login.txt', 'r').read(), open('pass.txt', 'r').read())
    system('rm ./tables/*.xlsx')
    print ('Sleeping')
    sleep(tim)

    wait(lambda: check_time())

    print('Done waiting')

    while True:
        if datetime.now().hour>=16:
            tim=7200
        else:
            tim=1800
        while check_time():
            check_title=get_xlsx(check_title,open('login.txt', 'r').read(), open('pass.txt', 'r').read())
            sleep(tim)
        wait(lambda: check_time())

        print('Done waiting')