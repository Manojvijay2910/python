from queue import Queue
from random import randint
from threading import Thread
from time import sleep

def producer(q):
    i = 0
    while i <= 5:
        print("Producing")
        q.put(randint(1,50))
        print("Produced")
        i += 1
        sleep(3)

def consumer(q):
    i = 0
    while i <= 5:
        print("Consuming")
        print("Consumed data: ", q.get())
        i += 1
        sleep(3)

q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()