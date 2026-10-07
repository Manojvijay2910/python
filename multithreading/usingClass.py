from threading import Thread, current_thread
from time import sleep

class MyThread():
    def displayNumbers(self):
        i = 0
        print(current_thread().name)
        sleep(1)
        while i <= 10:
            print(i)
            i += 1

obj = MyThread()
t = Thread(target=obj.displayNumbers)
t.start()