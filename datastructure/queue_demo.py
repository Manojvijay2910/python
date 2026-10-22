import queue

q = queue.Queue()


q.put("python")
q.put("django")
q.put("docker")

print(q.queue)

print(q.qsize())

while not q.empty():
    print(q.get())

print(q.qsize())