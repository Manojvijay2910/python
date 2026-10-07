from threading import Thread, Lock#, Semaphore


class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Lock() # we can also use self.s = Semaphore()

    def buy(self, seatsRequested):
        self.l.acquire()
        if(self.availableSeats >= seatsRequested):
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.availableSeats -= seatsRequested
        else:
            print("Not enough available seats")
        self.l.release()

obj = BookMyBus(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(5,))

t1.start()
t2.start()
t3.start()