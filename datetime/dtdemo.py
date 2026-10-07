import time, datetime

epocSeconds = time.time()
print(epocSeconds)
t = time.ctime(epocSeconds)
print(t)

dt = datetime.datetime.today()
print(dt)
print("Current date: {}/{}/{}".format(dt.day, dt.month, dt.year))
print("Current time: {}:{}:{}".format(dt.hour, dt.minute, dt.second))