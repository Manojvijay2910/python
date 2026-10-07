from queue import Queue, LifoQueue, PriorityQueue

q = Queue()
q.put(400)
q.put(100)
q.put(500)
q.put(50)
print("FIFO Queue:")
while not q.empty():
    print(q.get(), end = ' ')

lq = LifoQueue()
lq.put(400)
lq.put(100)
lq.put(500)
lq.put(50)
print("\nLIFO Queue:")
while not lq.empty():
    print(lq.get(), end = ' ')

pq = PriorityQueue()
pq.put(400)
pq.put(100)
pq.put(500)
pq.put(50)
print("\nPriority Queue:")
while not pq.empty():
    print(pq.get(), end = ' ')