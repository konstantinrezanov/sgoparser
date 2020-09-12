import os.path
from os import system
from dir import getdir
from datetime import datetime

def clean():
    directory=getdir()
    for n in range(0,len(directory)):
        file='./texts/'+directory[n]
        time=datetime.fromtimestamp(os.path.getmtime(file))
        if (datetime.now()-time).days>7:
            system('rm ./texts/'+directory[n])
