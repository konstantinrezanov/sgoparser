from datetime import datetime
def check_time():
    hour=datetime.now().hour
    if ((hour<11) and (hour>=0)) or (hour>=22):
        return False
    else:
        return True
print(check_time()) 