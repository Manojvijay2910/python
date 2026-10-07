import threading

print("Current thread: ", threading.current_thread().name)

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Some other thread")