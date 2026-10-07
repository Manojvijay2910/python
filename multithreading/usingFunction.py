from threading import Thread, current_thread


def displayNumbers():
    i = 0
    print(current_thread().name)
    while i <= 10:
        print(i)
        i += 1

print(current_thread().name)
t = Thread(target=displayNumbers)
t.start()