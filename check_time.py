from datetime import datetime
def check_time():
    hour=datetime.now().hour
    if ((hour<14) and (hour>=0)) or (hour>=20):
        return False
    else:
        return True
print(check_time()) 