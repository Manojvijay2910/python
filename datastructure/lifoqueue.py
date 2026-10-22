import queue

lq = queue.LifoQueue()
lq.put("python")
lq.put("django")
lq.put("AWS")
lq.put("flask")

print(lq.queue)
print(lq.qsize())

while not lq.empty():
    print(lq.get())

print(lq.qsize())