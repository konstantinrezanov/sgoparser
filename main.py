from time import sleep
from parser import get_xlsx

check_title='init'
mass=get_xlsx(check_title,YOUR_LOGIN, YOUR_PASSWORD)
check_title=mass[0]
print ('Sleeping')
print(mass[1])
sleep(300)
while True:
    mass=get_xlsx(check_title,YOUR_LOGIN, YOUR_PASSWORD)
    check_title=mass[0]
    print(mass[1])
    sleep(300)
